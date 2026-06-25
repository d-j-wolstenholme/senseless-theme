<!-- Generated 2026-06-25 · MacBook Pro · 13-agent image-slot audit (62 pages, 309 slots) -->

# Senseless — Site-Wide Image Audit

## 1. Executive summary

The catalogue is healthy and the conversion spine is in good shape: all 16 products carry real `senseless-*` featured images with proper alt text, all 16 collections have real `*-collection-hero.webp` heroes, and every product/collection/strength/format/procedure-collection page resolves its imagery correctly. The image gaps are not in the shop — they cluster almost entirely in two places: (1) the **`senseless-image-text-band` and `senseless-trio-card-row`/`senseless-procedure-grid` sections on `/pages/*` content pages and the umbrella `aesthetic-numbing-cream` page**, which render hard grey SVG placeholder boxes when no image is pinned, and (2) a **single global og:image wiring gap** plus **single-image PDP galleries**. The recurring root cause is one section pattern: `senseless-image-text-band` (L60-64) has no catalogue fallback, so any band with a blank picker shows a grey box; `format_card` and `procedure_card` behave the same way, whereas `tier_card` is empty-safe (degrades to clean text). The fix is overwhelmingly *placement* of already-produced assets, not new shooting — the procedure stills, range stills, cream warm/white variants, application shots and per-format/collection stills mostly already exist.

**Verified figures** (counted from the structured slot map across all 62 page templates — supersede the earlier estimates):

| Metric | Count |
|---|---|
| Page templates audited | 62 |
| Total image slots mapped | 309 |
| Slots filled / healthy (static, product-backed, collection-backed, metafield-backed) | 186 |
| Slots needing attention | 123 |
| — Visible grey-box placeholders (empty-placeholder state) | 87 |
| — `og:image` / social-share entries (37 slots, **one shared code fix** resolves nearly all) | 37 |
| — Unknown / metafield-dependent | 2 |
| Needs-attention by priority → launch-blocker / high / medium / low | 55 / 37 / 26 / 5 |

Note on counting: the og:image gap is a single code fix in `snippets/meta-tags.liquid` that resolves the share-image "need" on every `/pages/*`, blog and homepage at once. Per the completeness critic it is **high**, not a launch-blocker (it is not a visible grey box). The true launch-blockers are the **87 empty-placeholder slots** that render hard grey SVG boxes on live customer pages — concentrated on **About**, the **`aesthetic-numbing-cream` umbrella page**, the **default `product.json` template**, and the **`/pages/*` content + guide pages** (their `image-text-band` / `trio-card-row` bands).

## 2. Launch blockers (fix before public go-live)

These are visible grey SVG placeholder boxes rendering on live customer-facing pages. Every one is confirmed against source (the section hits `placeholder_svg_tag` with no fallback). Most fixes are *pinning an already-produced asset* or *binding a collection so the hero auto-fills* — both are theme-editor/JSON actions, not shoots.

