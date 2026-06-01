# Wave 3 — Ad-facing collections build · STAGE 1: Numbing Cream (HOLD checkpoint)

**Date:** 2026-06-02 (BST) · **Machine:** MacBook Pro (continued session) · **Branch:** dev
**Theme:** Senseless Dev `#199324434780` (unpublished) · **Store:** senseless-numbing.myshopify.com
**Scope:** STAGE 1 ONLY — build `/collections/numbing-cream` (head term, full 3-strength grid) + the **first build of the §8 quick-add card**. Report + **HOLD** so the card pattern is proven before it propagates to the other 6 collections (Stage 2).

## Sources read in full (before writing)
- 🟢 Canonical State §8 (quick-add card spec), §1 (range), §11 (QA gate + A–K Master Rubric) — https://www.notion.so/37258bc375ea813e895ccbe38c0cadc8
- Collections-as-primary-SEO-surface + injectable-clean bidirectional rules (Wave 3 brief)

## What was built
**New section `sections/senseless-collection-grid.liquid`** — the §8 quick-add card, self-contained markup + CSS (NOT a reuse of the shared card snippet with a modifier class — per the Totally Numb lesson). Per card:
- Image (lazy), strength label (from product tag), title, **live price** (`data-cg-price`, never £TBC).
- **Size chips** — radio + label, **active = solid purple fill** (`#6B3FA0`, `input:checked + .ss-cg__chip`); single-variant products render no selector.
- **Qty stepper** — `−` / `+` buttons driving a `<span>` display + `<input type="hidden" name="quantity">`.
- **Add-to-cart** — `<button type="submit" name="add">`, wired inside Horizon `<product-form-component on:submit="/handleSubmit">` with `<input name="id" ref="variantId">` + liveRegion (AJAX add → opens cart drawer).
- **Judge.me** per-card star slot (`data-judgeme-card`, `:empty`-hidden until the app block is added).
- **Strength filter tabs** (client-side, by product tag); **Professional card = `--flagship`** (2px purple border).

**Rebuilt `templates/collection.numbing-cream.json`** (v3 map) — order: hero → grid → why → onward → aftercare → trust → keyfacts → faq. Collection `templateSuffix="numbing-cream"` set via Admin API (without it the collection rendered the DEFAULT template — fixed). SEO title/description set via API.

## §8 quick-add card — live interaction proof (Playwright headless Chromium, against the preview theme)
A real bug was caught here and fixed before propagating the card:

- **BUG (found + fixed):** size radios carried `{% unless v.available %}disabled{% endunless %}`. With pre-launch inventory at 0, **every variant is unavailable → every size chip was disabled → the selector froze** (couldn't switch sizes or see per-size prices). Even in production a single out-of-stock size would have been unselectable. **Fix:** chips are now always selectable (`data-avail` attribute instead of `disabled`); selecting an out-of-stock size flips the **add button** to "Sold out"/disabled (correct quick-add convention). Out-of-stock sizes get a subtle strikethrough but stay clickable.
- **Verified live after the fix (real mouse clicks):**
  - Chips selectable (`disabled=false`); clicking 30g→10g switches price **£49.99 → £24.99** and the hidden variant id **…552604 → …519836**; clicking back restores £49.99.
  - Active chip fill = `rgb(107,63,160)` = **#6B3FA0** (solid purple) ✓
  - Add button correctly **"Sold out" + disabled** at 0 inventory, before and after size switch ✓
  - Qty stepper increments/decrements with a floor of 1 ✓
  - Card wired to `<product-form-component>` ✓

## §11 QA gate + A–K Master Rubric — `/collections/numbing-cream`
| # | Dimension | Result |
|---|---|---|
| **A** | Brand voice / tone | ✅ "matched to the work, not the marketing"; calm, practitioner-credible; no hype |
| **B** | Compliance (banned words / claims) | ✅ **0 banned words**; no effect-duration in hours, no onset-speed, no %, no mechanism, no active-ingredient naming. "Is this a medicine? No." present. FAQ substantive (no "practitioner is the best guide" dodge). Apply-before window (~45–60 min) present as an **instruction** (§11-permitted), not a timing claim |
| **C** | SEO — primary keyword placement | ✅ keyword in **H1** ("Numbing cream, in three strengths."), an **early H2** ("Shop numbing cream by strength."), **hero/intro body**, **image alt** ("Senseless numbing cream range"), **meta title/description**, and inbound anchors (header/footer "Numbing Cream") |
| **D** | SEO — long-tail capture | ✅ FAQ captures "which strength", "strongest numbing cream", "how long before … apply", "how long does it last", "patch test", "is this a medicine" |
| **E** | GEO / structured data | ✅ CollectionPage + ItemList + BreadcrumbList + FAQPage (6 Q&As) in JSON-LD; Key Facts block ("Not a medicine") |
| **F** | Injectable-clean (bidirectional) | ✅ no injectable terms; onward band → **/collections/numbing-gel + /collections/numbing-spray** (non-injectable only); no umbrella/"see all procedures" link |
| **G** | Range integrity | ✅ "three strengths"/"three formats" (never "four"); cream tiers Clinical/Advanced/Professional |
| **H** | Trust signals | ✅ 4 locked signals (UK formulated · Cosmetic product · CPSR assessed · Made for aesthetics) |
| **I** | Slugs de-suffixed | ✅ aftercare → **/products/foaming-cleanser** (no `senseless-` prefix); no suffixed product links |
| **J** | §8 quick-add card (collection-only) | ✅ built + **live-proven** (see above): chips (active solid fill), qty stepper, add-to-cart, product-form-component, Judge.me slot, flagship Professional, filter tabs |
| **K** | Build hygiene | ✅ theme-check **0 errors** (380 files; 24 pre-existing warnings); live prices £44.99/£49.99/£55.99 (never £TBC); inventory 0 → "Sold out"/OutOfStock; pushed via Shopify CLI; **Asset-API diff** confirmed remote == local (data-avail present, old `disabled` gone, JS sold-out branch present) |

## Honest notes / flags
- **Add-to-cart can't be exercised end-to-end yet** — inventory is 0, so every card correctly shows "Sold out" (disabled). The card *mechanics* (chips→variantId, qty stepper, product-form-component wiring) are live-proven; the AJAX add + cart-drawer open will fire once stock is set. (Same pre-launch gate as the product pages.)
- **Grid sort:** cards render in the collection's current sort (prices showed Advanced 30g £49.99 as the first multi-size card; Professional £55.99 present as flagship). If a strict **Clinical → Advanced → Professional** visual order is required, set it via collection sort / product position in Stage 2 — flagging for your call.
- **Judge.me per-card stars** pending app install (launch-gate, same as product pages); slot is `:empty`-hidden until then.

## Deploy
- `shopify theme push --store senseless-numbing.myshopify.com --theme 199324434780 --only sections/senseless-collection-grid.liquid` → Asset-API diff verified the fix landed.
- Git: committed to `dev`, pushed `origin/dev`.

## HOLD — Stage 1 checkpoint
Stage 2 (Numbing Gel, Numbing Spray, Microneedling, Laser Treatment, Semi-Permanent Makeup, Waxing) **NOT started** — awaiting your approval of the proven card pattern.
