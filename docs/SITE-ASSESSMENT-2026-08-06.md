# SENSELESS — INDEPENDENT SITE ASSESSMENT
**senseless.uk · live theme #199324434780 · repo HEAD `6a7a10f` · 6 August 2026**
Eight dimensions assessed and adversarially re-verified. Every claim below traces to a file:line, a URL, an API response or a measurement.

---

## 1. VERDICT

The foundations are sound and the problems are almost entirely in the last mile: 60/60 sitemap URLs return 200 and self-canonical, there are zero duplicate titles or meta descriptions across 59 HTML pages, the contextual internal link graph is genuinely dense (PDPs carry 19–23 in-body inbound links, `/pages/the-senseless-system` carries 50), and the ad-facing injectable invariant holds with zero leaks across every surface five separate dimensions checked — so nothing on-site explains GSC's 27 Discovered-not-indexed URLs, all of which Googlebot has *never fetched*. That is crawl demand, and crawl demand is a function of authority the domain has not had time to earn; at Authority Score 4 and eight weeks old, no amount of on-site SEO will move it. What is actually wrong is smaller and more fixable than an SEO problem, and more embarrassing: a £2 aftercare ointment PDP that renders the numbing range's per-procedure recommendation table and pre-procedure application directions; two bundles £36 apart in price with byte-identical Merchant Center descriptions; three collection FAQs telling customers to "take extra care on... broken skin" while the compliance-locked safety block on the same journey says "apply to clean, unbroken skin"; a "Sale" badge on a price nobody was ever charged; no statutory cancellation right disclosed on any surface; and an add-to-cart that fails silently on all three add paths. Roughly forty of the fifty-odd confirmed defects are single-file, single-string edits — this is a day or two of work, not a rebuild. The most useful strategic correction is this: with 34 organic clicks in the period, organic is not yet the channel — paid, the Merchant Center feed and direct traffic are, so `body_html` quality and the purchase path are where the money is, and they are entirely within your control.

---

## 2. WHAT IS GENUINELY GOOD — do not touch these

These are not consolation prizes. Several are better than what most two-month-old stores in regulated categories have, and a generic audit would tell you to "improve" some of them, which would make the site worse.

**Technical SEO hygiene is close to clean.** 60/60 sitemap URLs 200. 59/59 canonicals present and self-referencing. Zero duplicate titles, zero duplicate meta descriptions, zero missing — across every page. Faceted URLs handled correctly: `/collections/numbing-cream?strength=clinical` returns 200 with a canonical back to the clean URL and no robots meta; only 4 parameterised internal links exist site-wide and there is no sort/filter leakage. `robots.txt` explicitly allows 12 AI crawlers with all 44 `*`-group disallows mirrored per-agent, plus a `Sitemap:` line.

**Internal linking is not the problem, and the first version of this assessment got that wrong.** Rebuilding the graph by stripping the actual header/footer DOM zones (rather than treating any nav-linked URL as chrome) shows only two URLs on the entire site with zero in-body inbound links. `/products/professional-strength-cream` has 23. The PDP body zone links three sibling PDPs, four procedure collections, the cream collection, the cleanser and the aftercare pack. Do not commission internal-linking work.

**The ad-facing injectable invariant holds, completely.** Independently re-verified by five dimensions across 59 crawled pages, all 16 product `body_html` values, the full header and footer link sets (41 unique header links enumerated), and the Merchant Center feed field. Zero links to `numbing-cream-for-injections` / `-lip-fillers` / `-botox` from nav, homepage, any PDP, any format/strength/procedure collection, the procedures hub or the three commercial landing pages. The only referrers are five blog articles, `/pages/does-it-hurt-by-treatment`, and each other — all permitted. Even the `senseless.recommended_procedures` metafield renders as plain text, not a link. This is disciplined execution of a rule that would be very easy to break by accident.

**Theme code quality is high and the theme is not the performance problem.** Of ~1.6 MB encoded on a PDP, the theme's own JavaScript is 60,242 B — **3.7%**. Across home, PDP and collection: 35 `<img>` elements, **zero** missing `width`+`height`, exactly one `loading="eager" fetchpriority="high"` per page, everything else lazy. Server processing time is 90–180 ms on every template type. There is no slow page and no layout-shift exposure from images.

**Compliance is engineered, not just written.** `sections/senseless-safety-warnings.liquid:22` hardcodes the warning strings, and the schema note at `:85` reads *"Warning copy is fixed per variant (compliance-locked, spec 2 Jul 2026) and cannot be edited here"* — the safety copy is deliberately removed from the theme editor's reach. `aggregateRating` is emitted conditionally, so no product carries a fabricated rating. `snippets/senseless-cart-offer.liquid:5` documents a deliberate refusal of pop-ups, urgency and scarcity UI. These are good decisions, made on purpose, and visible in the code.

**The comparative pages refuse the right comparisons.** `/pages/senseless-vs-ametop` explicitly declines comparative strength, pricing and safety claims against a prescription product and routes readers to "your GP or pharmacist", closing with *"it doesn't make Senseless the answer to every numbing-product question."* That is exactly correct for a cosmetic competing against a P/POM. A generic conversion audit would tell you to strengthen those comparisons. **Do not.**

**The commercial data layer is exact.** Bundle savings are derived live from component prices (`sections/senseless-bundle-contents.liquid:10,42`), not hardcoded, and correct to the penny on all five kits. All 21 variants are consistent across Admin, storefront and render; all available, all `inventory_policy: deny`, none at zero. The delivery rate matrix has no coverage gap. Gel and spray step exactly +£5.00 per tier at both sizes.

**Judge.me is real.** 4.88/231 reviews on an eight-week-old store, correctly rendered client-side. Any curl-based audit that reports "0 reviews" is wrong — this has already produced one false alarm and should not produce another.

**Structured data coverage is broad and mostly correct.** `BreadcrumbList` + `FAQPage` on the page templates, `Product` + `Offer` + conditional `AggregateRating` + `shippingDetails` + `hasMerchantReturnPolicy` on PDPs, 45 templates carrying the FAQ accordion. The `FAQPage` markup no longer earns a Google rich result (Aug 2023) but remains a top extraction format for answer engines — **keep it**, and do not let anyone report the missing rich result as a bug.

**Accessibility fundamentals that are done right:** the contact form has `<label for>` on every field, `<legend>` on checkbox groups and native `required`; the mobile nav drawer correctly ships `inert aria-hidden="true"` in the initial HTML; `snippets/senseless-quick-add.liquid:38` implements the variant radiogroup pattern properly.

---

## 3. THE RANKED PROBLEM LIST

Ordered by impact ÷ effort. **S** = under an hour. **M** = half a day to a day. Items marked *reviews-guard* edit files in `reviews-guard.manifest` and therefore ship via `scripts/deploy.sh --reviews-changed` plus a rewritten lock commit — factor that in.

### TIER 1 — ship this week

**1. Three collection FAQs contradict the compliance-locked safety copy on the same journey.**
*Evidence:* `templates/collection.numbing-cream.json:301`, `collection.numbing-gel.json:298`, `collection.numbing-cream-for-microneedling.json:255` all read *"Take extra care on sensitive or broken skin."* Meanwhile all 9 core SKUs' `body_html` say *"Apply to clean, dry, unbroken skin"* and `sections/senseless-safety-warnings.liquid:22` hardcodes *"Apply to clean, unbroken skin."* — copy the project itself locked against editing. "Take extra care on broken skin" reads as *permitted with care*, which sits outside the CPSR claim envelope. Verified live on `/products/clinical-strength-cream` (both strings render on the same page).
*Fix:* Replace with *"Do not apply to broken or irritated skin."* in three files.
**Effort: S · Claude Code** *(reviews-guard)*