| Page | Location | Why it's a blocker | Recommended image (subject + style + ratio) | Candidate asset / action |
|---|---|---|---|---|
| Foaming Cleanser PDP | Cross-sell card A ("Numbing Cream", no product/image bound) | Card resolves no image and no collection is passed → grey box on a live PDP | Clinical/Advanced/Professional cream tubes grouped, warm off-white, soft top-light, asterisk accent — 1:1 | `processed:senseless-numbing-cream-trio.jpg` as the card image_picker, OR pass `collection: 'numbing-cream'` so it falls to the collection hero |
| Aesthetic Numbing Cream (umbrella) | Procedure grid cards ×4 (Microneedling/Laser/SPMU/Waxing) | Confirmed: blocks have no image AND no collection bound; `procedure-grid` passes blank → grey box ×4 on a live umbrella page | Per-procedure editorial stills, warm off-white, product-led, no needles/clinical drama — 1:1 | `processed:senseless-procedure-microneedling.jpg / -laser-hair-removal.jpg / -semi-permanent-makeup.jpg / -waxing.jpg` — OR (cheapest) bind each card's `collection` to its live procedure collection |
| Aesthetic Numbing Cream (umbrella) | Formats row cards ×3 (Cream/Gel/Spray) | `format_card` is not empty-safe; always renders media div → grey box ×3 | One still per format, warm off-white, consistent framing — 1:1 | `processed:senseless-numbing-cream-collection.jpg / -gel-collection.jpg / -spray-collection.jpg` — OR bind each card's `collection` |
| Aesthetic Numbing Cream (umbrella) | "Why" band + "Aftercare" band (`image-text-band`) | Blank picker, no fallback → grey box ×2 | Why: single cream tube close-up + lid, warm off-white. Aftercare: 150ml Foaming Cleanser on clean countertop — 1:1 | Why: `processed:senseless-advanced-strength-cream-white.jpg`; Aftercare: `processed:senseless-foaming-cleanser.jpg` |
| About Senseless | Hero (`hero-brand-led`) + "company" + "believe" + "practice" bands | 4–5 visible grey boxes on the brand's About page (hero placeholder + three `image-text-band` placeholders) | Hero: three-tier lineup grouped, warm off-white, asterisk in negative space. Bands: single-tube macro (company), three-tier peers (believe), Professional-tier still (practice) — 1:1 | Hero: `processed:senseless-range-upright.jpg`; company: `senseless-clinical-strength-cream-white.jpg`; believe: `senseless-range-angled.jpg`; practice: `senseless-professional-strength-collection.jpg` |
| About Senseless | "notice" row ×3 + "next" row ×4 (`trio-card-row` format_cards) | 7 grey boxes from the non-empty-safe format_card path | Matched asterisk-led brand graphics (notice) and wayfinding stills (next) — 1:1 | Wire each "next" card's `collection` to auto-fill heroes where a target exists; supply asterisk/brand graphics for concept cards (new render) |
| Default product template (`product.json`) | "system" + "aftercare" `image-text-band` | Grey box for any product landing on the fallback template; no catalogue fallback in the band | System: ascending three-tier cream lineup. Aftercare: Foaming Cleanser on countertop — 1:1 | System: `processed:senseless-range-upright.jpg`; Aftercare: `processed:senseless-foaming-cleanser.jpg` |
| Aesthetic Procedures (`/pages/aesthetic-procedures`) | Procedures row ×4 + Formats row ×3 (`trio-card-row` format_cards) | 7 grey boxes on a customer-facing shop landing | Per-procedure and per-format stills, warm off-white — 1:1 | Procedure + format collection stills already exist (`senseless-procedure-*`, `senseless-numbing-*-collection`), OR bind each card's `collection` |
| Choosing Your Format (`/pages/choosing-your-format`) | Cream/Gel/Spray/Complementary bands ×4 + Shop quad ×4 | 8 grey boxes (texture/format bands + shop cards) | Cream texture macro, gel ribbon macro, 100ml spray three-quarter, three-format grouped; shop cards bind to collections — 1:1 | `senseless-clinical-strength-cream-warm.jpg`, `senseless-advanced-strength-gel.jpg`, `senseless-advanced-strength-spray.jpg`, `senseless-cream-spray-gel-trio-angled.jpg`; bind shop cards' `collection` |
| Choosing Your Strength (`/pages/choosing-your-strength`) | "Misunderstandings" band + "Format" band | 2 grey boxes | Three tubes equal visual weight (no tier hero-ed); three-format trio — 1:1 | `senseless-numbing-cream-trio.jpg`; `senseless-cream-spray-gel-trio.jpg` |
| Trade & Wholesale (`/pages/trade`) | "Fit" band + "Position" band | 2 grey boxes | Precise product still signalling professionalism (NOT a clinic interior); Professional cream tube close-up — 1:1 | `senseless-range-upright.jpg`; `senseless-professional-strength-cream.jpg`. Update the "clinic-context" alt to a product-led description |
| Contact (`/pages/contact`) | "Company" band | Grey box on contact page | Brand-mark composition — purple six-point asterisk as quiet editorial graphic on warm off-white — 1:1 | New asterisk/brand-mark render, or `processed:senseless-editorial-head.jpg` |
| Does numbing cream work? | "category" + "varies" + "experience" + "failure" bands + "next" cards ×4 | ~8 grey boxes on a commercial-intent guide | Cosmetic still; three-tier line-up; application detail; tighter tier close-up; matched wayfinding cards — 1:1 | `senseless-clinical-strength-cream-white.jpg`, `senseless-range-upright.jpg`, `senseless-home-how-to-use-arm.jpg`, `senseless-advanced-strength-collection.jpg`; wire "next" cards |
| How long numbing cream lasts | "framework" + "cantell" + "runsout" bands + "next" cards ×4 | ~7 grey boxes | Three-tier upright; angled trio; single-tube macro; matched guide thumbnails — 1:1 | `senseless-range-upright.jpg`, `senseless-cream-spray-gel-trio-angled.jpg`, `senseless-editorial-head.jpg`, `senseless-home-how-to-use-arm.jpg` |
| How long numbing cream takes to work | "framework" + "cantell" + "system" bands + "next" cards ×4 | ~7 grey boxes | Three-tier; single-tube macro; format trio; matched cards — 1:1 | `senseless-range-upright.jpg`, `senseless-editorial-head.jpg`, `senseless-cream-spray-gel-trio.jpg`, `senseless-home-how-to-use-arm.jpg` |
| Strongest numbing cream | "meaning" + "dontneed" + "trade" bands + "tiers" cards ×4 | ~7 grey boxes | Professional tube close-up; three-tier; Professional-on-neutral-surface (NOT clinical); matched tier cards — 1:1 | `senseless-professional-strength-cream.jpg`, `senseless-range-upright.jpg`, `senseless-professional-strength-collection.jpg`, `senseless-clinical-strength-collection.jpg` |
| Best numbing cream | "framework" cards ×3 + "next" cards ×4 | 7 grey boxes (the framework cards are prominent mid-page content cards) | Treatment/area/you trio; system/selector/shop/strongest wayfinding — 1:1 | `senseless-cream-spray-gel-trio.jpg`, `senseless-numbing-cream-collection.jpg`; wire shop card to `numbing-cream` |
| Best EMLA alternative UK | "framing" + "reasons" bands + "recommend" procedure grid ×4 + "next" cards ×4 | ~10 grey boxes — comparison page, must stay Senseless-only (no competitor imagery) | Senseless close-up; range; four procedure stills; Senseless-only wayfinding — 1:1 | `senseless-editorial-head.jpg`, `senseless-range-angled.jpg`, `senseless-procedure-*` (or bind `collection`), `senseless-range-upright.jpg` |
| Senseless vs Ametop | "framing" + "fit" bands + "recommend" procedure grid ×4 + "next" cards ×4 | ~10 grey boxes — comparison page, Senseless-only | Senseless close-up; range; four procedure stills; Senseless-only wayfinding — 1:1 | `senseless-editorial-head.jpg`, `senseless-range-angled.jpg`, `senseless-procedure-*` (or bind `collection`), `senseless-range-upright.jpg` |
| Using numbing cream | "next" cards (if present as format_cards) | Grey boxes where `trio-card-row` format_cards are unbound | Matched warm off-white guide thumbnails — 1:1 | `senseless-home-how-to-use.jpg` + wire cards |
| Articles hub (`/pages/articles`) | Guide cards g1/g2/g3 (`articles-hub` guide_link) | 3 grey boxes on a hub linked from The System nav | Three reassuring topic thumbnails (does-it-hurt / microneedling / laser), no needles/clinical drama — 1:1 | `inbox:does-it-hurt.png` (process), `senseless-procedure-microneedling.jpg`, `senseless-procedure-laser-hair-removal.jpg` |

