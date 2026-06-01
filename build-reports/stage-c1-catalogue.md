# Stage C / Step 1 — Catalogue (senseless-numbing)

**Date:** 2026-06-01 (BST)
**Machine:** MacBook Pro
**Branch:** dev
**Store:** senseless-numbing.myshopify.com (confirmed via `{ shop }` before any mutation; token refreshed for a fresh 24h window)
**Scope:** Create the full catalogue — 10 products / 15 SKUs — ACTIVE + published to Online Store, inventory tracked @ 0, no oversell. **No collections (Step 2). No product-page content (Stage D).**

> Source of truth: Notion "Senseless — Pricing & SKU map (RRP)" reconciled matrix (the page's stale bottom table + gel-conflict sections ignored; old-store GIDs moot). Store was empty (0 products) at start — clean create, no reconcile.

---

## Result — ✅ all checks pass

- **10 products / 15 variants** exist; handles match exactly (size-agnostic).
- Every variant priced per matrix; every product has a **Size** option with a real value (no "Default Title").
- productTypes exact: **Cream / Gel / Spray / Cleanser**.
- Strength tag on every numbing product; **Foaming Cleanser = Cleanser, no tags, no "numbing" anywhere** (handle/title/type/tags).
- All **ACTIVE** + **published to Online Store** (`gid://shopify/Publication/354304655708`).
- Inventory **tracked**, **qty 0**, policy **DENY** (no oversell) on all 15.
- `body_html` empty on all 10 (content comes from theme sections in Stage D).
- **Not** added to any collection (Step 2); format smart-collections will auto-join by productType later.

### Method
`productSet` (synchronous) per product → `publishablePublish` to Online Store. Verified by an independent `products` query (not the create response): counts, handles, prices, SKUs, option values, productType, tags, status, `publishedOnPublication`, `inventoryItem.tracked`, `inventoryPolicy`, `inventoryQuantity`, `descriptionHtml`.

---

## Catalogue — GIDs / SKUs / prices / type / publish

| # | Handle | Product GID | productType | Tag | Status | Online Store |
|---|---|---|---|---|---|---|
| 1 | clinical-strength-cream | gid://shopify/Product/15610197246300 | Cream | Clinical | ACTIVE | ✅ |
| 2 | advanced-strength-cream | gid://shopify/Product/15610197344604 | Cream | Advanced | ACTIVE | ✅ |
| 3 | professional-strength-cream | gid://shopify/Product/15610197410140 | Cream | Professional | ACTIVE | ✅ |
| 4 | clinical-strength-gel | gid://shopify/Product/15610197475676 | Gel | Clinical | ACTIVE | ✅ |
| 5 | advanced-strength-gel | gid://shopify/Product/15610197541212 | Gel | Advanced | ACTIVE | ✅ |
| 6 | professional-strength-gel | gid://shopify/Product/15610197737820 | Gel | Professional | ACTIVE | ✅ |
| 7 | clinical-strength-spray | gid://shopify/Product/15610197868892 | Spray | Clinical | ACTIVE | ✅ |
| 8 | advanced-strength-spray | gid://shopify/Product/15610197967196 | Spray | Advanced | ACTIVE | ✅ |
| 9 | professional-strength-spray | gid://shopify/Product/15610198032732 | Spray | Professional | ACTIVE | ✅ |
| 10 | foaming-cleanser | gid://shopify/Product/15610198098268 | Cleanser | — (none) | ACTIVE | ✅ |

### Variants (Size · SKU · price · GID · tracked · policy · qty)

**1. clinical-strength-cream**
- 10g · S10CL · £19.99 · gid://shopify/ProductVariant/57777075224924 · tracked · DENY · 0
- 30g · S30CL · £44.99 · gid://shopify/ProductVariant/57777075257692 · tracked · DENY · 0

**2. advanced-strength-cream**
- 10g · S10AD · £24.99 · gid://shopify/ProductVariant/57777075519836 · tracked · DENY · 0
- 30g · S30AD · £49.99 · gid://shopify/ProductVariant/57777075552604 · tracked · DENY · 0

**3. professional-strength-cream**
- 30g · S30PR · £55.99 · gid://shopify/ProductVariant/57777076404572 · tracked · DENY · 0

**4. clinical-strength-gel**
- 15ml · SG15CL · £19.99 · gid://shopify/ProductVariant/57777076535644 · tracked · DENY · 0
- 35ml · SG35CL · £34.99 · gid://shopify/ProductVariant/57777076568412 · tracked · DENY · 0

**5. advanced-strength-gel**
- 15ml · SG15AD · £24.99 · gid://shopify/ProductVariant/57777076928860 · tracked · DENY · 0
- 35ml · SG35AD · £39.99 · gid://shopify/ProductVariant/57777076961628 · tracked · DENY · 0

**6. professional-strength-gel**
- 15ml · SG15PR · £29.99 · gid://shopify/ProductVariant/57777078239580 · tracked · DENY · 0
- 35ml · SG35PR · £44.99 · gid://shopify/ProductVariant/57777078272348 · tracked · DENY · 0

**7. clinical-strength-spray**
- 100ml · SSPCL · £19.99 · gid://shopify/ProductVariant/57777079746908 · tracked · DENY · 0

**8. advanced-strength-spray**
- 100ml · SSPAD · £24.99 · gid://shopify/ProductVariant/57777080205660 · tracked · DENY · 0

**9. professional-strength-spray**
- 100ml · SSPPR · £29.99 · gid://shopify/ProductVariant/57777080729948 · tracked · DENY · 0

**10. foaming-cleanser** (no strength tag; never numbing)
- 150ml · FOAM · £19.99 · gid://shopify/ProductVariant/57777080992092 · tracked · DENY · 0

---

## Notes / scopes
- `read_locations` scope is **not granted** — irrelevant here (inventory left at 0, no location-level quantity writes). If Stage launch-gate needs to set stock per location via API, that scope (or admin) will be needed.
- `metaobject_definitions` scope still missing (flagged Stage A) — not needed for this step.

## Not done (by design)
- No collection membership (Step 2 — procedure / Shop-All; format smart-collections auto-join by productType).
- No product-page content / images (Stage D).
- Stock stays 0 until the launch gate.

## Next
- **Await confirmation** before Step 2 (collections).
