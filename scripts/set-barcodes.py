#!/usr/bin/env python3
"""Set each Senseless variant's barcode to its GS1 UK code from the owner's barcode sheet.

Why: Google Merchant Center takes each item's GTIN from the Shopify variant barcode (Google & YouTube
channel), and so does the theme's JSON-LD gtin13. On 23 Sep 2026 Shopify held a barcode on only 3 of
22 variants, and those 3 were the sheet's OLD US-range codes (076.../079...), not its GS1 UK codes.

Source of truth: Google Sheet "Barcodes" (Drive 165V5aaEfCa3AWYv2Q5_Vxe-B5ImsJzP5NrJtaqQbyQk, owner
pajones78@googlemail.com, modified 21 Sep 2026), column D "GS1 CODES" (5065028388xxx). Columns A-C
are grouped under "OLD BARCODES".

Mapping is by product handle + size, i.e. tier x format x size, NEVER by the sheet's SKU column: the
sheet's gel SKUs (S15AD, S35PR...) are not Shopify's (SG15AD, SG35PR...), and the sheet writes gel,
spray and foam sizes in "g" where Shopify says "ml". Left empty on purpose: VAD-4PK (the sheet has no
GS1 code for it and lists it as Unbranded), the 5 bundles and the Build-your-own helper (not in the
sheet). Every code below has a valid GS1 check digit (verified in main()).

Safety: a variant is only written if its current barcode is empty or is the sheet's OLD code for that
same item. Anything else stops the run, so nothing unexpected is overwritten.

Usage (from the repo root, after ./scripts/refresh-token.sh):
  python3 scripts/set-barcodes.py           # dry run: prints the plan, writes nothing
  python3 scripts/set-barcodes.py --apply   # writes, then reads every variant back
"""
import json
import os
import re
import sys
import urllib.request

STORE = "senseless-numbing.myshopify.com"
URL = f"https://{STORE}/admin/api/2025-07/graphql.json"

# (handle, variant title) -> (GS1 code, OLD code or None, sheet row description)
PLAN = {
    ("clinical-strength-cream", "10g"): ("5065028388108", None, "Senseless Clinical Cream 10g"),
    ("clinical-strength-cream", "30g"): ("5065028388122", None, "Senseless Clinical Cream 30g"),
    ("advanced-strength-cream", "10g"): ("5065028388115", None, "Senseless Advanced Cream 10g"),
    ("advanced-strength-cream", "30g"): ("5065028388139", None, "Senseless Advanced Cream 30g"),
    ("professional-strength-cream", "30g"): ("5065028388146", None, "Senseless Professional Cream 30g"),
    ("clinical-strength-gel", "15ml"): ("5065028388047", "0767461321111", "Senseless CLINICAL Gel 15g"),
    ("clinical-strength-gel", "35ml"): ("5065028388009", "0795847726144", "Senseless Clinical Gel 35g"),
    ("advanced-strength-gel", "15ml"): ("5065028388054", None, "Senseless ADVANCED Gel 15g"),
    ("advanced-strength-gel", "35ml"): ("5065028388016", None, "Senseless Advanced Gel 35g"),
    ("professional-strength-gel", "15ml"): ("5065028388061", None, "Senseless PRO Gel 15g"),
    ("professional-strength-gel", "35ml"): ("5065028388023", None, "Senseless Professional Gel 35g"),
    ("clinical-strength-spray", "35ml"): ("5065028388078", None, "Senseless CLINICAL SPRAY 35g"),
    ("advanced-strength-spray", "35ml"): ("5065028388085", None, "Senseless ADVANCED SPRAY 35g"),
    ("professional-strength-spray", "35ml"): ("5065028388092", None, "Senseless PRO SPRAY 35g"),
    ("foaming-cleanser", "35ml"): ("5065028388030", "0795847726182", "Senseless FOAM SPRAY 35g"),
    ("senseless-cosmetics-bag", "Default Title"): ("5065028388344", None, "SenselessBag"),
}


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


def gtin_ok(code):
    digits = [int(c) for c in code]
    total = sum(d * (3 if i % 2 else 1) for i, d in enumerate(digits[:-1]))
    return len(code) == 13 and (10 - total % 10) % 10 == digits[-1]


def main():
    apply = "--apply" in sys.argv
    codes = [c for c, _, _ in PLAN.values()]
    if not all(gtin_ok(c) for c in codes) or len(set(codes)) != len(codes):
        sys.exit("STOP: a code in PLAN fails its GS1 check digit or is duplicated")
    load_env()
    shop = gql("{ shop { myshopifyDomain } }")["shop"]["myshopifyDomain"]
    if shop != STORE:
        sys.exit(f"STOP: store gate failed ({shop} != {STORE})")
    print(f"store gate: {shop}")

    variants = gql("{ productVariants(first: 100) { nodes { id sku title barcode product { id handle } } } }")["productVariants"]["nodes"]
    found, writes, problems = set(), {}, []
    for v in variants:
        key = (v["product"]["handle"], v["title"])
        if key not in PLAN:
            continue
        found.add(key)
        code, old, desc = PLAN[key]
        cur = v["barcode"] or ""
        if cur == code:
            print(f"  ok already  {v['sku']:7} {key[0]:30} {key[1]:13} {code}")
        elif cur in ("", old):
            writes.setdefault(v["product"]["id"], []).append((v, code))
            print(f"  WRITE       {v['sku']:7} {key[0]:30} {key[1]:13} {cur or '(empty)':15} -> {code}  [{desc}]")
        else:
            problems.append(f"{key}: current barcode {cur!r} is neither empty nor the sheet's old code {old!r}")
    problems += [f"{k}: variant not found in Shopify" for k in PLAN if k not in found]
    if problems:
        sys.exit("STOP, nothing written:\n  " + "\n  ".join(problems))
    print(f"planned: {sum(len(x) for x in writes.values())} writes on {len(writes)} products")
    if not apply:
        print("\nDRY RUN: nothing written. Re-run with --apply to write.")
        return

    mutation = """mutation($p: ID!, $v: [ProductVariantsBulkInput!]!) {
      productVariantsBulkUpdate(productId: $p, variants: $v) {
        productVariants { id sku barcode }
        userErrors { field message } } }"""
    bad = 0
    for pid, vs in writes.items():
        data = gql(mutation, {"p": pid, "v": [{"id": v["id"], "barcode": code} for v, code in vs]})
        r = data["productVariantsBulkUpdate"]
        if r["userErrors"]:
            bad += 1
            print("  USER ERRORS", [v["sku"] for v, _ in vs], r["userErrors"])
        want = {v["id"]: code for v, code in vs}
        for pv in r["productVariants"]:
            if pv["id"] in want:
                ok = pv["barcode"] == want[pv["id"]]
                bad += 0 if ok else 1
                print(f"  {'OK ' if ok else 'BAD'} {pv['sku']:7} {pv['barcode']}")
    print("\nDONE, all read back OK" if not bad else f"\nFINISHED WITH {bad} PROBLEM(S)")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
