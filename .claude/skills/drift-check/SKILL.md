---
name: drift-check
description: Use this skill to surface discrepancies between the live theme code, the four docs (BRAND.md, COMPLIANCE.md, SECTIONS.md, ARCHITECTURE.md), and DECISIONS-LOG.md. Run automatically at /session-start, included in /session-end build report, and on-demand via /drift-check. Trigger phrases include "drift check", "are we in sync", "audit the project state".
---

# Drift Check

## When to Use

- At /session-start (automatic)
- At /session-end inside commit-and-deploy build report (automatic)
- On-demand via /drift-check when something feels off

## Process

1. Read CLAUDE.md, BRAND.md, COMPLIANCE.md, SECTIONS.md, ARCHITECTURE.md, DECISIONS-LOG.md
2. Scan theme code for:
   - Uses of colour values not declared in BRAND.md
   - Uses of font-family values not declared in BRAND.md
   - Section files not listed in SECTIONS.md
   - Section files using `senseless-` prefix correctly
3. Compare DECISIONS-LOG.md timestamps to today — if oldest active entry is >7 days, flag as "stale, pull latest from Notion"
4. Cross-check ARCHITECTURE.md page list against actual templates and product/collection files where possible
5. Output drift report:
   - ✓ Pass items
   - ⚠ Warn items (with details)
   - ✗ Fail items (must resolve)

## Outputs

- Drift report
- Build report addendum if run during session-end

## Constraints

- Doesn't auto-fix — only surfaces. Fixes are explicit human decisions.
- Don't include false positives — only flag when the rule is clear.
