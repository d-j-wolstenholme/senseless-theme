#!/usr/bin/env python3
"""Set Shopify unit pricing on every Senseless variant that is sold by weight, volume or number.

Why: Google Merchant Center flags "Missing unit pricing measure" [unit_pricing_measure], which it
calls legally required in the UK. The Google & YouTube channel takes unit_pricing_measure /
unit_pricing_base_measure from each Shopify variant's unit price setting, so the fix is variant
data, not the theme.

Reference unit (UK Price Marking Order 2004 art. 1, as amended from 6 Apr 2026; Schedule 1 and its
per-100g/100ml list were omitted): the unit price is per 1 kilogram (sold by weight), per 1 litre
(sold by volume), or per individual item (sold by number).
  creams (g)                 -> per 1 KG
  gels, sprays, cleanser (ml) -> per 1 L
  Vitamin A&D ointment 4-pack -> 4 ITEM, per 1 ITEM
  bundles (mixed kits), the bag (single item), helper products -> left alone

Usage (from the repo root, after ./scripts/refresh-token.sh):
  python3 scripts/set-unit-pricing.py           # dry run: prints the plan, writes nothing
  python3 scripts/set-unit-pricing.py --apply   # writes, then reads every variant back
"""
import json
import os
import re
import sys
import urllib.request

STORE = "senseless-numbing.myshopify.com"
URL = f"https://{STORE}/admin/api/2025-07/graphql.json"


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


def measurement(variant):
    ptype = variant["product"]["productType"]
    m = re.fullmatch(r"(\d+(?:\.\d+)?)(g|ml)", (variant["title"] or "").strip().lower())
    if ptype in ("Cream", "Gel", "Spray", "Cleanser") and m:
        grams = m.group(2) == "g"
        return {"quantityValue": float(m.group(1)), "quantityUnit": "G" if grams else "ML",
                "referenceValue": 1, "referenceUnit": "KG" if grams else "L"}
    if variant["sku"] == "VAD-4PK":
        return {"quantityValue": 4.0, "quantityUnit": "ITEM", "referenceValue": 1, "referenceUnit": "ITEM"}
    return None


def main():
    apply = "--apply" in sys.argv
    load_env()
    shop = gql("{ shop { myshopifyDomain } }")["shop"]["myshopifyDomain"]
    if shop != STORE:
        sys.exit(f"STOP: store gate failed ({shop} != {STORE})")
    print(f"store gate: {shop}")

    variants = gql("{ productVariants(first: 100) { nodes { id sku title price product { id title productType } } } }")["productVariants"]["nodes"]
    plan, skipped = {}, []
    for v in variants:
        meas = measurement(v)
        if meas:
            plan.setdefault(v["product"]["id"], []).append((v, meas))
        else:
            skipped.append(f"{v['sku'] or '-'} {v['product']['title']} ({v['product']['productType']})")

    for vs in plan.values():
        for v, m in vs:
            per = float(v["price"]) / m["quantityValue"] * {"KG": 1000, "L": 1000, "ITEM": 1}[m["referenceUnit"]]
            print(f"  {v['sku']:7} {v['product']['title'][:28]:28} {v['title']:6} £{v['price']:>6} -> "
                  f"{m['quantityValue']:g}{m['quantityUnit']} per {m['referenceValue']}{m['referenceUnit']}  (~£{per:,.2f}/{m['referenceUnit'].lower()})")
    print(f"planned: {sum(len(x) for x in plan.values())} variants on {len(plan)} products")
    print("left alone:", "; ".join(skipped))
    if not apply:
        print("\nDRY RUN: nothing written. Re-run with --apply to write.")
        return

    mutation = """mutation($p: ID!, $v: [ProductVariantsBulkInput!]!) {
      productVariantsBulkUpdate(productId: $p, variants: $v) {
        productVariants { id sku showUnitPrice unitPrice { amount }
          unitPriceMeasurement { quantityValue quantityUnit referenceValue referenceUnit } }
        userErrors { field message } } }"""
    bad = 0
    for pid, vs in plan.items():
        data = gql(mutation, {"p": pid, "v": [{"id": v["id"], "unitPriceMeasurement": m, "showUnitPrice": True} for v, m in vs]})
        r = data["productVariantsBulkUpdate"]
        if r["userErrors"]:
            bad += 1
            print("  USER ERRORS", [v["sku"] for v, _ in vs], r["userErrors"])
        for pv in r["productVariants"]:
            m = pv["unitPriceMeasurement"] or {}
            ok = pv["showUnitPrice"] and m.get("referenceUnit") in ("KG", "L", "ITEM")
            bad += 0 if ok else 1
            print(f"  {'OK ' if ok else 'BAD'} {pv['sku']:7} {m.get('quantityValue')}{m.get('quantityUnit')} -> "
                  f"£{(pv['unitPrice'] or {}).get('amount')} per {m.get('referenceValue')}{m.get('referenceUnit')}")
    print("\nDONE, all read back OK" if not bad else f"\nFINISHED WITH {bad} PROBLEM(S)")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