Latent / verify-before-launch (treat as launch-gated once confirmed live):
- **Guides hub (`/blogs/guides`)** and **Articles hub article loop** render grey `placeholder_svg_tag` per article that lacks a featured image. Cannot be confirmed from the repo (blog content is admin-set; MEMORY notes blog was Horizon-default). **Action: live-render check before go-live; set a square featured image on every guide article.** If any card is grey at launch, this is a blocker.

## 3. Needs-an-image, by page

Grouped by cluster. Filled/healthy slots are omitted (counted in the Appendix only).

### Global / meta

- **og:image / twitter:image default (`snippets/meta-tags.liquid` L70-91)** — current: the entire og:image block is wrapped in `{% if page_image %}` with no shop-level fallback, so the homepage and every featured-image-less `/pages/*` emit no share image. Recommendation: add a fallback below the `page_image` branch that renders an uploaded brand share card (new shop-level setting or referenced file) — a 1.91:1 (1200×630) editorial range still-life on warm off-white with the purple asterisk and wordmark, crop-safe centred. This single fix resolves the share-image need across home, all guides and blog indexes. Candidate: `manifest-held:senseless-home-bundle-social-band` (re-crop to 1200×630), or `processed:senseless-range-angled.jpg`. **High** (invisible code gap, password-gated pre-launch — fix before *public* launch).
- **Organization JSON-LD logo (`senseless-org-schema.liquid`)** — current: no `logo`/`image` property emitted. Recommendation: add `Organization.logo` pointing at an uploaded square brand PNG (≥112px) for entity authority; reuse the same asset as the og:image fallback. Candidate: render a square logo PNG from `assets/senseless-logo.png`. **Medium** (GEO/entity, not a visible slot).
- **Password page logo + gift-card brand image** — current: no shop-level `settings.logo`, so the password splash shows a plain shop-name text wordmark and issued gift cards show Shopify's generic `card.svg`. Recommendation: upload one brand wordmark PNG as `settings.logo` — fixes both in one step (the password page is the only public-facing page pre-launch). **Low.**
- **Password page background** — current: `background_media: none`. Optional full-bleed warm off-white range still-life behind the holding page. Candidate: `processed:senseless-range-angled.jpg`. **Low.**

