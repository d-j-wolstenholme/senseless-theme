# Senseless.uk Google Ads & Merchant Centre audit: study

**Date:** 21 Sep 2026
**Source:** `docs/evidence/google-ads-merchant-centre-audit-2026-09-20.pdf`, 7 pages, public-site snapshot of 20 Sep 2026. It is byte-identical to `~/Desktop/Senseless-Google-Ads-Merchant-Centre-Audit.pdf` (sha1 `0d4510d613f92ffe78829a63584ffc8c4cf42dfa`) and is committed with this study.
**Method:** 9 read-only verification lenses, one synthesis, then a skeptic pass. The skeptic re-checked 25 load-bearing claims and they held. It found 12 errors and 7 gaps, all applied below. Nothing was written to Shopify, Notion or git during the study, and nothing was deployed. Evidence comes from:
- live senseless.uk, fetched 21 Sep with cache-bust and a browser user agent, plus headless Chrome where a render is claimed;
- the repo at `7e944a3`;
- Notion canon, read only;
- official Google, GOV.UK, MHRA and legislation.gov.uk texts.

**Line references to `NEXT_SESSION.md`** are to the handoff as it stood at `5ce0026`, before this session rewrote it.

**Checked by one lens only (the skeptic did not re-check them):** V24's "tube reads ADVANCED STRENGTH", N35 (Klaviyo covering the banner at about 7s) and N19 (sticky price, source-only). Treat them as single-source until the browser checks in §5A item 1 run.

**What the audit is.** An outside review of the public website only. It had no access to Merchant Centre, Google Ads, Shopify admin, Search Console or checkout. It says so, and it treats every account-side effect as conditional.

**Terms used once:**
- **MC**: Google Merchant Centre.
- **PMax**: Performance Max.
- **PDP**: product page.
- **JSON-LD**: the structured data in the page.
- **Compare-at**: Shopify's "was" price.
- **G&Y channel**: Shopify's Google & YouTube app.
- **Canon**: the Notion records that are the source of truth.
- **Ad-facing**: pages paid traffic may land on (`.claude/rules/ad-facing.md`).
- **Reviews-guard**: the lock that protects Judge.me markup on deploy.
- **CCR 2013 / CRA 2015**: the Consumer Contracts Regulations and the Consumer Rights Act.
- **GN8**: MHRA Guidance Note 8.

**Owner key:**
- **CC**: Claude Code (theme, schema and copy implementation).
- **Founder**: Daniel (content-language and business calls).
- **Legal**: MHG/legal (legal and borderline calls).
- **Account holder**: whoever holds the Senseless Google Ads and MC logins (Peter or Daniel). The ads are run by the agency Colossal Search, contact Martin. Our standing rule is that Ads is audit-only.

## Bottom line

- **What the audit could see, it got right.** Its catalogue, offer, GTIN-count, shipping-schema and returns-wording facts all hold live on 21 Sep: 17 products, 22 variants, and all 22 offers match. Two points are imprecise but not wrong: the Product-level SKU follows the selected variant, and the Clinical Gel GTIN switches with `?variant=`.
- **The most important finding is one the audit couldn't see: visitor consent has never been recorded.** Since 1 Jun the cookie banner has sent `sale_of_data` as a text string. Shopify rejects it on every Accept and Reject.
  - As a result, GA4 and the pixels gated by Shopify consent (the MC tag and Shopify customer-events pixels) never receive consent.
  - Klaviyo's onsite script is not consent-gated at all. It loads and sends `track-analytics` before any choice and after Reject (observed). Clarity runs after Accept through the theme's own gate.
  - Meanwhile the agency's Google Ads purchase pixel runs before any choice and after Reject.
  - The theme fix is one line and is ours. The pixel permission, the PECR (UK cookie law) position and the timing are not.
- **For ads, the biggest unknown is Google's product category.** Canon closed the cosmetic classification on 2 Jul. The audit brings no product-specific evidence to reopen it. Google's category is a separate question and it is open: an "Apply for healthcare certification" alert has been on the Ads account since at least 4 Sep. Only the account holder can read what it names. If Google treats the range as over-the-counter medicine, rewording the site won't fix that.
- **Nobody on our side can see Merchant Centre.** Every check on pp.5–6 waits on the account holder: obsolete items, price and sale price, GTIN diagnostics, spend by item. Our records name two MC accounts. The Google & YouTube app's store widget on senseless.uk is configured with MC `5805726847`, observed on every page on 21 Sep. Records once noted that account as "0 products synced". Still unknown: whether Ads `368-965-4782` links to `5805726847` or to `5653174667`, and where the Shopping/PMax items come from. §5D has the checklist.
- **Identifiers are the clearest feed win.** The owner's barcode sheet has GS1 UK codes for 16 of the 22 variants. None are in Shopify, and the 3 barcodes that are live are old US-range codes. This needs a founder decision after a pack scan, then a data write. No theme change is needed.
- **Three items go to Legal, not us:**
  - Returns wording. The UK 14-day right to cancel appears nowhere. A paragraph stating it was removed on 6 Jun with no recorded legal decision.
  - Imported Totally Numb reviews. Of the 59 reviews on product pages' first page, 55 are pre-launch imports, and their provenance badge is hidden. The full corpus is at least 235, and the imported share can't be counted from the public page. The imports drive three structured-data ratings (Professional cream 4.88/207, Advanced cream 4.92/12, Clinical cream 4.85/13) and the homepage "4.9 / 5 · 230+ reviews".
  - Classification evidence canon never recorded: the clove-oil SmPC and MHRA GN8 wording. It is not new since the 2 Jul closure. It existed before and canon doesn't show it was considered.
- **The rest waits on founder calls:**
  - One meaning for "Strength". The hidden line "not a measure of strength" is on 37 pages.
  - Whether "bundles are never on sale" extends to Google Shopping. All 5 bundles still carry a compare-at price, which probably syncs to Google as a sale price.
  - Whether the injectable rule covers text as well as links.
- **The shipping markup overstates free delivery.** `eligibleTransactionVolume` isn't a valid property where we use it, so Google probably reads two unconditioned £0 options on every offer. The fix has two parts: account-level shipping in MC (account holder; it outranks markup) and a schema restructure (us).

## 2. Verdict table

Verdicts:
- **Confirmed**.
- **Confirmed, understated**: true, and worse than the audit says.
- **Partly confirmed**.
- **Not verifiable publicly**: needs account access.
- **Closed in canon**: settled by a recorded decision; the audit brings no new evidence.
- **Agreed**: a recommendation rather than a factual claim.

