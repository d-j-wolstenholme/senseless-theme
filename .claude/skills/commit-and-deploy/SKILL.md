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

**`main` is the single working branch and `scripts/deploy.sh` deploys to the LIVE theme — verify before every deploy.**

> **COMMIT BEFORE YOU DEPLOY. The order below is load-bearing, not stylistic.**
> Deploying first opens a window where live is ahead of the repo, and anything that interrupts the
> session in that window — a crashed tool call, an API error, a lost connection — leaves the store
> carrying code that exists nowhere in git. That happened on **6 Aug 2026**: an API error landed between
> `deploy.sh` and `git commit`, and the fix was live and uncommitted until a `git status` re-check caught
> it. Commit → push → deploy means the worst case is a commit that hasn't shipped yet, which is visible,
> harmless and trivially re-deployed. **If you have already deployed, commit immediately — do not start
> anything else, and do not trust that you will remember.**

1. Run `git status` to show all changes
2. Ask user to confirm what's being committed
3. **Verify BEFORE deploying (pushes hit live):** `shopify theme check` must be **0 errors**, and render-verify the changed surfaces live (the storefront password is **OFF** — the site has been public since the 7 Jun launch, so anything deployed is immediately visible to customers). Also run the **content lint** (same pre-deploy slot as the Rich Results check): `python3 scripts/content-lint.py` — writes `reports/content-lint-<date>.{csv,md}`. **WARN-only for now (does NOT fail the build):** review BLOCK rows (MHRA/ASA hard-rule phrases) before pushing user-facing copy. Add `--first-party` to report Senseless-authored copy only (excludes Horizon vendor files — locales, blocks, vendor sections/snippets — writes `…-first-party.{csv,md}`). To make compliance BLOCKs gate the deploy later, run `python3 scripts/content-lint.py --fail-on-block` (exits 2 on any BLOCK).
4. Stage all changes: `git add .`
5. Commit with the provided message
6. Push to origin **main**:
   ```
   git push origin main
   ```
7. If theme files changed, deploy with **`scripts/deploy.sh` — never raw `shopify theme push`** (the script owns token refresh, `--allow-live`, scoped `--only`, and the reviews guard; see `.claude/rules/deploy-and-store.md`). **Run it under `bash`:**
   ```
   bash -c './scripts/deploy.sh <files>'          # add --reviews-changed if a guard file changed
   ```
   ⚠️ **zsh does not word-split an unquoted variable.** `./scripts/deploy.sh $FILES` under zsh passes every path as ONE `--only` argument; deploy.sh prints **"deploy: success"** and pushes **nothing**. This happened on 6 Aug 2026 with 25 templates. Always pass paths literally or run under bash, and always verify per file afterwards.
   Then re-verify per file via Asset-API compare — the combined push has silently skipped template JSON before:
   ```
   # for each deployed path: GET /admin/api/2024-10/themes/199324434780/assets.json?asset[key]=<path>
   # compare parsed JSON (strip the leading /* */ header, normalise \/ escaping) against the local file
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
