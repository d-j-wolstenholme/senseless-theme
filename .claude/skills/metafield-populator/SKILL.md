---
name: metafield-populator
description: Use this skill to create or update Shopify metafield definitions and values via the Admin API. Handles bulk operations across products, collections, and pages. Trigger phrases include "set up metafields", "populate metafields", "create metafield definitions for [resource]". Use during theme setup and for bulk content population from the Master Page Database.
---

# Metafield Populator

## When to Use

- Setting up the new theme's metafield definitions
- Bulk populating metafield values from Notion's Master Page Database
- Migrating metafield data from old structure to new

## Inputs

- **Operation type** — create-definition / set-value / bulk-set / list / delete-definition
- **Resource type** — products / collections / pages / blogs / articles
- **Namespace and key** — e.g. `senseless.hero_image`
- **Value type** — single_line_text / multi_line_text / rich_text / number / boolean / file_reference / etc.
- **Values payload** — for bulk operations, structured data with resource IDs and values

## Process

1. Authenticate using `SHOPIFY_ACCESS_TOKEN` from `.env`
2. For definition creation: use `metafieldDefinitionCreate` mutation
3. For value setting: use `metafieldsSet` mutation (supports up to 25 metafields per call)
4. For bulk: chunk into batches of 25, call mutation per batch, log progress
5. On success: log to `DECISIONS-LOG.md` if structural change (new namespace)
6. On failure: surface error in build report, don't retry silently

## Outputs

- Confirmation per metafield set/created
- Build report line: "Metafield operation: [count] [resource type] processed"

## Constraints

- Never operate on the live theme's data without explicit confirmation
- Always log new namespaces to DECISIONS-LOG.md
- Rate limit: max 25 metafields per API call (Shopify limit)
- Keep namespace consistent: `senseless.*` for all custom metafields
