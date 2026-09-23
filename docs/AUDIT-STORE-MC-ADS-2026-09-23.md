# Audit — Shopify store vs Merchant Center vs Google Ads (+ schema, rich results, Search Console)

**Date:** 23 Sep 2026 · **Machine:** Mac mini (`Ds-Mac-mini.local`) · **Auditor:** Claude Code (render side)
**Store gate:** `senseless-numbing.myshopify.com` confirmed via Admin API `shop.myshopifyDomain`.
**Accounts:** Merchant Center **5805726847** · Google Ads **368-965-4782** (manager `540-506-3786`) ·
Search Console property **`sc-domain:senseless.uk`** · GA4 `G-N6XKMWQ92N`.

Everything below was observed live. Nothing is inferred from the repo except the two root-cause file
references, which are labelled.

---

## Verdict

The three systems **reconcile**. Prices match to the penny across Shopify → Merchant Center →
structured data → `og:price`. Merchant Center has zero account, setup or policy issues; Search
Console reports zero invalid rich results and no manual actions; the schema.org validator returns
0 errors / 0 warnings on six representative pages.

**One regulated-risk defect was found, and it is live now:** an ad-facing product page declares an
injectable collection as its breadcrumb parent (§P0).

---

## P0 — Foaming Cleanser PDP declares "Numbing Cream for Botox" as its breadcrumb parent

**URL:** `https://senseless.uk/products/foaming-cleanser` — verified by two independent live fetches
(subagent, then my own cache-busted `curl`):

```json
{ "@type": "ListItem", "position": 2,
  "name": "Numbing Cream for Botox",
  "item": "https://senseless.uk/collections/numbing-cream-for-botox" }
```
inside `"@id": "https://senseless.uk/products/foaming-cleanser#breadcrumb"`.

**Why it matters.** `.claude/rules/ad-facing.md` names *every product page* as an ad-facing surface
with "zero inbound links to the three, ever". This is not an `<a href>`, so the rule's stated
anchor-counting method does not catch it — but Google consumes `BreadcrumbList` both as a link and as
a **SERP-rendered breadcrumb**. This PDP is eligible to render as
`senseless.uk › Numbing Cream for Botox › Foaming Cleanser`. Google Ads reviews the landing page *and
its destination experience*. It is also simply wrong: the cleanser's parent is aftercare, not Botox.

**Scope today:** all 17 PDP breadcrumbs were pulled; **only `foaming-cleanser` is affected**. Every
other PDP resolves to Aesthetic Numbing Cream, a strength collection, or Merchandise.

**Root cause:** `snippets/senseless-breadcrumbs-jsonld.liquid:20` —
`{%- assign col = product.collections.first -%}`, with no injectable exclusion.

**Latent blast radius:** live `products.json` shows **12 products** belong to an injectable
collection. `product.collections.first` ordering is not controlled by the theme, so a membership or
sort change can flip more PDPs into an injectable breadcrumb with no code change.

**Fix (one line):** filter the three protected handles before `.first`.

**Rule amendment needed:** the "How to check it" section of `.claude/rules/ad-facing.md` must widen
from "count anchors" to "count anchors **and** structured-data `item` URLs", or this class of breach
keeps passing the check.

---

## Reconciliation — Shopify ↔ Merchant Center

| | Count |
|---|---|
| Shopify products / variants (Admin API) | **18 / 23** — of which 1 product + 1 variant is the internal `build-your-own-bundle` helper (UNLISTED, £0.01, Online Store only) |
| Real catalogue | **17 / 22** — matches CLAUDE.md canon |
| Published to the Google & YouTube channel | **15 products / 20 variants** |
| Merchant Center total | **21** = 20 from the feed + 1 found by Google |

**Deliberately not on the Google channel:** `senseless-cosmetics-bag` (£9.99),
`vitamin-a-d-ointment-4-pack` (£2.00), `build-your-own-bundle` (£0.01).

**Finding — the 21st item.** Merchant Center holds **Vitamin A & D Ointment (4 Pack), £2.00,
In stock, Approved**, product ID `vitamin-a-d-ointment-4-pack`, sourced from **"More found by
Google"** (automatic crawling), *not* the feed. A cart add-on that Shopify deliberately withholds
from the Google channel is therefore live in Merchant Center and approved for free listings. The
"Allow ads" prompt on that data source has **not** been accepted, so it is not ad-eligible today —
accepting it would make a £2.00 add-on biddable. Decide: archive it in Merchant Center, or accept it
as an organic free listing.