**2. Five Hard-Rules breaches live in blog article bodies — and in the script that generates them.**
*Evidence:* `scripts/build-articles.py:104` *"numbing can help"*, `:113` *"take the edge off the anticipation as much as the sensation"*, `:134` *"any numbing takes hold"*, `:37` and `:92` *"feel less of the process"*. All five verified rendering in live `<p>` prose on `/blogs/guides/do-lip-fillers-hurt`, `/does-botox-hurt` (×2), `/botox-for-jowls`, `/how-long-does-botox-take-to-work`, and present in Admin `body_html`. In all three of the first cases "numbing" is the grammatical subject of an effect verb — the exact construction the Hard Rules ban.
*Fix:* Rewrite in `build-articles.py` **and** in the live article bodies. Fixing only the live articles means the next script run reintroduces the breach.
**Effort: S–M · Claude Code, then Daniel signs the replacement copy**

**3. The £2 Vitamin A&D aftercare PDP renders the numbing range's strength matrix, prep routine, strength ladder and cream FAQ.**
*Evidence:* `https://senseless.uk/products/vitamin-a-d-ointment-4-pack` → 200, 408,031 b, sections `__matrix`, `__strengths`, `__howtouse`, `__system`, `__faq`. Rendered body text includes *"Lip Fillers — Recommended · Botox — Recommended"*, *"Apply a thin layer... Remove before your appointment"*, and the FAQ *"Is Clinical Strength enough for lip fillers? Yes."* — on a post-procedure barrier ointment (`product_type: Aftercare`, 32-word `body_html`). It is the only `/products/*` page whose body text contains "Botox"/"Lip Filler". The same page also promises *"Full ingredients list available on the packaging and below"* with nothing below. Source: `templates/product.vitamin-a-d-ointment.json` (13 sections).
*Fix:* Copy the pattern already proven correct on `templates/product.foaming-cleanser.json` — drop `matrix`/`strengths`/`howtouse`/`system`, substitute a `senseless-callout-band`. Fix the unused default `templates/product.json` too. Remove or fulfil the ingredients promise.
**Effort: S · Claude Code**

**4. Add-to-cart fails silently on every add path on the site.**
*Evidence:* `assets/product-form.js:410` is `if (!addToCartTextError) return;`. `ref="addToCartTextError"` exists in exactly one file — `blocks/buy-buttons.liquid:77` — which **no template renders** (all 13 product templates use `senseless-product-hero`). So a failed add returns before showing any error. Separately, `product-form.js:321` queries `add-to-cart-component`, which is absent from `senseless-product-hero.liquid`, `senseless-collection-grid.liquid` and `snippets/senseless-quick-add.liquid` — so the success announcement at `:457` never fires either. The live-region plumbing already exists in all three (`hero:182`, `grid:171`, `quick-add:34`); only the gate is missing. With `auto_open_cart_drawer: false` (`config/settings_data.json:61`), a successful add produces no drawer, no animation and no announcement.
*Fix:* Add a `ref="addToCartTextError"` node to each of the three forms — restores the error text and the screen-reader announcement, zero visual change. **Do not** wrap in `<add-to-cart-component>`; that swaps in Horizon button markup that collides with `.ss-ph__atc` styling and the adjacent `payment_button`.
**Effort: S · Claude Code** *(reviews-guard)*

**5. The quantity stepper has no ceiling, so over-stock adds 422 and vanish.**
*Evidence:* `snippets/quantity-selector.liquid:77-79` emits `max` only from `variant.quantity_rule.max`; no PDP renders a `max` attribute. `assets/component-quantity-selector.js:62-70` therefore always returns `canAdd: true`. Professional Spray has **6 units**. A practitioner ordering 10 gets a server 422 swallowed by finding 4.
*Fix:* Emit `max` from `variant.inventory_quantity` when `inventory_policy == 'deny'`. Ship with 4.
**Effort: S · Claude Code**

**6. Two bundles £36 apart in price carry byte-identical Merchant Center descriptions.**
*Evidence:* Admin `body_html` MD5: `clinical-numbing-kit-small` (£71.99) and `clinical-numbing-kit-large` (£107.99) both `d00e8b1f`; `advanced-numbing-kit-small` (£84.99) and `advanced-numbing-kit-large` (£120.99) both `d6a07e00`. All five kits 63 words, all updated today at 10:13–10:14 — the rewrite did not differentiate them. Regex for `\d+\s?(g|ml)` across all five → **zero matches**. The differentiating facts exist in on-page HTML (*"Cream (10g) · Gel (15ml)"* vs *"Cream (30g) · Gel (35ml)"*) but nowhere machine-readable. `body_html` also feeds the PDP `Product` JSON-LD via `senseless-structured-data.liquid:38`.
*Fix:* Rewrite five `body_html` values stating contents and sizes. Composition, not effect — clean against the ceiling. Keep the existing *"not a medicine... supports comfort"* closers.
**Effort: S · Claude Code via Admin**

**7. `/collections/shop-all` drops the £2 add-on — the only SKU that bridges the free-shipping gap.**
*Evidence:* Live DOM shows 15 cards; the page's own JSON-LD declares `"numberOfItems": 16` with the Vitamin A&D pack at position 2. Cause: `templates/collection.shop-all.json`'s fifth grid passes `format: cleanser`, and `senseless-collection-grid.liquid:17` filters `where: 'type', 'Cleanser'` — the product's type is `Aftercare`. Compounding: four SKUs are £19.99, two of which is £39.98, and free standard shipping fires at £40.00 — `snippets/senseless-shipping-banner.liquid` renders *"You're £0.02 away from free standard delivery"*. The only item that closes that 2p gap is the £2 pack, which is unreachable from any browse page.
*Fix:* Add `aftercare` to the section schema enum (`senseless-collection-grid.liquid:258`) plus a sixth grid section — two parts, not one. Separately, put the free-shipping threshold to Daniel: £39.99 or £35 removes the trap, and touches the delivery profile plus `senseless-shipping-banner.liquid:46-47,62` plus both shipping surfaces — all four or none.
**Effort: S · Claude Code (grid) + Daniel (threshold)**

**8. Delivery prices and transit times appear on no pre-checkout surface.**
*Evidence:* Live rate card via `deliveryProfiles` — Standard 4-6 days £1.99 (free ≥£40), Express 2-3 days £3.99, Next Working Day £8.99 (free ≥£80). Grep for `£1.99` / `£3.99` / `£8.99` / `4-6 working` across home, both PDPs, cart, `/pages/shipping-delivery`, `/policies/shipping-policy`, `/pages/terms-conditions` → **zero matches on every one**. The shipping page names two of three options, prices none, and never states what "Standard" means. Express exists and no customer has been told about it. Note also that at £80+ Standard and Express are excluded (both capped at £79.99), so an £80 order is offered free next-day only.
*I am not asserting a CCRs Sch. 2 breach* — Shopify displays rate names and prices at checkout before the customer is bound. The finding is that the published shipping page is materially incomplete and the arrival-date question that governs an appointment-driven purchase is unanswerable at the point of decision.
*Fix:* Complete `/pages/shipping-delivery`; add a delivery line to the PDP (one schema default at `senseless-product-hero.liquid:305` + `templates/product.bundle.json`, not thirteen edits).
**Effort: S · Claude Code** *(reviews-guard)*

