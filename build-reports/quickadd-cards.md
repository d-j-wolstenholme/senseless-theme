# Build Report — Quick-add on product cards (storefront-wide)

- **Machine:** MacBook Pro
- **Date:** 2026-05-31 (BST)
- **Branch:** `feature/quickadd-cards` (off `dev`) → PR into `dev`
- **Live theme:** Horizon `#195280437583` — untouched, not published. `theme check`: **0 errors**.

## Completed

- **New shared control `snippets/senseless-quick-add.liquid`** — single source of truth for card quick-add. Renders an inline variant **`<select name="id">`** (only when `product.variants_count > 1` — Senseless sizes are variants), Horizon's **quantity stepper**, and **add-to-cart** button inside a Horizon **`<product-form-component on:submit="/handleSubmit">`** → AJAX `/cart/add`, never leaves the page, opens the existing cart drawer. Reuses Horizon `product-form-component` / `add-to-cart-button` / `quantity-selector` (so behaviour matches the rest of the theme).
- **Respects inventory / £TBC:** renders **nothing** unless a real product is linked; out-of-stock variants are `disabled` options; the whole control is inert/disabled while `variant.available == false` (0 stock / £TBC) and **auto-enables once price + stock are set** — driven by live `variant.available`, nothing hardcoded. Per-variant price shown in the `<select>` where it differs.
- **Wired into every senseless surface where a PRODUCT card appears:**
  - `senseless-product-grid` (collection grids) — **added a `product` picker** to the block (cards were editorial-only) + split the card anchor.
  - `senseless-cross-sell` (product-page related + Foaming Cleanser aftercare cross-sell) — split anchor + quick-add.
  - `senseless-product-showcase` — added quick-add (item already a div, no split needed).
  - `senseless-trio-card-row` → **`product_card` block only** — split anchor + quick-add.
- **Anchor refactor:** senseless cards were wrapped entirely in `<a>` (a form/buttons can't be nested in an anchor). Each product card was restructured to `div.card > a.cardlink (image+text) + senseless-quick-add (sibling)`. Procedure/format/tier/guide **navigation cards stay plain links** (no quick-add), per the brief.
- **Horizon native cards (search results, cart-drawer upsell)** already have quick-add — `settings.quick_add` defaults to `true` in `settings_schema.json` and `quick-add-modal` renders in `theme.liquid`. **No change needed** for those surfaces.

## Validation

- `theme check`: **0 errors** (24 warnings, baseline unchanged).
- **Live add-to-cart could NOT be verified** — no products exist in admin yet (range is In Progress; £TBC / 0 stock), and cards aren't linked to products. The mechanism reuses Horizon's proven cart components, so it will function once a card is linked to a purchasable product. **Recommend a live add-to-cart + drawer test once real products exist.**

## Assumptions logged (Hard Rule #6)

1. **Cards were not product-bound.** `senseless-product-grid` cards were editorial blocks (image/label/title/price-text/`cta_url`) with no product object; the other three card sections had a `product` picker used only for the image (price still a text field, CTA link-only). I added a `product` picker to product-grid and made quick-add **conditional on a linked product** — so existing editorial/link-only cards are unchanged until an editor links a product. This is the only way add-to-cart can work; flagged for confirmation.
2. **Activation is editor-driven.** Quick-add lights up per card once (a) the card is linked to its Shopify product in the theme editor AND (b) that product has price + stock. Until products are created in admin and linked, quick-add is **dormant** (cards render exactly as before).

## Open items / still needed

1. **Link cards to products** in the theme editor once products/variants/price/stock exist in admin (per-card `product` setting). Until then quick-add is dormant by design.
2. **Per-SKU product creation** in Shopify admin is the upstream blocker (range still In Progress).
3. **Variant `<select>` is a native picker** — it posts the chosen variant on add and disables out-of-stock options, but does not live-refresh the card's price/button state on selection (no per-card variant JS). Acceptable for a card quick-add; revisit if live per-variant card state is wanted.
4. **Injectable-clean:** quick-add only appears on product cards an editor links. The Senseless range has **no injectable products** (injectables are procedures, not SKUs), so ad-facing product cards remain injectable-clean; just don't link injectable-adjacent items. Noted.
5. **Carryovers:** PR #2 (GEO/schema layer) still unmerged; `docs/ARCHITECTURE.md` re-sync still queued.

## Git / deploy

- Commit `48ae859`. PR `feature/quickadd-cards` → `dev` (not merged — awaiting review). Deployed to unpublished dev theme `#196680057167` for preview.
