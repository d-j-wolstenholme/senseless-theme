# Phase 6 — Hub treatment-list cleanup + comfort-mode retire + dropdown background fix

**Date:** 2026-06-03 (BST) · **Branch:** dev · **Theme:** Senseless Dev `#199324434780` (store `senseless-numbing`)
Token refreshed (`./scripts/refresh-token.sh` → shpca_f699f5…). Build source: spec `37358bc375ea81df995afcf813dd03bb` — "HUB CLEANUP" (folds in the dropdown-background fix).

## 1. Hub `/pages/does-it-hurt` → clean treatment card list
Replaced the static comfort-comparison band with a **card list, one card per treatment** (8 cards, each a `senseless-link-row` item: label + one-line descriptor + link):
- Microneedling → `/pages/does-microneedling-hurt`
- Laser hair removal → `/pages/does-laser-hair-removal-hurt`
- Lip filler → `/pages/does-it-hurt-by-treatment#lip-filler`
- Botox → `…#botox` · Microblading → `…#microblading` · Lip blush → `…#lip-blush` · Waxing → `…#waxing` · Electrolysis → `…#electrolysis`

Hub order is now `hero → intro → cards → selectorlink → route → schema` (comfort band removed). Descriptors are short, drawn from the existing compliant page copy.

**Deep-link anchors:** added an optional `anchor_id` setting to `senseless-rich-text` (renders an `id` on the section) and set it on the by-treatment page's 6 sections (`lip-filler`, `botox`, `microblading`, `lip-blush`, `waxing`, `electrolysis`) so the cards deep-link to the right section. The by-treatment route-forward link was repointed off the now-gone `#comfort` anchor → `/pages/does-it-hurt`.

## 2. Comfort comparison — retired the static hub mode
The `senseless-comfort-compare` section's `mode: hub` (the static 8-row ranked band that caused the repetition) is **fully retired**: removed the hub markup branch, the hub-only CSS, and the `hub` schema option. The section now ships **only** the two per-page toggle modes (`microneedling`, `laser`) and lives **only** on the two deep pages at §2. No template uses `mode: hub` anymore (already removed from aesthetic-procedures last pass; now from the hub). Only retirement comments reference it.

## 3. Header dropdown panels — solid background + z-index
The dropdown panels rendered transparent because `.ss-hdr__panels` had **no z-index** (page content with stacking contexts painted over the 0.98-alpha panel). Fix (scoped to the header, no global fixed/sticky — per the ARCHITECTURE standard):
- `.ss-hdr__panel` background `rgba(255,255,255,0.98)` → **`#ffffff`** (fully solid); removed the now-pointless `backdrop-filter`; kept the existing `box-shadow` + `border-bottom` (shadow nudged to 0.12 for definition).
- `.ss-hdr__panels` → **`z-index: 99`** (under the sticky bar's 100, above all page content). Applies to **all** dropdowns (Shop, The System, Help) — they share `.ss-hdr__panel`. Mobile drawer (`.ss-hdr__drawer`, separate) unaffected.

## Verify
- **theme-check: 0 errors** (24 pre-existing Horizon warnings only; none on changed files).
- **Asset-API diff:** hub order `[hero, intro, cards, selectorlink, route, schema]` + 8 cards; comfort-compare has no functional hub remnants (only retirement comments); header panel `background: #ffffff` + panels `z-index: 99`.
- **Render-verify (Playwright, live preview):**
  - Hub: **no `.ss-cmp` / `#comfort`**; **all 8 treatment cards** present and pointing to the correct URLs.
  - Deep-links: all 6 `#anchor` ids exist on the by-treatment page; navigating to `…#lip-filler/#botox/#waxing/#electrolysis` **scrolls to the section** (top ≈ -12px, just under the sticky header).
  - Deep pages (microneedling, laser): the **toggle interactive stays inline at §2** (3 band segments, `position:static`).
  - **Static ranked band gone sitewide** (no `.ss-cmp__rows` anywhere).
  - **Dropdown panels:** all three (Shop, The System, Help) computed `background-color: rgb(255, 255, 255)` (opaque, no bleed-through); `.ss-hdr__panels` z-index 99. Desktop + mobile (drawer separate, unaffected).

## Compliance
0 banned words; card descriptors are reduce-not-eliminate and drawn from existing on-page copy; no efficacy/duration/onset/%; no tattoo.

## Files
- Edited: `sections/senseless-rich-text.liquid` (+anchor_id), `sections/senseless-comfort-compare.liquid` (hub mode retired), `sections/senseless-header.liquid` (panel bg + z-index), `templates/page.does-it-hurt.json` (card list, comforthub removed), `templates/page.does-it-hurt-by-treatment.json` (6 deep-link anchors + route link).

## HOLD
Hub card list live, comfort-hub mode retired, dropdown panels solid — all verified live, desktop + mobile.
