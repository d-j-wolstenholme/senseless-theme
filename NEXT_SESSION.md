# Next session — Senseless (Canon v2.19)

Read `CLAUDE.md` → run `scripts/reconcile.sh` → read the Project Instance + State Surface first.

## Done last session (2026-07-04, MacBook Pro)
Rewards-programme surfaces. Commits (newest first): `a079dca`, `b011169`, `60054d6`, `b7c1eab`, `6e485e1`.

**1. Rewards T&C published as a live policy page** (`6e485e1`) — new `/pages/rewards-terms` on the existing `policy` template/metafield pattern (page id `712303313244`, published, noindex like the other 5 legal pages via `seo.hidden=1` + `ss_noindex_handles` in `layout/theme.liquid`). Copy = Notion "current, revised 4 Jul 2026" §1–17 verbatim. Metafields set via the RT converter directly (record in `scripts/policy-metafields.py`, now the 6th policy page). Work Item `39358bc3-75ea-8152` → **Built**.

**2. Cross-links (all three).** Marketing `/pages/rewards` small-print → "full Rewards Terms & Conditions"; main T&C `see_also` → +Rewards Terms & Conditions; footer → "Rewards Terms".

**3. Footer placement = LEGAL BAR** (`60054d6`) — Daniel moved "Rewards Terms" out of the Help column into the **bottom legal bar** (hardcoded in `senseless-footer.liquid`, with Privacy/Terms/Cookie); removed the Help-menu item (`senseless-footer-help`).

**4. §17 "Lancashire" dropped** (`60054d6`) — rewards-terms §17 now matches the other legal pages ("…Skelmersdale, WN8 9PL"). Metafield corrected + Admin-API-verified. **Render note:** Shopify's storefront metafield-value cache lagged (still showed the old value at last check) — self-heals on TTL, NOT theme-deploy-bustable (re-deploying that page's own section didn't clear it).

**5. `/pages/rewards` reorganised + all ways to earn** (`b011169`, `a079dca`) — Daniel: "add all now". Split the flat rates list into **Ways to earn** (3 live: 1pt/£1 · 2× in-app · 200pt welcome) + **Redeeming & the rules** (redeem / no expiry / signed-in-only). Added the 4 planned methods as **"coming soon"** (Birthday 100pt [also App only] · Refer a friend · Product reviews · Follow us). Added `group` + `coming_soon` controls to the `senseless-rewards` `rate` block (rows render App-only + Coming-soon pills independently). New FAQ item + small-print note.

## Open follow-ups / flags
- **⚠️ Coming-soon earn methods are Daniel's explicit call — do NOT revert as a compliance regression.** They're framed "coming soon" (honest, not claimed active). This extends the earlier "exclude not-yet-active until shipped" stance to a *coming-soon-on-the-marketing-page* framing. Only birthday has a decided value (ADR-009, 100pt); referral/reviews/social have NO decided values (don't invent numbers).
- **The 4 planned earn methods are NOT built** (App project): birthday (Not-started, value 100pt decided, needs DOB capture) · referral (Not-started, value undecided, bigger build) · social (blocked — **social accounts don't exist**) · reviews (no direction). When any ship, flip its `coming_soon` off + set the real detail/value. Work Items: birthday `39358bc3-75ea-81d5`, referral `39358bc3-75ea-81a0`, social `39358bc3-75ea-81c0`.
- **Rewards T&C legal review (MHG/legal)** — source flags §6–8 placeholder numbering + "flag to a lawyer before publishing." Live per Daniel's go-ahead; Status = Built (not Final) for this reason.
- **Rewards page link-out destination still broken** (Daniel, 3 Jul): hosted account page shows no balance — Customer Account UI Extension may not be installed on `senseless-numbing`. Handoff issued to the App project.
- **Store province "England" (should be Lancashire)** — UNFIXABLE via UI/API (no county field, no shop-address mutation); never rendered. Cross-brand carriers (Totally Numb, MHG) still on the old London address — separate gated pass.
- Header mis-links (pre-existing): "How long it takes to work" / "How long it lasts" in the Application-guides menu point to `/pages/using-numbing-cream`, not the dedicated `how-long-*` pages.

## Backlog (unchanged)
- ntn write-back wiring · Phase 12 nav/link wiring · Phase 10 photography · optional GPay-at-checkout function. Launch-gate: **CLEAR**.

## Gotchas
- **Deploy order: SECTION (schema) BEFORE the TEMPLATE that uses new schema settings.** A combined push makes Shopify validate the JSON template against the pre-update schema and **silently STRIP** the unknown block-settings (hit this: `group`/`coming_soon` vanished until a template-only re-push against the live schema). Verify block settings via the Asset API after, not just the render.
- **Shopify metafield-value cache is NOT theme-deploy-bustable.** A page's rendered metafield value can lag minutes+ after `metafieldsSet`, even after deploying that page's own section. Verify the *stored* value via Admin API; the render self-heals. (Theme-FILE content changes DO bust their pages' cache; metafield-only changes don't.)
- **Adding a policy page** = `pageCreate` (handle + `templateSuffix: policy` + `isPublished`) → set `policy.*` metafields (build `prose_policy_body` with the `RT` converter in `scripts/policy-metafields.py`, never hand-JSON) + `global.title_tag`/`description_tag` + `seo.hidden=1` → add handle to `ss_noindex_handles` in `layout/theme.liquid`. Shopify normalizes `rich_text_field` on store (strips empty link `title`/`target`) → verify semantically, not by byte length.
- **Footer link tiers:** the 4 columns (Shop/Learn/Help/Company) are **Shopify nav menus** (`senseless-footer-*`, edit via `menuUpdate`, no deploy). The bottom **legal bar** (Privacy/Terms/Cookie/**Rewards Terms**) is **hardcoded** in `sections/senseless-footer.liquid`.
- `.env` Admin token expires — `./scripts/refresh-token.sh` then `set -a; source .env; set +a`. Token has full write scopes. MCP Shopify connector works independently.
- **Intermittent storefront HTTP 503s** appear under many rapid curls (rate-limiting) — can trip `deploy.sh`'s post-deploy reviews-guard verify falsely. Re-check Judge.me markers spaced out before treating a guard-fail as real.
- Reviews-guard: only product/reviews surfaces + `settings_data.json` are guarded (`--reviews-changed` rewrites the lock). Policy pages, footer, theme.liquid, rewards page are NOT guarded.
- Store gate: MCP/CLI default is Totally Numb — verify `senseless-numbing.myshopify.com` first. No rollback theme.
