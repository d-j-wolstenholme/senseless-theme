# Next session — Senseless (Canon v2.15)

Read `CLAUDE.md` → run `scripts/reconcile.sh` → read the Project Instance + State Surface first.

## Done last session (2026-07-02, MacBook Pro)
- **Launch-gate triple (commit `d62cc13`, deployed + live-verified):**
  - **PDP safety warnings BUILT** — new `senseless-safety-warnings` section, copy hardcoded per variant (numbing on 9 SKUs + 5 kits; cleanser/ointment aftercare variants with NO broken-skin line — intended use). Patch-test FAQ line folded in (exactly 1× per PDP live). New `product.vitamin-a-d-ointment.json` + templateSuffix set via API. Work Item → **Built**.
  - **About 'made' fix LIVE** — "Formulated / In the United Kingdom" + "Where is Senseless formulated?"; Compliance Hold → **Cleared**.
  - **Review-card 404 fixed** — re-uploaded the source jpg under the exact old Files name (Judge.me cached URL, ~80 refs healed, HTTP 200).
  - Verified: store gate · compliance PASS · theme-check 0 · guard 5/5 · Asset-API remote diff 14/14 · live curls per-variant.
- **How-to REVISION 2 LIVE** (commit `956a55c`) — Daniel rejected v1 as too generalized; v2 restores the specifics from the new TN co.uk guide in Senseless voice: 2–3mm layer, cling film standard (sealed edges), 45–60 general-guide window (**approved directions-for-use, Decision 39158bc3-75ea-8181 — carve-out encoded in compliance rules/doc/skill, do not re-flag**), gel band, checklist, night-before FAQ. Scope guards held: using-page + PDPs untouched.
- **How-to v1 rewrite** (commit `686a213`, superseded on how-to-apply; still current on using-page) — canonical steps on how-to-apply (5 cream/gel + 4 spray, patch-test lead), using page deduped to framework (routine one-liner + patch-test band; 45–60min line removed from this page ONLY). **Scope guard honoured: PDPs untouched** (45–60 line stays there per Decision 39158bc3-75ea-81f7). About tidy: "formulated for". Work Item → Built.

## Next Work Item
- Launch-gate: **CLEAR** — MHRA closed 2 Jul (product is a cosmetic; Decision 39158bc3-75ea-8194). Launch may proceed 3 Jul. Ongoing duty: keep efficacy/onset/duration claims off brand-authored surfaces (existing Hard Rules).
- Backlog: ntn write-back wiring · Phase 12 nav/link wiring · Phase 10 photography · optional GPay-at-checkout payment-customization function (Daniel undecided).

## Gotchas
- Safety-warnings copy is HARDCODED in the section (compliance-locked) — variant select only; don't move copy into editor settings.
- totally-numb.co.uk is password-locked (unlaunched rebuild) — the trading TN site is **totally-numb.com**; almost all its copy breaches Senseless Hard Rules, reference its *structure* only.
- Historical docs still say spray = 100ml by design; admin variants are size truth (35ml). No rollback theme. Store gate: MCP/CLI default is Totally Numb — verify `senseless-numbing.myshopify.com` first.
