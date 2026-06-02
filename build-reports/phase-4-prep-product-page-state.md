# Phase 4 prep — product-page state audit (10 products, report-only)

**Date:** 2026-06-02 (BST) · **Branch:** dev · **Theme:** Senseless Dev `#199324434780`
**Purpose:** snapshot every product PAGE so the product-page model copy can be written against reality. **No changes made.**

> ⚠ **Admin API token is currently 401** (the `.env` `SHOPIFY_ACCESS_TOKEN`, prefix `shpca_…`, worked earlier today but has since rotated/expired). This report is built from the **local template files** + state **verified earlier this session** (Track B suffix audit; the smaller-size-first variant reorder; §1 prices; the Wave-2 product-page build). **Live-only fields** — current admin description content, media counts, live variant order/prices/availability — need a **refreshed token** to re-confirm; flagged per row.

## Shared structure (all 9 numbing products)
Custom template `product.<handle>.json` (suffix set — Track B confirmed all 10 correct → **none on the Horizon default**). Section order:
**product-hero → trust-bar → decision-band → how-to-use → key-facts → faq-accordion → reviews → cross-sell → image-text-band.**
- **product-hero** renders: product title, live price, **size selector only when `variants.size > 1`**, **Add to cart** (filled) + **Buy it now** (`payment_button`), variant→image gallery swap, and **the product's admin `description`** as the body (`{% if p.description != blank %}` — empty if the admin field is blank). Gallery + thumbs now **1:1 square**.
- **trust-bar** = 4 locked signals (built). **decision-band** = links to the *other two strengths in the same format* (built) — **note: no link up to the product's own format collection.** **how-to-use** = application steps + "Before you apply" lead (built, Wave-2 copy). **key-facts** = fact blocks + fixed "UK cosmetic… not a medicine" line (built). **faq-accordion** = substantive Q&As (built). **reviews** = Judge.me app-block host (renders nothing until the app is installed — launch-gate). **cross-sell** = aftercare → Foaming Cleanser (built). **image-text-band** = editorial image+text (built; 1:1 square).
- **Schema** (Wave-2): Product + Offer (**OutOfStock** at 0 inventory) + BreadcrumbList + FAQPage.

## One-table state

| Product | Template (suffix) | What's BUILT | What's MISSING / placeholder |
|---|---|---|---|
| **clinical-strength-cream** | custom `clinical-strength-cream` | 9 sections; size selector **10g/30g** (smaller-first); ATC+Buy-now; how-to-use, key-facts, **FAQ 8**, decision-band→adv/pro cream, cross-sell→cleanser, editorial; schema | **Admin description** (hero body) likely empty†; **images placeholder**; reviews empty (Judge.me); ATC "**Sold out**" (inv 0); `/pages/how-it-works` interim 404; no link to /collections/numbing-cream |
| **advanced-strength-cream** | custom | as above; selector **10g/30g**; **FAQ 8**; decision→clinical/pro cream | same † + images/reviews/sold-out/interim-link |
| **professional-strength-cream** | custom | as above; **30g only → NO size selector**; **FAQ 8**; decision→clinical/adv cream | same † + images/reviews/sold-out/interim-link |
| **clinical-strength-gel** | custom | selector **15ml/35ml** (smaller-first); **FAQ 8**; decision→adv/pro gel | same † |
| **advanced-strength-gel** | custom | selector **15ml/35ml**; **FAQ 8**; decision→clinical/pro gel | same † |
| **professional-strength-gel** | custom | selector **15ml/35ml**; **FAQ 8**; decision→clinical/adv gel | same † |
| **clinical-strength-spray** | custom | **100ml single → NO selector**; **FAQ 7**; decision→adv/pro spray | same † |
| **advanced-strength-spray** | custom | **100ml single → NO selector**; **FAQ 7**; decision→clinical/pro spray | same † |
| **professional-strength-spray** | custom | **100ml single → NO selector**; **FAQ 7**; decision→clinical/adv spray | same † |
| **foaming-cleanser** | custom `foaming-cleanser` | **7 sections** (no decision-band, no editorial): product-hero → trust → how-to-use → key-facts → **FAQ 4** → reviews → cross-sell; links /collections/numbing-cream + clinical-cream | **Admin description** †; images placeholder; reviews empty; sold-out; `/pages/how-it-works` interim; "not a numbing product" framing per Wave-2 |

