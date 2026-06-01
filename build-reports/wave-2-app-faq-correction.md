# Wave 2 content correction — Application + FAQ (9 numbing product pages)

**Date:** 2026-06-01 (BST) · **Branch:** dev · **Theme:** Senseless Dev `#199324434780` (unpublished)
**Scope:** TWO sections only — **Application (how-to-use)** + **FAQ** — on the 9 numbing product pages (cream/gel/spray × Clinical/Advanced/Professional). **Foaming Cleanser excluded.** Everything else on the pages (order, hero, system band, key facts, related, schema wiring, buttons) unchanged. theme-check **0**; all 9 render-verified (cream/gel/spray).

## Sources read in full (before writing)
- 🟢 Canonical State §7 (corrected application + button) + §1 range + §11 QA gate (incl. the NB that the apply-before window is a required instruction, not a banned timing claim) — https://www.notion.so/37258bc375ea813e895ccbe38c0cadc8
- Governed Totally Numb pages (voice/substance model, ported to Senseless cosmetic voice):
  • How to Apply Numbing Cream — 5c883584-76e8-4054-927b-123a7e30d69d
  • Tattoo Numbing Cream (product) — ba9fa96c-24de-456c-ad2c-b91e11ec49a6
  • How Long Does Numbing Cream Last — 53cf9098-8498-42fa-bffe-79df64d8ac58

## What changed
**1) Application section (rebuilt):** added a **"Before you apply"** safety lead (patch test 24h ahead on wrist/behind ear; stop if redness/irritation/swelling; care on sensitive/broken skin; check with the practitioner rather than doubling up), then the steps:
- **Cream (5):** clean dry skin → thick visible layer (visibly white) → **cover with cling film** (occlusion) → **leave ~45–60 min (general guide, varies — follow product + practitioner)** → remove.
- **Gel (5):** same, but cover "if your preparation window is longer" and "allow time to take effect" (no minute figure).
- **Spray (4):** clean dry skin → **hold ~10–15cm, even coverage** (not a light mist) → allow time to take effect → proceed/remove as directed. No occlusion, no invented minute figure.
- Section adapt: `senseless-how-to-use` gained a `lead` richtext field (rendered as a callout above the numbered steps).

**2) FAQ (rebuilt, substantive — no "practitioner is the best guide" dodge):** per page —
- *How long before my appointment should I apply it?* (cream: ~45–60 min; gel/spray: allow time to take effect; both with the "varies — follow product + practitioner" caveat)
- *How long does it last?* — the three-variable answer (strength chosen · how well applied · appointment length/demand; **gradual fade, no hour-figures**)
- *Do I need to patch test?* (yes, 24h ahead) · *Can I apply it the night before?* (no, short window)
- *What size should I choose?* (cream/gel only — 10g/15ml single vs 30g/35ml regular; **omitted on spray**)
- *What's in it?* (UK cosmetic topical preparation by Matrix Health Group Ltd; full list on the pack; patch test if sensitive)
- tier-choice FAQ (Clinical → "When should I choose Advanced or Professional?"; Advanced → "…over Clinical?"; Professional → "When is Professional the right choice?")
- *Is this a medicine?* (no).

**3) FAQPage JSON-LD** regenerates from the FAQ blocks → updated automatically: **8 Q&As** on cream/gel pages, **7** on spray (verified in rendered schema).

## §11 / Master Rubric per-page QA gate — focused on the two corrected sections

**Shared, verified on all 9 (render):**
- **Compliance (A,B,F):** **0 banned words**; **no effect-duration in hours**, no onset-speed, no %, no mechanism, no active-ingredient naming. The **apply-before window (~45–60 min, cream, with "varies" caveat)** is present as a required **application instruction** (§11 NB), not a banned timing claim. Patch-test "24 hours ahead" is the only hour-figure (an instruction). Safety guidance (patch test / sensitive-broken skin / practitioner check) added. "Is this a medicine? No." retained. FAQ answers carry real substance — **no dodge phrasing**.
- **GEO (E):** FAQ answer-first; **FAQPage schema valid + matches the new Q&As** (8 cream/gel, 7 spray); Key Facts block unchanged (incl. "UK cosmetic product, by Matrix Health Group Ltd. Not a medicine.").
- **SEO (C,D):** these sections now capture more long-tail naturally — "how long before … apply", "how long does it last", "patch test", "apply the night before", size guidance — in answer-first FAQ phrasings. H1/eyebrow/meta unchanged.
- **Build:** theme-check 0; live price/OutOfStock/de-suffixed slugs unchanged; `senseless-how-to-use` adapted (lead field) — no new/duplicate sections; password-render verified per format.

**Per page (the two sections):**

| Product | App: lead+patch | App: format detail | FAQ count | tier-choice FAQ | size FAQ |
|---|---|---|---|---|---|
| clinical-strength-cream | ✅ | cling film + 45–60min | 8 | Advanced/Professional | ✅ 10g/30g |
| advanced-strength-cream | ✅ | cling film + 45–60min | 8 | over Clinical | ✅ |
| professional-strength-cream | ✅ | cling film + 45–60min | 8 | when Professional | ✅ |
| clinical-strength-gel | ✅ | cover-if-longer, no min | 8 | Advanced/Professional | ✅ 15ml/35ml |
| advanced-strength-gel | ✅ | cover-if-longer, no min | 8 | over Clinical | ✅ |
| professional-strength-gel | ✅ | cover-if-longer, no min | 8 | when Professional | ✅ |
| clinical-strength-spray | ✅ | 10–15cm, no occlusion | 7 | Advanced/Professional | — (single-size) |
| advanced-strength-spray | ✅ | 10–15cm, no occlusion | 7 | over Clinical | — |
| professional-strength-spray | ✅ | 10–15cm, no occlusion | 7 | when Professional | — |

## Deploy note
The combined `shopify theme push` **silently skipped 4 template files** (a recurring CLI quirk) — caught via an Asset-API diff (remote `lead` absent), re-pushed those 4 explicitly with `--only`, and re-verified the deployed asset + render. (Lesson logged: always diff remote after a multi-file push.)

## Unchanged (by scope)
- Foaming Cleanser page (cleanser, no numbing routine) — untouched.
- All other product-page sections — untouched. Wave 3 not started.
