# Spec — ProductGroup / hasVariant, Phase 1 (the 5 two-size PDPs)

**Status:** READY TO BUILD, pending decisions §4. Prepared 23 Sep 2026 (Mac mini) by a read-only research + design workflow
(4 grounding researchers → 3 independent designs → judge → adversarial critic). Nothing here has been deployed.
Target file: `snippets/senseless-structured-data.liquid` at sha256 `e0e50e770b7ee88f…` (repo `0a31b9e`); the draft applies
cleanly and produces sha256 `db5291d97804139501730d9cbc1388c2077ed2b0d4bfe250ddc280324ff13881`.

## 1. Why

Audit 2026-09-23 item 4: each PDP emits ONE Product with ONE Offer for the selected variant (the 22 Sep price fix, DECISIONS-LOG
2026-09-22 Decision 6). `?variant=` URLs canonicalise to the base URL and only base URLs are in the sitemap, so Google Search
never sees the larger size of the 5 two-size products (Clinical Cream 30g £44.99, Advanced Cream 30g £49.99, Clinical Gel 35ml
£34.99, Advanced Gel 35ml £39.99, Professional Gel 35ml £44.99). Since `0a31b9e` (23 Sep) every size carries its GS1 UK GTIN.

## 2. The design in one paragraph

WINNER: "MC-safety-first", with the implementation style of "minimal-change". The two designs arrived at the same gate and the same output independently, so the spec below is one design.

