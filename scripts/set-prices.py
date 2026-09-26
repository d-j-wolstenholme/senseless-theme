#!/usr/bin/env python3
"""Set Senseless single-product prices to match totally-numb.com, and keep the kits' "bought separately" figure true.

Founder, 26 Sep 2026: "change the price of all of the numbing products ... to match up with totally-numb.com's prices.
Ignore Bronze. Silver = Clinical, Gold = Advanced, Platinum = Professional ... it should be a price reduction overall."
Totally Numb prices were read from https://totally-numb.com/products.json on 26 Sep 2026 (public storefront, read-only).

CREAMS map one-to-one (TN sells Silver/Gold/Platinum creams in 10 g and 30 g):
  Clinical 10g 19.99 -> 14.99 (Silver)   Clinical 30g 44.99 -> 35.99 (Silver)
  Advanced 10g 24.99 -> 18.99 (Gold)     Advanced 30g 49.99 -> 45.99 (Gold)
  Professional 30g 55.99 = Platinum 30g 55.99 (no change)
GELS and SPRAYS: TN only sells Platinum and Professional gels/sprays (no Silver/Gold), so the mapping doesn't
determine Clinical/Advanced prices. They are held (GEL_SPRAY below is empty) until the founder decides.

Kits: compareAtPrice is the four-product sum (cream + gel + spray + Foaming Cleanser; the bag is free), per the
1 Sep 2026 bundle value model, and sections/senseless-bundle-contents.liquid prints it as "... are £X bought
separately". So every kit's compareAtPrice is recomputed from the NEW component prices in the same run. Kit
selling prices are only changed when KIT_PRICE says so; the run stops if a kit would cost as much as its parts.

Safety: store gate; a variant is written only if its current price is the expected old price; kits are written
only if their current compareAtPrice is the old four-product sum. Anything else stops the run before writing.

Usage (from the repo root, after ./scripts/refresh-token.sh):
  python3 scripts/set-prices.py           # dry run: prints the plan, writes nothing
  python3 scripts/set-prices.py --apply   # writes, then reads every variant back
"""
import json
import os
import re
import sys
import urllib.request
from decimal import Decimal as D

STORE = "senseless-numbing.myshopify.com"
URL = f"https://{STORE}/admin/api/2025-07/graphql.json"

# (handle, variant title) -> (old price, new price)
CREAMS = {
    ("clinical-strength-cream", "10g"): ("19.99", "14.99"),
    ("clinical-strength-cream", "30g"): ("44.99", "35.99"),
    ("advanced-strength-cream", "10g"): ("24.99", "18.99"),
    ("advanced-strength-cream", "30g"): ("49.99", "45.99"),
}
GEL_SPRAY = {}  # held: founder to decide (TN has no Silver/Gold gel or spray)
PLAN = {**CREAMS, **GEL_SPRAY}

