# Images — 1:1 square default, site-wide (Canonical §11 standing rule)

**Date:** 2026-06-02 (BST) · **Machine:** MacBook Pro (continued) · **Branch:** dev · **Commit:** `4969c7c`
**Theme:** Senseless Dev `#199324434780`

## Rule
Every image defaults to **1:1 square** — `aspect-ratio: 1 / 1` on the wrapper + `object-fit: cover` on the `<img>`, so any source crops to square cleanly (no distortion). Set as the section DEFAULT so future pages inherit it. Non-square is allowed **only as a deliberate per-section override**.

## Audit + changes (image-bearing senseless sections + product gallery)
| Section | Was | Now |
|---|---|---|
| collection-hero (`.ss-chero__media`) | 4/5 + 16/9 desktop | **1/1** |
| guide-hero (`.ss-gh__media`) | 4/3 | **1/1** |
| image-text-band (`.ss-itb__media`) | 4/5 + 3/2 desktop | **1/1** |
| hero-brand-led (`.ss-hero__stage`) | 4/5 | **1/1** (product still floats `object-fit:contain` within the square stage) |
| product-hero gallery (`.ss-ph__main`) | 4/5 | **1/1** |
| product-grid (`.ss-pg__media`) | 4/5 | **1/1** |
| product-showcase (`.ss-ps__media`) | 1/1 base, desktop `aspect-ratio:auto` | **1/1** (removed the auto override) |
| collection-grid, cross-sell, procedure-grid, trio-card-row, complete-prep | already 1/1 | unchanged |

All media imgs already had `object-fit: cover` (except the hero stage, intentionally `contain` for the floating-product composition — squared frame, product centred).

## Verification (Playwright, computed ratios = width/height)
| Page | Element | Ratio |
|---|---|---|
| /collections/numbing-gel | `.ss-chero__media` / `.ss-cg__media` | 1.000 / 1.000 |
| /products/clinical-strength-cream | `.ss-ph__main` (gallery) / `.ss-itb__media` (editorial) | 1.000 / 1.000 |
| / (home) | `.ss-hero__stage` / `.ss-itb__media` / `.ss-card__media` | 1.000 / 1.000 / 1.000 |

(All seven built collections use collection-hero + collection-grid, both verified 1:1; product pages + home verified above.) Images are placeholders pre-launch, but the **frames are square**, so uploaded sources crop to square automatically.

- theme-check **0**; Asset-API diff: all 7 squared sections **match remote**.
- **Screenshots** captured for sign-off: card grid (`/tmp/sq-cardgrid.png`), product gallery (`/tmp/sq-gallery.png`), editorial image (`/tmp/sq-editorial.png`) — all render square.

## Docs updated (same session)
- `docs/BRAND.md` — new **Images** section (1:1 standing rule + override note + squared-section list).
- `DECISIONS-LOG.md` — dated entry (2026-06-02 15:05 BST).

## HOLD
1:1 square default applied + verified site-wide. Nothing else started.
