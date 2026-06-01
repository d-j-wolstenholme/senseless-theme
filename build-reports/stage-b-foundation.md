# Stage B — Theme Foundation (senseless-numbing)

**Date:** 2026-06-01 (BST)
**Machine:** MacBook Pro
**Branch:** dev (up to date with origin/dev)
**Scope:** Push dev theme as a new **unpublished** theme, capture ID, audit Phase 0–2 + globals against what's actually built. **No publish. No product/collection/content work.**

> **Update 2026-06-01 ~17:10 BST — Stage B fixes applied.** Four foundation gaps from the audit below are now fixed and redeployed to the unpublished preview. See **"Stage B — Fixes applied"** at the end of this report. Theme check still **0 errors**; Horizon still **[live]**, Senseless Dev still **[unpublished]**.

---

## Deploy result

- **Theme:** "Senseless Dev" — **ID `199324434780`** — role **unpublished** ✅
- **Pushed via:** `shopify theme push --store senseless-numbing.myshopify.com --unpublished --theme "Senseless Dev"` (CLI 3.94.3)
- **Store default untouched:** `Horizon #199321977180` remains **[live]**. ✅ Not published.
- **`.env`:** `SHOPIFY_DEV_THEME_ID=199324434780` set.
- **Shop confirmed before push:** `{ shop }` → `senseless-numbing` / `senseless-numbing.myshopify.com`. ✅
- **Preview URL:** https://senseless-numbing.myshopify.com?preview_theme_id=199324434780
  - ⚠️ Storefront is **password-protected** (root + preview both 302 → `/password`). Rendered/visual verification (and a live DOM Google-Fonts check) requires the storefront password or the admin theme preview. Source-level checks below stand regardless.

## Theme check

- **`shopify theme check` → 0 errors.** 367 files inspected, **24 warnings** across 8 files (all `warning`/`info`; e.g. `ValidScopedCSSClass` in stock Horizon snippets like `search-modal.liquid`). No errors. ✅

## Google Fonts

- **0 Google-Fonts requests in theme source** (`fonts.googleapis.com` / `gstatic.com` across `*.liquid`/`*.json`/`*.css`). Only hit is a descriptive line in `docs/BRAND.md`. ✅
- Fonts self-host via Horizon `font_face` loop in `snippets/theme-styles-variables.liquid` (`| font_face: font_display: 'swap'`). Live-DOM count pending storefront password (see preview note).

---

## Phase 0 — Typography & tokens

| Item | Status | Notes |
|---|---|---|
| Montserrat self-hosted | ✅ Present | Wired via Horizon font roles in `settings_data.json`: body `montserrat_n4`, subheading `montserrat_n6`, heading `montserrat_n7`, accent `montserrat_n6`. Emitted via `font_face` in `theme-styles-variables.liquid`. |
| Weights 400 / 600 / 700 | ✅ Present | n4=400 (body), n6=600 (subheading/accent), n7=700 (heading). |
| Weight **500** (medium) | ⚠️ **Gap** | **No `montserrat_n5` role**; 500 is not emitted as a self-hosted webfont weight. `font-weight: 500` is referenced in stock Horizon CSS (cart-summary, list-filter, sorting, localization-form) → those will fall back / faux-render, not load a real 500. Phase 0 spec asks for 400/**500**/600/700. |
| 0 Google Fonts | ✅ Present | See above. |
| `--bg-canvas #f7f7f5` wired to **scheme-1** | ✅ Present | `scheme-1.background = #f7f7f5` in `settings_data.json` (genuinely on the color scheme). Also mirrored in `:root` of `senseless-typography.liquid`. |
| `--brand-primary #6B3FA0` | ⚠️ Present but **NOT via scheme-1** | Defined as a CSS var in `:root` of `snippets/senseless-typography.liquid` (rendered globally in `theme.liquid:34`) **and** repeated as `--ss-purple: #6B3FA0` per senseless-section. **`scheme-1` itself carries no purple** — its `primary`/`primary_button_background` are black (`#000000`). So Horizon-native buttons render **black**, not brand purple; purple appears only where senseless sections call `var(--brand-primary)`/`--ss-purple` (eyebrows, accents). This matches BRAND.md ("accent only") but **diverges from the brief's "wired to scheme-1" framing** — see Open Question 2. |
| `--text-body #2B2730` | ⚠️ Present but **NOT via scheme-1** | Set in `:root` + global `body { color: var(--text-body) }` of the typography snippet. `scheme-1.foreground` is `#000000cf` (Horizon default), so body copy renders #2B2730 via the snippet override, not the scheme. Applied globally because the snippet renders in `theme.liquid`. |

