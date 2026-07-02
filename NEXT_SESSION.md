# Next session — Senseless (Canon v2.15)

Read `CLAUDE.md` → run `scripts/reconcile.sh` → read the Project Instance + State Surface first.

## Done last session (2026-07-01, MacBook Pro)
- **Local = live verified** (full semantic diff): 556/556 theme files identical — repo `f31831e` = origin/main = live `#199324434780`. Only diffs = Shopify pull-header/key-order noise + local-only image-pipeline dirs. CLI token was stale (reconcile theme-list failure) — `refresh-token.sh` fixed it.
- **Spray size 100ml → 35ml sitewide** (Daniel's decision 2026-07-01; supersedes "canonical spray = 100ml" in all pre-July docs). Commit `669bd87`, deployed + verified:
  - Theme: 3 spray PDP Key Facts ("Available in 35ml."), spray-collection FAQ q5 (also dropped "larger-area and" — **flag for Daniel's copy review**), `scripts/build-bundles.py`.
  - Admin API: 3 spray variant option values renamed (titles now "35ml"), 5 bundle `senseless.bundle_contents` metafields, 3 spray image alt texts.
  - Compliance-check PASS · theme-check 0 errors · deploy.sh `--reviews-changed` (lock rewritten + committed) · guard markers 5/5 · live curl 0×"100ml" across spray PDPs/collection/bundles.

- **Mobile cart/payment fixes** (commit `94ae8fb`, deployed + WebKit-verified): wallet OS-gating via new `senseless-wallet-gate` snippet (Apple devices lose the redundant GPay button; /checkout itself is Shopify-controlled — not theme-modifiable); drawer line-item grid hardened (display:contents→block, iOS title-drop); close ✕ inset fixed; PDP "More payment options" one centred line.
- **PDP quantity selector added + all steppers unified** (`f7fefbc`): PDPs had no qty selector; added labelled row on `senseless-product-hero` (verified: qty 2 lands in cart); cart page + drawer steppers restyled to quick-add style (14px / #E5E2DC / white).
- **Tier language: Advanced ≠ "everyday"** (`5e851a4`): canon = Clinical everyday-default · Advanced consumer-upgrade. Audited theme + admin (4-agent sweep, exhaustive); 6 instances fixed (System card, how-to-apply, COMPLIANCE.md table, 3 collection SEO metas via API); Clinical "everyday" claims kept. Flags for Daniel: COMPLIANCE.md Clinical approved-phrase undersells the default positioning; archived Content Standards still has the old tier table.

## Next task (pick from Work Items)
- **Close the write-back loop:** wire `reconcile.sh` + Stop hook to live Notion via `ntn` CLI (currently session writes sync-status via MCP).
- Build queue (State Surface): Phase 12 nav/link wiring · Phase 13 audit · Phase 14 launch · Phase 10 photography.

## Gotchas
- Historical build-reports + DECISIONS-LOG still say spray = 100ml **by design** (records not rewritten, Daniel's scope call). Don't "fix" them back — admin variants are size truth (35ml).
- Spray `.jpg` stills may show non-35ml packaging on the label; alt text now says 35ml. Photography swap = separate work item if the render mismatches.
- Verify-store gate is real: MCP/CLI default is **Totally Numb** — `get-shop-info` must equal `senseless-numbing.myshopify.com` or STOP.
- Store timezone still **EDT** (fix outstanding, Daniel/admin). Foaming Cleanser = **35ml**. No rollback theme (Horizon deleted).
