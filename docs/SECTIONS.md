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
| `senseless-product-grid.liquid` | Product/SKU grid for collection pages (1:1 linked images). Cards take an optional linked `product` → inline quick-add (variant + qty + add-to-cart) via `senseless-quick-add`; unlinked = editorial link-only card | 10 collection templates |
| `senseless-trust-bar.liquid` | Trust signals strip (UK formulated · Cosmetic product · CPSR assessed · Made for aesthetics), single row desktop / 2×2 mobile, one per page | 15 templates |
| `senseless-faq-accordion.liquid` | Accessible FAQ accordion (question/answer blocks) | 24 templates |
| `senseless-guide-hero.liquid` | Guide/article hero for system + SEO pages | 15 templates |
| `senseless-callout-band.liquid` | CTA callout band (heading + body + button) | 10 templates |
| `senseless-rich-text.liquid` | Editorial rich-text block, ~60–65ch measure | 8 templates |
| `senseless-procedure-grid.liquid` | Procedure cards grid (1:1 linked collection images) | 4 templates |
| `senseless-how-to-use.liquid` | Numbered application/how-to-use steps | 4 templates |
| `senseless-strength-matrix.liquid` | Suitability / strength-by-procedure matrix | 3 templates |
| `senseless-key-facts.liquid` | Machine-extractable "Key facts" GEO block — semantic `<dl>` of label/value facts + a fixed, non-editable compliance line ("UK cosmetic product, by Matrix Health Group Ltd. Not a medicine."). Per-page facts seeded from each page's Notion v2 Key Facts. | product, 3 format collections, 6 guides, 4 landings (14) |
| `senseless-editorial-band.liquid` | Long-form editorial band | 2 templates |
| `senseless-contact-form.liquid` | Contact / enquiry form | contact, trade (2) |
| `senseless-cross-sell.liquid` | Related-product cross-sell row (1:1 linked images, Professional border) | product, foaming-cleanser (2) |
| `senseless-complete-prep.liquid` | Complementary format cross-sell ("Complete your prep") — 2 sibling-format cards + Compare-formats CTA. Variant by host (auto-detects product format; renders nothing if unresolved). Prep, not aftercare. | product (staged) |
| `senseless-format-row.liquid` | Format comparison row (typographic panels, intentionally imageless) | choosing-your-format, homepage (2) |
| `senseless-product-hero.liquid` | Product page hero (gallery + buy block). Live variant price (own line, not in chips); **size chips only when >1 variant** (single-size products show no selector); **variant-linked gallery image** (swaps to the variant's `featured_image`, capped `max-width:420px`); **Add to cart + Buy it now** (`form \| payment_button`), sold-out/unavailable at inventory 0; trust line; primary CTA filled brand-purple (no neutral border); Professional (tag/metafield) gets 2px purple info-panel border. | all 10 product templates |
| `senseless-reviews.liquid` | **NEW (Wave 2).** Reviews section that hosts the Judge.me widget as a theme **app block** (`@app`); renders nothing until a block is added (hidden until reviews exist). Judge.me hides until 5+ reviews and emits AggregateRating only when reviews exist. | clinical-strength-cream (1) |
| `senseless-product-showcase.liquid` | Product showcase grid (1:1 linked images, Professional border) | lip-fillers collection, homepage (2) |
| `senseless-decision-band.liquid` | Decision/choice band ("find your strength/format") | Homepage (1) |
| `senseless-newsletter-signup.liquid` | Single-field email signup (Shopify customer form, GDPR double opt-in) | Homepage (1) |
| `senseless-pull-quote.liquid` | Editorial pull quote | Homepage (1) |

## Header / Footer

| Section File | Purpose | Used On |
|---|---|---|
| `senseless-header.liquid` | Fully custom header (replaces Horizon native): large Montserrat wordmark, centred nav driven by the `senseless-main` menu (Shop mega By format/By procedure, The system + Help dropdowns, About + Trade), sticky + frosted, accordion mobile drawer. Reuses Horizon `header-actions` (cart drawer + account) + `search`. **Logo:** inlined from `assets/senseless-logo-header.svg` via `inline_asset_content` — does **not** flow through the shared `snippets/image.liquid` (Shopify's `image_url` returns blank for SVGs, so an SVG in the picker won't render); the `logo_image` picker is now a raster-only (PNG/JPG) override. The wordmark is outlined to vector paths (Helvetica-Light) so it renders identically to the printed packaging on devices without Helvetica. | header-group (all pages) |
| `senseless-footer.liquid` | Fully bespoke footer (replaces Horizon native `footer` + `footer-utilities`). Dense, large inlined wordmark, four columns — **Shop / The system / Brand / Newsletter** — over a legal band (© + Matrix Health Group Ltd parent attribution → matrixhealthgroup.co.uk + `shop.policies` links + social). Columns 1–3 are menu-driven (`senseless-footer-shop` / `-explore` / `-company`); where a menu or policy is not yet set in admin, an **injectable-clean** placeholder set renders and is flagged in-code for Stage D wiring. Newsletter column uses the native `{% form 'customer' %}`. Band setting: ink (default) / canvas / surface. | footer-group (all pages) |

> Footer is the bespoke `senseless-footer.liquid` section (replaces Horizon native `footer.liquid`). Header announcement bar removed (no placeholder text).

## Senseless Snippets

| Snippet File | Purpose |
|---|---|
| `senseless-typography.liquid` | Global `:root` tokens — colour-text ladder + fluid `clamp()` type scale — and global type classes (`.ss-h1/2/3`, `.eyebrow`, `.lead`, `.body-small`, `.caption`, `.t-em`). Rendered in `theme.liquid` head. |
| `senseless-card-image.liquid` | Shared 1:1 card image. Resolves the linked product's featured image / linked collection's image (then collection's first product), with a graceful theme placeholder fallback and an `image_picker` override. Single source of truth for card thumbnails. |
| `senseless-quick-add.liquid` | Shared inline quick-add control for product cards. Renders an inline variant `<select>` (when >1 variant), Horizon quantity stepper + add-to-cart inside a Horizon `<product-form-component>` (AJAX `/cart/add` → opens cart drawer). Renders nothing unless a real product is passed (nav/editorial cards stay plain links); stays inert/disabled until the product has price + stock. Reuses Horizon `product-form-component` / `add-to-cart-button` / `quantity-selector`. Used by `senseless-product-grid`, `-trio-card-row` (product_card), `-cross-sell`, `-product-showcase`. |
| `senseless-header-footer.liquid` | Brand styling + structural overrides for the configured Horizon header (mega menu, accordion drawer). Footer styling now lives in the bespoke `senseless-footer.liquid` section. |
| `senseless-structured-data.liquid` | JSON-LD dispatcher rendered in `theme.liquid` head. Emits Product+Offer (PDPs) and CollectionPage+ItemList (collections) via the `json` filter (live price/availability/currency; seller legalName "Matrix Health Group Ltd"; claim-free). Dispatches on `request.page_type`; does **not** duplicate Organization/FAQPage/Article schema emitted elsewhere. |
| `senseless-breadcrumbs-jsonld.liquid` | BreadcrumbList JSON-LD for product / collection / page, reflecting the real hierarchy (Home → [collection] → Product, etc.). Rendered by `senseless-structured-data`. |

> Header and footer are both bespoke `senseless-` sections (`senseless-header`, `senseless-footer`) — neither uses Horizon's native `header.liquid` / `footer.liquid`. Nav menus are set in Shopify admin: `senseless-main` (header), `senseless-footer-shop` / `-explore` / `-company` (footer columns Shop / The system / Brand). **Footer menus must be kept injectable-clean (no Botox/filler/injection links) when wired in Stage D.**

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
