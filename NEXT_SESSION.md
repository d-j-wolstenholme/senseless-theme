# Next session — Senseless (Canon v2.19)

Read `CLAUDE.md` → run `scripts/reconcile.sh` → read the Project Instance + State Surface first.

## Done last session (2026-07-03, MacBook Pro — canon re-stamp → v2.19)
- **Repo canon stamp bumped to v2.19**, closing the repo side of the re-stamp. Notion (Project Instance, State Surface, Front Door — Source of Record) was already moved to v2.19 by chat; this session matched the repo. Text/version-label only — **no logic or structure change**.
  - **Front door:** `CLAUDE.md:3` → "Canonical Reference Library v2.19".
  - **Machine-canon layer:** `canon/state.json` `canon_version`; `.claude/schema-contract.json` `canon_version` ×2 (lines 4, 11); `scripts/reconcile.sh` header comment (line 2) + banner (line 19) — all → v2.19.
  - **`.claude/rules/*.md`** carry no version marker — nothing to change.
- **Verified:** the prior canon-version stamp no longer appears in any tracked file (grep-clean); both JSON files parse; `reconcile.sh` prints "Canon v2.19" on both the hardcoded banner (line 19) and the dynamic `state.json` read (line 56) — no split. The only remaining bare `2.17` substrings are non-version data (SVG path coords in `snippets/icon.liquid` + `assets/senseless-logo-header.svg`; audit ID `P2.17` in `docs/AUDIT-2026-06-12.md`) — correctly left untouched.
- **No theme files touched — nothing to deploy.** Staged for the next commit-and-deploy flow (version labels only).
- **Prior work remains live:** how-to Revision 2 (commit `956a55c`) — 2–3mm layer, cling film standard, 45–60 general-guide window (approved directions-for-use carve-out, Decision `39158bc3-75ea-8181`); launch-gate triple (`d62cc13`): PDP safety warnings, About 'made' fix, review-card 404 heal.

## Next Work Item
- Launch-gate: **CLEAR** — MHRA closed 2 Jul (product is a cosmetic; Decision `39158bc3-75ea-8194`). Ongoing duty: keep efficacy/onset/duration claims off brand-authored surfaces (existing Hard Rules).
- Backlog: ntn write-back wiring · Phase 12 nav/link wiring · Phase 10 photography · optional GPay-at-checkout payment-customization function (Daniel undecided).

## Gotchas
- Canon is uniform at **v2.19** across front door + machine-canon layer + Notion — no split. `reconcile.sh` banner prints "Canon v2.19".
- This was a label-only bump of two minor versions to v2.19; no v2.18 intermediate stamp exists in the repo — the previous repo stamp jumped straight to v2.19 to match Notion.
- Safety-warnings copy is HARDCODED in the section (compliance-locked) — variant select only; don't move copy into editor settings.
- totally-numb.co.uk is password-locked (unlaunched rebuild) — the trading TN site is **totally-numb.com**; almost all its copy breaches Senseless Hard Rules, reference its *structure* only.
- Historical docs still say spray = 100ml by design; admin variants are size truth (35ml). No rollback theme. Store gate: MCP/CLI default is Totally Numb — verify `senseless-numbing.myshopify.com` first.
