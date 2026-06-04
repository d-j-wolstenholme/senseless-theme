# Site-wide internal linking audit (READ-ONLY)

**Date:** 2026-06-04 (BST) · **Branch:** dev · **Theme:** Senseless Dev `#199324434780`. Token refreshed. **No edits made — this is the map for the Phase 12 wiring pass.**

**Method:** crawled 41 surfaces (header + footer captured once as global; homepage; 14 collections; representative products + 1 bundle; all system/guide/policy/company pages; Articles hub; blog hub + 5 articles; commercial pages). Collected every internal `<a href>` (anchor → target), resolved each unique target with `maxRedirects:0` to catch 301s, and cross-checked sources in the repo. Status spread: overwhelmingly **200**, **2 × 301**, **0 × 404**.

---

## 1. Broken (404) — NONE ✅
No internal link resolves to 404. (The two previously-orphaned commercial pages are now live.)

## 2. Stale / 301 — 3 live links (2 retired targets)
Both retired targets DO 301 to a live page, so they "work" but cost a redirect hop on ad-facing pages — repoint at source.

| Source (live) | Anchor | Current target | Status | Fix → |
|---|---|---|---|---|
| Homepage (`index.json`) | "How Senseless works" | `/pages/how-it-works` | 301 | `/pages/the-senseless-system` |
| `collection.aesthetic-numbing-cream` | (how-it-works link) | `/pages/how-it-works` | 301 | `/pages/the-senseless-system` |
| `best-emla-alternative-uk` | "how long does numbing cream last" | `/pages/how-long-numbing-cream-lasts` | 301 | `/pages/using-numbing-cream` |

- **Latent (not currently rendered):** `templates/product.json` (the unused default — all products use per-product suffix templates) links `/pages/how-it-works`. Clean up if that template is ever used. Retired-page templates (choosing-your-strength, how-it-works, does-numbing-cream-work, etc.) also contain stale links, but those pages 301 and don't render — harmless.

## 3. Injectable-clean breach (ad-facing) — NONE ✅
Zero ad-facing surfaces link into the injectable collections (injections / lip-fillers / botox). Header, footer, homepage, all format/procedure collections, products, bundles, procedures hub, Selector, best-numbing-cream, vs-ametop, emla-alt all clean. (Blogs link injectable collections — organic, allowed, not flagged.)

## 4. Redundant CTA — NONE outstanding ✅
The one known case (the System guide's "Find your strength" button, redundant with the embedded Selector) was removed earlier this session. No new same-page-redundant CTAs found.

## 5. `?strength=` links (need the Phase-12 filtered-collection view)
These point at a strength filter that isn't built yet — they currently 200 to the base collection (Shopify ignores the unknown param), so no filtering happens. Wire with the filter build:
- Homepage: "Shop Clinical / Advanced / Professional" → `/collections/numbing-cream?strength={clinical|advanced|professional}` (×3).
- Also emitted by `senseless-collection-grid`, `senseless-product-grid`, `senseless-selector`, and `collection.aesthetic-numbing-cream` (strength filter UI). Confirm all resolve to the filtered view once built; ensure the filtered URLs canonical to the base collection.

## 6. Orphans (live page, no inbound internal links)
- `/pages/senseless-vs-ametop`
- `/pages/best-emla-alternative-uk`

These are **paid-search landing pages** (traffic from ads, just published this session), so zero inbound is expected — but for organic equity, consider one inbound each (e.g. from `best-numbing-cream` or a small "comparisons" block). Everything else has inbound links.

## 7. Anchor-text / duplicate-anchor
**Intended (NOT issues — by design):**
- Format collections link each strength product **twice** — hero word-link ("Clinical") + ladder full-name link ("Clinical Strength Cream"). Deliberate (Peter option C, distinct anchors).
- Articles show "← All guides" **twice** (header eyebrow + footer). Both → `/blogs/guides`.
- Product cards (aesthetic-numbing-cream, bundles grids) link each product **2–3×** per card (image + title + quick-add) — standard card markup.

**Worth a look (SEO):**
- `does-it-hurt-by-treatment`: "Use the Senseless Selector" **×6** → `/pages/the-senseless-system` (one per treatment section — same anchor, same target). Consider varying anchors or reducing.
- `using-numbing-cream` and `faq`: "Make your Selection" **×2** → `/pages/the-senseless-system`.
- No generic "click here"-type anchors found.

---

## Clean surfaces (zero issues)
Policy pages (×5), product pages (cream/cleanser/bundle templates), The Senseless System, FAQ, Contact, About, Trade, Articles hub, blog hub + 5 articles (organic), Shop All, the 3 format collections, the 4 procedure collections, bundles collection, Aesthetic Procedures hub, header (Shop mega + The System + Help), footer (4 columns + legal bar).

## Recommended Phase-12 wiring order
1. Repoint the 3 stale 301 links (§2) — homepage + aesthetic-numbing-cream → the-senseless-system; emla-alt → using-numbing-cream.
2. Build the `?strength=` filtered collection view, then confirm the §5 links filter + canonical.
3. Add one inbound link each to the two commercial landing pages (§6) if organic equity is wanted.
4. (Optional) Trim the repeated Selector anchors on does-it-hurt-by-treatment (§7).

## HOLD
Read-only audit complete. No edits made. This is the map; fixes are the Phase-12 pass.
