# Phase 6 — Aftercare sections on the two awareness pages

**Date:** 2026-06-03 (BST) · **Branch:** dev · **Theme:** Senseless Dev `#199324434780` (store `senseless-numbing`)
Token refreshed (`./scripts/refresh-token.sh`). Build source: spec `37358bc375ea81df995afcf813dd03bb` — "AFTERCARE — sections on existing pages", copy verbatim. **No standalone aftercare pages; no nav change.**

## What was added
A **"What to expect afterwards"** `senseless-rich-text` section near the end of each awareness page (after "How numbing fits in", before Key Facts → Selector → FAQ → route), plus new FAQ entries that extend each page's existing FAQPage.

### Microneedling (`/pages/does-microneedling-hurt`)
- Aftercare section (verbatim): pink/warm skin a day or two, redness settles 24–72h (deeper takes longer), keep clean/protected, follow practitioner advice, avoid heavy actives + sun. Boundary line: *"Numbing is only used before the treatment for comfort — it has no role in aftercare."*
- **+2 FAQ** (verbatim): "What should I expect after microneedling?" · "How long does microneedling take to heal?" → FAQPage now **6** Q&As.

### Laser (`/pages/does-laser-hair-removal-hurt`)
- Shorter aftercare section (verbatim): area slightly red/warm a few hours, settles quickly, avoid heat/sun/friction a day or two, follow clinic advice. Boundary line: *"Numbing is only used beforehand for comfort — it isn't part of aftercare."*
- **+1 FAQ** (verbatim): "What's the aftercare for laser hair removal?" → FAQPage now **5** Q&As.

By-treatment page: no per-treatment "afterwards" note added (optional per spec; skipped to avoid bloat).

## Compliance
- **Numbing-has-no-role-in-aftercare** line present on **both** (keeps the pre/post boundary honest — numbing is preparation, not aftercare).
- "Settles / usually / most people" experiential framing; **24–72h** stated as a general typical healing range with "most people find" — **not** a product duration/efficacy claim; no product onset/duration numbers. 0 banned words. Practitioner/clinic-routed on both. No tattoo.

## Verify
- **theme-check: 0 errors** (24 pre-existing Horizon warnings only).
- **Asset-API diff:** both templates landed; `aftercare` in `order`; FAQ block counts 6 / 5.
- **Render-verify (Playwright, live preview):** both pages 200; aftercare section H2 renders inline (no layout break — `senseless-rich-text` is inline by default per the new standard); FAQ shows the new questions; **FAQPage JSON-LD includes them** (6 / 5 questions); WebPage + BreadcrumbList + FAQPage all intact.

## Files
- Edited: `templates/page.does-microneedling-hurt.json`, `templates/page.does-laser-hair-removal-hurt.json` (aftercare section + FAQ entries + order).

## HOLD
Aftercare sections live and verified on both awareness pages.