| # | Audit claim (page) | Verdict | Evidence (short) | Owner | Ad impact |
|---|---|---|---|---|---|
| V1 | p1 · 17 products, 22 variant Offers; schema prices and stock match the catalogue | Confirmed | `/products.json` on 21 Sep has 17/22. Joining JSON-LD Offers to variants by SKU: 22/22 match | — | None |
| V2 | p1 · Strongest confirmed concerns are strength positioning and returns wording | Confirmed, incomplete | Both hold (V23–V32). The consent failure (V53) and review provenance (V39) belong beside them | — | — |
| V3 | p1 · Priority order: classification → returns → MC → identifiers → shipping/measurement | Agreed, with changes | Do the account-side reads first (healthcare alert, MC access, conversion set-up). They are cheap and they decide what the rest means. Add the consent fix | Founder | — |
| V4 | p1 · The "many old MC products" report concerned Totally Numb, not Senseless | Confirmed | The Desktop TN PDF is a separate document with no "Senseless" in its text. Nothing from it reached the repo, Notion or live tags. The public sitemap and `/products.json` hold the same 17 handles. MC contents unknown | Account holder | Unknown |
| V5 | p2 · All 17 PDPs have Product markup with populated descriptions | Confirmed | One Product node per PDP; descriptions are 66–218 chars. Minor: the ointment description contains a literal `&amp;` | CC | None |
| V6 | p2 · 22 Offers match price and InStock, URLs carry the variant ID, no AggregateOffer (incl. the Advanced Cream and Clinical Gel examples) | Confirmed | 22/22 on price, GBP, InStock and `?variant=<id>`. 0 AggregateOffer on the 17 PDPs | — | Low |
| V7 | p2/p3 · All 22 variants available (not a stock audit) | Confirmed | `available=true` ×22; public data only | — | None |
| V8 | p2 · Advanced Starter SBUN3 £84.99: check how the feed treats sale price | Confirmed risk; feed not visible | All 5 bundles carry a compare-at (SBUN3 £94.96 is the four-item sum and has never been the selling price). The 1 Sep ruling removed on-site sale styling but kept the data. Google says Shopify compare-at syncs to MC as sale pricing (MC help 15474557) | Founder + account holder; Legal only if a Shopping sale is kept | Medium |
| V9 | p2 · Three gtin13 values, all 13 digits and check-digit valid | Confirmed, but probably superseded codes | Check digits valid. All three are zero-padded US-range UPCs (076…/079…). The owner's barcode sheet files them under "OLD BARCODES" with GS1 UK replacements | Founder | Medium |
| V10 | p2 · 19 Offers omit GTIN; don't invent codes or set `identifier_exists=false` | Confirmed | 19 empty barcodes; the breakdown is exact. The owner's sheet has GS1 UK codes for 13 of those 19 and none for VAD-4PK or the kits | Founder decides; CC writes | High |
| V11 | p2 · Public schema doesn't show what the feed submits | Not verifiable publicly | Schema matches Shopify barcodes on all 22 in both directions. A different GTIN in the feed would therefore mean a second source | Account holder | Unknown |
| V12 | p2 · Multi-size pages put the "first/default" SKU at Product level | Partly confirmed (imprecise) | Product sku/mpn/gtin follow the selected-or-first-available variant (`snippets/senseless-structured-data.liquid:353`), and switch on `?variant=` URLs | CC | Low |
| V13 | p2 · Clinical Gel puts the 15ml GTIN on the parent Product | Partly confirmed | True on the canonical URL. On `?variant=<35ml>` the same `#product` @id carries the 35ml GTIN | CC | Low |
| V14 | p2 · Less explicit than ProductGroup; review against Google variant guidance | Confirmed (a modelling concern only) | One Product with N Offers; no ProductGroup or hasVariant. No GSC variant issue on record. The snippet is reviews-guard-locked (Judge.me fix 66aa9b8, @id wiring b19e710) | Founder (priority); CC | Low |
| V15 | p2 · Selected-variant rendering not fully tested | Tested server-side; mostly works | All 5 second-size URLs server-render the right size radio, price, sticky price, hidden variant id and SKU/GTIN. Gaps: `og:price:amount` stays at the lowest price, and both sizes share one image. Add-to-cart and the visual render were not observed | CC | Low |
| V16 | p2 · Shipping schema £1.99/£3.99/£8.99, free standard from £40, free next day from £80; delivery page agrees | Confirmed | The 5 nodes match the 13 Jul rate card (Decision 39c58bc3-75ea-81fe) and `/pages/delivery`. `/policies/shipping-policy` and `/pages/shipping-delivery` leave out Express and all paid prices | Founder (copy); CC | Low |
| V17 | p2 · Thresholds use `eligibleTransactionVolume`; don't assume Google reads it | Confirmed, understated | It is not a schema.org property of OfferShippingDetails (schema.org allows it only on Demand, Offer and PriceSpecification); the Schema Markup Validator flags it as UNKNOWN_FIELD. It is used 5 times, so re-run the validator before quoting a warning count. Google documents thresholds only through Organization `ShippingService`/`ShippingConditions`. Probable effect (inferred): two unconditioned £0 options on every offer | Account holder (MC shipping); CC (schema) | Medium |
| V18 | p2 · Checkout totals not tested | Not verifiable publicly | The only recorded test is 13 Jul at £30/£55/£85. Nothing at £39.99/£40/£79.99/£80 | CC (needs Admin API) | Unknown |
| V19 | p2 · Return schema: GB, 30 days, customer pays; misses page exceptions | Confirmed | Misses at least 8 exceptions, including free returns for faulty items and the sale-items exclusion | Legal → CC → account holder | Low |
| V20 | p3 · 22-row product/size/SKU/price table | Confirmed | 22/22 rows match live. "Single item" is the audit's wording; Shopify's variant title is "Default Title" | — | None |
| V21 | p3 · Five two-size products; Professional cream 30g only; kits are separate products | Confirmed | `/products.json` | — | None |
| V22 | p3 · Join MC to Shopify by SKU + product/size + URL | Confirmed | Expected MC IDs are `shopify_ZZ_<product_id>_<variant_id>` (the G&Y pixel has `target_country: "ZZ"`). Join on live SKUs, because some internal registries hold old codes | Account holder | Medium |
| V23 | p4 · System page sells by strength yet says the tiers are "not a measure of strength" | Confirmed, understated | The disclaimer comes from 2 snippets and appears on 37 of the 73 sitemap pages: the homepage, the System page, all 17 PDPs (the bag, ointment and cleanser get it through a related-product card) and 18 collections. It is screen-reader-only, so sighted visitors see only "Strength". Added 21 Jun (4bc9e9e); not swept after the 1 Sep "keep Strength" ruling | Founder decides; CC | Low |
| V24 | p4 · Advanced Cream: Strength title + "higher-strength" + disclaimer | Confirmed | `/products/advanced-strength-cream`: H1 "Advanced Strength Cream", "A higher-strength formula". The product image tube reads "ADVANCED STRENGTH". Screen readers hear the hidden disclaimer just before the H1 | Founder; CC | Low |
| V25 | p4 · Establish what differs between formulas; one explanation for pages, packs, feed and ads | Confirmed gap | No record anywhere says what differs. Canon holds three incompatible definitions (Decisions 38e58bc3-75ea-817f and -817c; `docs/COMPLIANCE.md:53,64`). The pack and the feed say "Strength"; only page text disagrees | Founder + formulator; Legal if "strength" means potency | Unknown |
| V26 | p4 · Presents itself as cosmetic and CPSR-assessed while recommending use before injections, tattoos and so on; formulation details "on the packaging" | Confirmed | The quotes are live on `/pages/the-senseless-system` and `/pages/faq`. 0 PDPs list ingredients (the founder decided on 14 Aug not to publish INCI) | Founder (INCI); Legal | Medium |
| V27 | p4 · Get ingredients, concentrations and the classification rationale; a CPSR alone doesn't settle medicinal status; MHRA weighs presentation and function | Closed in canon; the audit brings no product evidence | Decision 39158bc3-75ea-8194 (2 Jul) records cosmetic status on the founder's statement. Canon already accepts "CPSR ≠ claims permission". Our own checks found evidence that existed before the closure but is not recorded in canon (N6), which goes to Legal | Legal | High |
| V28 | p4 · Google healthcare rules are separate; UK OTC Shopping needs GPhC registration + Google certification; find the category first | Confirmed; open | Policy text verified (MC 6150151, Ads 176031). The "Apply for healthcare certification" alert on the Ads account has been unresolved since at least 4 Sep. Google's assigned category can only be seen in the account | Account holder + Legal | High |
| V29 | p4 · Returns page excludes sale items, requires unopened original packaging, says 10 working days, frames the 14-day cooling-off as EU-only | Confirmed word for word; not closed | Same text on `/pages/returns-refunds` and `/policies/refund-policy`. No page gives a right to cancel, a model form or a statutory-rights reminder. No legal sign-off is on record | Legal | Medium |
| V30 | p4 · The sealed-hygiene exception is narrower than "no opened goods", including for the bag | Confirmed | CCR 2013 reg 28(3)(a) covers goods sealed at delivery and unsealed afterwards. It can't cover the bag, whose PDP says the site policy applies. No copy says the topicals are sealed | Legal; MHG ops (seal facts) | Medium |
| V31 | p4 · Clarify statutory refund deadlines | Partly confirmed | "10 working days" can run past reg 34's 14 days over bank holidays. Refunding the original delivery charge isn't mentioned | Legal | Low |
| V32 | p4 · Set out faulty-item rights separately | Partly confirmed | A faulty-item section exists and the postage rule is lawful. But there is no statutory/CRA mention, and the delivery pages set a 14-day reporting deadline (N21) | Legal | Low |
| V33 | p4 · Misrepresentation review can weigh policy presentation; no evidence of suspension | Not verifiable publicly | No public sign of refused refunds or MC action | Account holder | Unknown |
| V34 | p4 · System page and FAQ promote injectable procedures | Confirmed, wider | On the ad-facing System page, the Selector offers "Lip fillers" and "Botox" and there is an injectables table. Three other ad-facing pages name injectables in text (N9). The link rule holds: 0 breaches across the sitemap | Founder (rule scope); Legal | Medium |
| V35 | p4 · Sensitive-health audience limits for remarketing and Customer Match; not a Search/PMax ban | Confirmed (policy); labels are account-only | Ads policy 16701855 lists injections and bars advertiser-curated audiences | Account holder | Medium |
| V36 | p4 · Check support for efficacy claims | Partly confirmed | Brand ad-facing copy has 0 medicinal verbs. The efficacy language sits in reviews. Of the 59 reviews on PDP first pages, about 10 describe no pain (pain-free, painless, no pain) and about 12 say they felt nothing. The full corpus (at least 235) was not counted. A few tier-performance lines also imply it | Founder; Legal (reviews) | Medium |
| V37 | p4 · Check support for duration claims | Closed in canon | FAQ onset and duration wording is the legal-verbatim exception. The PDP 45–60 line has its own Decision (39158bc3-75ea-81f7). Reviews are left as they are (39158bc3-75ea-8149). Two PDP strings flagged on 12 Aug are still unruled (N13) | Founder | Low |
| V38 | p4 · Check support for "antibacterial" | Closed in canon | Confirmed Fact 3b358bc3-75ea-8153 (6 Aug): substantiation is on file. The audit brings no new evidence | Founder (keep the file to hand) | Low |
| V39 | p4 · Inherited reviews must be about the same product and formula; don't delete genuine reviews | Confirmed, understated | Of the 59 reviews on PDP first pages, 55 are imports dated 2023–25, before launch; canon says they were ported from Totally Numb. The full corpus is at least 235 (207 on Professional cream), and the imported share can't be counted publicly. Their provenance badge is hidden. They drive three JSON-LD aggregateRatings (4.88/207, 4.92/12, 4.85/13) and the homepage "4.9 / 5 · 230+ reviews" (N4) | Legal; founder | High |
| V40 | p4 · Positive: contact details, business identity and delivery info are visible | Confirmed | The footer on every page has the company number, VAT number, address, phone and email | — | None |
| V41 | p4 · Positive: the FAQ and Professional Spray say unbroken skin | Confirmed, with a caveat | Three ad-facing collection FAQs say "Take extra care on sensitive or broken skin" (N17). Gate G2 is still open | Founder; G2 owner | Low |
| V42 | p4 · Positive: no sitewide AdsBot block | Confirmed | The `robots.txt` adsbot group blocks only checkout and cart-type paths. The AdsBot user agent gets 200 | — | None |
| V43 | p5 · Old approved items can keep serving | Not verifiable publicly | Needs MC/Ads access, which no one on our side has | Account holder | Unknown |
| V44 | p5 · Feed and destination mismatches cause disapprovals | Not verifiable publicly | The site side is consistent. Items to check: the bundle sale_price (V8) and the 5 second-size items | Account holder | Unknown |
| V45 | p5 · Automatic item updates don't retire old identities | Not verifiable publicly | An extra risk, not observed: on `?variant=` pages the Offer list still starts with the smaller size | Account holder | Unknown |
| V46 | p5 · A restricted category can bring item- or account-level enforcement | Not verifiable publicly | The healthcare alert exists. "Shopping - All products" was paused on 5 Aug. Impressions fell to about 0 from 21 Aug and the cause is unrecorded; don't assume a link | Account holder | High |
| V47 | p5 · Missing or wrong identifiers limit eligibility | Not verifiable at feed level | GS1 UK codes exist but aren't loaded (V10) | Account holder; founder | Medium–high |
| V48 | p5 · New IDs after a migration leave old records behind | Not verifiable publicly | The old store `senseless-tattooing.myshopify.com` still exists (302 → /password). A second submitter is a hypothesis to rule out | Account holder; founder | Unknown |
| V49 | p5 · PMax reaches pages through feed URLs and through URL expansion or text customisation | Confirmed (mechanism) | Google Ads help 14337539. With expansion on, PMax could land on the indexable, organic-only injectable collections. No record checks this | Account holder/agency; founder | Medium |
| V50 | p5 · Old items alone prove neither spend nor penalty; no account metrics available | Agreed | Our read-only audit of 4 Sep has metrics. From 5 Aug to 3 Sep, spend was £1,243.14 and Ads recorded £505 of conversion value from 13 purchases (ROAS 0.41). Total store revenue across all channels in the same period was £921.08, so even full attribution would give only 0.74. PMax "Shopping - Cream" cost £101.77 per conversion on an average order of about £38 | Founder (questions to Martin) | High |
| V51 | p6 steps 1–3 · Export current and obsolete listings, find out why they persist, prove spend | Agreed | Checklist in §5D. Blocked: "neither signed-in Google account has access" (`NEXT_SESSION.md:13`) | Account holder | High |
| V52 | p6 step 4 · Fix the confirmed website issues | Agreed, with additions | Covered in §5A–C. Add the consent fix and review provenance | CC / founder / Legal | — |
| V53 | p6 step 5 · "Measurement configuration and consent controls were present" | Partly confirmed: present but not working | The banner sends `sale_of_data: c.marketing ? 'enabled' : 'disabled'` (`snippets/senseless-cookie-consent.liquid:127`, re-read 21 Sep). The Storefront API rejects it with "Expected type 'Boolean'". After Accept, consent is still unset and no GA4 request fires (observed in headless Chrome) | CC (fix); founder (timing) | High |
| V54 | p6 step 5 · No visible AW tag doesn't prove tracking is broken | Confirmed | AW-18228180367 runs in a custom-pixel sandbox that anyone can fetch. It loads, pings Google and sets `_gcl_au` before any choice and after Reject (observed) | Legal; Shopify admin holder | High |
| V55 | p6 step 5 · Test a purchase and refund; GA4-imported vs native conversions; one primary | Not verifiable publicly | Both pixels dedupe on the order ID. Their values differ: Ads counts the total including shipping and VAT, GA4 counts the subtotal. Neither handles refunds. Any GA4 import is dormant now and would start counting after the fix | Account holder; CC | Medium |
| V56 | p6 step 6 + completion criteria · Resubmit, monitor, done-when list | Agreed | Mark the date of the consent fix as a break in measurement | Account holder | — |

