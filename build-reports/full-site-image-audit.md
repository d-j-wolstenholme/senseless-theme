# FULL SITE IMAGE AUDIT — source map + aspect ratios (read-only)

**Date:** 2026-06-07 (BST) · **Branch:** dev · **Theme:** Senseless Dev `#199324434780` (UNPUBLISHED). **READ-ONLY — no fixes.** Audited against Canonical §11 (1:1 default via `aspect-ratio:1/1`+`object-fit:cover`; non-1:1 = deliberate per-section exception), Image Generation Prompts §E (ratio guide), and the Image Management System pipeline.

**Headline:** After the Phase-10 fills, **there are no true broken (404) images** on the dev theme — earlier "broken-image icons" in screenshots were the pre-Phase-10 state (lazy-load false positives in a naïve scan resolve to HTTP 200 once scrolled). The real issues are **(A) mis-sourced bindings** (procedure cards show product bottles; one band crops a 3:2 source) and **(B) empty slots needing images** (4 of 5 bundles; per-procedure context; correct-ratio lifestyle bands; global OG/favicon).

---

## ASPECT-RATIO AUDIT (a–e)

**(e) Studio singles + trios + bundle = genuinely 1:1 at source — confirmed, not squeezed.** All 10 single PDP shots, both new trios, the 2 Pro crops, and the clinical-starter bundle are **1254×1254 (1:1)**; the first-pass lifestyle/range images (range-upright, range-angled, cream-spray-gel-trio, numbing-cream-trio) are also 1254² (1:1). They sit in 1:1 sections → no distortion.

**(b) Section configured ratio + fit (the §11 default is near-universal):**
| Section | Ratio + fit |
|---|---|
| product-hero (PDP) | `1/1` + cover |
| collection-hero | `1/1` + cover |
| image-text-band (home product/practitioners + About bands) | `1/1` + cover |
| hero-brand-led (home/About hero) | `1/1` + **contain** |
| guide-hero (guides/does-it-hurt) | `1/1` + cover |
| trio-card-row / card-image / procedure-grid / cross-sell | `1/1` + cover |
| article header | **no `aspect-ratio`** (unconstrained) |

**(a)+(c) Sources vs slots — what's cropped right now:**
- **Only one placed non-1:1 source:** `senseless-about-brand-band` is **3:2 (1536×1024)** in the About `what` band, which forces **1:1 cover → centre-cropped to square**. Cost: ~25% off each side — **the vanity bag (left) and the right-edge cleanser are clipped**. *(This is a defect I introduced in Phase 10 — flagged in A2.)*
- All other placed images are **1:1 sources in 1:1 slots → no crop, no stretch.** hero-brand-led uses `contain` (square source → no crop, no letterbox).
- The 2 unplaced Phase-10 bands (`home-bundle-social-band`, `procedure-band`) are **3:2** — if dropped into any 1:1-cover band they'd crop the same way.

