# Contact "Pick the right channel" (no-image cards) + About enquiries line

**Date:** 2026-06-04 (BST) · **Branch:** dev · **Theme:** Senseless Dev `#199324434780` · **Commit:** `e78f722`. Token refreshed.

## Problem
- **Contact §2** ("Pick the right channel") reused an image-bearing card module (`senseless-trio-card-row` / `format_card` blocks), so the four channel cards rendered with **empty image placeholder boxes** and uneven heights.
- **About** had no direct enquiries contact line on the company/MHG disclosure band.

## PART A — Contact §2 rebuilt (no-image cards)
- New section **`sections/senseless-contact-cards.liquid`** — no image. Each card = **Label + Body + CTA**, `display:flex;flex-direction:column;height:100%` with the CTA `margin-top:auto` (pinned to the bottom → equal heights regardless of body length). Grid **2-col mobile → 4-col desktop** (@860px). Brand tokens (`#6B3FA0`, canvas band, Montserrat, 4px card radius, subtle border).
- `templates/page.contact.json` `routes` section swapped to `senseless-contact-cards`, 4 blocks:
  | Card | CTA | Target |
  |---|---|---|
  | Customer enquiries | Contact form | `#contact-form` (in-page form anchor) |
  | For clinics and practitioners | Visit the trade page | `/pages/trade` |
  | Media and partnerships | Email us | `mailto:cs@senseless.uk` |
  | Data, privacy, legal | Email us | `mailto:cs@senseless.uk` |
- **All placeholder emails = `cs@senseless.uk`** (per your override — site-wide CS address), each flagged "(placeholder — confirm before launch)".
- Hero, form §3, company §4 left untouched. **Contact stays `noindex,nofollow`.**

## PART B — About enquiries line
- Appended to the `company` band (`senseless-image-text-band`, the Matrix Health Group disclosure) body:
  `Enquiries: cs@senseless.uk · 0333 049 5549` (mailto + `tel:+443330495549`). No form added; existing §7-onward Contact link kept.

## Verify (password render, desktop + mobile)
- **Contact §2:** 4 `.ss-cc4__card`, **no images** (`anyImg=false` — placeholder boxes gone), **equal heights + row-aligned**, **4-up desktop / 2×2 mobile**, robots `noindex,nofollow`. CTAs: `#contact-form`, `/pages/trade` (200), `mailto:cs@senseless.uk` ×2.
- **About:** enquiries line renders — `cs@senseless.uk` ✓ and `0333 049 5549` ✓ in the company band.
- **theme-check: 0 errors** (31 warnings, pre-existing).

## Files
- New: `sections/senseless-contact-cards.liquid`
- Edited: `templates/page.contact.json`, `templates/page.about.json`

## Open / standing
- `cs@senseless.uk` is a **placeholder** across all four Contact cards + the About line — confirm the real CS inbox before launch (single find/replace).
- `senseless-trio-card-row` remains in use elsewhere (best-numbing-cream etc.) — untouched.

## HOLD
Contact cards + About enquiries line live + verified.
