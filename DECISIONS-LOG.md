# Senseless — Decisions Log (Local Mirror)

**Mirrors the active volume of the Notion Decisions Log.**
Active volume: Vol 1 — May 2026
Notion source: https://www.notion.so/36d58bc375ea81708d1ac0fe0724d445

Newest at top. ISO 8601 timestamps in BST.

When this file is older than 24 hours, run `/drift-check` to surface any drift between this local mirror and the canonical Notion log.

---

### 2026-05-28 14:30 BST
**Decision:** Homepage built — 5 reusable sections (`senseless-hero-brand-led`, `senseless-trio-card-row`, `senseless-image-text-band`, `senseless-trust-bar`, `senseless-newsletter-signup`) + `templates/index.json` wiring all 8 homepage instances, copy populated verbatim from the audited Notion brief, all editable via theme editor. **Critical correction — dev theme target:** the Shopify CLI's default store is `matrix-group-totally-numb` (Totally Numb), and theme `#193366131072` belonged to that store, not Senseless. A first push accidentally landed there. Created a new unpublished theme **"Senseless Dev" `#196680057167`** on `senseless-tattooing.myshopify.com` — now the canonical Senseless dev theme. `.env` `SHOPIFY_DEV_THEME_ID` updated to `196680057167`; CLAUDE.md hard rule 11 updated to always pass `--store senseless-tattooing.myshopify.com`.

### 2026-05-28 13:45 BST
**Decision:** Three bootstrap open items resolved. (1) Dangling symlink `.cursor/skills/accessibility` (pointed to a non-existent `.claude/skills/accessibility` target that never came across in the clean Horizon build) deleted. (2) Theme-deploy ownership fixed: theme deploys go through Shopify CLI only (`shopify theme push --theme $SHOPIFY_DEV_THEME_ID`); the client_credentials API token (`shpca_`) cannot see CLI dev themes and is used only for products, collections, metafields, files, and content. (3) Branching strategy adopted: all day-to-day build work happens on `dev`; `main` is stable and merged into only at sprint/milestone completion; never commit directly to `main` during build sessions. `/session-start` checks out `dev` and pulls; `/session-end` commits and pushes to `dev`. Encoded in CLAUDE.md (hard rules 11–12 + Branching Strategy section) and the session-start/session-end command docs.

### 2026-05-27 09:00 BST
**Decision:** Mac mini directory wiped, GitHub repo history wiped, fresh clone of latest Horizon theme initialised, full project scaffolding created (10 skills, 4 slash commands, 4 docs, CLAUDE.md, image pipeline, .env.example, .gitignore, README, manifest). First clean commit pushed to GitHub.

### 2026-05-27 08:45 BST
**Decision:** Three-machine protocol locked in. Every CC session must begin with machine identity check. Git is the synchronisation layer between Mac mini and MacBook Pro. Local DECISIONS-LOG.md must be pulled fresh at session start.

### 2026-05-27 08:40 BST
**Decision:** Existing senseless-theme directory wiped on Mac mini. GitHub history wiped (Option B — kept repo URL). Fresh build starts from latest Horizon as a clean base.

### 2026-05-27 08:30 BST
**Decision:** Decisions Log restructured into paginated volume system in Notion. Sub-pages named "Vol N — [month] [year]". When a volume fills, a new one is created; old volumes never deleted. Local DECISIONS-LOG.md mirrors active volume only. Six-layer three-way sync protocol documented. Skills raised to 10 (added drift-check). Slash commands raised to 4 (added /drift-check).

### 2026-05-27 08:00 BST
**Decision:** Final Claude Code workflow structure locked in. 10 skills, 4 slash commands, 4 docs, 1 CLAUDE.md, image pipeline scaffolding.

### 2026-05-27 07:45 BST
**Decision:** Image Management System ported from Totally Numb. Pipeline: Sharp compression → Shopify Files staged upload → alt text set → manifest entry. Senseless naming prefix.

### 2026-05-27 07:30 BST
**Decision:** Typography confirmed. Manrope (500–700) headings, Inter (400) body. Reference brands Augustinus Bader, Dieux, Wildsmith Skin, 111SKIN. Clean geometric sans.

### 2026-05-27 07:15 BST
**Decision:** New theme built from latest Horizon as clean start. Brand purple `#6B3FA0`.

### 2026-05-27 07:00 BST
**Decision:** UK compliance non-negotiable. See docs/COMPLIANCE.md.

### 2026-05-27 06:55 BST
**Decision:** Senseless is a UK cosmetic product, not a medicine. Avoids MHRA borderline threshold. "Numbing" only in SEO/URLs/meta, never in claims about product effect.

### 2026-05-27 06:50 BST
**Decision:** Lidocaine-free positioning approved. Eugenol-based active.

### 2026-05-26 22:00 BST
**Decision:** Tier hierarchy: Clinical < Advanced < Professional. No percentage claims.

### 2026-05-26 21:55 BST
**Decision:** 10 SKUs confirmed. S30CL, S30AD, S30PR / S10CL, S10AD / SG35CL, SG35AD, SG35PR / SSPAD, SSPPR.

---

*For the full history, see the Notion Decisions Log: https://www.notion.so/36c58bc375ea81fd8a68c983b41c8a86*