WHAT CHANGES
- Only one kind of page changes: the BASE URL (/products/<handle>, no ?variant=) of a product with more than one variant and a single option named "Size". Today that is exactly the 5 two-size PDPs.
- On those pages the node at <canonical>#product becomes a ProductGroup:
  - Group properties: name, description, url (no variant selector), mainEntityOfPage, image[], productGroupID (the numeric Shopify product id), variesBy ["https://schema.org/size"], productID/identifier (kept as today), category, brand, manufacturer, and aggregateRating (on the group only; it moves here from the Product).
  - hasVariant lists every size, NESTED. The size the page preselects (v1, which is the smaller size on the base URL) comes first.
  - Each size is a Product with:
    - @id <canonical>#variant-<variant id>;
    - name "<product title> - <size>" (Shopify's own variant naming, so no new copy);
    - description (the product description), image (the variant image, falling back to the product image), sku/mpn, gtin13 (GS1 UK code, live on all 10 sizes since 0a31b9e) and size;
    - ONE Offer, as an object in the same form as Google's nested example: sku, gtin13, name, price, GBP, itemCondition, availability, url = its own ?variant=<id> URL, seller, shippingDetails from senseless-shipping-refs called with THAT size's price, and hasMerchantReturnPolicy by @id.
- Resulting shipping bands: the 30g creams and Professional Gel 35ml get standard-free; Advanced Gel 35ml at £39.99 stays paid.

WHAT STAYS EXACTLY AS TODAY (byte-identical render, proven locally on 22 of 27 PDP contexts against a fresh post-GS1 live capture)
- Every ?variant= URL. These are the Merchant Center landing pages, and they keep the 22 Sep a511a95 shape: one Product, ONE Offer for the selected size, with og:price following it.
- All 12 single-variant products.
- The collection ItemList branch, meta-tags.liquid (og:price, canonical), the breadcrumbs snippet, shipping-refs, the templates, the hero section and the FAQPage block.

HOW
- One file changes: snippets/senseless-structured-data.liquid. There are two edits:
  - E1: the header comment at line 16.
  - E2: replace lines 376-476 with the drop-in. It adds a gate in the existing {% liquid %} block and an {% if ss_group %} ProductGroup … {% else %} branch; the else branch is today's lines 404-476 verbatim, with comment-only edits.
- The gate is: `product.variants.size > 1 and options_with_values.size == 1 and option name == 'size' and product.selected_variant is nil`.
- Line 160 `class="jdgm-server-jld"` and the reviews-guard marker `product.metafields.reviews.rating` are untouched.
- Deploy with `--reviews-changed`, then commit the lock.

PHASE 2 (not this session, a separate decision)
- Put the full group on ?variant= URLs too, which is Google's literal single-page model. This became plausible TODAY because the GS1 GTINs are loaded and MC has synced them. Merchant Center Help 7331077 documents matching a page with several offers by GTIN.
- Do it one product at a time, only after MC has shown gtin = gtin13 for both sizes with 0 price/GTIN issues for 7+ days, and watch each product for a week.

### Why this design won

SCORES (1-5): MC safety / Google-doc fidelity / blast radius / Judge.me & reviews-guard / RRT testability / single-variant & collections

1. MC-safety-first (D1): 5 / 4 / 5 / 5 / 5 / 5 & 4. **Winner.**
2. Minimal-change (D3): 5 / 4 / 5 / 5 / 5 / 5 & 4. Converges with D1. It lost only on detail: no variant @id, and a thinner safety analysis. Its two-pass hasVariant loop is simpler than D1's capture and string-concatenation approach, so the final spec uses it.
3. Google-spec-first (D2): 4 / 3.5 / 2.5 / 5 / 3.5 / 5 & 3.

MC SAFETY: the deciding criterion, because constraint (a) is a hard constraint.
- D1/D3 leave every MC landing URL (?variant=) byte-identical. MC reads the same single Offer it reads today. That meets Help 7331077's first condition ("There's a single offer on the landing page", https://support.google.com/merchants/answer/7331077) by construction, and invariance can be proven by diff.
- D2 also keeps one Offer on ?variant= URLs, but it changes the shape MC parses there: a ProductGroup, a nested Product, and a url-only stub. That shape is undocumented for MC, and it can't be proven invariant by a byte diff.
- The adverse case for D1 is also covered now. Suppose MC read the base URL (through a bare feed link or the canonical). Since 0a31b9e both Offers there carry the GS1 gtin13 that MC has already synced from Shopify, so the documented multi-offer GTIN route applies. The first Offer is also the smaller, cheapest size, which is what the base page shows.

FIDELITY
- The base URL in D1/D3 is Google's documented single-page pattern ("For single-page sites, there must be only one distinct canonical URL for the overall ProductGroup ... Typically this is the base URL", https://developers.google.com/search/docs/appearance/structured-data/product-variants). Google indexes that URL. Every ?variant= URL canonicalises to it, and only base URLs are in the sitemap.
- The one deviation: Google's example serves identical markup on every URL, and D1/D3 do not. Our ?variant= duplicates carry a single-size Product instead.
- D2's ?variant= markup mixes the multi-page url-only stub into a single-page canonical setup. That combination is undocumented, so it is the larger deviation.
- D2 also retypes collection ItemList items as ProductGroup, which Google doesn't recommend for listing pages ("We recommend focusing on adding markup to product pages instead of pages that list products").

BLAST RADIUS
- D1/D3: one locked file, the PDP branch only, 22/27 renders byte-identical.
- D2: a new snippet, the PDP branch and the collection branch, with a two-commit deploy ordering. It changes about 19 collection URLs' GSC item counts too, which would confound the 27–30 Sep re-check.

JUDGE.ME
- All three keep @id #product, @type exactly "ProductGroup" and nested variants.
- The verbatim V() simulation rewrote 0 of 27 renders for the final draft.

RRT
- D1/D3 put a normal Google-shaped group on 5 URLs, testable in code mode before deploy and in URL mode after. The 10 ?variant= URLs should read exactly as today (1 Merchant listing each).
- D2's stubs on ?variant= URLs have no RRT precedent.

LOCAL EVIDENCE FOR THE FINAL DRAFT (this session; nothing written to the repo, Shopify, MC or Notion)
- Fresh live capture: 27 PDP URLs plus 17 product .js payloads, taken after the GS1 load. The liquidjs mock of the current file equals live on 26/27. The one miss is VAD "2" vs "2.0", a JS number-format artefact.
- Draft render:
  - 22/27 byte-identical;
  - 5 ProductGroups with 2 Offers each and correct prices, GTINs and shipping bands;
  - valid JSON, 0 dangling @ids, 0 injectable handles in ld+json;
  - Judge.me V() rewrites 0.
- Edge cases:
  - first size sold out: the 30g is listed first and the 10g is OutOfStock;
  - Size + Colour: falls back to Product, byte-identical;
  - option not named Size: falls back, byte-identical;
  - variant with its own image: that image is used;
  - lower-case "size": grouped.
- `shopify theme check`: 119 errors / 78 warnings both before and after (the recorded baseline), 0 offences on the snippet.

Artefacts are in /private/tmp/claude-501/-Users-matrixhealth-code-senseless-theme/4ae5dea4-c71e-4b16-85a2-90992fcf5da6/scratchpad/pg/judge/:
- new/senseless-structured-data.liquid (sha256 db5291d97804139501730d9cbc1388c2077ed2b0d4bfe250ddc280324ff13881);
- final.diff;
- harness/ (render.mjs, edge.mjs, simV.cjs, out/);
- rrt-code/<handle>__base.html;
- tc/ (theme-check results);
- live/ (the capture).
The scratchpad is per-session and may be cleared; liquid_draft below is the durable copy.

CORRECTIONS TO THE BRIEF, verified this session:
- HEAD is now 0a31b9e ("Barcodes: GS1 UK codes on all 16 covered Senseless variants"), not a5d7ecb. The snippet sha is still e0e50e77…, which equals reviews-guard.lock.
- All 10 two-size variants now carry check-digit-valid GS1 UK gtin13 values (5065028388xxx). The "only valid GTIN on Clinical Gel 35ml" premise is obsolete.
- DECISIONS-LOG 23 Sep Decision 5 and NEXT_SESSION item 7 say MC synced them within ~10 min. That is from the repo records; I did not check MC itself.

### Grafted from the other designs

- From minimal-change (D3): the two-pass hasVariant loop, `{%- for ss_pass in (1..2) -%}` with `continue`. The selected size is emitted first and the rest after, with an `ss_sep` comma. This replaces D1's capture and string concatenation: no string building, simpler whitespace control, and it passed theme-check and the renders.
- From MC-safety-first (D1): each nested variant gets an @id at <canonical>#variant-<variant id>. It follows the file's stable-address convention, is documented in the header comment (E1), and gives Phase 2 or a collection mirror a target to reference. The option name is compared after `| downcase | strip`.
- From MC-safety-first (D1): the adverse-case analysis for MC reading the base URL (first Offer = preselected = cheapest size), the pre-deploy MC export check of the feed `link` column, and the 'take the before-capture immediately before deploy' rule. The GS1 load has already changed live gtin13 values once today.
- From Google-spec-first (D2): the GS1 barcode discovery, now committed as 0a31b9e. It unlocks a documented Phase 2: the full group on ?variant= URLs through Help 7331077's GTIN route, one product at a time, gated on MC gtin = gtin13 for both sizes and a 7-day watch. It is recorded as a later decision, not built now.
- From Google-spec-first (D2): refresh the stale 'only three variants carry a barcode … GS1 UK codes … aren't loaded' comment (old lines 418-424) in the same edit. It is comment-only, so the output is unchanged.
- From Google-spec-first (D2): `offers` on each nested variant is a single Offer OBJECT, as in Google's nested single-page example, not a one-element array. The unchanged else-branch keeps its array so it stays byte-identical.
- From Google-spec-first (D2): an expectation checker run before and after (its live_check.py idea). The verification plan asserts per-URL expectations: 1 Offer on each ?variant= URL, 2 on each base URL, prices, GTINs and bands, rather than eyeballing.
- From Google-spec-first (D2): mirroring the ProductGroup into collection ItemLists. Kept as an OPTIONAL later change, not in this deploy, so the 27–30 Sep GSC re-check stays attributable.
- From the reviews_guard grounding: close the gap where `class="jdgm-server-jld"` is not a manifest marker, by adding one REPO marker line to reviews-guard.manifest (decision item 6). If that is declined, assert the class by hand in the repo, the Asset API copy and the live HTML.

## 3. Markup

### Base URL (e.g. `/products/clinical-strength-cream`) — AFTER

```json
Example product: Clinical Strength Cream. It shows both the rating-on-group rule and the in-product shipping-band split. Details of the example:
- URL: https://senseless.uk/products/clinical-strength-cream
- This URL is the canonical and is in the sitemap. The feed does not use it as the landing page for either size (the next session must confirm this).
- Rendered from the final draft against the live data captured 23 Sep 2026 after the GS1 load. Printed with "/" unescaped; live output uses "\/", and the parsed JSON is identical.

Script tag, unchanged: <script type="application/ld+json" class="jdgm-server-jld">. There is one @graph, and its nodes appear in this order:
1. ["Organization","OnlineStore"] https://senseless.uk/#organization (with the nested #return-policy)
2. WebSite https://senseless.uk/#website
3. ItemPage …/clinical-strength-cream#webpage (mainEntity → …#product)
4. BreadcrumbList …#breadcrumb: Home > Aesthetic Numbing Cream > Clinical Strength Cream
5-9. OfferShippingDetails #shipping-standard, #shipping-express, #shipping-next-working-day, #shipping-standard-free, #shipping-next-working-day-free

Nodes 1-9 are byte-identical to today's live output, and identical to the ?variant= URL below (verified in the render). Node 10 is new:

{
 "@type": "ProductGroup",
 "@id": "https://senseless.uk/products/clinical-strength-cream#product",
 "name": "Clinical Strength Cream",
 "description": "Clinical is the standard-strength cream — the tier most aesthetic appointments call for.",
 "url": "https://senseless.uk/products/clinical-strength-cream",
 "mainEntityOfPage": { "@id": "https://senseless.uk/products/clinical-strength-cream#webpage" },
 "image": [ "https://senseless.uk/cdn/shop/files/senseless-clinical-strength-cream_fccccf52-3e21-409d-83d5-820053e5f6ab.png?v=1781498779&width=1200" ],
 "productGroupID": "15610197246300",
 "variesBy": [ "https://schema.org/size" ],
 "productID": "shopify_GB_15610197246300",
 "identifier": [ { "@type": "PropertyValue", "propertyID": "shopify_product_id", "value": 15610197246300 } ],
 "category": "Cream",
 "brand": { "@type": "Brand", "name": "Senseless" },
 "manufacturer": { "@id": "https://senseless.uk/#organization" },
 "aggregateRating": { "@type": "AggregateRating", "ratingValue": "4.85", "reviewCount": "13", "bestRating": "5", "worstRating": "1" },
 "hasVariant": [
  {
   "@type": "Product",
   "@id": "https://senseless.uk/products/clinical-strength-cream#variant-57777075224924",
   "name": "Clinical Strength Cream - 10g",
   "description": "Clinical is the standard-strength cream — the tier most aesthetic appointments call for.",
   "image": "https://senseless.uk/cdn/shop/files/senseless-clinical-strength-cream_fccccf52-3e21-409d-83d5-820053e5f6ab.png?v=1781498779&width=1200",
   "sku": "S10CL", "mpn": "S10CL", "gtin13": "5065028388108", "size": "10g",
   "offers": {
    "@type": "Offer", "sku": "S10CL", "gtin13": "5065028388108", "name": "10g",
    "price": "19.99", "priceCurrency": "GBP",
    "itemCondition": "https://schema.org/NewCondition", "availability": "https://schema.org/InStock",
    "url": "https://senseless.uk/products/clinical-strength-cream?variant=57777075224924",
    "seller": { "@id": "https://senseless.uk/#organization" },
    "shippingDetails": [ { "@id": "https://senseless.uk/#shipping-standard" }, { "@id": "https://senseless.uk/#shipping-express" }, { "@id": "https://senseless.uk/#shipping-next-working-day" } ],
    "hasMerchantReturnPolicy": { "@id": "https://senseless.uk/#return-policy" }
   }
  },
  {
   "@type": "Product",
   "@id": "https://senseless.uk/products/clinical-strength-cream#variant-57777075257692",
   "name": "Clinical Strength Cream - 30g",
   "description": "Clinical is the standard-strength cream — the tier most aesthetic appointments call for.",
   "image": "https://senseless.uk/cdn/shop/files/senseless-clinical-strength-cream_fccccf52-3e21-409d-83d5-820053e5f6ab.png?v=1781498779&width=1200",
   "sku": "S30CL", "mpn": "S30CL", "gtin13": "5065028388122", "size": "30g",
   "offers": {
    "@type": "Offer", "sku": "S30CL", "gtin13": "5065028388122", "name": "30g",
    "price": "44.99", "priceCurrency": "GBP",
    "itemCondition": "https://schema.org/NewCondition", "availability": "https://schema.org/InStock",
    "url": "https://senseless.uk/products/clinical-strength-cream?variant=57777075257692",
    "seller": { "@id": "https://senseless.uk/#organization" },
    "shippingDetails": [ { "@id": "https://senseless.uk/#shipping-standard-free" }, { "@id": "https://senseless.uk/#shipping-express" }, { "@id": "https://senseless.uk/#shipping-next-working-day" } ],
    "hasMerchantReturnPolicy": { "@id": "https://senseless.uk/#return-policy" }
   }
  }
 ]
}

Other signals on this URL, all unchanged:
- og:price:amount stays 19.99, because meta-tags.liquid is untouched and v1 is the 10g.
- The canonical and og:url stay as they are.
- The FAQPage block (no class) stays.

Expected items on the other 4 base URLs, which follow the same shape:
- advanced-strength-cream:
  - S10AD 24.99 (gtin 5065028388115): std / express / nwd
  - S30AD 49.99 (…139): std-free / express / nwd
  - group rating 4.92/12
- clinical-strength-gel:
  - S15CL 19.99 (…047): std / express / nwd
  - S35CL 34.99 (…009): std / express / nwd
  - no rating
- advanced-strength-gel:
  - SG15AD 24.99 (…054): std / express / nwd
  - SG35AD 39.99 (…016): std / express / nwd
  - no rating
- professional-strength-gel:
  - SG15PR 29.99 (…061): std / express / nwd
  - SG35PR 44.99 (…023): std-free / express / nwd
  - group rating 2.0/1

The RRT should show "Merchant listings: 2 valid items", named "<title> - <size>".
```

### `?variant=` URL — UNCHANGED (byte-identical to today)

```json
Example page: https://senseless.uk/products/clinical-strength-cream?variant=57777075257692. This is the 30g, which is the Google & YouTube feed's landing URL for item shopify_ZZ_15610197246300_57777075257692 (the feed link format is to be confirmed in the MC export). Its canonical is https://senseless.uk/products/clinical-strength-cream.

This page is UNCHANGED, byte for byte. The draft's render parses equal to the live capture taken at 19:3x BST on 23 Sep (post-GS1).
- Nodes 1-9 are identical to the base URL above.
- Node 10 is today's plain Product with ONE Offer:

{
 "@type": "Product",
 "@id": "https://senseless.uk/products/clinical-strength-cream#product",
 "name": "Clinical Strength Cream",
 "description": "Clinical is the standard-strength cream — the tier most aesthetic appointments call for.",
 "url": "https://senseless.uk/products/clinical-strength-cream",
 "mainEntityOfPage": { "@id": "https://senseless.uk/products/clinical-strength-cream#webpage" },
 "image": [ "https://senseless.uk/cdn/shop/files/senseless-clinical-strength-cream_fccccf52-3e21-409d-83d5-820053e5f6ab.png?v=1781498779&width=1200" ],
 "sku": "S30CL", "mpn": "S30CL", "gtin13": "5065028388122",
 "productID": "shopify_GB_15610197246300",
 "identifier": [ { "@type": "PropertyValue", "propertyID": "shopify_product_id", "value": 15610197246300 }, { "@type": "PropertyValue", "propertyID": "sku", "value": "S30CL" } ],
 "category": "Cream",
 "brand": { "@type": "Brand", "name": "Senseless" },
 "manufacturer": { "@id": "https://senseless.uk/#organization" },
 "aggregateRating": { "@type": "AggregateRating", "ratingValue": "4.85", "reviewCount": "13", "bestRating": "5", "worstRating": "1" },
 "offers": [ {
   "@type": "Offer", "sku": "S30CL", "gtin13": "5065028388122", "name": "30g",
   "price": "44.99", "priceCurrency": "GBP",
   "itemCondition": "https://schema.org/NewCondition", "availability": "https://schema.org/InStock",
   "url": "https://senseless.uk/products/clinical-strength-cream?variant=57777075257692",
   "seller": { "@id": "https://senseless.uk/#organization" },
   "shippingDetails": [ { "@id": "https://senseless.uk/#shipping-standard-free" }, { "@id": "https://senseless.uk/#shipping-express" }, { "@id": "https://senseless.uk/#shipping-next-working-day" } ],
   "hasMerchantReturnPolicy": { "@id": "https://senseless.uk/#return-policy" }
 } ]
}

What this page carries:
- Exactly 1 Offer on the whole page, so the 22 Sep invariant holds.
- og:price:amount is 44.99, and the hero price and hidden id are the 30g's.

The same holds for all 10 ?variant= URLs; each keeps its own single Offer:
- S10CL 19.99, S30CL 44.99
- S10AD 24.99, S30AD 49.99
- S15CL 19.99, S35CL 34.99
- SG15AD 24.99, SG35AD 39.99
- SG15PR 29.99, SG35PR 44.99

In the RRT this URL should show "Merchant listings: 1 valid item", as it does today.
```

## 4. Decisions needed before coding

- 1. TIMING (founder). Two re-checks are scheduled for ~27–30 Sep: GSC/MC against the 23 Sep baseline (Merchant listings 94/0, Product snippets 94/0 with the non-critical aggregateRating 89 + review 89), and the MC GTIN check on the 16 re-barcoded items (0a31b9e). RECOMMENDED: deploy after both re-checks are recorded clean. If the founder wants it sooner, deploy anyway and log the expected deltas first: +5 valid items in both GSC Merchant listings and Product snippets, 0 change in MC. Don't commit the snippet change and leave it undeployed: main must equal live.
- 2. SCOPE (founder). Phase 1 only: the ProductGroup goes on the 5 base URLs. The ?variant= URLs (MC landing pages) and the collection ItemLists stay byte-identical. Google's literal 'same markup on every URL' is deferred to Phase 2 (the GTIN route), which needs its own decision later.
- 3. MC GO/NO-GO (read-only check in MC 5805726847, founder's Chrome). (a) The product export's `link` column shows all 10 two-size items linking to their OWN ?variant=<id> URL. If any links to the bare base URL, stop and decide. With the GS1 GTINs on both Offers this is documented-matchable, but it changes the risk. (b) MC shows gtin = the GS1 code for all 10 items. (c) Record the automatic item updates setting, the item_group_id values, the item total and diagnostics as the baseline. (d) The Advanced Gel 35ml item shows £39.99 with no open 'Mismatched product price'.
- 4. RRT DECISION RULE (founder/CC). Any NEW Merchant listings warning or error class on a base URL means don't deploy (code mode) or revert (URL mode); this is the 23 Sep priceValidUntil precedent. Product snippets 'Missing field aggregateRating/review' on the per-size items is the accepted pre-existing non-critical class. Pre-authorised fix, no new decision needed: if the RRT flags a missing `brand` on the nested sizes, add `"brand": { "@type": "Brand", "name": {{ seller_name | json }} },` to each size and re-test in code mode.
- 5. productGroupID VALUE. RECOMMENDED: the numeric Shopify product id (e.g. "15610197246300"). Google only needs it to be unique and doesn't require it to match the feed. If the MC export shows item_group_id in another form and the founder wants them aligned, it is a one-token change before coding.
- 6. CLOSE THE REVIEWS-GUARD GAP. RECOMMENDED yes: add `REPO | snippets/senseless-structured-data.liquid | class="jdgm-server-jld"` to reviews-guard.manifest in the same commit, so `--reviews-changed` can never pass an edit that drops the Judge.me gate class. If declined, the class is asserted by hand in the repo, the Asset API copy and the live HTML (verification steps 3, 11 and 12).

**BINDING AMENDMENT to decision 4 (critic):** the 'Missing field aggregateRating/review' Product-snippets warning is acceptable
ONLY on the two unrated gels. On the 3 RATED products — `clinical-strength-cream` (4.85/13), `advanced-strength-cream`
(4.92/12), `professional-strength-gel` (2.0/1) — the Rich Results Test (code mode, then URL mode) must show aggregateRating
detected on every Product-snippets item with no aggregateRating/review warning. If it appears on a rated product: do not deploy
(code mode) / revert (URL mode). Losing review-star eligibility would otherwise go unnoticed.

## 5. Implementation

- **Patch:** `senseless-structured-data.productgroup.diff` in this folder (`git apply --check` passes on HEAD). It is E1 (header
  comment) + E2 (lines 376–476 → `dropin-376-476.liquid`, also in this folder). E3 (optional, decision 6): add
  `REPO | snippets/senseless-structured-data.liquid | class="jdgm-server-jld"` to `reviews-guard.manifest`.
- Other files:
  - NO CODE CHANGE in: snippets/meta-tags.liquid (og:price and the canonical stay on the selected variant and the base URL), snippets/senseless-shipping-refs.liquid (reused per size as it is), snippets/senseless-breadcrumbs-jsonld.liquid (injectable filter unchanged; the change adds no collection URLs), the collection ItemList branch (lines 478-538), layout/theme.liquid, sections/senseless-product-hero.liquid, and the 5 product templates. The last three are reviews-guard locked and untouched.
  - reviews-guard.lock: rewritten by `deploy.sh --reviews-changed`. Commit it IMMEDIATELY after the deploy, in its own commit, following the a511a95+4950e15 and 4b3ed61+ddf2c41 precedents.
  - reviews-guard.manifest (OPTIONAL, decision 6): add `REPO | snippets/senseless-structured-data.liquid | class="jdgm-server-jld"` in the same commit as the snippet change.
  - DECISIONS-LOG.md: add a new decision under the session date. It covers the ProductGroup/hasVariant change on the 5 base URLs only, the gate, why ?variant= URLs are unchanged (22 Sep Decision 6), the commits and the lock, the RRT results (screenshots or counts), the census delta, and the MC re-check dates. Also note that the 20 Sep study's V14 text 'One Product with N Offers' went stale at a511a95 and is now resolved.
  - docs/SECTIONS.md:76-77: change 'Emits Product+Offer (PDPs)' to 'ProductGroup + hasVariant on the base URL of two-size PDPs; Product + 1 selected-variant Offer on ?variant= URLs and single-variant PDPs'.
  - docs/AUDIT-STORE-MC-ADS-2026-09-23.md item 4 (lines 225-231) and :324: mark as DONE, with the commit hash and the fact that the GTIN premise was superseded by 0a31b9e. docs/GOOGLE-ADS-MC-AUDIT-2026-09-20.md V14 (:82): add a one-line 'superseded' note, or record it in DECISIONS-LOG only (reconcile sweep).
  - NEXT_SESSION.md: record what was done and schedule the MC re-check (+2–3 d, +7 d) and the GSC re-check (+7–14 d). Add a gotcha: 'Never put the ProductGroup on ?variant= URLs until MC shows gtin = gtin13 for BOTH sizes with 0 price/GTIN issues for 7 days, and then do it one product at a time (Phase 2).' Add a second gotcha: 'renaming the Size option or adding a second option silently turns the group off'.
  - Notion write-back: update the State Surface (what is live, commits, open re-checks) at the task boundary, per CLAUDE.md. No Project Instance change is needed.
  - Scratch hygiene, outside the repo: /private/tmp/claude-501/-Users-matrixhealth-code-senseless-theme/4ae5dea4-c71e-4b16-85a2-90992fcf5da6/scratchpad/pg/design-minimal-change/theme/ is a full theme copy that INCLUDES a copy of .env (478 bytes) and .secrets/. Delete that directory. The judge did not delete it because deletion wasn't asked for.

## 6. Step-by-step plan

- 0. SESSION START. Ask which machine (Mac mini or MacBook Pro), run scripts/reconcile.sh and review the report. Read the Project Instance and the State Surface header. One task this session: ProductGroup Phase 1.
- 1. VERIFY-STORE GATE: the Shopify MCP get-shop-info must equal senseless-numbing.myshopify.com. Alternatively, run `./scripts/refresh-token.sh` and read shop.json myshopify_domain, or `shopify theme list --store senseless-numbing.myshopify.com` must show MAIN #199324434780. Check that `.env` keys are present (check key presence only, never print values). Check git: main is clean, HEAD is at or after 0a31b9e, and origin/main is equal.
- 2. PRECONDITIONS. `shasum -a 256 snippets/senseless-structured-data.liquid` must print e0e50e770b7ee88f818bfde056cda4f4804547dba956d58d54350532a6d4f9d2. The Asset API copy of the same key must be byte-equal to the repo (live == git).
- 3. DECISIONS 1–6 confirmed with the founder; the MC read-only pre-checks (decision 3) are done and recorded. If any go/no-go fails, stop here and write back.
- 4. BEFORE-CAPTURE, to scratch (never into the repo), taken immediately before editing:
- the 27 PDP URLs (17 base + 10 ?variant=), plus `/collections/numbing-gel/products/clinical-strength-gel?variant=57777076568412` and `/products/advanced-strength-gel?variant=57777076961628&srsltid=test&utm_source=x`;
- fetch them with rotating UA and a cb= cache-bust (the pg/live fetch.py pattern);
- save per URL: the jdgm-server-jld @graph, the FAQPage block, og:price:amount and the canonical;
- then run `python3 scripts/jsonld-census.py <scratch>/before.json` and `python3 scripts/injectable-clean-sweep.py --json <scratch>/sweep-before.json`.
- 5. EDIT. Apply E1 and E2 from liquid_draft with the Edit tool, plus E3 if decision 6 is yes. Check:
- `grep -c 'class="jdgm-server-jld"'` returns 1;
- `product.metafields.reviews.rating` is present;
- the sha256 is db5291d97804139501730d9cbc1388c2077ed2b0d4bfe250ddc280324ff13881 (a mismatch is acceptable only if the render checks in step 6 pass).
- 6. LOCAL PROOF (no deploy yet).
(a) liquidjs render harness (from …/pg/judge/harness, or re-create it) against a fresh .js and graph capture: 22/27 renders byte-identical, 5 ProductGroups with 2 Offers each, valid JSON, 0 dangling @ids, 0 injectable handles.
(b) Judge.me V() simulation: 0 rewrites.
(c) `shopify theme check` on a scratch copy made with rsync that EXCLUDES .env, .secrets, .venv and .git: 119 errors / 78 warnings, 0 offences in the snippet. Delete the copy afterwards.
- 7. RICH RESULTS TEST, CODE MODE (a gate). Paste each of the 5 rendered base-URL documents into https://search.google.com/test/rich-results (Code tab); the judge's copies are in …/pg/judge/rrt-code/. Expected: Merchant listings '2 valid items' named '<title> - <size>' with 0 warnings, Product snippets 2 items, and Breadcrumbs/Organization unchanged. Apply decision 4's rule. Record the screenshots.
- 8. COMPLIANCE. Confirm there is no new user-facing copy. The only new strings are '<product title> - <size>', which are existing product titles plus Shopify size values. Run the compliance-check skill on the 10 variant names for the record ("numbing" doesn't appear).
- 9. COMMIT: the snippet, plus the manifest if E3 is applied. The message covers what and why, cites DECISIONS-LOG 22 Sep Decision 6, and ends with the Co-Authored-By line from the session reminder. Then `git push origin main`. The push does NOT deploy.
- 10. DEPLOY: re-run the store gate, then `bash ./scripts/deploy.sh snippets/senseless-structured-data.liquid --reviews-changed`. Run it under bash with the path written literally. deploy.sh rewrites reviews-guard.lock. If auto mode blocks the deploy, give the founder that exact command to run with `!`.
- 11. LOCK: IMMEDIATELY `git add reviews-guard.lock`, commit 'reviews-guard.lock: re-pin senseless-structured-data.liquid (ProductGroup, <hash>)', and push. Check that `git status` is clean and origin equals local.
- 12. ASSET-API DIFF: GET `/admin/api/2024-10/themes/199324434780/assets.json?asset[key]=snippets/senseless-structured-data.liquid`. `.asset.value` must be byte-equal to the repo file, and the live copy must contain `class="jdgm-server-jld"` exactly once. deploy.sh's own 'success' is not proof.
- 13. LIVE VERIFICATION, within 10 minutes: steps 1–11 of verification_plan. On ANY failed gate, run the rollback immediately and investigate afterwards.
- 14. GSC: run URL Inspection, then Request indexing, for the 5 base URLs.
- 15. RECORDS: DECISIONS-LOG, docs/SECTIONS.md, audit docs, NEXT_SESSION.md (done, next Work Item = the MC/GSC re-checks and the Phase 2 decision, gotchas), then the Notion State Surface write-back. Commit and push the records.

**Plan amendments (critic, binding):**
- Run the Asset-API byte diff (step 12) BEFORE committing the lock (step 11): `deploy.sh` rewrites the lock before the push, and a push
  can report success after a silent no-op — never commit a lock for a file that isn't live.
- Add the **12 single-variant `?variant=<id>` URLs** (they are MC landing pages too) to `live/targets.json`, the before/after captures
  and verification step 1 — the 23 Sep precedent checked 39 PDP URLs; the spec's 27 drops them.
- Verification step 1's 'parse-equal the before-capture' will false-trigger on data that legitimately moves between captures
  (Judge.me rating sync, availability, a price edit). Compare structure + the fields this change could touch; explain any value
  drift from the product's own `.js` before calling it a failure.
- Expected RRT item types per PDP also include **Local businesses** (the OnlineStore Organization) — 5 types today.
- `scripts/jsonld-census.py` crawls the sitemap only (never `?variant=`) and does not count ProductGroup nodes or Offers nested in
  `hasVariant`; use the harness + a per-URL assertion script for those counts.

## 7. Verification plan

- 1. 22 SEP PRICE GUARD, all 10 ?variant= URLs:
- 4–6 sequential fetches each, varied UA plus cache-bust.
- The class-marked @graph must PARSE-EQUAL the step-4 before-capture.
- The whole page (all ld+json blocks, recursively) must hold exactly 1 Offer, whose sku, gtin13, price and url are that variant's:
  - S10CL 19.99, S30CL 44.99
  - S10AD 24.99, S30AD 49.99
  - S15CL 19.99, S35CL 34.99
  - SG15AD 24.99, SG35AD 39.99
  - SG15PR 29.99, SG35PR 44.99
- og:price:amount equals that price, and the canonical is the base URL.
- The collection-scoped URL and the srsltid/utm-tagged variant URL also show 1 top-level Product and 1 Offer.
- ANY difference: roll back.
- 2. UNCHANGED PAGES: the 12 single-variant base PDPs parse-equal the before-capture (kits, sprays, cleanser, bag, VAD, Professional cream).
- 3. THE 5 BASE URLs each show:
- exactly 1 `script.jdgm-server-jld`;
- a top-level node at …#product with @type exactly "ProductGroup";
- 0 top-level Product nodes;
- hasVariant of 2 with v1 (the smaller size) first, and the prices, GTINs (GS1 5065028388xxx) and shipping bands as in markup_example_base;
- aggregateRating on the group ONLY for clinical cream 4.85/13, advanced cream 4.92/12 and professional gel 2.0/1, and none on the sizes;
- og:price:amount, the canonical and og:url unchanged from the before-capture.
- 4. JUDGE.ME HEADLESS RENDER. Use puppeteer-core with the installed Chrome; this repeats the 66aa9b8 method. Pages: the 5 base URLs, plus 2 ?variant= URLs (clinical cream 30g, advanced gel 35ml), plus professional-strength-cream. After #judgeme_product_reviews mounts and the network is idle, check:
- the jdgm-server-jld script's textContent equals the server HTML's, so V() rewrote nothing;
- there is no `script.jdgm-aggregate-rating-jld`;
- the page holds exactly 1 aggregateRating;
- the widget renders (the manifest LIVE markers jdgm-widget and jdgm-preview-badge on clinical-strength-cream).
Kill headless Chrome afterwards.
- 5. RICH RESULTS TEST, URL MODE, on all 15 URLs:
- 5 base URLs: Merchant listings '2 valid items' with 0 warnings; Product snippets 2 items, with only the accepted aggregateRating/review class.
- 10 ?variant= URLs: Merchant listings '1 valid item' with 0 warnings, the same as today.
- Apply decision 4's rule. A new Merchant listings class means roll back. Record the results in DECISIONS-LOG.
- 6. JSON-LD CENSUS: `python3 scripts/jsonld-census.py <scratch>/after.json`, then diff against before.json by @type/@id (never by @graph index). Expected:
- Offers +5 in total (the 5 base PDPs go from 1 to 2 each);
- 5 ProductGroup nodes;
- 0 parse errors, 0 dangling @id, 0 entity leaks, 0 priceValidUntil;
- every other URL unchanged, including all collection ItemLists.
- 7. AD-FACING, both passes are required:
- Pass 1: `python3 scripts/injectable-clean-sweep.py --json <scratch>/sweep-after.json` must exit 0 with 0 breaches.
- Pass 2: grep every ld+json block in after.json, plus the 10 ?variant= captures, for numbing-cream-for-injections, numbing-cream-for-lip-fillers and numbing-cream-for-botox. Expect 0 on every ad-facing URL. BreadcrumbList parents are unchanged: advanced-* go to /collections/advanced, clinical/professional to /collections/aesthetic-numbing-cream.
- 8. THEME AND DEPLOY INTEGRITY: theme-check is at the 119/78 baseline, the Asset-API diff is byte-equal, the reviews-guard lock is committed and git is clean, and deploy.sh's post-deploy LIVE markers pass.
- 9. MERCHANT CENTER after recrawl, read-only in the founder's Chrome, at +2–3 days and +7 days. For each of the 10 items check:
- no 'Mismatched product price', 'Insufficient match of microdata price information', availability mismatch or GTIN issue;
- automatic item update history shows nothing new;
- the product total equals the baseline;
- 'More found by Google' still holds only the VAD 4-pack.
If ANY price issue appears on any size, roll back first and analyse afterwards.
- 10. SEARCH CONSOLE at +7–14 days:
- Merchant listings and Product snippets valid items each up by about 5 against the post-27–30 Sep baseline;
- 0 invalid, and no new issue types;
- URL Inspection on each base URL shows the ProductGroup detected.
Keep this separate from the barcode and 23 Sep batch re-checks.
- 11. EVIDENCE: save the before/after captures, census diffs, RRT screenshots and headless results under scratch, and summarise the counts in DECISIONS-LOG. Never claim a render fact that wasn't observed live (two-auditor split).

## 8. Rollback

TRIGGER: any failed gate in the verification plan, or any MC price or GTIN issue at the re-checks.

STEPS:
1. `git revert <snippet commit>`. If E3 was part of that commit, the revert removes the manifest marker too, which is fine.
2. `git push origin main`.
3. Pass the store gate.
4. Run `bash ./scripts/deploy.sh snippets/senseless-structured-data.liquid --reviews-changed`. The lock rewrites back to e0e50e770b7ee88f818bfde056cda4f4804547dba956d58d54350532a6d4f9d2.
5. Commit and push reviews-guard.lock immediately.
6. Run the Asset-API byte diff.
7. Re-fetch the 27 PDP URLs. They must parse-equal the before-capture.
8. Re-run the RRT on one base URL (expect 1 Merchant listings item, as before).

Nothing in Merchant Center, the feed, Shopify product data or Notion structure changed, so there is nothing else to undo. deploy.sh never deletes files, and no new file was added. Target: back to the pre-change live state within about 15 minutes of the trigger.

Log the rollback and its cause in DECISIONS-LOG and NEXT_SESSION, and write it back to the State Surface.

## 9. Risks

- **Merchant Center actually reads the BASE URL for some item, either because the feed `link` for a smaller size is the bare URL or because MC follows the canonical. The base URL now carries 2 Offers, which is the shape of the 22 Sep incident.** — Decision 3 pre-check of the MC export `link` column, with no-go if any link is bare. Even in the adverse case, since 0a31b9e both Offers carry the GS1 gtin13 that MC has synced, so Help 7331077's documented multi-offer GTIN match applies. The first Offer is also v1, the smaller, cheapest size the base page shows, so a first-offer or cheapest fallback lands on the right price as well. Evidence that MC reads the landing URL, not the canonical, is circumstantial: the 35ml mismatch cleared while the base URL still showed only the 15ml. MC re-checks at +2–3 and +7 days; any price issue means roll back.
- **Shopify sets `product.selected_variant` differently from the docs, for example nil on some ?variant= URLs. Those MC landing pages would then get the 2-Offer group.** — Verification step 1: all 10 ?variant= URLs, a collection-scoped URL and a tracking-param URL must parse-equal the before-capture and hold exactly 1 Offer, checked within 10 minutes of deploy. Any difference means immediate rollback. The gate fails safe in the other direction: if selected_variant is set unexpectedly, the page falls back to today's Product.
- **Google's single-page model assumes identical markup on every variant URL. Our ?variant= duplicates carry a single-size Product at the same #product @id that is a ProductGroup on the canonical. How Google treats differing markup on non-canonical duplicates is undocumented.** — Low: Google indexes the canonical (base) URL, and the facts on the ?variant= pages agree with the group's nested size. Watch RRT URL mode and GSC. Phase 2 (the full group everywhere through the GTIN route) removes the divergence once MC is proven.
- **The same @id (<base>/products/<h>#product) is typed ProductGroup on base PDPs but Product, with a single min-price Offer, in collection ItemLists and on ?variant= URLs.** — ProductGroup is a schema.org subtype of Product, so the other declarations are less specific rather than contradictory. Google documents no cross-page @id merging. Monitor GSC. Mirroring the group into ItemLists (the D2 idea) is an optional follow-up in its own session.
- **The Rich Results Test flags a new warning class on the nested sizes: a missing brand, or aggregateRating not inherited from the group.** — Code-mode RRT before deploy (plan step 7) with the decision-4 rule. aggregateRating/review on Product snippets is the accepted pre-existing class (GSC 89/89). Adding brand to each size is a pre-authorised one-line fix, re-tested in code mode. Any other new Merchant listings class means no deploy (the priceValidUntil precedent).
- **At runtime Judge.me's V() normaliser, or a changed bundle, rewrites the group or injects a second aggregateRating. That would reopen the 4 Sep 'multiple aggregate ratings' incident.** — @type is exactly "ProductGroup", the @id stays #product and the sizes are nested. The verbatim V() simulation rewrote 0 of 27 renders. The real headless-Chrome check (verification step 4) compares textContent before and after the widget mounts and requires no jdgm-aggregate-rating-jld script and exactly 1 aggregateRating. Confirm which bundle is live before reasoning about it.
- **reviews-guard gap: `--reviews-changed` accepts any edit to the locked snippet, including one that drops class="jdgm-server-jld".** — Decision 6: add the class as a REPO marker in reviews-guard.manifest. Otherwise check it by hand with grep in the repo, the Asset API copy and the live HTML (plan steps 5 and 12, verification step 3).
- **Confounded attribution. MC is still re-processing today's GS1 barcode load (0a31b9e), and the 27–30 Sep GSC/MC re-check expects unchanged counts. Deploying now mixes three changes.** — Decision 1: deploy after both re-checks are recorded clean. Otherwise log the expected deltas (+5 Merchant listings, +5 Product snippets, 0 MC change) in DECISIONS-LOG before deploying, and take the before-capture immediately before the edit.
- **Silent loss. Renaming the "Size" option, adding a second option, or making the Liquid gate never fire puts the larger sizes back out of Search with no error.** — The gate comment documents it, NEXT_SESSION gets a gotcha, and the GSC valid-item count (+5) is watched as the success metric. A later re-run of jsonld-census that shows 0 ProductGroup nodes flags it.
- **Liquid semantics were proven in liquidjs, not Shopify: `continue` inside a nested loop over a (1..2) range, `unless` on an object, and `options_with_values.size`.** — `shopify theme check` (Shopify's parser) passes with 0 offences on the snippet. The live check of the 5 base URLs (verification step 3) is the real proof. The else-branch is untouched, so a failing group branch cannot affect MC landing pages; if the group output is malformed, roll back.
- **Payload: each base PDP's head grows by about 2 KB (clinical cream went from 8,859 to 10,924 bytes of ld+json), because each size repeats the description.** — Accepted. Google recommends a description per variant, and a Shopify community report (not a Google doc) shows 'missing description' warnings on variants that lack one. Only 5 URLs are affected.
- **Secret hygiene: a scratch theme copy at …/scratchpad/pg/design-minimal-change/theme/ contains a copy of .env and .secrets/.** — Delete that directory. Any future scratch theme-check copy must use rsync with --exclude '.env' --exclude '.env.*' --exclude '.secrets' --exclude '.venv' --exclude '.git' (the judge's copy did, and was deleted after use).
- **More found by Google (the MC crawl source) could create extra crawled items from the base-URL group, as it did for the VAD 4-pack.** — All 10 sizes are already feed items with matching GTINs, so this isn't expected. Check that the MC product total and the 'More found by Google' count stay at baseline at the MC re-checks, and that 'Allow ads' stays unaccepted.

## 10. Critic's other findings (non-blocking)

- Re-verified independently from a copy (…/scratchpad/pg/adversarial/harness):
- Applying E1 and E2 to the repo file (sha e0e50e77…, which equals reviews-guard.lock:25) gives exactly db5291d97804139501730d9cbc1388c2077ed2b0d4bfe250ddc280324ff13881.
- The orig render equals live on 26/27; the one miss is VAD '2' vs '2.0'.
- Draft vs orig: 22/27 byte-identical. The 5 base URLs become ProductGroups with the prices, GTINs and bands in markup_example_base, and nodes 1–9 are parse-equal to today.
- More edge cases rendered; all give valid JSON with 0 dangling @ids:
- all variants unavailable: 2 Offers, both OutOfStock;
- no sku and no barcode: valid JSON, but no unique variant ID;
- 3 sizes with the first sold out: v1 = 35ml listed first, commas correct;
- quotes, & and <> in the product and variant titles: escaped correctly;
- no images: sizes emit no image;
- option named ' SIZE ': grouped;
- a ?variant= URL whose selected size is sold out: byte-identical to orig.
- MC safety on ?variant= URLs is stronger than the spec claims. Live, ?variant=57777075257692 renders S30CL/44.99 while the base URL renders S10CL. selected_or_first_available_variant can only return the non-first size if product.selected_variant is set, so the gate (`unless product.selected_variant`) cannot fire on the larger-size landing pages. For ?variant=<smaller size> URLs, live can't tell the difference. Verification step 1 covers that case, and its worst case is 2 GTIN-annotated Offers with the correct size first.
- Live pages (GET, 23 Sep) contain:
- exactly 2 ld+json blocks: the jdgm-server-jld @graph and the FAQPage;
- 0 itemprop/itemtype microdata, so '1 Offer on the whole page' holds;
- og:price 19.99 on the clinical cream base URL, 44.99 on its 30g URL, and 39.99 on the advanced gel 35ml URL;
- canonical = base URL, including on /collections/numbing-gel/products/clinical-strength-gel?variant=… and on the srsltid/utm URL, which both show 1 Offer today.
- No second Product emitter: the product templates don't use sections/product-information, featured-product or featured-product-information (the Horizon sections that call `structured_data`), and templates/product.quick-add.liquid is `layout none`. Exactly 5 of the 17 live products have more than 1 variant. build-your-own-bundle has 1 variant, so it takes the else branch.
- Judge.me:
- The live bundle is still judgeme-762. In the fetched bundle, only ReviewWidgetManager touches ld+json.
- K() returns null whenever any script.jdgm-server-jld exists (k()), whatever the @type.
- V() rewrites only top-level nodes whose @type === 'Product' or whose @type array includes 'Product'. A 'ProductGroup' node and the nested hasVariant Products are never touched.
- Re-running simV.cjs on my renders: 0/27 rewritten.
- E3 works with deploy.sh:
- Gate (a) (deploy.sh:52-60) splits on '|' and does a substring check.
- Gate (b) (deploy.sh:130-146) keeps a list of markers per path.
- The lock repeats the path, as config/settings_data.json already does 4 times.
- Caveat: it is a whole-file substring check, so a future comment that contains the literal `class="jdgm-server-jld"` would also satisfy it.
- theme-check, re-run on a secret-free rsync copy (assets excluded; deleted afterwards): the only snippet offence before and after is MissingAsset (senseless-logo.png, an artefact of excluding assets), at row 183 before and 186 after. That proves the draft was the file checked, and it adds no new offence. The judge's tc/orig.json and tc/new.json are both exactly 80,608 bytes, so those files alone can't show the draft was swapped in; this re-run settles it.
- All 10 GS1 gtin13 values have valid check digits, and the live /products/<h>.js matches the spec's table (SKUs, prices, barcodes, option 'Size', featured_image null).
- Verification step 1 ('the class-marked @graph must PARSE-EQUAL the before-capture … ANY difference: roll back') will false-trigger on data that can change between the before- and after-captures: Judge.me rating_count/rating sync, availability, a price edit, or an image ?v= bump. Compare with those fields masked, or re-read the product .js and re-render orig before treating a difference as a rollback trigger. The 'exactly 1 Offer with the right sku/price/url' assertion is the real MC guard.
- Step order: deploy.sh gate (c) rewrites reviews-guard.lock BEFORE the push (deploy.sh:98-103). The push is known to report 'success' after a silent no-op. Run step 12 (Asset-API byte diff) before step 11 (commit the lock), so the lock is never committed for a deploy that didn't land.
- Expected RRT results should also list 'Local businesses' (the OnlineStore Organization). NEXT_SESSION 23 Sep shows 5 valid item types per PDP: Product snippets, Merchant listings, Breadcrumbs, Local businesses, Organization.
- Records sweep:
- The spec cites docs/AUDIT-STORE-MC-ADS-2026-09-23.md ':324', but line 324 is the DONE schema-quality batch. The ProductGroup follow-up is line 327 (item 5); item 4 is at lines 225-231.
- Also mark docs/GOOGLE-ADS-MC-AUDIT-2026-09-20.md:239 ('Restructure variants into ProductGroup only if MC shows price issues on the second sizes (V14)') as superseded.
- Secret hygiene, confirmed: /private/tmp/…/4ae5dea4…/scratchpad/pg/design-minimal-change/theme/.env (478 B, 0600) and .secrets/ exist.
- Delete them in THIS session, with user OK. The next session gets a different scratchpad, so the item shouldn't be handed to it.
- Delete only theme/: judge/harness/node_modules is a symlink into design-minimal-change/harness/node_modules.
- No other .env copies are in pg/; only .env.example files remain elsewhere.
- scripts/jsonld-census.py takes one argument (the output file) and crawls the sitemap only, so it never sees ?variant= URLs. It prints totals (offers, dangling, pvu) but doesn't count ProductGroup nodes or diff runs. The assertions '5 ProductGroup nodes' and 'every other URL unchanged, including collection ItemLists' need a small diff script over the 'docs' in before.json and after.json.
- Unverified, and not in the spec: how Bing / Microsoft Shopping and answer engines handle ProductGroup + hasVariant on the 5 base URLs. The file's header calls itself the GEO/SEO layer. It's standard schema.org, but consumers other than Google may drop the nested Offers.
- The 'Mismatched product price' incident is better evidence than 'circumstantial' for MC reading the feed landing URL rather than the canonical. After a511a95, the base URL still showed only 15ml £24.99, yet the 23 Sep MC state shows 'no price or markup issues'. It still doesn't prove the smaller sizes' feed link isn't the bare base URL, so keep the decision 3(a) link check.

Liquid-draft notes:
- 'WHAT MUST STAY: Line 160 `class="jdgm-server-jld"`': after E1 adds 3 lines, the tag is at line 163 in the draft (grep -n confirmed). The grep -c check (=1) is the right assertion; drop the line number.
- Each nested size's description is the group description verbatim. Google's variants doc says 'Make sure that the variant description is more specific and ideally uses words that identify the variant'. It's a recommendation, not an RRT error, and adding size wording would be new copy (compliance-check). Acceptable as drafted; note it.
- No fallback unique ID: if a size ever has neither sku nor barcode, the draft still renders valid JSON (tested), but it breaks Google's 'Each variant must have a unique ID … (for example, using the sku or gtin properties)'. Every size has both today; optionally add a guard, or a gotcha in NEXT_SESSION.
- If the product and the variant both lack an image, the sizes emit no image, and image is a required Merchant listings property. That is the same outcome as today's Product; noted only.
- productGroupID is the bare numeric product id. The feed's item_group_id form (for example shopify_ZZ_… vs numeric) is unverified. Google doesn't require them to match, but decision 5 should be settled from the MC export in decision 3.
- The Offer body is now duplicated in two branches ('change one, change both'). Keeping the else branch byte-identical justifies it, but it is a standing maintenance trap. The NEXT_SESSION gotcha should name both branches.
- Size uses schema.org `size`, which Google's merchant-listing doc frames around apparel (sizeSystem/sizeGroup). It's still the only fitting value in the supported variesBy list, and MC allows size for non-apparel size variants. No change, but watch for any size-related MC/GSC diagnostic.

Missing from the plan (now folded into §6 amendments where binding):
- Durable artefacts. Step 6(a) (local proof) and step 7 (the RRT code-mode GATE) depend on files in this session's ephemeral scratchpad (/private/tmp/…/4ae5dea4…/scratchpad/pg/judge/{harness,live,rrt-code}); the next session gets a different scratchpad and /private/tmp may be cleared. Copy them now to a durable location outside the repo, or add an explicit re-creation recipe to the plan:
- the liquidjs `json` filter emulation (\/ plus & < > escapes);
- the image_url and asset_url emulation;
- the date '%z' stub;
- the mock built from /products/<h>.js plus the live graph's rating and breadcrumb;
- a fidelity check (orig render == live on 26/27) before trusting any draft render.
Re-render the RRT code documents from fresh data on the day, because ratings, stock and prices may have moved by 27–30 Sep.
- Add the 12 single-variant ?variant=<id> URLs (MC landing pages too) to the before and after captures and to verification step 1. The 23 Sep precedent verified 39 PDP URLs (22 ?variant= + 17 base); the spec's 27-URL set drops 12 of the ?variant= URLs.
- The RRT rating-detection check on the 3 rated base URLs (see the blocking problem), recorded in DECISIONS-LOG next to the item counts.
- OPTIONAL, founder decision: prove the real Shopify Liquid semantics BEFORE going live with an unpublished duplicate theme and ?preview_theme_id= renders of the 5 base and 10 ?variant= URLs. It would test selected_variant nil on the base URL, the nested `continue`, and options_with_values on Shopify's own parser rather than liquidjs; precedent: throwaway preview theme #200345092444, since deleted. It is a Shopify write and sits outside the main==live model, so it needs explicit approval; otherwise the live check within 10 minutes stays the only real-Shopify proof, as the spec says.
- A diff tool for the census (by @type/@id per URL, counting ProductGroup nodes and Offers nested in hasVariant). jsonld-census.py doesn't do this.
- Verification step 9 is partly unverifiable as written:
- 'automatic item update history shows nothing new' needs a named MC screen. MC Next exposes automatic-improvement counts in settings, not a per-item history; mark it unverified if the screen doesn't exist.
- The 'More found by Google' count needs a named location too.
- Attribution: step 10's 'about +5' in GSC Merchant listings and Product snippets is unverifiable if the deploy lands inside the window of the barcode re-check and the 23 Sep batch re-check. Decision 1's 'deploy after both re-checks are recorded clean' should be a hard precondition, or the expected deltas must be logged first; the spec says this but leaves it to the founder.

## 11. Evidence

### Google (fetched 23 Sep 2026; product-variants doc 'Last updated 2026-09-08')

- "Single page, where all variants are selectable on a single page without page reloads (usually through query parameters)" — https://developers.google.com/search/docs/appearance/structured-data/product-variants
- "Multi page, where variants of the same product are accessible on different pages" — https://developers.google.com/search/docs/appearance/structured-data/product-variants
- "When the user selects a different variant on the page (using dropdowns for color and size), the image, price, and availability information change dynamically on the page without a page reload. The markup on the page doesn't change dynamically as the user selects different variants." — https://developers.google.com/search/docs/appearance/structured-data/product-variants
- "The ProductGroup and three Offer entities (under the Product properties) all have distinct URLs. Alternatively, the URLs could have also been provided under Product." — https://developers.google.com/search/docs/appearance/structured-data/product-variants
- "The ProductGroup specifies the parent sku using productGroupID (which doesn't need to be repeated under the Product properties using inProductGroupWithID)." — https://developers.google.com/search/docs/appearance/structured-data/product-variants
- "We recommend this approach because it's the most compact and natural representation of a product group and its variants." — https://developers.google.com/search/docs/appearance/structured-data/product-variants
- "This structure is similar to the previous example except the variants are defined separate (unnested) from the ProductGroup. This approach might be easier for some content management systems (CMSes) to generate." — https://developers.google.com/search/docs/appearance/structured-data/product-variants
- "ProductGroup doesn't have a canonical URL, as there isn't a single URL representing the ProductGroup. / The ProductGroup on each page has a full definition of the variants on the page as well as a variant with only the url property to link to the variants on the other page, which helps Google find your variants. [multi-page example]" — https://developers.google.com/search/docs/appearance/structured-data/product-variants
- "Each variant must have a unique ID in its corresponding structured data markup (for example, using the sku or gtin properties)." — https://developers.google.com/search/docs/appearance/structured-data/product-variants
- "Each product group must have a unique ID in its corresponding structured data markup, specified with the inProductGroupWithID property in variant Product properties or the productGroupID property in the ProductGroup property." — https://developers.google.com/search/docs/appearance/structured-data/product-variants
- "Be sure to add Product structured data in addition to the product variant properties, following the list of required properties for merchant listings (or product snippets)." — https://developers.google.com/search/docs/appearance/structured-data/product-variants
- "For single-page sites, there must be only one distinct canonical URL for the overall ProductGroup that all variants belong to. Typically this is the base URL that leads to a page without a variant pre-selected, for example: https://www.example.com/winter_coat. For multi-page sites, this doesn't apply since there is no single canonical URL representing the ProductGroup property (since the variants are distributed across equally important pages)." — https://developers.google.com/search/docs/appearance/structured-data/product-variants
- "The site must have the ability to preselect each variant directly with a distinct URL (using URL query parameters), for example https://www.example.com/winter_coat/size=small&color=green. This allows Google to crawl and identity each variant. Preselecting each variant includes showing the right image, price, and availability, as well as allowing the user to add the variant to the cart." — https://developers.google.com/search/docs/appearance/structured-data/product-variants
- "Required properties — name — The name of the ProductGroup (for example, "Wool winter coat"). Make sure that the name of the variants in each Product item is more specific (for example, "Wool winter coat - green, size small", based on the variant-identifying properties." — https://developers.google.com/search/docs/appearance/structured-data/product-variants
- "A nested aggregateRating of the ProductGroup (which is representative of all variants), if applicable." — https://developers.google.com/search/docs/appearance/structured-data/product-variants
- "ProductGroup also lets you specify common product-properties for all variants, such as brand and review information, as well as the variant-determining properties, which can reduce the duplication of information." — https://developers.google.com/search/docs/appearance/structured-data/product-variants
- "The identifier of the product group (also known as the parent sku). This identifier must be provided for the ProductGroup property or, alternatively, using inProductGroupWithID property for variants of the ProductGroup property. If you provide the identifier for both the ProductGroup property and its variant Product properties, they must match." — https://developers.google.com/search/docs/appearance/structured-data/product-variants
- "For single-page websites only: The URL (without variant selectors) where the ProductGroup property is located, if applicable. Don't use this property for multi-page websites." — https://developers.google.com/search/docs/appearance/structured-data/product-variants
- "Aspects by which the variants in the ProductGroup vary, (for example, size or color), if applicable. Reference these variant-identifying properties through their full Schema.org URL (for example, https://schema.org/color). The following properties are supported: ... https://schema.org/size" — https://developers.google.com/search/docs/appearance/structured-data/product-variants
- "In addition to the description of the ProductGroup, we recommend also adding a description of each variant at the Product level." — https://developers.google.com/search/docs/appearance/structured-data/product-variants
- "Product snippets accept an Offer or AggregateOffer but merchant listings require an Offer as the merchant has to be the seller of the product in order to be eligible for merchant listing experiences." — https://developers.google.com/search/docs/appearance/structured-data/merchant-listing
- "A URL of the product web page from which a shopper can purchase the product. This URL may be the preferred URL for the current page with all variant options appropriately selected. The URL can be omitted. Don't provide multiple URLs." — https://developers.google.com/search/docs/appearance/structured-data/merchant-listing
- "Product rich results only support pages that focus on a single product (or multiple variants of the same product). For example, "shoes in our shop" is not a specific product. This includes product variants where each product variant has a distinct URL. We recommend focusing on adding markup to product pages instead of pages that list products or a category of products." — https://developers.google.com/search/docs/appearance/structured-data/merchant-listing
- "The ID of a product group that this product variant belongs to. See also Item Group Id in Google Merchant Center Help. Specify at most one value." — https://developers.google.com/search/docs/appearance/structured-data/merchant-listing
- "Unlike product snippets, merchant listing experiences require a price greater than zero." — https://developers.google.com/search/docs/appearance/structured-data/merchant-listing
- "End date and time: Use either the validThrough property or the priceValidUntil property. ... Provide both a start and an end date/time to clearly define the sale period." — https://developers.google.com/search/docs/appearance/structured-data/merchant-listing#sale-duration
- "Don't use AggregateOffer to describe a set of product variants." — https://developers.google.com/search/docs/appearance/structured-data/product-snippet
- "You only need to provide one of review, aggregateRating, and offers, but the product snippets section of the Rich Results Test may report a warning if you provide offers without review or aggregateRating properties." — https://developers.google.com/search/docs/appearance/structured-data/product-snippet
- "Do you offer variants of your products? Adding product variant structured data can help Google better understand which products are variations of the same parent product. Both product snippets and merchant listings support product variants." — https://developers.google.com/search/docs/appearance/structured-data/product
- "If you use optional query parameters to identify variants, use the URL with the query parameter omitted as the canonical URL. This can help Google better understand the relationship between product variants." — https://developers.google.com/search/docs/specialty/ecommerce/designing-a-url-structure-for-ecommerce-sites#how-google-understands-urls-for-product-variants

### How Merchant Center matches landing-page markup (the 22 Sep constraint)

WHAT MC DOES (Help 3246284): automatic updates use "the structured data markup found on your online shop and advanced data extractors". They cover price, sale price, availability and condition. MC finds "products on the product pages listed in your data source", i.e. the feed's link. For Senseless that is each variant's own ?variant= URL.

HOW MC MATCHES MARKUP TO A FEED ITEM (Help 7331077, the key rule for the 22 Sep incident): "In order for Google's crawler to match the structured data to your product data, the following conditions must be satisfied: There's a single offer on the landing page. If there are multiple offers on the whole page, each offer present on the page is annotated with a SKU or a GTIN and the respective offer in your product data on Shopping has the same SKU (ID [id] attribute) or GTIN (GTIN [gtin] attribute). ... If at least one of these conditions isn't met, the products on your landing page won't match your product data."
- Help 15071338 repeats it: "If there are multiple variants shown on the landing page, you can use the ID [id] or the GTIN [gtin] attribute to specify which variant a price corresponds to."
- Help 6386198 maps MC `id` to schema.org `sku`, and `item_group_id` to `inProductGroupWithID` ("A parent SKU, required to group all variant products").

SO, ON A ?variant= URL: if the page has ONE Offer, MC uses it. That is today's design and why the 22 Sep fix works. If the page has SEVERAL Offers, MC uses the one whose schema `sku` equals the MC item `id`, or whose `gtin` equals the feed gtin. Otherwise the documented result is "won't match". What MC then does is not documented. The 22 Sep evidence (DECISIONS-LOG Decision 6) is that it read the lower 15ml price on the 35ml URL. That fits Help 9773429's "price range → cheapest" guidance, but it isn't proven.

SENSELESS-SPECIFIC RISK (from repo docs, not re-checked live this session):
- The Google & YouTube item IDs are `shopify_ZZ_<product_id>_<variant_id>`. Source: docs/GOOGLE-ADS-MC-AUDIT-2026-09-20.md V22/N30 and snippets/senseless-structured-data.liquid:422-423. The schema `sku` is the Shopify SKU code, so a sku→id match fails for every variant.
- Only 3 of 22 variants have a barcode: S15CL, S35CL, SFOAM (docs/AUDIT-STORE-MC-ADS-2026-09-23.md:295).
- So a Google-style single-page ProductGroup with both Offers on every URL meets MC's documented multi-offer condition for at most one two-size product, Clinical Gel, and only if the feed's gtin equals the schema gtin13. The other 4 would reopen the 22 Sep "Mismatched product price" failure mode.
- MC landing-page rules also apply (Help 4752265): "If your landing page has multiple products on it, such as variants or similar items, the product in your product data should be the primary focus". Extra variant prices "should be clearly differentiable from the advertised base price". "make sure that the variant that matches the product data is the one that appears on your landing page by default". Help 6324416: "ensure that your microdata matches the variant displayed on your landing page".
- Help 3246284 gives one analogy: when a page shows multiple strikethrough prices, "You shouldn't enable automatic updates for price in this case."

OPTIONS FOR THE NEXT SESSION, all needing a decision:
(a) Load the GS1 UK GTINs (study N3, founder decision pending) so every variant Offer carries a gtin13 that matches the feed. This is the only documented way to make a multi-offer page match per variant.
(b) Keep ONE full Offer per URL (the selected variant) and add ProductGroup + hasVariant, with the non-selected size as a url-only variant stub. Google shows url-only stubs only in the MULTI-page example; mixing them into a single-page canonical setup is undocumented.
(c) Set the variant `sku` to the MC id `shopify_ZZ_…`. This matches the letter of Help 7331077 but misuses sku, which should be the merchant SKU.
(d) Turn off automatic price updates in MC. This is an account setting with its own risk.
Whichever is chosen, verify MC diagnostics afterwards. Nothing in Google's docs guarantees (b).

### Project history

- No ProductGroup or hasVariant has ever been emitted by either repo. `git log -S ProductGroup` and `-S hasVariant` in senseless-theme hit only four docs/records commits: 93bf0e4 (20 Sep study), 3debdd2 (23 Sep audit), d93b3d8 and 4c9835c (handoffs). There are 0 hits in theme code. Totally Numb's repo has 0 hits on both terms, including all branches.
- DECISIONS-LOG.md:48, 22 Sep Decision 6 (the hard constraint), verbatim: "Product schema: one Offer for the selected variant; og:price follows it (`a511a95` + lock `4950e15`, deployed with `--reviews-changed`). Merchant Center flagged \"Automatic updates: Mismatched product price\" on Advanced Strength Gel 35ml: the feed said £39.99, the \"online shop\" said £24.99. On the 35ml `?variant=` page, `og:price:amount` was `product.price` (lowest) and the JSON-LD listed both sizes with 15ml first. Now there is ONE Offer (`selected_or_first_available_variant`), `og:price` follows it, and the Offer name drops \"Default Title\" (study N29). Same fix as Totally Numb (6457125). Verified live on 21 URLs (8 products × canonical + each size): one Offer, the right SKU/price, and og:price equal on all."
- a511a95 diff (snippets/senseless-structured-data.liquid): it replaced `{%- for variant in product.variants -%}` (N Offers, smaller size first) with a single Offer built from `v1`. The code comment it added, now at lines 447-455, reads: "The other sizes are still reachable (the feed lists each variant's own ?variant= URL). Same fix as Totally Numb (21 Sep, 6457125)." v1 is assigned at :393 (`product.selected_or_first_available_variant | default: product.variants.first`). Product-level sku, mpn and gtin13 (:425-433) also follow v1. The Product @id is `canonical_url#product`, which is the same on the base URL and on ?variant= URLs; live 23 Sep, the ?variant=35ml page shows @id .../advanced-strength-gel#product with the SG35AD offer at £39.99.
- docs/GOOGLE-ADS-MC-AUDIT-2026-09-20.md:82, V14, verbatim: "p2 · Less explicit than ProductGroup; review against Google variant guidance | Confirmed (a modelling concern only) | One Product with N Offers; no ProductGroup or hasVariant. No GSC variant issue on record. The snippet is reviews-guard-locked (Judge.me fix 66aa9b8, @id wiring b19e710) | Founder (priority); CC | Low". The description "One Product with N Offers" is STALE since a511a95: it is now one Offer, and V14 was never updated. The PDF's own p2 wording was not re-read, because no PDF tool exists on this Mac.
- GOOGLE-ADS-MC-AUDIT-2026-09-20.md:239, the study's gating rule: "Restructure variants into ProductGroup only if MC shows price issues on the second sizes (V14)." The condition fired on 22 Sep: MC flagged a mismatch on a second size, Advanced Gel 35ml. The chosen remedy was the single selected-variant Offer, not ProductGroup. No record says ProductGroup was considered and rejected on 22 Sep.
- Other variant rows in the 20 Sep study. V12 (:80): "Product sku/mpn/gtin follow the selected-or-first-available variant ... and switch on `?variant=` URLs". V13 (:81): "True on the canonical URL. On `?variant=<35ml>` the same `#product` @id carries the 35ml GTIN". V15 (:83): "All 5 second-size URLs server-render the right size radio, price, sticky price, hidden variant id and SKU/GTIN. Gaps: `og:price:amount` stays at the lowest price, and both sizes share one image". V45 (:113) predicted the incident: "An extra risk, not observed: on `?variant=` pages the Offer list still starts with the smaller size". N28 and N29 (:191-192) are marked FIXED 22 Sep. N30 (:193) is still open: `productID` is `shopify_GB_<id>` but "The G&Y item IDs are `shopify_ZZ_<pid>_<vid>`".
- docs/AUDIT-STORE-MC-ADS-2026-09-23.md:225-231, item 4, verbatim: "Five multi-variant PDPs expose only the cheaper variant to Google. `?variant=` URLs emit the correct Offer but canonicalise to the base URL, and only base URLs are in the sitemap. So £44.99 clinical cream 30g, £49.99 advanced cream 30g, £34.99 clinical gel 35ml, £39.99 advanced gel 35ml, £44.99 professional gel 35ml — and the valid GTIN-13 on clinical gel 35ml — are structurally unindexable. Merchant Center is unaffected (the feed carries per-variant URLs). Fix: `ProductGroup` + `hasVariant`, keeping the selected variant's Offer. This touches exactly what the 22 Sep fix guarded, so it needs its own session and an MC re-check." :324 ranks it: "`ProductGroup` / `hasVariant` — the biggest upside; own session, MC re-check afterwards."
- NEXT_SESSION.md:45-47 (current handoff), verbatim: "Biggest upside, own session: `ProductGroup`/`hasVariant` for the 5 two-size PDPs (audit item 4) — run `scripts/jsonld-census.py` before and after, and re-check MC because it touches what the 22 Sep price fix guards." The same item first appeared in d93b3d8 and was expanded in 5918d68 (NEXT_SESSION.md:165-170).
- Default variant history. The DECISIONS-LOG entry is STALE. DECISIONS-LOG.md:191 (1 Jun 21:30) says "Variant default = 30g (reordered variants so 30g is position 1". DECISIONS-LOG.md:188 (1 Jun 23:10) says "Default variant = larger size (reordered: advanced-cream 30g, advanced/clinical/professional-gel 35ml; clinical-cream 30g already done". build-reports/wave-3-gel-spray.md:52 (2 Jun 11:02) flagged "If 15ml-first is preferred as the default price shown, reorder variants per product". Commit 7e079f2 (2 Jun 11:26) then did "Reorder variants smaller-size-first (10g/15ml) so cards default to the entry price." That was a Shopify data change, recorded only in the commit message and in build-reports/phase-4-prep-product-page-state.md:33-34 ("Reordered 10g-first" / "Reordered 15ml-first"). build-reports/phase13-full-site-audit.md:112 (6 Jun) says "variant-order (smaller-size-first)" matches canon. The DECISIONS-LOG entry was never marked superseded.
- Live check today (read-only GET of /products/<h>.js, 23 Sep): ALL FIVE two-size products are smaller-size first, not only the two that AUDIT-STORE-MC-ADS-2026-09-23.md:307-309 names. clinical-strength-cream: S10CL £19.99, then S30CL £44.99. advanced-strength-cream: S10AD £24.99, then S30AD £49.99. clinical-strength-gel: S15CL £19.99 (barcode 0767461321111), then S35CL £34.99 (barcode 0795847726144). advanced-strength-gel: SG15AD £24.99, then SG35AD £39.99. professional-strength-gel: SG15PR £29.99, then SG35PR £44.99. The only option on all five is "Size", each has 1 product image, and no variant has a featured_image. The audit's "DECISIONS-LOG.md:174" reference is now line 188.
- GTIN history. 20 Sep study V9 (:77): the three live gtin13 values are "all 13 digits and check-digit valid", but they are "zero-padded US-range UPCs (076…/079…). The owner's barcode sheet files them under \"OLD BARCODES\" with GS1 UK replacements". V10 (:78): 19 Offers have no GTIN, and the rule is "don't invent codes or set `identifier_exists=false`". N3 (:166): GS1 UK `5065028388xxx` codes exist for 16 variants, "Totally Numb made the same switch on 21 Sep (TN DEC-53)". The founder decision is still open (study §5B item 3: scan a Clinical Gel 15ml and 35ml pack first). The 23 Sep audit (:295) says only S15CL, S35CL and SFOAM have a barcode. So the phrase "the only valid GTIN-13 on Clinical Gel 35ml" is imprecise. The Clinical Gel 15ml code is equally valid and is already visible on the base URL. Both are probably superseded codes.
- Reviews-guard and Judge.me constraints. 66aa9b8 (4 Sep) added class="jdgm-server-jld" after GSC raised "Review has multiple aggregate ratings", which is critical for Review snippets. Judge.me's widget "injects a second Product node onto our own @id (<page_url>#product) carrying just name + aggregateRating ... its @id resolver DOES walk @graph". The exact class string suppresses the injection; the commit measured a decoy class as a control. The Judge.me dashboard "SEO Rich Snippets" setting is also OFF, but that setting lives outside git. reviews-guard.manifest requires `REPO | snippets/senseless-structured-data.liquid | product.metafields.reviews.rating`. Current lock: ddf2c41. aggregateRating is emitted only when the count is above 0.
- b19e710 (19 Aug) fixed three GSC Merchant listings issues on the collection ItemList Products. It moved shipping and returns to page-level nodes referenced by @id, and cited Google's product-variants doc: "Google documents this exact pattern (search/docs/appearance/structured-data/product-variants)". DECISIONS-LOG.md:58 (22 Sep Decision 11): each Offer's shipping refs are chosen by that item's own price through snippets/senseless-shipping-refs.liquid (under £40, £40–£79.99, £80 and over).
- DECISIONS-LOG.md:28 (23 Sep Decision 2): priceValidUntil was shipped and then REVERSED. "Lesson: the schema.org validator passed it 0/0; only Google's own test showed the cost — run the Rich Results Test before calling a Google-facing schema change done." DECISIONS-LOG.md:32 (Decision 4): Organization is ["Organization","OnlineStore"] and the return policy is nested at /#return-policy. Every Offer still references it by @id.
- Collection ItemList, current code at snippets/senseless-structured-data.liquid:493-531. Each item is a Product with @id `<base>/products/<handle>#product`, which is the same @id as the PDP's #product. Its `sku` comes from `pv` (selected_or_first_available_variant, :521), but its Offer `price` is `prod.price`, the lowest variant (:525 and the shipping refs at :531). These agree today only because every default variant is the cheapest one. Live check on /collections/numbing-gel: S15CL £19.99, SG15AD £24.99, SG15PR £29.99. Reordering variants to put the larger size first would put a 35ml SKU next to a 15ml price.
- No other Product emitter is live. Horizon's `{{ product | structured_data }}` sections (product-information, featured-product) are not referenced by any product template. templates/product.quick-add.liquid is `layout none`, so it emits no JSON-LD. og:price (snippets/meta-tags.liquid:119-121) = `product.selected_or_first_available_variant.price`.
- Superseded advice to ignore: docs/SITE-ASSESSMENT-2026-08-06.md:194 #53 and the 23 Sep handoff spec (a rolling priceValidUntil) were both overtaken by the 23 Sep reversal. docs/TATTOO-BEAT-THEM-PLAN-2026-08-12.md:276 specified the product-level sku/gtin13 that 2937072 shipped on 14 Aug.

### Open questions the research raised

- What exactly did MC's automatic item update read on 22 Sep: og:price, the first JSON-LD Offer, or something else? a511a95 changed both at once, so this is unknown. hasVariant will put every size's Offer on every page, including the ?variant= page MC samples. Before coding, read Google's own docs on how automatic item updates and merchant listings pick the Offer for a landing URL when a ProductGroup is present, and quote them verbatim. Possible designs: (a) a full ProductGroup only on the canonical URL, with ?variant= pages keeping the single selected Offer; (b) ProductGroup everywhere, where each variant's Offer url, sku and price match its own feed item; (c) the selected variant listed first. The TN precedent does not answer this, because TN never used ProductGroup.
- @id plan. Does the ProductGroup take the existing `#product` @id? That is the ItemPage mainEntity, and it is where Judge.me's injector aims. And what @ids do the variant Products get? The collection ItemList (snippets/senseless-structured-data.liquid:516) already declares `<base>/products/<handle>#product` as type Product on 20 collections. Decide whether ItemList items keep type Product or point to the group, so the same @id is not typed two different ways.
- Where aggregateRating sits. It should go on the ProductGroup only, never also on the variants. A duplicate would bring back the 4 Sep critical "Review has multiple aggregate ratings". After any @type change, re-run the 66aa9b8 CDP test (headless Chrome, disable_json_ld forced false) to prove class="jdgm-server-jld" still suppresses Judge.me's injection. The reviews-guard marker `product.metafields.reviews.rating` must survive. Deploy with --reviews-changed plus a lock commit.
- Default variant. Leave the order smaller-first (7e079f2, 2 Jun; live 23 Sep on all 5), or put the larger size first as the stale DECISIONS-LOG.md:188 says? This is a founder/data call. Reordering alone only swaps which size is invisible. It also changes card and collection prices, and it would expose the ItemList mismatch (sku from pv, price from prod.price at :521/:525). Either way, correct the log entry and AUDIT-STORE-MC-ADS-2026-09-23.md:307-309, which names only 2 of the 5.
- Scope. Is ProductGroup for the 5 two-size products only (single-variant products and bundles stay Product)? Confirm variesBy = https://schema.org/size, since every product's only option is named "Size". Should variant names carry the size (TN style), given Decision 6 dropped "Default Title"? Does productGroupID use product.id? Does the variant productID become `shopify_ZZ_<pid>_<vid>` so it matches the G&Y item IDs (study N30, AUDIT-STORE-MC-ADS-2026-09-23.md:86-89)?
- GTINs. Exposing both Clinical Gel codes (0767461321111 and 0795847726144) on the canonical URL surfaces codes the owner's sheet calls OLD (study V9/N3). Should the GS1 UK decision (founder, after a pack scan; the TN DEC-53 equivalent) come before or after ProductGroup? And should the gtin key follow barcode length, as TN does?
- Shipping. Each variant's Offer must call senseless-shipping-refs with its own price. £44.99 and £49.99 cross into the £40–£79.99 free-standard band; £34.99 and £39.99 do not.
- Timing. The ~27–30 Sep GSC/MC re-check is meant to attribute any new issue to the 23 Sep schema batch (NEXT_SESSION.md:33-37: "anything new is this batch's"). Shipping ProductGroup before that re-check confounds it. Is there also an Ads learning period or change freeze (open question in study §7; TN deferred MC work for exactly this reason)?
- Verification tooling. Is Google's Rich Results Test (the real gate, per DECISIONS-LOG.md:28) run on each base URL and each ?variant= URL, about 1 minute per URL? The 39-URL price-guard checker is not in the repo, and jsonld-census.py covers sitemap URLs only. Build a checker for canonical + 10 ?variant= URLs that asserts each Offer's url, sku, price and og:price. What is the MC re-check window, and which diagnostic names should be watched on the 10 variant items?
- Canonical and sitemap. Keep ?variant= canonicalising to the base URL, which the 23 Sep audit verified clean (:281). Google's variant guidance for Shopify-style ?variant= URLs needs checking against this. The two-pass injectable check (.claude/rules/ad-facing.md) and the breadcrumb filter are unaffected in principle but must be re-run after the change.
- Records to reconcile once decided. Study V14 (:82) still says "One Product with N Offers", and :239's gating rule fired on 22 Sep without ProductGroup being chosen. DECISIONS-LOG.md:188 has the stale "Default variant = larger size". The notion that a511a95 fully matches TN 6457125 is only partly true.

## 12. Running the harness (offline proof, no deploy)

```bash
T=$(mktemp -d) && cp -R docs/specs/productgroup-phase1/{harness,live} $T/
cd $T/live && python3 capture.py              # fresh live capture: raw/ graphs + js/ product data (add the 12 single-variant ?variant= URLs to targets.json first)
cd $T/harness && mkdir -p draft && cp <repo>/snippets/senseless-structured-data.liquid draft/ \
  && (cd draft && patch -s senseless-structured-data.liquid < <repo>/docs/specs/productgroup-phase1/senseless-structured-data.productgroup.diff)
npm i liquidjs@10 && PG_REPO=<repo> node render.mjs   # expect: 22/27 draft == orig, 27/27 valid JSON, 5 ProductGroups
```

Dry-run 23 Sep 19:5x BST from the committed files: 26/27 orig == live (the one miss is a known liquidjs artefact — it prints the
VAD-4PK price as `2` where Shopify prints `2.0`), 22/27 draft == orig, 27/27 draft JSON valid, and the 5 base URLs render a
ProductGroup with both sizes, each with its price and GS1 GTIN. `rrt-code/*.html` are the 5 rendered base documents for the
Rich Results Test code tab (re-render them after a fresh capture before relying on them). `harness/edge.mjs` covers
out-of-stock-first, two-option, non-size option, variant image and lowercase size. The Judge.me V() normaliser check
(`simV.cjs`) is not committed because it embeds Judge.me's own code — re-extract it from the live bundle if needed.

