#!/usr/bin/env python3
"""
Submit senseless.uk URLs to Bing for recrawl (Bing Webmaster URL Submission API).

WHY NOT INDEXNOW: IndexNow proves ownership with a key file hosted at the domain
root, and a key parked anywhere else only authorises URLs under that same prefix
(IndexNow "Option 2" scope rule). Shopify serves no writable root path -- verified
live: /indexnow.txt and /.well-known/indexnow.txt both 404. So self-hosted IndexNow
cannot cover products/collections/blogs on this store, at all. Shopify's own native
IndexNow integration still fires for a narrow subset of product changes; this script
supplements it for everything else.

This uses the JSON/REST endpoint. The "Legacy SOAP and POX APIs retire 31 Aug 2026"
notice does NOT apply -- JSON/REST is the migration target, not a casualty.

Auth: BING_API_KEY, read from the environment or .env. Never printed.

Usage:
    python3 scripts/bing-submit.py --dry-run        # show quota + what would be sent
    python3 scripts/bing-submit.py                  # submit fresh URLs from the sitemap
    python3 scripts/bing-submit.py --all            # ignore the cooldown, submit everything
    python3 scripts/bing-submit.py --urls URL [URL] # submit specific URLs

Exit code is ALWAYS 0 unless --strict is passed, so this can never fail a deploy.
"""
import argparse
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATE_PATH = os.path.join(REPO, ".bing-submit-state.json")
API = "https://ssl.bing.com/webmaster/api.svc/json"
SITE = os.environ.get("BING_SITE_URL", "https://senseless.uk")
SITEMAP = "https://senseless.uk/sitemap.xml"
UA = "senseless-deploy-bot/1.0 (+https://senseless.uk)"

# Child sitemaps to skip: agents.md is text/markdown, not a web page.
SKIP_SITEMAPS = ("sitemap_agentic_discovery",)
# Known-noindex URLs that sit in the sitemap by design. /blogs/guides is structurally
# noindex and must NOT be seo.hidden (that cascades to its articles), so filter here.
SKIP_URLS = {"https://senseless.uk/blogs/guides"}

_SECRETS = []


def redact(s):
    out = s or ""
    for sec in _SECRETS:
        if sec:
            out = out.replace(sec, "***").replace(urllib.parse.quote(sec, safe=""), "***")
    return out


def load_key():
    key = os.environ.get("BING_API_KEY", "").strip()
    if not key:
        envf = os.path.join(REPO, ".env")
        if os.path.exists(envf):
            for ln in open(envf):
                if ln.strip().startswith("BING_API_KEY="):
                    key = ln.split("=", 1)[1].strip().strip('"').strip("'")
                    break
    if key:
        _SECRETS.append(key)
    return key


def http(url, data=None, timeout=20):
    """Returns (status, body). Never raises -- network errors come back as (0, 'ERR ...')."""
    body = json.dumps(data).encode() if data is not None else None
    req = urllib.request.Request(
        url, data=body,
        headers={"Content-Type": "application/json; charset=utf-8", "User-Agent": UA},
    )
    try:
        r = urllib.request.urlopen(req, timeout=timeout)
        return r.status, r.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        try:
            return e.code, e.read().decode("utf-8", "replace")
        except Exception:
            return e.code, ""
    except (urllib.error.URLError, OSError, Exception) as e:  # incl. socket.timeout
        return 0, "ERR %s: %s" % (type(e).__name__, e)


def fetch_text(url, timeout=20):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        return urllib.request.urlopen(req, timeout=timeout).read().decode("utf-8", "replace")
    except Exception:
        return ""


def sitemap_urls(timeout=20):
    """Walk the sitemap index. Child <loc>s are used VERBATIM so Shopify's required
    ?from=&to= params come along and keep working when the id ranges rotate."""
    idx = fetch_text(SITEMAP, timeout)
    if not idx:
        return []
    ns = "{http://www.sitemaps.org/schemas/sitemap/0.9}"
    try:
        root = ET.fromstring(idx)
    except ET.ParseError:
        return []
    children = [e.text.strip() for e in root.iter(ns + "loc") if e.text]
    urls = []
    for child in children:
        if any(s in child for s in SKIP_SITEMAPS):
            continue
        body = fetch_text(child, timeout)
        if not body:
            continue
        try:
            croot = ET.fromstring(body)
        except ET.ParseError:
            continue
        for e in croot.iter(ns + "loc"):
            if e.text:
                u = e.text.strip()
                if u not in SKIP_URLS:
                    urls.append(u)
    # de-dupe, preserve order
    seen, out = set(), []
    for u in urls:
        if u not in seen:
            seen.add(u)
            out.append(u)
    return out


