# Brand Design System

The canonical code-side mirror of the Brand & Product System Notion page.

## Brand

- **Name:** Senseless
- **Parent:** Matrix Health Group Ltd
- **Audience:** Female users — cosmetic and aesthetic procedure clients
- **Headline:** Confidence Starts With Comfort
- **Positioning:** Premium, professional, clinical-aesthetic, female-leaning, UK formulated
- **Product naming:** Senseless products are named with **"Comfort"** — **Comfort Cream / Comfort Gel / Comfort Spray** (the brand name; describes the user experience, asserts no physiological mechanism). **"Numbing [format]"** is used only as an **SEO category descriptor** on search-facing surfaces (collections, meta keywords, guide/article body), never as the product name or in effect-attributing copy. See `docs/COMPLIANCE.md` → *Product naming — UK cosmetics compliance*.

## Colours

Locked colour-text ladder. Defined globally in `snippets/senseless-typography.liquid` (`:root`) and mirrored as `--ss-*` tokens inside every Senseless section.

| Token | Value | Use |
|---|---|---|
| `--brand-primary` | `#6B3FA0` | Brand accent (matches packaging); primary CTA fill + Professional border |
| `--brand-primary-hover` | `#5A3489` | Darkened brand purple — primary CTA / link hover. Wired into `scheme-1` (`primary_hover`, `primary_button_hover_*`) and `--ss-purple-hover` in sections |
| `--bg-canvas` | `#f7f7f5` | Warm off-white page background |
| `--bg-surface` | `#ffffff` | White card / panel surfaces |
| `--text-primary` | `#1A1816` | Headings, primary text |
| `--text-body` | `#2B2730` | Running body copy |
| `--text-secondary` | `#5C5853` | Leads, captions, secondary text |
| `--text-muted` | `#8E8A82` | Muted / de-emphasised text |
| `--color-border-subtle` | `#E5E2DC` | Card / divider borders |

Purple is an **accent only** by default — not used as a large area background. Filled-purple treatments are: **primary CTAs** (the `scheme-1` primary button is brand purple, hover `#5A3489`) and the Professional tier's 2px `#6B3FA0` border. Otherwise used for hover states, accent lines, the brand asterisk graphic, occasional emphasis. (Canvas stays `#f7f7f5`; the bespoke `senseless-footer` defaults to an **ink** band, never a large purple fill.)

## Typography

Typeface is **Montserrat**, self-hosted via the Shopify font CDN (no `fonts.googleapis.com` / `gstatic.com` requests). Wired through Horizon's font settings: body `montserrat_n4` (400), subheading `montserrat_n6` (600), heading `montserrat_n7` (700), accent `montserrat_n6`. Weight **500** (`montserrat_n5`, medium) is also self-hosted — emitted via `font_modify: 'weight', '500'` + `font_face` in `senseless-typography.liquid` — so the working weights are **400 / 500 / 600** (700 retained only for the header wordmark, footer column labels, the pull-quote glyph, and the FAQ-accordion group labels — see the FAQ override note below). Head weights now load 400 (body) + 500 (medium/accent) — see the reweight note below.

**Reweight — 2026-06-02 (Strand 1):** display/section heads dropped from 700 → **400** (700 read poster-like). Tracking → -0.02em; line-height 1.06/1.08 (H1), 1.1/1.12 (H2). H3/card titles + eyebrow **unchanged (600)**. Italic accent → **500**.

