# Wave 3 — Stage 2 batch 1: Numbing Gel + Numbing Spray collections

**Date:** 2026-06-02 (BST) · **Machine:** MacBook Pro (continued) · **Branch:** dev · **Commit:** `75c9eb2`
**Theme:** Senseless Dev `#199324434780` (unpublished) · **Store:** senseless-numbing.myshopify.com
**Scope:** Rebuild `/collections/numbing-gel` + `/collections/numbing-spray` to their Stage-2 model copy, exact. Reuse Stage-1 modules + the §8 quick-add card (no new sections); vary composition so the pages don't clone each other or Numbing Cream. **HOLD** after both for the Gel+Spray checkpoint.

## Sources read in full (verbatim)
- 🟢 Gel model — https://www.notion.so/37358bc375ea81f0a5acee4abe1f236a
- 🟢 Spray model — https://www.notion.so/37358bc375ea816c8528f539e288a7df
- Range/prices confirmed against live variants (Canonical §1) — the Master Page DB gel/spray specs are STALE ("two strengths / no Clinical") and were NOT used.

## Range reconciled (built from model = Canonical §1, not the stale DB)
- **Gel = 3 strengths × 15ml + 35ml.** Clinical 15ml £19.99 / 35ml £34.99 · Advanced £24.99 / £39.99 · Professional £29.99 / £44.99. Quick-add **15ml/35ml** selector.
- **Spray = 3 strengths × 100ml single-size (NO selector).** Clinical £19.99 · Advanced £24.99 · Professional £29.99.
- Stale **"two strengths" / "Why no Clinical spray?"** residue deleted (rebuilt templates; 0 occurrences confirmed on remote).

## Composition variation (no clones, no new sections)
Same 9-beat model order on all three (hero → trust → The Senseless Scale → grid → format check → philosophy → honest bit → what makes it Senseless → FAQ), differentiated by band/treatment:
| Module | Cream (S1) | Gel | Spray |
|---|---|---|---|
| Trust band | canvas | surface | canvas |
| Strength ladder band | surface | canvas | surface |
| Philosophy (editorial) | white / left | **canvas** / left | **dark** / left |
| Honest bit (callout) | brand | **neutral** | brand |
| Characteristics (key-facts) | surface | surface | **canvas** |
| §3 eyebrow | "Selection" | "The Senseless Scale" | "The Senseless Scale" |

## §11 QA gate + A–K Master Rubric (collections)
Both pages render-verified on the preview theme (Playwright). All checks PASS for **both** unless noted.

| # | Dimension | Gel | Spray |
|---|---|---|---|
| **A** | Brand voice (verbatim model copy) | ✅ | ✅ |
| **B** | Compliance — 0 banned; no hours/onset/%/mechanism; "Is this a medicine? No."; **no "made in the UK"**; no pain-elimination | ✅ 0 | ✅ 0 |
| **C** | SEO primary KW — H1 + §3 heading + intro + §4 grid heading + image alt + meta | ✅ *numbing gel* | ✅ *numbing spray* |
| **D** | Long-tail / FAQ | ✅ 8 Q&As (when-vs-cream, is-gel-stronger, size, apply…) | ✅ 8 Q&As (when-vs-cream/gel, is-stronger, apply-evenly, coverage…) |
| **E** | GEO/schema | ✅ CollectionPage+ItemList+BreadcrumbList+**FAQPage(8)** | ✅ same |
| **F** | Injectable-clean | ✅ format row = Cream+Spray; no injectable links/terms | ✅ format row = Cream+Gel; no injectable links/terms |
| **G** | Range integrity | ✅ 3 strengths, 15ml/35ml; "three" not "two"/"four" | ✅ 3 strengths, 100ml; no "Why no Clinical" |
| **H** | Trust signals | ✅ 4 locked | ✅ 4 locked |
| **I** | De-suffixed slugs | ✅ /products/*-strength-gel | ✅ /products/*-strength-spray |
| **J** | §8 quick-add card | ✅ 3 cards, **15ml/35ml chips**, qty stepper, add="Sold out" (0 stock), 1 `--pro`, no "flagship" | ✅ 3 cards, **no selector** (single-size), qty stepper, add="Sold out", 1 `--pro`, no "flagship" |
| **K** | Build hygiene | ✅ theme-check 0; MANUAL sort C→A→P (verified); live prices £34.99/£39.99/£44.99 (35ml default); meta 140; Asset-API diff clean (use_metaobject survived) | ✅ theme-check 0; MANUAL sort C→A→P; live prices £19.99/£24.99/£29.99; meta 149; Asset-API diff clean |
| — | The Senseless Scale (metaobject) | ✅ reads `strength_tier`, order C→A→P, accents Prof #6B3FA0 / C+A #1A1816 | ✅ same |

## Meta (set via Admin API, both ≤155)
- Gel: `Numbing Gel | Three Strengths, UK-Formulated | Senseless` · desc 140.
- Spray: `Numbing Spray | Three Strengths, UK-Formulated | Senseless` · desc 149 (model desc tail-trimmed per its "(≤155 — trim tail)" note; kept the "Three strengths: Clinical, Advanced, Professional" clause, shortened "awkward-to-reach areas" → "awkward areas" to fit while keeping strengths in the meta).

## Flags / open items
- **Add-to-cart not exercisable** until stock set (cards correctly "Sold out"); mechanics proven in Stage 1.
- **Gel card default variant = 35ml** (first variant in product order) → shows £34.99/£39.99/£44.99; 15ml selectable via chip. If 15ml-first is preferred as the default price shown, reorder variants per product (flag — not specified in model).
- **Spray secondary KW "numbing spray for injections"** is NOT surfaced: the model's verbatim copy doesn't contain it, and "do not recompose" + injectable-clean mean I didn't invent injection-mentioning copy. If wanted, add it to the model copy and I'll ship it (no injectable link either way).
- **Judge.me per-card stars** pending app install (launch-gate).

## HOLD — Gel+Spray checkpoint
The four procedure collections (Microneedling, Laser, SPMU, Waxing) **NOT started** — awaiting approval of Gel + Spray. (Track B store-integrity pass runs separately.)