def load_state():
    try:
        return json.load(open(STATE_PATH))
    except Exception:
        return {}


def save_state(st):
    try:
        json.dump(st, open(STATE_PATH, "w"), indent=1)
    except Exception as e:
        print("  bing-submit: could not write state (%s)" % type(e).__name__)


def get_quota(key, timeout=20):
    url = "%s/GetUrlSubmissionQuota?%s" % (
        API, urllib.parse.urlencode({"apikey": key, "siteUrl": SITE}))
    status, body = http(url, timeout=timeout)
    if status != 200:
        return None, None, "HTTP %s %s" % (status, redact(body)[:160])
    try:
        d = json.loads(body)["d"]
        return d.get("DailyQuota"), d.get("MonthlyQuota"), None
    except Exception:
        return None, None, "unparsable quota response"


def submit(key, urls, timeout=30):
    payload = {"siteUrl": SITE, "urlList": urls}
    # Microsoft renders the JSON method name both ways; try the documented JSON
    # casing first and fall through on anything that is NOT an auth failure.
    last = ""
    for method in ("SubmitUrlbatch", "SubmitUrlBatch"):
        url = "%s/%s?%s" % (API, method, urllib.parse.urlencode({"apikey": key}))
        status, body = http(url, data=payload, timeout=timeout)
        if status == 200:
            return True, method, body
        last = "HTTP %s %s" % (status, redact(body)[:200])
        if "invalidapikey" in (body or "").lower() or status in (401, 403):
            return False, method, last          # real auth failure -- do not retry
    return False, None, last


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true", help="fetch quota + list URLs; submit nothing")
    ap.add_argument("--all", action="store_true", help="ignore the per-URL cooldown")
    ap.add_argument("--urls", nargs="*", help="submit these URLs instead of the sitemap")
    ap.add_argument("--changed", nargs="*", help="deployed file paths; logged for context only")
    ap.add_argument("--cooldown-hours", type=float, default=6.0)
    ap.add_argument("--timeout", type=int, default=20)
    ap.add_argument("--strict", action="store_true", help="exit non-zero on failure (never use from deploy.sh)")
    a = ap.parse_args()

    fail = lambda msg: (print("  bing-submit: %s" % msg), sys.exit(1 if a.strict else 0))

    key = load_key()
    if not key:
        return fail("BING_API_KEY not set -- skipping (this is not an error).")

    if a.changed:
        print("  bing-submit: deploy touched %d file(s)" % len(a.changed))

    urls = a.urls if a.urls else sitemap_urls(a.timeout)
    if not urls:
        return fail("no URLs resolved from the sitemap -- skipping.")

    now = time.time()
    state = load_state()
    seen = state.get("submitted", {})
    if a.all or a.urls:
        fresh = urls
    else:
        cd = a.cooldown_hours * 3600
        fresh = [u for u in urls if now - seen.get(u, 0) > cd]
    if not fresh:
        print("  bing-submit: all %d URLs submitted within the last %.0fh -- nothing to do."
              % (len(urls), a.cooldown_hours))
        return

    daily, monthly, err = get_quota(key, a.timeout)
    if err:
        print("  bing-submit: quota unreadable (%s) -- using a conservative cap." % err)
        cap = 10
    else:
        print("  bing-submit: quota daily=%s monthly=%s" % (daily, monthly))
        cap = min(x for x in (daily, monthly, 500) if isinstance(x, int) and x > 0)

    batch = fresh[:cap]
    if len(fresh) > len(batch):
        print("  bing-submit: %d fresh URLs, submitting %d (quota cap); the rest go next run."
              % (len(fresh), len(batch)))

    if a.dry_run:
        print("  bing-submit: DRY RUN -- would submit %d URL(s):" % len(batch))
        for u in batch:
            print("     %s" % u)
        return

    ok, method, info = submit(key, batch, max(a.timeout, 30))
    if ok:
        print("  bing-submit: submitted %d URL(s) via %s" % (len(batch), method))
        for u in batch:
            seen[u] = now
        state["submitted"] = seen
        save_state(state)
    else:
        return fail("submission failed -- %s" % info)


if __name__ == "__main__":
    main()