**9. Every bundle PDP promises a vanity bag that appears in no bundle's contents.**
*Evidence:* Claimed at `templates/product.bundle.json:45` (trust tick), `:71` (body), `:83` (FAQ) and `templates/collection.bundles.json:25` — 7 renders on live `/products/clinical-numbing-kit-small`, **one of them inside the `FAQPage` JSON-LD served to Google**. The `senseless.bundle_contents` metafield on all five kits is a 4-element list: cream, gel, spray, Foaming Cleanser. The rendered `ss-kit__list` on the same page shows four items.
*Fix:* Daniel confirms whether the bag ships. If yes, add it to the metafield on all five. If no, remove four copy strings. Either way it cannot stay contradictory on a £71.99–£135.99 product.
**Effort: S once ruled · Needs Daniel**

**10. A "Sale" badge and a struck-through price that was never charged.**
*Evidence:* Live `/cart` renders `<span class="visually-hidden">Regular price </span><span class="compare-at-price">£94.96</span>` alongside £84.99, with a `Sale` badge. `SBUN3.compare_at_price = 94.96` is exactly `24.99×3 + 19.99` — a component sum, never an offered price. Same on all five bundles, and the same markup appears in the predictive-search dropdown site-wide. The PDP band gets it right (*"save £7.97 versus buying the items separately"*); the price widget does not, and the "Regular price" label is visually hidden so sighted users see only *was → now*. `compare_at_price` is non-null on exactly the five bundles and null on all 16 singles.
*Fix:* Qualify the comparator as "bought separately" wherever it renders, or remove `compare_at_price` and surface the saving as an explicit line (which composes with the missing-saving fix in item 21). Merchant Center consequence needs Daniel.
**Effort: M · Needs Daniel**

**11. No statutory cancellation right is disclosed anywhere; the 14-day right is presented as an EU-only extra.**
*Evidence:* `/pages/returns-refunds` and `/policies/refund-policy` (the checkout-linked one) both carry verbatim: *"Do you ship to the EU? UK only at present; if that changes, EU customers get the additional 14-day cooling-off period."* That is the only cooling-off mention on either. `right to cancel`, `consumer contracts`, `statutory`, `model cancellation` → 0 hits on `/pages/returns-refunds`, `/pages/terms-conditions` and `/pages/faq`. The two surfaces have already drifted: last-updated "3 July 2026" vs "2026-06-04".
Commercially the store is *more* generous than statute (30 days vs 14), and the sealed-goods exemption (CCRs 2013 reg 28(3)) plausibly covers unsealed product — but the disclosure duty is a separate obligation from the remedy, and non-disclosure carries a defined consequence. **INFERRED on the legal conclusion; this needs MHG legal, not a copy tweak.** Related terms to review at the same time: *"Items sent back without a prior return request are not accepted"* and *"Sale items... non-returnable"* (which, given the compare-at data, reads onto exactly the five most expensive SKUs).
*Fix:* Legal drafts; edit both surfaces together.
**Effort: M · Needs legal**

**12. `/collections` is live, indexable, orphaned, on the stock Horizon template — and links all three injectable collections.**
*Evidence:* Re-verified today: `https://senseless.uk/collections?_fd=0` → **200, 362,630 bytes, zero robots meta**, self-canonical, not in the sitemap, zero inbound links from any of 59 crawled pages, not disallowed in `robots.txt`. Its 101-word main section links all 16 collections including `numbing-cream-for-injections`, `-lip-fillers` and `-botox`. Not a formal invariant breach — nothing links it, and it is not on the canon ad-facing list — but it is an unmanaged indexable surface with an unintended link graph, invisible to any sitemap- or homepage-seeded crawl.
*Fix:* noindex the `list-collections` template + 301 to a real destination. **Do not 301 it to `/collections/aesthetic-numbing-cream`** — that page has no product grid.
**Effort: S · Claude Code**

**13. The most consequential rule in canon is enforced by a code comment.**
*Evidence:* `sections/senseless-header.liquid:12-13` is a comment. The four procedure-collection link blocks are hardcoded in four separate places in that one file (`:416-419`, `:482-485`, `:596-599`, `:627-630`). Nothing mechanically prevents an injectable link being added to an ad-facing surface.
*Fix:* Add a grep assertion for `numbing-cream-for-(injections|lip-fillers|botox)` across ad-facing templates to `scripts/deploy.sh`, alongside the existing reviews-guard. The invariant currently holds perfectly — this keeps it that way.
**Effort: S · Claude Code**

**14. Five public, guessable, no-minimum 10% codes are active with no end date.**
*Evidence:* `WELCOME10`, `COMFORT10`, `COMEBACK10`, **`Hannah10`**, **`Katie10`** — all ACTIVE, all 10%, all `DiscountCustomerAll`, all `minimumRequirement: None`, all `endsAt: null`, each once-per-customer but there are five, so one customer can take 10% off five separate orders with no minimum spend. Bundle savings are 9.92–10.50%, so a guessable code hands out the bundle's entire differentiator on a single £19.99 tube. `Hannah10`/`Katie10` have 0 uses and look like personal codes left publicly live.
*Fix:* Deactivate the two personal codes; add minimums and end dates to the rest.
**Effort: S config · Needs Daniel (margin call)**

**15. `read_orders` is denied, so nothing behavioural is measurable by anyone.**
*Evidence:* REST `orders/count.json` → `"This action requires merchant approval for read_orders scope."`; GraphQL `orders` → `ACCESS_DENIED`; `access_scopes.json` returns 31 scopes, `read_orders` absent. This blocks substantiating "Most Popular", sizing discount leakage, and validating any conversion claim.
*Fix:* Approve `read_orders` on the custom app.
**Effort: S · Needs Daniel**

### TIER 2 — real, worth doing

**16. The desktop mega menu has no keyboard path into the Shop panel.** `senseless-header.liquid:709` opens a panel on `focus`; `:696` `closeAll()`s on the next trigger's focus; and `:340` places `.ss-hdr__panels` as a DOM sibling *after* the bar, so tabbing off Shop destroys its panel before you can reach it. Enter is also a no-op on first press. WCAG 2.1.1 (A) and 2.4.3 (A) — the only Level A failure on the site, on the primary nav. The catalogue is still reachable via the 21 footer links, so this is a component failure, not an unreachable store. Fix: move `.ss-hdr__panels` inside the `<li>` (layout-safe — `.ss-hdr__item` is `position: static`, so geometry is preserved) and use the `focusout` close pattern already at `:743-745`. **M · Claude Code**

**17. The global focus ring is white-on-white on 11 sections.** `base.css` `*:focus-visible{outline:... solid currentcolor}` at 1.5px; on solid-purple CTAs `currentcolor` is `#ffffff` → 1.073:1 on canvas, 1.00:1 on white. AA needs 3:1. Affects 11 sections with resting-state purple/white controls (header ×3, hero, callout-band, collection-hero, cross-sell, decision-band, guide-hero, practitioner-cards, product-grid, product-showcase, section-statement). Fix: one `:where()` rule in `senseless-typography`'s inline style, which cascades correctly after `base.css` and loses to the four sections with bespoke rules. **S · Claude Code**

