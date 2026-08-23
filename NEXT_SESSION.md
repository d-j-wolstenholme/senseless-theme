# NEXT_SESSION — handoff

**Last session (23 Aug 2026, MacBook Pro):** launched the **Merchandise** line —
new collection + the Senseless Cosmetics Bag — and wired it into the promotion
surfaces. Shipped and live.

## Done

- **Product `senseless-cosmetics-bag`** — SKU `SENBAG`, £9.99, single variant,
  **150 units at UK Dispatch**, ACTIVE, published to Online Store. New
  `product_type` = **Merchandise**. Own template, own SEO.
- **Collection `merchandise`** — smart collection, rule `type = Merchandise`,
  published, own template, SEO set. `/collections/merchandise` is live.
- **The new product type had a blast radius and it bit immediately.**
  `aesthetic-numbing-cream` is a smart collection whose ONLY rule was
  `type != Cleanser`, so the bag auto-joined a *numbing cream* collection the
  moment it was created. Caught by querying the product's collections straight
  after creation rather than assuming. Fixed with `type != Merchandise`; the bag
  now sits in `shop-all` + `merchandise` only.
- **Image** through `scripts/image-pipeline.mjs`: 1254×1254 PNG 1.27MB → WebP
  **45.6KB** (ceiling 300KB), alt set, manifest logged.
  CDN: `https://cdn.shopify.com/s/files/1/1028/2565/6668/files/senseless-cosmetics-bag.webp?v=1787476407`
- **Promotion surfaces** (Daniel chose each one):
  1. **5th mega-menu column "Merchandise"** desktop + matching drawer accordion
     group on mobile. Professional Complete **keeps** the featured card. The Shop
     panel now uses `.ss-hdr__panelinner--wide` (1280px, the header bar's own
     width) so the existing four columns aren't squeezed by the new one.
  2. **Cart drawer now carries TWO offers** (ointment + bag). This deliberately
     supersedes the "ONE suggested add" rule for that pair. Laid out
     `repeat(auto-fit, minmax(240px,1fr))` — side by side on the cart page and
     wide viewports, **stacked** in the ~380px drawer where two-across is
     unusable.
  3. **New cross-sell row on `product.bundle.json`** — covers all 5 kits; it had
     no cross-sell row, so nothing was diluted.
  4. **Bag as a 4th card** on the two aftercare PDPs.
- **Shop All now has its own Merchandise section at the bottom** (`6666b0c`) —
  see the correction below; this was missed on the first pass.
- **Merchandise added to the footer Shop column** (found on audit — it listed
  every other category but not this one). 3 links live on every page: desktop
  mega, mobile drawer, footer.
- Commits `128ec63` (build) + `11f4ca0` + `6666b0c` (Shop All) + lock re-locks.
  Deployed via `deploy.sh --reviews-changed`; **Asset-API remote == local**.
- Written up: Decision `3c558bc3-75ea-8144-a998-cb11ae99170d` + State Surface
  sync-status and log entry.

## Open — needs Daniel

1. **The bag's MATERIAL and DIMENSIONS.** I inferred "faux leather" from the
   photograph and then **deliberately removed it** from the alt text and key
   facts — a wrong material statement on a product page is a consumer-law
   problem, not a copy nit. The key-facts block is honest but thin until these
   are supplied. Once you confirm, update the alt text, the Files asset alt, and
   the `Closure`/material key facts.
2. Everything below is unchanged from the previous handoff.

## Next

1. **Commission the 12 images.** Brief ready: `docs/IMAGE-BRIEF-tattoo-cluster.md`.
   Finals to `assets/images/inbox/`, `scripts/image-pipeline.mjs` does the rest.
2. **G2 — the only safety gate still open.** Can *"Apply to clean, unbroken skin"*
   change? Assume NO until the safety assessor rules. (**G1 is closed. Do not
   re-raise it.**)
3. **`tattoo pain chart`** — 6,900/mo at KD 1, `/pages/tattoo-pain-chart` is a
   404, and the two strategy docs contradict each other on whether it's winnable.
4. **Search Console** — still outstanding from 19 Aug: click **Validate fix** on
   each of the 3 Merchant listings issues. (The new bag PDP does *not* reopen
   them — its JSON-LD was verified to carry `description`, `shippingDetails` and
   `hasMerchantReturnPolicy`.)

## The correction that matters — a verification that lied

My first pass reported **"bag appears in Shop All: PASS"**. It did not appear.
The assertion matched the product **name** anywhere in the shop-all HTML, and the
name was there only inside the **JSON-LD `ItemList`**. Live before the fix:
`/collections/shop-all` declared **17** items in schema and rendered **16** cards.

Shop All is **not one grid** — it is six `senseless-collection-grid` sections,
each pinned to a `format` (cream/gel/spray/cleanser/bundle). None matched
`Merchandise`, so the bag fell through every one of them.

**The section's own comment already documents this exact failure** from the
Vitamin A&D case — *"shop-all, whose own JSON-LD declared 16 items while the DOM
rendered 15"* — and I reproduced it while editing that very file.

Fixed in `6666b0c`. Live now: **17 cards == 17 ItemList entries, bag last.**

> **Assert on RENDERED CARDS, never on a name appearing somewhere in the HTML.**
> JSON-LD, nav links and inline CSS all contain product names and will hand you a
> false PASS. `scratchpad/audit.py` now counts
> `<h3 class="ss-cg__title">` anchors.

## Gotchas earned this session

- **`nil == blank` is TRUE in Shopify Liquid but FALSE in python-liquid.** A guard
  written `if product != blank` therefore **cannot be exercised in the offline
  harness** — the missing-product branch never fires and the harness cheerfully
  renders a broken card while reporting success. **Write guards as plain
  truthiness** (`if p and v and v.available`): nil is falsy in both engines, so
  the guard is correct live *and* testable offline. This is what the cart-offer
  guard was rewritten to.
- **A new `product_type` is never a local change on this store.** All 19
  collections are smart collections keyed on `type` or a metafield. Read the rules
  before creating the product, and query the product's collections immediately
  after. One query, caught a real breach first time.
- **Checkout upsells are not buildable here and this should stop being asked.**
  The store is on the **Grow** plan, not Plus — no app, snippet or theme edit puts
  custom content or a pop-up on the checkout page. Only the cart drawer (ours) and
  a paid post-purchase app exist; Daniel chose to skip the paid route.
- **Verify a cart feature with an actual cart.** `curl` against `/cart` with an
  empty cart proves nothing about the offer logic. Building a real cart with
  `/cart/add.js` + a cookie jar proved both cards render *and* that each
  self-suppresses once its product is in the cart.
- **Watch your own verification regexes before believing a FAIL.** Three
  "failures" this session were all mine: the theme emits **multi-line** `<meta>`
  tags (so a single-line description regex misses it), product images serve from
  `senseless.uk/cdn/shop/files/` not `cdn.shopify.com`, and `.ss-ph__comfort`
  appears as a **CSS rule** on every product page — match the markup, not the
  class name.
