# Phase 8 cleanup — injectable meta trims + stale-link repoints

**Date:** 2026-06-04 (BST) · **Branch:** dev · **Theme:** Senseless Dev `#199324434780` (store `senseless-numbing`) · **Commit:** `866c9a9`
Token refreshed (shpca_a64055…). Cleanup of the two flags from the Phase 8 report (`ddfacb3`). Daniel confirmed the 3 commercial pages ARE ad-facing — the injectable-card removal stays.

## 1. Meta trims — 3 injectable collections (now ≤155, compliant)
Set via `global.description_tag` (GraphQL):
- **numbing-cream-for-injections** 156 → **144**: "Topical numbing cream to make injections more comfortable. A UK cosmetic range, formulated in the UK. Always check with your practitioner first."
- **numbing-cream-for-lip-fillers** 160 → **144**: "Topical numbing cream and gel for more comfortable lip filler. A UK cosmetic range, formulated in the UK. Most practitioners numb — check first."
- **numbing-cream-for-botox** 165 → **152**: "Topical numbing cream for Botox. A UK cosmetic range, formulated in the UK. Botox uses fine needles — numbing is optional; check with your practitioner."
All keep "formulated in the UK"; no efficacy/onset/duration/% claims; Botox keeps "optional"; practitioner-routed.

## 2. Stale 301 links on the 3 commercial pages — repointed (template-level)
Repointed every in-template stale link → **`/pages/the-senseless-system`** (direct 200):
- `best-numbing-cream`: choosing-your-strength ×3 → system.
- `senseless-vs-ametop`: choosing-your-strength ×3 + how-it-works ×1 → system.
- `best-emla-alternative-uk`: choosing-your-strength ×3 + how-it-works ×1 → system.
Grep confirms **zero** `choosing-your-strength` / `how-it-works` left in the 3 templates; render confirms **0 body-level stale links** on each page; `/pages/the-senseless-system` resolves **200 direct** (no 301 hop).

## ⚠ Remaining (out of scope — global footer, NOT "these 3 pages only")
Render-verify found each commercial page still shows **2 stale links — but they're in the global FOOTER** (`senseless-footer-explore` menu: "Choosing your strength" → /pages/choosing-your-strength, "How Senseless works" → /pages/how-it-works), which renders on **every** page, not just these 3. That's the **Phase 12 global link sweep**, explicitly outside this brief's "targeted fix on these 3 pages only." Those footer links currently **301** (resolve, not 404 — the redirects exist). Quick fix when wanted: `menuUpdate` on `senseless-footer-explore` (+ the footer "Choosing your format" / "How to apply" slots) → the System guide. Flagging, not doing (global scope).

## Verify
- **theme-check: 0 errors.**
- **Render-verify (live preview):** 3 injectable meta descriptions = 144/144/152 (≤155), compliant (no efficacy/onset/duration/%); 3 commercial pages have 0 body-level stale links + ≥1 system link; `the-senseless-system` 200 direct.
- **Injectable-clean re-confirmed:** grep = **zero inbound** links to the 3 injectable collections from any other file (commercial-page card removal intact, not reverted).

## Files / API
- Edited: `templates/page.best-numbing-cream.json`, `page.senseless-vs-ametop.json`, `page.best-emla-alternative-uk.json` (stale-link repoint).
- API: `metafieldsSet` ×3 (trimmed injectable descriptions).

## HOLD
Meta trims done (≤155, compliant); template-level stale links on the 3 pages repointed to the System guide (direct 200); injectable-clean graph intact. Remaining footer-level 301s flagged for the Phase 12 global sweep.
