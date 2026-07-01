#!/usr/bin/env python3
"""Senseless — build the 5-bundle product line (products + metafields + inventory).
Each bundle = own product + own SKU, single Default variant, ACTIVE, tracked, stock 20.
price = 5% off the sum of live component prices (computed elsewhere); compareAtPrice = the sum
(so the storefront shows the saving natively). productType=Bundle + tags=[tier] +
senseless.tier/format/bundle_contents metafields. Smart collection built separately.
"""
import os, sys, json, urllib.request, urllib.error, time
TOKEN=os.environ["SHOPIFY_ACCESS_TOKEN"]
URL="https://senseless-numbing.myshopify.com/admin/api/2024-10/graphql.json"
LOC="gid://shopify/Location/118501376348"

def gq(q,v=None):
    body=json.dumps({"query":q,"variables":v or {}}).encode()
    r=urllib.request.Request(URL,data=body,headers={"X-Shopify-Access-Token":TOKEN,"Content-Type":"application/json"})
    for a in range(4):
        try: return json.load(urllib.request.urlopen(r,timeout=40))
        except urllib.error.HTTPError as e:
            if a==3: raise
            time.sleep(2)

CL="/products/clinical-strength-cream"; CG="/products/clinical-strength-gel"; CS="/products/clinical-strength-spray"
AL="/products/advanced-strength-cream"; AG="/products/advanced-strength-gel"; AS="/products/advanced-strength-spray"
PL="/products/professional-strength-cream"; PG="/products/professional-strength-gel"; PS="/products/professional-strength-spray"
CLN="Foaming Cleanser (150ml)|/products/foaming-cleanser"

BUNDLES=[
 dict(sku="SBUN-CL-S",tier="Clinical",size="Small",title="Clinical Numbing Kit — Small",handle="clinical-numbing-kit-small",
      price="75.96",compare="79.96",contents=[f"Clinical Strength Cream (10g)|{CL}",f"Clinical Strength Gel (15ml)|{CG}",f"Clinical Strength Spray (35ml)|{CS}",CLN]),
 dict(sku="SBUN-CL-L",tier="Clinical",size="Large",title="Clinical Numbing Kit — Large",handle="clinical-numbing-kit-large",
      price="113.96",compare="119.96",contents=[f"Clinical Strength Cream (30g)|{CL}",f"Clinical Strength Gel (35ml)|{CG}",f"Clinical Strength Spray (35ml)|{CS}",CLN]),
 dict(sku="SBUN-AD-S",tier="Advanced",size="Small",title="Advanced Numbing Kit — Small",handle="advanced-numbing-kit-small",
      price="90.21",compare="94.96",contents=[f"Advanced Strength Cream (10g)|{AL}",f"Advanced Strength Gel (15ml)|{AG}",f"Advanced Strength Spray (35ml)|{AS}",CLN]),
 dict(sku="SBUN-AD-L",tier="Advanced",size="Large",title="Advanced Numbing Kit — Large",handle="advanced-numbing-kit-large",
      price="128.21",compare="134.96",contents=[f"Advanced Strength Cream (30g)|{AL}",f"Advanced Strength Gel (35ml)|{AG}",f"Advanced Strength Spray (35ml)|{AS}",CLN]),
 dict(sku="SBUN-PR-L",tier="Professional",size="Large",title="Professional Numbing Kit — Large",handle="professional-numbing-kit-large",
      price="143.41",compare="150.96",contents=[f"Professional Strength Cream (30g)|{PL}",f"Professional Strength Gel (35ml)|{PG}",f"Professional Strength Spray (35ml)|{PS}",CLN]),
]

def desc(b):
    return (f"<p>Everything for {b['tier'].lower()}-strength prep and aftercare in one kit: a strength-matched "
            f"numbing cream, gel and spray, plus the Foaming Cleanser for before and after. Assembled and picked as a single unit.</p>"
            f"<p>Senseless is a cosmetic product, formulated in the United Kingdom. It is not a medicine. "
            f"Numbing reduces discomfort rather than removing it — follow the product instructions and your practitioner's guidance.</p>")

