# Section Library Index

Auto-updated by the `create-section` skill. Don't edit manually unless removing a deprecated section.

"Used on" = count of templates referencing the section type (snapshot 2026-05-29).

| Section File | Purpose | Used On |
|---|---|---|
| `senseless-hero-brand-led.liquid` | Centred brand-statement hero (eyebrow → H1 → lead → 2 CTAs) + product-gallery framing (radial backdrop, single soft shadow, caption, 16:9 desktop / 4:5 mobile) | Homepage (1) |
| `senseless-section-statement.liquid` | The statement unit — composition spine. Eyebrow → headline → one lead (~58ch) → optional single CTA. Centred/left, canvas/surface band, narrow ~720px measure | Homepage (1), rollout |
| `senseless-trio-card-row.liquid` | Reusable trio/quad card row; blocks: tier_card, procedure_card, product_card; 1:1 linked-object images, Professional purple-border variant | 27 templates |
| `senseless-image-text-band.liquid` | Two-column image+text, `direction` text-left/text-right | 27 templates |
| `senseless-collection-hero.liquid` | Collection landing hero (eyebrow, H1, lead, CTA) | 11 collection templates |
| `senseless-product-grid.liquid` | Product/SKU grid for collection pages (1:1 linked images) | 10 collection templates |
| `senseless-trust-bar.liquid` | Trust signals strip (UK formulated · Cosmetic product · CPSR assessed · Made for aesthetics), single row desktop / 2×2 mobile, one per page | 15 templates |
| `senseless-faq-accordion.liquid` | Accessible FAQ accordion (question/answer blocks) | 24 templates |
| `senseless-guide-hero.liquid` | Guide/article hero for system + SEO pages | 15 templates |
| `senseless-callout-band.liquid` | CTA callout band (heading + body + button) | 10 templates |
| `senseless-rich-text.liquid` | Editorial rich-text block, ~60–65ch measure | 8 templates |
| `senseless-procedure-grid.liquid` | Procedure cards grid (1:1 linked collection images) | 4 templates |
| `senseless-how-to-use.liquid` | Numbered application/how-to-use steps | 4 templates |
| `senseless-strength-matrix.liquid` | Suitability / strength-by-procedure matrix | 3 templates |
| `senseless-editorial-band.liquid` | Long-form editorial band | 2 templates |
| `senseless-contact-form.liquid` | Contact / enquiry form | contact, trade (2) |
| `senseless-cross-sell.liquid` | Related-product cross-sell row (1:1 linked images, Professional border) | product, foaming-cleanser (2) |
| `senseless-complete-prep.liquid` | Complementary format cross-sell ("Complete your prep") — 2 sibling-format cards + Compare-formats CTA. Variant by host (auto-detects product format; renders nothing if unresolved). Prep, not aftercare. | product (staged) |
| `senseless-format-row.liquid` | Format comparison row (typographic panels, intentionally imageless) | choosing-your-format, homepage (2) |
| `senseless-product-hero.liquid` | Product page hero (gallery + buy block) | product, foaming-cleanser (2) |
| `senseless-product-showcase.liquid` | Product showcase grid (1:1 linked images, Professional border) | lip-fillers collection, homepage (2) |
| `senseless-decision-band.liquid` | Decision/choice band ("find your strength/format") | Homepage (1) |
| `senseless-newsletter-signup.liquid` | Single-field email signup (Shopify customer form, GDPR double opt-in) | Homepage (1) |
| `senseless-pull-quote.liquid` | Editorial pull quote | Homepage (1) |

## Header / Footer

| Section File | Purpose | Used On |
|---|---|---|
| `senseless-header.liquid` | Fully custom header (replaces Horizon native): large Montserrat wordmark, centred nav driven by the `senseless-main` menu (Shop mega By format/By procedure, The system + Help dropdowns, About + Trade), sticky + frosted, accordion mobile drawer. Reuses Horizon `header-actions` (cart drawer + account) + `search`. | header-group (all pages) |

> Footer still uses Horizon's native `footer.liquid`. Header announcement bar removed (no placeholder text).

## Senseless Snippets

| Snippet File | Purpose |
|---|---|
| `senseless-typography.liquid` | Global `:root` tokens — colour-text ladder + fluid `clamp()` type scale — and global type classes (`.ss-h1/2/3`, `.eyebrow`, `.lead`, `.body-small`, `.caption`, `.t-em`). Rendered in `theme.liquid` head. |
| `senseless-card-image.liquid` | Shared 1:1 card image. Resolves the linked product's featured image / linked collection's image (then collection's first product), with a graceful theme placeholder fallback and an `image_picker` override. Single source of truth for card thumbnails. |
| `senseless-header-footer.liquid` | Brand styling + structural overrides for the configured Horizon header/footer (mega menu, accordion drawer, 4-column footer). |

> Header/footer use Horizon's native `header.liquid` / `footer.liquid` (configured + brand-styled), not bespoke `senseless-` sections. Nav menus are set in Shopify admin: `senseless-main` (header), `senseless-footer-shop` / `-explore` / `-company` (footer).

## Naming Convention

All Senseless sections are prefixed `senseless-`:
- `senseless-home-hero.liquid`
- `senseless-product-system.liquid`
- `senseless-trust-bar.liquid`

## Schema Standards

Every section schema must include:
- `name` — Human-readable name with "Senseless —" prefix in the editor
- `tag` — Default `section` unless override needed
- `class` — Always include `senseless-section` for shared CSS targeting
- Editor-controlled settings for all headlines, body copy, image pickers, CTA labels and URLs
- A non-empty `default` on every text setting (server-side `theme push` rejects `default:""`)

No hard-coded copy in section files. Everything must be editor-accessible.