**18. The skip link renders behind the sticky header.** `.skip-to-content-link:focus` gets `z-index: var(--layer-temporary)` = 20; the header is `z-index: 100` and `#header-group` is `display: contents` so both sit in the root stacking context. The focused link lands at y≈16–56px inside an ~85–97px header band. One-line fix. **S · Claude Code**

**19. Loyalty rewards have an undisclosed £25 floor and combine with nothing.** All six `LOY-*` codes carry `minimumRequirement: £25.00`; `/pages/rewards` contains `£25` and `minimum` **zero times**. Worse: the three ACTIVE loyalty codes carry `combinesWith: {orderDiscounts: false, productDiscounts: false, shippingDiscounts: false}` while the app's 10% is a product-class discount — so redeeming £5 alongside it will be refused at checkout. (The three EXPIRED codes had `productDiscounts: true`, so this was configured differently once.) **S · Needs Daniel/admin**

**20. The cream grid compares £19.99, £24.99 and £55.99 across different sizes.** Live `/collections/numbing-cream`: Clinical £19.99 (10g chip shown), Advanced £24.99, Professional £55.99 with **no size chip at all** — it has a single 30g variant, and the chip block is guarded by `variants.size > 1`. Like-for-like at 30g is £44.99 → £49.99 → £55.99. `From £` renders zero times. **S · Claude Code** *(reviews-guard)*

**21. The bundle saving renders on no browsing surface.** `senseless-collection-grid.liquid` contains **zero** occurrences of `compare_at` (verified); it renders bare `{{ v0.price | money }}` at `:166` across all 15 collection templates. The homepage highlights section (`:106`) likewise. The saving exists only on the PDP band. Fix fires only where `compare_at > price`, i.e. bundles only; renders on injectable collections but creates no link, so no invariant issue. **S · Claude Code**, composes with item 10.

**22. Four floating widgets, two of them chat, and the largest is bigger than the whole theme bundle.** Dondy WhatsApp `ChatBubble.js` = 65,576 B brotli / 217,933 B raw, against the entire theme JS at 60,242 B encoded. Shopify Inbox adds a 12,780 B inline config blob in `<head>` on every page. Rendered simultaneously with Judge.me and a 368×84 Google Merchant widget. The Inbox pill (`bottom_center`) sits **on top of the trust-bar text "CPSR assessed"** — verified by `elementsFromPoint` and screenshot. All embeds are in `config/settings_data.json` (Dondy L102, Inbox L119, position L130) — this is an in-repo, reversible edit, not admin-only. Two chat widgets is one too many. **S · Claude Code + Daniel's call on which chat to keep**

**23. 192 KB of unrequested web fonts on every page.** Three GTStandard `.woff2` files (63,600 + 64,484 + 64,452 B) from `cdn.shopify.com/shop-assets/static_uploads/shoplift/`, declared by a 748-byte JS-injected `<style>` that appears in neither the served HTML nor the repo (`grep -ril 'shoplift\|GTStandard'` → 0 files). Separately, Klaviyo injects `@import` for Google Fonts Montserrat, breaching the explicit contract at `snippets/senseless-typography.liquid:3` (*"no Google Fonts"*) — small in bytes (655 B, no gstatic download observed) but it is an extra origin and a contract breach. *Caveat: measured in a browser signed into Shopify admin; whether the Shoplift injection fires for an anonymous visitor is unverified.* **S to audit · Needs Daniel (app review)**

**24. The font preload targets a weight nothing above the fold uses.** `snippets/fonts.liquid:2-22` preloads Montserrat 400 and **700**. Above-fold weight census: homepage 16×600, 0×700; collection 16×600, 0×700; PDP 17×600, 0×700. The dominant above-fold weight arrives 50–290 ms later than the one nobody uses. Both preloads carry `fetchpriority="low"`, so no high-priority bandwidth is being stolen — the win is swap timing, not priority. Fix: swap the 700 preload for `font_modify: 'weight','600'`. **S · Claude Code**

**25. The homepage body links nothing the chrome does not already carry.** Homepage `<main>` = 21 link instances, 17 unique targets, **all 17 in the site-wide chrome** (16 header, 1 footer). Consequence: the three highest-commercial-intent pages get 2 inbound links each — `/pages/best-emla-alternative-uk`, `/pages/senseless-vs-ametop`, `/pages/strongest-numbing-cream`. The anchor *"Strongest numbing cream"* is already live on two collection pages, so reusing it introduces no new claim language. **S · Claude Code**

**26. The three strength collections are the thinnest commercial pages on the site.** Chrome-stripped: `/collections/clinical` 360 words, `/collections/professional` 357, `/collections/advanced` 349 — against format collections at 1,103–1,327 and procedure collections at 855–921. Tokens unique to one strength page vs the other two: clinical 32, professional 24, **advanced 11**. Structural cause: those three templates are 7 sections and lack the `senseless-key-facts` + `senseless-faq-accordion` pair that `collection.numbing-cream.json` (11 sections) carries. *(The earlier "43–62% shared boilerplate" figure did not reproduce — actual overlap is 19–25%.)* **M · Claude Code + Daniel copy**

**27. Twelve of sixteen collections have empty `body_html`.** Only `clinical` (59 chars), `advanced` (59), `professional` (63) and `bundles` (135) have any. The code is correct — `senseless-structured-data.liquid:115` emits conditionally — the data is absent, so `CollectionPage` carries only `mainEntity`, `name`, `url`. *Caveat before bulk-populating:* `templates/collection.json:45` renders `collection.description` visibly, so any collection that ever falls back to the default template would suddenly display it. **S–M · Claude Code**

**28. Ingredients are published nowhere pre-purchase — and two dimensions disagreed on why.** Zero hits for `ingredient|INCI|lidocain|benzocain|tetracain|\d+%` across all 16 `body_html`, all PDPs and the FAQ. Five surfaces answer *"What's in it?"* by deferring to the pack. No ingredients metafield exists.
**Resolution of the disagreement:** the INCI list is already legally on-pack under the Cosmetic Products Regulation and publishing a factual ingredient list is a composition statement, not an effect claim. Stating a **% active concentration** is where the MHRA medicines-by-function question lives — precisely the axis closed by Decision `39158bc3-75ea-8194`. **Route: publish INCI, hold the percentage, and have legal bless the pairing before either goes live.** This is the top unanswered customer question and competitors publish it. **M · Needs Daniel/legal**

**29. `numbing-cream-for-injections` is a mathematically guaranteed duplicate of `-lip-fillers`.** From the Admin API: `injections` is disjunctive `[Lip Fillers] OR [Botox]`; `botox ⊆ lip-fillers` (both members are also lip-filler members); therefore `injections == lip-fillers` identically, for as long as the metafield data holds. All three are organic-only, `-for-injections` has 3 inbound links, all from permitted surfaces. Consolidate or re-scope. **S · Needs Daniel**

**30. `/pages/does-it-hurt` and `/pages/does-it-hurt-by-treatment` are a summary and its expansion, and the nav promotes the thin one.** Identical opening sentence verbatim, identical 8-treatment list in identical order, both titles and both metas say "by treatment". `does-it-hurt` = 471 words, 8 sections, **is** in nav (`senseless-header.liquid:500`, `:641`). `does-it-hurt-by-treatment` = 794 words, 13 sections, not in nav, and carries the actual per-procedure answers.
**Caveat before merging:** `does-it-hurt` links **no** injectable collection; `does-it-hurt-by-treatment` links **all three**. Repointing the nav at it puts an injectable-linking page one hop from every page including the homepage. Not a formal breach (a guide page may link them) but it is a material change to injectable exposure and must be Daniel's call, not a silent side-effect. Safer default: keep both URLs, re-scope `does-it-hurt` to the *why*, strip "by treatment" from its title and meta. **S · Needs Daniel**