## 3. What the audit got right, got wrong, or couldn't see

**Right**
- Every catalogue and offer fact (V1, V5–V7, V20–V21).
- It kept confirmed facts apart from conditional ad mechanisms, and refused to carry Totally Numb's allegation over to Senseless (V4).
- The strength contradiction and the returns wording are both real.
- The `eligibleTransactionVolume` caution and the GTIN caution ("never fabricate identifiers").
- The remediation sequence on p6 is sound. It becomes our account checklist (§5D).

**Wrong or imprecise.** Nothing material is factually wrong. These points are imprecise or understated:
- The "first/default SKU" at Product level is actually the selected-or-first variant (V12–V13).
- **Understated:** `eligibleTransactionVolume` is invalid where it's used, not just possibly ignored (V17). The strength disclaimer is sitewide and hidden from sighted users (V23). The reviews were imported from another brand, not just "inherited" (V39). Injectable mentions go beyond the System page and FAQ (V34).
- "Consent controls were present" reads as reassurance. The controls don't work (V53).
- "Single item" is the audit's gloss for Shopify's "Default Title".
- "Describes itself as cosmetic": canon removed most of those lines on 14 Aug and 1 Sep, but survivors are live (N14), so the observation still holds.

**Couldn't see**
- **Account data:** MC, Ads, Search Console, Shopify admin and checkout.
- **Behaviour after a click:** the consent write failure and the AW pixel sandbox.
- **Our internal context:** the owner's GS1 barcode sheet; canon history (the 6 Jun returns removal, the 20 Jun comfort reposition, the 1 Sep rulings); the Ads metrics of 4 Sep; the healthcare alert.
- **Offline facts:** the physical packs and the formulation.

