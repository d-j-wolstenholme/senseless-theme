# PHASE 13 — Full Site Audit (read-only, 12 domains)

**Date:** 2026-06-06 (BST) · **Branch:** dev · **Theme:** Senseless Dev `#199324434780` (unpublished, password-gated). **MAIN Horizon `#199321977180` never touched.** Token refreshed (read-scoped: content + themes only).

**READ-ONLY — no edits, no deploys.** Audited against the locked canon: Canonical State (§11 QA gate) + DECISIONS. Fixes follow as separate triaged briefs.

**Method:** 10-agent workflow — 7 static/Admin-API recon agents + 3 Playwright render agents (desktop 1366 + mobile 390, axe-core, structured-data, link resolution). theme-check, banned-term/slop grep, JSON-LD validation, Admin-API catalogue/collections/metafields/policies/settings.

**Result:** **110 findings — P0 ×6 (4 distinct; 2 double-reported) · P1 ×23 · P2 ×35 · P3 ×46.** Theme-check **0 errors**. Catalogue, prices, compliance-claims and injectable-clean are in strong shape; the launch blockers are an admin noindex flag, the 7 known placeholder images, two application-page compliance gaps, and a cart-drawer bug.

Each finding tagged **[API]** (API/theme-verifiable) or **[ADMIN]** (Daniel to confirm/fix in admin).

---

## ★ CONSOLIDATED P0 — LAUNCH GATES (4 distinct)

1. **`/collections/shop-all` is set to noindex** (Admin `seo.hidden=1`) — a primary money/commerce collection (nav + llms.txt destination) excluded from search. Compounded by **H1 count = 0** and **no meta description** on the same page. **[ADMIN]** — Admin → Collections → Shop All → Search engine listing → untick "Hide from search results"; add H1 + meta description. (All 15 products + the other 13 collections are correctly indexable — only shop-all.)

2. **7 placeholder product images live on money pages with literal placeholder ALT text.** The 7 products flagged `senseless.image_placeholder=true` (gels ×3, sprays ×3, cleanser) render a generic range stock shot, and their alt text is literally `"[PLACEHOLDER — strength-specific shot pending] Senseless range…"` — visible to screen-readers on Home, all gel/spray/cleanser PDPs, `/collections/shop-all` (9 such images), numbing-gel, numbing-spray. **[API/store]** — replace with real per-SKU pack artwork via the image pipeline + clear the metafield; **keep theme unpublished until cleared** (known gate a + e).

3. **`/pages/using-numbing-cream` is missing the required patch-test (24h) beat.** The canonical application page (§7/§11) must carry a patch-test instruction; rendered copy contains no "patch test" / "24 hour" anywhere. **[API — content/metafield]** — add "Do a patch test ~24h before first use; don't use if any reaction." (Daniel/planning authors copy.)

4. **`/pages/using-numbing-cream` is missing the occlusion/cover step.** Routine reads clean → apply → leave on → remove, with no "cover/occlude (cling film)" beat (required application instruction per §7). **[API — content/metafield]** — insert an occlusion step between apply and leave-on.

> Also standing/known launch-gates (confirm, not new): **Judge.me not installed** (reviews slot empty — correctly emits no Review/AggregateRating schema, good); **two cookie banners** render (Shopify native `#shopify-pc__banner` + the bespoke `.ss-cc`) → disable native + provision Customer Privacy **[ADMIN]**; **free-shipping £40/£80 thresholds** unverifiable via token **[ADMIN]**; **keep theme unpublished** until images + gates cleared.

---

