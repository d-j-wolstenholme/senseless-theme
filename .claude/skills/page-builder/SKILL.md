---
name: page-builder
description: Use this skill for end-to-end page builds. Chains content-brief → create-section (for each section in the brief) → seo-meta → image-process (for each image in the brief) → metafield-populator (for any page-level metafields) → commit-and-deploy. Trigger phrases include "build the [page] page", "build me [page]", "/build-page [page name]". This is the main workflow skill for the build phase.
---

# Page Builder

## When to Use

- User wants a complete page built from a Notion brief
- /build-page slash command invoked
- Multi-step page work where running skills individually would be slower

## Inputs

- **Page name or URL slug** (required) — what to build

## Process

1. Run `content-brief` to load the brief for the page
2. For each section listed in the brief:
   - Run `create-section` with the section's content
3. Run `seo-meta` to generate meta title and description
4. For each image in the brief:
   - Confirm source file is in `assets/images/inbox/`
   - Run `image-process` with brief-supplied name/type/alt
5. If page has metafields specified, run `metafield-populator`
6. Update the page template/JSON to assemble the sections in order
7. Run `compliance-check` one final time on the assembled page output
8. Optionally run `/session-end` to commit and deploy

## Outputs

- All sections built and registered
- Images processed and integrated
- Meta tags set
- Page template assembled
- Build report covering all sub-skill outputs

## Constraints

- Never start without a confirmed brief
- Confirm with user before each major step (sections built, before image upload, before deploy)
- If any sub-skill fails, halt and report — don't continue silently