**Where the lenses disagreed, and which evidence wins**
1. **GTINs.** The catalogue lens said the licence was unknown. The identifiers lens found the owner's barcode sheet, which lists GS1 UK replacements. **Identifiers wins**, because it found the document that answers the question. The sheet isn't Senseless canon and no pack has been scanned, so the founder still confirms.
2. **Product-level SKU.** The catalogue lens said "confirmed" and the identifiers lens said "partly". **Identifiers wins**: it tested `?variant=` URLs and read the snippet at `:353`.
3. **Decision ID for the PDP 45–60 line.** One lens cited 38e58bc3-75ea-81ca and another 39158bc3-75ea-81f7. `docs/COMPLIANCE.md:40` names **39158bc3-75ea-81f7**, so that ID is used here.
4. **"Our most concentrated formula"** (live on the tattoos collection). One lens treated it as approved (`docs/COMPLIANCE.md:53`). Another said it is banned by Notion 38e58bc3-75ea-817c. The Notion decision outranks the repo doc, but 38e58bc3-75ea-817f, which defines the Scale as the strength axis, is also still Accepted. **Canon contradicts itself.** Don't treat the line as cleared until the founder rules.
5. **G1.** The classification lens called it unanswered, citing the body of Compliance Hold 3bb58bc3-75ea-8147. The owner closed it on 14 Aug (State Surface log; `NEXT_SESSION.md:186` "G1 is CLOSED — do not re-raise"). **The closure wins**: it is later and it is an explicit owner statement. G1 is not raised again here.
6. **Sale styling in search.** Every lens saw it in the served HTML and none saw it rendered. Treat it as confirmed in the markup and unconfirmed visually. The browser check in §5A settles it.
7. **Cookie consent cause.** Earlier records blamed a store/admin setting. The measurement lens reproduced the Storefront API error and the repo line reads as described. **The code evidence wins.**
8. **"Conversion tracking works" (4 Sep) vs "Ads is blind" (31 Aug).** Both are true, for different systems. The native AW pixel isn't consent-gated, so it records conversions. GA4 and Shopify's journey data are gated and never receive consent, so they record nothing.

## 4. Issues the audit missed

Deduplicated across the lenses. Severity is ours.