**(d) Correct per §E + fix:**
- **Products / trios / bundles → 1:1: KEEP** (matches §11 + §E). ✓
- **Homepage hero, lifestyle bands, About, procedure bands → §E 16:9; flat-lay → 3:2; article header → 16:9; how-to-use → ~2:1; OG → 1.91:1.** Today these band sections render **1:1 cover** and hold **square** legacy sources (no visible crop, but they're *not* the §E band format and waste the bag/edge framing the prompts now generate). **Fix = give the band sections a deliberate per-section non-1:1 ratio (the §11 exception) AND supply correctly-ratio'd sources** (regenerate lifestyle/bands per §E). The About band's 3:2 source is the one actively losing content today.

---

## MASTER PER-SLOT MAP

| Slot | Source mechanism | Filled? | Correct source? | Ratio | Notes / fix |
|---|---|---|---|---|---|
| 10 single PDP featured | product.featured_media | ✅ all 10 | ✅ | 1:1 ✓ | Phase 10 done; Pro spray/gel are interim trio-crops (on-record note) |
| 5 bundle PDP featured | product.featured_media | ⚠ 1/5 (clinical-starter only) | ✅ where set | 1:1 | **4 EMPTY** → empty-safe placeholder on those PDPs (B1) |
| PDP variant/gallery media | per-variant media | ❌ none (media=1 each) | n/a | 1:1 | single image per product; no variant-swap media (B) |
| cream/gel/spray collection hero | template image_picker (trio) | ✅ | ✅ | 1:1 src in 1:1 slot | OK |
| 4 procedure collection heroes | collection-hero (no tmpl img + collection.image unset) | ❌ | — | — | renders no hero image (empty-safe) → needs §E 16:9 context (A4/B2) |
| shop-all / aesthetic-numbing-cream heroes | collection-hero, no image | ❌ | — | — | empty-safe text hero; optional context image |
| bundles collection | **default collection.json** (Horizon) | n/a | ⚠ inconsistent | — | uses default template, not the bespoke collection layout (A5) |
| injectable collection heroes ×3 | collection-hero, no image | ❌ | — | — | empty-safe; SEO-background, low priority |
| collection product cards | card-image → product.featured_media | ✅ | ✅ | 1:1 | OK (products all filled) |
| Homepage hero | template image_picker (range-upright) | ✅ | ✅ (square) | 1:1 contain | §E wants 16:9 band → currently square (B3) |
| Homepage "range — UK formulated" band | image-text-band image_picker (cream-spray-gel-trio) | ✅ | ✅ (square) | 1:1 cover | §E lifestyle band = 16:9 (B3) |
| Homepage practitioners band | image-text-band image_picker (range-angled) | ✅ | ✅ (square) | 1:1 cover | §E band = 16:9 (B3) |
| **Homepage "Shop by procedure" cards ×4** | procedure-grid → card-image → linked collection → **first-product fallback** | ✅ but **WRONG** | ❌ | 1:1 | **renders Advanced product bottles, not procedure imagery** (A1) |
| Homepage strength cards ×3 ("decide what you need") | trio-card-row tier_card | n/a (text cards) | — | — | no image rendered; confirm if imagery intended |
| Homepage formats row ×3 | format-row blocks | n/a (text) | — | — | text/label cards |
| About `what` brand band | image-text-band image_picker (about-brand-band) | ✅ | ⚠ **3:2 cropped** | 1:1 cover crops 3:2 | **bag + right edge clipped** (A2) |
| About company/believe/practice bands | image-text-band (image_alt, no image) | ❌ | — | — | empty-safe (no image set) |
| Mega-menu Featured card | dynamic ← professional-numbing-kit-large featured media | ❌ → placeholder | wiring ✅, image ✗ | 4:3→1:1 mobile | shows neutral "Senseless" placeholder; auto-fills when the Pro bundle image lands (B1) |
| Global logo / asterisk | inline theme asset SVG | ✅ | ✅ | n/a | OK |
| OG / social default image | none | ❌ | — | 1.91:1 | no default og:image (B5) |
| Favicon / touch icons | — | ❌ | — | — | not set (B5) |
| How-to-use illustrations | none | ❌ | — | ~2:1 | not created (B5) |
| Article/editorial headers | senseless-article (no ratio constraint) | ❌ | — | 16:9 | no header images (B5) |

---

## (A) SOURCE-WIRING DEFECTS — fix in code/admin (no new art needed for the wiring itself)
- **A1 [P1] Homepage "Shop by procedure" cards render product bottles.** `senseless-procedure-grid` cards link a collection but have no image override, and the 4 procedure collections have **`collection.image` unset**, so `senseless-card-image` falls back to the collection's **first product** → Advanced gel/cream/spray bottles show as "procedure" imagery. **Fix:** set `collection.image` on the 4 procedure collections (procedure context, §E 16:9) or a per-card image override. *(Needs the art too — see B2.)*
- **A2 [P1] About brand band crops a 3:2 source to square.** `image-text-band` forces 1:1 cover; `senseless-about-brand-band` is 3:2 → vanity bag + right edge clipped. **Fix:** give the lifestyle band a deliberate per-section ratio (§E 16:9, §11 exception) or supply a square/band-ratio source.
- **A3 [P2] Lifestyle bands locked to the 1:1 default.** Homepage hero/bands + About bands render 1:1 cover; per §E they should be 16:9 (deliberate exception). Square legacy sources hide it today, but the section ratio is the root fix.
- **A4 [P2] Procedure/shop-all/aesthetic collection heroes have no image source wired** (no template image, no `collection.image`). Empty-safe text heroes now; wire `collection.image`/template image when context art exists.
- **A5 [P3] `bundles` collection uses the default `collection.json`**, not the bespoke collection layout — visual inconsistency vs format collections.

## (B) NEEDS AN IMAGE — make/upload (feeds the prompts doc + photo lane)
- **B1 [P0 launch-gate] 4 bundle featured images** — `clinical-numbing-kit-large`, `advanced-numbing-kit-small`, `advanced-numbing-kit-large`, `professional-numbing-kit-large` (only clinical-starter is filled). 1:1 per §C. **`professional-numbing-kit-large` also feeds the mega-menu Featured card** (currently placeholder). Bundle PDPs + /collections/bundles depend on these.
- **B2 [P1] Per-procedure context imagery** (§E CONTEXT, 16:9) for the 4 procedure collections + the homepage procedure cards (kills the bottle fallback in A1).
- **B3 [P1] Correct-ratio lifestyle bands** — homepage hero/bands + About at §E 16:9 (current ones are legacy 1:1; About's is a cropped 3:2). Regenerate per §E D-LIFESTYLE.
- **B4 [P2] Two Phase-10 bands have no home** — `senseless-home-bundle-social-band` (3:2) + `senseless-procedure-band` (3:2) are **uploaded but unplaced**: the homepage social/bundle band + a procedures-page image band **don't exist as sections yet** (homepage "Complete kits" band is a pending Stage-2 build). Build the sections, then wire (and reconcile ratio per §E flat-lay 3:2 / band 16:9).
- **B5 [P2] Global assets** — default **OG/social image** (1.91:1, prompt exists), **favicon/touch icons** (derive from the asterisk SVG), **how-to-use illustrations** (~2:1, one per format), **article/editorial headers** (16:9, one per article).
- **B6 [P3] Homepage strength/"how we work" cards** are text-only — confirm whether tier/illustration imagery is intended.

## Manifest cross-check (orphans / missing)
- **No slot points at missing media** (no 404s).
- **True orphan:** `senseless-cream-spray-gel-trio-angled` — in the manifest, **uploaded but referenced nowhere** (the homepage product band uses `cream-spray-gel-trio`, not the `-angled` variant). Use it or retire it.
- **Orphan-by-design (ready, unplaced):** `senseless-home-bundle-social-band`, `senseless-procedure-band` (B4 — awaiting their sections).
- The product/collection **record** images (`senseless-clinical-strength-cream` etc.) show as "unreferenced in templates" because they're bound via the **Admin API** (product.featured_media / collection.image), not `shopify://shop_images` — these are correctly used, not orphans.

## Severity roll-up
- **P0 launch-gate:** B1 (4 bundle images — incl. Pro Ultimate feeding the mega card).
- **P1:** A1 (procedure cards show bottles) · A2 (About band 3:2 crop) · B2 (procedure context art) · B3 (16:9 lifestyle bands).
- **P2:** A3, A4 (band/collection ratio + hero wiring) · B4 (missing sections for 2 ready bands) · B5 (OG/favicon/how-to/article headers).
- **P3:** A5 (bundles default template) · B6 (text-card imagery) · orphan cleanup.

## HOLD
Read-only audit complete. No fixes applied. Recommend: B1 first (bundle shots — launch gate), then A1+B2 (procedure cards/context) and A2/B3 (band ratios), then the §11 per-section ratio exceptions for lifestyle bands so 16:9 sources stop being square-cropped.
