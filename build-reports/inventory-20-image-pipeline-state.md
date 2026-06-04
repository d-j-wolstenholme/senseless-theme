# Inventory → 20 on every variant + image-pipeline state

**Date:** 2026-06-04 (BST) · **Branch:** dev · **Store:** `senseless-numbing` · Token refreshed.
Admin-only change (TASK 1) + read-only audit (TASK 2). **No theme files touched.**

## TASK 1 — Inventory set to 20 (all 15 variants)
10 products / **15 variants** (5 single-size + 5 two-size). All were already `tracked=true`, policy DENY, sitting at 0/0 on the single stock location (`gid://shopify/Location/118501376348`) — so no tracking change was needed; just set the quantity.

- Set **on-hand = 20** for all 15 inventory items in one `inventorySetQuantities` call (name `on_hand`, reason `correction`, `ignoreCompareQuantity: true`). 30 changes applied (on_hand + derived available), 0 userErrors.
- Token scope was sufficient (`write_inventory` available). Note: `read_locations` is **denied** (couldn't read location names), but the location id came from the variants' existing inventory levels, so it wasn't needed.

**Verify (Admin GraphQL):** 15/15 variants report `inventoryQuantity = 20` and `availableForSale = true`:
Clinical Cream 10g/30g · Advanced Cream 10g/30g · Professional Cream 30g · Clinical Gel 15ml/35ml · Advanced Gel 15ml/35ml · Professional Gel 15ml/35ml · Clinical Spray 100ml · Advanced Spray 100ml · Professional Spray 100ml · Foaming Cleanser 150ml.

**Verify (storefront render, Playwright):**
- PDP (`/products/clinical-strength-cream`): add-to-cart label = **"Add to cart"** (not "Sold out").
- Shop All grid: **10× "Add to cart"**, **0× "Sold out"**.

The sitewide "Sold out" state is cleared; quick-add and live add-to-cart now work (and the shipping banner's live progress can now be exercised with real cart items).

## TASK 2 — Image-pipeline state (report only, nothing built/changed)
| Item | State |
|---|---|
| `scripts/image-pipeline.mjs` | ✅ Present (254 lines) |
| Sharp installed | ⚠️ **NOT installed** — declared in `package.json` (`"sharp": "^0.33.5"`) but no `node_modules/sharp`. Needs `npm install` before the pipeline can run. |
| `image-manifest.json` | ✅ Present, initialised skeleton (`version 1.0.0`, created 2026-05-27, `images: []`) |
| `assets/images/inbox` | ✅ Exists |
| `assets/images/processed` | ✅ Exists |
| `image-process` skill | ✅ Present (`.claude/skills/image-process/SKILL.md`) |
| `package.json` | ✅ Present |

**Summary:** the documented Sharp pipeline is fully scaffolded — script, manifest, inbox/processed folders, and skill all in place — with **one gap: dependencies aren't installed** (`npm install` / `npm i sharp` needed). The manifest is empty (no images processed yet). No build performed, per brief.

## Flags
- ⚠️ **Sharp not installed** — run `npm install` in the repo root before first pipeline use.
- (Carried) Free-shipping rules still need Admin confirmation (token lacks read_discounts/read_shipping); now that stock is live, the £40/£80 banner + shipping page can be checked end-to-end with a real cart.

## HOLD
All 15 variants at qty 20 + available; storefront shows add-to-cart everywhere; image-pipeline checklist reported (Sharp install is the only gap).
