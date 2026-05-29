# Brand Design System

The canonical code-side mirror of the Brand & Product System Notion page.

## Brand

- **Name:** Senseless
- **Parent:** Matrix Health Group Ltd
- **Audience:** Female users — cosmetic and aesthetic procedure clients
- **Headline:** Confidence Starts With Comfort
- **Positioning:** Premium, professional, clinical-aesthetic, female-leaning, UK formulated

## Colours

Locked colour-text ladder. Defined globally in `snippets/senseless-typography.liquid` (`:root`) and mirrored as `--ss-*` tokens inside every Senseless section.

| Token | Value | Use |
|---|---|---|
| `--brand-primary` | `#6B3FA0` | Brand accent (matches packaging); Professional border + filled CTA |
| `--bg-canvas` | `#f7f7f5` | Warm off-white page background |
| `--bg-surface` | `#ffffff` | White card / panel surfaces |
| `--text-primary` | `#1A1816` | Headings, primary text |
| `--text-body` | `#2B2730` | Running body copy |
| `--text-secondary` | `#5C5853` | Leads, captions, secondary text |
| `--text-muted` | `#8E8A82` | Muted / de-emphasised text |
| `--color-border-subtle` | `#E5E2DC` | Card / divider borders |

Purple is an **accent only** by default — not used as a large area background. The only filled-purple treatments are the Professional tier's 2px `#6B3FA0` border + filled CTA. Otherwise used for hover states, accent lines, the brand asterisk graphic, occasional emphasis.

## Typography

Typeface is **Montserrat**, self-hosted via the Shopify font CDN (no `fonts.googleapis.com` / `gstatic.com` requests). Wired through Horizon's font settings: body `montserrat_n4`, subheading `montserrat_n6`, heading `montserrat_n7`, accent `montserrat_n6`. Preloads: weight 400 (body) + 700 (heading) only.

- **Headings:** Montserrat 700 (H1/H2), 600 (H3), no text-transform
- **Body:** Montserrat 400, line-height 1.7
- **UI/labels/eyebrow:** Montserrat 600, uppercase, wide tracking
- **Emphasis (`.t-em`):** italic 600

Global classes live in `senseless-typography.liquid`: `.ss-h1`/`h1.senseless`, `.ss-h2`, `.ss-h3`, `.eyebrow`, `.lead`, `.body-small`, `.caption`, `.t-em`. Sections use their own `.ss-*` scoped classes (so global element rules never override section-tuned sizes) but inherit the same fonts + ladder.

### Type Scale

Fluid via `clamp()`. Format below: `clamp(min, preferred, max)`.

| Element | Size | Line Height | Weight | Letter Spacing |
|---|---|---|---|---|
| H1 (`.ss-h1`) | `clamp(2.5rem, 1.5rem + 4vw, 4rem)` | 1.04 | 700 | -0.03em |
| H2 (`.ss-h2`) | `clamp(1.875rem, 1.2rem + 3vw, 2.75rem)` | 1.1 | 700 | -0.025em |
| H3 (`.ss-h3`) | `clamp(1.25rem, 1.18rem + 0.3vw, 1.375rem)` | 1.25 | 600 | -0.01em |
| Lead (`.lead`) | `clamp(1.125rem, 0.95rem + 0.8vw, 1.375rem)` | 1.55 | 400 | — (secondary) |
| Body | `clamp(1rem, 0.98rem + 0.13vw, 1.0625rem)` | 1.7 | 400 | -0.003em |
| Body small (`.body-small`) | `0.875rem` | 1.6 | 400 | — |
| Caption (`.caption`) | `0.8125rem` | 1.5 | 400 | — (secondary) |
| Eyebrow (`.eyebrow`) | `0.75rem` | — | 600 | 0.2em, uppercase, brand-primary |

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