**31. `dateModified` is hardcoded to `datePublished`.** `sections/senseless-article.liquid:124-125` sets both from `article.published_at`. All five articles show Admin `updated_at: 2026-06-26` against a schema `dateModified: "2026-06-04"`. Liquid does not expose `article.updated_at`, so there is no free fix — either a per-article metafield holding a last-reviewed date, or drop `dateModified` rather than assert a false one. **M · design decision**

**32. Authorship is the weakest possible E-E-A-T configuration for this category.** All five articles have `author: "Senseless"` and schema `author: {"@type":"Organization"}`. For content adjacent to medical procedures, a named, credentialled reviewer is the single biggest available trust lift. **Needs Daniel**

**33. Homepage testimonials carry efficacy framing, three typos and a named competitor.** `templates/index.json:255` *"various **differnt** creams... others **where** just **aweful**... on another level"*; `:264` *"Having used **TKTX** for about 3 years... hit and miss **if it works**... so many **fakes**"*; `:273` *"so much easier to work on clients"*. These are hardcoded section settings — brand-authored and brand-placed, so the "leave published reviews as-is" decision does not reach them and the Hard Rules bind in every voice. Two separate exposures: efficacy framing (Hard Rules) and competitor denigration (CAP). Verbatim quotes must not be silently reworded — Daniel holds the originals. **S · Needs Daniel**

**34. Two unsubstantiated superlative badges on the highest-traffic URL.** `templates/index.json:307` "Most Popular" (Professional Strength Cream) and `:295` "Best Value". Neither is substantiable by anyone in this session — `read_orders` is denied. CAP requires superlatives to be substantiable. "Best Value" has a number one click away; "Most Popular" has nothing. **S · Needs Daniel — substantiate from Shopify Analytics or drop**

**35. Every strength-tier description that routes, routes downward.** Six of 16 `body_html` carry a routing sentence; all six route to a cheaper tier (*"Most sessions don't need the practitioner tier"*, *"the lighter one is usually the sensible start"*); **zero** route up. **The obvious fix is unsafe** — *"if your session runs long, Advanced is the match"* edges onto the banned duration axis. Safe route: surface the sentence Advanced already ships (*"Formulated for longer or more sensitive sessions"*) as the upward signal on Clinical PDPs, gated on `compliance-check`. **S · gated on compliance-check**

**36. The cart upsell is not cart-aware.** `templates/cart.json` uses a `product-list` section pointed at collection `all` with `max_products: 4` — verified live on an *empty* cart rendering the first four products alphabetically. Re-pointing at `/collections/bundles` is invariant-safe. **S · Claude Code**

**37. `/collections/bundles` claims Starter and Ultimate across all three strengths.** There is no Professional Starter, and one cannot be built to the Starter recipe — `professional-strength-cream` has a single 30g variant. `templates/collection.bundles.json:25`. One-line copy fix. **S · Claude Code**

**38. The Organization entity is emitted twice, differently, with no `@id` and no `sameAs`.** Homepage via `senseless-structured-data.liquid:139-161` (carries `logo`, `brand`, `areaServed`); about/contact via `sections/senseless-org-schema.liquid:6-32` (carries top-level `email`). `grep -rn sameAs` → 0 hits. A third, dormant emitter sits at `sections/header.liquid:288` and would duplicate if that header were ever re-enabled. `sameAs` is a symptom, not a markup gap — at AS 4 the constraint is the absence of off-site references, not the property. Fix: add `@id: https://senseless.uk/#organization` to both, have `Product.brand`/`Article.publisher` reference it, consolidate to one emitter. **S · Claude Code**

**39. `/search` has no `<h1>`.** `sections/search-header.liquid:17` emits `<h3>`. It is the only page on the site with zero `<h1>` — home, PDP, all collections, `/blogs/guides` and `/pages/faq` all have exactly one. **S · Claude Code**

**40. The PDP variant picker has no group name.** `senseless-product-hero.liquid:186-192` renders a native radio group with no `<fieldset>/<legend>`, no `role="radiogroup"`, no `aria-labelledby` — while `snippets/senseless-quick-add.liquid:38` does it correctly one file away. WCAG 1.3.1 (A). One attribute, all 16 PDPs. **S · Claude Code**

**41. Trade is absent from the header nav.** Enumerated all 40 unique header links — `/pages/trade` is not among them. It *is* reachable from a dedicated homepage band, the footer, and the Professional PDP signpost, so it is not buried — but it is invisible on every page that is not the homepage or a Professional PDP, for the highest-AOV segment. Related: the trade page claims *"Bulk sizes beyond the consumer 30g and 35ml ranges"* and Admin shows no such SKU. **S · Needs Daniel**

**42. Klaviyo's popup covers the hero, both CTAs and the H1.** Full-viewport `rgba(20,20,20,0.6)` scrim at z-index 90000, on every page type. It fires at **13.7 s** (homepage) / 16.5 s (PDP) against `loadEventEnd` 1.9 s, so it is **not** a performance or LCP problem — it is purely a CRO/UX call. **Needs Daniel**

### TIER 3 — hygiene and backlog

