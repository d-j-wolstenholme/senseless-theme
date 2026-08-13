#!/usr/bin/env python3
"""Publish (or re-publish) guide articles from a JSON content file — idempotently.

Why this exists rather than reusing scripts/build-articles.py: that script is a one-shot
POST-only create. It has no existence check and no update path, so running it again re-POSTs
the original five articles as duplicates. It also carries stale copy — four of its five live
meta descriptions have since been edited in the admin, and five Hard-Rule breaches recorded in
docs/SITE-ASSESSMENT-2026-08-06.md still sit in its article bodies. Leave it alone; use this.

This script:
  * verifies the store BEFORE any write (the CLI/MCP default account is Totally Numb),
  * matches existing articles by handle and UPDATES them in place, creating only what is absent,
  * updates metafields by (namespace, key) rather than appending duplicates,
  * is dry-run by default. Nothing is written without --apply.

Usage:
  python3 scripts/publish-articles.py docs/tattoo-cluster-content.json            # dry run
  python3 scripts/publish-articles.py docs/tattoo-cluster-content.json --apply    # write
  python3 scripts/publish-articles.py <file> --apply --only handle-a,handle-b     # subset

Requires SHOPIFY_ACCESS_TOKEN (run ./scripts/refresh-token.sh, then source .env).
"""
import argparse
import json
import os
import sys
import urllib.error
import urllib.request

STORE = "senseless-numbing.myshopify.com"
BASE = f"https://{STORE}/admin/api/2024-10"
BLOG_ID = 127881740636  # the `guides` blog — the only blog on the store
TEMPLATE_SUFFIX = "guides"
AUTHOR = "Senseless"


def api(path, payload=None, method=None):
    token = os.environ.get("SHOPIFY_ACCESS_TOKEN")
    if not token:
        sys.exit("SHOPIFY_ACCESS_TOKEN is not set. Run ./scripts/refresh-token.sh then `source .env`.")
    data = json.dumps(payload).encode() if payload is not None else None
    req = urllib.request.Request(
        f"{BASE}{path}", data=data, method=method or ("POST" if data else "GET"),
        headers={"X-Shopify-Access-Token": token, "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=60) as fh:
            return json.loads(fh.read() or "{}")
    except urllib.error.HTTPError as exc:
        sys.exit(f"HTTP {exc.code} on {method or 'GET'} {path}\n{exc.read().decode()[:2000]}")


def verify_store():
    """The store gate. Never optional — the CLI/MCP default account is Totally Numb."""
    shop = api("/shop.json")["shop"]
    if shop["myshopify_domain"] != STORE:
        sys.exit(f"STORE GATE FAILED: {shop['myshopify_domain']} != {STORE}. Stopping.")
    print(f"store gate PASS — {shop['myshopify_domain']} ({shop['name']})")


def existing_articles():
    out = {}
    for art in api(f"/blogs/{BLOG_ID}/articles.json?limit=250&fields=id,handle,title")["articles"]:
        out[art["handle"]] = art["id"]
    return out


def sync_metafields(article_id, wanted, apply_changes):
    """Update metafields by (namespace, key). A bare create on an existing key duplicates it."""
    current = {(m["namespace"], m["key"]): m
               for m in api(f"/articles/{article_id}/metafields.json")["metafields"]}
    for ns, key, mtype, value in wanted:
        found = current.get((ns, key))
        if found:
            if found.get("value") == value:
                print(f"      metafield {ns}.{key}: unchanged")
                continue
            print(f"      metafield {ns}.{key}: UPDATE")
            if apply_changes:
                api(f"/metafields/{found['id']}.json",
                    {"metafield": {"id": found["id"], "type": mtype, "value": value}}, method="PUT")
        else:
            print(f"      metafield {ns}.{key}: CREATE")
            if apply_changes:
                api(f"/articles/{article_id}/metafields.json",
                    {"metafield": {"namespace": ns, "key": key, "type": mtype, "value": value}})


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("content", help="JSON file with an `articles` array")
    ap.add_argument("--apply", action="store_true", help="actually write (default is a dry run)")
    ap.add_argument("--only", help="comma-separated handles to restrict the run to")
    args = ap.parse_args()

    with open(args.content, encoding="utf-8") as fh:
        articles = json.load(fh)["articles"]
    if args.only:
        keep = {h.strip() for h in args.only.split(",")}
        articles = [a for a in articles if a["handle"] in keep]
        missing = keep - {a["handle"] for a in articles}
        if missing:
            sys.exit(f"--only names handles not in {args.content}: {sorted(missing)}")

    verify_store()
    if not args.apply:
        print("DRY RUN — nothing will be written. Re-run with --apply.\n")

    live = existing_articles()
    print(f"{len(live)} articles already in blog {BLOG_ID}\n")

    for art in articles:
        handle = art["handle"]
        body = {
            "title": art["title"],
            "handle": handle,
            "author": AUTHOR,
            "body_html": art["body"],
            "summary_html": "<p>" + art["summary"] + "</p>",
            "published": True,
            "template_suffix": TEMPLATE_SUFFIX,
        }
        meta = [
            ("global", "title_tag", "single_line_text_field", art["mt"]),
            ("global", "description_tag", "single_line_text_field", art["md"]),
            ("custom", "faq", "json", json.dumps(art["faq"], ensure_ascii=False)),
        ]

        if handle in live:
            article_id = live[handle]
            print(f"  UPDATE {handle} (id {article_id})")
            if args.apply:
                api(f"/articles/{article_id}.json", {"article": dict(body, id=article_id)}, method="PUT")
        else:
            print(f"  CREATE {handle}")
            if args.apply:
                article_id = api(f"/blogs/{BLOG_ID}/articles.json", {"article": body})["article"]["id"]
                print(f"      created id {article_id}")
            else:
                print("      (dry run — metafield sync skipped, article does not exist yet)")
                continue
        sync_metafields(article_id, meta, args.apply)

    print("\ndone." if args.apply else "\ndry run complete — no writes made.")


if __name__ == "__main__":
    main()
