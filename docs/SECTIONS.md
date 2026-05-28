# Section Library Index

Auto-updated by the `create-section` skill. Don't edit manually unless removing a deprecated section.

| Section File | Purpose | Used On | Last Updated |
|---|---|---|---|
| `senseless-hero-brand-led.liquid` | Brand-led full-bleed hero (text-left/image-right desktop, stacked mobile, 2 CTAs, fetchpriority high) | Homepage (S1) | 2026-05-28 |
| `senseless-trio-card-row.liquid` | Reusable card row, `columns` 3/4; blocks: tier_card, procedure_card, product_card; flagship variant | Homepage (S2 tiers, S3 procedures, S6 products) | 2026-05-28 |
| `senseless-image-text-band.liquid` | Two-column image+text, `direction` text-left/text-right | Homepage (S4, S7) | 2026-05-28 |
| `senseless-trust-bar.liquid` | Trust signals strip (icon+label blocks), single row desktop / 2×2 mobile | Homepage (S5) | 2026-05-28 |
| `senseless-newsletter-signup.liquid` | Single-field email signup (Shopify customer form, GDPR double opt-in) | Homepage (S8) | 2026-05-28 |

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

No hard-coded copy in section files. Everything must be editor-accessible.
