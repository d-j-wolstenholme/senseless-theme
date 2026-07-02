# Next session — Senseless (Canon v2.15)

Read `CLAUDE.md` → run `scripts/reconcile.sh` → read the Project Instance + State Surface first.

## Done last session (2026-07-02, MacBook Pro)
- **Launch-gate triple (commit `d62cc13`, deployed + live-verified):**
  - **PDP safety warnings BUILT** — new `senseless-safety-warnings` section, copy hardcoded per variant (numbing on 9 SKUs + 5 kits; cleanser/ointment aftercare variants with NO broken-skin line — intended use). Patch-test FAQ line folded in (exactly 1× per PDP live). New `product.vitamin-a-d-ointment.json` + templateSuffix set via API. Work Item → **Built**.
  - **About 'made' fix LIVE** — "Formulated / In the United Kingdom" + "Where is Senseless formulated?"; Compliance Hold → **Cleared**.
  - **Review-card 404 fixed** — re-uploaded the source jpg under the exact old Files name (Judge.me cached URL, ~80 refs healed, HTTP 200).
  - Verified: store gate · compliance PASS · theme-check 0 · guard 5/5 · Asset-API remote diff 14/14 · live curls per-variant.
- **How-to pages rewrite DRAFTED (not deployed)** — full stepped redraft on Work Item 39158bc3-75ea-81e6… (TN-reference method; dedupe: how-to-apply = canonical steps, using = framework). 3 flagged calls incl. thick-vs-thin resolution + removed live "45–60 min" breach. **Awaiting Daniel sign-off.**

## Next Work Item
- **On Daniel's sign-off:** implement the how-to draft in `page.how-to-apply-numbing-cream` + `page.using-numbing-cream` templates + deploy.
- Launch-gate: **MHRA classification is the only open blocker** (Daniel/MHG).
- Backlog: ntn write-back wiring · Phase 12 nav/link wiring · Phase 10 photography · optional GPay-at-checkout payment-customization function (Daniel undecided).

## Gotchas
- Safety-warnings copy is HARDCODED in the section (compliance-locked) — variant select only; don't move copy into editor settings.
- totally-numb.co.uk is password-locked (unlaunched rebuild) — the trading TN site is **totally-numb.com**; almost all its copy breaches Senseless Hard Rules, reference its *structure* only.
- Historical docs still say spray = 100ml by design; admin variants are size truth (35ml). No rollback theme. Store gate: MCP/CLI default is Totally Numb — verify `senseless-numbing.myshopify.com` first.
