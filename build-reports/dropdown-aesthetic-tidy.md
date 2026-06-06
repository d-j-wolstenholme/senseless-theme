# Dropdown aesthetic tidy — Shop + The System (one consistent visual system)

**Date:** 2026-06-06 (BST) · **Branch:** dev · **Theme:** Senseless Dev `#199324434780` · **Commit:** `9fd8a37`. Token refreshed.

Pure CSS/layout pass on the **desktop** dropdowns in `sections/senseless-header.liquid`. **No link / structure / content / label / flyout changes**; **mobile drawer untouched**. Goal: Shop + The System read as one system.

## PART 1 — Shop mega
- **1a — Footer CTAs on one baseline:** nav columns made equal height (grid `align-items: stretch`; each `colgroup` is `flex-direction: column`), and each footer CTA block (`.ss-hdr__colfoot`: grey hairline + purple link) pinned to the bottom with `margin-top: auto`. The dividers **and** purple links now align across By Strength / By Procedure / Bundles regardless of item count. By Product (no footer) left as-is.
- **1b — Vertical dividers between nav columns:** `border-left: 1px solid var(--ss-border)` on By Strength / By Procedure / Bundles (not By Product). `var(--ss-border)` = `rgba(26,24,22,0.12)` — the **exact same token/colour as the existing horizontal dividers**. Column gutters rebuilt with per-column padding (`column-gap: 0` + `padding: 0 20px`, first column flush) so dividers sit centred. Featured card keeps its own border, 20px gap, **no doubled divider**.

## PART 2 — The System (Layout B)
- Equal-height columns (`sysgrid` + `sysgroups` → `align-items: stretch`).
- Vertical hairline dividers **between the 3 groups** (`border-left`, same grey). Group 1 (Understand by procedure) uses the **featured card's own border** as its boundary — no doubled divider. The "Comfort & pain" descriptor stays as-is.
- Eyebrow + item typography already share Shop's `.ss-hdr__col-title` / `.ss-hdr__sublink` tokens (12px eyebrow, 16px body links) — confirmed identical.

## PART 3 — Help
- Generic single list, already on the shared `.ss-hdr__sublink` token (16px / body colour `rgb(43,39,48)`). Confirmed matching — no change needed (simple list, no multi-column dividers required).

## Responsive
- At `≤1199px` (mega reflows to 2-col) the vertical dividers + per-column padding are reset so the tablet layout stays clean; footer pinning still works per row.

## Verify (desktop @1440, password render)
- **Shop:** 4 nav columns equal height (358px each); footer CTAs all align — divider top = 464, link top = 482 across all three ✓; vertical dividers = `1px rgba(26,24,22,0.12)` matching the horizontal colour exactly, By Product none ✓; featured card own 1px border, no shared divider ✓; flyout still opens → `/products/clinical-strength-cream` ✓.
- **The System:** 3 groups equal height (238px); group 1 no divider, group 2/3 matching dividers ✓; eyebrow 12px (same class as Shop) ✓.
- **Help:** sublink 16px / body colour — matches the other dropdowns ✓.
- **Mobile drawer:** unchanged — opens, group order intact (By product · By strength · By procedure · Bundles), nested subacc still expands ✓ (no drawer classes touched).
- **theme-check 0 errors** (52 warnings, standing baseline); **injectable-clean unaffected** (only the doc-comment names the rule).

## Files
- `sections/senseless-header.liquid` (CSS only: shopgrid/sysgrid/sysgroups equal-height + dividers + per-column padding, colfoot `margin-top: auto`, tablet resets). No markup/JS/schema changes.

## HOLD
Dropdown aesthetic tidy live + verified on the dev theme.
