---
name: commit-and-deploy
description: Use this skill at the end of every Claude Code session. Stages all changes, commits to GitHub on `main`, pushes to origin/main, deploys to the Shopify LIVE theme (#199324434780 on senseless-numbing.myshopify.com) via Shopify CLI, and generates the structured build report. As of 7 June 2026 `main` is the single working branch and pushes deploy directly to the live theme — verify (theme-check 0 + render) BEFORE pushing. This is the enforced session-end protocol — every session ends with this skill. Trigger by /session-end or "end session" or "commit and deploy".
---

# Commit & Deploy

## When to Use

- Every session end. No exceptions.
- Triggered by `/session-end` slash command.

## Inputs

- **Commit message** (required) — descriptive, imperative mood
- **Skip Shopify push** (optional) — if no theme files were changed

## Process

**`main` is the single working branch and pushes deploy to the LIVE theme — verify before every push.**

1. Run `git status` to show all changes
2. Ask user to confirm what's being committed
3. **Verify BEFORE deploying (pushes hit live):** `shopify theme check` must be **0 errors**, and render-verify the changed surfaces live (the storefront password is **OFF** — the site has been public since the 7 Jun launch, so anything deployed is immediately visible to customers). Also run the **content lint** (same pre-deploy slot as the Rich Results check): `python3 scripts/content-lint.py` — writes `reports/content-lint-<date>.{csv,md}`. **WARN-only for now (does NOT fail the build):** review BLOCK rows (MHRA/ASA hard-rule phrases) before pushing user-facing copy. Add `--first-party` to report Senseless-authored copy only (excludes Horizon vendor files — locales, blocks, vendor sections/snippets — writes `…-first-party.{csv,md}`). To make compliance BLOCKs gate the deploy later, run `python3 scripts/content-lint.py --fail-on-block` (exits 2 on any BLOCK).
4. Stage all changes: `git add .`
5. Commit with the provided message
6. Push to origin **main**:
   ```
   git push origin main
   ```
7. If theme files changed, deploy to the **LIVE** theme via Shopify CLI — **`--allow-live` is required** (the theme is published, so the CLI refuses without it). Push changed files with `--only` and re-verify via Asset-API diff (the combined push has silently skipped template JSON before):
   ```
   shopify theme push --store senseless-numbing.myshopify.com --theme 199324434780 --allow-live --only <files>
   ```
8. Run drift-check skill to surface any open discrepancies
9. Generate the build report (full format below)
10. Display report ready to paste into planning chat

## Build Report Format

```
# Senseless Build Report — [YYYY-MM-DD HH:MM BST]

**Machine:** [Mac mini | MacBook Pro]
**Session duration:** ~[X hours]
**Commit:** [hash] — "[commit message]"

## Tasks Completed
- [bullet list]

## Docs Updated
- [list of files in docs/ or root that changed]

## Decisions Logged This Session
- [list with timestamps]

## Open Questions
- [anything ambiguous or unresolved]

## To Push to Notion
- [strategic items the planning chat should mirror to Notion Decisions Log]

## Sync Status
- ✓/⚠ DECISIONS-LOG.md in sync with last known Notion volume
- ✓/⚠ BRAND.md matches theme tokens
- ✓/⚠ ARCHITECTURE.md aligned with Notion site architecture page
- ✓/⚠ All sections in docs/SECTIONS.md exist as files

## Next Steps
- [suggested priorities for next session]
```

## Outputs

- Git commit + push to `origin/main`
- Shopify **live** theme push (`#199324434780`, `--allow-live`) if theme files changed
- Build report (paste into planning chat)

## Constraints

- Never skip the build report.
- **Deploys hit the LIVE theme** (`#199324434780` on `senseless-numbing.myshopify.com`) — run `shopify theme check` (0 errors) + render-verify the changed surfaces BEFORE deploying. (A `git push` alone does NOT deploy; only `scripts/deploy.sh` does.)
- **The storefront password is OFF and the store is public** (since the 7 Jun launch). There is no password curtain — every deploy is customer-visible the moment it lands. Never turn the password back on as part of session-end.
- `--allow-live` is mandatory on `shopify theme push` (the theme is published); after pushing, Asset-API-verify the changed files (the combined push has silently skipped template JSON).
- If any drift-check warnings exist, flag in the report but don't block the push.
