# Senseless — Decisions Log (Local Mirror)

**Mirrors the active volume of the Notion Decisions Log.**
Active volume: Vol 1 — May 2026
Notion source: https://www.notion.so/36d58bc375ea81708d1ac0fe0724d445

Newest at top. ISO 8601 timestamps in BST.

When this file is older than 24 hours, run `/drift-check` to surface any drift between this local mirror and the canonical Notion log.

---

### 2026-05-28 (MacBook Pro — range correction, build-side)
**Decision:** Reconciled the built theme to the corrected product range (Decisions Log 2026-05-28 22:40: 8 product pages, 10 SKUs; Clinical = cream only; no Clinical Gel; sizes are variants with size-agnostic slugs). Repo audit found the build had used the pre-correction range. Fixes across 23 files (commit `5c6dd28`): removed every Clinical Gel reference (Numbing Gel + Lip Fillers); de-suffixed all 45 size-suffixed product slugs to the 8 canonical forms; collapsed separate 10g/30g cream cards to one card per tier (Botox, Injections, Laser, Microneedling, SPMU, Waxing, Numbing Cream); Numbing Gel → 2 tier cards + 2-SKU grid; Lip Fillers grid → Clinical Cream / Advanced Cream / Advanced Gel; gel "three strengths" → two and "four formats" → three formats; cleared leftover Professional "Flagship" badges. theme check 0 errors; pushed to Senseless Dev #196680057167 only. Notion: Clinical Gel + two merged 10g cream rows already archived (left so); Numbing Gel + Lip Fillers collection rows → QA; 8 canonical product rows left In Progress (template built, Shopify products/variants/tags pending admin). Build report posted to Build Reports.

### 2026-05-28 (MacBook Pro — full site build session)
**Decision:** Built and deployed Batches 2–6 to Senseless Dev `#196680057167` (0 theme-check errors, clean push). 22 page/collection templates + 9 new `senseless-` sections (procedure-grid, product-hero, strength-matrix, how-to-use, cross-sell, guide-hero, rich-text, callout-band, contact-form). Key decisions: (1) **Products modelled as 9 logical SKUs via ONE shared `product.json` with a native variant picker** (Clinical/Advanced cream = size variants), not 11 templates — Notion DB still lists 11 separate product rows; the two creams should be single products with 30g/10g variants in admin. (2) **Spray slugs canonicalised to `/products/advanced-strength-spray` + `/products/professional-strength-spray`** (DB canonical) rather than the `-100ml` form some briefs used, to avoid dead links. (3) **Landing pages built = the 4 actually Briefed in Notion** (Senseless vs Ametop, Strongest, Best Numbing Cream, Best Emla Alternative UK) — the launch brief's names differed. (4) **Professional tier treatment on product pages is driven by product tag `Professional` / metafield `senseless.tier`** so the shared template self-applies the flagship styling. (5) **`shopify theme check` does NOT catch `default:""` on text settings** — server-side `theme push` rejects it ("default can't be blank"); fixed on product-hero. Product rows left at **In Progress** (templates built; products + variants + tier tags need creating in Shopify admin); all 22 non-product pages set to **QA**. Build report posted to Notion Build Reports. Policy pages + blog cluster skipped (Brief Status = Not Started).

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
