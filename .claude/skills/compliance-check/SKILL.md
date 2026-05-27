---
name: compliance-check
description: Use this skill before any user-facing copy is shipped, committed, or used in a section schema default. Runs draft copy against the UK compliance banned phrases list from docs/COMPLIANCE.md and suggests approved alternatives from the don't/do translation table. Trigger automatically before output of any copy intended for headlines, body text, alt text, meta tags, or marketing assets. Non-negotiable check — UK compliance is mandatory.
---

# Compliance Check

## When to Use

- Before any copy is added to a section, page, alt text, or meta
- Before any marketing message is composed
- When the user pastes copy for review
- Inside /build-page workflow before deployment

## Inputs

- **Draft copy** (any text intended for user-facing display)

## Process

1. Read `docs/COMPLIANCE.md` for banned phrases and approved patterns
2. Scan input copy for hard-rule violations
3. For each violation:
   - Flag the exact phrase
   - Quote the rule it breaks
   - Suggest one or more approved alternatives from the don't/do table
4. Report scan results:
   - ✓ PASS — no violations found
   - ⚠ WARN — soft concerns (e.g. tone too close to a hard rule)
   - ✗ FAIL — explicit violations, must rewrite

## Outputs

- Scan result with violation list and suggested rewrites
- Build report line: "Compliance check on [page/asset]: PASS/WARN/FAIL"

## Constraints

- Never override a FAIL. Rewrite is mandatory.
- Don't ship copy without running this skill at least once.
- If unsure whether a phrase passes, default to flagging it for review.
