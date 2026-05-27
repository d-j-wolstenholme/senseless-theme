---
name: content-brief
description: Use this skill when the user asks for the content brief for a specific page, or when /build-page needs the brief as input. Pulls structured content brief from the Notion Master Page Database — primary/secondary keywords, meta title, meta description, section breakdown, cluster, priority, and compliance reminders. Trigger phrases include "brief for [page]", "what's the brief for [page]", "pull the homepage brief".
---

# Content Brief

## When to Use

- User asks for the brief for a specific page
- /build-page workflow needs the brief as input
- Compliance-check or seo-meta skills need page context

## Inputs

- **Page name or URL slug** (required) — e.g. "Homepage", "Numbing Cream for Lip Fillers", "/collections/aesthetic-numbing-cream"

## Process

1. Note: Direct Notion API access is not available from CC at present. Brief retrieval is currently a manual paste from the planning chat.
2. Ask the user to paste the brief from Notion if not already in the session context.
3. Parse the brief into structured fields: primary keyword, secondary keywords, meta title, meta description, page cluster, priority, section breakdown.
4. Confirm parsing back to the user before downstream use.

## Outputs

- Structured brief object stored in session context for downstream skills (create-section, seo-meta, image-process)
- Build report line: "Brief loaded for [page name]"

## Future Enhancement

When the Notion MCP becomes available inside CC sessions, this skill will auto-pull from the Master Page Database. Until then, planning chat (Claude) provides the brief content.

## Constraints

- Always verify brief is current before proceeding (check against Notion in planning chat at /session-end)