**Token wiring summary:** `#6B3FA0` and `#2B2730` do **not** appear anywhere in `settings_data.json` (verified count = 0). They live entirely in the `senseless-typography.liquid` `:root` block + per-section `--ss-purple`. Canvas (`#f7f7f5`) is the only one of the three genuinely wired into scheme-1.

## Phase 1 — Global navigation

| Item | Status | Notes |
|---|---|---|
| Header | ✅ Renders | `sections/senseless-header.liquid`, wired into `sections/header-group.json` (`header_section → senseless-header`); rendered via `{% sections 'header-group' %}` in `theme.liquid`. Sticky + frosted, centred nav, wordmark. |
| Mega menu | ✅ Built | "Shop" mega panel (By format / By procedure) + dropdowns; `mega_cta_label/url` settings present. Menu **content** is data-driven from Shopify linklists (`linklists[section.settings.menu]`) — **placeholder/empty until menus created in admin (Stage C)**, as the brief anticipated. |
| Mobile drawer | ✅ Built | Hamburger (`data-ss-burger`, `icon-menu.svg`) → off-canvas accordion drawer (`.ss-hdr__drawer`, `data-open`), close button, drawer footer links. |
| Footer | ✅ Renders | Via `footer-group.json` → stock Horizon `footer` + `footer-utilities`, styled by `snippets/senseless-header-footer.liquid`. **Note: no bespoke `senseless-footer` section** — it's the styled Horizon footer. Flag if a custom footer section was expected. |

## Phase 2 — Trust bar

| Item | Status | Notes |
|---|---|---|
| Trust bar section | ✅ Built | `sections/senseless-trust-bar.liquid`; included on homepage (`index.json` `trust` → `senseless-trust-bar`). Single row desktop / 2×2 mobile. |
| "CPSR assessed" signal | ✅ Present | Present in the preset default blocks. |
| **4 signals** | ⚠️ **Gap** | Preset ships **3** trust_item blocks: "UK formulated", "CPSR assessed", "Made for aesthetics". Brief requires **4**. Needs a 4th signal added to the preset (e.g. "Cruelty-free" / "Vegan-friendly" / "Made in the UK" — copy TBD, compliance-check required). |

## Globals

| Item | Status | Notes |
|---|---|---|
| Cart drawer | ✅ Renders | `settings_data.json` `cart_type: "drawer"`, `drawer_drop_shadow: true`; `assets/cart-drawer.js` + cart snippets present. |
| 404 | ✅ Renders | `templates/404.json` → `main-404` (+ a `product-list`). |
| Search | ✅ Renders | `templates/search.json` → `search-header` + `search-results`; predictive `search-modal` mounted globally in `theme.liquid`. |
| Homepage | ✅ Renders | `index.json`: hero (`senseless-hero-brand-led`) → trust-bar → section-statement → trio-card-row → decision-band → format-row → pull-quote → newsletter. All senseless sections. No injectable routing in committed homepage content. |

## Injectable-clean audit — ⚠️ **NOT clean (needs your decision)**

The brief's criterion is "**no Botox/fillers/injection routing**." The repo as built does **not** meet a literal reading of this — there is substantial Botox/filler/injection content and routing committed:

