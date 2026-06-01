# Wave 2 — Completion pass (application copy + buttons + §11/Master Rubric audit)

**Date:** 2026-06-01 (BST) · **Machine:** MacBook Pro · **Branch:** dev
**Theme:** Senseless Dev `#199324434780` (unpublished) · theme-check **0 errors** · all 10 rendered + verified via storefront password.

## Sources read in full
- 🟢 Canonical State §7 (application wording + button layout) + §10 (related) + **§11 per-page QA gate** — https://www.notion.so/37258bc375ea813e895ccbe38c0cadc8
- Master Rubric (product checklist A,B,C,D,E,F,G,H,I,K) — https://www.notion.so/37058bc375ea81b88b7fe9abc7b1469f
  *(Override per Canonical State §4: the rubric's §K "No Clinical gel" and £TBC/blockers are STALE — range & prices come from §1.)*

## 1. Application copy — updated (Canonical State §7, thick-layer / customer-reported)
All 9 numbing pages now carry the locked wording:
- **Cream + Gel (6):** Start with clean, dry skin → **Apply a thick, visible layer** ("…thick enough to look visibly white on the skin… Customers who get the best results typically report…") → Leave it in place → Remove before your appointment.
- **Spray (3):** step 2 = **Apply a full, even coverage** ("…hold the bottle around 10–15cm from the skin… customers who get the best results typically report a full, even coverage rather than a light mist").
- **Foaming Cleanser:** unchanged cleanser routine (not a numbing application).
- **No timing minutes** anywhere — timing routed to the practitioner. Framed as customer-reported, not a brand directive. ✓ verified on render.

## 2. Buttons — Add to cart + Buy it now side by side
`senseless-product-hero` form: both actions wrapped in `.ss-ph__actions` (flex row, `gap:12px`), each `flex:1 1 0` (equal width), both 50px height (`shopify-payment-button__button` height pinned) — a **2-column row, not stacked**, on all 10 pages. ✓ verified (`.ss-ph__actions` wrapper + equal-width CSS present on every page; both reflect sold-out at inventory 0).

## 3. §11 / Master Rubric audit — filled checklist PER PAGE

**Shared (verified identical on all 10):**
- **GEO/E:** Key Facts block present + extractable, including the locked statement **"UK cosmetic product, by Matrix Health Group Ltd. Not a medicine."**; FAQ answer-first; schema **Product + Offer + BreadcrumbList + Organization + FAQPage** all emitted (Offer availability **OutOfStock**, inventory 0).
- **Compliance/A,B,F,G:** 0 efficacy/timing/%/mechanism/active-ingredient claims; **0 banned customer-facing words** (everyday/upgrade/good-better-best/weak-medium-strong/flagship/concentration/clinical-grade — "flagship" exists only as a CSS class); **"Is this a medicine? No."** FAQ present; **injectable-clean** (no Botox/Lip Fillers/Injections); **trust bar = UK formulated · Cosmetic product · CPSR assessed · Made for aesthetics**; Professional = 2px `#6B3FA0` border + filled purple CTA, **no flagship word/badge**; Layer-1 clinic-softening (practitioner/studio framing).
- **Build:** **live GBP price from the variant, never £TBC**; **de-suffixed slugs** (no -10g/-30g/-15ml/-35ml/-100ml); relative links; reused sections only (no new sections, no duplicates); meta title + meta description + og:description **render** (Horizon multi-line meta tags); canonical tag present.

**Per page (SEO primary keyword · meta title rendered · price · sizes/selector · FAQ items):**

| Product | Primary keyword (H1 + eyebrow + meta) | Meta title (rendered) | Price | Sizes / selector | FAQ |
|---|---|---|---|---|---|
| clinical-strength-cream | Clinical Strength Cream / numbing cream | Clinical Strength Numbing Cream \| Senseless | £44.99 | 10g/30g · selector | 5 |
| advanced-strength-cream | Advanced Strength Cream / numbing cream | Advanced Strength Numbing Cream \| Senseless | £49.99 | 10g/30g · selector | 5 |
| professional-strength-cream | Professional Strength Cream / numbing cream | Professional Strength Numbing Cream \| Senseless | £55.99 | 30g · no selector | 4 |
| clinical-strength-gel | Clinical Strength Gel / numbing gel | Clinical Strength Numbing Gel \| Senseless | £34.99 | 15ml/35ml · selector | 6 |
| advanced-strength-gel | Advanced Strength Gel / numbing gel | Advanced Strength Numbing Gel \| Senseless | £39.99 | 15ml/35ml · selector | 6 |
| professional-strength-gel | Professional Strength Gel / numbing gel | Professional Strength Numbing Gel \| Senseless | £44.99 | 15ml/35ml · selector | 6 |
| clinical-strength-spray | Clinical Strength Spray / numbing spray | Clinical Strength Numbing Spray \| Senseless | £19.99 | 100ml · no selector | 5 |
| advanced-strength-spray | Advanced Strength Spray / numbing spray | Advanced Strength Numbing Spray \| Senseless | £24.99 | 100ml · no selector | 5 |
| professional-strength-spray | Professional Strength Spray / numbing spray | Professional Strength Numbing Spray \| Senseless | £29.99 | 100ml · no selector | 5 |
| foaming-cleanser | Foaming Cleanser / antibacterial cleanser | Senseless Foaming Cleanser — Antibacterial Aftercare | £19.99 | 150ml · no selector | 4 |

**SEO placement (rubric C/D, all pages):** primary keyword (Strength + Format) in **H1 + eyebrow + meta title**; "numbing {format}" captured in **meta title + meta description + og:description** (kept out of the product H1/URL per the strength+format naming rule — `numbing` lives in meta + the collection); secondary/long-tail (e.g. "{strength} strength numbing {format}") in meta. Anchor text into each page = its sibling/format keyword (de-suffixed). **Image alt:** section card slots carry keyword-context alts (e.g. "Advanced Strength Cream on a warm off-white background"); the **hero gallery currently shows the neutral placeholder (no product media), so its `alt` is pending image upload** — flagged.

### Gap found + fixed in this pass
- **"strong" (banned weak/medium/strong)** appeared in the Clinical FAQ ("Is Clinical **strong** enough for my appointment?") on the 3 Clinical pages → reworded to **"Is Clinical the right strength for my appointment?"**. Re-rendered: 0 banned words on all 10.

## Composed vs from-spec (honest flag)
- The per-product **SEO meta, FAQ, Key Facts, and system-band copy were COMPOSED** under the global rules from the Clinical base pattern + Canonical State §1/§7 — **not lifted from each product's own Master Page DB spec**, because the DB product specs/meta are **banned-word stale** ("everyday / concentration / considered upgrade / flagship / clinics / Most Concentrated"). Clinical Cream is the only product with a built v2 spec; the other 9 followed its pattern.
- **Could-not-confirm (flagged, not invented):** **Judge.me** AggregateRating/Review + hero star badge — pending app install on dev (Canonical State §9); reviews section renders nothing until then. **Hero image alt / variant-linked image** — dormant until product media is assigned (neutral placeholder now).

## Internal linking (rubric I) note
- Foaming Cleanser cross-linked as aftercare from every numbing product ✓. Related blocks = same-format siblings (§10) ✓. Canonical handles (/products/foaming-cleanser) ✓. The **≥3 inbound-links-per-page** whole-graph check is a final-pass item (runs once collections/guides exist — Wave 3/4).

## Not done (by design — still Wave 2 checkpoint)
- Wave 3 collections, cookie-consent banner (§6) — not started.
