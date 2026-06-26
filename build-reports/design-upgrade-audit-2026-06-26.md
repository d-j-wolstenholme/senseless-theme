# Senseless — Design-Upgrade Audit (2026-06-26)

**Method:** 9 parallel reviewers (5 pages + 4 cross-cutting dimensions), each grounded in `BRAND.md`, grading findings impact × effort, on-brand. Reviewers ran on a fast model and assessed **code, not rendered pixels** — so treat exact contrast numbers as "verify," and a few findings were stale (filtered below).

## Filtered out (false / already done — do NOT action)
- **"Reviews page empty / install Judge.me"** (3 reviewers) — FALSE. Reviews render fine in-browser (4.9 / 231); the reviewers curl'd and saw the no-JS placeholder, same artifact that bit me earlier. No action.
- **"Strength-ladder shows Scale + matrix both"** — already fixed today (`bc0602a`).
- Exact muted-contrast figures conflicted across reviewers (2.3 / 4.5 / 4.7); real value of `#8E8A82` on `#f7f7f5` ≈ **3.2:1** — so it *does* fail AA for body text (the concern is real; the numbers weren't).

---

## P1 — Accessibility (cheap, high-value, do first)
| # | Fix | Where | Impact/Effort |
|---|---|---|---|
| 1 | **`:focus-visible` sweep** — keyboard users get no focus ring on the key interactive elements | Add-to-cart (`.ss-ph__atc`), cart-offer add (`.ss-co__add`), card image links (`.ss-cg__media`), PDP thumbnails (`.ss-ph__thumb`), cart qty steppers (`.ss-co__qbtn`), contact/trade `select`+`textarea` | High / S |
| 2 | **Bump `--text-muted`** `#8E8A82` (~3.2:1, fails AA) → ~`#6E6A63` (≥4.5:1), or restrict it to large text only | `senseless-typography.liquid` — one token, cascades | High / S |
| 3 | **Form errors not colour-only** — add an icon + `role="alert"` + "Error:" prefix (WCAG 1.4.1) | `senseless-contact-form.liquid` | High / S |
| 4 | **Out-of-stock variant chips look selectable** — add `input:disabled + label { opacity:.4; cursor:not-allowed }` | `senseless-product-hero.liquid` | Med / S |

## P2 — Mobile quick wins
| # | Fix | Impact/Effort |
|---|---|---|
| 5 | **Size chips → 2-col grid at ≤749px** (currently ragged flex-wrap on narrow phones) | High / S |
| 6 | **Mobile H3 line-height 1.25 → 1.35** (card titles cramped at ~20px) | High / S |
| 7 | **Mobile section separator opacity 0.07 → ~0.15** (currently invisible) | High / S |
| 8 | Hero CTA button height 52 → 48px + tighter gap at ≤749px (overflow risk on iPhone SE) | Med / S |
| 9 | Mobile card-grid gap 16 → 12px; key-facts mobile row gap 2 → 12px | Med / S |

## P3 — Rhythm & polish
- **Practitioner cards padding 72px → 96px** (only section off the brand 96/56/44 rhythm). Med/S.
- **PDP buy-box** price→form gap 4px → 12px (cramped). Med/S.
- **Eyebrow fluid sizing** `clamp(0.625rem … 0.875rem)` (fixed 12px swings vs H1 64px / H3 20px). Med/S.
- **Scale breakpoint 600 → 750px** to match Selector/Ladder on the System page. Med/S.

## P4 — Conversion
- **Selector callout → primary (filled purple) CTA** — "Find the right tier" is a key decision tool currently styled as a secondary outline button; promote it (add a `cta_style` option to `senseless-callout-band`). High/M.
- **Surface reviews higher on the PDP** — the 4.9/231 is strong but the dedicated reviews block sits low (after FAQ); move it nearer the hero/system band. Med-High/M.
- **Professional-tier marker** — on the Scale, the 2px purple border barely changes on hover; a subtle background tint or 3px top-accent makes the "practitioner tier" read at a glance (stays on-brand — no fill). Med/S.

## P5 — Motion & animation (your specific ask)
All on-brand = restrained, single-play, `prefers-reduced-motion`-safe. The theme already has the reveal + hover engine, so these extend it.
| # | Animation | Impact/Effort |
|---|---|---|
| M1 | **Count-up on the 4.9 trust-bar rating** (0 → 4.9 on reveal, ~800ms) — the standout pick; premium trust mechanic | High / M |
| M2 | **Staggered section headers** — eyebrow → headline → body cascade (0/120/240ms) instead of one batch | High / M |
| M3 | **Per-row grid stagger** — refine the card reveal so row 2 feels intentional, not capped | Med / S |
| M4 | **Ken-Burns on product image hover** — slow scale + 1–2% pan (current is a flat 1.05 zoom) | Med / M |
| M5 | **Shipping-bar milestone pulse** when £40 / £80 thresholds unlock | Med / S |
| M6 | **CTA arrow micro-stagger** — arrow slides after the label settles (80ms delay) | Low / S |

## Brand judgment calls (your decision — not auto-applying)
- **H1/H2 at 400 weight** — a reviewer flags low weight-contrast vs 400 body. But this was a **deliberate Strand-1 decision** (poster-like). Only revisit if *you* feel the hierarchy reads weak; bumping to 500 is the lever.
- **Default-underline card titles** — would aid discoverability but adds visual weight against the clean look; the whole-card hover may be enough. Your call.

---
*Genuine findings ≈ 30 across the 9 reviewers; full per-reviewer detail in the workflow output. Top quick-win batches: P1 (a11y) + P2 (mobile) are ~9 small edits with outsized impact.*

---

## Deployment addendum — 2026-06-26 (MacBook Pro)

The design-upgrade batch (commit `8b14fe4`) was reviewed, fixed, deployed to the **live** theme (`#199324434780`), and verified. Plus the two pending manual edits.

### Review fixes before deploy
- **Reveal grid-stagger (`snippets/senseless-reveal.liquid`, commit `57d3741`)** — the committed M3 used a hardcoded 3-column assumption with an uncapped 200ms row step. Every reveal-group grid is responsive/settings-driven (`cols-2/3/4`, single-column at mobile), so the 3-col assumption mis-rowed the cascade and deep cards could wait too long after entering view. Now derives the column count from the *rendered* `grid-template-columns` (falls back to `data-cols`, then 3) and caps the delay at 360ms (row 120ms + col 60ms).
- **Trust-bar count-up, shipping-banner pulse, callout-band `cta_style`** — reviewed, no changes needed. Count-up: IO-gated, reduced-motion-safe, double-init guarded, decimals derived from the source string. Pulse: `prevTier` tracks upward crossings only, no pulse on first paint, resets on empty cart, restart-safe reflow. Callout-band: `--ss-purple-hover` confirmed in scope, default `secondary` preserves existing outline rendering.

### Deployed (scripts/deploy.sh, batched; live marker verify passed each time)
1. **Guarded** (`--reviews-changed`, lock re-pinned commit `217ad13`): `senseless-product-hero`, `senseless-collection-grid` — both were in the reviews manifest (markers `@app` / `judgeme`); changes were pure focus/hover/mobile CSS, markers intact.
2. **Normal batch**: callout-band, contact-form, hero-brand-led, practitioner-cards, trust-bar, cart-offer, reveal, scale, shipping-banner, typography.
3. **Manual edits** (commit `fcd0422`):
   - **3a** `templates/index.json` — Selector callout `cta_style: "primary"` ("Find the right tier" now a filled CTA).
   - **3b** `templates/product.*.json` (all 11 PDPs) — reviews section moved to immediately after the core-info block (`keyfacts`, or `system` on the bundle), above FAQ + outbound link rows. **Assumption logged:** applied to all PDPs for consistency (brief said "…cream.json *etc.*"); deterministic anchor rule, not just the one named template.

### Live verification (curl, live theme serving)
- Home: `ss-cb__cta--primary` + "Find the right tier" present; trust-bar `data-count-to="4.9"` + `ssTrustCountUpInit` wired; `ss-scale__tier--pro` tint present.
- PDP (`clinical-strength-cream`): section render order now `…keyfacts → reviews → linksout → faq…` (reviews lifted from after-FAQ); `ss-ph__atc:focus-visible`, `ss-ph__opt-values` (mobile 2-col chips), `ss-ph__thumb:focus-visible`, disabled-variant CSS all present.
- theme-check: **0 errors** (1819 pre-existing Horizon-base warnings, unchanged).
- **Not visually confirmed:** animation playback (count-up easing, focus-ring on Tab, pulse on threshold) — Chrome extension wasn't connected this session. Code paths all present in live HTML + reviewed; a browser pass is the only outstanding check.

### Deferred to a later session
- **M2 — staggered section headers** (eyebrow → headline → body cascade). Not started.
- Browser visual QA of the motion set once the Chrome extension is connected.
