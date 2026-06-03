# Shop All deploy — COMPLETE ✅

**Date:** 2026-06-03 (BST) · **Branch:** dev · **Theme:** Senseless Dev `#199324434780` (store `senseless-numbing`)
Token refreshed (`./scripts/refresh-token.sh` → shpca_cc1db2…). The blocked deploy (commits `4494993` etc.) is now finished — Shopify connectivity from this environment recovered (probe 8/8 after earlier ~20%), and the CLI push went through.

## The 3 remaining steps — all done
1. **`shopify theme push`** of the 3 staged files succeeded (`templates/collection.shop-all.json`, `templates/index.json`, `sections/header-group.json`). Confirmed on remote: shop-all template present (`senseless-collection-grid`); index hero CTA = `/collections/shop-all`; mega CTA = `/collections/shop-all`.
2. **`collectionUpdate templateSuffix="shop-all"`** on `Collection/690350031196` (GraphQL) — set, no userErrors.
3. **Render-verify** — all green (below).

## Verify (live preview, desktop + mobile)
- **`/collections/shop-all`** (200): **10 product cards**, **10 quick-add buttons** (size chips wired), **Foaming Cleanser present**; heading "Shop all"; **no editorial sections** (clean fast-lane grid); **`<meta robots> = noindex,nofollow`** (from `seo.hidden=1`). Mobile (390px): 200, 10 cards, 10 quick-add, single-column grid. All 10 products / 15 SKUs reachable via the cards.
- **`/collections/numbing-cream`** (200): **not noindex** (`robots` null) — SEO collection untouched + still indexed.
- **CTAs:** homepage hero "Shop the range" → `/collections/shop-all` ✓; Shop mega "Shop all" → `/collections/shop-all` ✓.
- **Sitemap:** preview sitemap is password-gated (HTTP 400) so not directly checkable here, but `seo.hidden=1` excludes the collection from the sitemap at the Shopify platform level (same mechanism that emitted the noindex meta).
- **theme-check: 0 errors** (local).

## Final state
- `shop-all` (smart collection, `VARIANT_PRICE > 0`) auto-populates the full catalogue — 10 products / 15 SKUs incl. cleanser; stays in sync.
- Clean custom template live (`templateSuffix=shop-all`): grid + quick-add only, canvas/Montserrat/purple, 1:1 cards.
- noindex + sitemap-excluded (returning-customer fast lane, not an SEO surface).
- Both primary CTAs (homepage hero + Shop mega) drive into Shop All; the SEO collection `/collections/numbing-cream` is unchanged and still indexed.

## Note on the blocker
The earlier failures were intermittent connectivity to `*.myshopify.com` from this environment (per-request ~70% 404, defeating the multi-call CLI push) — not the Shopify incident and not the CLI session. It cleared; the push then succeeded first try in a stable window. No API-token substitution was used for the theme push (Hard Rule #11 respected).

## HOLD
Shop All complete, deployed, and verified live (desktop + mobile). Mobile-header fix (`482aec4`) also confirmed pushed earlier this session.