- **Collection templates (3):** `collection.numbing-cream-for-botox.json`, `collection.numbing-cream-for-injections.json`, `collection.numbing-cream-for-lip-fillers.json`.
- **Active CTA routing:** `page.best-numbing-cream.json` and `page.best-emla-alternative-uk.json` link cards to `/collections/numbing-cream-for-botox` and `/collections/numbing-cream-for-lip-fillers`; FAQ entries on "best numbing cream for injections".
- **Body copy / section defaults:** Botox + lip-filler references throughout guide pages (`does-numbing-cream-work`, `how-long-*`, `choosing-your-strength`, `about`, `senseless-vs-ametop`) and as default labels in `senseless-procedure-grid`, `senseless-trio-card-row`, `senseless-strength-matrix`, `senseless-complete-prep`.

**Interpretation gap:** These read as "**numbing cream _for_ [procedure]**" use-case/SEO pages (customer prepping for a procedure done elsewhere), not the brand offering injectables as a service. Whether that satisfies "injectable-clean" is a **brand/compliance decision I won't make silently** (Hard Rule 6 + Rule 8). Nothing routes at the storefront yet because (a) menus aren't built and (b) the backing collections don't exist until Stage C — but the templates and copy are committed now. **See Open Question 1.** No changes made this stage.

---

## Gaps → Stage B build tasks

1. **Trust bar: add a 4th signal** to the preset (copy TBD → run `compliance-check`).
2. **Weight 500 (montserrat_n5):** decide — either wire an `n5` font role / emit a 500 `font_face`, or accept 400/600/700 and treat the stock-CSS 500 references as fallback. (Brief lists 400/500/600/700.)
3. **Injectable-clean decision (Open Q1)** — confirm whether the "numbing-cream-for-botox/-injections/-lip-fillers" templates + CTAs stay, get reframed, or get removed. Blocks Stage C collection creation either way.
4. **Brand purple vs scheme-1 (Open Q2)** — confirm intended: native Horizon buttons render **black** (scheme-1 primary), purple is accent-only. If primary buttons should be purple, scheme-1 needs editing.
5. **(Optional) Footer** — confirm the styled Horizon footer is acceptable vs a bespoke `senseless-footer` section.

## Open questions

1. **Injectable-clean:** Do the Botox/filler/injection use-case templates + routing satisfy "injectable-clean", or should they be reframed/removed? (Compliance-sensitive.)
2. **Token model:** Is brand purple intentionally accent-only (buttons stay black), or should `#6B3FA0` be wired into scheme-1 as the primary/button colour? The brief said "wired to scheme-1"; reality is `:root`/per-section vars + black scheme-1 buttons.
3. **Storefront password** — provide it (or use admin preview) so rendered/visual + live-DOM Google-Fonts verification can be completed.

## Not done (by design)

- No publish (Horizon stays live).
- No products, collections, menus, or content (Stages C/D).

---

# Stage B — Fixes applied (2026-06-01 ~17:10 BST, MacBook Pro)

Redeployed to **Senseless Dev `#199324434780` (unpublished)** — Horizon `#199321977180` still **[live]**. `shopify theme check` → **0 errors** (368 files, 24 pre-existing Horizon warnings). Shop confirmed `senseless-numbing` before push.

| # | Fix | Status | Detail |
|---|---|---|---|
| 1 | Self-host Montserrat **500** (n5) | ✅ Done | `snippets/senseless-typography.liquid`: emits `settings.type_body_font \| font_modify: 'weight','500' \| font_face: font_display:'swap'` inside the global `{% style %}`. Four weights now self-hosted from the Shopify font CDN: **400 / 500 / 600 / 700**. Still **0 Google Fonts**. |
| 2 | Brand purple → **scheme-1** buttons | ✅ Done | `config/settings_data.json` scheme-1: `primary`, `primary_button_background`, `primary_button_border` → `#6B3FA0`; `primary_hover`, `primary_button_hover_background/border` → `#5A3489` (canonical darkened purple, matches header `--ss-purple-hover`). Secondary button text/border also → `#6B3FA0`. **Canvas kept `#f7f7f5`.** Primary CTAs now render purple, not black. |
| 3 | Trust bar → **4 signals** | ✅ Done | Locked set **UK formulated · Cosmetic product · CPSR assessed · Made for aesthetics** (per DECISIONS-LOG 2026-05-29 + SECTIONS.md). Only `index.json` (homepage) + the section preset were short at 3 — added "Cosmetic product" as the 2nd signal in both. The other 14 template instances already carried the 4-set (verified). |
| 4 | Bespoke **senseless-footer** | ✅ Done | New `sections/senseless-footer.liquid` replaces Horizon `footer` + `footer-utilities` (`sections/footer-group.json` rewired). Dense, large inlined wordmark; 4 columns + legal band. `shopify theme check` clean; passed Shopify's stricter server-side schema validation after two fixes (see Notes). |

