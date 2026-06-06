# PHASE 10 — per-strength photography: process + assign

**Date:** 2026-06-07 (BST) · **Branch:** dev · **Theme:** Senseless Dev `#199324434780` (UNPUBLISHED — kept unpublished). theme-check **0 errors**. Commits `067efdb`, `bdf1886`. Originals kept in `assets/images/processed-sources/`.

## Inbox gate
**13 of 14 files present.** The one missing — `article` — is itself on the EXCLUDE list (garbled "CLIANCLE STRENGTH", re-source pending). Per your "proceed with the 13" call, I processed the 11 usable shots + skipped all 3 excludes (`article` is both missing and excluded; `howtouse-homepage` and `cc-gpt1` remain in the inbox, untouched).

## Processing
All shots → JPEG masters (mozjpeg q85–88); product/collection shots are 1:1 squares (sources were already 1254²), lifestyle bands kept landscape (1536×1024). **WebP/AVIF + responsive srcset are delivered by the Shopify CDN at render** from the JPEG masters (same as the existing pipeline). Uploaded to Shopify Files; manifest updated (13 entries).

## Assigned — product / collection records (Admin API)
| Target | Image | Placeholder flag |
|---|---|---|
| Clinical Spray PDP (featured) | senseless-clinical-strength-spray | **removed** |
| Advanced Spray PDP (featured) | senseless-advanced-strength-spray | **removed** |
| Clinical Gel PDP (featured) | senseless-clinical-strength-gel | **removed** |
| Advanced Gel PDP (featured) | senseless-advanced-strength-gel | **removed** |
| Foaming Cleanser PDP (featured) | senseless-foaming-cleanser | **removed** |
| **Professional Spray PDP** (featured) | senseless-professional-strength-spray *(interim crop)* | set **false** + note |
| **Professional Gel PDP** (featured) | senseless-professional-strength-gel *(interim crop)* | set **false** + note |
| Numbing Spray COLLECTION image | senseless-numbing-spray-collection | — |
| Numbing Gel COLLECTION image | senseless-numbing-gel-collection | — |
| Clinical Starter bundle (featured) | senseless-clinical-starter-bundle | — |

- For each PDP the old placeholder media was **deleted** (so the new shot is featured and the `"[PLACEHOLDER…]"` alt is gone) and the new media carries proper descriptive alt. Verified on render: all 7 PDPs show the new image, `placeholderAlt=false`, desktop + mobile.
- **Pro Spray + Pro Gel** = interim crops of the Professional bottle from the spray/gel collection trios (rightmost bottle, padded square on the sampled bg). Correct pack (Professional Strength, 100ml / 15ml) = launch-safe. `senseless.image_placeholder=false` + `senseless.image_note = "interim crop from collection trio — swap when dedicated Pro single regenerated"`. **cc-gpt1 was NOT used.**
- **All 7 first-pass placeholder products are now resolved** (5 flags removed, 2 Pro set false + note).
- Collection images: set the **Admin-API record** (collection.image) AND wired the **theme collection-hero** template image (the custom hero uses a template image setting, not the record — both done, matching the numbing-cream pattern). Verified: spray/gel collection heroes now render the trios.

## Assigned — theme section bands
- **About brand band** (`page.about.json` → `what` band) ← senseless-about-brand-band. Verified rendering (replaced range-angled).

## ⚠ FLAGS / not assigned
1. **homepage social/bundle band** (senseless-home-bundle-social-band) and **procedure page band** (senseless-procedure-band): the target sections **do not exist yet** — the homepage "Complete kits"/social band is a pending Stage-2 build, and `/pages/aesthetic-procedures` has no image-bearing section (its guide-hero has no image slot). Both images are **processed + uploaded to Files and ready** — they just need the bands built, then I'll wire them. Not forced into unrelated slots.
2. **clinical-starter-test**: the brief listed it under "theme section image settings (not product records)" but the target was "Clinical Starter bundle featured image" — a **product record**. I assigned it as the **clinical-numbing-kit-small** product's featured image (it filled the Phase-13 gap of bundles having no featured image). Two things to confirm: (a) that's the intended target (product record, not a theme band), and (b) the source filename carries a **`-test`** suffix — confirm it's the final render, not a test-only output.
3. **Pro singles** remain interim crops (flagged on-record) — swap when dedicated Professional Spray/Gel singles are regenerated.

## Pack-artwork check (report-don't-fix)
All new shots are **correct** and resolve the earlier Phase-10 pack flags: sprays show **100 ml** (not 50ml), gels **15 ml**, foaming cleanser carries **no strength label** (the earlier "Professional Strength cleanser" issue is gone), fl-oz conversions correct. No pack issues to report on the processed shots.

## Excluded (not processed)
`article` (garbled brand text — and missing from inbox), `howtouse-homepage` (label "3.35 oz" should be 0.35), `cc-gpt1` (GPT-made, "FOAM CLEANSER" misname — reference only).

## Files / verification
- Theme: `page.about.json`, `collection.numbing-spray.json`, `collection.numbing-gel.json`, `image-manifest.json` + processed JPEGs + processed-sources.
- Store-level (API): 7 PDP featured, 1 bundle featured, 2 collection image records, placeholder metafields.
- Verified desktop + mobile: 7 PDP featured images correct (no placeholder alt), 2 collection heroes show the trios, About brand band renders. theme-check 0. Theme unpublished.

## HOLD
Per-strength photography processed + assigned. Pro singles interim (flagged); 2 lifestyle bands uploaded + awaiting their sections; clinical-starter `-test` filename + grouping flagged for your confirmation.
