# Shop All collection + CTA repoints (⚠ theme deploy blocked on Shopify CLI incident)

**Date:** 2026-06-03 (BST) · **Branch:** dev · **Theme:** Senseless Dev `#199324434780` (store `senseless-numbing`)
Token refreshed (`./scripts/refresh-token.sh` → shpca_64b5ea…). Build source: spec `37458bc375ea81d3aa90de00c9e52a7d`.

## 0. Mobile-header fix push — CONFIRMED + pushed ✅
The prior session committed the mobile-header/drawer fix (`482aec4`, `senseless-header.liquid` + `ARCHITECTURE.md`) but hit ConnectionRefused before `git push`. Verified it was **unpushed** (`origin/dev` was at `253090f`) and **pushed it** — `origin/dev` is now at `482aec4`, nothing unpushed. Done.

## 1. Shop All collection — REUSED (not duplicated), auto-populates the full range ✅
- A `shop-all` collection **already exists** (`gid://shopify/Collection/690350031196`, handle **`shop-all`**, title "Shop All") — reused, not duplicated.
- It's a **smart collection** (rule `VARIANT_PRICE > 0`) → auto-populates **every product**, stays in sync. Verified contents via GraphQL: **10 products / 15 SKUs incl. Foaming Cleanser** (Cream 5 + Gel 6 + Spray 3 + Cleanser 1). No injectable products pulled in (injectables are collections, not products).
- **noindex set ✅** — `seo.hidden = 1` metafield set on the collection via GraphQL (Shopify platform adds `noindex` + excludes from the XML sitemap). [Live `<meta robots>` render-verify pending — see blocker.]
- Clean custom template written: **`templates/collection.shop-all.json`** — a single `senseless-collection-grid` section (short heading "Shop all", `show_filters:false`, no editorial/System/procedure) → 1:1 cards + storefront quick-add + native sort, canvas/Montserrat/purple. **Committed to git; NOT yet deployed (blocker).**

## 2. CTA repoints — written, committed, NOT yet deployed
- Homepage hero primary "Shop the range": `index.json` `primary_cta_url` `/collections/numbing-cream` → **`/collections/shop-all`**.
- Shop mega "Shop all": `header-group.json` `mega_cta_url` `/collections/numbing-cream` → **`/collections/shop-all`**.
- (Cream product/collection "Shop the cream range" CTAs left pointing at the cream collection, per the brief.)
- Both edits **committed to git (`4494993`)** but **NOT deployed** to the theme (blocker) — so live CTAs still point at /collections/numbing-cream until the push lands.

## ⚠ BLOCKER — Shopify CLI / API incident (theme deploy could not complete)
A sustained Shopify-side incident is in progress. State observed:
- `shopify theme push` fails on every attempt (~13 tries over the session) with: **`Error connecting to your store … GraphQL Error (Code: 404) … query publicApiVersions … 404 Not Found`** — the CLI's API-version negotiation endpoint is 404ing.
- The **REST Asset API** (`/admin/api/2024-10/themes/{id}/assets.json`) now also **404s** (it worked earlier this session) — so even the Asset-API diff is unavailable.
- **Storefront** collection pages (incl. the known-live `/collections/numbing-cream`) returned 404 in render checks — broadly flaky.
- **Working:** Admin **GraphQL** (`graphql.json`) and **git/GitHub**. That's how the collection audit + `seo.hidden` were done and the code was preserved.

Per **Hard Rule #11**, theme deploys must go through the Shopify CLI (never the API token), so I did **not** deploy the 3 theme files via `themeFilesUpsert`/Asset API. They remain committed in git, ready to push the moment the CLI recovers.

No live breakage from the half-state: `shop-all` still renders via the default collection template (functional + now noindex); the collection `templateSuffix` was deliberately **left unset** (setting it to `shop-all` before the template asset is deployed would break the page).

## Remaining to complete when the Shopify CLI recovers
1. `shopify theme push --only templates/collection.shop-all.json --only templates/index.json --only sections/header-group.json` (store senseless-numbing, theme 199324434780).
2. `collectionUpdate` set `templateSuffix = "shop-all"` on collection `690350031196` (GraphQL) — **only after step 1 lands**.
3. Render-verify: grid lists all 10/15 incl. cleanser + quick-add works; `<meta robots>` noindex on shop-all + absent from sitemap; homepage hero + Shop mega resolve to `/collections/shop-all`; `/collections/numbing-cream` untouched + still indexed; desktop + mobile.

## Verify (what passed now)
- **theme-check: 0 errors** (local; 395 files, 24 pre-existing Horizon warnings).
- **GraphQL:** shop-all = 10 products / 15 SKUs incl. cleanser; `seo.hidden=1` set (no userErrors).
- **git:** `482aec4` (mobile fix) + `4494993` (shop-all template + CTAs) on `origin/dev`.

## Files / API
- New: `templates/collection.shop-all.json`. Edited: `templates/index.json` (hero CTA), `sections/header-group.json` (mega CTA).
- API (GraphQL, allowed): `metafieldsSet` `seo.hidden=1` on the shop-all collection.

## HOLD
Mobile-fix push confirmed; shop-all reused + noindex set; clean template + CTA repoints committed to git. **Theme deploy + `templateSuffix` wiring + render-verify are blocked on a live Shopify CLI/API incident (`publicApiVersions` 404).** Re-run the deploy (3 steps above) when Shopify's API recovers — happy to complete it on a re-trigger.
