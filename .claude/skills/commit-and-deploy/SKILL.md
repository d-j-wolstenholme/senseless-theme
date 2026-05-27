---
name: commit-and-deploy
description: Use this skill at the end of every Claude Code session. Stages all changes, commits to GitHub with a descriptive message, pushes to origin/main, deploys to Shopify dev theme via Shopify CLI, and generates the structured build report. This is the enforced session-end protocol — every session ends with this skill. Trigger by /session-end or "end session" or "commit and deploy".
---

# Commit & Deploy

## When to Use

- Every session end. No exceptions.
- Triggered by `/session-end` slash command.

## Inputs

- **Commit message** (required) — descriptive, imperative mood
- **Skip Shopify push** (optional) — if no theme files were changed

## Process

1. Run `git status` to show all changes
2. Ask user to confirm what's being committed
3. Stage all changes: `git add .`
4. Commit with the provided message
5. Push to origin: `git push origin main`
6. If theme files changed, push to Shopify dev theme:
   ```
   shopify theme push --store senseless-tattooing.myshopify.com --theme [dev-theme-id]
   ```
7. Run drift-check skill to surface any open discrepancies
8. Generate the build report (full format below)
9. Display report ready to paste into planning chat

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

- Git commit + push
- Shopify dev theme push (if applicable)
- Build report (paste into planning chat)

## Constraints

- Never skip the build report.
- Never push to live theme (only dev).
- If any drift-check warnings exist, flag in the report but don't block the push.
