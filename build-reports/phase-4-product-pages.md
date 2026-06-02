# Phase 4 — product pages: short description (template) + links-out + meta (all 10)

**Date:** 2026-06-02 (BST) · **Branch:** dev · **Commit:** `6dbc6dc` · **Theme:** Senseless Dev `#199324434780`
**Source:** model `37358bc375ea811da9f8dd59f368fe2a` (lean product-page template). Token refreshed first (`./scripts/refresh-token.sh`; shop = senseless-numbing).

## What changed (all 10 product templates)
The model's correction: **per-product body copy lives in the page TEMPLATE, not the product admin `description`** (our hero doesn't rely on that field). Implemented:
1. **Short description** — new `senseless-rich-text` section after the trust bar, carrying the model's 2–3 line copy **verbatim** (what it is · format + strength · "Formulated in the UK/United Kingdom, CPSR assessed"). Template content, not admin.
2. **Links-out** — new `senseless-link-row` section after key-facts: **(a) "Back to the range" → the product's OWN format collection (REQUIRED — the gap I'd flagged)**; (b) "What it's used for" → the procedure collections that product serves; (c) "Not sure which strength?" → `/pages/the-senseless-system`. (Anchors use target keywords.)
3. **Per-product SEO meta** (title + ≤155 description, primary keyword) set via Admin API for all 10.

Per-product back-to-range + used-for:
| Product | Back to range | Used-for links |
|---|---|---|
| 3× cream | /collections/numbing-cream | microneedling · laser · SPMU · waxing |
| 3× gel | /collections/numbing-gel | microneedling · SPMU |
| 3× spray | /collections/numbing-spray | waxing · laser |
| foaming-cleanser | /collections/numbing-cream (prep pairing) + /pages/aesthetic-procedures | — (aftercare; no strength siblings) |

Resulting order (9 numbing): hero → trust → **shortdesc** → system → howto → key-facts → **linksout** → faq → reviews → related → aftercare. (Cleanser: hero → trust → shortdesc → howto → key-facts → linksout → faq → reviews → pairing.)

## §11 + A–K + Standard-bar (per product) — render-verified one per format + cleanser
Verified live (HTTP 200) on clinical-cream / clinical-gel / clinical-spray / foaming-cleanser; the rest share the same scripted structure + copy.
- **A voice:** short desc verbatim ✅
- **B compliance:** 0 banned; **"formulated in the United Kingdom/UK" not "made"**; reduce-not-eliminate; no efficacy/duration/onset/% ✅
- **C SEO:** primary keyword at **meta** level (title + desc), per §11 surface weighting (not forced into H1) ✅ — titles e.g. "Clinical Numbing Cream | UK-Formulated | Senseless"; desc ≤155 (139–145)
- **F injectable-clean:** links only to format + procedure collections + the guide; no injectable links ✅
- **I slugs:** de-suffixed, relative ✅
- **J components:** square images, variant chips size-only, ATC + Buy-it-now, related siblings ✅ (existing)
- **K build:** **back-to-range present on all** (render + Asset-API confirmed); theme-check **0**; Asset-API diff clean (slash-normalized) ✅
- **Std-bar:** short desc carries the keyword once; depth deferred to collections (lean) ✅

## Honest scope note (what's done vs the fuller lean model)
The user's two explicit Phase-4 deltas are **done on all 10**: short-description-in-template + back-to-range link (+ used-for + guide links + meta). The model's **fuller lean restructure is NOT fully applied** and is flagged for a follow-up:
- **how-to-use** section still present (model moves application into the FAQ on lean pages).
- **§4 "system band" (3×3 with this product highlighted)** not built — the model gives no exact copy for it and it'd need a bespoke 3×3 highlight section; the guide link in links-out covers "see the system" for now.
- **FAQ** still runs 7–8 Q&As (model says 3–4 lean); existing governed FAQ kept rather than trim 10× without per-product trim copy.
- **aftercare** is still `image-text-band` (editorial) on the 9 numbing pages; model frames aftercare as a cleanser cross-sell.
These are deliberate holds (un-modeled copy / 10×-edit risk), not misses — decide whether to run the full lean trim next.

## HOLD
Short description (template) + back-to-range + meta live + verified on all 10. Fuller lean trim flagged. Nothing else started.
