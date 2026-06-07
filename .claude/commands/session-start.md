# /session-start

Run at the beginning of every Claude Code session before any work begins.

## Steps

1. **Ask which machine I'm on:** Mac mini or MacBook Pro? Log the answer.
2. **Check out main and pull latest:** `git checkout main && git pull origin main`. `main` is the single working branch and deploys to the live theme (the `dev`-staging model was retired 7 June 2026).
3. **Check status:** `git status` — confirm clean working tree
4. **Load context:** Read CLAUDE.md, BRAND.md, COMPLIANCE.md, SECTIONS.md, ARCHITECTURE.md, DECISIONS-LOG.md
5. **Run drift-check skill** — surface any discrepancies
6. **Ask me:** "What are we working on today?" — and offer to load a content brief if a page name is given.

## Output

Session start summary:
- Machine: [Mac mini | MacBook Pro]
- Branch: main
- Latest pulled: [commit hash]
- Drift status: ✓ / ⚠ / ✗
- Today's intended focus: [what I tell you]
