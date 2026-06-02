# Phase 6 — "Does it hurt?" hub page + comfort-section fix + global inline standard

**Date:** 2026-06-03 (BST) · **Branch:** dev · **Theme:** Senseless Dev `#199324434780` (store `senseless-numbing`)
Token refreshed (`./scripts/refresh-token.sh` → shpca_935e22…). Build source: spec `37358bc375ea81df995afcf813dd03bb` — "RESTRUCTURE — Does it hurt? HUB page" (incl. the folded-in positioning bug + global standard).

## 1. Comfort-section positioning bug — FIXED (root cause: CSS class collision)
`senseless-comfort-compare` used the `.ss-cc` prefix, which is **owned by `senseless-cookie-consent`** (`position:fixed; left:0; right:0; bottom:0; z-index:1000`). The cookie banner's fixed positioning leaked onto the comfort section via the shared class, pinning it to the viewport bottom over the page content (Daniel's screenshot, microneedling page).
- **Fix:** renamed the section's entire CSS prefix `.ss-cc*` → unique **`.ss-cmp*`** (classes + JS `closest()`/selectors; 63 occurrences). Added explicit `position:static` on the root as belt-and-braces. No `bottom`/`z-index` was ever in the section's own CSS.
- **Verified:** computed `position: static` on the hub, both awareness pages, and at 390px mobile; comfort rect top≈883 (in normal flow, not pinned); no overlap.

## 2. Global build standard — logged in ARCHITECTURE.md
Audited every `senseless-*` section/snippet for `position:fixed|sticky|bottom:0|z-index`. Only deliberate uses remain: `senseless-header` (sticky header + fixed mobile drawer/scrim) and `senseless-cookie-consent` (fixed bottom banner). Added a **"Section build standards"** section to `docs/ARCHITECTURE.md`: sections render inline by default; fixed/sticky is opt-in only; no stray z-index; each section's CSS scoped to a unique prefix (or `#shopify-section-{id}`); `.ss-cc` reserved for cookie-consent; new sections copy a corrected inline skeleton. *(ARCHITECTURE.md edit surfaced here per Hard Rule #5.)*

## 3. New hub page `/pages/does-it-hurt` (router; Option B)
Template `page.does-it-hurt`; page resource created (id `711028212060`, published, suffix set). Schema **WebPage + BreadcrumbList ONLY** (no FAQPage — it's a router; the FAQs live on the standalone pages that rank). Structure: hero (H1 "Does it hurt?", eyebrow "An honest guide", subhead verbatim) → honest-framing intro (editorial band) → **comfort comparison hub (relocated here)** → 3 out-link cards (microneedling / laser / by-treatment, each with a one-line descriptor, via `senseless-link-row`) → Selector link-in band → route to shop. Meta via `global.*`: title 54, desc 146 (both within limits).

## 4. Relocation + nav re-point
- **Comfort comparison hub moved** off `/pages/aesthetic-procedures` → `/pages/does-it-hurt` (default per spec). aesthetic-procedures order now `[main, selectorlink]`. The by-treatment route link repointed `…aesthetic-procedures#comfort` → `…does-it-hurt#comfort`.
- **Nav:** header "Does it hurt?" now a **single destination** → `/pages/does-it-hurt`; the 3 standalone pages removed as direct nav children (they sit under the hub via cards + comparison rows). Menu rebuilt from the live tree; other branches intact (4 top-level; The System keeps its 4 guide children + the single "Does it hurt?").

## 5. Standalone pages preserved (rankings intact — Option B)
All three keep their own URLs, H1 and schema unchanged: microneedling + laser (WebPage + BreadcrumbList + FAQPage, H1 verbatim), by-treatment (unchanged). Verified live.

## Verify
- **theme-check: 0 errors** (24 pre-existing Horizon warnings only).
- **Asset-API diff:** comfort-compare remote = 63 `ss-cmp` / **0 `ss-cc`**; hub template present (correct order); aesthetic-procedures hub removed.
- **Render-verify (Playwright, live preview):** hub 200, WebPage+BreadcrumbList (no FAQPage), comfort `position:static`, 8 rows, 3 cards resolve; microneedling/laser 200, H1 + W+B+FAQ schema unchanged, comfort `position:static`; by-treatment route → does-it-hurt#comfort; aesthetic-procedures comfort absent; mobile 390px comfort static + visible.

## Compliance
Comfort interactive unchanged (qualitative, 0 banned words). Hub copy reduce-not-eliminate; practitioner-routed intro; no efficacy/duration/onset/%; no tattoo.

## Files / API
- Edited: `sections/senseless-comfort-compare.liquid` (prefix rename + position:static), `templates/page.aesthetic-procedures.json` (hub removed), `templates/page.does-it-hurt-by-treatment.json` (route link), `docs/ARCHITECTURE.md` (standard).
- New: `templates/page.does-it-hurt.json`.
- API: `pageCreate` (hub), `metafieldsSet` (hub meta), `menuUpdate` (re-point "Does it hurt?").

## HOLD
Hub built, comfort bug fixed, standard logged, nav re-pointed — all verified live. Note: aftercare-sections brief received and queued next.
