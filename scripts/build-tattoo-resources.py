#!/usr/bin/env python3
"""Create the Shopify-side resources for Phase A of docs/TATTOO-BUILD-SWEEP.md.

Pages (A1, A9), product procedure metafields (A4/A8) and three collections (A4, A5, A8).
Articles are handled separately by scripts/publish-articles.py.

Everything here is idempotent: resources are matched by handle and updated in place, and the
metafield write is a READ-MODIFY-WRITE. `metafieldsSet` replaces the whole value of a
list.single_line_text_field — writing ["Tattooing"] onto professional-strength-cream would
destroy its existing six procedures — so the current list is read, appended to, de-duplicated
and written back with its compareDigest for concurrency safety.

Dry run by default. Nothing is written without --apply.

PUBLISH STATE, deliberate:
  tattoo-aftercare              PUBLISHED   — no new intended-use claim. Both products are
                                              already sold with published aftercare positioning.
  numbing-cream-for-tattoos     UNPUBLISHED — sweep item A4 says so explicitly; publishing is
                                              Phase B1, gated on G1.
  numbing-cream-for-piercings   UNPUBLISHED — A8 is marked "no tattoo gate", which is not the
                                              same as ungated. G1 asks what the CPSR declares as
                                              intended use; that question covers piercing exactly
                                              as it covers tattooing, and G1's own default is
                                              "build, do not publish". One line to publish once
                                              the safety assessor answers.

Usage:
  python3 scripts/build-tattoo-resources.py            # dry run
  python3 scripts/build-tattoo-resources.py --apply
"""
import argparse
import json
import os
import sys
import urllib.error
import urllib.request

STORE = "senseless-numbing.myshopify.com"
BASE = f"https://{STORE}/admin/api/2024-10"
PROC_DEF_GID = "gid://shopify/MetafieldDefinition/429332955484"  # senseless.recommended_procedures
NEW_PROCEDURES = ["Tattooing", "Piercing"]


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
        sys.exit(f"HTTP {exc.code} {method or 'GET'} {path}\n{exc.read().decode()[:2000]}")


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


# --------------------------------------------------------------------------- pages
PAGES = [
    {
        "handle": "delivery",
        "title": "Delivery",
        "suffix": "delivery",
        "mt": "Numbing Cream Delivery UK — Next-Day | Senseless",
        "md": "Free UK delivery over £40, free next-day over £80. Order by 1pm on a working day "
              "for same-day dispatch. Royal Mail, tracked, plain unbranded packaging.",
    },
    {
        "handle": "tktx-numbing-cream-uk",
        "title": "TKTX numbing cream in the UK",
        "suffix": "tktx-numbing-cream-uk",
        "mt": "TKTX Numbing Cream UK: What to Check | Senseless",
        "md": "Buying numbing cream in the UK? Seven checks for any listing — who is behind it, "
              "whether it holds a CPSR, size and price per gram, and where it ships from.",
    },
]


def sync_pages(apply_changes):
    print("== pages ==")
    live = {p["handle"]: p for p in rest("/pages.json?limit=250&fields=id,handle,template_suffix")["pages"]}
    for page in PAGES:
        body = {"title": page["title"], "handle": page["handle"],
                "template_suffix": page["suffix"], "published": True,
                "body_html": ""}
        if page["handle"] in live:
            pid = live[page["handle"]]["id"]
            print(f"  UPDATE /pages/{page['handle']} (id {pid})")
            if apply_changes:
                rest(f"/pages/{pid}.json", {"page": dict(body, id=pid)}, method="PUT")
        else:
            print(f"  CREATE /pages/{page['handle']}")
            if not apply_changes:
                continue
            pid = rest("/pages.json", {"page": body})["page"]["id"]
            print(f"      created id {pid}")
        if apply_changes:
            sync_metafields("pages", pid, [
                ("global", "title_tag", "single_line_text_field", page["mt"]),
                ("global", "description_tag", "single_line_text_field", page["md"]),
            ])


def sync_metafields(owner_path, owner_id, wanted):
    current = {(m["namespace"], m["key"]): m
               for m in rest(f"/{owner_path}/{owner_id}/metafields.json")["metafields"]}
    for ns, key, mtype, value in wanted:
        found = current.get((ns, key))
        if found and found.get("value") == value:
            print(f"      {ns}.{key}: unchanged")
        elif found:
            print(f"      {ns}.{key}: UPDATE")
            rest(f"/metafields/{found['id']}.json",
                 {"metafield": {"id": found["id"], "type": mtype, "value": value}}, method="PUT")
        else:
            print(f"      {ns}.{key}: CREATE")
            rest(f"/{owner_path}/{owner_id}/metafields.json",
                 {"metafield": {"namespace": ns, "key": key, "type": mtype, "value": value}})