**Prices:** every Merchant Center row sampled matched Shopify exactly (Clinical Spray £19.99,
Professional Cream £55.99, Professional Spray £29.99, Clinical Gel 15ml £19.99, Advanced Cream 30g
£49.99). The subagent independently confirmed all 17 PDP Offer prices against the Shopify truth table.

**Feed item IDs are `shopify_ZZ_<product>_<variant>`**, while the theme emits
`productID: "shopify_GB_<product>"`. Already documented in
`senseless-structured-data.liquid:385-394` (study N30) — the `shopify_GB_` label corresponds to
nothing that exists. Cheap improvement: emit the real variant-level item ID, or drop `productID`.

---

## Merchant Center — state

- **Delivery policies survived overnight.** Still exactly 3, all **Complete**: 2–4 days (Price),
  4–7 days (Price), 1–2 days (Flat), UK, All products. The broken `Custom_rate_price_based` has
  **not** been recreated. Yesterday's Decision 12 fixes held.
- **Unit pricing issue is gone** from diagnostics — the 22 Sep fix cleared it.
- **Setup and policy issues: none.** "No issues for you to fix."
- **Products:** 15 Approved, 6 Limited, 0 Not approved, 0 Under review.
- **The only remaining issue is "Personalised advertising: Personal hardships" — 6 products
  (28.6%)**, which the founder has already ruled to leave. For the record it is now the *sole* cause
  of anything being Limited: Clinical Gel 35ml, Clinical Cream 10g, Clinical Cream 30g, Advanced
  Cream 10g, Advanced Gel 15ml, Advanced Gel 35ml.
- **Shop quality:** Overall *Great*, Delivery time *Good*, Delivery cost *Good*.
- **Risk carried over:** the Google & YouTube app's "Shipping Information" sync is **On**, and
  Shopify's two free rates still have **no transit time** set. See `NEXT_SESSION.md` §2(c).

---

## Google Ads — state

Last 7 days: 269 clicks · 21.2K impressions · avg CPC £0.84 · cost £225 · conv. value 235.89.
Active daily budget **£115/day**.

| Campaign | Budget | Status | Type | Bidding |
|---|---|---|---|---|
| Shopping - All products | £40.00 | **Paused** | Shopping | Target ROAS |
| Seneseless Search | £20.00 | Eligible — **some ads limited by policy** | Search | **Manual CPC** |
| PMax: Shopping - Cream | £25.00 | Eligible | Performance Max | Target ROAS |
| Search - Microneedle | £40.00 | Eligible | Search | Target ROAS |
| Search - Tatoo Numbing | £20.00 | Eligible (Limited) — bid setting limited | Search | Maximize clicks |
| Pmax - Spray | £10.00 | Eligible | Performance Max | Target ROAS |

**Account alerts open:** **"Apply for healthcare certification"** and **"Experiment paused"**.
The healthcare-certification prompt is the §5D item carried since 4 Sep — it lives in Ads, not
Merchant Center.

**Conversion tracking:** exactly **one** conversion action — `Purchase`, source *Website*, tracking
**Active**, optimisation **Primary**, count *Every*, 30-day click-through window, included in
account-level goals. 6 conversions / £235.89 in the last 7 days. No secondary actions (Add to cart,
Begin checkout are suggested but not created). Conversion diagnostics: *Not applicable*.

**Ads and the injectable rule.** There is a **"Lip Fillers & Injectables" ad group** in the
*Seneseless Search* campaign with the ad *"Lip Filler Numbing Cream | Numb Before Your Filler"*,
display path `/numbing-cream/lip-fillers`. It is **Paused** and **"Limited all locations"** — the
policy limitation that produces the campaign's "some ads limited by policy" status. Nothing is
serving. **Landing pages over the last 30 days contain zero injectable collections** (8 URLs: 5 PDPs
plus `numbing-spray`, `numbing-cream-for-waxing`, `numbing-cream-for-semi-permanent-makeup`), so the
paid-side invariant holds today. Paused ≠ deleted: if that ad group is ever re-enabled it becomes an
ad-facing injectable surface.