| # | Finding | Evidence | Effort · Owner |
|---|---|---|---|
| 43 | 8.13 MB of image working files live on the theme and publicly fetchable | 18 assets under `assets/images/` in the theme manifest; `processed-sources/*.png` up to 1.25 MB each, 200 on public CDN. No `.shopifyignore` | S · Claude Code |
| 44 | 31 of 88 sections unused — 373,938 B, 40% of `sections/` | Recomputed across all templates + section groups + `theme.liquid`. 4 abandoned bespoke sections (27,037 B) are zero-risk deletes. `product-recommendations` (42,126 B) is dead — element on 0/59 pages. **`snippets/list-filter.liquid` is NOT dead** — rendered from `blocks/filters.liquid:197,455` | S · Claude Code |
| 45 | Empty cart sends everyone to noindexed `/collections/all` | `snippets/cart-products.liquid:49` falls back because `settings.empty_cart_button_link` is unset. One theme setting, not a snippet edit | S · Claude Code |
| 46 | `#8E8A82` muted text fails AA | 3.20:1 on canvas. Live footprint is **4 text nodes on the homepage only**; `senseless-typography.liquid:15` already documents the `#6E6A63` replacement (5.01:1) | S · Claude Code |
| 47 | Duplicate card links + redundant accessible names | `/blogs/guides`: 10 tab stops for 5 guides, same href, same name (`senseless-article-hub.liquid`; needs `position: relative` added for the stretched-link fix). Procedure grid computes *"Senseless topical preparation for microneedling Microneedling View range"* | S · Claude Code |
| 48 | `/search` + `/collections/all` duplicate DOM IDs; **mobile sort is functionally broken** | 11 and 17 duplicate IDs. The mobile drawer's sort radio shares an ID with the desktop one but a different `form` attribute, so `for` resolves to the desktop form and the overflow form never sees the change. Only these two auto-generated URLs use the Horizon facets component | M · vendor/backlog |
| 49 | `/pages/aesthetic-procedures` is 174 words with dead `body_html` | Custom template never outputs `body_html`; 745 chars of copy render nowhere. A primary nav destination | S · Claude Code |
| 50 | `aesthetic-numbing-cream` smart rule admits the Vitamin A&D pack | Rule is `type != Cleanser` → 15 members including the aftercare pack, while excluding the Foaming Cleanser the System sells as part of the routine. Invisible today (no grid on that page); wrong the moment a grid, feed or collection-scoped discount touches it | S · admin |
| 51 | Three orphan page templates | `page.how-it-works.json`, `page.choosing-your-strength.json`, `page.choosing-your-format.json` — all 301 correctly. Note `page.best-numbing-cream.json` is attached to an **unpublished draft**, not orphaned, and carries INCI copy item 28 may want | S · Claude Code |
| 52 | 5 inert `/policies/*` redirects | `/policies/shipping-policy`, `-refund-policy`, `-privacy-policy`, `-terms-of-service`, `-contact-information` all return 200 natively, so their redirects can never fire | S · admin |
| 53 | Product/Offer missing `itemCondition` and `priceValidUntil` | Both derivable. **`priceValidUntil` must be a rolling date** (`'now' \| plus: 31536000`) — a past date makes Google drop the offer. `gtin` is data-blocked: only 3 of 21 variants have a barcode; emit `gtin13` conditionally | S · Claude Code |
| 54 | 10 live page templates emit no `WebPage` entity | 13 of 26 `page.*.json` include `senseless-page-schema`. **Not a one-line branch fix** — that would double-emit on the 13 that already have it, and each needs an authored description. Low value: every page already carries `BreadcrumbList` + `FAQPage` | M · low priority |
| 55 | Judge.me: 33 KB of inline settings on every page, duplicated bundle on PDPs | `window.jdgmSettings` = 33,139 B inline in `<head>` site-wide — the largest inline script on the site. On PDPs `widget_common.js` and `widget_main.js` each load **twice** (24,983 B encoded of pure duplicate), and `widget_form.js` (26,675 B) loads before anyone opens the form | S to raise · vendor |
| 56 | `senseless-article-hub` vs `senseless-articles-hub` vs `senseless-article` | Three near-identical filenames, three different jobs. Rename is behaviour-neutral | S · Claude Code |
| 57 | 7 titles over 60 chars, 2 meta descriptions over 160 | `/pages/using-numbing-cream` 177, `/pages/how-long-numbing-cream-lasts` 161 | S · Claude Code |
| 58 | Professional Spray at 6 units, `inventory_policy: deny` | Will sell out with no warning to a practitioner ordering multiples. The absence of a scarcity indicator is a documented deliberate brand position, not a defect | restock · Daniel |
| 59 | `/llms.txt` is shadowed by Shopify's platform file | A redirect `/llms.txt → /pages/llms-txt` exists and no longer fires; the path now returns 4,347 B of Shopify Shop-app boilerplate. `/pages/llms-txt` is one of the 11 deliberate noindex pages. Its unique facts are already published on indexable surfaces | no action |
| 60 | The shipping bar reads pre-discount subtotal | `senseless-shipping-banner.liquid:83` uses `items_subtotal_price`. **Unreachable today** — there are zero automatic discounts on the store and discount *codes* never reach `cart.js`. Latent only; revisit if an automatic order-level discount is ever created | S · latent |

---

## 4. THE TOP 5

If only five things get done, these five — chosen because each is either non-negotiable, or has an unusually high impact-to-effort ratio, or unblocks measurement. Together they are roughly one and a half days of work plus two legal reviews.

**1 — Ship the compliance batch: items 1, 2, 33 and 34.**
*Worth:* it removes every confirmed live breach of the project's own non-negotiable rules. The broken-skin item alone is three strings and it currently contradicts copy the project deliberately locked against editing — that is the single worst kind of defect to be found by a regulator, because it demonstrates the control existed and was worked around. The article breaches are five strings, and they must be fixed in `scripts/build-articles.py` as well as the live bodies or they come back on the next run. *Why first:* zero of these are judgement calls. They are rule violations, they are cheap, and unlike everything else on this list they carry a downside that is not measured in conversion rate.

**2 — Repair the purchase path: items 4, 5, 7.**
*Worth:* right now a customer can click Add to cart, get a server error, and see nothing at all — no message, no announcement, no change. The lowest-stock SKU (6 units) has no quantity ceiling, so this is not theoretical. Meanwhile the only product that bridges a £39.98 basket to the £40 free-shipping threshold is invisible on the page it should be sold from. *Why second:* with 34 organic clicks in the period, the traffic you have is paid and direct — and paid traffic that hits a silently-failing cart is money set on fire. Every item here is an S, all in files you already control.

**3 — Fix the ad-landing surfaces: items 3, 6, and the `body_html` half of 28.**
*Worth:* `body_html` is the Merchant Center description, and Merchant Center is a ranking surface that is completely independent of domain authority — it is the one place where better copy converts into better placement immediately. Today two bundles £36 apart in price ship byte-identical descriptions with no sizes in either, and a £2 aftercare ointment's PDP tells shoppers which strength to use for Botox. *Why third:* it is where paid spend actually lands, and it is the highest-leverage content work on the site precisely because organic is not available to you yet.

**4 — Get legal onto items 11, 10 and 9 — as one instruction, this week.**
*Worth:* these are the only three findings with a defined statutory downside rather than a commercial one. No cancellation right is disclosed anywhere, and the only cooling-off mention presents 14 days as an EU benefit. A "Sale" badge sits over a strikethrough price that was never charged on any bundle. And a reusable vanity bag is promised seven times on the bundle PDP, including inside the `FAQPage` JSON-LD served to Google, while the contents metafield on all five kits lists four items and no bag. *Why fourth and not first:* none of it is fixable by Claude Code without a ruling, so the action is to brief legal now and let the drafting happen in parallel with 1–3.

**5 — Approve `read_orders` and close `/collections` (items 15, 12, 13).**
*Worth:* `read_orders` is a five-minute approval that unblocks substantiating "Most Popular", sizing the discount-code leakage, and validating every conversion claim in this document — no one can currently measure anything behavioural. `/collections` is a live, indexable, orphaned stock-Horizon page that links all three injectable collections, invisible to any sitemap-seeded audit. And the invariant that keeps those collections organic-only is currently enforced by a code comment — a grep in `deploy.sh` makes it mechanical. *Why fifth:* small, cheap, and each removes a category of future surprise rather than fixing a present loss.

**What just missed the cut, and why:** the mega-menu keyboard trap (item 16) is the site's only WCAG Level A failure and would be top-5 on a mature site — it is M rather than S, and the footer keeps the catalogue reachable, so it is #6. The app payload (item 22 — Dondy at 65 KB brotli, more than the entire theme bundle, plus a second redundant chat widget whose pill covers the words "CPSR assessed") is #7: real, cheap, and an in-repo edit, but the theme is already only 3.7% of page weight and no LCP regression was measured.

---

## 5. WHAT AN EXTERNAL AUDIT COULD NOT HAVE SEEN

I have not read the agency's report, so I am not scoring it. What I can state precisely is which findings here are **structurally invisible to any audit conducted from outside** — no repo, no Admin API, no live DOM. That is where the value of this assessment concentrates.