† **Admin product `description`** = the hero body copy; whether it's populated is admin-side and could not be re-checked (401). This is the **primary target for the product-page model copy** — the templates are built, the prose body is the gap.

## Variants / prices (verified earlier this session — re-confirm live once token refreshed)
- **Cream:** 10g/30g (Professional 30g only). Reordered **10g-first**. Prices (§1): Clinical £19.99/£44.99 · Advanced £24.99/£49.99 · Professional £55.99 (30g).
- **Gel:** 15ml/35ml, all three strengths. Reordered **15ml-first**. Clinical £19.99/£34.99 · Advanced £24.99/£39.99 · Professional £29.99/£44.99.
- **Spray:** 100ml single-size. Clinical £19.99 · Advanced £24.99 · Professional £29.99.
- **Foaming Cleanser:** single size; price not captured here (needs live confirm).
- **Inventory 0 across all → ATC "Sold out" / Offer OutOfStock** (correct pre-launch).

## Links out (per template)
- Every numbing product: `/pages/how-it-works` (**interim — 404 until Wave 4**), the **two sibling strengths** (decision-band), `/products/foaming-cleanser` (cross-sell aftercare).
- Cleanser: `/collections/numbing-cream`, `/products/clinical-strength-cream`, `/pages/how-it-works`.
- **Observation for the model:** product pages do **not** link up to their own format collection (only sideways to sibling strengths). Worth deciding whether the model adds a "back to the range" link.

## Summary for the copy model
- **Templates + sections are fully built and consistent** across all 10 (custom templates, not Horizon default); variants/selectors/prices/schema wired; 1:1 images; ATC correctly Sold-out at 0 stock.
- **The real gap is content, not structure:** (1) the **hero `description` body** (admin field — the main copy to write per product); (2) real **images** (placeholders now); (3) **Judge.me reviews** (launch-gate); (4) `/pages/how-it-works` (Wave-4 page). The how-to-use / key-facts / FAQ copy already exists in the templates (Wave-2) — the model can refine or keep.

## Template assignment (#1) — from the Track B audit earlier this session (live API re-confirm blocked by 401)
All 10 products carry a **bespoke Senseless template suffix** (`product.<handle>`), each matching a deployed template file — **none on the Horizon default** `product.json` (which exists but is unused by these 10). This was confirmed live in the Track B store-integrity pass earlier today (`build-reports/track-b-store-integrity.md`); it cannot be re-queried right now because the Admin token 401s. Re-verify with a refreshed token if a fresh API read is required.

## Blog / awareness content scaffolding (separate confirm)
- **Blog + article templates exist as Horizon STOCK defaults:** `templates/blog.json` + `templates/article.json` (auto-generated; use Horizon's `main-blog`, `main-blog-post`, `featured-blog-posts` sections). **No `senseless-*` sections** in them → **no bespoke Senseless blog/article template** yet.
- So the theme *can* render a blog/articles (default styling), but the pain/awareness content (e.g. "does laser hair removal hurt") has **no branded template** and — per the Track B audit — the related awareness targets are currently **page-template stubs with no page resources** (`how-long-numbing-cream-lasts`, `does-numbing-cream-work`, `senseless-vs-ametop`, etc. exist as `page.*.json` templates but no live pages; only `contact` exists as a page).
- **Whether any blog or articles exist as content resources is unverified** (Admin API 401). For Wave-4 awareness content, a decision is needed: bespoke Senseless blog/article template + a blog, vs. building them as pages (the existing page-template route).

## HOLD
Report only. No fixes, no building. **Action for Daniel:** refresh `SHOPIFY_ACCESS_TOKEN` in `.env` (current one 401s — token rotated since earlier today) so live fields (descriptions, media, prices/availability, blog/article existence) can be re-confirmed before/with the Phase-4 build.
