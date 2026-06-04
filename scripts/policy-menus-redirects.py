#!/usr/bin/env python3
"""
Senseless — footer/nav menu repoints + /policies/* -> /pages/* redirects (Strand 5).
- Rebuilds the footer "THE SYSTEM" column (senseless-footer-explore): retires the dead
  choosing-your-strength / choosing-your-format / how-it-works / how-to-apply paths,
  repoints to live System + guide pages.
- Fixes the stale "By strength" submenu link in senseless-main.
- Creates /policies/* -> /pages/* URL redirects (dormant safety net; native policies
  return 200 so these only fire if a native policy is later removed).
"""
import os, sys, json, urllib.request, urllib.error
TOKEN = os.environ["SHOPIFY_ACCESS_TOKEN"]
URL = "https://senseless-numbing.myshopify.com/admin/api/2024-10/graphql.json"

def gq(query, variables=None):
    body = json.dumps({"query": query, "variables": variables or {}}).encode()
    req = urllib.request.Request(URL, data=body, headers={
        "X-Shopify-Access-Token": TOKEN, "Content-Type": "application/json"})
    for attempt in range(4):
        try: return json.load(urllib.request.urlopen(req, timeout=40))
        except urllib.error.HTTPError:
            if attempt == 3: raise
            import time; time.sleep(2)

MENU_UPDATE = """
mutation($id: ID!, $title: String!, $handle: String!, $items: [MenuItemUpdateInput!]!) {
  menuUpdate(id: $id, title: $title, handle: $handle, items: $items) {
    menu { id handle } userErrors { field message }
  }
}"""

def H(title, url, items=None):
    d = {"title": title, "type": "HTTP", "url": url}
    if items: d["items"] = items
    return d

# THE SYSTEM footer column — all live pages, no retired 301 paths
EXPLORE = {
  "id": "gid://shopify/Menu/334354022748", "title": "Senseless Footer Explore", "handle": "senseless-footer-explore",
  "items": [
    H("The Senseless System", "/pages/the-senseless-system"),
    H("Find your strength", "/pages/the-senseless-system#selector"),
    H("Using numbing cream", "/pages/using-numbing-cream"),
    H("Does it hurt?", "/pages/does-it-hurt"),
    H("FAQ", "/pages/faq"),
  ],
}

# Senseless Main — preserve structure; fix only the stale "By strength" child
MAIN = {
  "id": "gid://shopify/Menu/334353727836", "title": "Senseless Main", "handle": "senseless-main",
  "items": [
    H("Shop", "/collections/shop-all", [
      H("By format", "/collections/numbing-cream"),
      H("By procedure", "/pages/aesthetic-procedures"),
      H("By strength", "/pages/the-senseless-system#selector"),  # was /pages/choosing-your-strength (retired)
    ]),
    H("The System", "/pages/the-senseless-system", [
      H("The System", "/pages/the-senseless-system"),
      H("Guides", "/pages/does-it-hurt"),
    ]),
    H("About", "/pages/about"),
    H("Help", "/pages/faq", [
      H("FAQ", "/pages/faq"),
      H("Contact", "/pages/contact"),
      H("How long to work", "/pages/using-numbing-cream"),
      H("How long to last", "/pages/using-numbing-cream"),
      H("Does numbing cream actually work", "/pages/faq"),
    ]),
  ],
}

def update_menu(m):
    r = gq(MENU_UPDATE, {"id": m["id"], "title": m["title"], "handle": m["handle"], "items": m["items"]})
    res = r["data"]["menuUpdate"]; e = res["userErrors"]
    print(f"  menu {m['handle']}: {'OK' if not e else e}")

REDIRECT_CREATE = """
mutation($r: UrlRedirectInput!) {
  urlRedirectCreate(urlRedirect: $r) { urlRedirect { id path target } userErrors { field message } }
}"""
REDIRECTS = [
  ("/policies/shipping-policy", "/pages/shipping-delivery"),
  ("/policies/refund-policy", "/pages/returns-refunds"),
  ("/policies/privacy-policy", "/pages/privacy-policy"),
  ("/policies/terms-of-service", "/pages/terms-conditions"),
  ("/policies/contact-information", "/pages/contact"),
]

def create_redirects():
    # existing
    ex = gq('{ urlRedirects(first:100, query:"path:/policies"){nodes{path}}}')["data"]["urlRedirects"]["nodes"]
    have = {n["path"] for n in ex}
    for path, target in REDIRECTS:
        if path in have:
            print(f"  redirect exists {path}"); continue
        r = gq(REDIRECT_CREATE, {"r": {"path": path, "target": target}})
        res = r["data"]["urlRedirectCreate"]; e = res["userErrors"]
        print(f"  redirect {path} -> {target}: {'OK' if not e else e}")

if __name__ == "__main__":
    print("== menus ==")
    update_menu(EXPLORE); update_menu(MAIN)
    print("== redirects (dormant safety net) ==")
    create_redirects()
    print("Done.")
