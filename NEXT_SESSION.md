# Next session — Senseless (Canon v2.19)

Read `CLAUDE.md` → run `scripts/reconcile.sh` → read the Project Instance + State Surface first.
**Machine last used:** MacBook Pro (`Daniels-MacBook-Pro.local`) — confirm at session start.

## Done last session (2026-07-09 late, Claude Code · Opus) — Cannibalisation phase 3
**Guides-hub canonical + does-it-hurt disambiguation** — Work Item `39858bc3-75ea-8116` → **Built**; Decision `39858bc3-75ea-812f`. Commit **`065052c`**. Metadata/linking/indexing only.
- **Fix A:** `/blogs/guides` **INDEX** set `noindex,follow` in `layout/theme.liquid` (guarded `template.name == 'blog' and blog.handle == 'guides'`) — **articles under it stay indexed** (they render as `template 'article'`; verified live: index noindex=1, `does-botox-hurt`/`do-lip-fillers-hurt` articles noindex=0). Blog index links up to `/pages/articles`; the `/pages/articles` hub (auto-lists all blog articles) got the education-cluster guide cards added so it's comprehensive.
- **Fix B:** `does-it-hurt` hub's lip-filler/botox cards repointed → the blog spokes (hub now links all 4 procedure spokes + product/collection); `does-it-hurt-by-treatment` retitled off the bare "Does it hurt?" → `<title>` "How Much Does Each Treatment Hurt? Pain by Procedure", H1 "How much each treatment hurts", schema/FAQ headings updated, route row → 4-spoke router. `title_tag` + `page.title` updated Admin-side.
- **Watch:** by-treatment **breadcrumb** JSON-LD still shows the old page.title live — page-resource cache lag (NOT theme-deploy-bustable), self-heals on TTL; `<title>`+H1 are live-correct. Recheck ~1h.
- **Judgment call (Daniel):** `/pages/articles` "every guide" = the education cluster (6 cards added); flagship/system pages (`the-senseless-system`, `choosing-*`) left to nav. Easy to widen/narrow.