# ------------------------------------------------------- product procedure metafields
READ_PROC = """
query { products(first: 50) { edges { node { id handle title
  metafield(namespace: "senseless", key: "recommended_procedures") { value compareDigest } } } } }
"""

SET_PROC = """
mutation SetProc($metafields: [MetafieldsSetInput!]!) {
  metafieldsSet(metafields: $metafields) {
    metafields { key value ownerType }
    userErrors { field message code elementIndex }
  }
}
"""


def sync_product_procedures(apply_changes):
    print("\n== product procedure metafields (read-modify-write) ==")
    edges = gql(READ_PROC)["products"]["edges"]
    payload = []
    for edge in edges:
        node = edge["node"]
        mf = node.get("metafield")
        existing = json.loads(mf["value"]) if mf and mf["value"] else []
        merged = list(existing)
        for proc in NEW_PROCEDURES:
            if proc not in merged:
                merged.append(proc)
        if merged == existing:
            print(f"  {node['handle']:34} unchanged ({len(existing)} values)")
            continue
        added = [p for p in merged if p not in existing]
        state = "CREATE field" if not mf else f"append to {len(existing)}"
        print(f"  {node['handle']:34} {state}: +{added}")
        entry = {"ownerId": node["id"], "namespace": "senseless",
                 "key": "recommended_procedures", "type": "list.single_line_text_field",
                 "value": json.dumps(merged, ensure_ascii=False)}
        if mf and mf.get("compareDigest"):
            entry["compareDigest"] = mf["compareDigest"]
        payload.append(entry)

    if not payload:
        print("  nothing to write")
        return
    print(f"  -> {len(payload)} product(s) to write")
    if not apply_changes:
        return
    for i in range(0, len(payload), 25):
        res = gql(SET_PROC, {"metafields": payload[i:i + 25]})["metafieldsSet"]
        if res["userErrors"]:
            sys.exit(f"metafieldsSet errors: {json.dumps(res['userErrors'], indent=2)}")
        print(f"  wrote {len(res['metafields'])} metafield(s)")


# ---------------------------------------------------------------------- collections
COLLECTIONS = [
    {
        "handle": "numbing-cream-for-tattoos",
        "title": "Numbing Cream for Tattoos",
        "suffix": "numbing-cream-for-tattoos",
        "published": False,
        "seo_title": "Numbing Cream for Tattoos UK — Three Strengths | Senseless",
        "seo_desc": "Numbing cream, gel and spray for tattoo appointments. Three UK-formulated "
                    "strengths matched to the length of the sitting. CPSR assessed. Ask your artist first.",
        "body": "<p>A tattoo sitting is measured in hours rather than minutes, over an area that can "
                "be a few centimetres or a whole limb. The Senseless range is built around that: three "
                "strengths matched to the length of the booking, and three formats matched to the size "
                "of the area. Cream is general-purpose, gel is precise on smaller defined work, and "
                "spray covers a limb or a back piece. Every formula is UK-formulated by Matrix Health "
                "Group Ltd and assessed under a Cosmetic Product Safety Report. It is a cosmetic "
                "product, not a medicine. Whether to use anything before your appointment is your "
                "artist's decision — ask them when you book.</p>",
        "rules": [{"column": "PRODUCT_METAFIELD_DEFINITION", "relation": "EQUALS",
                   "condition": "Tattooing", "conditionObjectId": PROC_DEF_GID}],
        "disjunctive": False,
    },
    {
        "handle": "numbing-cream-for-piercings",
        "title": "Numbing Cream for Piercings",
        "suffix": "numbing-cream-for-piercings",
        "published": False,
        "seo_title": "Numbing Cream for Piercings UK | Senseless",
        "seo_desc": "Numbing cream and gel for piercing appointments — three UK-formulated strengths, "
                    "CPSR assessed. Honest guidance on when preparation is and isn't worth it.",
        "body": "<p>A single lobe piercing is over in seconds, and we would rather say so than sell "
                "into it. Where preparation earns its place is cartilage, several piercings in one "
                "appointment, or simply arriving less anxious than last time. Gel is usually the "
                "format — a piercing site is small and precise — and Clinical is the sensible default, "
                "with Advanced for cartilage or a multi-piercing sitting. UK-formulated by Matrix "
                "Health Group Ltd and CPSR assessed. A cosmetic product, not a medicine. Studios have "
                "their own protocols, so ask your piercer when you book.</p>",
        "rules": [{"column": "PRODUCT_METAFIELD_DEFINITION", "relation": "EQUALS",
                   "condition": "Piercing", "conditionObjectId": PROC_DEF_GID}],
        "disjunctive": False,
    },
    {
        "handle": "tattoo-aftercare",
        "title": "Tattoo Aftercare",
        "suffix": "tattoo-aftercare",
        "published": True,
        "seo_title": "Tattoo Aftercare UK — Cleanser & Ointment | Senseless",
        "seo_desc": "Tattoo aftercare from Senseless: an antibacterial cleanser and a simple "
                    "barrier ointment. UK-formulated and CPSR assessed. Your artist comes first.",
        "body": "<p>Two products rather than a routine you have to learn. The Foaming Cleanser is an "
                "antibacterial cleanser, suitable for use before treatment and on freshly treated "
                "skin. The Vitamin A &amp; D Ointment is a simple barrier ointment for keeping freshly "
                "treated skin comfortable and protected — four travel tubes for £2. Neither is a "
                "numbing product; both sit outside the strength range and have no tier. Everything "
                "else about looking after a new tattoo comes from the person who did it: aftercare "
                "advice differs between studios because the wrapping does, so your artist's "
                "instructions come before any guide, including ours.</p>",
        "rules": [{"column": "TYPE", "relation": "EQUALS", "condition": "Cleanser"},
                  {"column": "TYPE", "relation": "EQUALS", "condition": "Aftercare"}],
        "disjunctive": True,
    },
]

