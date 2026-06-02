# Phase 6 interactives — comfort comparison (qualitative)

**Date:** 2026-06-03 (BST) · **Branch:** dev · **Theme:** Senseless Dev `#199324434780` (store `senseless-numbing`)
Token refreshed (`./scripts/refresh-token.sh` → shpca_4051ff…). Build source: spec `37358bc375ea81df995afcf813dd03bb` — sections "INTERACTIVE — qualitative version" + "DESCRIPTOR STRINGS", all strings verbatim. **No numeric pain scale, no "/10", no sourcing.**

## What was built
New section **`sections/senseless-comfort-compare.liquid`** — a qualitative relative-comfort comparison (3-segment band **Mild · Moderate · Sharper**, active segment = `#6B3FA0`). Plain JS; each toggle combo maps to one band segment + a verbatim descriptor; no data table of numbers. Three modes via a `mode` setting:

1. **microneedling** — toggles: needle depth (Light refresh / Standard / Deeper for scarring) × area (Cheeks / Forehead-jaw-hairline) = **6 combos**. Descriptor below the band; fixed numbing line below that.
2. **laser** — toggles: area (Legs-back-arms / Underarms-bikini-upper lip) × session (First / Later) = **4 combos**. Same numbing line.
3. **hub** — the 8-row Mild→Sharper ordered list, each row links to its awareness page; hub eyebrow "A general guide", heading "How treatments compare for comfort", framing line instead of a numbing line.

It **replaced** the empty `senseless-pain-scale-slot` placeholder at §2 on both pages. Anchor renamed `#pain-scale` → **`#comfort`** (no external refs to the old anchor — verified by grep). The orphan `senseless-pain-scale-slot.liquid` was deleted (local file + remote asset, confirmed 404).

## Placement
- `page.does-microneedling-hurt` — `comfort` section (mode microneedling) at §2; order `hero → honest → comfort → affects → numbing → keyfacts → selectorlink → faq → route → schema`.
- `page.does-laser-hair-removal-hurt` — `comfort` (mode laser) at §2; same order shape.
- `page.aesthetic-procedures` — `comforthub` (mode hub) added; order `main → comforthub → selectorlink`.

## Copy (all verbatim from spec)
- Fixed numbing line (both per-page modes, under the result): "Numbing is commonly used to make this more comfortable — it reduces the sensation rather than removing it."
- All 6 microneedling + 4 laser descriptor strings and band assignments exactly per the DESCRIPTOR STRINGS tables.
- Hub: 8-row order (rows 1/3/5/7 → laser page; 2/4/6/8 → microneedling page), "milder"/"sharper" end-annotations on rows 1 & 8, framing line "Comfort is personal and varies by area, technique and individual sensitivity — this is a general guide, not a measurement."

## Compliance
- **Qualitative only** — no numbers, no "/10", no efficacy / duration / onset / %. 0 banned words; reduce-not-eliminate.
- Per-page modes carry the reduce-not-eliminate **numbing line**; hub carries the **"general guide, not a measurement"** framing line (and no numbing line).
- The interactive only recombines wording already live on each page — asserts no new fact.

## Verify
- **theme-check: 0 errors** (24 pre-existing Horizon warnings only; none on the new section or edited templates).
- **Asset-API diff:** section + 3 templates landed; per-template settings (mode/anchor/eyebrow/heading) intact, no pruning; orphan slot asset deleted (404).
- **Render-verify (Playwright, live preview):**
  - Microneedling — **all 6 combos** show the correct band + descriptor; numbing line present.
  - Laser — **all 4 combos** correct; numbing line present.
  - Hub — heading + eyebrow + framing line present; **8 rows**, each linking to the correct awareness page; no numbing line on the hub.

## Files
- New: `sections/senseless-comfort-compare.liquid`.
- Deleted: `sections/senseless-pain-scale-slot.liquid` (local + remote).
- Edited: `templates/page.does-microneedling-hurt.json`, `templates/page.does-laser-hair-removal-hurt.json`, `templates/page.aesthetic-procedures.json`.

## Open questions / assumptions
- **Toggle defaults** — each group defaults to its first option (microneedling: Light refresh + Cheeks → Mild; laser: Legs/back/arms + First session → Moderate), so a result shows on load.
- **Per-page eyebrow** "What changes it" composed to label the interactive; headings reuse the spec's own placeholder headings verbatim. Hub eyebrow/heading/framing all verbatim.
- Numeric version not built (de-scoped per the locked 2 June decision — qualitative ships, numeric only if cited data is later gathered).

## HOLD
Both interactives + the hub complete and verified live. Nothing else started.
