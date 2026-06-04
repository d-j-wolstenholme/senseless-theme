# Peter's requests — stacked three-strength callout + first-mention body links

**Date:** 2026-06-04 (BST) · **Branch:** dev · **Theme:** Senseless Dev `#199324434780` · **Commits:** `0eaf1be` (R1 collections), `461c7e2` (R1 product pages), `4e6cd9d` (R2). Token refreshed.

## REQUEST 1 — Stacked three-strength callout, each hyperlinked (full product name)
**Format collections (`0eaf1be`):** the `senseless-strength-ladder` block gained a `link` URL setting (rendered in the manual-block path; the metaobject path already linked). On numbing-cream / numbing-gel / numbing-spray, each ladder row now shows the **full product name** linking to that product, and `use_metaobject` was set to **false** (the shared `strength_tier` metaobject can't produce per-format full names). Verified: 3 stacked links per collection → correct `/products/*`.

**Product pages (`461c7e2`):** new **`senseless-strength-links`** section — a lean stacked list of the three strengths in the *current product's format*, each linking to that product (full name anchor), resolved **dynamically** from the format collection by `product.type`. The 10 products use **per-product template suffixes** (`product.{handle}.json`, not the shared `product.json`), so it was added to the 9 strength-product templates. Verified: cream/gel/spray PDPs each list their 3 siblings with "You're viewing this" on the current one; cleanser renders nothing.

## REQUEST 2 — First-mention body hyperlinks (first meaningful mention only)
First body-prose mention only, descriptive anchor, format name → format collection (`4e6cd9d`):
| Page | First mention linked |
|---|---|
| /pages/does-microneedling-hurt | "numbing gel" → /collections/numbing-gel |
| /pages/does-laser-hair-removal-hurt | "spray" → /collections/numbing-spray |
| /pages/best-numbing-cream | "numbing cream" → /collections/numbing-cream |
| /collections/numbing-cream-for-semi-permanent-makeup (SPMU) | "Gel" → /collections/numbing-gel |
| /collections/numbing-cream-for-waxing | "Spray" → /collections/numbing-spray |

**Assessed, no edit (rationale):**
- **the-senseless-system** — already links all 3 format collections; adding inline body links would duplicate (violates first-mention-only).
- **senseless-vs-ametop**, **best-emla-alternative-uk** — already link 5 collections each; no clean *unlinked* first format/product prose mention (they use the brand "Senseless" + competitor names, not a linkable format/product first-mention). Left to avoid over-linking.
- SPMU/waxing were collections (not /pages/); microneedling/laser are /pages/.

## Compliance / SEO discipline
- **First meaningful mention ONLY** — each edit wrapped exactly one occurrence (asserted unique at edit time); no second-or-later occurrence linked.
- **Descriptive anchors** (format/product names), never bare/generic.
- **Injectable-clean** — grep across all 5 touched ad-facing pages: zero inbound to the 3 injectable collections.
- No `?strength=` links created (Phase 12). About/Contact/policies/FAQ untouched.
- Did not regress existing links, the Professional 2px #6B3FA0 border, or quick-add.

## Verify
- **theme-check: 0 errors.** Pushed via CLI; combined-push pruning handled (sections pushed before templates; `use_metaobject` re-pushed).
- **Render (Playwright):** R1 collections — 3 stacked full-name links each → correct products; R1 product pages — correct per-format siblings + current marker; R2 — each page shows its single new descriptive body anchor (other counts to the same dest are global nav/footer, not body).

## Files
- New: `sections/senseless-strength-links.liquid`. Edited: `sections/senseless-strength-ladder.liquid`, `templates/collection.numbing-{cream,gel,spray}.json`, the 9 `templates/product.{strength}-strength-{format}.json`, `templates/product.json`, `templates/page.does-microneedling-hurt.json`, `templates/page.does-laser-hair-removal-hurt.json`, `templates/page.best-numbing-cream.json`, `templates/collection.numbing-cream-for-{semi-permanent-makeup,waxing}.json`.

## HOLD
Both of Peter's requests complete + verified. Remaining queued briefs: Blog + Article Hub + 6 ports; 5-bundle product line.