FIND_COLLECTION = """
query Find($q: String!) { collections(first: 5, query: $q) { edges { node { id handle title } } } }
"""

CREATE_COLLECTION = """
mutation Create($input: CollectionInput!) {
  collectionCreate(input: $input) {
    collection { id handle title templateSuffix productsCount { count } }
    userErrors { field message }
  }
}
"""

UPDATE_COLLECTION = """
mutation Update($input: CollectionInput!) {
  collectionUpdate(input: $input) {
    collection { id handle title templateSuffix productsCount { count } }
    userErrors { field message }
  }
}
"""

PUBLICATIONS = """
query { publications(first: 20) { edges { node { id name } } } }
"""

UNPUBLISH = """
mutation Unpub($id: ID!, $input: [PublicationInput!]!) {
  publishableUnpublish(id: $id, input: $input) {
    publishable { availablePublicationsCount { count } }
    userErrors { field message }
  }
}
"""

PUBLISH = """
mutation Pub($id: ID!, $input: [PublicationInput!]!) {
  publishablePublish(id: $id, input: $input) {
    publishable { availablePublicationsCount { count } }
    userErrors { field message }
  }
}
"""


def sync_collections(apply_changes):
    print("\n== collections ==")
    online_store = None
    for edge in gql(PUBLICATIONS)["publications"]["edges"]:
        if edge["node"]["name"] == "Online Store":
            online_store = edge["node"]["id"]
    print(f"  Online Store publication: {online_store}")

    for col in COLLECTIONS:
        found = gql(FIND_COLLECTION, {"q": f"handle:{col['handle']}"})["collections"]["edges"]
        base_input = {
            "title": col["title"],
            "handle": col["handle"],
            "descriptionHtml": col["body"],
            "templateSuffix": col["suffix"],
            "seo": {"title": col["seo_title"], "description": col["seo_desc"]},
            "ruleSet": {"appliedDisjunctively": col["disjunctive"], "rules": col["rules"]},
        }
        state = "PUBLISHED" if col["published"] else "UNPUBLISHED"
        if found:
            cid = found[0]["node"]["id"]
            print(f"  UPDATE /collections/{col['handle']} ({cid}) -> {state}")
            if apply_changes:
                res = gql(UPDATE_COLLECTION, {"input": dict(base_input, id=cid)})["collectionUpdate"]
                if res["userErrors"]:
                    sys.exit(f"collectionUpdate errors: {res['userErrors']}")
                print(f"      products: {res['collection']['productsCount']['count']}")
        else:
            print(f"  CREATE /collections/{col['handle']} -> {state}")
            if not apply_changes:
                continue
            res = gql(CREATE_COLLECTION, {"input": base_input})["collectionCreate"]
            if res["userErrors"]:
                sys.exit(f"collectionCreate errors: {res['userErrors']}")
            cid = res["collection"]["id"]
            print(f"      created {cid}, products: {res['collection']['productsCount']['count']}")

        if apply_changes and online_store:
            mutation = PUBLISH if col["published"] else UNPUBLISH
            key = "publishablePublish" if col["published"] else "publishableUnpublish"
            res = gql(mutation, {"id": cid, "input": [{"publicationId": online_store}]})[key]
            if res["userErrors"]:
                sys.exit(f"{key} errors: {res['userErrors']}")
            print(f"      {state.lower()} on Online Store")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()
    if "SHOPIFY_ACCESS_TOKEN" not in os.environ:
        sys.exit("SHOPIFY_ACCESS_TOKEN not set. Run ./scripts/refresh-token.sh then `source .env`.")
    verify_store()
    if not args.apply:
        print("DRY RUN — nothing will be written. Re-run with --apply.\n")
    sync_pages(args.apply)
    sync_product_procedures(args.apply)
    sync_collections(args.apply)
    print("\ndone." if args.apply else "\ndry run complete — no writes made.")


if __name__ == "__main__":
    main()