## Earlier same day — Cannibalisation phase 2
**Cannibalisation fixes phase 2 (title/heading/anchor disambiguation)** — Work Item `39858bc3-75ea-8139` → **Built**; commit `3e95454`. Titles/headings/meta/anchors only — no rewrites/redirects/merges.
- Collection `<title>` metafields now lead with the head term: Numbing Cream/Spray/Gel "… UK — Three Strengths | Senseless".
- `using-numbing-cream` → overview hub: SEO title off "How to Use / How Long It Lasts" → "The Complete Guide"; the competing "How long it lasts" H2 → "Timing depends on your appointment"; now links to BOTH how-long guides. (how-long lasts vs takes-to-work titles were already distinct.)
- `best-emla` FAQ anchor "how long does numbing cream last" repointed `/pages/using-numbing-cream` → `/pages/how-long-numbing-cream-lasts` — also fixes the how-long-lasts orphan.
- Laser collection "microneedling" mention hyperlinked → microneedling collection (bleed fix + interlink; reciprocal skipped to protect the #2 page).
- **⚑ FLAGGED for Daniel (EXCLUDE, not executed):** (1) `/pages/does-it-hurt` vs `/pages/does-it-hurt-by-treatment` — recommend does-it-hurt = hub, by-treatment = retitled detail spoke, interlink; NO merge. (2) `/blogs/guides` vs `/pages/articles` — recommend ONE canonical hub; needs an IA call. aesthetic-numbing-cream (SEO-only) + shop-all (canonical) left untouched per the 22-Jun hub Decision.

## Earlier same day (2026-07-09 am, Claude Code · Opus)
**Merge best-numbing-cream → strongest-numbing-cream (301 + keyword consolidation)** — Work Item `39858bc3-75ea-812f` → **Built**; Decision `39858bc3-75ea-811b` (Accepted 9-Jul). Commit **`fd50656`** (main, pushed). Session Log `39858bc3-75ea-81b9`.
- **301** `/pages/best-numbing-cream` → `/pages/strongest-numbing-cream` (UrlRedirect `1692265578844`); **best page unpublished** (retired, not deleted — reversible). Origin 301 6/6.
- **Keep-the-keyword on strongest:** "best numbing cream" folded into H2 + `meaning` body + new FAQ ("What's the best numbing cream?"); SEO `title_tag`="Best & Strongest Numbing Cream UK | Senseless" + new `description_tag`. "strongest numbing cream" retained (NOT de-optimised off "numbing cream"). Funnel CTA → `/collections/numbing-cream` intact.
- **Links repointed** (zero live links left to the retired URL): strongest `rel_best` card → collection; `page.choosing-your-format` CTA → strongest; `llms.txt` → strongest.
- Files: `templates/page.strongest-numbing-cream.json`, `page.choosing-your-format.json`, `page.llms-txt.liquid`. Gates: store-verify ✓ · compliance PASS · theme-check 0 · Asset-API semantic diff (deployed==local) ✓.

### Next / monitor
1. **GSC (Work Item step 7):** strongest should retain/absorb "best numbing cream"; best URL drops out via 301.
2. **Recheck ~1h:** `senseless.uk` edge → consistent 301 (gotcha below). Poll at ship time: origin 6/6 301; edge still ~1-in-6 stale-200.
3. Next highest-value SEO fix from the **2026-07-09 cannibalisation audit**: ranks 2–3 (spray + gel format-cluster splits — collection vs product on the head term).

### New gotchas this session
- **Retiring a Shopify page via 301 needs an UNPUBLISH.** A URL redirect is inert while the page still resolves 200 (Shopify serves the live page over the redirect). Create the redirect *first*, then unpublish → no 404 gap.
- **CDN lag after unpublish:** `senseless.uk` (Fastly) keeps serving a stale 200 of the old page for a while; `?cb=` does NOT bust it (edge normalises the param). Origin (`*.myshopify.com`) is authoritative — verify there. No manual purge; ages out on TTL.
- **Store gate recurring:** MCP `get-shop-info` defaulted to **Totally Numb** again. Reliable path: Admin-API token (`scripts/refresh-token.sh` → curl the hardcoded `senseless-numbing` Admin URL) + `deploy.sh` (both store-pinned). MCP alt: `switch-shop` → re-auth Senseless → `get-shop-info`.
- **Cross-terminal:** a "Totally Numb Rewards — T&C" build request was mis-sent to this Senseless terminal on 9-Jul and **cancelled** — belongs on the Totally Numb repo, not here.

---
## Carried forward — open from 2026-07-04 rewards session (still open)
- **⚠️ Coming-soon earn methods on `/pages/rewards` are Daniel's explicit call — do NOT revert as a compliance regression** (framed "coming soon", not claimed active). Only birthday has a decided value (100pt); referral/reviews/social have NO decided values — don't invent numbers.
- **4 planned earn methods NOT built** (App project): birthday (`39358bc3-75ea-81d5`, 100pt, needs DOB capture) · referral (`39358bc3-75ea-81a0`, value undecided) · social (`39358bc3-75ea-81c0`, blocked — accounts don't exist) · reviews (no direction). When any ship: flip `coming_soon` off + set real value.
- **Rewards T&C legal review (MHG/legal)** — §6–8 placeholder numbering flagged; live per Daniel; Status Built (not Final) for this reason.
- **Rewards link-out broken** (3 Jul): hosted account page shows no balance — Customer Account UI Extension may not be installed on `senseless-numbing`. Handed to App project.
- **Store province "England"** (should be Lancashire) — UNFIXABLE via UI/API; never rendered.
- Header mis-links (pre-existing): "How long it takes to work"/"How long it lasts" in Application-guides menu → `/pages/using-numbing-cream`, not the dedicated `how-long-*` pages.

## Carried-forward gotchas (still valid)
- **Deploy order: SECTION (schema) BEFORE the TEMPLATE using new schema settings** — a combined push makes Shopify validate the template against the old schema and silently STRIP unknown block-settings. Verify block settings via Asset API after.
- **Shopify metafield-value cache is NOT theme-deploy-bustable** — a rendered metafield value can lag minutes after `metafieldsSet`; verify the *stored* value via Admin API, render self-heals. (Theme-FILE changes DO bust their page cache.)
- **Adding a policy page:** `pageCreate` (handle + `templateSuffix: policy` + `isPublished`) → `policy.*` metafields via the `RT` converter in `scripts/policy-metafields.py` (never hand-JSON) → `global.title_tag`/`description_tag` + `seo.hidden=1` → add handle to `ss_noindex_handles` in `layout/theme.liquid`.
- **Footer tiers:** 4 columns (Shop/Learn/Help/Company) are Shopify nav menus (`senseless-footer-*`, `menuUpdate`, no deploy); the bottom **legal bar** (Privacy/Terms/Cookie/Rewards Terms) is **hardcoded** in `sections/senseless-footer.liquid`.
- **Intermittent 503s under rapid curls** (rate-limiting) can falsely trip `deploy.sh`'s post-deploy reviews-guard — space out re-checks before treating a guard-fail as real.
- `.env` Admin token expires — `./scripts/refresh-token.sh` then `set -a; source .env; set +a`. No rollback theme.