**Requires Admin API access — invisible to every crawler:**
- Two bundle pairs with byte-identical `body_html` (MD5 `d00e8b1f`, `d6a07e00`) across a £36 price gap. Visible only by hashing the feed field.
- The live delivery rate card: three rates, five definitions, and the fact that at £80+ Standard and Express are excluded.
- Five active public 10% codes including **`Hannah10`** and **`Katie10`** — personal-looking codes left publicly live.
- Loyalty codes carrying `combinesWith` all-false plus a £25 minimum stated on no customer-facing surface.
- `numbing-cream-for-injections == numbing-cream-for-lip-fillers` proven by membership, not guessed from text similarity — the disjunctive OR is mathematically forced because `botox ⊆ lip-fillers`.
- The `senseless.bundle_contents` metafield showing four items and no vanity bag on all five kits.
- `product_type: Aftercare` on the Vitamin A&D pack, which is exactly why the shop-all grid drops it.
- Article `updated_at: 2026-06-26` against a schema `dateModified` of `2026-06-04` — the content *was* revised, contradicting the obvious external read that nothing has been touched since launch.
- `read_orders` denial, which is why "Most Popular" cannot be substantiated by anyone.

**Requires repo access — the fix is in a file no crawler renders:**
- The five Hard-Rules strings live in `scripts/build-articles.py`. An external audit would recommend editing the live articles, the next script run would silently revert them, and the breach would come back.
- `addToCartTextError` exists in `blocks/buy-buttons.liquid:77`, which no template renders — the reason a failed add is invisible. Unreachable by inspection of the rendered page.
- The `add-to-cart-component` gate at `product-form.js:321` that silently disables every success announcement.
- `quantity_rule.max` being the only source of a quantity ceiling, so `canAddToCart()` always returns true.
- `settings.empty_cart_button_link` being unset (a one-key fix, not the snippet edit an outside auditor would prescribe).
- The invariant enforced by a comment at `senseless-header.liquid:12-13` and the taxonomy hardcoded in four places in one file.
- 31 unused sections, 373,938 B — and the fact that `snippets/list-filter.liquid`, which *looks* dead, is rendered from `blocks/filters.liquid` and would break collection filtering if deleted.

**Requires live DOM and Resource Timing — static HTML analysis gets these actively wrong:**
- Judge.me's `shopify_v2.css` is inside a `<noscript>` wrapper. Any regex over the served HTML reports a 137 KB render-blocking stylesheet on every page. It is **never fetched** — zero Resource Timing entries on four page types. Both the original pass and my own first static pass made this error.
- The 192 KB of GTStandard fonts is declared by a JS-injected `<style>` that appears in neither the served HTML nor the repo. Invisible to `curl`.
- The Klaviyo popup fires at 13.7 s, not on load — so it is not an LCP factor, despite looking like one in a screenshot.
- The Shopify Inbox chat pill physically overlapping the words "CPSR assessed" in the trust bar.
- Safari < 18 receiving JPEG (170,883 B) where Chrome receives WebP (88,250 B) from the identical URL.
- Judge.me renders client-side, so any curl-based audit reports "0 reviews" against a real 4.88/231.

**Nobody crawling the sitemap or the homepage finds `/collections`.** It is not in the sitemap and has zero inbound links from any of 59 pages — yet it is 200, has no robots meta, and links all three injectable collections.

**And the category constraint itself.** A generic ecommerce playbook applied here recommends before/after imagery, "works in X minutes", efficacy testimonials, and strengthened competitor comparisons. Every one of those is banned in this category. An audit that does not know that will produce a list of recommendations you cannot legally implement, and will simultaneously miss the compliance defects that are actually live.

---

## 6. WHAT IS OUTSIDE OUR CONTROL

**Be clear-eyed about this: organic performance is currently constrained by domain authority, and nothing on this site changes that.**

The domain is eight weeks old. Semrush Authority Score 4, 343 backlinks, 68 organic keywords, 34 total web-search clicks in the period. GSC shows 34 indexed against 61 not indexed, and the largest bucket — **27 Discovered-not-indexed, every one with "Last crawled: N/A"** — means Googlebot has never fetched those URLs at all. Not fetched and rejected. Never fetched.

Two independent rebuilds of the link graph agree that internal linking is not the cause. 42 of 60 sitemap URLs are linked from the site-wide chrome, i.e. from every page. Of the remainder, PDPs carry 19–23 contextual in-body inbound links, format collections 21, `/pages/the-senseless-system` 50. Only two URLs on the entire site have no in-body inbound link. All 60 sitemap URLs return 200 and self-canonical. There is no crawl trap, no duplicate-title cluster, no parameter leakage, no canonical conflict, and no orphan cluster of any size.

**Crawl budget is allocated on host-level authority signals.** A site Google has not yet decided is worth crawling deeply does not get crawled deeply, regardless of how well it is linked internally. That is the binding constraint, and it is bought with off-site signals — links, citations, brand searches, real-world mentions — not with schema, not with internal linking, not with word counts.

**A realistic expectation, and I am marking this INFERRED:** a regulated-category commercial domain typically needs six to twelve months of consistent off-site signal accumulation before crawl depth and indexation catch up with a complete site. Judge everything here against that clock. The single highest-leverage lever available is the one that is off-site: the trade and practitioner channel. Real practitioner partnerships, trade-press coverage, and clinic listings produce exactly the citation profile that moves an Authority Score of 4, and Senseless has a genuine, differentiated story to pitch — a UK-formulated cosmetic with completed CPSRs, a closed MHRA classification and a named limited company behind it. That is a PR asset, not an SEO asset, and it is worth more than every item in section 3 combined for organic outcomes.

**Also outside our control, and worth not spending money on:** Safari < 18 receives JPEG rather than WebP from Shopify's CDN (+93.6% on the LCP image) regardless of the `Accept` header or `&format=webp` — platform-owned. Shopify's checkout prefetch pulls 449 KB encoded / 4.08 MB decoded on every PDP, over half the page's decoded weight — platform-owned, leave it. `/llms.txt` is now served by Shopify and shadows the store's own redirect — platform-owned. `/policies/*` are served natively so the five redirects pointing at them can never fire. `/search` and `/collections/all` use Shopify's stock facets component with its duplicate-ID bug.

**What is still worth doing on-site anyway, and why:**

1. **Everything conversion-related.** The traffic you already have — paid, direct, referral — converts or does not convert entirely independently of domain authority. A silently-failing add-to-cart costs the same whether you have 34 clicks or 34,000.
2. **The Merchant Center feed.** `body_html` quality is a ranking surface you control completely and that does **not** depend on domain authority. It is the highest-return content work available to you right now, and it is the reason items 3 and 6 rank where they do.
3. **Compliance.** Non-negotiable, independent of traffic, and the exposure exists whether or not anyone visits.
4. **The technical foundation you already have.** It is genuinely good and it should be *maintained*, not extended. When authority does arrive, a site with clean canonicals, complete structured data and a dense internal graph converts that authority into indexation immediately. That work is already done — protect it.
5. **What NOT to do:** do not commission internal-linking work, do not rewrite thin collections *expecting indexation movement*, do not invest further in `llms.txt`, `sameAs` or `WebPage` entities hoping to move rankings. Rewrite the strength collections because they are the thinnest commercial pages on the site and read poorly to a human — that is a good enough reason. Just do not expect Google to notice this quarter.

---

## 7. COMPLIANCE EXPOSURE — RANKED

Not zero, but nothing here is catastrophic and nothing requires taking the site down. Ranked by severity × likelihood. Items 1–4 should be resolved this week; 5–8 need Daniel or legal; 9–11 are watch items.

