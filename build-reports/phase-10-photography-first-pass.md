# Phase 10 — product photography (first pass)

**Date:** 2026-06-04 (BST) · **Branch:** dev · **Theme:** Senseless Dev `#199324434780` (UNPUBLISHED) · **Commit:** `991cbcd`. Token refreshed.

## Prereq
**Sharp installed** via `npm install` (was scaffolded, not installed) — `sharp 0.33.5`. No substitute used.

## Process (all 8 inbox shots)
Run through `scripts/image-pipeline.mjs` → 1:1 (sources were already 1254×1254 white-bg), optimised JPEG (~60KB), uploaded to **Shopify Files**, alt text per image, originals moved to `assets/images/processed-sources/`. Shopify serves WebP + responsive srcset automatically via the templates' `image_url`/`image_tag`.

| Shot (identified by viewing) | File name |
|---|---|
| Clinical cream single | senseless-clinical-strength-cream |
| Advanced cream single | senseless-advanced-strength-cream |
| Professional cream single | senseless-professional-strength-cream |
| 3 cream tubes together | senseless-numbing-cream-trio |
| Full range × 4 upright | senseless-range-upright |
| Full range × 4 angled | senseless-range-angled |
| cream+spray+gel trio (cream upright) | senseless-cream-spray-gel-trio |
| cream+spray+gel trio (cream lying) | senseless-cream-spray-gel-trio-angled |

**Note:** there were **two** cream+spray+gel trio shots (brief said one) — both processed; the upright trio is used for placements, the angled one is spare.

## Assign — REAL / matching
- **Clinical / Advanced / Professional Cream PDPs** → that strength's single-cream shot as the **product featured image** (renders in the PDP hero via `product.featured_media`). ✅
- **Numbing Cream collection** → 3-cream trio, set on **both** the hero section image (renders) and the collection record image. ✅
- **Homepage** (section image settings): hero = range-upright; "format overview" band = cream+spray+gel trio; secondary band = range-angled. ✅
- **About** → image-text band = range-angled. ✅
- **Shop All / format-overview:** Shop All itself has **no hero image slot** (it's the 4 quick-add grid sections), so the trio sits on the homepage **format-overview band** (the format-overview context). Noted.

## Placeholders — DEV ONLY, FLAGGED (must not ship)
No individual spray/gel/cleanser shots were supplied — only group shots. So group shots are used as **flagged placeholders**:
- Spray PDPs ×3 + Gel PDPs ×3 → cream+spray+gel trio.
- Foaming Cleanser PDP → range-upright.
**Flagged** by: `senseless.image_placeholder = true` metafield on all 7 products + alt text prefixed `[PLACEHOLDER…]`.
**Hard launch gate:** theme kept **UNPUBLISHED** and the store is password-gated; product featured images are store-level (not theme-gated), so these MUST be replaced with strength-specific shots before the store goes public — a Professional pack on a Clinical/Advanced page is a mislabelling issue once live.

## REPORT — physical pack artwork (for Daniel → pack producer; not fixable in theme)
- **Spray** pack reads **50ml** — canonical spray is **100ml**.
- **Gel** pack reads **15ml** — canonical gel is **15ml + 35ml** (two sizes).
- **Foaming Cleanser** pack reads **"Professional Strength"** — the cleanser is single-strength aftercare, not strength-tiered.
These show in any hero using the range/group shots.

## Verify
- theme-check **0 errors**. Renders confirmed (Playwright, desktop + mobile): cream PDP heroes show the correct strength; collection hero shows the trio; homepage hero/bands + About render the range/trio shots; placeholder PDPs show the flagged group shot.
- Theme **not published** (hard gate held).

## Files / API
- New: `assets/images/processed/*.jpg` (8), `assets/images/processed-sources/*` (8 originals). Edited: `image-manifest.json`, `templates/collection.numbing-cream.json`, `templates/index.json`, `templates/page.about.json`. Sharp added to node_modules (gitignored).
- API: 10× productCreateMedia (3 real + 7 placeholder), 7× placeholder metafield, collectionUpdate (record image), Files uploads ×8.

## HOLD
First-pass photography live on the dev theme. Pending: real strength-specific spray/gel shots (to replace the 7 placeholders); pack-artwork corrections (Daniel→producer); do not publish until placeholders replaced.
