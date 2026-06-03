# Phase 7 follow-up — meta trims + Shop mega CTA swap

**Date:** 2026-06-03 (BST) · **Branch:** dev · **Theme:** Senseless Dev `#199324434780` (store `senseless-numbing`)
Token refreshed (`./scripts/refresh-token.sh` → shpca_fa2d3c…).

## 1. Meta trims (global.* metafields)
- **`/pages/using-numbing-cream`** description 159 → **153** (≤155): "How to use numbing cream, how long to leave it on, and how long it lasts — an honest guide. Always follow the product instructions and your practitioner." (kept the how-long-it-lasts / how-to-use / follow-product-instructions sense; no efficacy/duration claims).
- **`/pages/does-it-hurt-by-treatment`** title 70 → **43** (≤60): "Does It Hurt? Pain by Treatment — Senseless".

## 2. Shop mega-menu CTA swap
- Setting (`header-group.json`): `mega_cta_label` "Find your strength" → **"Shop all"**; `mega_cta_url` `/pages/the-senseless-system` → **`/collections/numbing-cream`** (the full range / Shop All). It's the Shop menu, so the bottom action now drives into the catalogue, not a guide.
- **Highlighted as the primary action:** restyled `.ss-hdr__megacta a` from a plain purple text link to a **filled purple button** — `background:#6B3FA0`, white text, 14px radius (brand button radius), `inline-flex`, hover `#5A3489`, `→` arrow. Updated the schema label default + info hint to match.

## Verify
- **theme-check: 0 errors.**
- **Asset-API diff:** `header-group.json` remote = `Shop all` → `/collections/numbing-cream`; filled-button CSS present in `senseless-header.liquid`.
- **Render-verify (Playwright, live preview):**
  - Shop mega CTA: label **"Shop all"**, href **`/collections/numbing-cream`**, computed **filled button** (bg `rgb(107,63,160)` = #6B3FA0, color white, radius 14px, inline-flex); target resolves **200**.
  - Meta: `using-numbing-cream` `<meta description>` **153** chars; `does-it-hurt-by-treatment` `<title>` core (title_tag) **43** chars — both within limits.

## Files / API
- Edited: `sections/header-group.json` (mega CTA label+url), `sections/senseless-header.liquid` (megacta button CSS + schema hint).
- API: `metafieldsSet` (2 meta trims). No template files changed (meta is metafield-driven).

## HOLD
Meta within limits on both pages; Shop mega CTA now a highlighted "Shop all" button into the catalogue.
