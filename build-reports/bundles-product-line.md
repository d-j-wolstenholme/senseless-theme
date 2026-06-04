# 5-bundle product line + bundles collection + bundle template

**Date:** 2026-06-04 (BST) · **Branch:** dev · **Theme:** Senseless Dev `#199324434780` · **Commit:** `9dc599c`. Token refreshed.

## Computed prices (5% off the live component sum; compareAtPrice = the sum)
Read from current variant prices at build (not hardcoded), ×0.95, 2dp — matched the indicative values exactly.

| Bundle | SKU | Components | Sum | Price | Save |
|---|---|---|---|---|---|
| Clinical Numbing Kit — Small | SBUN-CL-S | cream 10g + gel 15ml + spray + cleanser | £79.96 | **£75.96** | £4.00 |
| Clinical Numbing Kit — Large | SBUN-CL-L | cream 30g + gel 35ml + spray + cleanser | £119.96 | **£113.96** | £6.00 |
| Advanced Numbing Kit — Small | SBUN-AD-S | cream 10g + gel 15ml + spray + cleanser | £94.96 | **£90.21** | £4.75 |
| Advanced Numbing Kit — Large | SBUN-AD-L | cream 30g + gel 35ml + spray + cleanser | £134.96 | **£128.21** | £6.75 |
| Professional Numbing Kit — Large | SBUN-PR-L | cream 30g + gel 35ml + spray + cleanser | £150.96 | **£143.41** | £7.55 |

## Build
- **5 products** created (`scripts/build-bundles.py`): ACTIVE, **own SKU each**, single **Default** variant (kit = one unit), inventory **tracking ON**, **stock 20** at the single location, **published to Online Store** (API-created products aren't auto-published — caught a 404, then `publishablePublish`). `compareAtPrice` = the component sum → storefront shows the saving natively.
- **Metafields:** `senseless.tier` (Clinical/Advanced/Professional), `senseless.format` = **Bundle** (new value), `senseless.bundle_contents` (list of "Component (size)|/products/handle"). Definitions created. Also `productType=Bundle` + `tags=[tier, Bundle]`.
- **Collection** `/collections/bundles` — smart, **rule product type = Bundle**, published + indexed. Populates with all 5.
- **Bundle template** `templates/product.bundle.json` (suffix `bundle`, assigned to all 5): `senseless-product-hero` (price + saving via compare-at, **AJAX add-to-cart** that stays on page, Buy-it-now) → `senseless-bundle-contents` (new — "What's in the kit", each component linked, "save £Y vs buying separately") → trust bar → System band (rich-text) → FAQ. **Product/Offer + BreadcrumbList + FAQPage** schema (Product/Offer + Breadcrumb come automatically from the head dispatcher since bundles are products; FAQPage from the FAQ section).

## Compliance
Strength-matched messaging; cleanser framed as aftercare; "everything for [tier] prep + aftercare in one"; "formulated in the United Kingdom", cosmetic not medicine, "numbing reduces discomfort rather than removing it"; no efficacy/onset/duration/% claims; Professional never flagged as flagship/strongest; 0 banned words.

## Verify
- **theme-check: 0 errors.** **Asset-API diff:** both new theme files MATCH/semantic-match.
- **API:** 5/5 ACTIVE, own SKU, price + compareAt correct, availableForSale=true, qty 20, tier+format+4 contents each; collection productsCount=5.
- **Render (Playwright):** /collections/bundles lists the 5; bundle PDP shows price £75.96 / compare £79.96, "save £4.00 versus buying separately", 4 kit links → component products, "Add to cart", schema = Product + BreadcrumbList + FAQPage.

## Flags / deviations
- **Reviews slot — pending Judge.me.** Judge.me isn't installed (Phase 11 flag), so I did **not** add a review widget. Per the app-block discipline, once Judge.me is installed add its **app block** to the bundle template in the theme editor (don't add a snippet `<div>` — Judge.me CSS suppresses `[data-from-snippet]`).
- **Smart-collection rule uses `productType=Bundle`** (reliable smart-collection condition + consistent with how the storefront filters format) rather than the `senseless.format` metafield; the metafield is also set per the brief.
- **System band** built with `senseless-rich-text` (no image needed) rather than the image-text-band.
- **Photography deferred** — bundles have no images yet; the hero shows the placeholder. Add kit photography later.
- Titles: "[Tier] Numbing Kit — [Size]" (handles `…-numbing-kit-{small,large}`). Adjust if a different naming is preferred.

## Files / API
- New: `sections/senseless-bundle-contents.liquid`, `templates/product.bundle.json`, `scripts/build-bundles.py`.
- API: 3 metafield definitions, 5 productCreate + variant price/compareAt/SKU/tracking + inventory 20 + metafields + Online-Store publish + suffix, 1 smart collection (published).

## HOLD
Bundle line live + verified. Pending: Judge.me reviews app block (ops), bundle photography. The Blog + Article Hub brief remains queued.
