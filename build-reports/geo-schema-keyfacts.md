# Build Report — GEO + schema layer (Key Facts, JSON-LD, footer attribution)

- **Machine:** MacBook Pro
- **Date:** 2026-05-31 (BST)
- **Branch:** `feature/geo-schema-keyfacts` (off `dev`) → PR into `dev`
- **Live theme:** Horizon `#195280437583` — untouched, not published.

## Completed

1. **Key Facts block (GEO)** — new `sections/senseless-key-facts.liquid`: machine-extractable semantic `<dl>` (label/value fact rows) + heading, with a **fixed, non-editable** closing line `UK cosmetic product, by Matrix Health Group Ltd. Not a medicine.` (hardcoded so it can't be removed in the editor). Per-page facts seeded **verbatim from each page's Notion v2 "Key Facts" block**. Wired into **14 templates**: product, 3 format collections (numbing-cream/gel/spray), 6 guides (choosing-your-strength, choosing-your-format, how-it-works, how-long-…-takes-to-work, how-long-…-lasts, does-numbing-cream-work), 4 landings (best-numbing-cream, strongest-numbing-cream, best-emla-alternative-uk, senseless-vs-ametop).
2. **Product + Offer JSON-LD** — `snippets/senseless-structured-data.liquid` (rendered once in `theme.liquid` head, dispatched on `request.page_type`): name, claim-free description, up to 5 images, brand "Senseless", manufacturer + offer `seller.legalName` "Matrix Health Group Ltd", and an Offer per variant with **live** price / `priceCurrency` (`cart.currency.iso_code | default: shop.currency`) / availability (`InStock`/`OutOfStock` from `variant.available`) — nothing hardcoded.
3. **CollectionPage + ItemList JSON-LD** — same snippet: CollectionPage + `mainEntity` ItemList of products (position + name + url), `numberOfItems` from `collection.all_products_count`.
4. **BreadcrumbList JSON-LD** — `snippets/senseless-breadcrumbs-jsonld.liquid`: product (Home → [collection] → product), collection (Home → collection), page (Home → page).
5. **Footer MHG attribution** — `blocks/footer-copyright.liquid` + `footer-group.json`: subtle text link in the legal band → `https://matrixhealthgroup.co.uk` (`target="_blank" rel="noopener"`, label/title "Matrix Health Group Ltd — parent company"). **No MHG logo asset exists → text link used (asset needed, flagged).**

## Idempotency / no-duplication

- The dispatcher emits **only the missing types**; it does **not** duplicate the existing schema: Organization (Horizon `header.liquid`), FAQPage (`senseless-faq-accordion`), Article (Horizon `main-blog-post`).
- Key-facts wiring script is idempotent (skips templates already wired).

## Validation

- **Compliance-check on authored copy: PASS** (fixed line mirrors COMPLIANCE.md classification; "topical cosmetic preparation" is the approved pattern; tier names correct; schema = Product type, not Drug/Medicine).
- **JSON-LD well-formedness: PASS** — simulated + `json.loads` across 8 cases (1/3 variants, 0/2 images, optional vendor/sku/description, all breadcrumb branches). Fixed a real bug pre-commit: Product `image` array now loops `product.images` (was `product.media` with a `media_type` guard that could leave a trailing comma after a video).
- **`theme check`: 0 errors** (24 warnings, unchanged baseline).
- **Live Google Rich Results test: PENDING** — products/collections don't exist in admin yet (£TBC / 0 stock), so run the live Rich Results test once real product/collection data is created.

## Files added / changed

- **Added:** `sections/senseless-key-facts.liquid`, `snippets/senseless-structured-data.liquid`, `snippets/senseless-breadcrumbs-jsonld.liquid`, `build-reports/geo-schema-keyfacts.md`.
- **Changed:** `layout/theme.liquid` (render dispatcher), `blocks/footer-copyright.liquid` + `sections/footer-group.json` (MHG link), `docs/SECTIONS.md` (new section + 2 snippets), 14 templates (key-facts wiring).

## Open items / still needed

1. **MHG logo asset** — none in `assets/`; footer uses a text link. Supply `senseless-mhg-logo.svg` (or PNG) for a logo treatment.
2. **Per-SKU product Key Facts** — the shared `product.json` carries **generic range-level** facts (Category / Strengths / Formats / Made in). Once products exist in admin, drive per-SKU facts from a product metafield (e.g. `senseless.key_facts`) so each PDP shows SKU-specific facts.
3. **"numbing" in body copy (compliance WARN)** — several audited v2 Key Facts use "numbing cream/gel/spray" as a category noun in body (3 format collections + "best-numbing-cream"). This is **not** in COMPLIANCE.md's hard "Never Use" list (those are effect claims); it touches the *SEO-vs-body placement* guideline. Shipped **verbatim** (audited GEO copy, on the numbing-cream category pages). **Owner to confirm** whether the body-copy "numbing" usage stands or should be reworded; reconcile COMPLIANCE.md if it stands.
4. **Notion-row vs built-slug mismatches** — facts were wired to the built template filenames; some Notion rows use different slugs: how-it-works (Notion `how-senseless-works`), how-long-…-takes-to-work (Notion `how-long-does-numbing-cream-takes-to-work`), how-long-…-lasts (Notion `how-long-does-numbing-cream-lasts`), does-numbing-cream-work (Notion `does-numbing-cream-actually-work`). Reconcile canonical slugs.
5. **best-emla-alternative-uk & senseless-vs-ametop** — their Notion Key Facts list a fixed-line *variant* as fact 1; skipped to avoid duplicating the section's hardcoded fixed line.
6. **Carryover:** `docs/ARCHITECTURE.md` re-sync (stale nav) still queued (doc-only, non-blocking).

## Git / deploy

- Commits: `b5fb64a` (code layer) → `1f4429e` (wiring + docs). PR `feature/geo-schema-keyfacts` → `dev` (not merged — awaiting review).
- Deployed to unpublished dev theme `#196680057167` for preview.
