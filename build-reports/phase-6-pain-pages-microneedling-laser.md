# Phase 6 — Pain/awareness pages (microneedling + laser)

**Date:** 2026-06-02 (BST) · **Branch:** dev · **Theme:** Senseless Dev `#199324434780` (store `senseless-numbing`)
Token refreshed (`./scripts/refresh-token.sh` → shpca_719735…). Build source: build-ready spec `37358bc375ea81df995afcf813dd03bb`, PRODUCTION COPY section used verbatim.

## What was built — two standalone awareness pages
Both ship complete **without** the interactive (per spec build order — the pain-scale numbers are TODO-SOURCE and must not be invented). Reused existing modules only; one tiny placeholder section added for the interactive slot.

### Pages
1. **`/pages/does-microneedling-hurt`** — template `page.does-microneedling-hurt` → routes to `/collections/numbing-cream-for-microneedling`.
2. **`/pages/does-laser-hair-removal-hurt`** — template `page.does-laser-hair-removal-hurt` → routes to `/collections/numbing-cream-for-laser-treatment`.

### Structure (both, verbatim copy)
- **Hero** (`senseless-guide-hero`) — H1 = the query verbatim; answer-first subhead; eyebrow "What to expect".
- **§1 The honest answer** (`senseless-editorial-band`) — AI-extractable lead paragraph.
- **§2 Interactive slot** (`senseless-pain-scale-slot`, **NEW** placeholder) — renders **only** an empty, hidden `#pain-scale` anchor + an HTML comment storing the future heading. Page validates and reads complete without it; the slider gets built in here later once numbers are sourced.
- **§3 What affects how much you feel** (`senseless-rich-text`, `<ul>`).
- **§4 How numbing fits in** (`senseless-rich-text`) — practitioner-routed; inline links to the procedure collection + the Selector.
- **§5 Key Facts** (`senseless-rich-text`, eyebrow "The essentials", `<ul>`) — System-guide §7 pattern, GEO-extractable.
- **Selector link-in** (`senseless-callout-band`, neutral) → `/pages/the-senseless-system#selector` (per Phase 6a follow-up: pain pages get the link-in when built).
- **§6 FAQ** (`senseless-faq-accordion`) — 4 Q&As; **emits FAQPage JSON-LD**.
- **§7 Route forward** (`senseless-link-row`) — collection + Selector.
- **Schema** (`senseless-page-schema`) — emits **WebPage**; Horizon emits **BreadcrumbList**; FAQ emits **FAQPage**.

### Page resources + meta (Admin API)
- `pageCreate` both (title = H1, handle, `templateSuffix`, `isPublished: true`) — Page IDs `711026934108` (microneedling), `711026966876` (laser); no userErrors.
- Meta via `global.title_tag` / `global.description_tag` metafields (the supported SEO-override mechanism): titles 51 / 56 chars (≤60), descriptions 155 / 147 chars (≤155). Verbatim from spec.

### Nav
- `menuUpdate` on `senseless-main` — added a **"Does it hurt?"** pain/awareness branch under **The System**, with both pages as children (branch header points to the first child, matching the menu's own convention, e.g. "By format" → numbing-cream; mirrors how "Shop" uses 3 levels). Full menu rebuilt from the live tree programmatically — verified intact (4 top-level branches preserved, nothing lost).

## §11 / compliance gate
- **0 banned words.** Reduce-not-eliminate throughout (no pain-free / completely numb / removes pain / won't feel anything). No efficacy / duration / onset / % claims. "Formulated in the United Kingdom." Cosmetic, not a medicine.
- **Practitioner-routed** present in §4 *and* the FAQ on both pages ("most practitioners apply their own…", "check with your practitioner / clinic's guidance first").
- **Every FAQ lead sentence is compliant standalone** (AI-extract safe) — each opens with a reduce-not-eliminate framing.
- Interactive numbers remain **TODO-SOURCE** — not invented; interactive not shipped.

## Verify
- **theme-check: 0 errors** (24 pre-existing Horizon warnings only; none on the 3 new files; 391 files inspected).
- **Asset-API diff:** slot section + both templates landed; settings intact, **no pruning** (only JSON slash-escaping `<\/p>` + trailing-newline serialization artifacts).
- **Render-verify (Playwright, live preview), both pages:** HTTP 200; H1 = query verbatim; **JSON-LD = WebPage + BreadcrumbList + FAQPage**; FAQ 4 questions render; **`#pain-scale` present but empty + hidden**; collection link + Selector link both resolve (collection target 200); Selector link-in band renders; **meta `<title>` + description render per spec**.

## Files / API
- New: `sections/senseless-pain-scale-slot.liquid`, `templates/page.does-microneedling-hurt.json`, `templates/page.does-laser-hair-removal-hurt.json`.
- API: `pageCreate` ×2, `metafieldsSet` (global title/description) ×2, `menuUpdate` (senseless-main).

## Open questions / assumptions logged
- **Nav branch label** — used **"Does it hurt?"** for the pain/awareness branch header (spec said "pain/awareness branch" without a label) and pointed the header at the first child (microneedling), per the menu's existing convention. Confirm the label if you'd prefer something else (e.g. "Will it hurt?", "Pain & comfort").
- **Hero eyebrow** "What to expect" (drawn from the spec's own meta title) and §1/§4 head wording ("What it actually feels like", "Preparation, not the result") were composed to fit the reuse modules — all compliant, no claims.
- **Interactives (both per-page sliders + the comparison hub) remain TODO-SOURCE** — deferred until typical-experience numbers are sourced. Slot anchor is in place on both pages.

## HOLD
Both pages complete, published and verified live. Interactives deferred (gating numbers). Nothing else started.
