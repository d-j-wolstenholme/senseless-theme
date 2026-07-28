# Next session — Senseless (Canon v2.19)

Read `CLAUDE.md` → run `scripts/reconcile.sh` → read the Project Instance + State Surface first.
**Machine last used:** MacBook Pro — confirmed 28 Jul. NOTE: hostname can display as `Daniels-MBP.Home` (network-dependent); canon's `Daniels-MacBook-Pro.local` is the same machine.

## Done last session (2026-07-28, Claude Code · Fable 5) — app-store badges live + local↔live reconcile
Both apps are approved and public: **iOS** `apps.apple.com/gb/app/senseless/id6792059702` (Apple approved 28 Jul 14:41; listing verified 200 — closes the App project's "confirm it went live" question) · **Android** `play.google.com/store/apps/details?id=uk.senseless.app` (1.0.1 since 24 Jul).

- **Local↔live reconciled FIRST** (Daniel: live is the most up-to-date version; don't lose add-ons). Full semantic diff found **one real delta** — live carried a **Shopify Inbox chat app block** in `config/settings_data.json` added via admin. Adopted live verbatim (`96e6427`) so no future push wipes it. Everything else was editor noise. `sections/footer-utilities.liquid` was the reverse (local ahead — `64fcfdc` cleanup never deployed); now deployed. 2 known inert orphans unchanged.
- **NEW `/pages/app`** — page gid `713221013852`, template `page.app.json` + `sections/senseless-app-download.liquid`, published, meta set, **not** `seo.hidden` (a real public destination). **`/app` → `/pages/app` 301** created (gid `1707295768924`) as the short URL for QR encoding. This page is the **QR fail-safe**.
- **OS detection** — `snippets/senseless-os-class.liquid` (head) stamps `ss-os-ios`/`ss-os-android` on `<html>`; badge visibility is then pure CSS. Live-verified: classified → own badge only (60px) + cross-link; unclassified/no-JS → both at equal 52px. No zero-badge state.
- **Cart app banner** — `snippets/senseless-app-banner.liquid` via `cart-summary.liquid` (drawer + cart page), above the checkout CTAs. Live 10% app discount (`ZK7QF3M9N2X8WB4D6PLA`, ACTIVE) with was/now maths + double points + 200-pt welcome.
- **Cart line-item images no longer cropped** — `templates/cart.json` had `image_ratio: portrait` (0.8) vs 1:1 photography → sides clipped. Now `adapt`.

### Gotchas earned this session (don't re-derive)
- **Cart banner is mobile-layout only (≤749px) — Daniel's explicit call.** An earlier reviewer-suggested "OR any `ss-os` device" rule was reverted. **Do NOT re-raise "iPads report 768px+, so tablets are excluded" as a bug** — it is deliberate.
- **A PRODUCT-class discount leaves `cart.cart_level_discount_applications` EMPTY** while `cart.total_discount` is set. The app 10% is product-class, so any "is a discount applied?" check must test **both** — testing only the former fails open. (This is why the banner's misleading-price guard checks both.)
- **The cart drawer and the cart PAGE do not share block settings.** `header-actions` renders `cart-products` with none, so it falls back to the snippet's `ratio = 1` default; the cart page passes `templates/cart.json`'s value. A drawer-only check will miss cart-page-only image bugs (exactly how the crop survived).
- **Official Google Play badge art ships with a ~41px transparent border baked in** (opaque 564×168 inside 646×250). Under equal CSS heights it renders at 67% of the Apple badge → breaks Google's own parity guidance. The repo copy `assets/senseless-badge-google-play.png` is **already cropped full-bleed**; if you ever re-import from Google, re-crop.
- **`reviews-guard` guard(c) trips on `config/settings_data.json`** whenever it's synced from live, even though it is never deployed (the guard checksums repo files regardless of the push set). Verify the 4 markers match live (judge-me-reviews 2 · klaviyo 1 · google-youtube 1 · dondy 1), then `--reviews-changed` + commit the rewritten lock.
- **Shopify MCP connector is STILL invalid** (`get-shop-info` → token expired; unchanged since 27 Jul) — **Daniel needs to reconnect it**. The CLI + Admin-API-token path (`scripts/refresh-token.sh`, `deploy.sh`) is unaffected; use that.
- `templates/page.app.json` byte-differs from live on the Asset API (Shopify reformats template JSON) but is **semantically identical** — compare parsed JSON, not bytes, before calling it a failed push.

### Next / watch (this task)
- **Daniel: encode the packaging/QR download URL as `https://senseless.uk/app`** — live and 301-ing now.
- ~~`/pages/app` not linked from any menu~~ — **DONE 28 Jul:** "Get the app" added to `senseless-footer-company` (footer **Company** column, after About / Trade & wholesale) via `menuUpdate`, no deploy. Verified in-browser on the live homepage.
- **`/pages/rewards` omits the 10% app discount** from its app-vs-web comparison while the new surfaces lead with it. A clarifying row/sentence would remove the inconsistency — **not changed without sign-off** (rewards copy is approved).
- Optional: the badge store URLs are hard-coded in the banner but editor-settable on the page — two sources of truth if a listing URL ever changes.

## Carried forward — open flags (compressed from 9–17 Jul sessions; detail in Session Log)
- **`mobile-app-privacy-policy`** still missing here (wrong-store casualty); store listings currently use `/pages/privacy-policy`. Needs a decision.
- **MHG footer logo** (12 Jul, `508d399`): Daniel to sign off full-lockup vs monogram. Lockup is a light-background asset.
- **Injectables** (10 Jul, `1fa8678`): botox fold-vs-keep (301-merge call, deferred); GSC watch — `numbing-cream-for-injections` should move off 0 impressions.
- **Cannibalisation** (9 Jul): GSC watch — strongest absorbs "best numbing cream" via 301; next SEO fix = spray/gel format-cluster splits.
- **Live theme carries TWO inert orphans** (scoped deploys can't delete remote files; Asset-API delete barred): `blocks/footer-copyright.liquid` + `templates/page.how-long-numbing-cream-takes-to-work.json`. Harmless; clears on a full re-sync.
- **If totally-numb.com recovers** (503 on 17 Jul): delete the stray 16-Jul `delete-account`/`mobile-app-privacy-policy` pages there — they name the Senseless app.

## Carried forward — open from 2026-07-04 rewards session (still open)
- **⚠️ Coming-soon earn methods on `/pages/rewards` are Daniel's explicit call — do NOT revert as a compliance regression.** Only birthday has a decided value (100pt); referral/reviews/social have NO decided values — don't invent numbers.
- **4 planned earn methods NOT built** (App project): birthday · referral · social (blocked) · reviews. When any ships: flip `coming_soon` off + set the real value.
- **Rewards T&C legal review (MHG/legal)** — §6–8 placeholder numbering flagged; Status Built (not Final).
- **Rewards link-out** (3 Jul): hosted account page showed no balance; Customer Account UI Extension handed to the App project.
- **Store province "England"** (should be Lancashire) — UNFIXABLE via UI/API; never rendered.

## Carried-forward gotchas (still valid)
- **Store gate recurring:** the Shopify MCP connector can silently point at **Totally Numb** — gate every session on `senseless-numbing.myshopify.com`. Reliable CLI path: `scripts/refresh-token.sh` + `deploy.sh` (both store-pinned).
- **`senseless-numbing.myshopify.com` 301s to `senseless.uk`** — always `-L`.
- **Cache-busting a live check: use `?_fd=0`, NOT `?cb=`.** The edge normalises `?cb=` away and serves a cached snapshot, so you get a convincing **false negative**. (28 Jul: ten `?cb=` polls over 150s said a new footer link was missing; `?_fd=0` and a real browser both showed it instantly.) The cache is **per URL + per variant** — a stale desktop homepage can sit alongside a fresh mobile homepage and four fresh pages, so check several URLs and finish in the browser before concluding a change failed. Theme-FILE deploys bust page caches on their own; admin-side changes (`menuUpdate`, `metafieldsSet`) do not.
- **Adding a policy page:** `pageCreate` (handle + `templateSuffix: policy` + `isPublished`) → `policy.*` metafields via the `RT` converter in `scripts/policy-metafields.py` (never hand-JSON) → `global.title_tag`/`description_tag` + `seo.hidden=1` → add handle to `ss_noindex_handles` in `layout/theme.liquid` (+ deploy). Never run the script wholesale (per-page `last_updated` regresses).
- **Deploy order: SECTION (schema) BEFORE the TEMPLATE using new schema settings** — a combined push makes Shopify validate against the old schema and silently STRIP unknown block-settings. Verify via Asset API after. (Held correctly on 28 Jul: section pushed stage 1, template stage 2, all 4 blocks intact.)
- **Footer tiers:** 4 columns are Shopify nav menus (`senseless-footer-*`, `menuUpdate`, no deploy); the bottom **legal bar** is **hardcoded** in `sections/senseless-footer.liquid`.
- **Never set `seo.hidden` on a BLOG to tidy the sitemap** — it cascades to its articles (tested live 17 Jul, reverted). The `/blogs/guides` conflict is structural; accept the GSC warning. Child sitemaps need their `?from=&to=` params.
- **Retiring a page via 301 needs an UNPUBLISH** (a redirect is inert while the page resolves 200).
- **Intermittent 503s under rapid curls** can falsely trip the post-deploy reviews-guard — space out re-checks before treating it as real.
- `.env` Admin token expires — `./scripts/refresh-token.sh` then `set -a; source .env; set +a`. No rollback theme.
