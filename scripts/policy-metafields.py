#!/usr/bin/env python3
"""
Senseless — policy metafield definition creation + value population (Strand 5, the TN way).
Creates PAGE metafield definitions in the `policy` namespace, ports the vetted policy copy
into rich_text_field / json values, applies the £40/£80 free-shipping reconciliation on the
Shipping page, and assigns all 5 policy pages to the custom `policy` template.

Run:  python3 scripts/policy-metafields.py [--dry]
"""
import os, sys, json, html.parser, urllib.request, urllib.error

DRY = "--dry" in sys.argv
TOKEN = os.environ["SHOPIFY_ACCESS_TOKEN"]
STORE = "senseless-numbing.myshopify.com"
URL = f"https://{STORE}/admin/api/2024-10/graphql.json"
TODAY = "2026-06-04"

def gq(query, variables=None):
    body = json.dumps({"query": query, "variables": variables or {}}).encode()
    req = urllib.request.Request(URL, data=body, headers={
        "X-Shopify-Access-Token": TOKEN, "Content-Type": "application/json"})
    for attempt in range(4):
        try:
            return json.load(urllib.request.urlopen(req, timeout=40))
        except urllib.error.HTTPError as e:
            if attempt == 3: raise
            import time; time.sleep(2)

# ---------------- HTML -> Shopify rich-text JSON converter ----------------
class RT(html.parser.HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = {"type": "root", "children": []}
        self.block = None          # current block node (paragraph/heading/list-item)
        self.list = None           # current list node
        self.bold = 0; self.italic = 0
        self.link = None           # current link node
    def _target(self):
        return self.link["children"] if self.link is not None else (self.block["children"] if self.block else self.root["children"])
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "p":
            self.block = {"type": "paragraph", "children": []}; self.root["children"].append(self.block)
        elif tag in ("h2", "h3", "h4"):
            self.block = {"type": "heading", "level": int(tag[1]), "children": []}; self.root["children"].append(self.block)
        elif tag in ("ul", "ol"):
            self.list = {"type": "list", "listType": "unordered" if tag == "ul" else "ordered", "children": []}
            self.root["children"].append(self.list); self.block = None
        elif tag == "li":
            self.block = {"type": "list-item", "children": []}; (self.list["children"] if self.list else self.root["children"]).append(self.block)
        elif tag in ("strong", "b"): self.bold += 1
        elif tag in ("em", "i"): self.italic += 1
        elif tag == "a":
            self.link = {"type": "link", "url": a.get("href", ""), "title": "", "target": "", "children": []}
            (self.block["children"] if self.block else self.root["children"]).append(self.link)
        elif tag == "br":
            self._target().append({"type": "text", "value": "\n"})
    def handle_endtag(self, tag):
        if tag in ("strong", "b"): self.bold = max(0, self.bold-1)
        elif tag in ("em", "i"): self.italic = max(0, self.italic-1)
        elif tag == "a": self.link = None
        elif tag in ("ul", "ol"): self.list = None; self.block = None
        elif tag in ("p", "h2", "h3", "h4", "li"): self.block = None
    def handle_data(self, data):
        if not data: return
        if self.block is None and self.link is None:
            if not data.strip(): return
            self.block = {"type": "paragraph", "children": []}; self.root["children"].append(self.block)
        node = {"type": "text", "value": data}
        if self.bold: node["bold"] = True
        if self.italic: node["italic"] = True
        self._target().append(node)

def to_richtext(html_str):
    p = RT(); p.feed(html_str); return json.dumps(p.root, ensure_ascii=False)

# ---------------- Page content (ported + reconciled) ----------------
# Shipping: paid tiers KEPT, free £40/£80 thresholds ADDED, "Free shipping?" FAQ corrected.
SHIPPING_BODY = """
<h2>Dispatch</h2>
<p>Orders placed before 1pm on a working day are dispatched the same day; after 1pm or at weekends, the next working day. All orders ship from the United Kingdom via Royal Mail.</p>
<h2>Free delivery</h2>
<p>Free standard UK delivery on orders over &pound;40. Free next-day delivery on orders over &pound;80. Order before 1pm on a working day for same-day dispatch.</p>
<h2>Delivery options</h2>
<ul>
<li><strong>Standard</strong> — &pound;1.99 — 4&ndash;6 working days. <strong>Free on orders over &pound;40.</strong></li>
<li><strong>Express</strong> — &pound;2.99 — 2&ndash;3 working days.</li>
<li><strong>Next working day</strong> — &pound;7.99 — order by 1pm. <strong>Free on orders over &pound;80.</strong></li>
</ul>
<h2>Tracking your order</h2>
<p>A confirmation email with a tracking link is sent on dispatch. Track directly at <a href="https://www.royalmail.com/track-your-item">royalmail.com/track-your-item</a>. No confirmation within 24 hours — check spam or contact <a href="mailto:cs@senseless.uk">cs@senseless.uk</a>.</p>
<h2>Problems with your delivery</h2>
<p>Damaged, missing, or late beyond the expected window — contact <a href="mailto:cs@senseless.uk">cs@senseless.uk</a> with your order number. Report delivery issues within 14 days of the expected delivery date.</p>
"""

RETURNS_BODY = """
<h2>Returns policy</h2>
<p>You have 30 days from receipt to request a return. Items must be unused, unopened, and in original packaging; proof of purchase required. Items sent back without a prior return request are not accepted.</p>
<h2>How it works</h2>
<ul>
<li><strong>Step 1 — Request:</strong> contact <a href="mailto:cs@senseless.uk">cs@senseless.uk</a> with your order number; we confirm eligibility.</li>
<li><strong>Step 2 — Return:</strong> once approved, we send instructions. Returns to: Paddock Business Centre, Paddock Road, Skelmersdale, WN8 9PL.</li>
<li><strong>Step 3 — Refund:</strong> after we receive and inspect, refund to your original payment method within 10 working days.</li>
</ul>
<h2>Damaged or incorrect items</h2>
<p>Inspect on arrival. If anything is defective, damaged, or incorrect, contact <a href="mailto:cs@senseless.uk">cs@senseless.uk</a> immediately — handled separately from standard returns, don't wait for the window to pass.</p>
<h2>What cannot be returned</h2>
<p>Opened or used products are not eligible (hygiene). Sale items and gift cards are non-returnable. If unsure, ask before sending.</p>
"""

PRIVACY_BODY = """
<h2>Introduction</h2>
<p>This policy explains how Senseless (a trading name of Matrix Health Group Ltd) collects, uses, and protects your personal information when you visit our website, make a purchase, or communicate with us. We are committed to protecting your privacy in accordance with UK data protection law, including the UK General Data Protection Regulation (UK GDPR) and the Data Protection Act 2018. Contact for data-protection enquiries: <a href="mailto:cs@senseless.uk">cs@senseless.uk</a>.</p>
<h2>What we collect</h2>
<ul>
<li><strong>Information you provide</strong> — name, email, postal address, phone number, and payment details when you order or contact us.</li>
<li><strong>Automatic information</strong> — IP address, browser type, device information, and how you interact with our site, via cookies and similar technologies.</li>
<li><strong>Third-party information</strong> — payment processors and Shopify may provide information needed to complete your order.</li>
</ul>
<h2>How we use it</h2>
<p>To process and fulfil orders, communicate about your purchases, respond to enquiries, improve our site and services, comply with legal obligations, and prevent fraud. Marketing is sent only with your consent, and you can opt out at any time.</p>
<h2>Who we share it with</h2>
<p>Only where necessary: Shopify (our e-commerce platform), payment processors, delivery partners, and where required by law. We do not sell your personal information.</p>
<h2>Cookies</h2>
<p>We use cookies to operate the site, remember preferences, and understand usage. Full detail in our <a href="/pages/cookie-policy">Cookie Policy</a>.</p>
<h2>Your rights</h2>
<p>Under UK GDPR you can access, correct, or delete your data, restrict or object to processing, and request portability. Contact <a href="mailto:cs@senseless.uk">cs@senseless.uk</a>; we respond within 30 days. You may also complain to the Information Commissioner's Office (ICO) at <a href="https://ico.org.uk">ico.org.uk</a>.</p>
<h2>Data retention</h2>
<p>Held only as long as necessary for the purposes collected, including legal, accounting, or reporting requirements. Order data is retained for six years per UK tax and accounting obligations.</p>
"""

TERMS_BODY = """
<h2>Introduction</h2>
<p>These terms govern your use of the Senseless website and your purchase of products from us. By accessing the site or placing an order, you agree to them. Senseless is a trading name of Matrix Health Group Ltd, a company registered in England and Wales (company number 17099304). Registered address: Paddock Business Centre, Paddock Road, Skelmersdale, WN8 9PL.</p>
<h2>Using the site</h2>
<p>You must be at least 18 to purchase. Use the site only for lawful purposes; do not interfere with its operation, transmit harmful code, or access it through automated means without permission. We may withdraw or restrict access at any time without notice.</p>
<h2>Orders &amp; payment</h2>
<p>All orders are subject to acceptance and availability; placing an order is an offer to purchase. We may decline or cancel any order at our discretion, including suspected fraud or a pricing/description error. Prices are in GBP and include VAT where applicable. Payment is taken at order via the methods at checkout. You are responsible for the accuracy of the payment and delivery information you provide.</p>
<h2>Products &amp; descriptions</h2>
<p>We take reasonable care that descriptions and images are accurate; slight colour variation may occur due to screens. Descriptions are general information, not medical advice. All Senseless products are cosmetic-grade and assessed under the UK Cosmetic Products Regulation. They are not intended to diagnose, treat, cure, or prevent any medical condition.</p>
<h2>Intellectual property</h2>
<p>All content — text, images, logos, product names, and the Senseless system framework — is owned by Matrix Health Group Ltd or its licensors and protected by UK and international copyright and trademark law. No reproduction, distribution, or use without written permission.</p>
<h2>Limitation of liability</h2>
<p>Nothing excludes or limits liability for death or personal injury caused by our negligence, fraud, or anything that cannot be excluded under English law. Otherwise, to the extent permitted by law, we are not liable for indirect, incidental, or consequential losses (including loss of profit, data, or business opportunity), and our total liability for any claim shall not exceed the amount you paid for the relevant order.</p>
<h2>Governing law</h2>
<p>Governed by the laws of England and Wales; disputes subject to the exclusive jurisdiction of the courts of England and Wales.</p>
<h2>Changes</h2>
<p>We may update these terms; the current version always lives on this page. Continued use after changes is acceptance.</p>
"""

COOKIE_BODY = """
<h2>What cookies are</h2>
<p>Cookies are small text files stored on your device when you visit a website. They help the site function properly, remember your preferences, and understand how visitors use the pages. This policy explains what cookies the Senseless website uses and how you can manage them.</p>
<h2>Cookies we use</h2>
<ul>
<li><strong>Essential (Required)</strong> — Required for the site to function. These include session cookies for your shopping cart, authentication, and security. You cannot opt out of these without affecting site functionality.</li>
<li><strong>Analytics (Optional)</strong> — Help us understand how visitors use the site so we can improve it. These collect anonymous usage data and do not identify you personally.</li>
<li><strong>Marketing (Optional)</strong> — Used to deliver relevant advertising and track the effectiveness of campaigns. These are only set with your consent.</li>
</ul>
<h2>Managing your cookies</h2>
<p>You can control and delete cookies through your browser settings. Most browsers allow you to block cookies entirely, delete existing cookies, or be prompted before a cookie is set. Be aware that blocking essential cookies may prevent parts of the site from functioning correctly.</p>
<h2>Third-party cookies</h2>
<p>Our site uses services from Shopify, and may include integrations with payment processors and analytics providers that set their own cookies. We do not control these cookies. For information on their use, refer to the relevant provider's cookie or privacy policy.</p>
"""

PAGES = {
  "shipping-delivery": {
    "body": SHIPPING_BODY,
    "faq": [
      {"question": "Is delivery free?", "answer": "<p>Yes — free standard UK delivery on orders over &pound;40, and free next-day delivery on orders over &pound;80. Below those thresholds, Standard is &pound;1.99, Express &pound;2.99, and Next working day &pound;7.99.</p>"},
      {"question": "Change my address after ordering?", "answer": "<p>If not yet dispatched, contact <a href=\"mailto:cs@senseless.uk\">cs@senseless.uk</a>; once dispatched it can't be changed.</p>"},
      {"question": "International shipping?", "answer": "<p>UK only at present.</p>"},
      {"question": "Not home for delivery?", "answer": "<p>The courier follows its standard redelivery process; check your tracking link.</p>"},
      {"question": "Order hasn't arrived?", "answer": "<p>Check tracking first; if the window has passed with no update, contact <a href=\"mailto:cs@senseless.uk\">cs@senseless.uk</a> with your order number.</p>"},
    ],
    "see_also": [{"label": "Returns & Refunds", "url": "/pages/returns-refunds"}],
  },
  "returns-refunds": {
    "body": RETURNS_BODY,
    "faq": [
      {"question": "Can I exchange instead?", "answer": "<p>No direct exchanges — return the original and place a new order.</p>"},
      {"question": "Who pays return postage?", "answer": "<p>The customer, unless the item arrived damaged, defective, or incorrect.</p>"},
      {"question": "How long for a refund?", "answer": "<p>Within 10 working days of receipt; your bank may take longer to post it. Over 15 working days since approval — contact <a href=\"mailto:cs@senseless.uk\">cs@senseless.uk</a>.</p>"},
      {"question": "Do I need original packaging?", "answer": "<p>Yes — original, unopened.</p>"},
      {"question": "Item arrived damaged?", "answer": "<p>Contact <a href=\"mailto:cs@senseless.uk\">cs@senseless.uk</a> immediately with order number + photo.</p>"},
      {"question": "Do you ship to the EU?", "answer": "<p>UK only at present; if that changes, EU customers get the additional 14-day cooling-off period.</p>"},
    ],
    "see_also": [{"label": "Shipping & Delivery", "url": "/pages/shipping-delivery"}],
  },
  "privacy-policy": {
    "body": PRIVACY_BODY,
    "faq": [
      {"question": "Who is the data controller?", "answer": "<p>Matrix Health Group Ltd, registered in England and Wales (17099304). Contact: <a href=\"mailto:cs@senseless.uk\">cs@senseless.uk</a>.</p>"},
      {"question": "Do you sell my data?", "answer": "<p>No. Never to third parties.</p>"},
      {"question": "How do I opt out of marketing?", "answer": "<p>Use the unsubscribe link in any marketing email, or contact <a href=\"mailto:cs@senseless.uk\">cs@senseless.uk</a>.</p>"},
      {"question": "How do I request deletion?", "answer": "<p>Email <a href=\"mailto:cs@senseless.uk\">cs@senseless.uk</a>; we respond within 30 days.</p>"},
      {"question": "Where can I complain?", "answer": "<p>Contact us first; if unsatisfied, the ICO at <a href=\"https://ico.org.uk\">ico.org.uk</a>.</p>"},
    ],
    "see_also": [{"label": "Cookie Policy", "url": "/pages/cookie-policy"}, {"label": "Terms & Conditions", "url": "/pages/terms-conditions"}],
  },
  "terms-conditions": {
    "body": TERMS_BODY,
    "faq": [
      {"question": "Who operates this website?", "answer": "<p>Senseless, a trading name of Matrix Health Group Ltd (17099304), Paddock Business Centre, Paddock Road, Skelmersdale, WN8 9PL.</p>"},
      {"question": "How do I contact you about these terms?", "answer": "<p><a href=\"mailto:cs@senseless.uk\">cs@senseless.uk</a>.</p>"},
      {"question": "What law applies?", "answer": "<p>England and Wales.</p>"},
      {"question": "Can I use content from the site?", "answer": "<p>No — written permission required.</p>"},
    ],
    "see_also": [{"label": "Privacy Policy", "url": "/pages/privacy-policy"}, {"label": "Cookie Policy", "url": "/pages/cookie-policy"}],
  },
  "cookie-policy": {
    "body": COOKIE_BODY,
    "faq": [
      {"question": "What happens if I block all cookies?", "answer": "<p>Essential site functions like the shopping cart and checkout may not work. Analytics and marketing cookies can be blocked without affecting core functionality.</p>"},
      {"question": "Do you use cookies to track me across other websites?", "answer": "<p>We do not track you across other websites. Any marketing cookies used on our site operate within the scope of our advertising partnerships and only with your consent.</p>"},
      {"question": "How do I withdraw my cookie consent?", "answer": "<p>You can change your preferences at any time through the cookie consent banner on the site, or by clearing cookies in your browser settings.</p>"},
    ],
    "see_also": [{"label": "Privacy Policy", "url": "/pages/privacy-policy"}, {"label": "Terms & Conditions", "url": "/pages/terms-conditions"}],
  },
}

DEFS = [
  {"key": "prose_policy_body", "name": "Policy body (prose)", "type": "rich_text_field",
   "description": "Designed long-form policy body, rendered by the policy template."},
  {"key": "faq", "name": "Policy FAQ", "type": "json",
   "description": "Array of {question, answer} rendered as an accordion."},
  {"key": "see_also", "name": "Policy see-also links", "type": "json",
   "description": "Array of {label, url} related-page links."},
  {"key": "last_updated", "name": "Policy last updated", "type": "date",
   "description": "Version date shown at the top of the policy page."},
]

DEF_CREATE = """
mutation($d: MetafieldDefinitionInput!) {
  metafieldDefinitionCreate(definition: $d) {
    createdDefinition { id namespace key }
    userErrors { field message code }
  }
}"""

def create_defs():
    print("== metafield definitions ==")
    for d in DEFS:
        var = {"d": {"namespace": "policy", "key": d["key"], "name": d["name"],
                     "description": d["description"], "type": d["type"], "ownerType": "PAGE"}}
        if DRY:
            print(f"  [dry] would create policy.{d['key']} ({d['type']})"); continue
        r = gq(DEF_CREATE, var)
        res = r["data"]["metafieldDefinitionCreate"]
        errs = res["userErrors"]
        if errs and any(e.get("code") == "TAKEN" for e in errs):
            print(f"  exists  policy.{d['key']}")
        elif errs:
            print(f"  ERR     policy.{d['key']}: {errs}")
        else:
            print(f"  created policy.{d['key']} ({d['type']})")

PAGE_QUERY = '{ pages(first:50){nodes{ id handle templateSuffix }}}'
MFSET = """
mutation($m: [MetafieldsSetInput!]!) {
  metafieldsSet(metafields: $m) { metafields { key } userErrors { field message } }
}"""
PAGE_UPDATE = """
mutation($id: ID!, $page: PageUpdateInput!) {
  pageUpdate(id: $id, page: $page) { page { id templateSuffix } userErrors { field message } }
}"""

def populate():
    pages = {p["handle"]: p for p in gq(PAGE_QUERY)["data"]["pages"]["nodes"]}
    print("\n== values + template assignment ==")
    for handle, content in PAGES.items():
        pg = pages.get(handle)
        if not pg:
            print(f"  MISSING page /{handle}"); continue
        gid = pg["id"]
        rt = to_richtext(content["body"])
        mfs = [
            {"ownerId": gid, "namespace": "policy", "key": "prose_policy_body", "type": "rich_text_field", "value": rt},
            {"ownerId": gid, "namespace": "policy", "key": "faq", "type": "json", "value": json.dumps(content["faq"], ensure_ascii=False)},
            {"ownerId": gid, "namespace": "policy", "key": "see_also", "type": "json", "value": json.dumps(content["see_also"], ensure_ascii=False)},
            {"ownerId": gid, "namespace": "policy", "key": "last_updated", "type": "date", "value": TODAY},
        ]
        if DRY:
            print(f"  [dry] /{handle}: rt {len(rt)}b, {len(content['faq'])} faq, suffix->policy"); continue
        r = gq(MFSET, {"m": mfs})
        e = r["data"]["metafieldsSet"]["userErrors"]
        print(f"  /{handle}: metafields {'OK' if not e else e}")
        u = gq(PAGE_UPDATE, {"id": gid, "page": {"templateSuffix": "policy"}})
        ue = u["data"]["pageUpdate"]["userErrors"]
        print(f"           templateSuffix -> {'policy OK' if not ue else ue}")

if __name__ == "__main__":
    create_defs()
    populate()
    print("\nDone." + (" (dry run)" if DRY else ""))