## ★ ADMIN-UI-ONLY ITEMS FOR DANIEL (consolidated)
- **P0** Untick noindex on the **Shop All** collection (+ add H1/meta).
- **P1** Set the **shop name to "Senseless"** (Admin → General) — currently `senseless-numbing`, which (a) is the homepage `<title>`/`og:title` fallback and (b) leaks as the "– senseless-numbing" suffix on **every** page title.
- **P1** Set a **homepage SEO title + meta description** (none currently).
- **P1** **Customer accounts → Classic + branded** — currently NEW passwordless; account links point off-domain to `shopify.com/.../account` (canon = native classic, branded).
- **P1** Confirm **free-shipping £40/£80** rules exist + shipping rates match the Shipping policy (£1.99/£2.99/£7.99).
- **P1** **Cookie:** provision Customer Privacy / consent management + **disable Shopify's native banner** so only the bespoke `.ss-cc` shows (two banners currently).
- **P1** Provide the **VAT number** (Contact legal block shows "to be confirmed before launch" while Terms states VAT-inclusive).
- **P1** Set **noindex on Contact + the 5 policy pages** (theme has no robots mechanism; Contact page is noindex via metafield, but the 5 policy `/pages/*` and the native `/policies/*` are currently indexable).
- **P2** **Bundles SEO** — 5 bundles have no meta title/desc (320-char body leaking as desc), empty featured-image + alt; add per-bundle SEO + image.
- **P2** Page meta for **the-senseless-system, aesthetic-procedures, articles** (blank); shorten over-length titles (waxing 63, trade 69 chars).
- **P2** **Store email** = personal iCloud → branded `cs@senseless.uk`.
- **P2** **Privacy policy** = unmodified Shopify default with raw `{{ }}` placeholders → MHG-tailored UK-GDPR rewrite.
- **P2** **Refund policy** add explicit **14-day Consumer Contracts Regulations 2013** cooling-off right.
- **P3** Add a "Prices include VAT" note on PDPs (taxesIncluded=true confirmed). Confirm unreadable settings: Markets, payment methods, checkout branding, email-notification templates, web pixel.
- **Gate** Install Judge.me (drop app block; keep Review schema gated until reviews exist); keep theme unpublished; replace 7 placeholder images.

---