**1 — Safety-instruction contradiction, live on the same customer journey. (CPSR claim envelope)**
Three collection FAQs say *"Take extra care on sensitive or broken skin"* while every product `body_html` and the compliance-locked warning block say *"Apply to clean, unbroken skin."* Verified rendering together on `/products/clinical-strength-cream`. "Take extra care on broken skin" reads as permitted-with-care and sits outside the CPSR claim envelope. **The aggravating factor is that the project deliberately locked the safety warnings against editing (`senseless-safety-warnings.liquid:85`) and this copy contradicts them anyway.** Three strings. Fix today.

**2 — A product-inclusion claim that appears not to be delivered. (DMCCA 2024 unfair commercial practices / misleading action)**
The vanity bag is claimed seven times on the live bundle PDP — including inside the `FAQPage` JSON-LD served to Google — while the `bundle_contents` metafield on all five kits lists four items and no bag, and the rendered contents list on the same page shows four. On products priced £71.99–£135.99. This is the highest-probability consumer-law issue on the site because it is a factual, checkable, itemised promise. Daniel must state which is true.

**3 — A "was" price that was never charged. (Misleading price indication; CMA pricing practices / DMCCA 2024)**
`SBUN3.compare_at_price = £94.96` is exactly `24.99×3 + 19.99` — a component sum, never an offered price — rendered on `/cart` and in predictive search as a strikethrough alongside £84.99, under a `Sale` badge, with the "Regular price" qualifier `visually-hidden`. Same pattern on all five bundles. The PDP band handles this correctly (*"versus buying the items separately"*); the price widget does not. Either qualify the comparator everywhere it renders or remove `compare_at_price` and state the saving explicitly.

**4 — Five Hard-Rules breaches in live article bodies. (MHRA / ASA axis; project non-negotiable)**
*"any numbing takes hold"*, *"numbing can help"*, *"take the edge off... the sensation"* — in the first two, "numbing" is the grammatical subject of an effect verb, which is the precise construction the category-noun rule bans; the third is a reduced-sensation claim. Plus two weaker *"feel less of the process"* instances. All five originate in `scripts/build-articles.py`, so a live-only fix reverts.

**5 — Statutory cancellation right disclosed nowhere; 14 days framed as an EU benefit. (Consumer Contracts Regs 2013, reg 13 / Sch. 2)**
Verbatim on both `/pages/returns-refunds` and `/policies/refund-policy`: *"if that changes, EU customers get the additional 14-day cooling-off period."* No mention of a UK right to cancel, no model cancellation form, on any of the four surfaces checked. The disclosure duty is separate from the remedy, and non-disclosure carries a defined consequence — the cancellation period extends. Mitigating: the store's actual terms are more generous than statute (30 days), and the sealed-goods exemption plausibly applies once unsealed. Also review *"Items sent back without a prior return request are not accepted"* and *"Sale items... non-returnable"*, which given the compare-at data reads onto exactly the five most expensive SKUs. **INFERRED on the legal conclusion — this is MHG legal's call, not a copy edit.**

**6 — Efficacy framing and competitor denigration in a brand-authored homepage module. (Hard Rules + CAP)**
`templates/index.json:255,264,273` are hardcoded section settings, not a Judge.me feed — so the "leave published reviews as-is" decision does not reach them and the Hard Rules bind ("in every voice, incl. testimonials"). *"some have worked"*, *"if it works"*, *"on another level"*, *"so much easier to work on clients"* are efficacy framings; attribution never licenses an effect claim. Separately, quote two names TKTX by brand, calls it *"hit and miss if it works"* and associates its market with *"fakes"* — a comparative/denigration exposure on a different axis. Three typos in the same block (*differnt*, *where*, *aweful*) are a credibility cost on top. Verbatim quotes must not be silently reworded — Daniel holds the originals on file.

**7 — Unsubstantiated superlatives on the highest-traffic page. (CAP substantiation)**
"Most Popular" on Professional Strength Cream and "Best Value" on the Advanced Ultimate kit (`templates/index.json:307,295`). Neither is substantiable by anyone in this session — `read_orders` is denied at the API level, confirmed on both REST and GraphQL. Substantiate from Shopify Analytics and keep the evidence, or drop the badges.

**8 — Publishing a prescription-only medicine's effect timeline on a commercial seller's blog. (Human Medicines Regs 2012, Part 14 — INFERRED, needs legal)**
`/blogs/guides/how-long-does-botox-take-to-work` states *"Botox usually starts to work within 3 to 4 days, with the full effect visible around 10 to 14 days... It then typically lasts about 3 to 4 months."* Botulinum toxin is a POM, and advertising POMs to the public is prohibited. Whether editorial content about a procedure on a seller's site engages that prohibition is a genuine legal question I cannot resolve, and the same content is standard across the aesthetics sector. Note the structural irony: that is precisely the onset/duration shape the Senseless Hard Rules ban for its own product. **Do not action on my assessment — put the axis to legal.**

**9 — Materially incomplete published shipping information.**
Three live rates; two named, none priced; transit times published nowhere pre-checkout. Express (£3.99, 2–3 days) exists and can only be discovered by surprise at checkout. **I am explicitly not asserting a CCRs Sch. 2 breach** — Shopify displays rate names and prices before the customer is bound. This is a commercial and completeness failure with a legal edge, not an established breach.

**10 — Accessibility: one WCAG Level A failure on the primary nav. (Equality Act 2010 s.29 — INFERRED, low probability)**
The desktop mega menu is keyboard-inoperable: `focus` on a trigger opens its panel and `focus` on the next trigger closes it, while the panels sit outside the tab path entirely. Plus a focus indicator that is white-on-white across 11 sections and a skip link that renders behind the sticky header. A UK service provider has a reasonable-adjustments duty; enforcement against small ecommerce sites is rare, and the footer keeps the catalogue reachable, so I rank this low on likelihood while noting it is the only Level A failure on the site.

**11 — Composition not disclosed pre-purchase, plus one live unmet promise.**
No INCI, no active, no concentration anywhere on the site; five surfaces defer to the pack. `/products/vitamin-a-d-ointment-4-pack` promises *"Full ingredients list available on the packaging and below"* and nothing renders below — that unmet promise should be fixed immediately regardless of the wider decision. **Two dimensions disagreed on whether the wider gap is compliance-gated; the resolution is:** publishing the INCI list is a factual composition statement about a cosmetic, not a medicinal or effect claim, and the list is already legally on-pack. Stating a **% active** is where MHRA medicines-by-function sits — the axis closed by Decision `39158bc3-75ea-8194`. Publish the INCI, hold the percentage, have legal bless the pairing.

**And what is clean, which is worth stating plainly:**
- **The ad-facing injectable invariant has zero breaches.** Verified five independent times across 59 pages, all 16 `body_html`, and the full header/footer link sets.
- The ten core-SKU product descriptions written today contain no medicinal, effect or time-to-effect claims.
- No before/after or efficacy imagery anywhere.
- The `/pages/faq` legal-verbatim exemption is documented, scoped to that page, and has not propagated.
- The PDP 45–60 minute line is operator-accepted under a logged decision.
- VAT number, company details and legal entity are present and correct.
- CPSRs complete on all SKUs; core safety warnings built, live and compliance-locked in code.
- `/pages/senseless-vs-ametop` correctly refuses comparative strength, pricing and safety claims against a prescription product and routes readers to a GP or pharmacist.