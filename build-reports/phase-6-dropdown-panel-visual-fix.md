# Phase 6 — Header dropdown panel "transparency" — true root cause + fix

**Date:** 2026-06-03 (BST) · **Branch:** dev · **Theme:** Senseless Dev `#199324434780` (store `senseless-numbing`)
Token refreshed (`./scripts/refresh-token.sh` → shpca_0ab033…).

## Actual root cause (diagnosed live, before editing)
The previous fix (a27406c) set `.ss-hdr__panel { background:#ffffff }` + `.ss-hdr__panels { z-index:99 }`. Live diagnosis on `/pages/does-it-hurt` proves that fix **did** make the panel opaque and on top:
- **9-point `elementFromPoint` probe** across the full panel band (left/centre/right × top/mid/bottom): every point returns `inPanel: true` with effective `background-color: rgb(255,255,255)` on `.ss-hdr__panel`. Panel rect = full width (0–1280), opaque.
- Screenshot confirms the hero **H1 is covered** by the panel; only the hero **subhead below** the short 2-item panel is visible.

So it was **not** a transparency or z-index bug. The real problem was **visual**: the panel is `#ffffff` sitting on the `#f7f7f5` canvas (~2% difference) with a faint shadow (`0.12`), so the solid panel **blended into the page** — the menu items read as "floating over content," which looks like bleed-through, especially on the short 2-item "The System" panel where the page subhead sits right beneath it.

## Fix
Made the panel read as a clearly elevated, distinct solid surface (scoped to the header, no global fixed/sticky — per the ARCHITECTURE standard):
- `box-shadow` `0 12px 28px rgba(26,24,22,0.12)` → **`0 18px 40px rgba(26,24,22,0.22)`** (deeper, larger — clear elevation off the off-white page).
- `border-bottom` `1px solid var(--ss-border)` → **`1px solid rgba(26,24,22,0.18)`** (crisper bottom edge separating the panel from content below).
- Background stays solid `#ffffff`; `z-index:99` retained. Applies to **all** dropdowns (Shop, The System, Help) via `.ss-hdr__panel`.

## Verify
- **theme-check: 0 errors.**
- **Computed-style + `elementFromPoint`, hub + homepage, all 3 dropdowns:** panel `background-color: rgb(255,255,255)`, full width (1280), `inPanel: true` at the panel's lower edge (panel on top), strengthened shadow present (`rgba(26,24,22,0.22) 0 18px 40px`).
- **Visual check (screenshot, /pages/does-it-hurt):** the panel now reads as a distinct white shelf with a clear drop shadow; page content sits visibly **below** it (separated by the shadow), not through it. No page text shows through the panel box.
- **Mobile unaffected:** `.ss-hdr__panels { display:none }` at the mobile breakpoint — the mobile drawer (`.ss-hdr__drawer`) is a separate element, untouched.

## Files
- Edited: `sections/senseless-header.liquid` (panel shadow + border strengthened).

## Note
If a still-stronger separation is wanted (e.g. a faint top hairline or a slightly tinted panel), easy to bump further — but the panel is now provably opaque and clearly elevated. The pre-existing About/Help branch 404s (flagged in the nav-fix report) remain a separate open item.

## HOLD
Dropdown panels render as solid, clearly-elevated surfaces on hub + homepage (Shop / The System / Help); mobile drawer unaffected.