**Commercial gap.** The Shopping campaign that covered *all products* is paused, and the two PMax
campaigns cover only **Cream** and **Spray**. Gels, the Foaming Cleanser and all five bundles have no
Shopping coverage at all, despite being approved in Merchant Center.

**Naming / hygiene:** campaign **"Seneseless Search"** (misspelt), campaign **"Search - Tatoo
Numbing"** (misspelt), ad display path **`/numbing-cream/tatoo`** (misspelt, customer-visible).
Display URL host is inconsistent — some ads show `senseless.uk`, others `www.senseless.uk`. One
Search campaign still runs **Manual CPC**.

---

## Search Console — what Google reports

| Report | Result |
|---|---|
| **Merchant listings** | **94 valid, 0 invalid.** All four "improve appearance" issues — missing `hasMerchantReturnPolicy`, missing `shippingDetails`, multiple aggregate ratings, missing `description` — now show **Passed / 0 items** |
| **Product snippets** | **94 valid, 0 invalid.** Non-critical: missing `aggregateRating` (89), missing `review` (89) |
| **Manual actions** | **No issues detected** |
| **Indexing** | **62 indexed / 108 not indexed** |
| Performance | 77 web search clicks (3 months) |

**This closes the three GSC "Validate fix" items carried since 4 Sep** — they have passed.

**Not-indexed breakdown (108):** blocked by robots.txt 48 · alternate page with proper canonical 13 ·
excluded by `noindex` 12 · page with redirect 5 · not found (404) 1 · **crawled – currently not
indexed 16** · **discovered – currently not indexed 12** · blocked by unauthorized request (401) 1.
The first group is normal Shopify hygiene; the **28 crawled/discovered-not-indexed** pages are the
real signal and are worth a content pass.

---

## Other findings (from the two live audits)

**Indexing / crawl**
1. **Unbounded `?page=N` crawl space.** `/collections/shop-all?page=500` returns **200** and
   self-canonicalises to `?page=500`, rendering the identical 17 products. `robots.txt` blocks
   `sort_by` and `filter` but **not** `page=`. Mitigating: page 1 renders no pagination links, so
   on-site discovery is nil. Fix: `Disallow: /collections/*?*page=`.
2. **`/blogs/guides` is `noindex,follow` but is submitted in `sitemap_blogs_1.xml`** — the only
   noindex URL among all 74. Search Console raises this as an error. `/pages/articles` is the
   indexable hub with the identical 12 articles. Pick one deliberately.
3. **Every product `<lastmod>` equals the moment of the request** — all 18 entries share one
   timestamp that tracks the clock (11:36:08, 11:48:38, 11:49:01 across three fetches). Google
   ignores `lastmod` site-wide when it looks untrustworthy. Pages, collections and blogs have sane
   varied dates, so this is isolated to products.
   **CLOSED 23 Sep — confirmed Shopify platform behaviour, no action available to us.**
   The original "Admin/app investigation" diagnosis was **wrong** and is retracted: `updated_at` via
   the Admin API is stable and varied (1–23 Sep), so nothing is touching the products. Re-measured
   without any cache-busting or `no-cache` header, with a Googlebot UA, to rule out my own method:
   15:40:28 → all 17 stamped `15:40:28`; 15:41:13 → all 17 stamped `15:41:13`; the pages sitemap at
   the same moment returned 20 distinct real dates. Both files are uncached (no `Age`, no
   `Cache-Control`, unique `X-Request-ID`). The product sitemap is also the only one carrying
   `<image:image>` blocks — a separate renderer. No vendors/markets/stores sitemap exists on this
   store (404), so the full comparison set is products vs pages vs collections vs blogs.
   **Raised with Shopify Support 23 Sep** (live chat, advisor *Iqra*; chat reference to follow by
   email). Outcome, in their words: the first-tier assistant called it "a known characteristic of how
   Shopify generates its product sitemaps … set dynamically at request time", "platform-level
   behaviour with no merchant-facing setting to change it", and conceded there is **no public
   documentation** for it and that the products-vs-other-types difference "isn't something documented
   as intentional". The advisor **confirmed in writing that there is no merchant-side setting
   affecting product sitemap `lastmod`**, could not confirm whether the behaviour is intentional
   (no visibility into the renderer), stated there is **no escalation path to engineering** for a
   non-urgent, no-customer-impact issue, and **logged it as product feedback** to the team that owns
   sitemap generation.
   **Workaround for genuine changes:** Search Console → URL Inspection → Request indexing on the
   changed product URL. Manual, but it bypasses `lastmod`, and at 17 products that is trivial.
   **Note for honesty:** we have *not* observed an actual delay in Google reflecting product changes;
   this was raised as a data-correctness point, and Support was told so explicitly.

