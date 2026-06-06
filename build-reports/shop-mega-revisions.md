# Shop mega-menu revisions (revise header from 01a4afc)

**Date:** 2026-06-06 (BST) · **Branch:** dev · **Theme:** Senseless Dev `#199324434780` · **Commit:** `8027da2`. Token refreshed.

Three Shop-mega changes only. By Procedure, The System dropdown, Shop-all CTA, injectable-clean and accessibility are unchanged from `01a4afc`.

## 1 — By Strength: repositioned + flyout
- **New column order: By Product · By Strength · By Procedure · Bundles** (desktop + mobile drawer).
- By Strength now mirrors By Product: each strength (Clinical / Advanced / Professional) is a disclosure **trigger** — a `<button>`, **never an `<a>` (non-navigating)**. Opens on **hover + keyboard-focus** (desktop) and **tap** (mobile); `aria-expanded`, keyboard-operable, not hover-only.
- Each strength reveals its **3 formats** → size-agnostic product pages:
  - Clinical → `/products/clinical-strength-{cream,gel,spray}` (labels "Clinical Cream/Gel/Spray")
  - Advanced → `/products/advanced-strength-{cream,gel,spray}`
  - Professional → `/products/professional-strength-{cream,gel,spray}`
- No per-strength collection ⇒ no "Shop all [strength]" in the flyout.
- **"Find your strength →"** kept at the foot → `/pages/the-senseless-system` (direct 200). This supersedes the previous "all strength items → System"; only "Find your strength" now goes to the System page.

## 2 — Featured card: Professional Complete + dynamic image
- Points at **Professional Complete** (`professional-numbing-kit-large`, SKU **SBUN-PR-L**).
- Image is **pulled dynamically from the product's own featured media** (no manual section image), so real photography auto-populates. **Neutral brand placeholder fallback** while the product is imageless (it currently has none).
- Title defaults to the **product's title** ("Professional Complete" once the rename brief lands); eyebrow / title-override / text / cta / featured-product all remain editable section settings (the old `image_picker` was replaced by a `product` setting).

## 3 — Bundles: fixed order
- Rendered by **explicit handle order** in the section (not the collection's default sort, not title-dependent): **Clinical Starter · Clinical Complete · Advanced Starter · Advanced Complete · Professional Complete** = `clinical-numbing-kit-small, clinical-numbing-kit-large, advanced-numbing-kit-small, advanced-numbing-kit-large, professional-numbing-kit-large`. "Shop all bundles →" kept.

## Verify (desktop + mobile, password render)
- **Column order** = By Product · By Strength · By Procedure · Bundles ✓ (both viewports).
- **By Strength:** heads are `<button>` with `hasHref:false` (non-navigating) ✓; each reveals the correct 3 product pages (**all 200**) ✓; **hover-opens + keyboard-focus-opens + mobile tap** all true ✓; "Find your strength" → `/pages/the-senseless-system` (**200, no 301**) ✓.
- **Featured card:** title "Professional Numbing Kit — Large" (dynamic from product; becomes "Professional Complete" on rename), image = placeholder fallback (product imageless — dynamic source confirmed), CTA → `/products/professional-numbing-kit-large` ✓.
- **Bundles** render in the specified order ✓; Shop all bundles → `/collections/bundles` (200) ✓.
- **Injectable-clean grep = 0** (source + rendered header/drawer DOM); **theme-check 0 errors** (52 warnings, standing `ValidScopedCSSClass` baseline).

## Files
- Edited: `sections/senseless-header.liquid` (By Strength flyout markup desktop + drawer, column reorder, dynamic featured card, bundle handle-order, schema: `shop_feat_product` replaces `shop_feat_image`).

## Notes
- All 9 strength products + 5 bundles + System page resolve 200, no redirects.
- Featured card image will switch from the placeholder to the real shot automatically once `professional-numbing-kit-large` gets featured media (no theme edit needed) — ties into the standing photography launch gate.

## HOLD
Shop mega revisions live + verified on the dev theme.
