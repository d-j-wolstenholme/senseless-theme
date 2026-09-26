# NEXT_SESSION — handoff

**Last session (26 Sep 2026, Mac mini `Ds-Mac-mini.local`):** unit-price basis re-checked (unchanged: per kg /
litre); Merchant Center "Limited" items cross-referenced; Shopify categories + kit brand set on the 15 feed
products (Admin API only, no theme deploy). Live theme `#199324434780` unchanged since `d04c60d` (ProductGroup).

## ON-CONTINUE — do these first

<!-- ON-CONTINUE:START -->
0. **DONE 26 Sep — MC Limited cross-reference + categories** (`DECISIONS-LOG.md` 2026-09-26).
   - The 6 Limited items ("Personal hardships" → Dynamic remarketing only) have no data difference from their
     Approved siblings (Adv Cream 10g vs 30g, Clinical Gel 35ml vs 15ml identical) → classifier variance.
   - Fixed what was wrong: `scripts/set-product-category.py --apply` → Skin Care (`hb-3-2-9`) on creams/gels/
     sprays/cleanser, Skin Care Kits & Sets on the 5 kits, kit vendor `senseless-numbing` → `Senseless`. MC re-synced
     11:01 26 Sep (gels had NO Google category before; kit brand fixed).
   - **From 29 Sep:** request ONE re-review of the 6 in MC (Needs attention → item → Request review). Repeat
     failures add cooldowns. If still Limited, leave them — Shopping ads + free listings are unaffected.
   - **Founder/legal, open:** unit prices are hidden on the site (22 Sep Decision 5), but the PMO likely requires
     them on PDPs for online sales (small-shop exemption is floor-area based). Recommend per kg/l on the PDP, optional
     per-100 g figure alongside. The feed stays per kg/l (GB law since 6 Apr 2026; the 22 Sep log date is corrected).
   - Noticed, not changed: MC titles use the SEO title where set ("Clinical Strength Cream | UK-Formulated 10g",
     "Foaming Cleanser | Aftercare | Senseless"). This is copy, so it's the founder's call.
1. **DONE 23 Sep (Mac mini) — schema-quality batch (`7224825`, lock `84efe3f`).** Detail:
   `DECISIONS-LOG.md` 2026-09-23 and `docs/AUDIT-STORE-MC-ADS-2026-09-23.md` items 5–8.
   - Census of all 74 sitemap URLs (`scripts/jsonld-census.py`, before → after): JSON-LD entity
     leaks 34 → **0**; run-together FAQ sentences 20 → **0**; Offers with `priceValidUntil`
     0/188 → 188/188 → **REMOVED again (`4b3ed61`)**: Google's Rich Results Test showed it adds a Merchant
     listings warning ("Missing field validFrom" — Google reads it as a sale end), and GSC never
     flagged it as missing; conflicting `#webpage` pages 12 → **0**; Organization now
     `["Organization","OnlineStore"]`; 0 parse errors, 0 dangling `@id`s, Offers per URL unchanged.
   - Verified live: validator.schema.org 0 errors / 0 warnings on 12 pages; the 22 Sep price guard
     holds on all 39 PDP URLs (22 `?variant=` + 17 base: 1 Offer, price/sku/og:price match);
     Judge.me injects no second Product/rating in a real headless render (6 reviewed PDPs); ad-facing
     invariant 0 breaches in BOTH passes; theme-check at the 119/78 baseline; reviews-guard 6/6.
   - **Org-level return policy — DONE the same evening** on the founder's go-ahead ("yes put it
     on"; `4be298b` + lock `51db25c`): nested in `#organization` on all 73 HTML pages, terms
     unchanged, the standalone node removed, Offers still reference it by `@id`. If Legal changes
     the returns wording, update this node too.
2. **Follow-ups from the batch:**
   - **Google Rich Results Test — DONE 23 Sep eve** (live, after the `priceValidUntil` removal):
     `/products/advanced-strength-gel` and `/products/professional-numbing-kit-large` — 5 valid items
     each (Product snippets, Merchant listings, Breadcrumbs, Local businesses, Organization); Merchant
     listings **0 issues**; Product snippets only the pre-existing `aggregateRating`/`review` (no
     reviews on those products). Google resolves each Offer's `hasMerchantReturnPolicy` `@id` to the
     policy nested in `#organization`. `/pages/how-to-apply-numbing-cream` — 3 valid (Breadcrumbs,
     Local businesses, Organization); HowTo isn't a Google rich result any more (retired 2023).
     "Local businesses" = the `OnlineStore` Organization; valid, no warnings, left as is.
   - **~27–30 Sep re-check against the 23 Sep baseline:** Search Console Merchant listings **94 valid /
     0 invalid**, all 4 issues Passed 0; Product snippets **94 valid / 0 invalid**, non-critical
     `aggregateRating` 89 + `review` 89; Indexing **62 indexed / 111 not indexed**; 78 clicks / 3
     months. Merchant Center: 6 Limited, all "Personalised advertising: Personal hardships" (founder:
     leave); no price or markup issues. Expect the same counts — anything new is this batch's.
