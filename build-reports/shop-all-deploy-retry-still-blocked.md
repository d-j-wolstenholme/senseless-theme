# Shop All deploy — retry attempt (still blocked: intermittent Shopify connectivity from this environment)

**Date:** 2026-06-03 (BST) · **Branch:** dev · **Theme:** Senseless Dev `#199324434780` (store `senseless-numbing`)
Token refreshed (`./scripts/refresh-token.sh` → shpca_cc1db2…). Re-attempt of the blocked deploy after "incident cleared".

## Outcome: theme push still cannot complete from this environment
Re-ran the deploy. The Shopify CLI still fails on the `publicApiVersions` handshake, and the root cause is now pinned down:

- **It's not push-specific:** `shopify theme list` fails identically → the CLI can't complete *any* theme command's API handshake.
- **It's not the CLI session/version:** CLI 3.94.3 (worked earlier this session, unchanged). Direct probing with the Admin token shows the failure is at the network/request layer.
- **It's intermittent connectivity to `*.myshopify.com` from this environment.** Probing `admin/api/2024-10/graphql.json` with the working Admin token: the **same endpoint** returns HTTP **404** for most requests and **OK** for a few, seemingly at random (e.g. `{shop{name}}` 404'd on 6/6 tries while `{publicApiVersions}` succeeded on 2/6 in the same loop). Roughly ~70%+ of single requests 404. `{shop{name}}` and `seo.hidden` succeeded earlier this session during a better window.
- **git/GitHub is reliable throughout** — so this is a network path specific to Shopify from this sandbox, not a general outage, and not necessarily reflected on Shopify's status page.

The CLI `theme push` needs *many consecutive* successful API calls (handshake → `themeFilesUpsert` → verify). At a ~25–30% per-call success rate, a full clean run almost never lands — **26 push attempts across the two sessions, 0 successes.** Per **Hard Rule #11** I did not substitute the Admin API token (`themeFilesUpsert`) for the CLI.

## State (unchanged from the prior report — all still true)
- **Code ready on `origin/dev`:** `templates/collection.shop-all.json` (clean grid-only), `index.json` hero CTA → `/collections/shop-all`, `header-group.json` mega CTA → `/collections/shop-all` (commit `4494993`).
- **`shop-all` collection** reused (`690350031196`), auto-populates **10 products / 15 SKUs incl. cleanser**; **`seo.hidden=1` set** (noindex + sitemap exclusion).
- **No live breakage:** `shop-all` renders via the default collection template (functional + noindex); `templateSuffix` deliberately left unset; live CTAs still point at `/collections/numbing-cream` until the push lands.
- **theme-check: 0 errors** (local).

## To finish (unchanged — 3 steps, need stable Shopify connectivity)
1. `shopify theme push --store senseless-numbing.myshopify.com --theme 199324434780 --only templates/collection.shop-all.json --only templates/index.json --only sections/header-group.json`
2. `collectionUpdate templateSuffix="shop-all"` on `690350031196` (GraphQL) — only after step 1 lands.
3. Render-verify: grid 10/15 + quick-add; noindex meta + not in sitemap; hero + Shop mega resolve to `/collections/shop-all`; `/collections/numbing-cream` untouched + indexed; desktop + mobile.

## Recommendation
Two paths, whichever is faster:
- **Run the push from a machine with clean Shopify connectivity** (e.g. Daniel's Mac via `! shopify theme push …`) — the network path there is fine; then the `templateSuffix` + verify can follow.
- **Or re-trigger me later** when this environment's path to `*.myshopify.com` stabilises — the code is staged and the 3 steps are scripted.

## HOLD
Deploy still blocked on intermittent Shopify connectivity from this environment (not the cleared incident; a per-request ~70% 404 rate that defeats the multi-call CLI push). Nothing changed live this attempt; `seo.hidden` already set; code on `origin/dev`.