### The 4 trust labels used
**UK formulated · Cosmetic product · CPSR assessed · Made for aesthetics** (in that order).

### Footer — columns + placeholders
- **Wordmark:** inlined `assets/senseless-logo-header.svg` (`inline_asset_content`), height setting (default 64px), `currentColor` fill.
- **Band:** **ink** (`#1A1816`) default — mirrors prior scheme-5 dark footer; not a purple fill (respects "purple = accent only"). Editor options: ink / canvas / surface.
- **Column 1 — Shop** → menu `senseless-footer-shop`. Placeholder fallback: All numbing cream · Numbing cream · Numbing gel · Numbing spray.
- **Column 2 — The system** → menu `senseless-footer-explore`. Placeholder: Choosing your strength · Choosing your format · How it works · Does numbing cream work?
- **Column 3 — Brand** → menu `senseless-footer-company`. Placeholder: About · Trade enquiries · Contact · FAQ.
- **Column 4 — Newsletter** → native `{% form 'customer' %}` email signup (purple Join button) + blurb + optional small print.
- **Legal band:** `© {year} Senseless` · "A **Matrix Health Group Ltd** brand" (→ matrixhealthgroup.co.uk) · `shop.policies` links (placeholders: Privacy / Terms / Refund / Shipping while unset) · social (Instagram / TikTok / Facebook, placeholders while unset).
- **Injectable-clean:** ✅ no Botox/filler/injection links anywhere in the footer (placeholders included).

### Placeholder links flagged for **Stage D** wiring
1. `senseless-footer-shop` / `senseless-footer-explore` / `senseless-footer-company` menus — create in admin; columns auto-populate (Liquid falls back to these handles when the link_list settings are unset). **Must be kept injectable-clean.**
2. Store **policies** (Privacy / Terms / Refund / Shipping) — set in admin; legal band auto-swaps placeholders for real `shop.policies` links.
3. **Social URLs** (Instagram / TikTok / Facebook) — set in the section settings.

### Notes / gotchas
- Shopify's **server-side** schema validation (on push) is stricter than local `shopify theme check`, which passed all three rounds. Two push-time schema errors were fixed: (a) a `url` setting can't carry a plain-URL `default` (removed `mhg_url` default — Liquid `| default:` covers it); (b) a `link_list` setting only accepts `main-menu`/`footer` as a `default` (removed the custom-handle defaults; Liquid falls back to the `senseless-footer-*` handles instead).

### Docs updated (Hard Rule 5 + 9)
- `docs/SECTIONS.md` — added `senseless-footer.liquid` row; corrected the "footer uses Horizon native" notes; narrowed `senseless-header-footer` snippet scope to header-only; added Stage-D injectable-clean caveat.
- `docs/ARCHITECTURE.md` — footer section rewritten to the bespoke 4-column + in-section legal band model.
- `docs/BRAND.md` — added `--brand-primary-hover #5A3489`; updated "purple accent only" note (primary CTAs now purple); documented self-hosted weight 500 / n5.
- `DECISIONS-LOG.md` — new 2026-06-01 17:10 BST entry covering all four fixes.

### Still open (carried from audit — NOT addressed here, by scope)
- **Injectable-clean decision (Open Q1)** — the Botox/filler/injection *collection templates + page CTAs* still exist (unlinked; under review per DECISIONS-LOG 2026-05-31). The footer itself is clean; the broader decision is still yours and blocks Stage C.
- **Storefront password** — still needed for rendered/visual + live-DOM verification (preview 302 → /password).
- **Footer band** — confirm **ink** vs canvas/surface.