3. **DONE 23 Sep eve:** robots `Disallow: /collections/*?*page=` (+ `/*/` form) in the `*` and all AI
   groups (`9454886` + whitespace fix `c3ef726`; live diff 26 added / 0 removed; no sitemap URL newly
   blocked; AdsBot untouched). **`/blogs/guides` is NOT an open question** — decided 9 Jul (noindex,
   `/pages/articles` canonical) and 17 Jul (`dc7b3ee`: blog-level `seo.hidden` tested live, it drops
   the ARTICLES from the sitemap too, reverted; accept the GSC warning). Never set `seo.hidden` on a
   Blog.
3b. **DONE 24 Sep 00:00 — ProductGroup / hasVariant Phase 1 LIVE (`d04c60d`, lock `0af1488`).** Spec:
   `docs/specs/productgroup-phase1/SPEC.md`. The 5 two-size base URLs carry a ProductGroup with both sizes;
   every `?variant=` URL and single-variant PDP is byte-identical (22 Sep price fix untouched). Google RRT live:
   Merchant listings 2 valid items on each of the 5, review stars kept on the 3 rated products, no new warnings.
   **Follow-ups:** MC diagnostics at +2–3 d and +7 d (no price/GTIN issue on the 10 two-size items); GSC Merchant
   listings + Product snippets should rise by ~5 valid items vs the 94/94 baseline (it's this change, not a
   regression). Phase 2 (group markup on `?variant=` URLs) only after 7 clean MC days, as its own decision.
   Gotcha: the Offer body now lives in TWO branches of the snippet (group + else) — change one, change both.
4. **Founder / account-holder items still open** (unchanged, detail in the previous block below):
   ~~Google Play developer verification~~ — **CLOSED 23 Sep, checked in Play Console via Chrome:**
   Android developer verification shows both packages **Registered** (`uk.senseless.app` 18 Jul 2026,
   `com.totallynumb` 3 Jul 2026, 1 key each) and the Identity tab carries MATRIX HEALTH GROUP LTD,
   Paddock Business Centre, 2 Paddock Road, Skelmersdale WN8 9PL (org account 8140414713800942317,
   signed in as senseless.tattooing@gmail.com). Nothing was changed; the only related notification is
   Google's generic 8 Sep reminder. Then: MC delivery re-check + the G&Y app's shipping-sync switch (item 2b/2c
   below); §5B decisions (Strength meaning, bundle sale scope, GS1 barcodes, ad-facing scope, returns
   wording to legal, bag compliance status); §5D (healthcare certification alert in Ads, 4 questions
   to Martin); Ads hygiene (misspelt campaigns/display path, Manual CPC, Shopping coverage).
5. **Noticed, not caused by this batch, not changed:** `/pages/articles` and the 5 policy pages emit a
   second, anonymous page-level node (CollectionPage / WebPage, no `@id`) beside `#webpage`;
   `/pages/contact` serves two robots metas (`noindex,follow` + `noindex,nofollow`); pre-existing
   theme-check `ValidSchema` errors in `senseless-faq-accordion` and `senseless-how-to-use`; the
   page-schema Name/Description settings are now Service-only (labelled) on 14 templates.
6. **Records corrected:** the 2 July orphans (`blocks/footer-copyright.liquid`,
   `templates/page.how-long-numbing-cream-takes-to-work.json`) are **gone from live** (Asset API 404,
   23 Sep) — the old "needs an OK" item was stale.
