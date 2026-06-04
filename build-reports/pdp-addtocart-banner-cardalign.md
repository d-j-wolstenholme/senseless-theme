# PDP add-to-cart redirect + banner real-time + card alignment

**Date:** 2026-06-04 (BST) · **Branch:** dev · **Theme:** Senseless Dev `#199324434780` · **Commit:** `9512cf3`. Token refreshed.

## BUG 1 — PDP add-to-cart redirected to /cart (FIXED)
**Root cause:** the product-hero add-to-cart was a bare `{% form 'product' %}` → native full-page POST to `/cart/add` → Shopify 302-redirects to `/cart`. It was NOT using the AJAX path the collection quick-add uses.
**Fix:** wrapped the PDP form in Horizon's `<product-form-component>` with the exact structure the working quick-add uses — `liveRegion` ref, `ref="variantId"` on the id input, `data-type: 'add-to-cart-form'`, `on:submit="/handleSubmit"`. `product-form.js` is loaded globally (scripts.liquid), so the component is defined on the PDP. Now AJAX-adds, increments the cart-count bubble, and **stays on the product page**.
**Verified live:** clicked Add to cart on `/products/clinical-strength-cream` → `stayedOnPDP=true` (no `/cart` navigation), `cartCount=1`.

## BUG 2 — Banner didn't update in real time (FIXED)
**Root cause (three compounding):** (1) no `pageshow`/bfcache re-sync (Horizon's own cart-icon uses `pageshow` for exactly this); (2) wrong event name — banner listened for `cart:updated`, but Horizon dispatches **`cart:update`** (CartAddEvent → `cart:update`); (3) `/cart.js` fetched without cache-busting, so a cached empty-cart response kept it stuck on the empty line.
**Fix:** banner now re-queries its elements each render (survives header morph), fetches `/cart.js` with `cache:'no-store'` + one retry, runs on first parse + DOMContentLoaded + `pageshow`, and subscribes to `cart:update` (plus legacy `cart:updated`/`cart:refresh`/`cart:change`) — so it updates instantly on every add/remove. Kept the fetch-wrap on `/cart/{add,change,update,clear}`.
**Verified live:** empty cart → banner EMPTY; PDP add (£19.99) → banner flipped to PROGRESS **without reload**: *"You're £20.01 away from free standard delivery"* (correct £X). Both PDP add and quick-add fire `cart:update`, so both update the banner.

## BUG 3 — Card action row didn't bottom-align (FIXED)
**Root cause:** `.ss-cg__buy { margin-top:auto }` was nested inside `<product-form-component> > <form>`, both block-level/content-sized, so the auto-margin had no free space — cards without a size-chip row (Professional) floated their qty+Add-to-cart up.
**Fix:** extended the flex column through the component and form (`[data-cg-form]` and its `> form` → `display:flex; flex-direction:column; flex:1 1 auto`), so `.ss-cg__buy` bottom-aligns to the card.
**Verified live:** every row `aligned=true` on numbing-cream and shop-all, desktop (1366) + mobile (390), including mixed opt/no-opt rows. Professional 2px #6B3FA0 border + quick-add intact.

## Verify
- **theme-check: 0 errors.** **Asset-API diff:** all 3 files MATCH remote.
- Live interaction (Playwright): BUG1 stayedOnPDP + cartCount=1; BUG2 EMPTY→PROGRESS with correct message; BUG3 rows aligned desktop+mobile.

## Flag / recommendation
- **Cart drawer auto-open is OFF** (`settings.auto_open_cart_drawer` default false; the live `settings_data.json` is an auto-generated JSONC blob the theme editor may overwrite, so I did not hand-edit it). The PDP now **matches the quick-add exactly** — both AJAX-add and update the cart-count bubble (the in-place confirmation), neither auto-opens the drawer. To make every add open the cart drawer, enable **Settings → Cart → "Auto-open cart drawer"** (one toggle; applies to PDP + quick-add consistently). Recommend enabling it for the stronger UX.
- Note: storefront `.js` cart endpoints were intermittently rate-limited (429 / Cloudflare challenge) during testing from repeated automated runs — this is a test-harness artifact, not a production issue; real users are unaffected.

## Files
- Edited: `snippets/senseless-shipping-banner.liquid`, `sections/senseless-product-hero.liquid`, `sections/senseless-collection-grid.liquid`.

## HOLD
All three bugs fixed and verified live. Awaiting Daniel on whether to enable the auto-open cart drawer toggle.
