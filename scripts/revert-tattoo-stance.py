#!/usr/bin/env python3
"""REVERSAL RUNBOOK — undo the tattoo/piercing stance shipped 2026-08-14.

Written on the day it shipped, while every ID and every reason was still in hand. If the stance
has to come off — the safety assessor comes back with a narrower CPSR scope, the MHRA or ASA take
an interest, or it simply does not work commercially — this is the one command that does it.

    python3 scripts/revert-tattoo-stance.py                    # dry run, shows every action
    python3 scripts/revert-tattoo-stance.py --apply            # unpublish (default, reversible)
    python3 scripts/revert-tattoo-stance.py --apply --hard     # also delete the collections

DEFAULT IS UNPUBLISH, NOT DELETE. Unpublishing takes the surfaces off the internet in seconds and
keeps every URL, template and body of copy recoverable. Deleting a collection loses its handle,
its rules and its SEO fields. Only pass --hard if someone has decided the URLs must not exist.

--------------------------------------------------------------------------------------------
WHAT IS TATTOO-DEPENDENT (this script's scope)
--------------------------------------------------------------------------------------------
  Shopify
    collection  numbing-cream-for-tattoos       gid://shopify/Collection/695670669660   16 products
    collection  numbing-cream-for-piercings     gid://shopify/Collection/695670702428   16 products
    collection  tattoo-aftercare                gid://shopify/Collection/695670735196    2 products
    7 articles in the `guides` blog (ids in ARTICLES below)
    16 products carrying "Tattooing" + "Piercing" in senseless.recommended_procedures

  Theme (needs a deploy after reverting — see the printed instructions)
    templates/collection.numbing-cream-for-tattoos.json
    templates/collection.numbing-cream-for-piercings.json
    templates/collection.tattoo-aftercare.json
    templates/page.how-to-apply-numbing-cream.json   <- step s6, FAQ q8, the Tattooing row

  Notion
    Decision       3bb58bc3-75ea-81b2-9c32-c0e2d8b577e0  -> set Status = Superseded, add a reversal row
    ComplianceHold 3bb58bc3-75ea-8147-ad45-e77a97ac8ddc  -> re-open, Status = Applied
    State Surface  38e58bc3-75ea-81ad-87eb-e20fcfc22406  -> new log entry (append, never overwrite)

--------------------------------------------------------------------------------------------
WHAT IS *NOT* TATTOO-DEPENDENT — leave all of it alone
--------------------------------------------------------------------------------------------
Most of what shipped on 14 Aug survives a full reversal, because it was never about tattooing:

  /pages/delivery                  targets "numbing cream next day delivery"; no tattoo word on it
  /pages/tktx-numbing-cream-uk     a buyer's checklist; TKTX is the category incumbent, not a
                                   tattoo brand, and the page makes no tattoo claim
  sections/senseless-spec-table    generic; used by both pages above
  the sitewide @id-linked @graph   pure entity/schema work
  the Offer.shippingDetails fix    removed an unpublished £1.99 rate and a 4-6 day transit that
                                   contradicted the live next-day offer. NEVER restore those.
  FAQ heading levels, <time datetime>, dateModified, ItemList.item
  every A10 doc fix                they corrected things that were factually wrong regardless
  all four new scripts

Reverting the stance therefore costs 3 collections, 7 articles, one metafield value on 16
products and 3 blocks on one page. It does not cost the GEO work, the delivery page or the
tooling. That asymmetry was deliberate.

--------------------------------------------------------------------------------------------
WHAT THIS SCRIPT DOES NOT AND CANNOT DO
--------------------------------------------------------------------------------------------
  * It cannot un-index. Google and Bing already have these URLs — deploy.sh submitted them to
    Bing on 14 Aug. After reverting, unpublished collections 404 and articles 404; that is the
    correct signal, but expect them to sit in SERPs for days to weeks. If speed matters, use
    Search Console's Removals tool and Bing's equivalent.
  * It does not touch the compliance-locked safety warnings. Those never changed.
  * It does not restore the Foaming Cleanser's "For use on unbroken skin" line. That line was
    removed because it contradicted the product's own safety block, which is true whatever
    happens to the tattoo stance. Restoring it would re-create a live contradiction.
  * It does not revert the A10 canon corrections. `docs/AUDIT-2026-06-12.md` items 10/P3.5 closed
    on the G5 owner ruling ("both target the same customer base"). If THAT ruling is also
    reversed, re-open them by hand — but note it is a separate decision from the CPSR question.
"""
import argparse
import json
import os
import sys
import urllib.error
import urllib.request

STORE = "senseless-numbing.myshopify.com"
BASE = f"https://{STORE}/admin/api/2024-10"
BLOG_ID = 127881740636

COLLECTIONS = [
    ("numbing-cream-for-tattoos", "gid://shopify/Collection/695670669660"),
    ("numbing-cream-for-piercings", "gid://shopify/Collection/695670702428"),
    ("tattoo-aftercare", "gid://shopify/Collection/695670735196"),
]