## DOMAIN 1 — COMPLIANCE
**Headline: very clean on the highest-risk axes.** ZERO banned claim words (pain-free/painless/completely numb/no pain/won't-feel-anything/eliminates), ZERO percentages/strength-%, ZERO named actives in Senseless's own copy (EMLA/Ametop appear only as competitor names on the approved comparison landers), ZERO mechanism-of-action, ZERO AI-slop, ZERO "made/manufactured in the UK". Injectable-clean holds on every ad surface (no commerce links into botox/lip-fillers/injections collections); the System-page + does-it-hurt educational text is the approved/closed exception. Trust bar = the 4 locked signals.

- **P1 [API]** `collection.aesthetic-numbing-cream.json:40-42` — LIVE Stage-1 tier model uses banned brand words + implied mechanism: Clinical "The **everyday** Senseless…", Advanced "The considered **upgrade**. Higher **concentration**…", Professional "Our most **concentrated** formula". Fix → canonical Scale framing ("standard-strength / higher-strength / highest-strength"; drop everyday/upgrade/concentration).
- **P2 [API]** Same banned tier-card copy is **shared** (via the trio-card-row / tier-card snippet) onto LIVE SEO landers `page.senseless-vs-ametop.json` + `page.best-emla-alternative-uk.json` ("The everyday formula", "The considered upgrade", "Higher concentration", "Our most concentrated formula"). Root cause = one shared copy block → fix once at source.
- **P2 [API]** `page.trade.json:84` — banned word **"flagship"** in visible body ("The flagship is sold direct-to-consumer…"). (The schema `flagship` styling key is NOT a finding.)
- **P2 [API]** Retired guide templates (`strongest-numbing-cream`, `choosing-your-strength`, `choosing-your-format`, `how-long-*`, `how-to-apply-numbing-cream`) still hold "concentration/upgrade/everyday" + an onset/mechanism line ("different concentrations means different recommended timing"). Confirm page resources are unpublished + 301'd; strip if templates retained.
- **P2 [API]** `product.json` (default fallback) carries the same banned words — unused if every SKU keeps its custom template, but a latent defect; align or delete.
- **P3** Internal `--flagship` CSS class on cross-sell/Professional cards (not rendered to visitors) — optionally rename to `--professional`. Homepage "highest strength in the system" is acceptable under the Scale (no strongest/flagship in visitor copy).
- **False-positives (no action):** "painless" on `do-lip-fillers-hurt` is a compliant debunk; "strongest" on the System FAQ is a descriptive debunk ("stronger is NOT automatically better").

## DOMAIN 2 — CONTENT / COPY
Sizes are correct everywhere; the issues are stale bundle copy, hardcoded prices and exposed placeholders.

- **P1 [API]** `product.bundle.json:13-14,73-74,95` (shared by all 5 bundles) — stale **"kit"** naming + "Small and Large" tiers instead of **Starter/Ultimate** ("In the kit", "Which kit should I choose?", "Small and Large differ by…"). The product titles were renamed; the template copy wasn't.
- **P1 [API]** Hardcoded visitor-facing **"£TBC"** on `senseless-trio-card-row` blocks with no linked product (`collection.aesthetic-numbing-cream.json:61-63` LIVE + retired pages + `product.json`). Section renders the literal `block.settings.price` when `card_product` is blank.
- **P1 [API]** `page.contact.json:46` — internal note **"(placeholder — confirm before launch)"** exposed to visitors next to the legal/data email. (`cs@senseless.uk` itself is intentional; the parenthetical is the leak — recurs at contact:19,37,46 + about:36.)
- **P2 [API]** `product.bundle.json:36,62,74` — bundle contents copy omits the **vanity bag** (lists only cream+gel+spray+cleanser); canon bundle includes a vanity bag.
- **P2 [API]** `product.json:8` trust_line "Free UK shipping over **£TBC**".
- **P2 [API]** `page.contact.json:140` — "VAT number: **to be confirmed before launch**" rendered in the live company block.
- **P2 [API]** `page.choosing-your-format.json:178` — factual contradiction: "Spray starts at Advanced, not Clinical" but a **Clinical Strength Spray exists** (£19.99). (Retired page — fix or confirm 301.)
- **P2 [API]** `collection.numbing-spray.json:310-311` — spray-collection FAQ recommends spray "to prepare for injectable appointments"; miscategorised (spray = large/body areas; injectables → cream/gel) + funnel issue.
- **P2 [ADMIN]** "Stocked/used in **clinics** across the UK" / "Trusted at the chair" (home uses "studios") on Home + About — substantiation risk; standardise clinics-vs-studios; confirm evidence.
- **P3** "The Senseless System" capitalisation inconsistency (~26 lowercase "the system"); duplicated intro across `does-it-hurt` vs `does-it-hurt-by-treatment`; FAQ headline punctuation drift ("Common questions" vs "Common questions."); "available without restriction" (×7) implies it could otherwise be restricted.

## DOMAIN 3 — SEO (on-page + technical)
- **P0 [ADMIN]** `/collections/shop-all` noindex (see P0 #1) + H1=0 + no meta desc.
- **P1 [ADMIN]** Homepage has **no meta title + no meta description**; `<title>`/og:title fall back to "senseless-numbing".
- **P1 [ADMIN]** Every page title carries the **"– senseless-numbing" suffix** (raw store handle) → set shop name to "Senseless".
- **P1 [API]** Duplicate **H1** across two indexable landers: `best-emla-alternative-uk` + `senseless-vs-ametop` both = "A different category. A different purpose."
- **P2 [ADMIN]** 5 bundles: no meta title/desc (320-char admin-body leaks as desc); bundle featured-image **alt empty**. Over-length titles: numbing-cream-for-waxing 63, trade 69. No meta on the-senseless-system / aesthetic-procedures / articles.
- **P2 [ADMIN]** 5 policy `/pages/*` not flagged `seo.hidden` (indexable); canon = policy pages noindex. Native `/policies/*` also emit no robots (indexable). Contact correctly noindex.
- **P3** `/sitemap.xml` 404 + `/llms.txt` 302→/password (expected pre-launch — re-verify after publish); `senseless-page-schema.liquid` stale "Horizon emits BreadcrumbList" comment; System page H1 is the Selector's "Make your Senseless Selection" (heading-semantics note); articles hub thin meta ("Guides and articles.", 20 chars).

## DOMAIN 4 — GEO / AI-SEARCH
Product/Offer, FAQPage, BreadcrumbList, Article, Organization all present + valid; **AggregateRating correctly gated** (no leak with zero reviews).
- **P2 [API]** `the-senseless-system` (the named GEO/citation hub) has **no Key Facts** block. `does-it-hurt` hub has **no FAQ accordion (no FAQPage)** and **no Key Facts** — a GEO miss on a high-intent "does it hurt" query.
- **P2 [API]** Live `/robots.txt` serves Shopify's default (no AI-bot allow-groups, no Sitemap line) rather than `templates/robots.txt.liquid` — re-verify after publish (launch-gate check).
- **P3** Key Facts on 4/7 procedure collections (absent on the 3 injectable); Org-schema NAP/email inconsistency across schema surfaces; format collections emit two ItemList nodes (nested + standalone).

## DOMAIN 5 — VISUAL DESIGN / BRAND
Design system largely faithful: every section redefines `--ss-purple:#6B3FA0`, CTAs filled-purple @14px radius, headings weight 400 + `-0.02em` + italic accent, Professional = 2px `#6B3FA0` border + 4px radius (confirmed, no "flagship" badge), dividers on `var(--ss-border)`.
- **P2 [API]** Undocumented **"brand dark" `#241836`** (aubergine) used as a **full-section background** across 5 sections (decision-band, guide-hero, pull-quote, editorial-band, trio-card-row) + companion tint text colours (#c8a9e6, #b794d6, …) — none in the canonical token list/BRAND.md. Either adopt as official tokens (define once) or reconcile.
- **P2 [API]** "Purple tint" band option paints the whole band with `rgba(107,63,160,0.06-0.07)` (decision-band, pull-quote) — borderline vs "purple is accent only, never a section background". Confirm with Daniel or remove the option.
- **P3** Hardcoded `#E5E2DC` divider (`complete-prep`) instead of `var(--ss-border)`; card-radius drift (product-showcase 6px, selector 8px vs canon 4px); mega-menu featured image default 4/3 (overridden to 1/1 on mobile only); off-token icon fill `#333030`; article-body H2 weight 600 (canon H2=400).

## DOMAIN 6 — UI / UX
- **P1 [API]** **Cart drawer never opens** on add-to-cart **or** quick-add (desktop + mobile). Item adds (count increments, `/cart` correct, banner math correct) but a `pageerror` fires — *"Failed to execute 'showPopover'… not connected"* — so the `<cart-drawer-component>` is detached/re-rendered before `showPopover()`. Net effect: items add **silently, with no drawer/notification feedback** → real conversion risk. (config `cart_type=drawer`.)
- **P3** Contact + Trade forms POST to native `/contact` (`form_type=contact`), fields labelled + validated (no CRM endpoint — flag if a CRM route is intended). Header (Shop/System/Articles/About/Help; **Trade footer-only**, correct), flyouts and footer links resolve. 404 branded with nav/search. Free-shipping banner reads £40/£80 correctly (rules = ADMIN confirm).

## DOMAIN 7 — ACCESSIBILITY (WCAG 2.1 AA, axe-core)
- **P1 [API]** **CRITICAL `aria-required-children`** on PDPs: `<div class="ss-sb__grid" role="table">` (strength comparison/Scale module) has no row/rowgroup children. Fix → add row/cell roles or drop `role=table` / use a real `<table>`.
- **P1 [API]** Triple-nested `<footer>` → `landmark-contentinfo-is-top-level` (×2), `landmark-no-duplicate-contentinfo`, `landmark-unique` on **every** page. Fix → make the wrapper(s) `<div>` so one top-level contentinfo remains.
- **P2 [API]** `aria-hidden-focus` (serious) on every page: the mobile nav drawer is `aria-hidden` while closed but keeps focusable links in tab order → use `inert`/`display:none`/`tabindex=-1`. Same pattern on Contact + Cart (off-canvas/cart drawer).
- **P2 [API]** System page: 2× `color-contrast` failures (low-contrast text pairs against tokens).
- Recommend confirming a skip-link; reduced-motion is already respected in the header.

## DOMAIN 8 — PERFORMANCE / TECHNICAL
- **P3** **theme-check 0 errors**, 52 warnings in 3 non-blocking classes: HardcodedRoutes ×26, ValidScopedCSSClass ×24 (mostly inherited Horizon search snippets + new BEM classes), VariableName ×2.
- **P3** Image pipeline healthy: 8 processed images all 1254×1254 square JPG, 55-103KB (none >300KB; Shopify serves WebP/AVIF + srcset). Above-fold heroes use `loading=eager`+`fetchpriority=high`; below-fold lazy. Montserrat self-hosted via Shopify font CDN (`font_face`), no Google Fonts, no FOUT risk.
- **P3** **4 unused sections** (never referenced as a `type` in any template/section-group): decision-band, product-showcase + 2 others — dead code to prune.
- Console: recurring `shop.app` frame-ancestors CSP + 403 on every page = password/preview-mode infrastructure noise (re-verify clean after publish), not a defect.

## DOMAIN 9 — CATALOGUE INTEGRITY (Admin API)
**Strong.** All 15 products ACTIVE; all 10 single SKUs match canon exactly on price/size/variant-order (smaller-size-first)/inventory=20, no stray compareAt, correct productType + templateSuffix. **All 5 bundles perfect** — titles Starter/Ultimate, prices, savings, compareAt=sum, productType=Bundle, handles, template.
- **P0 [API]** 7 products carry `senseless.image_placeholder=true` (gels ×3, sprays ×3, cleanser) — see P0 #2.
- **P1 [API]** `senseless.tier` + `senseless.format` are **NULL on all 10 single SKUs** (only the 5 bundles are populated). The Scale/format system has nothing to bind to for the core range — populate tier (Clinical/Advanced/Professional) + format (Cream/Gel/Spray/Cleanser).
- **P1 [API]** All 5 bundles have **featuredImage = NONE** (not flagged by `image_placeholder`, so invisible to that gate) — bundle cards render imageless. Add images or flag them.
- **P2 [API]** `clinical-strength-gel` + `clinical-strength-spray` have empty `recommended_procedures` → they appear in **zero** procedure collections. Confirm intentional or populate.
- **P3** shop-all smart rule = `VARIANT_PRICE > 0` (captures all incl. bundles — confirm intended); `aesthetic-numbing-cream` (+1) have no custom templateSuffix; injectable collections populated (good — published SEO); auto `frontpage` collection has 1 product.

## DOMAIN 10 — ADMIN / STORE SETTINGS (mostly ADMIN-UI)
- **P1 [ADMIN]** Customer accounts on **NEW passwordless** flow; canon = native **Classic + branded**. New-account links go off-domain (`shopify.com/.../account`).
- **P1 [ADMIN]** Theme has **no robots mechanism** → Contact + policy noindex depends entirely on admin per-page flags (Contact is set; policies are not — see Domain 3).
- **P1 [ADMIN]** **Shipping** (`deliveryProfiles` ACCESS_DENIED — `read_shipping` not in token) → confirm £40/£80 free thresholds + rates vs Shipping policy.
- **P2 [ADMIN]** Store `email`/`contactEmail` = **personal iCloud** (`d.j.wolstenholme@icloud.com`) → branded address.
- **P2 [ADMIN]** Customer Privacy / consent + native banner (two-banner gate).
- **P3 [ADMIN]** `taxesIncluded=true` (VAT-inclusive, correct) but no "Prices include VAT" note on PDPs; **Markets / payments / checkout branding / email-notification templates / web pixel** unreadable with this token — confirm in admin; billing address mostly empty. Shopify native nav menus are decoupled from the bespoke header (intended).

## DOMAIN 11 — LEGAL / REGULATORY (UK cosmetics)
- **P1 [API/business]** **VAT number is a placeholder** ("to be confirmed before launch") on Contact while Terms states VAT-inclusive + `taxesIncluded=true` — a VAT-registered seller must display the number (or remove VAT-inclusive wording if not yet registered).
- **P1 [API]** `cs@senseless.uk` carries "(placeholder)" qualifiers in production-facing legal text (the address is intentional; the qualifier is the leak).
- **P2 [API]** Native **Privacy policy = unmodified Shopify default** with raw `{{ last_updated }}`/`{{ shop_name }}` placeholders; not MHG-tailored as data controller.
- **P2 [API]** Native **Refund policy** lacks the explicit **14-day Consumer Contracts Regulations 2013** right-to-cancel (only a 30-day goodwill return + hygiene exclusion).
- **P3** "CPSR assessed" present (good); INCI correctly kept off-site (pack only); no Responsible Person named (confirm if required). MHG company details consistent; **phone 0333 049 5549 is NOT in the footer/homepage body** (see Domain 3/trust) — add as a `tel:` link + confirm in Organization schema.

## DOMAIN 12 — CROSS-DEVICE
All 26 money pages + content/legal pages return 200 at desktop **and** mobile; **no horizontal overflow on mobile**. The two-banner cookie issue and the cart-drawer bug reproduce on both viewports. No browser-specific breakage observable in the harness (Chromium only).

---

## POSITIVE CONFIRMATIONS (logged so they aren't re-flagged)
- Compliance claim-axes clean (no pain/% /actives/mechanism/slop/made-in-UK); injectable-clean holds on all ad surfaces; trust bar = the 4 locked signals.
- Catalogue + prices + bundles match canon exactly; inventory 20/SKU; variant order smaller-first; Professional = border+filled-CTA (no flagship badge).
- Structured data complete + valid per type; AggregateRating gated until reviews exist.
- Header (Shop/System/Articles/About/Help; Trade footer-only), flyouts (hover+keyboard+tap), footer links, 404, breadcrumbs all resolve.
- Selector embedded on the System page renders + functions; no redundant same-page CTA found (the earlier System "Find your strength" redundancy is already resolved).
- theme-check 0 errors; image pipeline 1:1 square + lightweight; Montserrat self-hosted; lazy-loading correct.

## SCOPE LIMITS (read-scoped token)
Could NOT read (record as ADMIN-UI for Daniel): shipping/delivery profiles, markets, payments, checkout branding, email-notification templates, web pixel/analytics, discounts, locations, script tags. Live `/robots.txt`, `/sitemap.xml`, `/llms.txt` are masked by the storefront password — re-verify at launch.

## HOLD
Read-only audit complete. **No fixes applied.** Recommend triaging the 4 P0s + the cart-drawer P1 first, then the shared tier-card banned-copy block (one fix clears several Domain-1/2 findings), then the ADMIN-UI batch for Daniel.