### Homepage

- **og:image** — same single global fix as above (homepage is the most-shared URL). **High.** Otherwise the homepage is fully filled (hero, both image-text bands, all three product-highlight cards and all four procedure cards resolve real images — the home procedure grid IS correctly collection-backed, unlike the umbrella page).

### PDPs

- **All PDP galleries (custom strength×format, bundle, cleanser, default)** — current: every product has `mediaCount=1`, so the hero thumbnail strip never renders. Recommendation: attach gallery angles #2/#3. For creams, the **`*-warm` and `*-white` variant stills are already produced and sitting in assets, just not attached as media** — attach them, then add a texture/lid-off macro (no skin contact). 1:1 square to match the featured image. Candidates: `senseless-clinical-strength-cream-warm.jpg`, `senseless-clinical-strength-cream-white.jpg` (and equivalents); cleanser foam macro and bundle contents flat-lay = new shoot. **High** (single biggest PDP gap).
- **Foaming Cleanser cross-sell card A** — launch-blocker, see §2.
- **Default `product.json` "system"/"aftercare" bands** — launch-blockers, see §2.

### Collections

- **shop-all collection image** — current: reuses `senseless-homepage-hero.webp` with **NULL altText**, and the `shop-all` template hero borrows the homepage hero rather than a true full-range shot. Recommendation: pin an explicit full-range hero (cream+gel+spray+cleanser) on the template and set an alt on the collection image. Candidate: `processed:senseless-range-upright.jpg`. **Medium.**
- **All other collections (strength, format, procedure, bundles)** — heroes and grids are fully filled and on-brand; no work. The bundles hero is a verification chore only (see §4).

### Pillar pages

- **The Senseless System, Aesthetic Procedures, Does it hurt? (hub)** — heroes are filled. Aesthetic Procedures' procedure/format card rows are launch-blockers (see §2).
- **How it works** — guide-hero is empty (degrades to text-only, not a grey box) → **Medium** enrichment: pin a multi-SKU system still (`senseless-range-angled.jpg`). Its five `image-text-band` slots (category/system/application/expect) are grey boxes → **High/launch-blocker** (single-tube macro, full system matrix, application arm shot, reassuring range still).

### Guide pages

- **Guide heroes that degrade gracefully (text-only, no grey box):** How it works, How to apply numbing cream, How long lasts, How long takes to work, Strongest, Best numbing cream, Best EMLA alternative, Senseless vs Ametop, Using numbing cream, plus Reviews/Trade/Contact/FAQ. These are **held/intentional text-led**, not blockers — **Medium/Low** enrichment only (pin a topic-matched still per page; candidates listed per page in the JSON, e.g. gel still for microneedling, spray still for laser, cream macro for "does it work").
- **Guide `image-text-band` and `trio-card-row` slots** across the does-it-hurt family and the commercial guides — these ARE grey boxes (launch-blockers, see §2).
- **How to apply** — "mistakes" band grey box → **High**: thin-layer application detail (`senseless-home-how-to-use-arm.jpg`).

### Blog

