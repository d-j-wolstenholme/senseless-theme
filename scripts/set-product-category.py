#!/usr/bin/env python3
"""Give every Senseless product in the Google feed a Shopify standard category, and fix the kits' brand.

Why: the Google & YouTube channel sends Shopify's standard product category to Merchant Center as
google_product_category, and the vendor as brand. On 26 Sep 2026 no product had a category (null on
the singles, "Uncategorized" on the kits), so Google guessed one itself: the 3 gels got NO category
at all, the creams "Skin Care > Lotion & Moisturizer", the sprays only "Health & Beauty > Personal
Care". The 5 kits showed brand "senseless-numbing" (their vendor) instead of "Senseless" (audit N18,
docs/GOOGLE-ADS-MC-AUDIT-2026-09-20.md).

Category choice: "Health & Beauty > Personal Care > Cosmetics > Skin Care" (hb-3-2-9) for the
creams, gels, sprays and the cleanser: they are cosmetics (MHRA classification closed as cosmetic),
and no narrower leaf is accurate ("Lotions & Moisturizers" is not what they are). The kits get
"Skin Care > Skin Care Kits & Sets" (hb-3-2-9-25). Not touched: Vitamin A&D 4-pack, the Cosmetics
Bag and the Build-your-own helper (none is in the Google & YouTube feed).

Safety: a category is only written where it is empty or "Uncategorized"; a vendor only where it is
"senseless-numbing". Anything else stops the run before writing.

Usage (from the repo root, after ./scripts/refresh-token.sh):
  python3 scripts/set-product-category.py           # dry run: prints the plan, writes nothing
  python3 scripts/set-product-category.py --apply   # writes, then reads every product back
"""
import json
import os
import re
import sys
import urllib.request

STORE = "senseless-numbing.myshopify.com"
URL = f"https://{STORE}/admin/api/2025-07/graphql.json"
TAX = "gid://shopify/TaxonomyCategory/"
SKIN_CARE, KITS = TAX + "hb-3-2-9", TAX + "hb-3-2-9-25"
EMPTY_CATEGORIES = (None, TAX + "na")
OLD_VENDOR, VENDOR = "senseless-numbing", "Senseless"

# handle -> category
PLAN = {h: SKIN_CARE for h in (
    "clinical-strength-cream", "advanced-strength-cream", "professional-strength-cream",
    "clinical-strength-gel", "advanced-strength-gel", "professional-strength-gel",
    "clinical-strength-spray", "advanced-strength-spray", "professional-strength-spray",
    "foaming-cleanser",
)}
PLAN.update({h: KITS for h in (
    "clinical-numbing-kit-small", "clinical-numbing-kit-large",
    "advanced-numbing-kit-small", "advanced-numbing-kit-large", "professional-numbing-kit-large",
)})


def load_env():
    for line in open(".env"):
        m = re.match(r"^([A-Z_]+)=(.*)$", line.strip())
        if m:
            os.environ.setdefault(m.group(1), m.group(2).strip().strip('"').strip("'"))


def gql(query, variables=None):
    req = urllib.request.Request(
        URL,
        data=json.dumps({"query": query, "variables": variables or {}}).encode(),
        headers={"X-Shopify-Access-Token": os.environ["SHOPIFY_ACCESS_TOKEN"], "Content-Type": "application/json"},
    )
    out = json.load(urllib.request.urlopen(req, timeout=60))
    if out.get("errors"):
        sys.exit(f"GraphQL errors: {out['errors']}")
    return out["data"]


def main():
    apply = "--apply" in sys.argv
    load_env()
    shop = gql("{ shop { myshopifyDomain } }")["shop"]["myshopifyDomain"]
    if shop != STORE:
        sys.exit(f"STOP: store gate failed ({shop} != {STORE})")
    print(f"store gate: {shop}")

    names = {c: gql("query($id: ID!) { node(id: $id) { ... on TaxonomyCategory { fullName } } }", {"id": c})["node"]
             for c in set(PLAN.values())}
    if not all(names.values()):
        sys.exit(f"STOP: a planned category does not exist in Shopify's taxonomy: {names}")

    products = gql("{ products(first: 100) { nodes { id handle vendor category { id } } } }")["products"]["nodes"]
    writes, problems, found = [], [], set()
    for p in products:
        if p["handle"] not in PLAN:
            continue
        found.add(p["handle"])
        want = PLAN[p["handle"]]
        cur = (p["category"] or {}).get("id")
        change = {}
        if cur != want:
            if cur in EMPTY_CATEGORIES:
                change["category"] = want
            else:
                problems.append(f"{p['handle']}: category is {cur}, not empty/Uncategorized")
        if p["vendor"] == OLD_VENDOR:
            change["vendor"] = VENDOR
        elif p["vendor"] != VENDOR:
            problems.append(f"{p['handle']}: vendor is {p['vendor']!r}")
        if change:
            writes.append((p, change))
            print(f"  WRITE     {p['handle']:31} category {cur or '(none)'} -> {names[want]['fullName'].split(' > ')[-1]}"
                  + (f"; vendor {p['vendor']!r} -> {VENDOR!r}" if "vendor" in change else ""))
        else:
            print(f"  ok already {p['handle']}")
    problems += [f"{h}: product not found" for h in PLAN if h not in found]
    if problems:
        sys.exit("STOP, nothing written:\n  " + "\n  ".join(problems))
    for c, n in names.items():
        print(f"  {c.split('/')[-1]:12} = {n['fullName']}")
    print(f"planned: {len(writes)} product updates")
    if not apply:
        print("\nDRY RUN: nothing written. Re-run with --apply to write.")
        return

    mutation = """mutation($p: ProductUpdateInput!) {
      productUpdate(product: $p) { product { handle vendor category { id } } userErrors { field message } } }"""
    bad = 0
    for p, change in writes:
        r = gql(mutation, {"p": {"id": p["id"], **change}})["productUpdate"]
        got = r["product"] or {}
        ok = not r["userErrors"] and (got.get("category") or {}).get("id") == PLAN[p["handle"]] \
            and got.get("vendor") == VENDOR
        bad += 0 if ok else 1
        print(f"  {'OK ' if ok else 'BAD'} {p['handle']:31} {(got.get('category') or {}).get('id', '?').split('/')[-1]:12} "
              f"{got.get('vendor')!r} {r['userErrors'] or ''}")
    print("\nDONE, all read back OK" if not bad else f"\nFINISHED WITH {bad} PROBLEM(S)")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
