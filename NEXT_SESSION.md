# Next session — Senseless (Canon v2.15)

Read `CLAUDE.md` → run `scripts/reconcile.sh` → read the Project Instance + State Surface first.

## Done last session (2026-06-29)
- **Bootstrap-parity (Decision #41).** Authored the Claude Code enforcement bundle, superseding the pre-migration `CLAUDE.md`:
  - `CLAUDE.md` (thin front door, references Notion by id), `.claude/settings.json` (3 hooks), `scripts/reconcile.sh`, `.claude/schema-contract.json` (12 DBs + 3 pages, fields harvested live), plus `.claude/hooks/{guard-write,session-stop}.py`, `.claude/rules/{deploy-and-store,compliance}.md`, `canon/state.json`.
- Wrote back: Project Instance §7 (schema-contract path), Session Log row, State Surface sync-status = "CC bundle present + verified".
- Repo-only — **nothing deployed** to the theme. `reconcile.sh` verified live: store `senseless-numbing.myshopify.com`, MAIN theme `#199324434780`.

## Next task (pick from Work Items)
- **Close the write-back loop:** wire `reconcile.sh` + the Stop hook to live Notion via the `ntn` CLI so sync-status writes back automatically (currently the session writes it via MCP). This is the scaffold's "next wire-up".
- Build queue (State Surface): Phase 12 nav/link wiring · Phase 13 audit · Phase 14 launch · Phase 10 photography.

## Gotchas
- `.claude/settings.json` hooks activate **next** session (loaded at session start). The `PreToolUse` guard fails-closed only on a *corrupt* schema-contract; it allows writes when the contract is absent.
- Verify-store gate is real: Shopify MCP/CLI default is **Totally Numb** — `get-shop-info` must equal `senseless-numbing.myshopify.com` or STOP.
- Store timezone is misconfigured to **EDT** (fix outstanding, Daniel/admin).
- Foaming Cleanser = **35ml**; Horizon `#199321977180` is **deleted** (no rollback theme).
