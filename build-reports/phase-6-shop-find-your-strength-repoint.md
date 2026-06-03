# Phase 6 — Shop mega "Find your strength" link repoint

**Date:** 2026-06-03 (BST) · **Branch:** dev · **Theme:** Senseless Dev `#199324434780` (store `senseless-numbing`)
Token refreshed (`./scripts/refresh-token.sh`).

## Change
The Shop mega-menu's "By strength" group footer link **"Find your strength →"** pointed at `/pages/choosing-your-strength` (retired — now a 301). It's not a menu item — it's the header section's **`mega_cta_url` setting** (stored in `sections/header-group.json`), so the fix is a section-setting edit (not `menuUpdate`):
- `header-group.json` → `mega_cta_url`: `/pages/choosing-your-strength` → **`/pages/the-senseless-system`**.
- Updated the matching schema `info` hint in `senseless-header.liquid` (was "Set to /pages/choosing-your-strength") so it no longer points at the retired page.
- The 3 strength items (Clinical / Advanced / Professional → `…?strength=…`) left **as-is** — the grid filter is Phase 12; they land on the right collection unfiltered.

## Verify
- **theme-check: 0 errors.**
- **Render-verify (Playwright, live preview):** Shop mega "Find your strength" href = `/pages/the-senseless-system`; target resolves **200 direct** (final path `/pages/the-senseless-system`, no 301 hop). The 3 strength items unchanged and present. Rest of Shop branch + other branches untouched (menu not modified).

## Files
- Edited: `sections/header-group.json` (mega_cta_url), `sections/senseless-header.liquid` (schema info hint).

## HOLD
Shop "Find your strength" now links direct to the live System guide.