**Structured data** (173 JSON-LD blocks over 72 URLs, 0 parse failures, validator 0/0 on six pages)

4. **Five multi-variant PDPs expose only the cheaper variant to Google.** `?variant=` URLs emit the
   correct Offer but canonicalise to the base URL, and only base URLs are in the sitemap. So
   £44.99 clinical cream 30g, £49.99 advanced cream 30g, £34.99 clinical gel 35ml, £39.99 advanced
   gel 35ml, £44.99 professional gel 35ml — and the valid GTIN-13 on clinical gel 35ml — are
   structurally unindexable. Merchant Center is unaffected (the feed carries per-variant URLs). Fix:
   `ProductGroup` + `hasVariant`, keeping the selected variant's Offer. This touches exactly what the
   22 Sep fix guarded, so it needs its own session and an MC re-check.
5. **HTML entities leak into JSON-LD strings — 33 occurrences** (`&amp;`, `&#39;`). JSON-LD inside
   `<script>` is not HTML-parsed, so Google reads them literally. Root causes: `page_title` /
   `page_description` (Shopify pre-escapes) and `product.description | strip_html`.
6. **Duplicate, conflicting `#webpage` node on 12 pages** — `sections/senseless-page-schema.liquid`
   re-declares the sitewide `@id` with a different `name`/`description`.
7. **`priceValidUntil` missing on every Offer** (0 of 173) — recommended for Merchant listings.
8. **Organization is thin:** no `sameAs` anywhere, `@type` is `Organization` rather than
   `OnlineStore`, no organization-level `hasMerchantReturnPolicy`.
   **Items 5–8 FIXED AND LIVE 23 Sep (`7224825`, lock `84efe3f`).** Census of all 74 sitemap URLs,
   before → after: entity leaks 34 → **0** (the true count; 33 above was one short); run-together
   sentences in FAQ answers 20 → **0** (same root cause, found in this pass); Offers with
   `priceValidUntil` 0/188 → **188/188**, all `2027-12-31` (31 Dec of next year, not now+365, so it
   changes once a year); pages with conflicting `#webpage` 12 → **0** (plus `/pages/contact`, outside
   the sitemap); Organization now `["Organization","OnlineStore"]`. One shared helper,
   `snippets/senseless-jsonld-text.liquid`, decodes `&amp;` LAST and leaves `&lt;`/`&gt;` encoded
   because `/search` titles carry the visitor's query. validator.schema.org 0/0 on 12 live pages; the
   22 Sep price guard holds on all 39 PDP URLs; Judge.me injects nothing in a real headless render;
   ad-facing invariant 0 breaches in both passes. **Not done, on purpose:** the organisation-level
   `hasMerchantReturnPolicy` waits for Legal to sign off the returns wording (study 2026-09-20 step 7,
   N38), and `sameAs` stays empty until a profile exists.
9. **A 2.0-star rating from a single review is live** on `/products/professional-strength-gel`
   (£29.99). Genuine data, but SERP-facing off a sample of one. Reviews are under legal hold — change
   only the emission threshold, never the reviews.
10. **Dead rich-result types:** `HowTo` (retired 2023) and `FAQPage` on 50+ surfaces (restricted to
    government/health sites since Aug 2023). They earn nothing in Google. Worth flagging to the
    source auditor separately: those FAQ answers are brand-authored copy at scale, so the compliance
    surface is wider than what is visible on the page.
11. **Dead emitters still in the repo** — `sections/header.liquid`,
    `sections/product-information.liquid`, `featured-product*.liquid` would emit a duplicate
    Organization / Product. No template references them. Delete before someone re-enables them.

