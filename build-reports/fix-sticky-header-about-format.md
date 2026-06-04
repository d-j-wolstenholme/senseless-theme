# Fix sticky header + About format-count

**Date:** 2026-06-04 (BST) · **Branch:** dev · **Theme:** Senseless Dev `#199324434780` (store `senseless-numbing`) · **Commit:** `9b5f522`
Token refreshed.

## BUG — header not staying pinned (root cause found)
**Symptom:** the always-sticky header (commit `a282fab`, `.ss-hdr position:sticky; top:0` with the banner as child) scrolled away instead of staying pinned — confirmed live on shop-all desktop. The earlier report only checked the CSS property + markup nesting, which is why it passed while the behaviour failed.

**Root cause (diagnosed from the live DOM, not assumed):** `position:sticky` is bounded by the element's **containing block = its parent's content box**. Shopify renders header-group sections inside two wrappers — `<div id="header-group">` and `<div class="shopify-section shopify-section-group-header-group">` — and **both are only as tall as the header itself** (measured 113px each in-browser). So the header stayed pinned only until the page scrolled past the wrapper height (~113px), then un-stuck and scrolled away with its parent (observed: scrollY 1145 → header top −1145). No ancestor `overflow`/`transform`/`contain`/`filter` was involved — the ancestry was clean; it was purely the short-parent constraint.

**Fix:** collapse both wrappers with `display:contents` (added as a plain `<style>` in `layout/theme.liquid`, co-located with `#header-group`). This removes the wrapper boxes so `.ss-hdr` becomes a direct child of `<body>`, whose content box spans the whole page — the sticky constraint rectangle is now the full document, so the banner+header unit stays pinned at `top:0` through the entire scroll. Kept `position:sticky` (TN's plain always-sticky final state) — no need for `position:fixed`/offset.

**Why it's safe:** Horizon's inline header-height script (`setHeaderHeighCustomProperties`) queries `header-component`, which the custom `.ss-hdr` does not use, so it early-returns and never sets `--header-group-height` — collapsing `#header-group` changes nothing it relies on. The `<style>` lives in theme.liquid (not a section `{% style %}` block), so it adds no `ValidScopedCSSClass` warning.

## ABOUT format fix (`/pages/about`)
"four formats" → "three formats" everywhere (canonical = three formats: cream/gel/spray; the cleanser is aftercare). All 4 occurrences fixed: hero subhead, Section 2 body, the "three-tier, four-format" line, and the page-schema description. Grep: **zero "four format" remain**.

## Verify
- **theme-check: 0 errors** (26 pre-existing warnings, unchanged — the new `<style>` adds none).
- **Asset-API diff:** `layout/theme.liquid` MATCH (display:contents rule present on remote); `page.about.json` semantic-match.
- **Render-verify — ACTUAL SCROLL (Playwright), header top measured at 3 scroll depths per page:**
  - **Desktop (1366):** shop-all, product, homepage → header `top=0.0` PINNED at every depth (up to scrollY ~4074).
  - **Mobile (375):** shop-all, homepage → header `top=0.0` PINNED at every depth (up to scrollY ~5228).
  - **About:** "three formats" ×2 in body, "four formats" ×0 → clean.
  - **No regressions:** mobile drawer opaque (`rgb(247,247,245)`, opacity 1), logo SVG present; banner cart-driven content still updates after the fix ("You're £15 away from free standard delivery", progress visible).

## Files
- Edited: `layout/theme.liquid` (display:contents wrapper-collapse + explanatory comment), `templates/page.about.json` (four→three formats ×4).
- No API writes (theme push via Shopify CLI only).

## HOLD
Header stays pinned on every page + breakpoint (verified by scrolling, not just CSS inspection); About format count corrected. Standing flags from the prior session unchanged (free-shipping rules need Admin confirmation; product inventory unset).