- **Guides hub (`/blogs/guides`) per-article cards** — reachable grey placeholder path; depends on whether each guide article has a featured image. **High** — set a square featured image on every guide article; live-render check before launch.
- **Default blog/article (`/blogs/news`)** — graceful text-only fallback (no grey box); the legacy/unused blog. **Low** — per-article admin images only.
- **Guide article template (`article.guides.json`)** — text-first by design, no on-page hero slot. og:image is driven by the (admin-set) article featured image → **Medium**: set featured images so guide shares get a preview.

## 4. Cross-cutting recommendations

- **PDP galleries are single-image site-wide.** Every product has `mediaCount=1`. Attach the **already-produced cream `warm` and `white` variant shots** as media #2/#3 (they exist in assets, unattached), then commission a small set of standard angles per format: a lid-off / texture macro for creams and gels, a foam-lather macro for the cleanser, and a contents flat-lay (cream+gel+spray+cleanser+vanity bag) for each bundle to support the "What's in the bundle" copy. All 1:1 square to match the featured image so the thumbnail swap is seamless.
- **Fix the one og:image wiring gap once.** A single fallback in `snippets/meta-tags.liquid` (render an uploaded brand share card when `page_image` is blank) resolves the missing share image on the homepage, every `/pages/*` guide/pillar and both blog indexes simultaneously. Pair it with one uploaded 1200×630 asset (`senseless-home-bundle-social-band` re-cropped). Reuse the same PNG for the Organization.logo schema property and the password/gift-card `settings.logo`.
- **Two cheap structural fixes kill most launch-blockers.** (1) For `procedure_card`/`format_card` rows whose cards point at a real collection via `cta_url`, set the block's **`collection` setting** (not just the URL) — `senseless-card-image` then auto-fills from the live `*-collection-hero.webp`. (2) For `image-text-band` slots, pin the matching produced asset. The vast majority of the 41 blockers are placement, not shoots.
- **shop-all null alt.** Set an alt on the `shop-all` collection image (currently NULL) and pin a true full-range hero on the template rather than borrowing the homepage hero.
- **Held/produced-but-unplaced assets that just need placing:** the four `senseless-procedure-*` stills, `senseless-numbing-cream/gel/spray-collection` stills, `senseless-range-upright`/`-angled`, `senseless-cream-spray-gel-trio`(`-angled`), `senseless-home-how-to-use`(`-arm`), `senseless-*-cream-warm`/`-white`, and `manifest-held:senseless-home-bundle-social-band`. Almost all §2/§3 needs draw on these.
- **Verify the bundle hero cleanser label.** Live ground truth says all 16 products carry real featured images, so `senseless-professional-bundle-hero.webp` (and the per-bundle heroes) are filled. But a manifest HELD note flagged earlier `.jpg` bundle renders for showing an **incorrect cleanser strength label**. Confirm the live `*-bundle-hero.webp` images show no wrong strength label. This is a **Low verification chore**, not a missing-image priority.

## 5. Photographer's brief (the consistent visual language)

Shoot everything so a new asset drops into any slot without looking foreign.

- **Background:** warm off-white seamless (`#f7f7f5`), surface white (`#ffffff`) where a brighter ground is needed. Never a coloured or purple fill ground.
- **Lighting:** soft, directional top-light; a single soft shadow; gentle falloff. Premium and restrained — Augustinus Bader, Dieux, Wildsmith Skin, 111SKIN, The Inkey List as benchmarks.
- **Subjects:** product still-life is the default. Real packaging — Cream (10g/30g tubes), Gel (15ml/35ml), Spray (100ml), Foaming Cleanser (150ml). Group as three-tier lineups (Clinical/Advanced/Professional) or three-format trios (cream/gel/spray). Texture macros (a swipe of cream, a translucent gel ribbon) and lid-off details are welcome — on clean surfaces, never on faces.
- **People:** natural, unmedicated, female-leaning, no faces in current slots; application cues are fingertip/forearm only.
- **Props:** minimal — a neutral linen, a soft botanical sprig for warmth, the brand surface. No clinical/medical equipment, no clinic interiors, no laser/needle devices.
- **Palette:** brand purple `#6B3FA0` is an **accent only** — the six-point asterisk, the Professional 2px border cue on packaging, a thin accent line. Never a large fill.
- **The asterisk:** use the purple six-point asterisk as a quiet hero accent, divider, or brand-mark in negative space (and as the basis for the concept/brand-graphic cards on About). It is the natural subject for "company/legal" and brand-mark slots over a product shot.
- **Ratio rules:** **1:1 square is the default site-wide** (wrappers enforce `aspect-ratio:1/1` + `object-fit:cover`) — shoot square-croppable. The only deliberate non-square overrides: **social/og cards at 1.91:1 (1200×630)**, the default-blog article hero at 16:9, and a couple of intentional 3:2 `image-text-band` overrides. When in doubt, deliver square.
- **Compliance do's and don'ts (non-negotiable, UK):** NO medical/clinical settings on consumer pages; NO needles-in-skin or procedure-in-progress; NO before/after; NO efficacy/duration claims implied by props (no stopwatches-as-claim). "Numbing" is a category term, never a claim. On comparison pages (EMLA / Ametop) show **Senseless only** — never a competitor's packaging.