**FAQ-accordion override — 2026-06-28 (edited on the live theme, Mac mini; in repo via commit `67dc679`):** `senseless-faq-accordion` carries a **bespoke** type treatment, intentionally distinct from the global H3 / eyebrow specs below — questions lighter and smaller, group labels heavier and larger ("calmer question type + bolder eyebrows for clearer hierarchy"). This is a component-scoped exception to "H3/card titles = 600"; the global H3/eyebrow rows in the Type Scale table are **unchanged**.
- **Group label** (`.ss-faq__group`): weight **700**, `0.8125rem`, letter-spacing `0.18em`, uppercase, brand-primary, margin `44px 0 14px` (vs the eyebrow's 600 / `0.75rem` / `0.2em`).
- **Question** (`.ss-faq__q`): weight **500**, `clamp(1.0625rem, 1.01rem + 0.25vw, 1.125rem)`, line-height `1.35`, letter-spacing `-0.005em`, padding `18px` block (vs the H3 600 / `1.25–1.375rem` / `1.25` / `-0.01em` it previously inherited).
- **Toggle glyph** (`.ss-faq__q::after`): `19px`.

- **Headings:** Montserrat **400** (H1/H2), 600 (H3 / card titles), no text-transform
- **Body:** Montserrat 400, line-height 1.7
- **UI/labels/eyebrow:** Montserrat 600, uppercase, wide tracking
- **Italic accent (`.ss-accent` / `.t-em`):** Montserrat italic **500** — exactly one emphasis word per hero/section head, same colour as the head (no purple), never the keyword (the Senseless-positioning/decision word). Built sections take their word from the page word-map.

Global classes live in `senseless-typography.liquid`: `.ss-h1`/`h1.senseless`, `.ss-h2`, `.ss-h3`, `.eyebrow`, `.lead`, `.body-small`, `.caption`, `.t-em`. Sections use their own `.ss-*` scoped classes (so global element rules never override section-tuned sizes) but inherit the same fonts + ladder.

### Type Scale

Fluid via `clamp()`. Format below: `clamp(min, preferred, max)`.

| Element | Size | Line Height | Weight | Letter Spacing |
|---|---|---|---|---|
| H1 (`.ss-h1`) | `clamp(2.5rem, 1.5rem + 4vw, 4rem)` | 1.06 / 1.08 mob | 400 | -0.02em |
| H2 (`.ss-h2`) | `clamp(1.875rem, 1.2rem + 3vw, 2.75rem)` | 1.1 / 1.12 mob | 400 | -0.02em |
| H3 (`.ss-h3`) | `clamp(1.25rem, 1.18rem + 0.3vw, 1.375rem)` | 1.25 | 600 | -0.01em |
| Lead (`.lead`) | `clamp(1.125rem, 0.95rem + 0.8vw, 1.375rem)` | 1.55 | 400 | — (secondary) |
| Body | `clamp(1rem, 0.98rem + 0.13vw, 1.0625rem)` | 1.7 | 400 | -0.003em |
| Body small (`.body-small`) | `0.875rem` | 1.6 | 400 | — |
| Caption (`.caption`) | `0.8125rem` | 1.5 | 400 | — (secondary) |
| Eyebrow (`.eyebrow`) | `0.75rem` | — | 600 | 0.2em, uppercase, brand-primary |

## Components

- **Card corner radius:** 4px
- **Product card corner radius:** 4px *(standardised 2026-06-12 to the theme-majority value; the prior "0" was never built — no card used it. Cards = 4px, buttons/inputs/buy-controls = 14px, pills/badges = 999px.)*
- **Button border radius:** 14px (primary and secondary)
- **Badge corner radius:** 100 (pill-shaped)
- **Input border radius:** 4px, 1px border
- **Variant swatch:** 34×34px, radius 32
- **Variant button:** 14px radius, 1px border

## Images

- **Default aspect ratio: 1:1 square, site-wide (standing rule, Canonical §11, 2026-06-02).** Every image-bearing element — product/collection cards, galleries, editorial/content images, hero media — defaults to `aspect-ratio: 1 / 1` on the wrapper + `object-fit: cover` on the `<img>`, so any source crops to square cleanly (no distortion). This is the section DEFAULT, so future pages inherit it.
- A **non-square ratio is allowed only as a deliberate per-section override**, never the default.
- Squared sections: collection-hero, guide-hero, image-text-band, hero-brand-led (stage), product-hero (gallery), product-grid, product-showcase, collection-grid, cross-sell, procedure-grid, trio-card-row, complete-prep (thumbnail).

## Spacing

- **Section padding desktop:** 96px vertical
- **Section padding tablet:** 56px vertical (≤989px)
- **Section padding mobile:** 44px vertical (≤749px)
- **Container max-width:** narrow
- **Card padding:** 24–32px depending on density
- **Gutter spacing:** 16–24px depending on context

## Cart

- **Type:** drawer (auto-opens on add to cart)
- **Drop shadow:** enabled

## Imagery

- Editorial, premium, soft warm tones
- No clinical/medical setting imagery on consumer pages
- People photography: natural, unmedicated, female-leaning
- No before/after shots implying medicinal effect (compliance)

## Brand Asterisk

Purple six-point asterisk graphic from packaging. Used as visual signature — hero accent, section dividers, footer mark. Always brand purple (`#6B3FA0`) on light backgrounds. Minimum size 16px.

## Image Pipeline Tokens

See `docs/SECTIONS.md` and `scripts/image-pipeline.mjs`. Image naming: `senseless-[page-or-context]-[descriptor]`. Image manifest at repo root.

## Reference Brands

Visual benchmark — clinical-aesthetic premium: Augustinus Bader, Dieux, Wildsmith Skin, 111SKIN, The Inkey List.
