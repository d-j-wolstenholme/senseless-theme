# Phase 6 close — "Does it hurt? — by treatment" article

**Date:** 2026-06-03 (BST) · **Branch:** dev · **Theme:** Senseless Dev `#199324434780` (store `senseless-numbing`)
Token refreshed (`./scripts/refresh-token.sh` → shpca_935e22…). Build source: spec `37358bc375ea81df995afcf813dd03bb` — "PHASE 6 CLOSE — Does it hurt? by treatment", copy verbatim.

## What was built
One knowledge article: **`/pages/does-it-hurt-by-treatment`** (template `page.does-it-hurt-by-treatment`), six treatments on one page (no thin standalone pages). Page resource created via Admin API (id `711028048220`; title = H1; published; templateSuffix set). Built from existing modules only.

### Structure
- **Hero** (`senseless-guide-hero`) — H1 "Does it hurt? Pain by treatment"; eyebrow "An honest guide"; answer-first subhead (verbatim).
- **Intro** (`senseless-editorial-band`) — composed from the spec's intro directive (personal/varies by area·technique·sensitivity; numbing = preparation not part of the treatment; practitioner-routed). AI-extractable.
- **6 per-treatment sections** (`senseless-rich-text`, alternating canvas/white) — H2 = the query verbatim; 2–3 sentence answer-first; a bold **We'd reach for:** line; inline links to the relevant collection + the Selector. Treatments: lip filler, Botox, microblading, lip blush, waxing, electrolysis. **No tattoo content.**
- **Key Facts** (`senseless-rich-text`, "The essentials", `<ul>`) — verbatim.
- **Selector link-in** (`senseless-callout-band`).
- **FAQ** (`senseless-faq-accordion`) — the 6 "does X hurt" Q&As, answer-first leads verbatim from the sections; **emits FAQPage JSON-LD**.
- **Route forward** (`senseless-link-row`) — comfort comparison hub + Selector + Shop by procedure.
- **Schema** (`senseless-page-schema`) — WebPage; Horizon BreadcrumbList; FAQ FAQPage.

### Meta + nav
- Meta via `global.title_tag`/`description_tag`: title **70 chars** (spec verbatim — exceeds the ≤60 guideline; used per the brief's "per spec" instruction, flagged here), description 147 (≤155).
- Nav: added a 3rd child **"Pain by treatment"** under the existing "Does it hurt?" branch (alongside microneedling + laser). Menu rebuilt from the live tree, verified intact (4 top-level branches preserved). *(Note: a follow-up restructure brief — now in progress — re-points this branch to a new hub page and removes the direct children; that change is tracked in the restructure report.)*

## §11 / compliance gate
- **0 banned words**; **no tattoo content** (excluded per spec — Totally Numb's lane). Reduce-not-eliminate; no efficacy/duration/onset/% claims; "formulated in the United Kingdom"; practitioner-routed in the intro *and* per-treatment framing; every FAQ lead sentence compliant standalone. Botox keeps **"optional, not required"** (anti-upsell).

## Verify
- **theme-check: 0 errors** (24 pre-existing Horizon warnings only; none on the new template).
- **Asset-API:** template pushed; page resource created/published with correct suffix.
- **Render-verify (Playwright, live preview):** 200; H1 correct; **JSON-LD = WebPage + BreadcrumbList + FAQPage**; all **6 treatment H2s** render; 6 "We'd reach for" lines; **all collection + Selector + comfort-hub links present and resolve** (SPMU/aesthetic targets 200); FAQ 6 Q&As render; **no "tattoo"** anywhere on the page.

## Deviation logged
- Spec linked microblading/lip-blush to `/collections/numbing-cream-for-spmu`, which **does not exist** (no resource, no redirect). Canonical handle is **`numbing-cream-for-semi-permanent-makeup`** — used that so the links resolve (prose unchanged). Flag if a `-spmu` vanity handle/redirect is wanted instead.
- Intro paragraph composed from the spec's directive (the intro was described, not given verbatim); all other copy verbatim.

## Files / API
- New: `templates/page.does-it-hurt-by-treatment.json`. API: `pageCreate`, `metafieldsSet` (meta), `menuUpdate` (nav child).

## Phase 6 status
This completes the by-treatment article. A restructure brief (Does-it-hurt **hub page** + comfort-section inline fix + nav re-point) is now in progress and will formally close Phase 6.

## HOLD
By-treatment article complete, published and verified live.

---

## Correction appended 2026-08-13 — the tattoo exclusion above is superseded

The compliance-gate line in §11 reads *"**no tattoo content** (excluded per spec — Totally Numb's
lane)"*. That was an accurate record of the spec this page was built to, and the build is not being
restated — but the reason no longer holds, and this file is the most-cited source of the
"tattoo belongs to Totally Numb" canon.

**Owner ruling, 2026-08-13:** *"senseless and totally numb both target the same customer base
now."* There is no lane split. Senseless competes for tattoo demand on merit.

Left deliberately unchanged: the page itself, and this report's record of what shipped in June. A
build report is evidence of what was done and when; rewriting one to match a later decision
destroys the audit trail that makes the decision legible. What changes is the **canon** — see
`docs/AUDIT-2026-06-12.md` items 10 / P3.5 (both closed the same day) and
`docs/TATTOO-BUILD-SWEEP.md`.

Note this does **not** dissolve the regulatory point underneath: Senseless and Totally Numb publish
different claim sets under one company number and one VAT number. That is an MHG legal question,
not a lane question, and nothing in this correction touches it.
