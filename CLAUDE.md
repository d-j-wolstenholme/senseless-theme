# Senseless — Claude Code Rules

You are Claude Code working on the Senseless Shopify theme. Read this file in full at the start of every session. The four docs (`docs/BRAND.md`, `docs/COMPLIANCE.md`, `docs/SECTIONS.md`, `docs/ARCHITECTURE.md`) and the `DECISIONS-LOG.md` mirror at the repo root are also canonical and must be loaded before any work begins.

## Project Overview

Senseless is a UK-based topical preparation brand for aesthetic and cosmetic procedures. Female-leaning audience. Three strength tiers (Clinical → Advanced → Professional). Four formats (Cream 30g, Cream 10g, Gel 35ml, Spray). 10 SKUs at launch. Manufactured by Matrix Health Group Ltd. Brand colour `#6B3FA0`.

This repo is the new build, started from latest Horizon as a clean base. Old theme is reference only.

## Hard Rules

1. **Always ask which machine I'm on at session start.** Mac mini or MacBook Pro. Log it in the session report.
2. **Always run `/session-start` before any work.** Pulls latest, runs drift check, fetches Notion priorities.
3. **Always run `/session-end` before closing.** Commits and pushes to both GitHub and Shopify dev theme. No exceptions.
4. **Never push to the live theme.** Build environment is the Shopify dev theme. Live theme is only switched at launch.
5. **Never edit BRAND.md, COMPLIANCE.md, ARCHITECTURE.md silently.** When a decision changes the design system, compliance rules, or architecture, update the relevant doc in the same session and surface the update in the build report.
6. **Never default silently when ambiguous.** If a task isn't fully resolved by CLAUDE.md, the four docs, or `DECISIONS-LOG.md`, ask me before proceeding. Or proceed with an explicit assumption logged in the build report's Open Questions section.
7. **Always use the `senseless-` prefix on new section files.** No exceptions.
8. **Always run `compliance-check` before producing user-facing copy.** UK compliance is non-negotiable.
9. **Always log strategic decisions in `DECISIONS-LOG.md`** with ISO 8601 timestamp in BST. Surface them in the build report so the planning chat (Claude) can mirror them to Notion.
10. **Never put credentials in committed files.** `.env` is gitignored. Tokens stay in `.env` only.
11. **Theme deploys go through Shopify CLI only** (`shopify theme push --store $SHOPIFY_STORE --theme $SHOPIFY_DEV_THEME_ID`). **Always pass `--store senseless-tattooing.myshopify.com`** — the CLI's default store is a different account (Totally Numb, `matrix-group-totally-numb`), so omitting `--store` pushes to the wrong store. Keep theme deploys in the CLI; never use the API token for theme push operations. The API token is for products, collections, metafields, files, and content only. Canonical Senseless dev theme: "Senseless Dev" `#196680057167` (unpublished).
12. **All day-to-day work happens on the `dev` branch.** `main` is stable and merged into only at sprint/milestone completion. Never commit directly to `main` during build sessions.

## Branching Strategy

- **`dev`** — the default working branch. All day-to-day build work happens here.
- **`main`** — stable. Merged into only at sprint/milestone completion. Never commit directly to `main` during build sessions.
- `/session-start` checks out `dev`, pulls latest (`git pull origin dev`), then runs drift-check.
- `/session-end` commits to `dev` and pushes to `dev`, then generates the build report.
- Feature/fix branches (`feature/<desc>`, `fix/<desc>`) branch off `dev` and merge back into `dev`.

## Naming Conventions

- **Section files:** `senseless-<purpose>.liquid` in `/sections/` (e.g. `senseless-home-hero.liquid`)
- **Snippet files:** `senseless-<purpose>.liquid` in `/snippets/`
- **Image files:** `senseless-[page-or-context]-[descriptor]` (e.g. `senseless-home-hero-products`). See `docs/BRAND.md` Image Pipeline section.
- **Branch names:** `feature/<short-description>`, `fix/<short-description>`
- **Commit messages:** Imperative mood, short, descriptive (e.g. `Add senseless-home-hero section`)

## Design Tokens

See `docs/BRAND.md` for the canonical design system. Quick reference:

- **Brand purple (`--brand-primary`):** `#6B3FA0`
- **Background canvas (`--bg-canvas`):** `#f7f7f5`
- **Background surface (`--bg-surface`):** `#ffffff`
- **Text primary (`--text-primary`):** `#1A1816` — headings
- **Text body (`--text-body`):** `#2B2730` — running body
- **Text secondary (`--text-secondary`):** `#5C5853` — leads, captions
- **Text muted (`--text-muted`):** `#8E8A82`
- **Border subtle:** `#E5E2DC`
- **Typeface:** Montserrat, self-hosted via Shopify font CDN (no Google Fonts requests). **Headings (reweight 2026-06-02, Strand 1): display/H1 + H2 = 400** (tracking -0.02em; line-height 1.06/1.08 H1, 1.1/1.12 H2); **H3 / card titles = 600**; body 400; eyebrow/labels 600; **italic accent = 500** (`.ss-accent` / `.t-em` — one emphasis word per head, same colour as the head, never the keyword). Type scale is fluid `clamp()` — see `snippets/senseless-typography.liquid` + `docs/BRAND.md`.
- **Button radius:** 14px
- **Card radius:** 4px
- **Page width:** narrow

## Skills Available

In `.claude/skills/`:

| Skill | Purpose |
|---|---|
| create-section | Generate a Liquid section + schema using brand tokens |
| content-brief | Pull a content brief from Notion's Master Page Database |
| compliance-check | Run draft copy against banned phrases, suggest alternatives |
| seo-meta | Generate compliant meta title (≤60 chars) and description (≤155 chars) |
| commit-and-deploy | Session-end: commit, push to GitHub, push to Shopify dev theme, build report |
| image-process | Run the image pipeline end-to-end (compress → upload → manifest → integrate) |
| metafield-populator | Create/update Shopify metafield definitions and values via API |
| page-builder | Chain content-brief → create-section → seo-meta → image-process |
| redirects | Manage 301 redirects via Shopify API |
| drift-check | Compare code against docs and DECISIONS-LOG, surface discrepancies |

## Slash Commands

In `.claude/commands/`:

- `/session-start` — Pull latest, drift check, fetch today's Notion priorities
- `/session-end` — Run commit-and-deploy
- `/build-page` — End-to-end page build (uses page-builder skill)
- `/drift-check` — On-demand sync audit

## Build Report Format

Every session ends with a build report containing:

1. **Machine** — Which machine this session was on
2. **Session duration** — Approximate hours
3. **Tasks completed** — What was done
4. **Docs updated** — Which of CLAUDE.md / BRAND.md / COMPLIANCE.md / SECTIONS.md / ARCHITECTURE.md / DECISIONS-LOG.md were changed
5. **Decisions logged this session** — Operational decisions made
6. **Open questions** — Anything ambiguous, unresolved, or needs my decision
7. **To push to Notion** — Strategic items to mirror to the Notion Decisions Log
8. **Sync status** — Pass/Warn flags from drift check
9. **Next steps** — Suggested next session priorities

Paste this report into the planning chat (Claude conversation) after every session.

## What NOT to Touch

- The live theme on Shopify (build environment is the dev theme)
- `.env` file contents (set up once, never committed)
- The four `[ARCHIVED]` or `[DELETE]` Notion pages
- Old Senseless-Horizon theme files (reference only — don't pull from them)

## Source of Truth

- **Strategy:** Notion Senseless — Site Build OS (parent page: `https://www.notion.so/36c58bc375ea812c9682ca2aa0bc1950`)
- **Decisions:** Notion Decisions Log (Vol 1 active: `https://www.notion.so/36d58bc375ea81708d1ac0fe0724d445`)
- **Code:** This repo + GitHub `d-j-wolstenholme/senseless-theme`
- **Live state:** Shopify Partners account `senseless-tattooing.myshopify.com`
- **Local mirror:** `DECISIONS-LOG.md` at repo root (active volume only)

## References

- **Site-wide Standards (Notion):** consolidated human-facing index of site-wide standards — `https://www.notion.so/36f58bc375ea8100bc2af19a9dd3747d`. This is a **pointer only**. Canonical values live in the Strands and in this repo's `BRAND.md` / `CLAUDE.md` / `COMPLIANCE.md`. If they ever conflict, the repo docs and Strands win.
