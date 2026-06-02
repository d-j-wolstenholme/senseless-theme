# Phase 6a — The Senseless Selector

**Date:** 2026-06-02 (BST) · **Branch:** dev · **Theme:** Senseless Dev `#199324434780` (store `senseless-numbing`)
Token refreshed at session start (`./scripts/refresh-token.sh`); shop = senseless-numbing. Build source: build-ready spec Notion `37358bc375ea81aea7ccf870ff8c70b0` (read in full).

## What was built
New schema-driven section **`sections/senseless-selector.liquid`** — a hybrid guided selector: three inputs on one screen, live result, no page reload.

- **Inputs:** (1) Treatment — 8 chips; (2) Skin — Sensitive / Normal / Resilient (default **Normal**); (3) Duration — Under 30 min / 30–60 min / Over an hour (default **30–60**). Result hidden until a treatment is picked; empty prompt "Pick your treatment to see what we'd reach for."
- **Engine (plain JS, no deps):** strength index Clinical=0 / Advanced=1 / Professional=2; format fixed by treatment. `final = clamp(base + modifiers, base, ceiling)`; modifiers Sensitive +1, Over-an-hour +1, all others 0.
- **Single source:** the 8-row table (treatment → format / base / ceiling / honest note) is carried as `data-*` attributes on the treatment chips and read by the engine from the DOM — so there is one copy of the data, with a `⚠ SINGLE SOURCE` comment tying it to the System-guide §5 by-procedure matrix (`senseless-strength-matrix`). If the matrix changes, the chips must change too.
- **Result:** two cards (Format · Strength). **Professional** strength → 2px `#6B3FA0` border + purple label (never "flagship"). Conditional lines: **stepped-up** ("Stepped up for sensitive skin and/or a longer session.") only when final > base; **capped** ("We'd keep it here for this treatment — more isn't needed.") only when base+modifiers exceeded the ceiling; **honest note** always (per treatment); **CTA** "Shop [Strength] [Format] →" → the strength-filtered format collection (`/collections/numbing-{format}?strength={strength}`); **practitioner line** always.
- **Tokens:** purple `#6B3FA0`, canvas `#f7f7f5`, ink `#1A1816`, Montserrat 400/500/600. Mobile: input chips wrap, result cards stack (≤600px).

## Placement / entry points
- **Embedded once** on `/pages/the-senseless-system`, high — after "What the System is" (`what`), before `dial1`. Anchor **`#selector`**. Order is now `hero → what → selector → dial1 → dial2 → matrix → honest → keyfacts → faq → route → schema`. Not re-embedded anywhere else.
- **Homepage link-in band** (`senseless-callout-band`, brand style) after the `strength` section → `/pages/the-senseless-system#selector`.
- **Collection link-in bands** (`senseless-callout-band`, neutral) after the Scale (`match`) on the **7 storefront collections**: numbing-cream / -gel / -spray + -for-microneedling / -laser-treatment / -semi-permanent-makeup / -waxing.

## Verify
- **theme-check: 0 errors** (24 pre-existing Horizon snippet warnings only; none on any changed file).
- **Asset-API diff:** new section + all template edits landed; the new `senseless-selector` settings survived intact (no pruning); `selectorlink` present and ordered after `match` on all 7 collections; homepage band present.
- **Render-verify (Playwright, live preview theme):** selector renders on the guide; empty prompt at load; 8 treatments; defaults Normal / 30–60. Engine click-throughs all correct:
  - Lip fillers (Normal/30–60) → Cream / Clinical, no stepped/capped, note shown, CTA `…numbing-cream?strength=clinical`.
  - Lip fillers + Sensitive → Advanced (**stepped**). + Over-an-hour → **capped** at Advanced (raw 2 > ceiling 1).
  - Microneedling (Normal/30–60) → Gel / Advanced. + Sensitive → **Professional** (purple border). + Over-an-hour → **capped** at Professional (raw 3 > ceiling 2).
  - Laser — body → Spray. Practitioner line always visible.
  - Homepage + collection (gel) link-ins both resolve to `…the-senseless-system#selector`.

## Compliance
- Recommendation framing throughout ("we'd reach for", "a recommendation, not a rule — your practitioner has the final say"); reduce-not-eliminate; no efficacy / duration / onset / % claims; no "made/manufactured in the UK". Professional never called "flagship". Honest notes retained verbatim from spec. 0 banned terms in authored copy (the only grep hits are the `flagship` schema boolean and a pre-existing untouched injectable-FAQ question).

## Open questions
- **Injectable collections excluded from link-ins (explicit assumption).** The 3 injectable collection templates — `collection.numbing-cream-for-botox`, `-for-injections`, `-for-lip-fillers` — were **not** given the Selector link-in, on the injectable-clean principle (they're the deliberately-segregated injectable set, structured around `recommendation` not the Scale). The brief said "every collection page"; I read that as the 7 storefront/Scale collections. **Confirm whether the injectable collection pages should also carry the link-in.**
- **`?strength=` filter param.** The CTA + tier links use `/collections/numbing-{format}?strength={strength}` (the documented pattern, matches the homepage tier cards). The collection grids don't currently filter on this param (filters off) — the link lands on the correct collection but doesn't pre-filter. If pre-filtering is wanted, that's a separate grid change.

## Files
- New: `sections/senseless-selector.liquid`.
- Edited: `templates/page.the-senseless-system.json` (embed selector), `templates/index.json` (homepage link-in band), 7 × `templates/collection.numbing-*.json` (link-in band after `match`).

## HOLD
Phase 6a complete and verified live. Nothing else started.
