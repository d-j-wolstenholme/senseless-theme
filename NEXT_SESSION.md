# Next session — Senseless (Canon v2.19)

Read `CLAUDE.md` → run `scripts/reconcile.sh` → read the Project Instance + State Surface first.

## Done last session (2026-07-04, MacBook Pro)
**Rewards T&C published as a live policy page + cross-linked everywhere** (commit `6e485e1`, deployed + live-verified). Work Item `39358bc3-75ea-8152` → **Built**.

- **New page `/pages/rewards-terms`** — reuses the existing policy pattern (`page.policy.json` → `senseless-policy-page`, `policy.*` metafields); published; noindexed like the other 5 legal pages (`seo.hidden=1` + handle added to `ss_noindex_handles` in `layout/theme.liquid`). Page id `gid://shopify/Page/712303313244`.
- **Copy** = Notion "current, revised 4 Jul 2026" §1–17 **verbatim** (the superseded 12-month-expiry / unbuilt-earning-methods draft was ignored). `prose_policy_body` render-verified (17 headings / 4 links / 7 list-items), `see_also` = Senseless Rewards + Terms & Conditions, `last_updated` 2026-07-04, `faq` []. `global.title_tag`/`description_tag` set (provisional — SEO is Daniel's axis).
- **Cross-links — all three:** ① marketing `/pages/rewards` small-print → "full Rewards Terms & Conditions"; ② main T&C `see_also` → +Rewards Terms & Conditions; ③ footer **Help** menu (`senseless-footer-help`) → "Rewards terms" (Help-column tier, not the strict legal bar).
- **How it was set:** metafields written via the RT converter **directly** on senseless-numbing (scratchpad script) — the `policy-metafields.py` *record* was updated (rewards-terms = 6th page) but NOT run wholesale (would regress the other pages' `last_updated`); added per-page `last_updated` support to the script to remove that footgun.
- Gates: store ✓ · compliance PASS · theme-check 0 · deploy.sh guard 5/5 · Asset-API semantic diff MATCH + live curl of all 4 surfaces ✓.

## Open follow-ups / flags
- **Rewards T&C legal review (MHG/legal) — recommended before "Final".** Source flags §6–8 placeholder numbering + "flag to a lawyer before publishing regardless." Daniel aware, non-blocking; page is live. Status left at **Built** (not Final) for this reason.
- **`rewards-terms` §17 keeps "Lancashire"** (verbatim from source: "…Skelmersdale, Lancashire, WN8 9PL") whereas the other legal pages/policies still OMIT the county — this is the older open **Lancashire content gap** (footer, 3 native shop policies, T&C page all read "…Skelmersdale, WN8 9PL"). Still fixable (plain content edit, no platform limit); never actioned. Decide: add Lancashire everywhere, or drop it from rewards-terms for consistency.
- **Rewards page link-out destination not working** (Daniel, 3 Jul): signed-in hosted account page shows no points/balance — Customer Account UI Extension may not be installed/active on `senseless-numbing`. Handoff issued to the Senseless App project; blocks the "your balance lives on your account page" promise on `/pages/rewards`.
- **Rewards fast-follow (deferred, needs its own decision):** live-balance teaser on `/pages/rewards` — needs an auth-bridge (storefront lacks hosted-account auth). Not built. Also: an OS-aware mobile-only "get the app" prompt on the Rewards page (flagged, not built).
- **Store province = "England" (should be Lancashire) — UNFIXABLE** via admin UI/API (no county field, no shop-address mutation). Never rendered → harmless. Only Shopify Support can amend.
- **Cross-brand carriers on the OLD London address** (same legal entity, separate gated pass — don't edit from a Senseless session): Totally Numb (store + /about + /terms), MHG Holding Site.
- Header mis-links (pre-existing): "How long it takes to work" / "How long it lasts" in the Application-guides menu still point to `/pages/using-numbing-cream`, not the dedicated `how-long-*` pages.

## Backlog (unchanged)
- ntn write-back wiring · Phase 12 nav/link wiring · Phase 10 photography · optional GPay-at-checkout payment-customization function (Daniel undecided). Launch-gate: **CLEAR**.

## Gotchas
- **Adding another policy page** = (1) `pageCreate` handle + `templateSuffix: policy` + `isPublished`; (2) set `policy.prose_policy_body` (rich_text_field — build via the `RT` HTML→richtext converter in `scripts/policy-metafields.py`, NOT hand-JSON), `policy.see_also` (json `[{label,url}]`, literal strings), `policy.last_updated` (date), optional `policy.faq`; (3) `global.title_tag`/`description_tag` + `seo.hidden=1`; (4) add the handle to `ss_noindex_handles` in `layout/theme.liquid` (deploy). No new template/section needed.
- **Shopify normalizes `rich_text_field` on store** (strips empty `title`/`target` on link nodes) → a byte-compare of sent-vs-stored will differ (~5%); verify **semantically** (node counts + rendered text), not by length.
- `.env` Admin token expires (401s) — run `./scripts/refresh-token.sh` (client-credentials) then `set -a; source .env; set +a` before any Admin-API script. The token has full write scopes (content/pages/navigation/products/themes). The MCP Shopify connector works independently.
- Policies live in **two places**: native shop policies (`/policies/*`, checkout) AND page metafields (`/pages/*`, `policy` namespace). The rewards T&C is metafield-page-only (it's a programme policy, not a checkout policy).
- Footer columns are **Shopify nav menus** (`senseless-footer-{shop,explore,help,company}`), NOT theme code — add/reorder footer links via `menuUpdate`, no deploy. The strict legal bar (Privacy/Terms/Cookie) IS hardcoded in `senseless-footer.liquid` — different tier, don't touch for programme-specific links.
- Reviews-guard: editing `senseless-structured-data.liquid` / product templates / `settings_data.json` needs `deploy.sh --reviews-changed` (rewrites `reviews-guard.lock` — commit it). Policy pages + footer/theme.liquid edits are NOT guarded.
- Canonical registered address string: **`Paddock Business Centre, 2 Paddock Road, Skelmersdale, WN8 9PL`** (rewards-terms §17 additionally carries "Lancashire" — verbatim, see flag above). Store gate: MCP/CLI default is Totally Numb — verify `senseless-numbing.myshopify.com` first. No rollback theme.