## 6. Appendix — full slot map

| Page | Location | State | Needs? | Priority |
|---|---|---|---|---|
| Global header | Brand logo (SVG wordmark) | filled-static | No | none |
| Global header | Mega-menu Featured card | product-backed | No | low |
| Global footer | Brand logo (SVG) | filled-static | No | none |
| Meta | og:image default (home + /pages/*) | meta-og | Yes | high |
| Meta | og:image (product/collection/article) | meta-og | No | none |
| Meta | Favicon | filled-static | No | none |
| Org schema | Organization.logo property | unknown | Yes | medium |
| 404 | (no image slots) | filled-static | No | none |
| Search | Result card images | product-backed | No | none |
| List-collections | Collection card images | collection-backed | No | low |
| Cart | Line-item thumbs / recs | product-backed | No | none |
| Password | Logo block | empty-placeholder | Yes | low |
| Password | Background media | empty-placeholder | Yes | low |
| Gift card | Brand image (settings.logo) | empty-placeholder | Yes | low |
| Gift card | Favicon | filled-static | No | none |
| Homepage | Hero | filled-static | No | none |
| Homepage | Strength ladder / callout / format row / trust bar / newsletter / practitioner cards | no slot | No | none |
| Homepage | Image-text bands ×2 | filled-static | No | none |
| Homepage | Product-highlight cards ×3 | product-backed | No | none |
| Homepage | Procedure grid cards ×4 | collection-backed | No | none |
| Homepage | og:image | meta-og | Yes | high |
| PDP (custom ×9) | Hero gallery (single-image) | product-backed | Yes | high |
| PDP (custom) | Cross-sell cards | product-backed | No | none |
| PDP (custom) | og:image | product-backed | No | none |
| PDP (custom) | text/diagram sections | no slot | No | none |
| Cleanser PDP | Hero gallery | product-backed | Yes | high |
| Cleanser PDP | Cross-sell card A (unbound) | empty-placeholder | Yes | launch-blocker |
| Cleanser PDP | Cross-sell cards B/C | product-backed | No | none |
| Bundle PDP | Hero gallery | product-backed | Yes | high |
| Bundle PDP | Bundle contents (text) | filled-static | No | low |
| Default PDP | Hero gallery | product-backed | Yes | high |
| Default PDP | "system" band | empty-placeholder | Yes | launch-blocker |
| Default PDP | "aftercare" band | empty-placeholder | Yes | launch-blocker |
| Default PDP | Complete-prep cards | collection-backed | No | low |
| Default PDP | Cross-sell / matrix / how-to / key-facts | product-backed / no slot | No | none |
| Generic collection | Product cards | product-backed | No | none |
| Generic collection | Heading band | no slot | No | none |
| Clinical/Advanced/Professional collection | Hero | filled-static | No | none |
| Clinical/Advanced/Professional collection | Grid cards | product-backed | No | none |
| Clinical/Advanced/Professional collection | Scale / bands | no slot | No | none |
| Clinical/Advanced/Professional collection | og:image | meta-og (collection.image) | No | none |
| Numbing Cream/Gel/Spray collection | Hero + grid | filled / product-backed | No | none |
| Procedure collections (botox/injections/laser/lip/micro/spmu/wax) | Hero + grid + og:image | filled / product-backed / collection-backed | No | none |
| Aesthetic Numbing Cream (umbrella) | Hero | collection-backed | No | low |
| Aesthetic Numbing Cream | Procedure grid ×4 | empty-placeholder | Yes | launch-blocker |
| Aesthetic Numbing Cream | Formats row ×3 | empty-placeholder | Yes | launch-blocker |
| Aesthetic Numbing Cream | Why band | empty-placeholder | Yes | launch-blocker |
| Aesthetic Numbing Cream | Aftercare band | empty-placeholder | Yes | launch-blocker |
| Aesthetic Numbing Cream | Tiers row ×3 | empty-safe (text) | No | medium |
| Aesthetic Numbing Cream | Featured trio ×3 | product-backed | No | none |
| Shop All | Hero | collection-backed (borrows home hero, NULL alt) | Yes | medium |
| Shop All | Cream/Gel/Spray/Aftercare grids | product-backed | No | none |
| Bundles | Hero | filled-static (verify cleanser label) | No | low |
| Bundles | Scale / grid | no slot / product-backed | No | none |
| About | Hero | empty-placeholder | Yes | launch-blocker |
| About | "what" band | filled-static | No | none |
| About | "company" / "believe" / "practice" bands | empty-placeholder | Yes | launch-blocker |
| About | "notice" row ×3 | empty-placeholder | Yes | launch-blocker |
| About | "next" row ×4 | empty-placeholder | Yes | launch-blocker |
| About | credentials/key-facts/FAQ/schema | no slot | No | none |
| About | og:image | meta-og | Yes | high (global fix) |
| The Senseless System | Hero | filled-static | No | none |
| The Senseless System | body sections | no slot | No | none |
| The Senseless System | og:image | meta-og | Yes | high (global fix) |
| How it works | Hero | empty-safe (text) | Yes | medium |
| How it works | category/system/application/expect bands | empty-placeholder | Yes | launch-blocker |
| How it works | "next" cards ×4 | empty-placeholder | Yes | launch-blocker |
| How it works | callout/key-facts/faq | no slot | No | none |
| Aesthetic Procedures | Hero | filled-static | No | none |
| Aesthetic Procedures | Procedures row ×4 | empty-placeholder | Yes | launch-blocker |
| Aesthetic Procedures | Formats row ×3 | empty-placeholder | Yes | launch-blocker |
| How to apply | Hero | empty-safe (text) | Yes | medium |
| How to apply | how-to-use steps / rich-text / callout / faq | no slot | No | none |
| How to apply | "mistakes" band | empty-placeholder | Yes | high |
| How to apply | "next" cards ×4 | empty-placeholder | Yes | high |
| Choosing Your Format | Hero | empty-safe (text) | Yes | high |
| Choosing Your Format | Cream/Gel/Spray/Complementary bands ×4 | empty-placeholder | Yes | launch-blocker |
| Choosing Your Format | Shop quad ×4 | empty-placeholder | Yes | launch-blocker |
| Choosing Your Format | format row / matrix / callout / key-facts / faq | no slot | No | none |
| Choosing Your Strength | Hero | empty-safe (text) | Yes | high |
| Choosing Your Strength | Misunderstandings band | empty-placeholder | Yes | launch-blocker |
| Choosing Your Strength | Format band | empty-placeholder | Yes | launch-blocker |
| Choosing Your Strength | Tiers trio | empty-safe (text) | No | low |
| Choosing Your Strength | Shop trio ×3 | product-backed | No | none |
| Choosing Your Strength | matrix/editorial/callout/key-facts/faq | no slot | No | none |
| Articles hub | Guide cards g1/g2/g3 | empty-placeholder | Yes | launch-blocker |
| Articles hub | Article loop cards | unknown (per-article admin) | Yes | high |
| Reviews | Hero | empty-safe (text) | No | low |
| Reviews | Judge.me block / schema | app / no slot | No | none |
| Trade | Hero | empty-safe (text) | No | low |
| Trade | "offer" trio ×3 | empty-placeholder | Yes | high |
| Trade | Fit band / Position band | empty-placeholder | Yes | high |
| Trade | "next" trio ×3 | empty-placeholder | Yes | high |
| Trade | credentials/process/faq/form/schema | no slot | No | none |
| Contact | Hero | empty-safe (text) | No | low |
| Contact | Company band | empty-placeholder | Yes | launch-blocker |
| Contact | "next" trio ×3 | empty-placeholder | Yes | high |
| Contact | contact-cards / form / callout / key-facts / faq / schema | no slot | No | none |
| FAQ | Hero | empty-safe (text) | No | low |
| FAQ | intro / accordion / essentials / route / schema | no slot | No | none |
| Policy (legal) | content + og:image | filled-static / meta-og | No | none/low |
| Default page template | body + og:image | filled-static / meta-og | (No) / Yes | none / low |
| Does it hurt? (hub) | Hero | filled-static | No | none |
| Does it hurt? (hub) | og:image | meta-og | Yes | high (global fix) |
| Does it hurt? by treatment | Hero | empty-safe (text) | Yes | high |
| Does microneedling hurt? | Hero | empty-safe (text) | Yes | high |
| Does laser hair removal hurt? | Hero | empty-safe (text) | Yes | high |
| Does numbing cream work? | Hero | empty-safe (text) | Yes | high |
| Does numbing cream work? | category/varies/experience/failure bands | empty-placeholder | Yes | launch-blocker |
| Does numbing cream work? | "next" cards ×4 | empty-placeholder | Yes | launch-blocker |
| How long lasts | Hero | empty-safe (text) | Yes | medium |
| How long lasts | framework/cantell/runsout bands | empty-placeholder | Yes | launch-blocker |
| How long lasts | "next" cards ×4 | empty-placeholder | Yes | launch-blocker |
| How long lasts | rich-text/callout/faq/key-facts | no slot | No | none |
| How long takes to work | Hero | empty-safe (text) | Yes | medium |
| How long takes to work | framework/cantell/system bands | empty-placeholder | Yes | launch-blocker |
| How long takes to work | "next" cards ×4 | empty-placeholder | Yes | launch-blocker |
| Strongest numbing cream | Hero | empty-safe (text) | Yes | medium |
| Strongest numbing cream | meaning/dontneed/trade bands | empty-placeholder | Yes | launch-blocker |
| Strongest numbing cream | "tiers" cards ×4 | empty-placeholder | Yes | launch-blocker |
| Strongest numbing cream | "range" product grid ×3 | product-backed | No | low |
| Best numbing cream | Hero | empty-safe (text) | Yes | medium |
| Best numbing cream | "framework" cards ×3 | empty-placeholder | Yes | launch-blocker |
| Best numbing cream | "next" cards ×4 | empty-placeholder | Yes | launch-blocker |
| Best numbing cream | editorial/rich-text/key-facts/faq/schema | no slot | No | none |
| Best EMLA alternative UK | Hero | empty-safe (text) | Yes | medium |
| Best EMLA alternative UK | framing/reasons bands | empty-placeholder | Yes | launch-blocker |
| Best EMLA alternative UK | recommend procedure grid ×4 | empty-placeholder | Yes | launch-blocker |
| Best EMLA alternative UK | "next" cards ×4 | empty-placeholder | Yes | launch-blocker |
| Best EMLA alternative UK | tiers (tier_card) ×3 | empty-safe (text) | No | low |
| Senseless vs Ametop | Hero | empty-safe (text) | Yes | medium |
| Senseless vs Ametop | framing/fit bands | empty-placeholder | Yes | launch-blocker |
| Senseless vs Ametop | recommend procedure grid ×4 | empty-placeholder | Yes | launch-blocker |
| Senseless vs Ametop | "next" cards ×4 | empty-placeholder | Yes | launch-blocker |
| Senseless vs Ametop | tiers (tier_card) ×3 | empty-safe (text) | No | low |
| Using numbing cream | Hero | empty-safe (text) | Yes | medium |
| Using numbing cream | how-to-use / editorial / rich-text / link-row / faq / schema | no slot | No | none |
| Using numbing cream | og:image | meta-og | Yes | high (global fix) |
| All guide pages | og:image | meta-og | Yes | high (one global fix) |
| Blog index (default) | Article cards | metafield-backed (graceful) | No | low |
| Blog index (default) | og:image | meta-og | Yes | low |
| Guides hub (/blogs/guides) | Article card thumbs | empty-placeholder (reachable) | Yes | high |
| Guides hub | og:image | meta-og | Yes | medium |
| Blog article (default) | Featured image / og:image | metafield-backed | No | low |
| Guide article (article.guides) | body (no hero slot) | filled-static | No | low |
| Guide article | og:image (admin featured image) | meta-og | Yes | medium |
