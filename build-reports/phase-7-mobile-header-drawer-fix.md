# Mobile header + drawer fix (raw store name + transparent drawer)

**Date:** 2026-06-03 (BST) · **Branch:** dev · **Theme:** Senseless Dev `#199324434780` (store `senseless-numbing`)
Token refreshed (`./scripts/refresh-token.sh` → shpca_4ff388…).

## Root causes (diagnosed live before editing)
The two symptoms were one linked bug, **not** a Horizon fallback — the header group contains only `senseless-header` (no default `header` section).

1. **Raw "senseless-numbing" text.** The mobile **drawer head** rendered `<span class="ss-hdr__wordmark">{{ shop.name }}</span>` — i.e. the raw store handle as a text wordmark — instead of the SENSELESS SVG logo the bar uses. (The bar's mobile + desktop logos correctly inline `senseless-logo-header.svg`; only the drawer head used `shop.name` text.)
2. **Transparent drawer.** The `--ss-*` brand vars (incl. `--ss-bg`) are defined **only on `.ss-hdr`**. The drawer + scrim render as **siblings outside `.ss-hdr`** (they must — `.ss-hdr`'s `backdrop-filter` would make their `position:fixed` resolve against the 81px header box instead of the viewport). Being non-descendants, they don't inherit those vars, so the drawer's `background: var(--ss-bg)` resolved to **nothing → transparent** (its text/border/font vars failed too).

Combined: with the drawer open, its `shop.name` head showed over the header's SENSELESS logo *through* the transparent drawer — exactly the reported overlap.

## Fix
- **Drawer head → SVG logo.** Replaced the `shop.name` wordmark span with the shared `logo_markup` (the inline SENSELESS SVG). `shop.name` now appears only in non-visual `aria-label`. No raw store name renders anywhere.
- **Drawer opaque + correct colours.** Defined the brand `--ss-*` vars **on `.ss-hdr__drawer`** itself (it can't inherit them across the `.ss-hdr` boundary) and hardcoded `background: #f7f7f5` (belt-and-braces). This restores the opaque drawer surface plus correct fonts/text/border/accent colours for the nav, accordion and footer. z-index 120 (scrim 110) already above page content.

## ARCHITECTURE standard extended
Added a **"Menu-surface standard"** subsection to `docs/ARCHITECTURE.md`: all menu surfaces opaque (desktop dropdowns `#fff`, mobile drawer `#f7f7f5`, submenu/accordion expansions); the custom header renders at every breakpoint (no Horizon fallback) and never renders raw `shop.name` as a visible wordmark (SVG logo only; `shop.name` only in alt/aria-label); sibling surfaces outside `.ss-hdr` (drawer/scrim) must define their own brand vars rather than relying on inheritance.

## Verify (real mobile viewport, 390×844)
- **theme-check: 0 errors.**
- **Header:** mobile SENSELESS **SVG logo** visible; **no visible "senseless-numbing" text** anywhere in header/drawer (DOM scan = none).
- **Drawer:** computed `background-color: rgb(247, 247, 245)` (opaque); drawer head = SVG logo, **no `shop.name` wordmark**; with consent banners removed, **3/3 probe points inside the drawer return drawer content (zero bleed-through to page)**. Screenshot confirms: solid drawer with legible nav, the SENSELESS logo, and the right-edge **scrim** dimming the page (correct), not see-through.
- **Submenu expansion:** accordion panel opaque over the drawer, 12 links.
- **Desktop unaffected:** changes are drawer-scoped (drawer head markup + `.ss-hdr__drawer` CSS); the desktop bar + dropdown panels (`.ss-hdr__panel`) were not touched.

## Observation (not a defect, out of scope)
On mobile, the **cookie-consent banner** (`.ss-cc`, fixed bottom, z-index 1000) overlaps the lower part of the open drawer — it legitimately sits above all surfaces as a consent gate. Flagging only; left as-is.

## Files
- Edited: `sections/senseless-header.liquid` (drawer head logo + drawer vars/bg), `docs/ARCHITECTURE.md` (menu-surface standard).

## HOLD
Mobile header shows the SENSELESS logo only; drawer + submenu expansions fully opaque; desktop unaffected.
