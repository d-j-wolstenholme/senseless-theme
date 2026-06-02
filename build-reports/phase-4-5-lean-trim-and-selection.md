# Phase 5 wording + Phase 4 full lean trim

**Date:** 2026-06-02 (BST) · **Branch:** dev · **Commits:** `b0f0496` (Task 1), `d2c36e5` (Task 2) · **Theme:** Senseless Dev `#199324434780`
Token refreshed earlier this session (`./scripts/refresh-token.sh`).

## Task 1 — Phase 5: "Senseless Selection" wording (System guide)
Re-pulled the updated model (`37358bc375ea81b6a070e7e2145c7bf7`) and applied verbatim to `/pages/the-senseless-system`:
- Hero **"Make your Senseless Selection"** (italic accent **Selection**) + new subhead ("Within the Senseless System, your selection has two parts…").
- §2 body → the "Making your Senseless Selection means two choices…" wording.
- §3 **"Selection one: the format"** · §4 **"Selection two: the strength"** · §5 **"Putting your selection together: what we recommend by procedure"**. (dial1 eyebrow "Dial one" → "Selection one".)
- **Accent map:** Selection · System · format · strength · procedure · skip (route head clean).
- **Render-verified (200):** H1 "Make your Senseless Selection"; all 6 accents render one-per-head at **weight 500**; "Two dials" gone. theme-check 0; Asset-API diff clean.

## Task 2 — Phase 4: full lean trim (all 10 product pages)
Per the model's new **Lean trim spec**. Lean order now: hero → trust → short desc → **system band** → key facts → links-out → **FAQ (trimmed)** → reviews → related → **aftercare (1-line)**.

**A · System band (§4) — NEW `senseless-system-band`:** compact **3×3** (rows = Cream/Gel/Spray, cols = Clinical/Advanced/Professional = the 9 numbing products). Current product's cell filled **#6B3FA0** (no link); the other 8 link to those products (de-suffixed). Eyebrow "The Senseless System"; caption "Every format comes in three strengths. You're looking at the [format], at [strength] strength." No prices. **Cleanser:** no 3×3 — a one-line callout: "The Foaming Cleanser sits outside the strength range — it's aftercare, used before and after, never numbing." (verified rendering).

**B · FAQ (§7) — trimmed to the 4** (how-to-use folded into the first answer; extras dropped):
- How do I apply it? (thick visible surface layer · cover/occlude · apply-before window — cream ~45–60 min "varies" caveat / gel·spray "allow time" · patch test 24h) — per-format copy.
- How long before my appointment? (window + caveat, no hour claims).
- How long does it last? (three-variable fade, no hours).
- What size should I get? — **multi-size only**; single-size products (Professional cream, all sprays) drop it → **3 FAQs**.
- **Cleanser FAQ** swapped to: what's it for / when do I use it / is this a numbing product (no) / what's in it.

**C · Aftercare (§10):** the editorial `image-text-band` removed; replaced with a **single-line Foaming Cleanser cross-sell** (`link-row`, one item → /products/foaming-cleanser). how-to-use section removed (folded into FAQ).

**D · Kept unchanged:** buy box (product-hero), trust bar, short description, key facts, links-out (with the back-to-range up-link), reviews host, related siblings.

### §11 + A–K + Standard-bar (per product) — render-verified one per format + cleanser
| Dim | Result |
|---|---|
| A voice | ✅ governed application/longevity copy; verbatim model where given |
| B compliance | ✅ 0 banned; **reduce-not-eliminate**; no hour-duration/onset/% (longevity = 3-variable fade); "formulated in the UK/United Kingdom" |
| C SEO | ✅ primary kw at meta (set Task earlier); not forced into H1 |
| E GEO | ✅ key-facts strip + FAQPage(3–4) + system band names The Senseless System |
| F injectable-clean | ✅ links → format + procedure collections + guide; no injectable links |
| G range | ✅ 3×3 shows three formats × three strengths; current highlighted |
| H/I | ✅ trust 4; de-suffixed/relative links; **back-to-range present** |
| J components | ✅ system band (9 cells, 1 current), FAQ 4/3, 1-line aftercare, square images |
| K build | ✅ theme-check 0; Asset-API diff (system-band present, how-to absent, faq=4, aftercare link-row); pushed |
| Std-bar | ✅ lean: buy + decide-in-context + depth on collections |

**Verified live:** clinical-cream (3×3 current=Clinical, FAQ 4), advanced-gel (current=Advanced, FAQ 4), clinical-spray (current=Clinical, FAQ 3, single-size), foaming-cleanser (one-line band, FAQ 4). All 200; how-to + editorial gone; caption + back-to-range correct.

### Build fix logged
First push errored "Section id 'howto' must exist in order" — I'd removed `howto` from `order` but left the orphan section object. Deleted the orphaned `howto` section from all 10 → pushed clean. (Lesson: when dropping a section, delete it from BOTH `sections` and `order`.)

## HOLD
Both tasks done + live + verified. The fuller lean model is now fully applied (system band + FAQ trim + aftercare tidy). Nothing else started.