| # | Issue | Evidence | Severity | Owner |
|---|---|---|---|---|
| N1 | Cookie banner consent write fails on every click, and has done since 1 Jun | `snippets/senseless-cookie-consent.liquid:127` has sent a string since the first commit 91f3bbd. Storefront API: "Argument 'saleOfData' … Expected type 'Boolean'". After Accept, `analyticsProcessingAllowed=false` and there are 0 GA4 requests. This one cause explains the 1 Jun "consentManagement undefined" error, the 22 Jun banner re-show, the 8 Aug "event doesn't fire" note and 72 of 75 orders with no attribution | High | CC (fix); founder (timing) |
| N2 | Google Ads custom pixel 329908572 runs before consent and after Reject. **CLOSED 22 Sep 2026 by the founder: intentional, leave as is, do not re-raise** (DECISIONS-LOG 2026-09-22). The consent fix keeps `sale_of_data: true`, so the pixel's behaviour is unchanged | It declares `SALE_OF_DATA` only, although the 12 Jun record said "Required (Marketing+Analytics)". Observed: `gtag/js?id=AW-18228180367`, `ccm/collect … en=page_view` and cookie `_gcl_au` with no choice made and after Reject. No consent-mode call in its code. Google's EU user-consent policy covers the UK. The same PECR package should cover two more pre-consent calls: Klaviyo's onsite script (`a.klaviyo.com/onsite/track-analytics`, before any choice and after Reject) and the G&Y store widget's call to `google.com/shopping/merchantverse` | High | Legal (PECR); Shopify admin holder; agency told |
| N3 | GS1 UK barcodes exist for 16 variants but none are in Shopify | The owner's sheet (Drive `165V5aaEfCa3AWYv2Q5_Vxe-B5ImsJzP5NrJtaqQbyQk`, read only) has `5065028388xxx` codes for the 15 single SKUs and the bag, all with valid check digits, and files the 3 live codes as "OLD". Totally Numb made the same switch on 21 Sep (TN DEC-53). Sheet quirks: gel, spray and foam sizes are in "g"; gel SKU codes differ from Shopify's; the S35CL box dimensions look copied | High | Founder (after a pack scan); CC writes |
| N4 | Imported reviews: provenance hidden, they feed ratings, and their text shows signs of editing | Judge.me CSS sets `display:none` on the "collected from another provider" badge. The imports feed JSON-LD `aggregateRating` and the homepage figure. Professional cream (sold only in 30g) has reviews mentioning a "10g" and a "small tube". "Tattoo" appears 0 times and "procedure" 35 times in tattoo contexts. Brand artefacts: "Senseless numbing cream Senseless numbing cream", "numbs cream". A parcel-replacement thank-you is dated before launch. Rules in play: Google's review-snippet rule ("Don't aggregate reviews or ratings from other websites") and DMCC Act 2024 Sch 20 para 13. This doesn't prove who edited the text | High | Legal; founder supplies the Judge.me import and export |
| N5 | Statutory 14-day cancellation paragraph was removed on 6 Jun with no recorded legal decision | Added in Phase 13 (`build-reports/phase13-remediation.md:55`) and removed on 6 Jun (`build-reports/native-legal-policies.md`). Re-flagged on 6 Aug (`docs/SITE-ASSESSMENT-2026-08-06.md:96-100`) but never logged in Notion. If the CCR Sch 2(l) information isn't given, reg 31 extends the cancellation period by up to 12 months | High | Founder routes it and logs a hold; Legal decides |
| N6 | Classification evidence canon hasn't recorded (none of it is new since the 2 Jul closure) | (a) The Clove Oil BP SmPC (GSL, PL 12965/0006; emc text last revised 10/09/2014) says it "has local anaesthetic… properties", against canon's "the function test is weak against us". (b) GN8 §13 (Miscellaneous) has an entry headed "Topical anaesthetics (Numbing Gels/Creams)". It names lidocaine, prilocaine and epinephrine and does not mention eugenol or clove. Legal should read the full entry. (c) GN8 §5 (Advertising) lists "comparison with licensed medicines" among forms of marketing that may suggest a medicinal product, and the EMLA and Ametop pages are ad-facing comparisons. (d) GN8 Appendix 9 ("Testimonials"): where reviews make medicinal or implied medicinal claims, "these should be removed from public view as soon as possible". GN8 was published in September 2025, before the 2 Jul 2026 advice. Canon doesn't record whether Legal considered it | High | Legal |
| N7 | Bundle sale styling survives the 1 Sep "no sale styling anywhere" ruling | **Also `/collections/all`** (Horizon default `templates/collection.json` price block): all 5 bundles render `price__sale` with a struck compare-at (e.g. £84.99 with £94.96 struck) and 5 "Sale" badges (re-verified in served HTML, 22 Sep, during the records audit). A struck £94.96 on the Advanced Starter card in the search modal on all 70 pages fetched. "Sale" badges on `/search?q=ultimate&type=product` (`blocks/_product-card-gallery.liquid:12-22`, a visible class, not visually hidden). `/search/suggest` shows the same. Seen in served HTML; the visual render was not observed | Medium | Founder (scope); CC |
| N8 | Bundles carry a compare-at price, and the returns page makes "Sale items" non-returnable | Bundle PDPs and the return schema promise 30-day returns, yet the only products with a compare-at price are the 5 bundles | Medium | Founder + Legal |
| N9 | Injectables are named in text on ad-facing pages; the rule only covers links | Selector options and the matrix on `/pages/the-senseless-system` (`sections/senseless-selector.liquid:62`); `/pages/strongest-numbing-cream` (:35, :116); `/pages/senseless-vs-ametop` ("injectable work"); `/collections/aesthetic-numbing-cream` (:8, :282) | Medium | Founder (rule scope); CC |
| N10 | The Foaming Cleanser's breadcrumb JSON-LD names "Numbing Cream for Botox" as its parent | `snippets/senseless-breadcrumbs-jsonld.liquid:20` uses `product.collections.first`. There is no visible anchor, so the link sweep misses it | Low | CC (on a founder go) |
| N11 | A "Lip Fillers" tag is on 12 of 17 products and a "Botox" tag on 9 of 17 (all 5 kits, the ointment, the Foaming Cleanser, and the Clinical and Professional creams); both are public in `/products.json` | Harmless unless the G&Y channel maps tags into custom labels | Low | Account holder checks |
| N12 | Strength wording contradicts itself beyond the hidden disclaimer | Visible "peers, not a ranking" and "None is 'better'" sit beside "a step up" and "The considered upgrade". The ad-facing strongest-numbing-cream page says "Picking Professional doesn't make the appointment more comfortable" while the Scale is framed as a comfort level. `docs/COMPLIANCE.md:53,64` still approves "Our most concentrated formula", so `compliance-check` would pass wording canon bans | Medium | Founder; CC (docs pass) |
| N13 | Two PDP strings flagged on 12 Aug are still unruled | "the tiers are formulated to match the session lengths they're built for" (near the banned duration axis) and "get their best results" (an efficacy word) (`docs/TATTOO-BEAT-THEM-PLAN-2026-08-12.md:309-312`) | Medium | Founder; Legal if borderline |
| N14 | Classification lines are still live after the 14 Aug and 1 Sep removals, in two groups | (a) **Held GREY on purpose for Daniel on 1 Sep** (DECISIONS-LOG) and awaiting his ruling: the comparison pages and "Numbing is a cosmetic preparation that supports comfort" (live on the injections, laser and SPMU collections). (b) **True survivors outside that list:** `/pages/does-numbing-cream-work` ("They're not anaesthetics. They're not medicines.", "This is preparation, not anaesthesia.", linked in the header), `/pages/about`, 3 tattoo articles ("Senseless is a cosmetic product."), the format-collection FAQ "Each formula is a UK cosmetic…" and `/pages/llms-txt` | Medium | Founder |
| N15 | The tattoo buying guide tells readers a missing INCI list "is information in itself" | `/blogs/guides/where-to-buy-numbing-cream-for-tattoos-uk`. Senseless publishes no INCI | Medium | Founder |
| N16 | No evidence pack for a Google appeal or an MHRA question | No public INCI; no SCPN notification numbers or Responsible Person on record; the Shopify product category (which maps to `google_product_category`) is unknown | Medium | Legal; founder |
| N17 | Three ad-facing collection FAQs contradict the unbroken-skin instruction | "Take extra care on sensitive or broken skin." on `/collections/numbing-cream`, `/collections/numbing-gel` and `/collections/numbing-cream-for-microneedling`. Deferred by Daniel on 7 Aug | Medium | Founder; G2 owner |
| N18 | The 5 kits have vendor `senseless-numbing`; every other product has `Senseless` | If the feed takes brand from vendor, the kits' brand is wrong. The feed brand was not observed | Medium | Account holder checks; CC fixes |
| N19 | The mobile sticky add-to-cart price doesn't update when the size changes | `sections/senseless-product-hero.liquid:237`; `update()` at :308-336 never touches it. Seen in source only; not observed live | Medium | CC |
| N20 | The "formal record" shipping pages omit Express and paid prices; date stamps are stale | `/pages/shipping-delivery` says "Last updated 4 June 2026" although its body was rewritten on 12 Sep. `/policies/refund-policy` says 2026-06-04 while the page says 3 July | Medium | Founder approves; CC |
| N21 | Delivery pages set a 14-day deadline to report damaged or missing goods | `templates/page.delivery.json:114,206` and the shipping-delivery metafield. CRA s22 gives a 30-day right to reject; s31 makes restrictive terms non-binding | Medium | Legal |
| N22 | The T&Cs have no cancellation clause and no statutory-rights reminder; the liability cap may restrict CRA remedies | `/pages/terms-conditions`, `/policies/terms-of-service` | Medium | Legal |
| N23 | Merchant Centre identity is only partly resolved | Records name MC `5653174667` and `5805726847` (the second noted "0 products synced", peter@…). Public evidence narrows it: every served page carries the G&Y app's `store_widget` with `merchantId` `5805726847`, and the widget calls Google with `merchant_id=5805726847`. So the G&Y app on senseless-numbing links to `5805726847`. That doesn't prove it's the MC linked to Ads `368-965-4782`. It does sharpen one question: which feed has PMax "Shopping - Cream" (£1,017.71 spend) been serving from? Stakeholder Action 38e58bc3-75ea-81da has been open since 29 Jun. The old store is still alive (V48) | Medium | Account holder; founder |
| N24 | This Mac mini can't mint an Admin token or deploy | `.env` Shopify credentials are empty; `scripts/deploy.sh:118-120` exits. All Admin API and deploy work must run on the MacBook Pro | Medium | Founder (copy the `.env`) |
| N25 | Threshold wording and the banner maths don't match the rate card | Copy says "over £40/£80", but the rate card is inclusive ("from £40"). The banner uses the pre-discount subtotal (`snippets/senseless-shipping-banner.liquid:83`); rates use the post-discount total | Low | Founder |
| N26 | Offer-level `cutoffTime` is outside Google's documented offer-level subset | Probably ignored; valid schema.org | Low | CC |
| N27 | The noindex policy pages emit two conflicting robots meta tags | `noindex,follow` from the theme and `noindex,nofollow` from `content_for_header` | Low | CC |
| N28 | `og:price:amount` always shows the lowest variant price | `snippets/meta-tags.liquid:120` uses `product.price` | Low | CC |
| N29 | Offer `name` is "Default Title" on 7 single-variant products | `snippets/senseless-structured-data.liquid:412` | Low | CC |
| N30 | `productID` is emitted as `shopify_GB_<id>`, and a comment claims that's MC's key | The G&Y item IDs are `shopify_ZZ_<pid>_<vid>` | Low | CC (comment) |
| N31 | VAD-4PK is published with brand "Senseless" | The owner's sheet lists it as "Unbranded" with no GS1 code | Low | Founder |
| N32 | "our practitioner grade" appears in the Professional Ultimate description, which feeds MC | COMPLIANCE.md bans the "-grade" family. Other Professional SKUs say "practitioner tier" | Low | Founder |
| N33 | Phrases dropped from other ad-facing pages on 6 Jun (4284390) remain on two | "available without restriction. Trusted at the chair." on `/collections/professional`; "Available to all, without restriction." on `/pages/strongest-numbing-cream` | Low | Founder |
| N34 | Purchase value is defined differently in Ads and GA4/MC | Ads: total including shipping and VAT. GA4: subtotal. Don't compare them one for one | Low | Founder + agency |
| N35 | The Klaviyo popup covers the cookie-banner buttons | About 7s after load, `elementFromPoint` at "Accept all" returns Klaviyo's dialog (z-index 90000) | Low | Founder (Klaviyo) |
| N36 | The live SKU re-code is documented nowhere | SBUN-xx → SBUN1–5, SG15CL → S15CL, FOAM → SFOAM. The Clinical Gel breaks the gel pattern | Low | Founder (SKU master) |
| N37 | A "Verified" review describes using the product before a 17-year-old's blood tests | On `/products/advanced-strength-spray`. The ad-facing vs-ametop page says Senseless isn't formulated for medical procedures | Low | Legal |
| N38 | Returns wording is authored in 5 separate places | Page metafields, native REFUND_POLICY, `templates/page.faq.json`, the bag PDP and the delivery pages. They drift silently | Low | CC (ship together) |
| N39 | No delivery page states postcode coverage | The audit (p6 step 4) asks for it. `/pages/delivery` and `/pages/shipping-delivery` have 0 mentions of Highlands, Islands, Northern Ireland, Channel Islands, Isle of Man or BFPO (21 Sep). Whether the rate card surcharges or excludes them is an Admin question | Low | Founder (copy); CC reads the delivery zones |
| N40 | The imported reviews undercut the premise of the 2 Jul reviews ruling | Decision 39158bc3-75ea-8149 was framed around "genuine UGC reviews" ("genuine UGC reviews are out of scrub scope"). Reviews imported from another brand are exactly what puts that premise in question (N4) | Medium | Legal |

