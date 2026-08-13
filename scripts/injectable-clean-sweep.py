#!/usr/bin/env python3
"""Injectable-clean sweep — enforces .claude/rules/ad-facing.md against the LIVE site.

The three injectable collections are organic-only. No ad-facing surface may link them.
This script fetches every URL in sitemap.xml (plus the ad-facing URLs that are
deliberately absent from it), strips <script> blocks, and counts anchors to the three
handles. Ad-facing hits are BREACHES; organic hits (blogs + the does-it-hurt / procedure
guide cluster + the three collections cross-linking each other) are expected.

Usage:  python3 scripts/injectable-clean-sweep.py [--json out.json]
Exit 0 = 0 breaches. Exit 1 = at least one breach.
"""
import argparse
import gzip
import json
import re
import sys
import urllib.request
from concurrent.futures import ThreadPoolExecutor

BASE = "https://senseless.uk"
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36")

PROTECTED = [
    "numbing-cream-for-injections",
    "numbing-cream-for-lip-fillers",
    "numbing-cream-for-botox",
]

# The named ad-facing surfaces from .claude/rules/ad-facing.md. Everything else in the
# sitemap that is not one of these and not a blog/guide is classified by path.
AD_FACING_EXTRA = [
    "/pages/strongest-numbing-cream",
    "/pages/senseless-vs-ametop",
    "/pages/best-emla-alternative-uk",
    "/pages/aesthetic-procedures",
    "/pages/the-senseless-system",
]

# Organic surfaces that MAY link the three (rule: blogs + the does-it-hurt / procedure
# explainer guide cluster + the three collections themselves).
ORGANIC_PAGES = {
    "/pages/does-it-hurt",
    "/pages/does-it-hurt-by-treatment",
    "/pages/does-microneedling-hurt",
    "/pages/does-laser-hair-removal-hurt",
    "/pages/does-numbing-cream-work",
    "/pages/how-long-numbing-cream-lasts",
    "/pages/how-to-apply-numbing-cream",
    "/pages/using-numbing-cream",
    "/pages/articles",
    "/pages/faq",
}

SCRIPT_RE = re.compile(r"<script\b.*?</script>", re.S | re.I)
NOSCRIPT_RE = re.compile(r"<noscript\b.*?</noscript>", re.S | re.I)
HREF_RE = re.compile(r"""<a\b[^>]*?href\s*=\s*["']([^"']+)["']""", re.I)
LOC_RE = re.compile(r"<loc>(.*?)</loc>")


def fetch(url, timeout=45):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=timeout) as fh:
        raw = fh.read()
    if raw[:2] == b"\x1f\x8b":
        raw = gzip.decompress(raw)
    return raw.decode("utf-8", "replace")


def sitemap_urls():
    root = fetch(f"{BASE}/sitemap.xml")
    urls = []
    for child in LOC_RE.findall(root):
        child = child.replace("&amp;", "&")
        try:
            urls += [u.replace("&amp;", "&") for u in LOC_RE.findall(fetch(child))]
        except Exception as exc:  # pragma: no cover - network
            print(f"  ! child sitemap failed {child}: {exc}", file=sys.stderr)
    return sorted(set(urls))


def classify(path):
    """ad | organic — per .claude/rules/ad-facing.md."""
    if path.startswith("/blogs/"):
        return "organic"
    if path in ORGANIC_PAGES:
        return "organic"
    if any(path == f"/collections/{h}" for h in PROTECTED):
        return "organic"  # the cluster cross-linking itself is the cluster, not a surface
    if path in AD_FACING_EXTRA:
        return "ad"
    if path.startswith("/collections/") or path.startswith("/products/") or path == "/":
        return "ad"
    return "ad"  # default-deny: an unclassified surface is treated as ad-facing


def scan(url):
    path = url.split(BASE, 1)[-1].split("?", 1)[0].rstrip("/") or "/"
    try:
        html = fetch(url + ("&" if "?" in url else "?") + "_fd=0")
    except Exception as exc:  # pragma: no cover - network
        return {"path": path, "error": str(exc), "hits": {}, "kind": classify(path)}
    body = NOSCRIPT_RE.sub("", SCRIPT_RE.sub("", html))
    hits = {}
    for href in HREF_RE.findall(body):
        for handle in PROTECTED:
            if f"/collections/{handle}" in href:
                hits[handle] = hits.get(handle, 0) + 1
    return {"path": path, "hits": hits, "kind": classify(path), "bytes": len(html)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", help="write the full result set here")
    args = ap.parse_args()

    urls = sitemap_urls()
    extra = [BASE + p for p in AD_FACING_EXTRA if BASE + p not in urls]
    urls = urls + extra
    print(f"sweep: {len(urls)} URLs ({len(extra)} added outside the sitemap)")

    with ThreadPoolExecutor(max_workers=6) as pool:
        results = list(pool.map(scan, urls))

    breaches = [r for r in results if r["kind"] == "ad" and r["hits"]]
    organic_hits = [r for r in results if r["kind"] == "organic" and r["hits"]]
    errors = [r for r in results if r.get("error")]
    ad_count = sum(1 for r in results if r["kind"] == "ad")

    print(f"ad-facing surfaces scanned: {ad_count}")
    print(f"organic surfaces scanned:   {len(results) - ad_count}")
    for r in organic_hits:
        print(f"  organic (allowed) {r['path']}: {r['hits']}")
    for r in errors:
        print(f"  ! ERROR {r['path']}: {r['error']}")
    print(f"BREACHES: {len(breaches)}")
    for r in breaches:
        print(f"  BREACH {r['path']}: {r['hits']}")

    if args.json:
        with open(args.json, "w") as fh:
            json.dump({"breaches": breaches, "organic_hits": organic_hits,
                       "errors": errors, "results": results}, fh, indent=2)
        print(f"wrote {args.json}")

    return 1 if breaches or errors else 0


if __name__ == "__main__":
    sys.exit(main())
