# Wave 2 — All 10 product pages (§7 re-order of page 1 + products 2–10)

**Date:** 2026-06-01 (BST) · **Machine:** MacBook Pro · **Branch:** dev
**Theme:** Senseless Dev `#199324434780` (unpublished) · **Checkpoint:** Wave 2 complete — STOP.

## Notion sources read in full
1. 🟢 Canonical State (§1 live range/prices, §7 product-page rules + section order, §9 finishing list, §10 related-cards rule) — https://www.notion.so/37258bc375ea813e895ccbe38c0cadc8
2. Master Rebuild Brief (global rules + audit protocol) — https://www.notion.so/37258bc375ea8109813ff0857e42903c
3. Per-product meta from the Master Page Database (queried the default view). *Note: the DB product meta is banned-word stale ("everyday / concentration / flagship / clinics / considered upgrade") — per the build protocol I composed compliant meta and scrubbed those.*

## Section order (Canonical State §7) — applied to ALL product pages
`product-hero → trust bar → system band → how-to-use → key-facts → FAQ → reviews → related → aftercare`
(Trust bar directly under the hero; application steps below the system band. Page 1 was re-ordered to match — Step 0.)
**Foam (cleanser):** `product-hero → trust bar → how-to-use → key-facts → FAQ → reviews → cross-sell(pairing)` — no system band, no strength framing, no tier row.

## Result — ✅ all 10 pass (theme-check 0; rendered each via storefront password)
Verified per page: §7 order; **live price** (correct default variant) never £TBC; **size selector only on multi-size**; **Add to cart + Buy it now**; sold-out at inventory 0; **no suitability**; injectable-clean; **0 banned words in visible copy** ("flagship" exists only as a CSS class); `Product+Offer(OutOfStock)+BreadcrumbList+FAQPage` schema.

| # | Product | default price | sizes / selector | system band siblings | related (Professional = flagship) |
|---|---|---|---|---|---|
| 1 | clinical-strength-cream | 30g £44.99 | 10g/30g · selector | Advanced, Professional | Advanced + **Professional** |
| 2 | advanced-strength-cream | 30g £49.99 | 10g/30g · selector | Clinical, Professional | Clinical + **Professional** |
| 3 | professional-strength-cream | £55.99 | 30g · **no selector** | Clinical, Advanced | Clinical + Advanced |
| 4 | clinical-strength-gel | 35ml £34.99 | 15ml/35ml · selector | Advanced, Professional | Advanced + **Professional** |
| 5 | advanced-strength-gel | 35ml £39.99 | 15ml/35ml · selector | Clinical, Professional | Clinical + **Professional** |
| 6 | professional-strength-gel | 35ml £44.99 | 15ml/35ml · selector | Clinical, Advanced | Clinical + Advanced |
| 7 | clinical-strength-spray | £19.99 | 100ml · **no selector** | Advanced, Professional | Advanced + **Professional** |
| 8 | advanced-strength-spray | £24.99 | 100ml · **no selector** | Clinical, Professional | Clinical + **Professional** |
| 9 | professional-strength-spray | £29.99 | 100ml · **no selector** | Clinical, Advanced | Clinical + Advanced |
| 10 | foaming-cleanser | £19.99 | 150ml · **no selector** | — (no system band) | pairing: Numbing Cream + Clinical Cream (not a tier row) |

*Professional product pages correctly carry no flagship card (their siblings are Clinical + Advanced).*

## Section reconciliation — reuse / adapt / new
- **No new sections** this batch. All 10 templates reuse the Clinical base set: `senseless-product-hero`, `senseless-trust-bar`, `senseless-decision-band` (system band), `senseless-how-to-use`, `senseless-key-facts`, `senseless-faq-accordion`, `senseless-reviews`, `senseless-cross-sell` (related / foam pairing), `senseless-image-text-band` (aftercare). No duplicate sections.
- **Adapted — `senseless-product-hero` (site-wide):**
  1. **Buy it now** dynamic checkout button (`{{ form | payment_button }}`) alongside Add to cart.
  2. **Variant-linked gallery image** — JS swaps the main image to the variant's `featured_image` on size change (dormant until per-variant media exists).
  3. **Gallery image capped** at `max-width: 420px` (was oversized).
  4. **Size selector only when `variants.size > 1`** — single-size products (Professional cream, all sprays, foam) show no selector.
- **Re-ordered:** page 1 (Clinical) to the §7 order (trust up, application down).
- **Foam** uses a tighter composition of the same sections (no system band; "not a numbing product" FAQ; aftercare-pairing cross-sell).

## API / store changes
- `templateSuffix` set on all 10 products (= handle).
- **Variants reordered for default-larger-size:** advanced-cream→30g, advanced-gel→35ml, clinical-gel→35ml, professional-gel→35ml (clinical-cream 30g already; single-size products n/a).
- **SEO meta** set per product — compliant, composed (DB meta was banned-word stale).

## Flags / pending
- **Judge.me not installed** on dev (Canonical State §9 launch-gate) — every product's reviews section is an app-block host that renders nothing until the block is dropped in; hero star badge + AggregateRating/Review JSON-LD pending install (verify on render at integration, don't assume).
- **Images:** gallery + card slots use neutral placeholder fallback (no external source); per-variant image swap is wired but dormant until product media is assigned.
- Wave-4 `/pages/*` links 404 on dev until built (how-it-works, choosing-your-strength).
- **Suitability content** intentionally absent from product pages — to be surfaced on the **collection** pages in Wave 3 (Canonical State §7/§10).

## Not done (by design — Wave 2 checkpoint)
- Wave 3 (collections), Wave 4 (guides/pages), Wave 5 (repoint pass). Cookie-consent banner (Canonical State §6) recommended next.