# 1. metafield definitions (idempotent)
DEF="""mutation($d:MetafieldDefinitionInput!){metafieldDefinitionCreate(definition:$d){createdDefinition{key} userErrors{code message}}}"""
for d in [
  {"namespace":"senseless","key":"tier","name":"Strength tier","type":"single_line_text_field","ownerType":"PRODUCT"},
  {"namespace":"senseless","key":"format","name":"Format","type":"single_line_text_field","ownerType":"PRODUCT"},
  {"namespace":"senseless","key":"bundle_contents","name":"Bundle contents","type":"list.single_line_text_field","ownerType":"PRODUCT"},
]:
    r=gq(DEF,{"d":d}); e=r["data"]["metafieldDefinitionCreate"]["userErrors"]
    print("def",d["key"],"->","exists" if e and any(x["code"]=="TAKEN" for x in e) else ("OK" if not e else e))

PCREATE="""mutation($p:ProductInput!){productCreate(input:$p){product{id handle variants(first:1){nodes{id inventoryItem{id}}}} userErrors{field message}}}"""
VUPDATE="""mutation($pid:ID!,$v:[ProductVariantsBulkInput!]!){productVariantsBulkUpdate(productId:$pid,variants:$v){productVariants{id sku price compareAtPrice} userErrors{field message}}}"""
ACT="""mutation($id:ID!,$loc:ID!){inventoryActivate(inventoryItemId:$id,locationId:$loc,available:20){inventoryLevel{id} userErrors{field message}}}"""
MSET="""mutation($m:[MetafieldsSetInput!]!){metafieldsSet(metafields:$m){metafields{key} userErrors{field message}}}"""

# find existing bundle handles to avoid dupes
existing={p["handle"] for p in gq('{products(first:50,query:"product_type:Bundle"){nodes{handle}}}')["data"]["products"]["nodes"]}

results=[]
for b in BUNDLES:
    if b["handle"] in existing:
        print("SKIP exists",b["handle"]); continue
    r=gq(PCREATE,{"p":{"title":b["title"],"handle":b["handle"],"descriptionHtml":desc(b),"productType":"Bundle","status":"ACTIVE","tags":[b["tier"],"Bundle"]}})
    res=r["data"]["productCreate"]
    if res["userErrors"]: print("CREATE ERR",b["sku"],res["userErrors"]); continue
    pid=res["product"]["id"]; var=res["product"]["variants"]["nodes"][0]; vid=var["id"]; iid=var["inventoryItem"]["id"]
    # price + compareAt + sku + tracking
    u=gq(VUPDATE,{"pid":pid,"v":[{"id":vid,"price":b["price"],"compareAtPrice":b["compare"],"inventoryItem":{"sku":b["sku"],"tracked":True}}]})
    ue=u["data"]["productVariantsBulkUpdate"]["userErrors"]
    # inventory 20
    a=gq(ACT,{"id":iid,"loc":LOC}); ae=a["data"]["inventoryActivate"]["userErrors"]
    # metafields
    m=gq(MSET,{"m":[
        {"ownerId":pid,"namespace":"senseless","key":"tier","type":"single_line_text_field","value":b["tier"]},
        {"ownerId":pid,"namespace":"senseless","key":"format","type":"single_line_text_field","value":"Bundle"},
        {"ownerId":pid,"namespace":"senseless","key":"bundle_contents","type":"list.single_line_text_field","value":json.dumps(b["contents"])},
    ]})
    me=m["data"]["metafieldsSet"]["userErrors"]
    print(f'{b["sku"]} created {b["handle"]} £{b["price"]} (cmp {b["compare"]}) var:{"OK" if not ue else ue} inv:{"OK" if not ae else ae} mf:{"OK" if not me else me}')
    results.append((b["sku"],b["handle"],pid))
print("\nCreated:",len(results))
PY = None