**Outside the ads scope but due in 9 days:** Google Play developer verification (deadline 30 Sep 2026) was dropped from the handoff on 4 Sep with no recorded closure. Ask Daniel.

## 5. Action list, ordered by value

### A. Claude Code can do

**Prerequisites:**
- Admin API and deploy work must run on the MacBook Pro (N24).
- Google Ads is audit-only for us.

**Gates on every change:**
- `compliance-check` on any user-facing copy.
- theme-check must report 0.
- Commit → push → `bash ./scripts/deploy.sh --only <paths>` (under bash).
- Asset-API diff plus a live curl.
- Two files touched below are reviews-guard-locked: `snippets/senseless-structured-data.liquid` and `sections/senseless-product-hero.liquid`. They need `--reviews-changed` and a lock commit.
- Run the injectable-clean sweep after any nav, collection or landing-page change.

1. **Browser checks, available now (read-only, puppeteer-core):**
   - whether the bundle sale styling is visible in the search modal and on `/search` (N7);
   - the sticky price after a size change (N19);
   - that add-to-cart on each `?variant=` URL adds the right size (V15);
   - a cart line with a bundle in it (cart session only, no order).
2. **Consent fix (N1).** Change line 127 to `sale_of_data: !!c.marketing`. Do this only after the founder agrees the timing, and after the account holder has confirmed the conversion set-up (§5D step 8). Otherwise a dormant GA4 import could start double-counting.
   - Verify with a live three-state test (no choice / Accept / Reject): the `graphql.json` response, `Shopify.customerPrivacy` state, GA4 collect requests and Clarity.
   - Add a consent-path check to post-deploy verification.
3. **Structured-data batch**, one reviews-guard deploy of `snippets/senseless-structured-data.liquid`:
   - **Shipping (V17).** Remove `eligibleTransactionVolume`. Then either:
     - move the policy to `Organization.hasShippingService`, with `ShippingConditions.orderValue` bands matching the rate card and Offers pointing at it; or
     - emit only the methods that are valid at each variant's own price.
   - **Hygiene:** give Offer `name` a fallback for "Default Title" (N29); decode `&amp;` (V5); correct the `productID` comment (N30); relocate `cutoffTime` (N26).
   - **Keep:** `class="jdgm-server-jld"`, the `#product` @id, and the shipping and returns @id references on every Offer.
   - **Verify:** re-run the Judge.me CDP test from 66aa9b8, the Schema Markup Validator (0 warnings) and the Rich Results Test.
   - **Outside the locked file:** `og:price` → selected variant in `snippets/meta-tags.liquid` (N28), and the breadcrumb skipping the three injectable handles on a founder go (N10).
   - Restructure variants into ProductGroup only if MC shows price issues on the second sizes (V14).
4. **Sticky price fix** if check 1 confirms it (N19). Reviews-guard-locked file.
5. **After the founder's tier ruling** (see B2):
   - Edit the 3 lines in `snippets/senseless-comfort-mark.liquid:44` and `snippets/senseless-scale.liquid:63,76`. That covers all 37 URLs.
   - Fix the visible "not a ranking" copy.
   - Do a COMPLIANCE.md/BRAND.md docs pass.
   - Re-grep the whole site; expect 0 hits.
6. **After the founder's bundle scope call** (B4): suppress compare-at and Sale badges for bundles in `snippets/price.liquid` and `blocks/_product-card-gallery.liquid`. Alternatively, clear compare-at at the data level. In that case, first move the four-item sum to a metafield, because `sections/senseless-bundle-contents.liquid:42` reads `product.compare_at_price`.
7. **After Legal signs off the returns wording:**
   - Ship all the surfaces in one change (N38): policy metafields and the `scripts/policy-metafields.py` mirror, native REFUND_POLICY, the bag PDP, the delivery pages, and the T&Cs (both copies).
   - `page.faq.json` changes only with Legal's verbatim wording.
   - Then move the return schema to `Organization.hasMerchantReturnPolicy` so it mirrors the final text.
8. **After the founder approves copy:** rewrite `/policies/shipping-policy` and `/pages/shipping-delivery` from the rate card, and fix the date stamps (N20, N25). Suggested wording, matching the rate card band by band (no claims; compliance-neutral; founder approves): *"Under £40: Standard (4–6 working days) £1.99, Express (2–3 working days) £3.99, Next working day £8.99. £40–£79.99: Standard free, Express £3.99, Next working day £8.99. £80 or more: every order ships next working day, free."* (Decision 39c58bc3-75ea-81d1: the ≥£80 band shows a single £0 next-day rate.) Add postcode coverage once the delivery zones are read (N39).
9. **After the GTIN decision (B3):** write the barcodes with `productVariantsBulkUpdate`, mapped by tier × format × size and never by the sheet's SKU column. Leave VAD-4PK and the kits empty. Re-check `gtin13` on all 22.
10. **Boundary shipping test (read-only):** `draftOrderCalculate` at £39.99, £40.00, £79.99 and £80.00, plus a £45 cart with a £10 order discount. Also test a mainland, a Highlands/Islands, a Northern Ireland and a Channel Islands postcode, and read the delivery zones (N39). Record the results.
11. **If the founder extends the ad-facing rule:**
    - make `scripts/injectable-clean-sweep.py` count injectable terms as well as links;
    - edit the Selector options and the System matrix, or move the matrix into the organic guide cluster;
    - trim strongest-numbing-cream, vs-ametop and aesthetic-numbing-cream.
12. **Small copy fixes after the founder's calls:** N14, N17, N32 and N33. Change kit vendors to `Senseless` if MC shows the wrong brand (N18).

### B. Founder decisions

1. **Consent fix timing.** Brief Martin (Colossal Search) first. Once the AW pixel is gated, conversions from visitors who reject stop being recorded, which will affect bidding.
2. **Tier basis: pick one** (V23–V25, N12). First record with the formulator what actually differs between the tiers, as a Confirmed Fact with no percentages published.
   - **Option 1 (smallest; matches the 1 Sep naming, the pack and the feed).** "Strength" is the tier name and the Scale shows position. Change the hidden text to "Advanced — tier 2 of 3 on the Senseless Scale". Replace "not a ranking" with "Three tiers in sequence, each matched to a different kind of session. Higher isn't automatically better."
   - **Option 2.** "Strength" means a substantiated formulation level. Remove the disclaimer and supersede 38e58bc3-75ea-817c. Legal should bless this first.
   - **Option 3.** Finish the 20 Jun "comfort, not potency" reposition. Least recommended: products named "Advanced Strength" would still sit next to "not a measure of strength".
3. **GTINs.** Scan one Clinical Gel 15ml and one 35ml to see which code is printed. Then decide whether to adopt the GS1 UK codes (a Senseless equivalent of TN DEC-53). Also decide the kits' GTIN approach and VAD-4PK's brand (N31).
4. **Bundles.**
   - Does "never presented as on sale" cover Google Shopping/PMax and on-site search?
   - If so, which mechanism: clear compare-at and use a metafield, or an MC supplemental feed override?
   - With Legal: are bundles "sale items" for returns (N8)?
