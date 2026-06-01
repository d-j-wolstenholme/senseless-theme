# Wave 2 — Product Page 1: Clinical Strength Cream (BASE TEMPLATE)

**Date:** 2026-06-01 (BST) · **Machine:** MacBook Pro · **Branch:** dev
**Theme:** Senseless Dev `#199324434780` (unpublished) · **Checkpoint:** Wave 2 page 1 — STOP (other 9 products not built).
**URL:** /products/clinical-strength-cream (template suffix `clinical-strength-cream`)

## Notion sources read in full
1. Master Rebuild Brief (global rules + build/audit protocol) — https://www.notion.so/37258bc375ea8109813ff0857e42903c
2. Clinical Strength Cream spec — https://www.notion.so/36c58bc375ea8186a047e8ba3ab64748

## Result — ✅ all checks pass (render via storefront password)
- PDP HTTP 200; **theme-check 0 errors** (370 files, 24 pre-existing Horizon warnings).
- **Buy box:** H1 "Clinical Strength Cream"; eyebrow "Clinical Strength · Cream"; size radios 10g/30g; **default 30g**; **live price £44.99** (10g £19.99) — never £TBC; add-to-cart **"Sold out"** (inventory 0); trust line "UK formulated · Cosmetic product · CPSR assessed" (no free-shipping clause).
- **Suitability matrix injectable-clean:** Lip Fillers + Botox **absent**; 5 rows (Microneedling/Laser/SPMU/Waxing×2).
- All 10 sections present in order; reviews section renders **nothing** (hidden, no app block).
- **Related = 2 cards** (Advanced, Professional); **no 10g card**; Professional = 2px purple border + filled purple CTA, **no badge word**; links de-suffixed.
- **Banned words:** none in visible copy (everyday/concentration/concentrated/clinical-grade = 0; "flagship" only as CSS class).
- **No neutral/black CTA borders** anywhere; **no £TBC** anywhere (0).
- **Cross-links de-suffixed** (no -30g/-10g).
- **Schema:** Product (1) + Offer ×2 (£44.99/£19.99 GBP, **OutOfStock**) + BreadcrumbList + FAQPage (6 Q/A). SEO meta title/description set on the product.

## Section reconciliation — reuse / adapt / new
| Map § | Section used | reuse / adapt / new |
|---|---|---|
| 1 Product hero (gallery + buy box) | `senseless-product-hero` | **adapt** — add-to-cart black border → filled purple (button rule) |
| 2 What it's for (suitability matrix) | `senseless-strength-matrix` (`suitability_row` blocks) | **reuse** + **adapt** (CTA black→purple) |
| 3 How to use | `senseless-how-to-use` | **reuse** |
| 4 The Senseless system band | `senseless-decision-band` (2 CTAs) | **reuse** + **adapt** (secondary CTA black→purple) |
| 5 Trust bar | `senseless-trust-bar` | **reuse** |
| Key Facts (GEO) | `senseless-key-facts` | **reuse** |
| 6 FAQ | `senseless-faq-accordion` (FAQPage) | **reuse** |
| 7 Reviews | `senseless-reviews` | **NEW** — Judge.me `@app` block host, hidden until reviews |
| 8 Related (2 cards) | `senseless-cross-sell` | **reuse** + **adapt** (added `cols-2`; related CTA → purple pill, filled for flagship) |
| 9 Aftercare | `senseless-image-text-band` | **reuse** |

**New file:** `sections/senseless-reviews.liquid`. **Adapted (shared, site-wide benefit):** `senseless-product-hero`, `senseless-decision-band`, `senseless-strength-matrix`, `senseless-cross-sell`. No duplicate sections created.

