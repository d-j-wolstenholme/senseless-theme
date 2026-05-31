# Built-State Inventory — Senseless Theme

- **Machine:** MacBook Pro
- **Date:** 2026-05-31 (BST)
- **Branch audited:** `dev` (after PR #1 merge — merge commit `2946259`)
- **Mode:** READ-ONLY audit. No code changes. (Live store navigation queried read-only via Shopify Admin API to resolve menu state.)
- **Purpose:** A complete, reality-checked picture of what is built and which locked decisions are reflected, so the next build prompt is written against reality.

> **Top-line:** the store is materially built (homepage, header/footer, 11 collections, product template, ~15 pages, 25 senseless sections). The biggest reality gaps vs locked decisions: **(1) no Product/Offer JSON-LD on product pages**, **(2) quick-add is absent storefront-wide** (cards link to PDP), **(3) `ARCHITECTURE.md` is stale** — it still documents the old injectable menu while the live nav is injectable-clean, **(4) injectable collection templates (botox/injections/lip-fillers) are still fully built and URL-reachable** though unlinked, and **(5) a couple of nav targets (`/pages/aesthetic-procedures`, `/pages/about-us`) have no matching template in-repo**.

---

## 1. SECTIONS (`sections/`)

### Senseless sections (25)
| File | Schema name | Purpose |
|---|---|---|
| `senseless-callout-band` | Callout band | Emphasised note/callout box (neutral / accent / dark variants) |
| `senseless-collection-hero` | Coll hero | Collection-page hero: heading + 4:5 media panel |
| `senseless-complete-prep` | Complete prep | "Complete your prep" complementary cross-sell card row |
| `senseless-contact-form` | Contact form | Contact form (name/email/message → form) |
| `senseless-cross-sell` | Cross-sell | Related/cross-sell product card row |
| `senseless-decision-band` | Decision | Decision/choice prompt band (canvas/dark) |
| `senseless-editorial-band` | Editorial | Editorial text band (canvas / white / dark) |
| `senseless-faq-accordion` | (per-Q) | FAQ accordion — **emits FAQPage JSON-LD** |
| `senseless-format-row` | Format row | Cream/Gel/Spray typographic panel row (intentionally imageless) |
| `senseless-guide-hero` | Guide hero | Guide / about / blog hero |
| `senseless-header` | Header | **Custom header** — mega nav driven by `senseless-main` linklist |
| `senseless-hero-brand-led` | Hero | Homepage brand-led hero (radial-gradient canvas) |
| `senseless-how-to-use` | How to use | How-to-apply step sequence |
| `senseless-image-text-band` | Image band | Alternating image + text band |
| `senseless-newsletter-signup` | Newsletter | Email capture |
| `senseless-procedure-grid` | Procedures | Procedure collection grid (1:1 cards) |
| `senseless-product-grid` | Product grid | Product grid w/ tabs — **link-only cards, no quick-add** |
| `senseless-product-hero` | Product hero | **PDP hero**: gallery + variant radios + qty + add-to-cart form |
| `senseless-product-showcase` | Showcase | Product showcase item(s), 1:1 media |
| `senseless-pull-quote` | Pull quote | Pull quote (canvas/white/sunken/tint/dark) |
| `senseless-rich-text` | Rich text | Rich-text block (canvas / white) |
| `senseless-section-statement` | Statement | Statement unit for typographic rhythm (canvas/surface) |
| `senseless-strength-matrix` | Suitability | Strength/suitability matrix table |
| `senseless-trio-card-row` | Card row | 3-up card row (tier/procedure/product/format cards) |
| `senseless-trust-bar` | Trust bar | Trust signals (4-up: UK formulated · Cosmetic product · CPSR assessed · Made for aesthetics) |

### Horizon-native sections still present (used by non-senseless templates)
`header.liquid` (emits **Organization JSON-LD**, line ~288), `footer.liquid`, `footer-utilities.liquid`, `password-footer.liquid`, `main-collection`, `main-collection-list`, `main-page`, `main-blog`, `main-blog-post` (emits **Article JSON-LD**), `main-cart`, `main-404`, `product-information` / `featured-product` / `featured-product-information` (emit **Product JSON-LD** — **but NOT used by any senseless template**, see §4), `search-header`, `search-results`, `password`.

---

## 2. TEMPLATES (`templates/`)

### index
- `index.json` — **index** → senseless-hero-brand-led, trust-bar, section-statement, trio-card-row, decision-band, format-row, pull-quote, newsletter-signup

### product
- `product.json` — **product** (shared SKU template) → senseless-product-hero, strength-matrix, how-to-use, image-text-band, trust-bar, faq-accordion, cross-sell, complete-prep, image-text-band
- `product.foaming-cleanser.json` — **product** → senseless-product-hero, image-text-band, how-to-use, image-text-band, trust-bar, faq-accordion, cross-sell *(note: a foaming-cleanser product — outside the 10-SKU numbing range; verify intent)*

### collection (all senseless-composed; **none use Horizon `main-collection`**)
- `collection.numbing-cream`, `collection.numbing-gel`, `collection.numbing-spray` — **format** hubs
- `collection.aesthetic-numbing-cream` — **procedure hub** (uses senseless-procedure-grid)
- `collection.numbing-cream-for-microneedling`, `-for-laser-treatment`, `-for-semi-permanent-makeup`, `-for-waxing` — **procedure** collections (linked in nav)
- `collection.numbing-cream-for-botox`, `-for-injections`, `-for-lip-fillers` — **procedure** collections **(fully built; NOT linked in nav — see §4 injectable-clean)**
- `collection.json` — default → Horizon `main-collection` (fallback only)

Each senseless collection composes: collection-hero + trio-card-row(s) + image-text-band(s) + product-grid (or procedure-grid for the hub) + trust-bar + faq-accordion.

### page (15 page.*.json suffixes)
about, contact, trade, faq, how-it-works, choosing-your-strength, choosing-your-format, how-to-apply-numbing-cream, does-numbing-cream-work, how-long-numbing-cream-lasts, how-long-numbing-cream-takes-to-work, senseless-vs-ametop, strongest-numbing-cream, best-numbing-cream, best-emla-alternative-uk.
- `page.about.json` is the only page on **senseless sections** (guide-hero + image-text-bands + rich-text + trio-card-row). **All other pages use Horizon `main-page`** (content driven by the page's rich-text body / metafields).
- Plain `page.json` → main-page.

### blog / article / system
- `blog.json` → main-blog · `article.json` → main-blog-post (**Article JSON-LD**)
- `cart.json` → main-cart + product-list · `search.json` → search-header + search-results
- `404.json`, `password.json`, `list-collections.json`, `gift_card.liquid`

---

## 3. SNIPPETS (`snippets/`)

Mostly Horizon stock (~100 files). Senseless-specific + load-bearing ones:

- **`senseless-typography.liquid`** — token `:root` (colour ladder + `--font-sans`) + global type scale (`.ss-h1/2/3`, `.lead`, `.eyebrow`, etc.). Loaded in `theme.liquid` after Horizon CSS.
- **`senseless-card-image.liquid`** — card-image resolver: prefers linked product/collection image with placeholder fallback + `image_picker` override.
- **`senseless-header-footer.liquid`** — **intentionally empty** placeholder (rendered in `theme.liquid`; reserved for future cross-cutting brand touch).
- **`fonts.liquid`** — preloads Montserrat 400 + 700 via `font_url` (Shopify CDN).
- **`theme-styles-variables.liquid`** — Horizon: emits `@font-face` (`font_face: font_display:'swap'`) for body/subheading/heading/accent + Horizon font vars (`--font-body--family` etc.).
- **`color-schemes.liquid`** — emits `.color-scheme-N` vars; **applies scheme-1 to `:root`** (the global canvas).
- **Product/commerce (Horizon stock):** `product-card.liquid`, `quick-add.liquid` + `quick-add-modal.liquid` (present in repo **but not used by senseless card sections**), `variant-main-picker.liquid`, `variant-swatches.liquid`, `swatch.liquid`, `quantity-selector.liquid`, `add-to-cart-button.liquid`, `price.liquid`, `sku.liquid`, `buy-buttons-styles.liquid`.
- **SEO:** `meta-tags.liquid` (title/description/OG).

**Key-facts block: ABSENT** — no key-facts snippet/section/block anywhere.

---

## 4. LOCKED-DECISION CHECK

| Decision | Status | Evidence |
|---|---|---|
| **Header nav: hub model (not old per-procedure menu)** | ✅ **Reflected** (live menu) | `senseless-header.liquid:13` reads `linklists[section.settings.menu]`; `header-group.json:17` sets `"menu": "senseless-main"`. **Live `senseless-main`** (queried): **Shop** → *By format* (Cream/Gel/Spray) + *By procedure* (Microneedling/Laser/SPMU/Waxing/"See all procedures"); **The system**; **About**; **Help**. This is the hub shape. |
| ↳ *exact spec "Shop All / By strength / By format / By procedure"* | ⚠️ **Partial** | "By format" ✓ and "By procedure" ✓ exist; **"By strength" axis is ABSENT** from nav (strength lives only under *The system → Choosing your strength*); no explicit "Shop All" (Shop parent → `/collections/aesthetic-numbing-cream`). |
| **Header reads which linklists** | — | `senseless-main` (header). Stale Horizon `main-menu` (Home/Catalog/Contact) still exists in store but is **not** wired. |
| **Injectable-clean (nav/menus)** | ✅ **Reflected** | `senseless-main` and all three footer menus surface **no Botox / Lip Fillers / Injections**. Procedures shown = Microneedling, Laser, SPMU, Waxing only. |
| **Injectable-clean (whole build)** | ⚠️ **Partial / conflict** | But `templates/collection.numbing-cream-for-botox.json`, `-for-injections.json`, `-for-lip-fillers.json` are **fully built senseless collections** — URL-reachable + crawlable even though unlinked. Not stubs. See Gaps. |
| **Footer structure + policy links** | ✅ **Reflected** | `footer-group.json`: 3 senseless menus (`senseless-footer-shop` / `-explore` / `-company`) + `footer-utilities` + `footer-policy-list` (iterates `shop.policies` → Privacy/Terms/Refund/Shipping) + `social-links` + `footer-copyright`. |
| **Footer MHG logo → matrixhealthgroup.co.uk** | ❌ **Absent** | No `matrixhealthgroup.co.uk` link or MHG logo anywhere in code. MHG appears only as **body copy** on About/Contact/FAQ pages. `senseless-header-footer.liquid` is empty. |
| **Quick-add on product cards (variant/size + qty + add-to-cart)** | ❌ **Absent (storefront-wide)** | All active collections use `senseless-product-grid` (link-only cards — no `cart/add`, no add button). Horizon `quick-add.liquid` exists but is **not wired** into any senseless section. Add-to-cart exists **only on the PDP**: `senseless-product-hero.liquid:121` `form 'product'`, `:137` hidden `name="id"`, `:138` `<button name="add">`. |
| **Key-facts block** | ❌ **Absent** | No such snippet/section/block. |
| **Schema / JSON-LD — FAQPage** | ✅ Present | `senseless-faq-accordion.liquid:56` (FAQPage + Question/Answer). |
| **Schema — Organization** | ✅ Present | Horizon `header.liquid:288` (emits on every page via layout). |
| **Schema — Article** | ✅ Present | Horizon `main-blog-post.liquid` (used by `article.json`). |
| **Schema — Product / Offer** | ❌ **Absent on product pages** | Product JSON-LD lives only in Horizon `product-information`/`featured-product` sections, which **`templates/product.json` does NOT use** (it uses `senseless-product-hero`, which emits no structured data). So real PDPs ship **no Product/Offer schema**. |
| **Schema — CollectionPage / ItemList** | ❌ Absent | Not emitted anywhere. |
| **Schema — BreadcrumbList** | ❌ Absent | Not emitted anywhere. |
| **Locked slugs (no size-suffix, no Clinical Gel)** | ✅ **Reflected** | No `-30g/-10g/-35ml/-100ml` slugs; no "Clinical Gel" links. Collections format/procedure-based; products variant-driven. Only "no Clinical gel" appears as **copy** (`page.choosing-your-format.json`), which is correct. |
| ↳ *nav target integrity* | ⚠️ **Partial** | `senseless-main` links `/pages/about-us` and "See all procedures" → `/pages/aesthetic-procedures`. **Neither has a matching template in-repo** (`page.about.json` exists with suffix `about`, not `about-us`; no `aesthetic-procedures` page/template). Per DECISIONS-LOG the `about-us` page was repointed to the `about` template in admin — verify both pages exist in admin or these are dead links. |

### Tokens — DEFINED vs APPLIED
Global `:root` tokens live in `snippets/senseless-typography.liquid`. Sections additionally define **scoped `--ss-*`** mirrors (e.g. `--ss-bg:#f7f7f5`, `--ss-surface:#ffffff`, `--ss-text`, `--ss-border`) and paint those.

| Token | Defined | Applied? |
|---|---|---|
| `--text-primary` `#1A1816` | ✓ | ✓ (headings) |
| `--text-body` `#2B2730` | ✓ | ✓ (body color) |
| `--text-secondary` `#5C5853` | ✓ | ✓ (lead/caption) |
| `--text-muted` `#8E8A82` | ✓ | ✗ **defined, unconsumed** (reserved — owner: keep) |
| `--brand-primary` `#6B3FA0` | ✓ | ✓ (eyebrow + 26 files use literal) |
| `--bg-canvas` `#f7f7f5` | ✓ | global token still ✗ unconsumed, **but canvas now applied via `scheme-1` background (fixed 2026-05-31) + sections' scoped `--ss-bg`** |
| `--bg-surface` `#ffffff` | ✓ | ✗ global unconsumed (reserved — owner: keep; sections use scoped `--ss-surface`) |
| `--font-sans` Montserrat stack | ✓ | ✓ (body + h1–h6) |

---

## 5. CONFIG / STATE

- **Fonts** (`config/settings_data.json`): `type_body_font montserrat_n4`, `type_subheading_font montserrat_n6`, `type_heading_font montserrat_n7`, `type_accent_font montserrat_n6`. Served via Shopify CDN, `font-display:swap`, preload 400/700. Zero Google-Font requests.
- **Colour schemes** (7): `scheme-1 #f7f7f5` **(brand canvas — set 2026-05-31; applied to `:root`)**, `scheme-2 #f5f5f5`, `scheme-3 #eef1ea`, `scheme-4 #e1edf5`, `scheme-5 #333333` (dark), `scheme-6` transparent, + 1 custom transparent. Scheme usage across sections/templates: scheme-1 ×13, scheme-5 ×7, scheme-3 ×3, scheme-2 ×2, scheme-6 ×2, scheme-4 ×1. **Scheme primary buttons remain Horizon `#000000`** — purple is accent-only per BRAND.md; native primary CTAs are not purple by design.
- **Other locked settings:** page_width narrow; button radius 14; card radius 4; product card radius 0; badge radius 100; cart drawer + drop shadow. All match BRAND.md.
- **Nav data (store-side):** `senseless-main` (header), `senseless-footer-shop/-explore/-company` (footer). Horizon `main-menu` + `footer` menus exist but unused.

---

## 6. GIT STATE

- **Branches:** `dev` (current, clean), `main`, `build/phase-0-foundations` (merged into dev). Remotes: `origin/dev`, `origin/main`, `origin/build/phase-0-foundations`. `origin/HEAD → main`.
- **Working tree:** clean (the header/logo edits were committed by owner as `6121e39` and merged via PR #1).
- **Recent dev history:** `2946259` merge PR #1 → `bb10b88` logo img width fix → `893ccce` scheme-1 canvas #f7f7f5 → `6121e39` inline header logo SVG (owner) → `311c13b` Phase-0 verify+report.
- **DECISIONS-LOG phase summary:** 2026-05-27 fresh Horizon base + scaffolding → 2026-05-28 full site build (Batches 2–6, 22 templates, 9 sections) + range correction (10 SKUs, no Clinical Gel, de-suffixed slugs) + dev-theme target fix (#196680057167) → 2026-05-29 Phase 0 typography (Montserrat/Shopify CDN), Phase 1 header/nav/footer + 13 backing pages, Phase 2 trust signal (CPSR), Phase 3 card images + CPSR confirmed → Phase A homepage recompose + fully custom header + format positioning → **2026-05-31 Phase-0 verify + scheme-1 canvas fix** (this session).
- **`theme check`:** 0 errors, 24 warnings.

---

## 7. GAPS / CONFLICTS (punch-list)

1. **Product/Offer JSON-LD missing on PDPs.** `templates/product.json` uses `senseless-product-hero` (no structured data); Horizon's Product emitters aren't in the template. **SEO-critical.** → add a Product+Offer JSON-LD emitter to `senseless-product-hero` (or a snippet).
2. **No CollectionPage/ItemList or BreadcrumbList schema** anywhere. → consider adding for collections + breadcrumbs.
3. **Quick-add absent storefront-wide.** Senseless cards are link-only. If quick-add is a locked requirement, it must be added to `senseless-product-grid`/card sections (Horizon `quick-add.liquid` is available to adapt).
4. **`ARCHITECTURE.md` is STALE** — it documents the OLD nav (`By Procedure → Lip Fillers / Botox / Microneedling / SPMU / Laser / Waxing`). Live nav is injectable-clean (Microneedling/Laser/SPMU/Waxing only). → update `ARCHITECTURE.md` to the hub + injectable-clean model. *(Note: an earlier inventory agent wrongly "confirmed" Lip Fillers/Botox in nav by reading this stale doc — the live store query disproves it.)*
5. **Injectable collection templates still built & reachable** (`numbing-cream-for-botox/-injections/-lip-fillers`). Unlinked but crawlable. → decide: delete/redirect, or `noindex`, to honour injectable-clean.
6. **Nav dead-link risk:** `/pages/aesthetic-procedures` (no template/page in repo) and `/pages/about-us` (repo has `page.about` suffix only). → confirm both pages exist in admin with correct template assignment, or fix the links/create the pages.
7. **No "By strength" shop axis** in nav despite tiers (Clinical/Advanced/Professional) being core. → decide whether a strength-led entry belongs in `senseless-main`.
8. **No footer MHG attribution link** to `matrixhealthgroup.co.uk` (only in-body copy). → add to footer if required for parent-company attribution.
9. **Key-facts block absent.** → build if the PDP/collection spec calls for a structured key-facts module.
10. **`product.foaming-cleanser.json`** exists — a product outside the 10-SKU numbing range. → confirm intentional or remove.
11. **Reserved-but-unconsumed global tokens** `--bg-surface`, `--text-muted` (owner: keep, to be consumed as components build). Sections currently use scoped `--ss-*` instead of the globals — consider unifying so the global tokens are the single source.
12. **Stale unused Horizon menus** (`main-menu`, `footer`) remain in store nav. Harmless; tidy if desired.
