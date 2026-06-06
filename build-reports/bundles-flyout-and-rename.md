# Bundles column → flyout + bundle title rename

**Date:** 2026-06-06 (BST) · **Branch:** dev · **Theme:** Senseless Dev `#199324434780`. Token refreshed. Two briefs handled back-to-back (they interlock — the rename supplies the names the flyout already references by handle).

---

## Brief A — Bundles column → flyout (header revise from `8027da2`) · Commit `ae09f33`
Only the Bundles column of the Shop mega changed. By Product, By Strength, By Procedure, The System, featured card, Shop-all CTA, injectable-clean, accessibility — all unchanged.

- Flat 5-item list replaced with a **flyout** using the same interaction as By Product / By Strength (desktop **hover + keyboard-focus**, mobile **tap accordion**, `aria-expanded`; tier triggers are `<button>`, **non-navigating**):
  - **Clinical** (trigger) → Starter `/products/clinical-numbing-kit-small` · Ultimate `/products/clinical-numbing-kit-large`
  - **Advanced** (trigger) → Starter `/products/advanced-numbing-kit-small` · Ultimate `/products/advanced-numbing-kit-large`
  - **Professional** → flat **direct link** `/products/professional-numbing-kit-large` (no Starter ⇒ no flyout; behaves like Foaming Cleanser in By Product).
- Flyout labels are **size only** ("Starter" / "Ultimate", Starter first) — the tier is the header, not repeated. Linked **by handle** (rename-proof). "Shop all bundles →" → `/collections/bundles` kept at foot.

**Verify (desktop + mobile):** 3 top items — Clinical `<button>` (no href), Advanced `<button>` (no href), Professional flat link ✓. Clinical/Advanced open on **hover + keyboard-focus + tap**; each reveals Starter + Ultimate → the correct 2 product pages (all **200**) ✓. Professional direct link → `professional-numbing-kit-large` (**200**) ✓. "Shop all bundles" → `/collections/bundles` (**200**) ✓. Injectable grep **0** (source + rendered DOM); **theme-check 0 errors** (52 warnings, standing baseline).

**Files:** `sections/senseless-header.liquid` (desktop + drawer Bundles markup, `bundle_tiers` data).

---

## Brief B — Rename the 5 bundle product titles (Admin API, title only)
`productUpdate` on the title only, matched by SKU; handles, price, compareAtPrice, metafields, template all untouched.

| SKU | Handle (unchanged) | Old title | New title | Price / compareAt / saving (intact) |
|---|---|---|---|---|
| SBUN-CL-S | clinical-numbing-kit-small | Clinical Numbing Kit — Small | **Clinical Starter** | £75.96 / £79.96 / £4.00 |
| SBUN-CL-L | clinical-numbing-kit-large | Clinical Numbing Kit — Large | **Clinical Ultimate** | £113.96 / £119.96 / £6.00 |
| SBUN-AD-S | advanced-numbing-kit-small | Advanced Numbing Kit — Small | **Advanced Starter** | £90.21 / £94.96 / £4.75 |
| SBUN-AD-L | advanced-numbing-kit-large | Advanced Numbing Kit — Large | **Advanced Ultimate** | £128.21 / £134.96 / £6.75 |
| SBUN-PR-L | professional-numbing-kit-large | Professional Numbing Kit — Large | **Professional Ultimate** | £143.41 / £150.96 / £7.55 |

**Verify:** all 5 titles updated, **handles unchanged**, price/compareAt/saving intact, all ACTIVE. `/collections/bundles` shows the new names; the Shop-mega featured card now reads **"Professional Ultimate"** (it pulls title dynamically from the product — confirms the dynamic wiring from the prior brief). Header bundle links unaffected (linked by handle).

**API:** Admin GraphQL `productUpdate` (title only) ×5. No theme files changed for this brief.

---

## Note on naming
The bundle large SKUs are titled **"Ultimate"** as products, while the Shop-mega **featured card eyebrow/copy** and earlier reports referred to the large kit as "Complete". The flyout/menu uses size labels "Starter"/"Ultimate" per Brief A and the product titles are now "…Ultimate" per Brief B — consistent. (The featured card's editable text/eyebrow settings are unchanged; only its dynamic title now reads "Professional Ultimate".)

## HOLD
Bundles flyout live + verified; 5 bundle titles renamed + verified.
