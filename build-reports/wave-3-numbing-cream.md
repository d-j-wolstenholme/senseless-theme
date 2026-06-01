# Wave 3 — Stage 1: Numbing Cream collection (model page) · HOLD checkpoint

**Date:** 2026-06-02 (BST) · **Machine:** MacBook Pro (continued session) · **Branch:** dev
**Theme:** Senseless Dev `#199324434780` (unpublished) · **Store:** senseless-numbing.myshopify.com
**Scope:** STAGE 1 ONLY — `/collections/numbing-cream` as the **site-wide model** that propagates to the other 6 collections. Built first, reviewed, then **corrected to the planning model copy** (`37258bc375ea81429e43c95a17e0e702`). Report + **HOLD**.

## Sources read in full
- 🟢 **Stage-1 model copy** — Numbing Cream collection — https://www.notion.so/37258bc375ea81429e43c95a17e0e702 (copy shipped **verbatim**, structure exact)
- 🟢 Canonical State §1 (range), §8 (quick-add card), §11 (QA gate + A–K rubric) — https://www.notion.so/37258bc375ea813e895ccbe38c0cadc8

## Review outcome — three confirms from the planning layer, all resolved

### 1 · Section order aligned to the model (decision-led) + 5 modules first-built
The first build led with the grid and was missing the decision modules. Rebuilt to the model's **9-section decision-led order** (decide, then buy):
`Hero → trust bar → strength ladder → grid → format check → philosophy → honest bit → what makes it Senseless → FAQ`
- Trust bar now sits **directly under the hero** (as on product pages); the **strength ladder sits ABOVE the grid**; the grid no longer leads.
- **Five modules first-built here** (reusable system components for Stage 2):
  - **§3 strength ladder** — NEW section `senseless-strength-ladder` (Strength | Matched-to matrix + anti-upsell note). Distinct from `senseless-strength-matrix` (procedure-suitability, in use on product pages) — not repurposed.
  - **§5 format check** — `senseless-format-row` (Gel + Spray blocks) + a new optional **footer cross-link** setting for "See all procedures".
  - **§6 philosophy** — `senseless-editorial-band`.
  - **§7 the honest bit** — `senseless-callout-band` (brand tint).
  - **§8 what makes it Senseless** — `senseless-key-facts` (4 characteristics + fixed "not a medicine" line).

### 2 · Copy shipped verbatim (planning layer owns the copy)
Every module ships the model's copy **as written** — hero, strength matrix (intro + 3 rows + anti-upsell note), format check, philosophy, the honest bit, the 4 characteristics, and **all 9 FAQs**. Render-verified each (H1, §3 heading + anti-upsell, 3 ladder rows, §4 grid heading, §5 + "See all procedures", §6 + skin-numbing-cream KW, §7, §8 + topical-numbing-cream + numbing-cream-UK KWs, 9/9 FAQ questions). No recomposition.

### 3 · "Flagship" removed from markup
The bordered Professional card's class was renamed `ss-cg__card--flagship` → **`ss-cg__card--pro`**. "flagship" now appears **0 times** anywhere in rendered markup/aria/copy. Professional = 2px `#6B3FA0` border + filled purple CTA only.

## Sort (your Q1 = yes) — applied now, convention for Stage 2
Collection set to **MANUAL** sort and reordered **Clinical → Advanced → Professional** (Admin API `collectionUpdate sortOrder:MANUAL` + `collectionReorderProducts`). Verified live: collection product order and grid DOM order both Clinical→Advanced→Professional; card prices render £44.99 → £49.99 → £55.99. **Make manual Clinical→Advanced→Professional the convention for every Stage-2 grid.**

## Render-verify (Playwright, preview theme)
| Check | Result |
|---|---|
| 9-section order present + monotonic (decision-led) | ✅ |
| Verbatim copy (15 spot-checks: headings + KW phrases) | ✅ all present |
| FAQ count | ✅ **9/9** (model) |
| "flagship" anywhere | ✅ **0** |
| Grid cards | ✅ 3 cards, order Clinical→Advanced→Professional, exactly **1** `--pro` card |
| Card interactivity (post-edit) | ✅ chips switch (£44.99→£19.99 on 30g→10g); add stays "Sold out" at 0 stock; tabs absent (show_filters:false) |
| Strength ladder | ✅ rows Clinical/Advanced/Professional + heading "Match your numbing cream to the session" |
| Schema JSON-LD | ✅ CollectionPage + ItemList + BreadcrumbList + **FAQPage (9 Questions)** |
| Keyword placement | ✅ *numbing cream* → H1 + §3 heading + intro + body + image alt + meta; *buy numbing cream* → §4 + meta; *skin numbing cream* → §6; *topical numbing cream* + *numbing cream UK* → §8 |
| Compliance | ✅ 0 banned words; no hours/onset/%/mechanism; "Is this a medicine? No."; **no "four"**; injectable-clean (format siblings + procedures hub only; no injectable terms/links) |
| Slugs | ✅ de-suffixed (`/products/clinical-strength-cream` etc.); no `/products/senseless-…` leakage |
| Build | ✅ theme-check **0 errors** (381 files; 24 pre-existing warnings); Admin-API meta set; live render reflects all 4 pushed files (Asset-API push confirmed by render) |

## Meta
- **Title** set verbatim: `Numbing Cream | Three Strengths, UK-Formulated | Senseless` (58 chars; Shopify's `<title>` appends the theme's shop-name suffix "– senseless-numbing" on every page — theme-level, not page-specific).
- **Description** set verbatim from the model.

## Flags / open items
- ⚠ **Meta description is 203 chars** — the model's description verbatim, over our seo-meta house standard (≤155). Shipped verbatim per "planning owns the copy"; Google will truncate display ~155 but the keyword-rich front ("Buy numbing cream built for aesthetic appointments, not generic skin numbing. Three strengths — Clinical, Advanced, Professional —") still shows. **Your call:** keep verbatim, or trim the model description to ≤155 (which then propagates).
- **Add-to-cart not exercisable** until stock is set (cards correctly "Sold out"); mechanics proven; AJAX add fires at launch. Same gate as product pages.
- **Judge.me per-card stars** pending app install (launch-gate); slot `:empty`-hidden until then.

## Cookie/consent aside (Canonical §9) — can the two items move from Daniel to me?
**No.** The `.env` Admin API token has 20 scopes, but the only settings-adjacent ones are `read/write_content` and `read/write_themes` — **no privacy/consent/preferences/shop-settings scope**. And independently of scope, the two cookie items are **not exposed as Admin API mutations**: disabling Shopify's native cookie banner and provisioning Customer Privacy / consent-management region settings are **Settings → Customer privacy admin-UI** actions (the consent-tracking API only lets the storefront read/set a *visitor's* consent — which the custom banner already does). So both remain **Daniel admin actions** (launch-gate). The theme-side banner wiring is already correct and verified.

## New / changed files
- **NEW** `sections/senseless-strength-ladder.liquid` (§3 — reusable strength matrix)
- `sections/senseless-format-row.liquid` (added optional footer cross-link)
- `sections/senseless-collection-grid.liquid` (`--flagship` → `--pro`)
- `templates/collection.numbing-cream.json` (rebuilt to the 9-section model)
- Admin API: collection `sortOrder=MANUAL` + Clinical→Advanced→Professional order + model SEO meta

## HOLD — Stage 1 checkpoint
Stage 2 (Numbing Gel, Numbing Spray, Microneedling, Laser Treatment, Semi-Permanent Makeup, Waxing) **NOT started** — awaiting approval of the corrected model + a decision on the meta-description length flag.