7. **DONE 23 Sep late — barcodes match the owner's "Barcodes" sheet** (Drive
   `165V5aaEfCa3AWYv2Q5_Vxe-B5ImsJzP5NrJtaqQbyQk`; founder: "make sure the ones on Shopify and the
   Merchant Center match"). `scripts/set-barcodes.py --apply` wrote the GS1 UK code to 16 variants
   (13 empty + 3 that held the sheet's OLD US codes), mapped by product + size, never by the sheet's
   SKU column (its gel SKUs differ from Shopify's). VAD-4PK + the 5 kits stay empty (no GS1 code).
   Verified: admin read-back 16/16; live `.js` + JSON-LD `gtin13` 16/16; Merchant Center synced
   within ~10 min (Advanced Cream 30g → `…139`, Clinical Gel 15ml → `…047`). **Sheet units fixed at
   the founder's request:** every gel, spray and foam row "g" → "ml" (both brands, Sheet1 + Sheet2),
   TN oil 30g → 30ml; column J's `VALUE(SUBSTITUTE(I,"g",""))` formulas were widened to strip "ml"
   too (34 formulas) after the unit change made them `#VALUE!`. **Totally Numb Shopify/MC: not
   touched (founder did TN).** Noticed for the founder, not changed: TN Comfort Cream Professional
   30g (PR30) carries `10795847726097`, the sheet's old GTIN-14 case code; the sheet has no GS1 code
   for it. **Re-check ~27–30 Sep:** MC diagnostics for any GTIN issue on the 16 items.
<!-- ON-CONTINUE:END -->

## Gotchas (23 Sep)

- **The handoff's decode chain had `&amp;` first** — that double-decodes "&amp;#39;". Decode it last.
  And never decode `&lt;`/`&gt;` into JSON-LD: `/search` titles carry the visitor's query.
- **Google's Rich Results Test is the real gate, not validator.schema.org.** The validator passed
  `priceValidUntil` 0/0; only the RRT showed it adds a Merchant listings warning. RRT takes ~1 min per URL.
- **Never set `seo.hidden` on a Blog** — it drops the blog's articles from the sitemap (17 Jul test).
  The `/blogs/guides` GSC "noindex in sitemap" warning is accepted by design.
- **validator.schema.org rate-limits by IP** (~20 POSTs, then Google's "sorry" page). Space calls,
  or use the Rich Results Test in a browser.
- **Any edit to `snippets/senseless-structured-data.liquid` needs `deploy.sh --reviews-changed`** and a
  lock commit straight after — guard (c) checks the whole manifest, so even a deploy of an unrelated
  file aborts until the lock matches.
- **robots.txt.liquid: a literal `{{ 'Disallow: …' }}` gets NO trailing newline** (the `{{ rule }}` /
  `{{ group.sitemap }}` drops behave differently). Keep literal whitespace between added lines, and
  diff the live `/robots.txt` against a saved copy after every deploy — 4e7386a glued a line for ~3 min.
- **Deploy a new snippet before the files that render it** (two `deploy.sh` calls), so no page renders
  "Could not find asset" in between.
- JSON-LD merges same-`@id` nodes as a UNION: re-declaring a node with a different `name` gives it two
  names. Re-declare type only.

---

## Previous ON-CONTINUE block (22–23 Sep) — kept for reference; items above supersede it

1. **DONE 22 Sep (Mac mini):**
   - **Mac mini credentials:** the MacBook `.env` is installed (chmod 600); `refresh-token.sh` and `deploy.sh` work here. `shopify store auth` (read/write_themes) also works.
   - **Cookie banner:** records consent (`24e9f5e`); `sale_of_data` is kept true so the Ads pixel is unchanged (founder decision; never re-raise). It sits above every popup via the top layer (`de6259e`), and the mobile gap is fixed. Verified live, desktop + mobile.
   - **Merchant Center unit pricing:** 16 variants are per kg / per litre / per item (`scripts/set-unit-pricing.py`, applied by the founder). The UK PMO as amended from 1 Oct 2025 requires kg/litre; smaller units are not allowed.
   - **Merchant Center account:** confirmed as **5805726847** (founder's screenshot), and the founder has access.
   - **Unit prices hidden on the site** (founder); the data stays for Merchant Center (`0403cf2`).
   - **Merchant Center price mismatch (35ml gel):** a single selected-variant Offer + og:price (`a511a95`); verified on 21 URLs.
   - **Card prices follow the size** (all quick-add cards + the PDP sticky bar, `f922cfa`): live audit 196/196.
   - **Horizon quick-add modal fixed** (was empty for two-size products): `templates/product.quick-add.liquid` + quick-add.js; verified desktop + mobile.
   - **Permission rule** (project-local) + **2 live orphans deleted** (founder yes).
   - **Bundle sale styling gone** from /collections/all, search and the search modal (N7).
   - **Shipping schema fixed** (V17): per-offer methods by price; validator 0 errors / 0 warnings.
1b. **DONE 23 Sep (Mac mini) — audit of store vs Merchant Center vs Google Ads vs schema/GSC.**
   Full write-up: `docs/AUDIT-STORE-MC-ADS-2026-09-23.md` (commit `3debdd2`). Headlines:
   - **P0 FIXED AND LIVE (`7199dd5`):** `/products/foaming-cleanser` was declaring
     **"Numbing Cream for Botox"** as its `BreadcrumbList` parent — an ad-facing PDP associating
     with an injectable collection in markup Google follows *and* renders as the SERP breadcrumb.
     Cause: `senseless-breadcrumbs-jsonld.liquid` took `product.collections.first`; 12 products are
     injectable-collection members, so the three handles are now filtered in that snippet rather
     than the one product being fixed. Verified live on all 17 PDPs: **0 injectable parents**
     (cleanser now reads "Numbing Cream for Laser Treatment"); theme-check at baseline;
     Asset-API byte-identical.
   - **`.claude/rules/ad-facing.md` now requires TWO passes** — anchors **and** structured-data
     `item` URLs. Pass 1 alone reported 0 breaches on 23 Sep while this one was live.
   - **Yesterday's MC delivery fixes survived** (3 policies, all Complete, no recreated 4th) and the
     unit-pricing issue is gone from diagnostics.
   - **The three GSC "Validate fix" items carried since 4 Sep have all PASSED.** Merchant listings
     94 valid / 0 invalid; Product snippets 94 valid / 0 invalid; no manual actions.
   - **Vitamin A&D 4-Pack (£2.00) is in Merchant Center via Google's own crawl**, Approved, despite
     being withheld from the Google channel in Shopify. Not ad-eligible unless someone accepts the
     "Allow ads" prompt on that data source. Needs a decision.
   - **Product `<lastmod>` = request time: CLOSED 23 Sep.** Not an app/Admin issue (that diagnosis
     was wrong and is retracted - `updated_at` is stable). Confirmed Shopify platform behaviour;
     Support advisor Iqra confirmed in writing there is no merchant-side setting, said there is no
     engineering escalation path for a non-urgent issue, and logged it as product feedback (chat
     reference to arrive by email). Workaround for genuine changes: Search Console URL Inspection ->
     Request indexing. We have NOT observed a real indexing delay - raised as data correctness only.
   - **RECOMMENDED NEXT TASK — the schema-quality batch.** Four small fixes, one deploy, one verify
     pass. Low risk and, importantly, none of them touch the variant/Offer logic that the 22 Sep
     price fix guards. Evidence for each is in `docs/AUDIT-STORE-MC-ADS-2026-09-23.md`:
       1. **HTML entities leaking into JSON-LD — 33 occurrences.** `&amp;` / `&#39;` are read
          literally by Google because JSON-LD in a `<script>` is not HTML-parsed. Two root causes in
          `snippets/senseless-structured-data.liquid`: `page_title`/`page_description` (Shopify
          pre-escapes these) and `product.description | strip_html` (strips tags, leaves entities).
          Fix: one shared unescape chain before `| json` —
          `| replace: '&amp;','&' | replace: '&#39;',"'" | replace: '&quot;','"'
           | replace: '&lt;','<' | replace: '&gt;','>'` — applied to `sd_name`, `sd_desc`, `pd`,
          `pdesc`, and the same in `sections/senseless-faq-accordion.liquid`. Worst case is an
          ad-facing one: `/products/vitamin-a-d-ointment-4-pack` description reads "Vitamin A &amp; D".
       2. **`priceValidUntil` missing on every Offer** (0 of 173 blocks). Add a rolling +1 year:
          `"priceValidUntil": "{{ 'now' | date: '%s' | plus: 31536000 | date: '%Y-%m-%d' }}"` on both
          the PDP Offer and the collection ItemList Offer. **Never emit a past date** — that
          suppresses the rich result rather than improving it.
       3. **Duplicate, conflicting `#webpage` node on 12 pages.**
          `sections/senseless-page-schema.liquid` re-declares the sitewide `@id` with a *different*
          `name`/`description`, so two statements about one entity merge and Google picks one at
          random (e.g. `/pages/faq` → "Numbing Cream FAQ — Safety…" vs "Numbing cream FAQ"). Fix:
          drop `name` and `description` from that re-declaration, emit only `@id` + the narrower
          `@type` (the `@type` merge is correct and should be kept — about/contact resolve to
          `["WebPage","AboutPage"]`).
       4. **Organization is thin.** Set `"@type": ["Organization","OnlineStore"]`, add org-level
          `"hasMerchantReturnPolicy": {"@id": ".../#return-policy"}`. `sameAs` stays empty until a
          social profile actually exists — do not invent one.
     Verify after deploy: `theme-check` at baseline (119 errors / 78 warnings — anything above that
     is yours), Asset-API byte diff, then re-POST two pages to `https://validator.schema.org/validate`
     (`--data-urlencode "html@<file>"`) and confirm 0 errors / 0 warnings as today.
   - **Also cheap, not yet done:** add `Disallow: /collections/*?*page=` to `robots.txt.liquid`
     (`/collections/shop-all?page=500` returns 200 and self-canonicalises — infinite crawl space,
     though page 1 renders no pagination links so on-site discovery is nil); and decide deliberately
     whether `/blogs/guides` should lose its `noindex` or be canonicalised to `/pages/articles` —
     today it is `noindex,follow` *and* submitted in `sitemap_blogs_1.xml`, which Search Console
     reports as an error. It is the only noindex URL among all 74.
   - **Biggest upside, own session:** `ProductGroup`/`hasVariant` — 5 PDPs expose only the cheaper
     variant to Google (£44.99 clinical cream 30g, £49.99 advanced cream 30g, £34.99 clinical gel
     35ml, £39.99 advanced gel 35ml, £44.99 professional gel 35ml, plus a valid GTIN-13). The
     `?variant=` pages emit the right Offer but canonicalise to the base URL. Merchant Center is
     unaffected (the feed carries per-variant URLs). Needs an MC re-check afterwards because it
     touches exactly what the 22 Sep fix guards.
   - **Ads hygiene (founder/Ads console, not theme):** paused Shopping campaign vs Cream/Spray-only
     PMax coverage — gels, cleanser and all 5 bundles have no Shopping coverage at all;
     "Seneseless Search" and "Search - Tatoo Numbing" are misspelt, as is the customer-visible
     display path `/numbing-cream/tatoo`; one Search campaign still runs Manual CPC; and the
     **"Apply for healthcare certification"** alert is open in Ads (this is the §5D item — it lives
     in Ads, not Merchant Center).
2. **Next in sequence:**
   - (a) Founder call: show the unit price on the PDP hero (the theme doesn't yet).
   - (b) **Merchant Center delivery policies FIXED by hand 22 Sep** (DECISIONS-LOG Decision 12): Express 2–4 d £3.99 to £79.99; Standard 4–7 d £1.99 to £39.99, free £40–£79.99; NWD 1–2 d £8.99 to £79.99, free £80+; all 15:00 London cut-off, handling 0–1; the broken `Custom_rate_price_based` deleted. **FIRST THING NEXT SESSION: re-check MC → Delivery and returns** (3 policies, those day ranges) in case the Google & YouTube app resynced or recreated the 4th. Merchant API client ready (`scripts/merchant-api.py`); the founder's GCP/service-account setup is still pending.
   - (c) **Shopify-side root cause found 22 Sep — NOT yet fixed (needs the founder's hands).**
     The Google & YouTube app's **"Shipping Information — automatically syncs your Shopify shipping
     information to Google Merchant Center" is ON** (app → Settings; Google account
     `peter@matrixhealthgroup.co.uk`, MC `5805726847`, GA4 `G-N6XKMWQ92N`). So yesterday's hand-made MC
     policies can be overwritten at any time. Verified live in the General profile (GB zone), the
     defect is a **missing transit time on the two free rates** — that is the only field Google reads
     for delivery days:
       * Express 2-3 working days · £3.99 · £0–79.99 — transit **2–3 business days** ✅
       * Next Working Day (Order by 3pm) · £8.99 · £0–79.99 — transit **1 business day** ✅
       * Next Working Day (Order by 3pm) · **Free · £80+ — transit NONE** ❌
       * Standard 4-6 Working Days · £1.99 · £0–39.99 — transit **4–6 business days** ✅
       * Standard 4-6 Working Days · **Free · £40–79.99 — transit NONE** ❌
     Fix (Settings → Shipping and delivery → General profile → the rate's ⋯ → Edit shipping option →
     Transit time → **Custom**): free NWD = untick "Use a range", **1** business day; free Standard =
     range **4**–**6** business days. Cosmetic only at checkout — "Estimated delivery dates" is set to
     **Automated**, and automated dates replace transit time when available.
     Two rates also share a name with their paid twin ("Standard 4-6 Working Days",
     "Next Working Day (Order by 3pm)"). Left alone deliberately: customers only ever see one of each
     pair, so renaming is a customer-visible change with no proven benefit. Revisit only if a resync
     still mis-maps after the transit times are set.
     **Irreducible gap:** Shopify has **no order-cut-off field anywhere** — "Order by 3pm" exists only
     inside the rate *name*, and Estimated delivery dates offers only Off / Automated / Manual plus a
     Fulfilment time of Same business day / Next business day / 2 business days / Custom (currently
     **Next business day**, described as a fallback "when automated dates are unavailable"). So a
     resync can never reproduce the **15:00 London cut-off** set by hand in MC. Either re-add the
     cut-off in MC after each resync, or switch the app's Shipping Information sync **Off** and own the
     MC policies (by hand or via `scripts/merchant-api.py`). Founder's call.
     *Nothing in Shopify was changed — the Claude Code auto-mode classifier blocks typing into the
     live store admin.*
   - Then the founder's §5B items below.
3. **Founder decisions from the study (§5B):**
   - what "Strength" means (the hidden "not a measure of strength" is on 37 pages; canon 817f vs 817c);
   - bundle sale styling (still on `/collections/all` + search) and whether it extends to Google Shopping;
   - ~~GS1 UK barcodes for 16 variants~~ — DONE 23 Sep (see item 7 in ON-CONTINUE);
   - scope of the ad-facing rule (links only, or injectable text too);
   - route returns wording + imported reviews + classification evidence to MHG/legal, and log a
     Compliance Hold on returns wording;
   - set the Cosmetics Bag's Compliance status (Products DB row 3e258bc3-75ea-8144).
4. **Account holder (study §5D):** name the live MC (the G&Y widget says `5805726847`); read the
   "Apply for healthcare certification" alert; run the export/join checklist; put the four 4 Sep
   questions to Martin.
5. **Ask Daniel:** Google Play developer verification (deadline **30 Sep 2026**). It was flagged URGENT
   31 Aug and dropped from the 4 Sep handoff with no recorded closure.
6. **Needs an OK:** delete the 2 July orphans still on the live theme (`blocks/footer-copyright.liquid`,
   `templates/page.how-long-numbing-cream-takes-to-work.json`). They are unused, and the page URL already 301s.
7. **Canon owner passes (flagged, not changed):**
   - Decision 38e58bc3-75ea-817f vs -817c (founder ruling);
   - Decisions 38e58bc3-75ea-8177 (trust bar) and -81fb (bundles 5%) need supersession;
   - the 22 Jun shipping-schema decision -8109 needs a new decision (V17);
   - Compliance Hold 3bb58bc3 title still says "G1 unanswered" (owner);
   - Shipping model Confirmed Fact: re-read `deliveryProfiles` via the Admin API on the MacBook.
8. **Theme comment-only fixes, batched with the next structured-data deploy** (kept out of git so
   git == live holds): `senseless-structured-data.liquid` comments (productID `shopify_GB_`, rate-card
   re-read date, `cutoffTime` scope), `senseless-shipping-banner.liquid:7`, `senseless-header.liquid:42`
   (SBUN5), and `senseless-scale.liquid:9` / `senseless-comfort-mark.liquid:5` after the Strength ruling.
9. **Carried over:** Rich Results Test + 3 GSC "Validate fix" (from 4 Sep);
   `matrix-health-ecommerce/brands/senseless` "before 1pm" (not on the Mac mini); MC order cut-off
   15:00; Klaviyo; totallynumb.com 1pm; G2 safety gate stays open (G1 CLOSED, do not re-raise).

## Done 21–22 Sep

- **Sync (`7e944a3`):** fetch showed 0/0. A full pull of live vs `git ls-files` found one real
  difference: Shopify's Liquid migration rewrote `sections/senseless-complete-prep.liquid` on live
  (behaviour unchanged). Adopted verbatim. 117 byte-only diffs (pull noise); 113 repo-only image-pipeline
  sources; 2 live-only July orphans.
- **Audit (`93bf0e4`):** `docs/evidence/google-ads-merchant-centre-audit-2026-09-20.pdf` plus the study
  `docs/GOOGLE-ADS-MC-AUDIT-2026-09-20.md`: 9 lenses → synthesis → skeptic (25 claims re-checked, 12 fixes
  + 7 gaps applied). Verdict table V1–V56, issues the audit missed N1–N40, owner-split action list.
- **App:** Senseless 1.0.7 is LIVE on both stores (App Store released 14 Sep, Play updated 12 Sep);
  release notes state the 3pm cut-off. The in-app copy was not observed.
- **Records (`ae2c017` + Notion):** 98 stale statements found and corrected where evidence was decisive:
  - repo: CLAUDE.md range 17/22, ARCHITECTURE, COMPLIANCE/BRAND naming, DECISIONS-LOG order + footer,
    STATE.md archived pointer, consent build-report root cause, deploy rule per-machine `.env`;
  - Notion: Project Instance, 9 Confirmed Facts, Products + Handle Registry, 6 Decision rows transcribed,
    3 Stakeholder Actions closed with evidence, State Surface header + log;
  - memory rewritten as pointers.
  An independent audit confirmed 24 Notion changes. Its 2 real problems were fixed the same night.

## Gotchas (21–22 Sep)

- **Shopify rewrites theme files itself** (Liquid parser migration, with a change-log comment appended).
  Adopt verbatim with a live→git commit; never pull blindly over `main`.
- **`deploy.sh --only` never deletes**, so files removed from git linger on live.
- **Auto-mode blocks saving or printing the OAuth token response.** Check HTTP status codes and
  `.env` key presence (set/EMPTY) instead.
- **The State Surface fetch is about 240k characters.** Grep the saved tool-result file; don't read it whole.
- **Notion auto-links bare filenames** (`DECISIONS-LOG.md` → `http://DECISIONS-LOG.md`) in new rows.
  It's cosmetic; wrap filenames in backticks to avoid it.
- The State Surface log is append-only, so corrections to old entries go in the new entry
  ("Corrections to earlier log entries").

---

## Previous handoff (12 Sep 2026, MacBook Pro) — kept for reference

Same-day dispatch cut-off moved **3:30pm → 3pm** on Senseless (and Totally Numb). Theme deployed and
verified live; every Shopify-side statement and both checkout rate names changed. Then fixed the Shop
mega-menu layout. Repo == origin/main @ `daa52f7` at the time.

## Done 12 Sep — dispatch cut-off 3:30pm → 3pm (`01544e5`, `5dc687b`, lock `fbcbb59`)

- **Theme:** shipping banner (3 states), `page.delivery.json` (12), `page.tktx-numbing-cream-uk.json`
  (2), structured-data `cutoffTime` `15:00:00` (offset still from the shop clock). Deployed via
  `deploy.sh --reviews-changed`; Asset API 584 files before and after, only these 4 updated.
- **Shopify:** both rate names "Next Working Day (Order by 3pm)" (prices + conditions diffed
  unchanged), `SHIPPING_POLICY`, page `shipping-delivery` (SEO tag + `policy.prose_policy_body`),
  page `delivery` (SEO tag), article `where-to-buy-numbing-cream-for-tattoos-uk` (body + `custom.faq`).
- **Stale 1pm** removed from `docs/tattoo-cluster-content.json`, `scripts/build-tattoo-resources.py`,
  `scripts/policy-metafields.py` so a re-run can't republish it.
- **Live:** crawl of 81 URLs 0 × 3:30; Admin re-sweep 0 × 3:30. Detail in `DECISIONS-LOG.md`.

## Done 12 Sep — Shop mega-menu layout (`daa52f7`)

- `sections/senseless-header.liquid`, CSS only: Merchandise had a narrower track, so its heading broke
  "MERCHANDIS/E" and footer links wrapped, knocking the column feet out of line. Nav columns are now
  `minmax(min-content, 1fr)`; headings + footer links `nowrap`; footers 14px + 16px column bottom
  padding so they share one line with the card's "Shop the kit →"; Bundles rows `min-height: 28px`;
  card 200px at 1200–1279px.
- Verified live in Chrome at 1712px (no injected CSS): no overflow, only "Semi-permanent makeup"
  wraps (as before), footers level, first rows level.
- **Gotcha:** to preview CSS in the browser, append the test `<style>` to the END of `<body>` — the
  section's own `{% style %}` block renders in the body, so a `<style>` in `<head>` loses on equal
  specificity and the preview silently half-applies.

## Checked 12 Sep — no cut-off found (nothing to change)

- Shopify Settings → Shipping and delivery → Estimated delivery dates: Automated, fulfilment "Next
  business day"; no cut-off field anywhere in delivery or location settings.
- Customer notification emails (rendered previews): order confirmation, draft order invoice, order
  invoice, shipping confirmation, shipping update, out for delivery, delivered, order edited, abandoned
  checkout — no cut-off wording. Pickup, gift-card, returns, refunds, POS and payment-failure templates
  were not verified.
- Knowledge Base / AI-agent answers via the public Storefront MCP (`/api/mcp`,
  `search_shop_policies_and_faqs`): no cut-off returned.
- Dondy WhatsApp widget config (`widget-view.dondy.net/api/WhatsAppWidgetsView/<shop>`): no cut-off.
- Google Ads (audit only, nothing edited): account 368-965-4782 — the ads table, the account- and campaign-level assets (callouts,
  structured snippet, calls, sitelinks) and the first page of ad headlines and of descriptions (10 of 33)
  show no cut-off. Later asset pages were not verified: the table pager did not respond to automation.
- GoDaddy site `senseless-numbing.com`: no cut-off.

**Gotchas (12 Sep):**
- **Renaming a delivery method re-issues its `DeliveryCondition` ids.** A raw before/after diff of
  the rate card flags it "changed"; compare price + field/operator/amount instead.
- **The Admin writes landed ~30 min before the theme deploy.** The first deploy attempt was blocked
  by Claude Code's auto-mode permission check, so checkout and the policy said 3pm while the banner
  said 3:30pm until Daniel confirmed. Next time: deploy the theme first, then the Admin writes.
- The custom-app token lacks `read_locales` / `read_translations`, so translations can't be swept
  (no locale is published today — `/fr`, `/de`, `/en-us` all 404).

---

## Previous handoff (4 Sep 2026) — kept for reference

**Session (4 Sep 2026, MacBook Pro):** Google Search Console raised three structured-data
alerts; root-caused, fixed on both layers, and verified. Separately, the Google Ads account was
audited for the first time and the picture there is bad. Repo == origin/main @ `6053eec`, clean.

## What was wrong, and what fixed it

GSC alerted 2026-09-04 ~09:20 (forwarded by Peter 09:30): "Review has multiple aggregate ratings" —
CRITICAL for Review snippets, non-critical for Product snippets and Merchant listings.

**Root cause.** Judge.me's v3 Vue widget (`ReviewWidgetManager`, `widget_version: 3.0`,
`review_widget_revamp_enabled: true`) injected a SECOND Product node onto our own `@id`
(`<page_url>#product`) carrying only name + aggregateRating. Its duplicate-suppressor `W()` parses
only TOP-LEVEL ld+json objects and our Product sits inside `@graph`, so it never saw the rating we
already emit — while its `@id` resolver DOES walk `@graph`, which is why the injected node landed on
our exact `@id`. That asymmetry is the entire bug.

**Blast radius: 6 of 17 products** — the ones carrying reviews (professional-strength-cream 207/4.88,
clinical-strength-cream 13/4.85, advanced-strength-cream 12/4.92, vitamin-a-d-ointment-4-pack 1/5.0,
professional-strength-gel 1/2.0, advanced-strength-spray 1/5.0). The other 11 were clean only for
want of a first review.

**Two independent layers now close it; either alone is sufficient:**
1. **Judge.me dashboard** (Daniel, 13:49) — Settings → Google, SEO and AI → SEO Rich Snippets →
   BOTH "Add microdata snippets" and "Add JSON-LD snippets" unticked. Live values are now
   `disable_json_ld: true`, `remove_microdata_snippet: true`. Outside git, outside reviews-guard.
2. **Theme** (`66aa9b8`) — `class="jdgm-server-jld"` on the JSON-LD tag at
   `snippets/senseless-structured-data.liquid:139`, satisfying `N()` in the injector's gate:
   `if(i.jldDisable||i.disable_json_ld||N()||W()||!o||!e) return null;`
   Deployed via `deploy.sh --reviews-changed`; lock re-committed (`6053eec`).

## Verification state

- theme-check 0 errors (1832 warnings = pre-existing baseline).
- deploy.sh reviews-guard: all markers present 5/5 pulls.
- Asset-API remote diff: class present on live theme, `updated_at 2026-09-04T15:22:53+01:00`.
- All 6 reviewed PDPs re-fetched live: exactly 1 aggregateRating each (ours).
- Headless-Chrome CDP experiment WITH A PLACEBO CONTROL (forcing `disable_json_ld` back to false to
  reproduce): no class → 2 Product/2 ratings/1 injection; DECOY class → 2/2/1; `jdgm-server-jld`
  → 1/1/0. The decoy row proves the effect comes from the exact class string.
- NOT yet done: Rich Results Test, and the 3 GSC "Validate fix" submissions.

## GOTCHAS — read before repeating this work

- **Two Judge.me bundles exist and only one is live here.** The legacy `widget/main.js`
  (cdn2.judge.me) defines `c()` for `script.jdgm-server-jld` but EXCLUDES it from the PDP gate. The
  v3 `ReviewWidgetManager` bundle DOES gate on it. Reading the wrong bundle produced a confident,
  wrong refutation mid-session. Confirm which bundle runs before reasoning about the gate.
- **`curl` cannot see this class of bug.** The duplicate is injected after load. Two PDPs
  (professional-/clinical-strength-cream) still carry a frozen `jdgm-rich-snippet` microdata blob in
  the `judgeme.widget` metafield (written 2026-06-08) which Judge.me's JS now strips at runtime.
  Server HTML therefore still shows 1 microdata hit on those two — that is expected, not a breach.
- **Headless Chrome left 32 orphan processes** and stopped Chrome opening for the user. If a
  workflow spawns headless browsers, kill them afterwards (`pkill -f "headless=new"`).
- The Claude Chrome extension disconnected three times during the session.
- `senseless-jdgm-badge.liquid` is now redundant (Judge.me no longer emits badge microdata at
  source). Harmless; remove only as deliberate cleanup.

## Google Ads — AUDIT ONLY, do not change anything

Standing instruction from Daniel, 4 Sep: **read and report, never edit.** Agency-run account
(`ads@colossalsearch.com` / Colossal Search; Martin is the contact). See memory
`ads-account-audit-only`.

Audited 4 Sep, account "Senseless" 368-965-4782, last 30 days (5 Aug – 3 Sep):

- **Spend £1,243.14 against £921.08 of TOTAL store revenue (all channels). ROAS 0.41.**
  Prior 30 days also loss-making: £2,332 spend → £1,182 value (0.51).
- PMax: Shopping - Cream = £1,017.71 of the spend, 10 conversions, **£101.77/conversion on a ~£38
  AOV**. Senseless Search £94.93 / 3 conv. Two new Search campaigns built 27 Aug, £0 spend so far.
- **"Shopping - All products" was PAUSED on 5 Aug 15:27 by `ads@colossalsearch.com`** — a month ago,
  not "yesterday".
- Impressions peaked ~8,500/day 18–19 Aug, **crashed to 59 on 21 Aug**, then decayed to near zero;
  down 171,938 (−59%) on the prior 30 days.
- Conversion tracking WORKS (13 purchases, £505 recorded). **The "Google Ads is blind / bidding is
  starving" note from 31 Aug is REFUTED** — that was Shopify's journey data being empty, a different
  system. Real gap: Goals → Diagnostics says "You haven't set up any measurement features yet"
  (no enhanced conversions).
- "Apply for healthcare certification" alert is showing on the account. Unresolved.
- Campaign view has 2 filters applied showing 5 campaigns; not confirmed there are only 5.

**Sales reality (Shopify, via `shopify store execute`):** weekly revenue ran £250–575 through July
and early Aug, then collapsed — w/c 24 Aug £28.99, w/c 31 Aug £21.98. 1 Jul – 4 Sep total
£2,485.86 / 68 orders. **The collapse began w/c 24 Aug — before the schema breach existed** (widget
went on 31 Aug), and there were NO theme commits 28–31 Aug. The schema bug did not cause it, and
`aggregateRating` is not a Merchant Center eligibility field.

**Four questions for Martin, not yet asked:** (1) why is PMax paying £100 for a £38 order, and what
is Target ROAS set to; (2) what caused the 21 Aug impressions crash; (3) Shopping has been paused
since 5 Aug — deliberate, and what replaced it; (4) on current numbers the account loses money daily
— what is the plan and the stop-loss.

## Tooling notes from this session

- Orders/ShopifyQL: the custom-app Admin API token LACKS `read_orders` and `read_reports` (403).
  `shopify store execute -s senseless-numbing.myshopify.com --query-file f.graphql --json` CAN read
  orders but NOT products; the custom-app token is the reverse. Use both.
- Shopify MCP connector is token-expired (re-auth needs a browser). Per the standing rule that is
  NOT a blocker — the CLI + Admin API cover everything.
- Ahrefs' GSC mirror ended 27–31 Aug, so the last week of organic data was invisible. Organic runs
  at ~1 click/day (34 clicks in 39 days) and is irrelevant to revenue.
- Order attribution is empty on all 74 orders since 1 Jul (`customerJourneySummary.firstVisit` null,
  zero gclids) — a measurement gap, NOT evidence about paid traffic.

## Still open (unchanged from before)

- G2 safety gate ("Apply to clean, unbroken skin"). G1 is CLOSED — do not re-raise.
- Consent Mode v2 check on the Google & YouTube app (Daniel) — open since 31 Aug.
- Klaviyo popup suppression on gclid sessions (Daniel) — flagged since 6 Aug.
- 12 images to commission (`docs/IMAGE-BRIEF-tattoo-cluster.md`).
- "tattoo pain chart" (6,900/mo, KD 1) is still a 404; two strategy docs still contradict each other
  on whether it is winnable.
- Judge.me: only 7 products carry `judgeme.badge`; sync the rest so stars cover all cards.