ARTICLES = [
    ("does-numbing-cream-affect-a-tattoo", 1007440560476),
    ("can-you-use-numbing-cream-before-a-tattoo", 1007440593244),
    ("do-tattoo-artists-use-numbing-cream", 1007440626012),
    ("what-to-tell-your-artist-about-numbing-cream", 1007440658780),
    ("where-to-buy-numbing-cream-for-tattoos-uk", 1007440691548),
    ("tattoo-aftercare-first-48-hours", 1007440724316),
    ("tattoo-healing-stages-day-by-day", 1007440757084),
]

REMOVE_PROCEDURES = {"Tattooing", "Piercing"}


def rest(path, payload=None, method=None):
    token = os.environ["SHOPIFY_ACCESS_TOKEN"]
    data = json.dumps(payload).encode() if payload is not None else None
    req = urllib.request.Request(
        f"{BASE}{path}", data=data, method=method or ("POST" if data else "GET"),
        headers={"X-Shopify-Access-Token": token, "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=60) as fh:
            return json.loads(fh.read() or "{}")
    except urllib.error.HTTPError as exc:
        sys.exit(f"HTTP {exc.code} {method or 'GET'} {path}\n{exc.read().decode()[:1500]}")


def gql(query, variables=None):
    token = os.environ["SHOPIFY_ACCESS_TOKEN"]
    body = json.dumps({"query": query, "variables": variables or {}}).encode()
    req = urllib.request.Request(
        f"{BASE}/graphql.json", data=body, method="POST",
        headers={"X-Shopify-Access-Token": token, "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as fh:
        out = json.loads(fh.read())
    if out.get("errors"):
        sys.exit(f"GraphQL errors: {json.dumps(out['errors'], indent=2)}")
    return out["data"]


def verify_store():
    shop = rest("/shop.json")["shop"]
    if shop["myshopify_domain"] != STORE:
        sys.exit(f"STORE GATE FAILED: {shop['myshopify_domain']} != {STORE}")
    print(f"store gate PASS — {shop['myshopify_domain']} ({shop['name']})\n")


def online_store_publication():
    for edge in gql("{ publications(first: 20) { edges { node { id name } } } }")["publications"]["edges"]:
        if edge["node"]["name"] == "Online Store":
            return edge["node"]["id"]
    sys.exit("could not find the Online Store publication")


def revert_collections(apply_changes, hard):
    print("== collections ==")
    pub = online_store_publication()
    for handle, gid in COLLECTIONS:
        if hard:
            print(f"  DELETE  /collections/{handle}  ({gid})")
            if apply_changes:
                res = gql("mutation D($input: CollectionDeleteInput!){ collectionDelete(input:$input)"
                          "{ deletedCollectionId userErrors{ field message } } }",
                          {"input": {"id": gid}})["collectionDelete"]
                if res["userErrors"]:
                    sys.exit(f"collectionDelete errors: {res['userErrors']}")
                print(f"      deleted {res['deletedCollectionId']}")
        else:
            print(f"  UNPUBLISH  /collections/{handle}  ({gid})")
            if apply_changes:
                res = gql("mutation U($id: ID!, $input: [PublicationInput!]!){ publishableUnpublish"
                          "(id:$id, input:$input){ userErrors{ field message } } }",
                          {"id": gid, "input": [{"publicationId": pub}]})["publishableUnpublish"]
                if res["userErrors"]:
                    sys.exit(f"publishableUnpublish errors: {res['userErrors']}")
                print("      unpublished from Online Store (URL now 404s)")


def revert_articles(apply_changes):
    print("\n== articles ==")
    for handle, aid in ARTICLES:
        print(f"  UNPUBLISH  /blogs/guides/{handle}  (id {aid})")
        if apply_changes:
            rest(f"/articles/{aid}.json",
                 {"article": {"id": aid, "published": False}}, method="PUT")
            print("      unpublished (URL now 404s; body and metafields retained)")


def revert_metafields(apply_changes):
    """Read-modify-write, exactly as the forward pass did. Removing the two values must not
    disturb the procedures that were there before 14 Aug."""
    print("\n== product procedure metafields ==")
    edges = gql('query { products(first: 50) { edges { node { id handle '
                'metafield(namespace: "senseless", key: "recommended_procedures") '
                '{ value compareDigest } } } } }')["products"]["edges"]
    payload = []
    for edge in edges:
        node = edge["node"]
        mf = node.get("metafield")
        if not mf or not mf["value"]:
            continue
        existing = json.loads(mf["value"])
        kept = [p for p in existing if p not in REMOVE_PROCEDURES]
        if kept == existing:
            continue
        removed = [p for p in existing if p in REMOVE_PROCEDURES]
        print(f"  {node['handle']:34} {len(existing)} -> {len(kept)}  removing {removed}"
              + ("   (field becomes EMPTY — it had none before 14 Aug)" if not kept else ""))
        entry = {"ownerId": node["id"], "namespace": "senseless",
                 "key": "recommended_procedures", "type": "list.single_line_text_field",
                 "value": json.dumps(kept, ensure_ascii=False)}
        if mf.get("compareDigest"):
            entry["compareDigest"] = mf["compareDigest"]
        payload.append(entry)
    if not payload:
        print("  nothing to change")
        return
    print(f"  -> {len(payload)} product(s)")
    if not apply_changes:
        return
    for i in range(0, len(payload), 25):
        res = gql("mutation S($metafields: [MetafieldsSetInput!]!){ metafieldsSet(metafields:$metafields)"
                  "{ metafields{ key } userErrors{ field message } } }",
                  {"metafields": payload[i:i + 25]})["metafieldsSet"]
        if res["userErrors"]:
            sys.exit(f"metafieldsSet errors: {json.dumps(res['userErrors'], indent=2)}")
        print(f"  wrote {len(res['metafields'])} metafield(s)")


MANUAL = """
================================================================================
STILL TO DO BY HAND — this script only touched Shopify
================================================================================

1. THEME. Revert the tattoo additions to the how-to-apply page and remove the three collection
   templates, then deploy:

       git revert --no-commit <the commits>   # or edit directly:
       #   templates/page.how-to-apply-numbing-cream.json
       #     - delete block s6 from sections.creamgel.blocks and from block_order
       #     - delete block q8 from sections.faq.blocks and from block_order
       #     - delete the "<strong>Tattooing.</strong> ..." paragraph from
       #       sections.procedures.settings.body
       #     - restore sections.creamgel.settings.headline to "Five steps."
       #   git rm templates/collection.numbing-cream-for-{tattoos,piercings}.json
       #   git rm templates/collection.tattoo-aftercare.json

       shopify theme check --fail-level error         # must be 0 errors
       git add -A && git commit && git push            # COMMIT BEFORE DEPLOY
       bash -c './scripts/deploy.sh templates/page.how-to-apply-numbing-cream.json'

   Deleting a template file does NOT remove it from the live theme — deploy.sh only pushes what
   you name. Remove the three collection templates from the live theme through the theme editor
   or leave them; with no collection at those handles they render nowhere.

2. RE-RUN THE INVARIANT. Unpublishing removes ad-facing surfaces, so the baseline moves:

       python3 scripts/injectable-clean-sweep.py       # expect 0 breaches, ~43 surfaces

3. NOTION.
   - Decision  3bb58bc3-75ea-81b2-9c32-c0e2d8b577e0  -> Status = Superseded, and create a new
     row recording WHY it was reversed and by whom. Do not edit the original's Decision text:
     it is the record of what was believed on 14 Aug.
   - Hold      3bb58bc3-75ea-8147-ad45-e77a97ac8ddc  -> Status = Applied, Cleared-by cleared.
   - State Surface 38e58bc3-75ea-81ad-87eb-e20fcfc22406 -> APPEND a log entry. The Sync-status
     block is prepend-only; never overwrite it.
   - canon/state.json -> update sync_status to match, so reconcile.sh reports the truth.

4. SEARCH ENGINES. Unpublished URLs 404, which is the correct signal, but they will sit in SERPs
   for days to weeks. If that matters, use Search Console Removals and the Bing equivalent.

5. WHAT NOT TO TOUCH. /pages/delivery, /pages/tktx-numbing-cream-uk, the spec-table section, the
   entity graph, the shippingDetails correction, the A10 doc fixes and all four scripts are not
   tattoo-dependent. Reverting them would undo work that is correct either way — and restoring
   the old £1.99 / 4-6 day shipping claim would re-create a CPUT 2008 problem.
"""


def main():
    ap = argparse.ArgumentParser(description="Revert the 2026-08-14 tattoo/piercing stance.")
    ap.add_argument("--apply", action="store_true", help="actually write (default is a dry run)")
    ap.add_argument("--hard", action="store_true",
                    help="DELETE the collections instead of unpublishing them. Loses handles, "
                         "rules and SEO fields. Only with an explicit decision.")
    args = ap.parse_args()
    if "SHOPIFY_ACCESS_TOKEN" not in os.environ:
        sys.exit("SHOPIFY_ACCESS_TOKEN not set. Run ./scripts/refresh-token.sh then `source .env`.")

    verify_store()
    if args.hard:
        print("*** --hard: collections will be DELETED, not unpublished. Handles, rules and SEO")
        print("*** fields are lost. Ctrl-C now unless that is the decision that was taken.\n")
    if not args.apply:
        print("DRY RUN — nothing will be written. Re-run with --apply.\n")

    revert_collections(args.apply, args.hard)
    revert_articles(args.apply)
    revert_metafields(args.apply)
    print(MANUAL)
    print("done." if args.apply else "dry run complete — no writes made.")


if __name__ == "__main__":
    main()
