---
name: create-section
description: Use this skill when the user asks to create, build, or add a new Shopify section to the Senseless theme. Generates a complete Liquid section file with schema, scoped CSS, and editor-controlled settings using brand tokens from docs/BRAND.md. Trigger phrases include "create a section", "build [section name]", "new section for [page]". Outputs the section file to /sections/ with the senseless- prefix, registers it in the relevant template if applicable, and appends an entry to docs/SECTIONS.md.
---

# Create Section

## When to Use

- User asks to create a new Shopify section
- A content brief specifies a section that doesn't exist yet
- /build-page workflow requires a section that isn't in docs/SECTIONS.md

## Inputs

- **Section name** (required) — what the section is for (e.g. "home hero", "product system")
- **Brief** (optional) — content brief from Notion or inline description
- **Page** (optional) — which page/template will use the section

## Process

1. Read `docs/BRAND.md` for design tokens (colours, typography, spacing)
2. Read `docs/COMPLIANCE.md` for copy rules
3. Read `docs/SECTIONS.md` for existing sections (avoid duplicating)
4. Construct the file name: `sections/senseless-<purpose>.liquid`
5. Generate the section with:
   - **Liquid template** using brand tokens, semantic HTML, and accessible markup
   - **Scoped CSS** inside the section (no global styles unless agreed)
   - **Schema** with editor-controlled settings for every headline, body copy, image picker, CTA label and URL — no hard-coded copy
   - **Name** in schema prefixed `Senseless —` for clarity in the editor
   - **Class** `senseless-section` on the root for shared targeting
6. If user-facing copy is included, run `compliance-check` skill on it first
7. Append entry to `docs/SECTIONS.md` with: file name, purpose, used on (if known), today's date
8. Show me the generated file before saving — confirm before write

## Outputs

- New file at `sections/senseless-<purpose>.liquid`
- Updated `docs/SECTIONS.md`
- Build report line: "Created section senseless-<purpose>"

## Examples

User: "Create a hero section for the homepage"
→ Section name: home hero
→ File: `sections/senseless-home-hero.liquid`
→ Brief: Pull from Notion Homepage brief if available, or ask for content brief

User: "Build the trust bar"
→ Section name: trust bar
→ File: `sections/senseless-trust-bar.liquid`

## Constraints

- Never hard-code copy. Everything in schema settings.
- Use brand tokens, not raw hex/px values.
- Mobile breakpoints at 989px and 749px.
- Accessibility: semantic HTML, alt text required for image settings, ARIA where needed.
- Compliance: any default copy in schema must pass `compliance-check`.
