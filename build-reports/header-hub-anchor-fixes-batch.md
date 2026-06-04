# Header / hub / anchor fixes — batch (2026-06-04)

**Branch:** dev · **Theme:** Senseless Dev `#199324434780` · **Commits:** `b9b5726` (anchor + System button + hero links), `fe6f489` (procedures hub). Menu changes via `menuUpdate` API (no theme files). Token refreshed.

## 1. Shop mega-menu regression (FIXED)
**Cause (reported):** NOT the strength commits the brief guessed — it was my **policy-era `menuUpdate`** (`scripts/policy-menus-redirects.py`) which rebuilt `senseless-main` two levels deep and **dropped the grandchildren** under By format / By procedure / By strength. The header renders the styled columns **and** the "Shop all" CTA only inside `has_grandchildren` (senseless-header.liquid); with no grandchildren it falls through to a bare `<ul>` and skips the CTA — exactly the "plain list, Shop All missing" symptom.
**Fix:** `menuUpdate` restored the three axes' grandchildren → columns + the "Shop all" button return. Injectable-clean (By procedure = micro/laser/SPMU/waxing only). Reconstructed column contents (originals weren't recoverable): By format = the 3 formats + cleanser; By procedure = the 4 non-injectable procedures + See all; By strength = Clinical/Advanced/Professional → the lead cream product each + Find your strength.
**Note:** the "Shop all" sits at the **bottom** (the Phase-8 documented known-good deduped the top group to the bottom button). The brief said "at the top" — flagging the discrepancy; restored the documented known-good.
**Verified:** 3 columns (By format/procedure/strength) + Shop all → /collections/shop-all + 0 injectable inbound.

## 2. By-format "See all" removed (FIXED)
`menuUpdate` dropped the By-format column's "See all" item (the formats are the complete set; a See all could only dump to the full catalogue — ad-facing injectable-clean risk). **Kept** the By-procedure See all + the Shop all button. Verified: By format seeAll=false, By procedure seeAll=true, Shop all present. Intended asymmetry, by design.

## 3. "Match the strength" anchor overshoot (FIXED)
**Cause:** the always-sticky header + banner overlap in-page anchor jumps (browser scrolls the target to top:0, under the fixed chrome). The `#match` id is already on the section top (good), so only an offset was needed.
**Fix:** global `scroll-margin-top` on `[id]` targets in `layout/theme.liquid` — **145px desktop / 120px mobile** (≈ header+banner height). Covers `#match`, `#shop` (hero "Shop the cream range"), `#faq`, `#selector` site-wide.
**Verified:** clicking "Match the strength" → section top lands ~145px (just below chrome), eyebrow/heading fully visible, no overshoot; mobile offset applied.

## 4. System guide redundant CTA removed (FIXED)
Cleared the strength-matrix `cta_label` on `page.the-senseless-system` (the "Find your strength →" button). The matrix CTA wrapper is conditional (`if cta_label != blank`) so it drops cleanly — no empty container/gap. **Kept:** the embedded Selector, the strength matrix, and the "between strengths" line. The header mega "Find your strength" link is untouched. Verified: `.ss-sm__cta` absent; matrix + selector present.

## 5. Hero three-strength links — Peter option C (BUILT)
The 3 format-collection **hero subheads** now link each strength **word** (Clinical / Advanced / Professional) to that strength's product **in the current format** (cream→cream, gel→gel, spray→spray). Anchor = the strength word (deliberately different from the ladder module's full-name anchors, so the two links on the page aren't identical). The R1 strength-ladder links are unchanged (page now links each product twice — intended). Injectable-clean. **Verified:** gel hero → gel products, spray hero → spray products (no wrong-format), ladder intact.

## 6. Aesthetic Procedures hub styled + framing intro (BUILT)
**Cause: (b) — always plain.** The page used Horizon's `main-page` rendering the admin page body (plain `<h2>` + `<ul>` links); never styled. Not a regression (last touched Phase 6). 
**Fix:** rebuilt with `senseless-guide-hero` (H1 + **framing intro**: "The aesthetic treatments Senseless makes a numbing preparation for…" — frames the four as the served set, not an exhaustive list, so the excluded injectables don't read as missing) + two `senseless-trio-card-row` card rows (By procedure: 4 cards; By format: 3 cards) + the existing Selector callout. **Injectable-clean** (only microneedling/laser/SPMU/waxing). Verified: styled cards, all links resolve, 0 injectable inbound.

## Verify (all)
- **theme-check: 0 errors.** Push via CLI; menu changes via `menuUpdate`.
- Password render (Playwright) confirmed each item above. Nothing else regressed: strength-ladder `link` feature + Peter's callouts intact; mobile drawer/header unaffected.

## Files / API
- Edited: `layout/theme.liquid` (anchor offset), `templates/page.the-senseless-system.json` (matrix CTA cleared), `templates/collection.numbing-{cream,gel,spray}.json` (hero links), `templates/page.aesthetic-procedures.json` (restyled).
- API: `menuUpdate` ×2 (restore Shop grandchildren; remove By-format See all).

## Flag
- Shop mega "Shop all" is at the **bottom** (Phase-8 known-good), not the top as the regression brief described — confirm if you want it moved to the top of the panel (a small header-markup change).

## HOLD
All six items fixed/built and verified.