## Spec → build audit (Global-Rule overrides over v1/v2 residue)
| Section | Spec said | Built | Override applied |
|---|---|---|---|
| Hero | eyebrow/H1/subhead; price £TBC; trust line incl. "Free UK shipping over £TBC" | eyebrow "Clinical Strength · Cream", H1 "Clinical Strength Cream", subhead "The clinical baseline…"; **live £44.99**; trust "UK formulated · Cosmetic product · CPSR assessed" | Live price (never £TBC); **dropped free-shipping clause** (Ops blocker); size = variant, default 30g |
| What it's for | 7-row matrix incl. Lip Fillers + Botox | **5 rows, injectable-clean** (Lip Fillers/Botox dropped); CTA Find your strength | Injectable-clean; honest "when NOT to buy" kept |
| How to use | 4 steps, no timings | 4 steps (Clean/Apply/Leave it/Remove); CTA How Senseless works | — |
| System band | "Clinical is the everyday…"; "higher concentration"; "Professional is the flagship" | "Clinical is the standard…"; "higher-strength"; "the highest strength, developed with practitioners" | Banned-word scrub (everyday/concentration/flagship); honest beat kept; CTAs de-suffixed |
| Trust bar | UK formulated · Cosmetic product · **Cruelty-free** · Made for aesthetics | UK formulated · Cosmetic product · **CPSR assessed** · Made for aesthetics | CPSR overrides cruelty-free |
| FAQ | 6 items incl. "Is Clinical enough for lip fillers?"; "higher concentration" | 6 items injectable-clean (lip-fillers FAQ dropped); "higher strength" | Injectable-clean + banned-word reword; FAQPage schema |
| Reviews | hidden until 5+ | `senseless-reviews` @app host, renders nothing now | Judge.me app block (not snippet div) |
| Related | 3 cards incl. 10g + "flagship badge" | **2 cards** (Advanced, Professional); **no 10g**; Professional border + purple CTA, **no badge** | 10g is a variant of this page; no flagship word |
| Aftercare | Foaming Cleanser → /products/senseless-foaming-cleanser | → /products/foaming-cleanser | De-suffixed/canonical slug |

## API / store changes
- Product `templateSuffix` → `clinical-strength-cream`.
- **Variants reordered:** 30g (S30CL, £44.99) position 1, 10g (S10CL, £19.99) position 2 — default 30g.
- SEO: title "Clinical Strength Numbing Cream | Senseless"; description "The clinical baseline: the numbing cream most aesthetic appointments call for. UK-made."

## Flags / pending
- **Judge.me app not installed** on dev — reviews section is present but renders nothing; place the Judge.me app block here once installed (it owns AggregateRating + the 5-review threshold).
- **Images:** gallery + card image slots use neutral placeholder fallback (no external source) per global rule; real product photography swaps in later.
- **Cross-cutting fixes folded in (benefit all pages):** purple CTAs (no black borders) across product-hero/decision-band/strength-matrix/cross-sell; `£TBC` price default removed from cross-sell/product-showcase/product-grid/trio-card-row.
- Interim/Wave-4 links unchanged: /pages/choosing-your-strength, /pages/how-it-works (404 on dev until built).

## Not done (by design — Wave 2 checkpoint)
- The other 9 product pages (build after this base template signs off).

---
**Corrections (follow-up, on top of ec61de8):** (1) **Removed the suitability / "What it's for" section** from the product template entirely (per Canonical State §7 — product pages are ad-facing and carry no suitability; it moves to collections in Wave 3). Render confirms the matrix/heading/CTA are gone with no empty container; sequence is now hero → how-to-use → system → trust → key-facts → FAQ → reviews → related → aftercare. (2) **Constrained the hero gallery image** — `.ss-ph__main` capped at `max-width: 420px` (responsive 4:5 frame; the variant image swaps inside it) so it no longer dominates the viewport. (3) Confirmed the two unverified buy-box items and **added the missing ones**: **Buy it now** dynamic checkout button (`{{ form | payment_button }}`) now renders alongside Add to cart (both reflect sold-out at inventory 0); **variant-linked image swap** wired in the hero JS (`v.featured_image` → main gallery image on 10g/30g change) — mechanism verified in the render, though no visible swap yet because the products have no per-variant media (both show the neutral placeholder until images are assigned). theme-check 0; re-rendered + confirmed. Still the Wave 2 checkpoint.