5. **Routing.** Open an MHG/legal work package (§5C). Log a Compliance Hold (Applied) on returns wording so nobody edits it piecemeal.
6. **MC access.** Get Peter or the agency to name the live MC account and either run §5D or give read access. Put the four open questions from 4 Sep to Martin (`NEXT_SESSION.md:167`).
7. **Ad-facing rule scope.** Should it cover injectable text and campaign settings (PMax URL expansion) as well as links (N9, V49)? Should `/pages/faq`, which is linked from every header, count as ad-facing?
8. **Interim Judge.me steps while Legal considers N4.** Options: turn the source badges back on, or stop imports feeding the JSON-LD rating and the homepage "4.9 / 5 · 230+". Don't delete genuine reviews.
9. **Content calls:**
   - classification survivors (N14);
   - INCI: publish it, or soften the buying guide (N15), e.g. *"A full ingredients list. Every cosmetic carries one on the pack; if it isn't on the page, ask the seller."*;
   - the PDP FAQ lines (N13), e.g. *"Match the tier to the session you're booked for; your practitioner is the best guide."*;
   - N17, N25, N32 and N33.
10. **Housekeeping:**
    - confirm the SKU master (N36);
    - check the old store's sales channels (V48);
    - delay the Klaviyo popup until a cookie choice exists (N35);
    - copy the MacBook `.env` to the Mac mini (N24);
    - Google Play verification (deadline 30 Sep).

### C. MHG/legal

1. ~~**Consent (N2).**~~ **Closed 22 Sep 2026 by the founder: the Ads pixel behaviour is intentional; leave it as is.** (Klaviyo onsite and the merchantverse call were raised in the same package and fall under the same decision.)
2. **Returns and statutory rights (V29–V32, N5, N8, N21, N22).**
   - 14-day right to cancel and a model cancellation form (CCR Sch 3 Part B).
   - The sale-items exclusion.
   - The sealed-hygiene scope under reg 28(3)(a). MHG ops should first say whether the topicals are physically sealed.
   - The refund deadline (reg 34) and refunding the delivery charge.
   - Faulty-goods rights (CRA s20, s22, s31).
   - The 14-day delivery-report deadline.
   - A T&Cs cancellation clause and the liability cap.
   - Whether orders placed since launch need any remediation.
   - Bundles where one item has been unsealed.

<details><summary>Draft wording for Legal to review (not final copy)</summary>

**Your right to cancel.** If you change your mind, you can cancel your order within 14 days of the day you receive it, without giving a reason. Tell us by emailing cs@senseless.uk with your order number, or use our cancellation form. Then send the items back to Paddock Business Centre, 2 Paddock Road, Skelmersdale, WN8 9PL within 14 days of telling us. We will refund the price and the standard delivery charge you paid within 14 days of receiving the items back, or of you showing us you have sent them if that is sooner, to your original payment method. You pay the cost of returning items you cancel. We may reduce the refund if an item has been handled more than you would in a shop.

**Sealed items (only if Legal confirms the seal facts).** For health-protection and hygiene reasons, the right to cancel ends for a sealed cream, gel, spray or cleanser once its seal is broken after delivery. This does not apply to items that are still sealed, or to the Senseless Cosmetics Bag.

**Our 30-day returns.** In addition to your legal rights, you can ask to return unused, unopened items in their original packaging within 30 days of receipt.

**EU line.** Replace with: "We deliver to UK addresses only at present."
</details>

3. **Reviews (V39, N4, N37).**
   - Provenance and attribution of the Totally Numb imports: the hidden badge, the rating in structured data, the signs of text editing, and consent and data protection for named TN customers.
   - Does the 2 Jul "leave as-is" ruling still stand, given GN8 Appendix 9 (Sep 2025), and given that the ruling was framed around "genuine UGC reviews" while most rendered reviews were imported from another brand (N40)?
   - The blood-test review.
4. **Classification (V27, N6, N16).** Weigh the new evidence. Decide whether the 2 Jul closure stands or whether to ask MHRA through its Borderline Advice Form. Assemble the evidence pack: CPSR scope, SCPN numbers, Responsible Person, INCI. Our authority doesn't extend to reopening this.
5. **Google category (V28).** Once the account holder has read the alert, choose the route. Google warns: "Do not apply for a category that does not match your business model". Rewording the site won't change a category Google has assigned.
6. **Injectable text on ad-facing pages** against Google's UK rule on prescription drugs in landing pages (V34, N9).
7. **Bundle reference price.** Only if a Shopping sale presentation is kept: may a never-charged component sum be shown as a sale price (CMA guidance, DMCC Act 2024)?

### D. Google-account holder: export and join checklist

1. **Access.** Confirm that Ads `368-965-4782` links to MC `5805726847`, which is the G&Y app's account (seen in the live store widget). If it links to `5653174667` instead, identify that account's data source. Say who administers each account and grant read access to a working login.
2. **Healthcare.** Open the "Apply for healthcare certification" alert and record:
   - the certification type it names;
   - which ads, assets, keywords or destinations triggered it;
   - the date it first appeared, compared with the 21 Aug impressions drop.
   Also export MC account-level issues (healthcare, misrepresentation). Healthcare or destination enforcement can limit **Search** too, not only Shopping/PMax (audit p5). The two Search campaigns built on 27 Aug had £0 spend at last record (`NEXT_SESSION.md:148`), so check whether their ads, keywords or assets are limited by the healthcare policy. Send all of it to Legal before applying for anything.
3. **MC product export.** Export all items with all columns:
   - id, item_group_id, title, link, image_link;
   - price, sale_price, availability;
   - gtin, mpn, brand;
   - processed `google_product_category`, product_type, custom labels;
   - feed label/country, language, data source, last updated;
   - destination status (Shopping ads, free listings) and item issues.
   Also export Needs-attention, the data-sources list, and the automatic item updates setting and history.
4. **Join.** Build the baseline of 22 expected IDs `shopify_ZZ_<product_id>_<variant_id>` from live `/products.json` (compare case-insensitively).
   - Then match the `?variant=` value in `link` to the variant id.
   - Then match on live SKU + title + size. Don't use the Notion Handle Registry SKUs.
   - Classify every row: current-match / current-mismatch / obsolete / unknown-source.
   - More than 22 rows is legitimate only for extra feed labels or languages.
   - Expect a second ID family. The 1 Jun move to the new store (senseless-numbing) changed every Shopify product ID. Any MC history from the old store (`senseless-tattooing`, still live behind `/password`) will sit under different `shopify_ZZ_` IDs, so match those rows on SKU, title and size, not on ID.
5. **Per-item checks:**
   - SBUN1–5 price and sale_price (expect price = compare-at, sale_price = current if the channel passes compare-at);
   - GTINs (expect only the 3 old codes);
   - kit brand (`senseless-numbing`?);
   - price mismatches or automatic price corrections on S30CL, S30AD, S35CL, SG35AD and SG35PR;
   - "missing identifiers" diagnostics;
   - whether custom labels use the Botox/Lip Fillers tags;
   - whether Judge.me feeds product ratings.
6. **Why obsolete items persist.** Give each non-current ID's data source. Explain why the G&Y-linked MC (`5805726847`) was once noted "0 products synced" while PMax "Shopping - Cream" spent £1,017.71. Check the G&Y channel's current product sync count, whether `senseless-tattooing.myshopify.com` has a G&Y channel, and any supplemental feeds or apps. For each item: keep / update / retire / investigate. Changes need founder and agency sign-off.
7. **Spend by item.** Ads report editor with Campaign, Item ID, MC ID and Channel against Impressions, Clicks, Cost, Conversions and Conversion value, for the last 30 and 90 days. Join to the 22 and total the cost on non-current IDs.
   **PMax:** for each campaign, record Final URL expansion, URL exclusions, text customisation and listing groups. Flag any route to the 3 injectable collections, `/blogs/` or `/pages/does-it-hurt-by-treatment`. Check audience lists and assets for health policy labels.
