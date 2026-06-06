# Image fix pass 1 (A2 + A5) + bundle photography (held)

**Date:** 2026-06-07 (BST) · **Branch:** dev · **Theme:** Senseless Dev `#199324434780` (UNPUBLISHED). theme-check **0 errors**. Commits `34d178d` (A2/A5), `2918b01` (bundle photo). Originals kept in processed-sources.

---

## IMAGE FIX PASS 1 — unblocked only

### A2 — About brand band no longer square-cropped
`senseless-image-text-band` gained an **`image_ratio`** setting (default `1 / 1` = the §11 site default, so every other instance is untouched). The About brand band (`page.about.json` → `what`) is set to **`3 / 2`** as a **deliberate per-section exception** (§11), driven by an inline `aspect-ratio` that overrides both the base and mobile 1:1 rules.
**Verified desktop + mobile:** band `aspect-ratio = 3/2`, the rendered box ratio (1.50) matches the source ratio (1.50) → **no centre-crop; the vanity bag (left) and cleanser (right) are fully visible.** When the §E 16:9 band art lands, switch the setting to `16 / 9`.

### A5 — bundles collection now uses the brand layout
Created `templates/collection.bundles.json` (hero + trust bar + collection grid + Selector callout — parity with the format collections) and set the bundles collection `templateSuffix = "bundles"` (was the default Horizon `collection.json`). **No new art** (the hero is text-only; collection.image stays unset → empty-safe).
**Verified:** `/collections/bundles` renders the brand hero (`H1 "Complete numbing kits, matched and ready."`) + grid (the 5 bundles) + trust bar.

*(Did not touch any art-gated or section-gated slot.)*

---

## BUNDLE PHOTOGRAPHY — processed + uploaded, **HELD (not assigned)**

### ⚠ Cleanser pack-artwork defect — CONFIRMED on all 4 new shots
On every new bundle source, the **Foaming Cleanser carries the bundle's strength word** — "SENSELESS **CLINICAL** FOAMING CLEANSER", "… **ADVANCED** …", "… **PROFESSIONAL** …". The cleanser is **strengthless** (one FOAM SKU, Canonical §1; the standalone cleanser shot has no strength). Per the brief's conditional: **DO NOT ASSIGN.**
- Secondary pack note (report-don't-fix): the new shots print the tier as **"CLINICAL"** (no "STRENGTH") on the numbing items too, vs the established packs' **"CLINICAL STRENGTH"**.
- The **previously-assigned Clinical Starter image is correct** (cleanser reads just "SENSELESS FOAMING CLEANSER", strengthless) — left in place on `clinical-numbing-kit-small`.

### What was done
- **Processed all 4 → 1:1** (clinical-ultimate/advanced-starter/advanced-ultimate were 1254² square; prof-bundle was 1316×1195 → centre-cropped to square), uploaded to Shopify Files, manifest entries added (tagged "HELD — cleanser defect"), originals moved to processed-sources.
- **Not assigned.** The 4 imageless bundle PDPs (`clinical-numbing-kit-large`, `advanced-numbing-kit-small`, `advanced-numbing-kit-large`, `professional-numbing-kit-large`) left as-is (imageless = empty-safe on the unpublished theme).
- **On-record flag** set on those 4: `senseless.image_placeholder=true` + `senseless.image_note = "bundle photo held — cleanser shows incorrect strength label; awaiting strength-less re-render"`.
- **Mega-menu Featured card** (pulls Professional Ultimate's featured image) → still the neutral placeholder, since Pro Ultimate was not assigned. It will auto-populate when a clean Pro Ultimate render is assigned.

### Assigned vs held
| Bundle | New shot | Status |
|---|---|---|
| Clinical Starter (kit-small) | — (already has correct image) | unchanged ✓ |
| Clinical Ultimate (kit-large) | clinical-ultimate | **HELD** (cleanser label) |
| Advanced Starter (kit-small) | advanced-starter | **HELD** |
| Advanced Ultimate (kit-large) | advanced-bundle | **HELD** |
| Professional Ultimate (kit-large) | prof-bundle | **HELD** (also gates the mega featured card) |

### Manifest entries added (4)
`senseless-clinical-ultimate-bundle` (196KB) · `senseless-advanced-starter-bundle` (173KB) · `senseless-advanced-ultimate-bundle` (166KB) · `senseless-professional-ultimate-bundle` (132KB) — all 1:1, uploaded to Files, marked HELD.

### Render check
4 bundle PDPs confirmed `featuredImage = NONE` (held/empty-safe). theme-check 0. Theme unpublished.

## To resolve (Daniel / photo lane)
Re-render the 4 bundle shots with a **strengthless Foaming Cleanser** (and ideally "CLINICAL STRENGTH" wording on the numbing items, matching the established packs). On receipt I'll assign them to the 4 bundle PDPs + clear the flags; the Professional Ultimate one also lights up the Shop mega Featured card.

## HOLD
A2 + A5 live + verified; 4 bundle shots uploaded + held with on-record flags. theme-check 0; unpublished.
