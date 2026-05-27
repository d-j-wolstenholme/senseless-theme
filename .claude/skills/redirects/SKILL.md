---
name: redirects
description: Use this skill to manage Shopify 301 redirects via the Admin API. Primarily used at launch for migrating old URLs to new ones. Trigger phrases include "set up redirects", "create redirect from X to Y", "bulk redirects for launch".
---

# Redirects

## When to Use

- Migrating old URLs to new ones at launch
- Adding individual redirect for an old URL
- Bulk migration of legacy paths

## Inputs

- **Operation** — create / list / delete / bulk-import
- **From path** — e.g. `/collections/tattoo-numbing-cream`
- **To path** — e.g. `/collections/aesthetic-numbing-cream`
- **CSV file** (for bulk) — two columns: from,to

## Process

1. Authenticate using `SHOPIFY_ACCESS_TOKEN`
2. For create: use `urlRedirectCreate` mutation
3. For bulk: parse CSV, create redirects in batches, log progress
4. Verify each redirect by testing the URL after creation (optional)
5. Log all bulk operations to DECISIONS-LOG.md

## Outputs

- Confirmation per redirect created
- Build report with totals

## Constraints

- Avoid redirect chains — always redirect to final destination
- Never redirect a page to itself
- Keep a CSV record of all redirects in `docs/redirects-log.csv` for audit