CLEANSER = ("foaming-cleanser", "35ml")
KITS = {  # kit handle -> its four priced components (the bag is a free inclusion)
    "clinical-numbing-kit-small": [("clinical-strength-cream", "10g"), ("clinical-strength-gel", "15ml"), ("clinical-strength-spray", "35ml"), CLEANSER],
    "clinical-numbing-kit-large": [("clinical-strength-cream", "30g"), ("clinical-strength-gel", "35ml"), ("clinical-strength-spray", "35ml"), CLEANSER],
    "advanced-numbing-kit-small": [("advanced-strength-cream", "10g"), ("advanced-strength-gel", "15ml"), ("advanced-strength-spray", "35ml"), CLEANSER],
    "advanced-numbing-kit-large": [("advanced-strength-cream", "30g"), ("advanced-strength-gel", "35ml"), ("advanced-strength-spray", "35ml"), CLEANSER],
    "professional-numbing-kit-large": [("professional-strength-cream", "30g"), ("professional-strength-gel", "35ml"), ("professional-strength-spray", "35ml"), CLEANSER],
}
KIT_PRICE = {}  # kit handle -> new selling price; empty = selling prices unchanged (founder's call)


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

    nodes = gql("{ productVariants(first: 100) { nodes { id sku title price compareAtPrice product { id handle } } } }")["productVariants"]["nodes"]
    var = {(v["product"]["handle"], v["title"]): v for v in nodes}
    problems, writes = [], {}  # product id -> [variant input]

    for key, (old, new) in PLAN.items():
        v = var.get(key)
        if not v:
            problems.append(f"{key}: variant not found")
        elif D(v["price"]) == D(new):
            print(f"  ok already  {v['sku']:7} {key[0]:30} {key[1]:5} £{new}")
        elif D(v["price"]) != D(old):
            problems.append(f"{key}: price is £{v['price']}, expected £{old}")
        else:
            writes.setdefault(v["product"]["id"], []).append({"id": v["id"], "price": new})
            print(f"  PRICE       {v['sku']:7} {key[0]:30} {key[1]:5} £{old} -> £{new}")

    def price_of(key, new_prices):
        return D(PLAN[key][1]) if new_prices and key in PLAN else D(var[key]["price"])

    for kit, parts in KITS.items():
        k = var.get((kit, "Default Title"))
        if not k or any(p not in var for p in parts):
            problems.append(f"{kit}: kit or a component not found")
            continue
        old_sum = sum(D(var[p]["price"]) if p not in PLAN or D(var[p]["price"]) == D(PLAN[p][0]) else D(PLAN[p][0]) for p in parts)
        new_sum = sum(price_of(p, True) for p in parts)
        cur_cmp = D(k["compareAtPrice"] or 0)
        sell = D(KIT_PRICE.get(kit, k["price"]))
        if cur_cmp not in (old_sum, new_sum):
            problems.append(f"{kit}: compareAtPrice £{cur_cmp} is neither the old (£{old_sum}) nor the new (£{new_sum}) sum")
        if sell >= new_sum:
            problems.append(f"{kit}: selling price £{sell} would not be below its parts (£{new_sum})")
        change = {}
        if cur_cmp != new_sum:
            change["compareAtPrice"] = str(new_sum)
        if sell != D(k["price"]):
            change["price"] = str(sell)
        if change:
            writes.setdefault(k["product"]["id"], []).append({"id": k["id"], **change})
        save = new_sum - sell
        print(f"  {'KIT' if change else 'kit ok'}{'':6}{k['sku']:7} {kit:30} sell £{k['price']}"
              f"{' -> £' + str(sell) if 'price' in change else ''}; bought separately £{cur_cmp}"
              f"{' -> £' + str(new_sum) if 'compareAtPrice' in change else ''}; saving £{save} ({save / new_sum:.1%})")

    if problems:
        sys.exit("STOP, nothing written:\n  " + "\n  ".join(problems))
    print(f"planned: {sum(len(x) for x in writes.values())} variant writes on {len(writes)} products")
    if not apply:
        print("\nDRY RUN: nothing written. Re-run with --apply to write.")
        return

    mutation = """mutation($p: ID!, $v: [ProductVariantsBulkInput!]!) {
      productVariantsBulkUpdate(productId: $p, variants: $v) {
        productVariants { id sku price compareAtPrice } userErrors { field message } } }"""
    bad = 0
    for pid, vs in writes.items():
        r = gql(mutation, {"p": pid, "v": vs})["productVariantsBulkUpdate"]
        if r["userErrors"]:
            bad += 1
            print("  USER ERRORS", r["userErrors"])
        want = {x["id"]: x for x in vs}
        for pv in r["productVariants"]:
            if pv["id"] in want:
                w = want[pv["id"]]
                ok = all(D(pv[f] or 0) == D(w[f]) for f in ("price", "compareAtPrice") if f in w)
                bad += 0 if ok else 1
                print(f"  {'OK ' if ok else 'BAD'} {pv['sku']:7} price £{pv['price']} compare-at {pv['compareAtPrice'] or '-'}")
    # independent read-back from a fresh query
    after = {(v["product"]["handle"], v["title"]): v for v in gql(
        "{ productVariants(first: 100) { nodes { title price compareAtPrice product { handle } } } }")["productVariants"]["nodes"]}
    for key, (_, new) in PLAN.items():
        if D(after[key]["price"]) != D(new):
            bad += 1
            print(f"  READ-BACK MISMATCH {key}: £{after[key]['price']} != £{new}")
    print("\nDONE, all read back OK" if not bad else f"\nFINISHED WITH {bad} PROBLEM(S)")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
