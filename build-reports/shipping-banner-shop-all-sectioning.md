# Shipping progress banner + Shop All sectioning

**Date:** 2026-06-04 (BST) · **Branch:** dev · **Theme:** Senseless Dev `#199324434780` (store `senseless-numbing`) · **Commit:** `a282fab`
Token refreshed. Build source (verbatim): 🚚 spec `37558bc375ea818b987bcad87242da2c`.

## PART A — Shipping-threshold header banner
New snippet `snippets/senseless-shipping-banner.liquid`, rendered **inside** `<header class="ss-hdr">` above `.ss-hdr__bar`, so banner + header are **one always-sticky unit** (`.ss-hdr` stays `position:sticky; top:0` — TN's stated "plain always-sticky" final state; no hide-on-scroll). Because it's in-flow sticky, page content sits naturally below it — no body top-padding hack and no risk of content hiding behind a fixed bar.

- **Header position is constant** regardless of cart; only **banner content** is cart-driven (read live via `/cart.js`, re-rendered on add/remove).
- **Empty basket (static):** "Free UK standard delivery over £40 · Free next-day over £80 · Order before 1pm for same-day dispatch".
- **Items (live 2-milestone progress, subtotal-driven, 0→£40→£80):**
  - `< £40` → "You're £X away from free standard delivery"
  - `£40–79.99` → "Free standard delivery unlocked — £X more for free next-day"
  - `£80+` → "Free next-day delivery unlocked — order before 1pm for same-day dispatch"
  - `£X` computed live from cart subtotal (`items_subtotal_price`). **Same-day-dispatch line present in all states** (persistent sub-line for the two lower tiers; in-message for £80+). **£40 midpoint** marked distinctly on the bar.
- **Live updates:** `fetch` wrapper re-pulls `/cart.js` after any `/cart/{add,change,update,clear}` request, plus `cart:updated`/`cart:refresh` listeners → works with the quick-add and the cart drawer.
- **Tokens:** #6B3FA0 fill / #f7f7f5 ground / #1A1816 text / Montserrat. **No paid-price references** (grep clean — no "normally"/"was £"/"rrp"/etc.).
- **Product hero:** static "Free UK delivery over £40" line added below the trust line (`.ss-ph__delivery`, purple, van icon) — **no live progress there** (new `delivery_line` setting, default on).

## PART B — Shop All sectioning (`/collections/shop-all`)
Flat grid split into **4 format sections** via a new `format` filter on the shared `senseless-collection-grid` (filters `collection.products` by `type`, then orders Clinical → Advanced → Professional using a `where:'id'` concat; default `all` leaves every other collection untouched). Template `collection.shop-all.json` rebuilt into 4 grids:

1. **Numbing Cream** [3] — eyebrow "By format"
2. **Numbing Gel** [3] — eyebrow "By format"
3. **Numbing Spray** [3] — eyebrow "By format"
4. **After your appointment** [1] — eyebrow "Aftercare" (Foaming Cleanser)

Within each: Clinical → Advanced → Professional. §8 quick-add card, canonical styling, Professional 2px #6B3FA0 border + filled CTA, and noindex all preserved. Professional never "flagship/strongest".

## Verify
- **theme-check: 0 errors** (26 pre-existing info/warnings, none in the new/edited files).
- **Asset-API diff:** all 5 files MATCH remote (shop-all.json semantically equal — Shopify reformats JSON whitespace; all 4 `format` settings + order confirmed present after standalone re-push).
- **Render-verify (Playwright, desktop 1366 + mobile 375):**
  - **Shop All:** robots = `noindex,nofollow`; 4 sections in order cream/gel/spray/aftercare; each Clinical→Advanced→Professional; Professional cards `pro=true` border `2px`; aftercare = single Foaming Cleanser card; quick-add controls (size chips, qty stepper, CTA) render.
  - **Banner empty state:** visible, exact static copy, progress hidden.
  - **Banner items-states (mocked `/cart.js` against the deployed JS):** £25 → "You're £15 away from free standard delivery", fill 31.25%, same-day line shown; £55.50 → "Free standard delivery unlocked — £24.50 more for free next-day", fill 69.375%, same-day shown; £90 → "Free next-day delivery unlocked — order before 1pm for same-day dispatch", fill 100%.
  - **Always-sticky:** `.ss-hdr` `position:sticky`, banner is a child of the header (desktop + mobile).
  - **No regressions:** mobile drawer opaque (`rgb(247,247,245)`, opacity 1), logo SVG present; header sticky on mobile; banner renders at all breakpoints.
  - **Product hero:** "Free UK delivery over £40" line present, purple (`rgb(107,63,160)`).

## Flags / deviations
- **⚠ Free-shipping rules NOT API-confirmable — needs Daniel.** The custom-app token is denied both `read_discounts` and `read_shipping` (deliveryProfiles) scopes, so I could not verify the actual Shopify rules. **Action:** confirm in Admin → Settings → Shipping/Discounts that **free standard delivery ≥ £40** and **free next-day ≥ £80** exist, so the banner's promise matches checkout. The banner is **display-only** and commented as such.
- **⚠ All 10 product variants are `availableForSale=false`** (no inventory set) → quick-add buttons render as "Sold out" and live add-to-cart can't be exercised yet; the items-state banner was therefore verified by mocking `/cart.js` against the live deployed JS. Once inventory is set, both quick-add and the live banner work with no further code change.
- **Eyebrow interpretation (logged):** "eyebrow headers (Shop-dropdown eyebrow style)" built as eyebrow (`.ss-cg__eyebrow`, small uppercase purple — same register as the dropdown's `.ss-hdr__col-title`) **+ format-name H2**, matching the site's standard section-head pattern. The three formats share "By format" (their dropdown group); aftercare uses "Aftercare" + headline "After your appointment" (brand-consistent, avoids duplicating the lone card title). Flag if you'd prefer eyebrow-only or the literal "Foaming Cleanser" headline.
- **Header kept plain-sticky, not pure-fixed:** the spec described "always fixed + top-padding," but TN's actual final state is "plain always-sticky," which the existing header already is. In-flow sticky meets every requirement (always visible, one unit, nothing hidden) without a body-padding hack — lower-risk. Flag if you specifically want `position:fixed`.

## Files / API
- New: `snippets/senseless-shipping-banner.liquid`.
- Edited: `sections/senseless-header.liquid` (render banner inside header), `sections/senseless-product-hero.liquid` (static delivery line + setting), `sections/senseless-collection-grid.liquid` (`format` filter + setting), `templates/collection.shop-all.json` (4 format sections).
- No API writes (theme push via Shopify CLI only).

## HOLD
Both parts built, pushed, and verified. Awaiting Daniel on the two flags (confirm free-shipping rules; set product inventory).
