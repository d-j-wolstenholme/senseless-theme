# Phase 5 — "The Senseless System" combined guide page

**Date:** 2026-06-02 (BST) · **Branch:** dev · **Commit:** `a57cc9e` · **Theme:** Senseless Dev `#199324434780`
**Source:** model copy `37358bc375ea81b6a070e7e2145c7bf7` (built verbatim). Supersedes the separate Choosing-Your-Strength + Choosing-Your-Format briefs; replaces the broken cream-only page in nav.

## Built
`templates/page.the-senseless-system.json` — bespoke order, reusing existing modules (no new heavy sections):
| § | Section | Module | Italic accent |
|---|---|---|---|
| 1 Hero | guide-hero (canvas; CTAs: "Shop the range"→/pages/aesthetic-procedures · "Jump to the by-procedure guide"→**#matrix**) | senseless-guide-hero | *system* |
| 2 What the System is | senseless-editorial-band (white) | | *System* |
| 3 Dial one — format | senseless-link-row (Cream/Gel/Spray + links + closer) | | *format* |
| 4 Dial two — strength | **senseless-strength-ladder `layout: rows`** (the comprehensive variant reserved for this page), manual re-cut rows (session-variable led, not procedure names), Advanced "**Most popular**" tag, Professional 2px `#6B3FA0` border, anti-upsell note (pull-quote) | | *strength* |
| 5 Combine — by procedure | **senseless-strength-matrix** (8 rows, 3-col Procedure · We'd reach for · Honest note; mobile-stacks), anchor `#matrix`, closing line | | *procedure* |
| 6 The honest note | senseless-callout-band (brand) | | *skip* |
| 7 Route to shop | senseless-link-row (Shop cream/gel/spray + Browse by procedure) | | — clean |

### Module touches (additive only — no new sections, no clones)
- **guide-hero:** `accent_word` setting + render via `senseless-accent`.
- **strength-ladder `ladder_row`:** optional `tag` (e.g. "Most popular") + `featured` (2px purple border, rows variant). Manual-mode `<strong>`/`<em>` styling. (Note: in the rows variant the strength label is already purple — Professional's "purple label" is automatic.)
- **strength-matrix:** `accent_word` + `closer` (line under the table) + `anchor_id` (→ `id="matrix"` so the hero CTA jumps to it).

## §11 gate (guide-applicable) + A–K + Standard-bar — assessed against the built template
| Dim | Result |
|---|---|
| **A** voice (verbatim model copy) | ✅ all 7 heads + bodies verbatim |
| **B** compliance | ✅ **0 banned**; **0 pain-free/painless** (reduce-not-eliminate: "overkill", "rarely enough", "optional, not required"); **0 "made in the UK"**; no efficacy/duration/onset/% claims; practitioner nuance kept |
| **C/D** SEO/long-tail | n/a by design (no primary keyword — internal decision-help + brand/GEO); "The Senseless System" named in hero + §2 |
| **E** GEO/schema | ⚠ "The Senseless System" named in-page; **WebPage + BreadcrumbList JSON-LD not yet emitted** (no section emits it) — flagged below |
| **F** injectable-clean | ✅ **RELAXED per the model (guide):** matrix names Botox + lip fillers as recommendations; route/links point only to format collections + the procedures hub (no injectable collection links) |
| **G** range integrity | ✅ three formats × three strengths; "three" framing; no "four"/"flagship" |
| **H/I** trust/slugs | ✅ de-suffixed links (/collections/numbing-cream|gel|spray, /pages/aesthetic-procedures) |
| **J** components | ✅ ladder rows variant + tag/featured; matrix 8 rows + pills + honest notes; mobile-stacks |
| **K** build | ✅ theme-check **0** (384 files); page template + 3 sections pushed (CLI); JSON valid |
| **Std-bar A** | ✅ decision-led: two dials explained then combined; honest note before route-to-shop |

Section order monotonic + accents one-per-head (route head clean), verified by local parse. Matrix anchor `#matrix` ↔ hero secondary CTA confirmed.

## ⚠ Blocked on the Admin token (currently 401) — page does not render live yet
The theme template + section code are **pushed and correct**, but the page **cannot render** until a **page resource** exists. This needs the Admin API (or admin UI), which is currently 401 (the `.env` `SHOPIFY_ACCESS_TOKEN` rotated earlier today). **Outstanding step (when the token is refreshed, or via admin UI):**
1. Create an Online Store **page**: title "The Senseless System", handle **`the-senseless-system`**, **template `the-senseless-system`**, published.
2. **Render-verify** live: head weights 400 + one italic accent per head (system/System/format/strength/procedure/skip; route clean); ladder rows variant shows Clinical/Advanced(Most popular)/Professional(border); 8-row matrix stacks on mobile; anchor `#matrix` jump works.
3. **Asset-API diff** (also 401 right now) to confirm `use_metaobject:false` / `layout:rows` / accent words survived the push.

(CLI theme push uses separate auth and worked; only the Admin API is down.)

## Flags / follow-ups
- **WebPage + BreadcrumbList JSON-LD** (model "schema") is **not emitted** by these reused sections — needs a small schema snippet on the page (follow-up; doesn't block render).
- **Pull-quote** (§4) is rendered via the ladder's `note` field (purple left-border quote), not a separate `senseless-pull-quote` section — same content/placement; switch if a distinct pull-quote treatment is wanted.
- **Phase 12 wiring** (not now): point the header "Find your strength" + every collection's "Match the strength"/secondary CTA to `/pages/the-senseless-system`; mark the two old guide briefs merged.
- Old `/pages/choosing-your-strength` + `/pages/choosing-your-format` page-template files remain in repo (now superseded) — retire when this page is live.

## HOLD
Template + modules built, pushed, theme-check 0, copy verbatim + compliant. **Page-resource creation + live render-verify pend a refreshed Admin token.**
