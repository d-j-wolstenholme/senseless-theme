# Brand Design System

The canonical code-side mirror of the Brand & Product System Notion page.

## Brand

- **Name:** Senseless
- **Parent:** Matrix Health Group Ltd
- **Audience:** Female users — cosmetic and aesthetic procedure clients
- **Headline:** Confidence Starts With Comfort
- **Positioning:** Premium, professional, clinical-aesthetic, female-leaning, UK formulated

## Colours

| Token | Value | Use |
|---|---|---|
| `--color-brand-purple` | `#6B3FA0` | Brand accent (matches packaging) |
| `--color-bg-warm` | `#f7f7f5` | Warm off-white background |
| `--color-bg-white` | `#ffffff` | White card surfaces |
| `--color-text-primary` | `#1a1a1a` | Headings, primary text |
| `--color-text-body` | `#4a4a50` | Body text |
| `--color-border-subtle` | `rgba(26,26,26,0.10)` | Card borders |

Purple is an **accent only** by default — not used as button fill or large area background. Used for hover states, accent lines, the brand asterisk graphic, occasional emphasis.

## Typography

- **Headings (H1–H4):** Manrope, weights 500–700, no text-transform
- **Body:** Inter, weight 400
- **UI/labels:** Inter, weight 500, slight letter-spacing
- **Optional accent (use sparingly):** TBC editorial display cut for hero numerals or pull-quotes

### Type Scale

| Element | Size | Line Height | Letter Spacing |
|---|---|---|---|
| H1 | 40px | display-normal | heading-normal |
| H2 | 32px | display-tight | heading-normal |
| H3 | 20px | display-normal | heading-normal |
| H4 | 16px | display-tight | normal |
| H5 | 14px | display-loose | normal |
| H6 | 12px | display-loose | normal |
| Body | 16px | 1.6 (loose) | normal |

## Components

- **Card corner radius:** 4px
- **Product card corner radius:** 0
- **Button border radius:** 14px (primary and secondary)
- **Badge corner radius:** 100 (pill-shaped)
- **Input border radius:** 4px, 1px border
- **Variant swatch:** 34×34px, radius 32
- **Variant button:** 14px radius, 1px border

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