8. **Conversions.** Do this before the consent fix ships. Export Goals → Conversions → Summary, including Diagnostics (enhanced conversions, consent mode). Expect exactly one Primary purchase (`AW-18228180367/0WySCJLhqrwcEI_r7_ND`, Count = One, transaction value). Any GA4 purchase must be Secondary.
9. **Settings.** Set GB account-level shipping in MC to mirror the rate card:
   - £0–39.99: £1.99 standard;
   - £40–79.99: free standard, £3.99 express, £8.99 next day;
   - £80+: free next day only;
   - cut-off 15:00 Europe/London.
   Enter the return policy once Legal has settled the wording. Check the Search Console Merchant listings report and the 19 Aug "Validate fix" requests (Peter).
10. **Test purchase.** Do this after the consent fix and the pixel-permission change.
    - In a fresh browser, click Reject and confirm there are no Google Ads or GA4 requests.
    - In a new profile, click Accept and place one low-value order.
    - Capture the conversion (label, value, GBP, order ID) and the GA4 purchase, and match both to the Shopify order.
    - Refund the order and note that neither pixel retracts the conversion.
11. **Monitor weekly:**
    - eligible current variants out of 22;
    - obsolete IDs with impressions (target 0);
    - mismatch issue counts;
    - cost by item, conversion rate and ROAS.
    Treat the consent-fix date as a break in the data, and compare equal periods only after about 30 days of conversion restatement.

## 6. Canon context

| Record | What it says | How this study touches it |
|---|---|---|
| Decision 39158bc3-75ea-8194 (2 Jul) | MHRA classification closed: cosmetic | **Closed.** The audit re-raises it with no product-specific evidence. Our new evidence (N6) goes to Legal, the named owner of Stakeholder Action 38e58bc3-75ea-812a, which was closed on the founder's statement |
| Confirmed Fact 3b358bc3-75ea-8153 (6 Aug) | "Antibacterial" substantiation is on file | **Closed.** The audit re-raises it with no new evidence |
| FAQ legal-verbatim exception (`.claude/rules/compliance.md`) + Decision 39158bc3-75ea-81f7 (PDP 45–60 line) | Onset and duration wording allowed on the FAQ only; the customer-attributed timing line has its own decision | **Closed.** The audit's duration question is answered. "Best results" and "session lengths" are still unruled (N13) |
| Decision 39158bc3-75ea-8149 (2 Jul) | Leave published reviews unedited (legal advice), framed around "genuine UGC reviews" | Closed for **phrasing**. Not covered: provenance and attribution, GN8 Appendix 9, and the fact that most rendered reviews were imported from another brand, which is exactly what the "genuine UGC" premise did not contemplate (N4, N6, N40) |
| Returns wording | No legal sign-off exists anywhere | **Not closed.** The audit's p4 concern is live and independently confirmed |
| Decisions 38e58bc3-75ea-817f (2 Jun), 38e58bc3-75ea-817c (20 Jun); DECISIONS-LOG 1 Sep "keep Strength" | "Scale = strength axis" / "not potency" / "one name everywhere" | **Canon contradicts itself.** A founder ruling must supersede one of them |
| DECISIONS-LOG.md:211-222 (1 Sep) | Bundles never on sale; the compare-at data kept; bag free | Search surfaces missed (N7); feed consequence open (V8). First flagged on 6 Aug (`docs/SITE-ASSESSMENT-2026-08-06.md:93`) |
| Decision 3b358bc3-75ea-8148 (6 Aug) + `.claude/rules/ad-facing.md` | Injectable collections are organic-only; no links from ad-facing pages | Holds (0 breaches). Gaps: text mentions, the breadcrumb, PMax URL expansion |
| Decisions 39c58bc3-75ea-81fe / -81d1 (13 Jul); 3c158bc3-75ea-8165 (19 Aug); 38e58bc3-75ea-8109 (22 Jun) | Rate card; shipping and returns by @id; "thresholds belong in MC" | The 22 Jun position was overtaken on 14 Aug with no record, and Google's docs support it (V17) |
| Decision 3bc58bc3-75ea-81d2 (14 Aug) + DECISIONS-LOG 1 Sep "certification-only" | Classification statements and "not an anaesthetic" lines removed | Survivors still live (N14) |
| Compliance Hold 3b158bc3-75ea-8183 (EMLA keyword, Applied) | Comparison pages held (GREY) | Add the GN8 §5 "comparison with licensed medicines" citation (N6) |
| Compliance Hold 3bb58bc3-75ea-8147 (14 Aug) | INCI not published (founder); eugenol "function test weak" reasoning | The reasoning is unverified against the SmPC (N6). G1 is **closed** (owner, 14 Aug) and not re-raised |
| G2 ("Apply to clean, unbroken skin") | The open safety gate | Keep it. It is why the audit's positive finding holds (V41). No Compliance Holds row found for it |
| Decision 37d58bc3-75ea-8172 | Senseless Ads `368-965-4782` separate from Totally Numb; Purchase is the primary goal | Consistent with V4 and V54 |
| Stakeholder Action 38e58bc3-75ea-817a (cookie consent, Open) | Called it an admin setting | The cause is theme code (N1) |
| TN DEC-53 / 56 / 57 (21 Sep) | GS1 UK codes; single selected-variant Offer; `og:price` follows the variant | Sister-store precedents, **not Senseless canon** |
| Standing rule (Daniel, 4 Sep) | Google Ads is audit-only | All of §5D is read or export unless the owner decides otherwise |

Records drift: the lenses logged 98 stale statements in internal records (repo docs, Notion, memory). They are handled in the 21–22 Sep records update and are not repeated here.

## 7. Open questions

**Account holder**
- Which MC account is live and linked to Ads and to the G&Y app? Who administers it?
- What certification does the healthcare alert name, what triggered it, and when did it first appear?
- What does MC hold for SBUN1–5 (price and sale_price), the kit brand, GTINs and the processed category?
- Is a GA4 purchase imported into Ads, and is it Primary?
- Is the G&Y channel the only feed source? Does it map tags to custom labels? Does Judge.me feed product ratings?
- Is the Ads account in a learning period or under a change freeze that should set the timing of the consent fix?
- Was the unidentified Ads customer ID `966-010-0403` (open since 12 Jun) ever resolved?
- Are the two Search campaigns from 27 Aug limited by the healthcare policy, and is that why they have spent £0?
- Does the rate card surcharge or exclude Highlands, Islands, Northern Ireland, the Channel Islands or BFPO (N39)?

**Founder**
- What actually differs between the Clinical, Advanced and Professional formulas? Does the physical pack print "<TIER> STRENGTH"?
- Who authorised the 20 Jun "comfort, not potency" reposition, and was it on legal advice?
- Which barcode is printed on the packs? Are the GS1 UK records right (ml, not g)? Should the barcode sheet become Senseless canon?
- Were the four 4 Sep questions put to Martin?
- Why were the SKUs re-coded, and which system is the SKU master?
- Is VAD-4PK a third-party product?
- Which Shopify product category is set on each product?
- Was the AW pixel's permission changed after 12 Jun, or was the 12 Jun record wrong from the start? (Needs Shopify admin.)

**MHG/legal**
- Did Legal review the 2 Jul classification closure, or is the founder's statement its only basis? Is the formulation still eugenol-based, and at what concentration?
- Are the topicals physically sealed on delivery? (MHG ops)
- Who instructed the 6 Jun removal of the 14-day cancellation paragraph?
- Does the order-confirmation email carry cancellation information? What do Shopify's admin return rules encode?
- Did the 2 Jul review advice consider GN8 Appendix 9 (Sep 2025) and the reviews' origin at another brand?
- Are SCPN notifications and a Responsible Person in place for every SKU?
- Only if Legal sees a separate axis: does "antibacterial" raise a biocide or antiseptic classification question? The substantiation itself is closed in canon.

**Claude Code**
- Cart line items since b124e51 haven't been observed. They need a cart session, which is covered in §5A item 1.