**Copy / source-side (Daniel's lane, flagged not asserted)**
12. `<title>` on `/pages/strongest-numbing-cream` reads *"Strongest Numbing Cream UK — An Honest
    Guide | Senseless"*. `docs/COMPLIANCE.md` lists "Strongest numbing cream" under *Don't write*,
    but the replacement ("most concentrated") is marked **PENDING founder ruling**. Only hit in 146
    title/description strings scanned.

**Nits:** 10 pages with over-length titles/descriptions (zero duplicates across 73 URLs) ·
`lang="en"` rather than `en-GB` · `http://www` takes two redirect hops.

---

## Verified clean

Store gate · all 74 sitemap URLs return 200 (zero redirects, zero 404s) · robots.txt blocks nothing
Googlebot needs, and the `adsbot-google` group leaves Ads landing-page crawling unimpeded · all 73
indexable pages self-canonical, absolute, https, correct host · `?variant=`, `?sort_by=`, `?filter.`,
`utm_*`, collection-scoped product URLs and trailing slashes all canonicalise correctly · the
collection-scoped *injectable* product URL does not leak into the canonical · `/collections/all` is
noindex and absent from the sitemap · no cloaking (Googlebot vs desktop UA byte-identical) · OG /
Twitter complete on every page · 164 PDP images, 0 missing alt · no render-blocking third-party JS ·
gzipped HTML 82–110 KB · Judge.me injects no competing JSON-LD (confirmed in a real headless render)
· GTIN-13 check digits valid on all three barcodes · shipping-band selection correct on every offer ·
`cutoffTime` renders `15:00:00+01:00` · MerchantReturnPolicy complete · **ad-facing anchor invariant
intact: 9 pages, 15 anchors, 0 breaches — exactly the 2026-08-06 baseline**.

---

## Open / not verified

- **Barcodes:** only 3 of 22 variants have one (`S15CL`, `S35CL`, `SFOAM`). GS1 UK barcodes for the
  remaining 19 are still a founder task.
- **Whether GA4 is linked to Ads** — not checked (the Ads↔Merchant Center link is confirmed by MC
  showing Ads campaign stats).
- **Google Rich Results Test** has no public API; schema.org's validator was used instead, which does
  not enforce Google's required/recommended field lists.
- **Judge.me's own rich-snippet setting** — confirmed it injects nothing today; not confirmed OFF in
  the Judge.me admin.
- **`cutoffTime` after BST ends** — cannot be observed from September.
- **Ads account is signed in as `senseless.tattooing@gmail.com`**, while the Shopify Google & YouTube
  app links Merchant Center via `peter@matrixhealthgroup.co.uk`. Worth reconciling under the §5D
  account-holder question.
- Live default variant is the **smaller** size on `clinical-strength-cream` and
  `clinical-strength-gel`; `DECISIONS-LOG.md:174` records "Default variant = larger size …
  clinical-cream 30g already done". Live disagrees with the log.

---

## Recommended order

1. **P0 injectable breadcrumb** — one line, regulated risk, also closes the latent risk on 12 products.
   Widen the ad-facing rule's check method in the same change.
2. ~~Product `lastmod` = request time~~ — **CLOSED 23 Sep.** Confirmed Shopify platform behaviour;
   no merchant-side setting exists, logged by Support as product feedback. See the finding above.
3. **`Disallow: …page=`** and the `/blogs/guides` noindex-vs-sitemap decision — minutes each.
4. ~~**Entity unescape, `priceValidUntil`, duplicate `#webpage`, Organization → `OnlineStore`**~~ —
   **DONE 23 Sep (`7224825`)**; org-level return policy held for Legal. Originally: batch
   as one schema-quality deploy.
5. **`ProductGroup` / `hasVariant`** — the biggest upside; own session, MC re-check afterwards.
6. **Ads hygiene** — campaign/display-path spellings, Manual CPC, the paused Shopping campaign vs the
   Cream/Spray-only PMax coverage, and a decision on the crawled Vitamin A&D item.
7. **Founder/source calls** — healthcare certification, "strongest" title, aggregateRating threshold,
   GS1 barcodes.

*Read-only audit. No file was edited, nothing was deployed, no Shopify or Google setting was changed.*
