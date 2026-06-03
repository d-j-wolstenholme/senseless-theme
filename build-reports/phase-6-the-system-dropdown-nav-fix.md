# Phase 6 — "The System" dropdown nav fix (+ stale-path redirects)

**Date:** 2026-06-03 (BST) · **Branch:** dev · **Theme:** Senseless Dev `#199324434780` (store `senseless-numbing`)
Token refreshed (`./scripts/refresh-token.sh` → shpca_388e98…). Build source: spec `37358bc375ea81df995afcf813dd03bb` — "NAV FIX — The System dropdown is STALE" (+ the already-built RESTRUCTURE / AFTERCARE items, re-confirmed below).

## Context — items 1, 2, 4 already shipped earlier this session
The comfort-section fix, global inline standard, `/pages/does-it-hurt` hub, and the aftercare sections were built + verified in commits `ef346f4` and `6bd3d70`. Re-confirmed live this pass (see Verify). The **new** work here is item 3: the full "The System" dropdown.

## 3. "The System" dropdown rebuilt (menuUpdate on `senseless-main`)
The dropdown was stale — its four guide children pointed at pages with **no resource** (all 404): `/pages/how-it-works`, `/pages/choosing-your-format`, `/pages/how-to-apply`, and `/pages/choosing-your-strength` (the latter already 301'd). Rebuilt "The System" to **exactly**:
- **The Senseless System** → `/pages/the-senseless-system` (replaces Choosing your strength + Choosing your format + How Senseless works)
- **Does it hurt?** → `/pages/does-it-hurt` (single, no nested children)
- Parent "The System" itself → `/pages/the-senseless-system` (was the dead `/pages/how-it-works`).
- Removed: Choosing your strength, Choosing your format, How Senseless works, How to apply, and the 2 nested awareness children. "Using numbing cream" omitted (not built yet).

## Stale-path redirects (301 → /pages/the-senseless-system)
The dead system paths are still linked from ~70 places sitewide (homepage, collections, products, other guide pages — that repoint is Phase 12). To stop them 404-ing, created 301s:
- `/pages/how-it-works` → `/pages/the-senseless-system` (the spec's named retire target)
- `/pages/choosing-your-format` → `/pages/the-senseless-system`
- `/pages/how-to-apply` → `/pages/the-senseless-system`
- (`/pages/choosing-your-strength` → `/pages/the-senseless-system` already existed.)
No `how-it-works` page **resource** exists, so there was nothing to unpublish (the brief's unpublish step was conditional on the resource existing).

## Verify
- **Every "The System" menu link resolves 200, direct (no redirect):** the-senseless-system ✓, does-it-hurt ✓.
- **Rendered header nav:** shows The Senseless System + Does it hurt?; stale how-it-works / choosing-your-format / how-to-apply **absent**. Shop/About/Help structurally untouched.
- **Items 1/2/4 re-confirmed live:** hub schema = WebPage + BreadcrumbList (no FAQPage); comfort `position:static` on the hub + both awareness pages (bug stays fixed); aftercare "What to expect afterwards" present on both; awareness H1s unchanged.
- **theme-check: 0 errors.** (No theme files changed this pass — menu + redirects are Admin-API state.)

## ⚠ Flagged — pre-existing broken links in the *untouched* branches (NOT fixed; brief said leave Shop/About/Help untouched)
A full menu HTTP sweep found these **pre-existing 404/301s outside my scope**, caused by page **resources never being created** (templates exist, resources don't):
- **About** → `/pages/about` — **404** (no page resource).
- **Help → FAQ** (and the Help parent) → `/pages/faq` — **404**.
- **Help → How long to work** → `/pages/how-long-numbing-cream-takes-to-work` — **404**.
- **Help → How long to last** → `/pages/how-long-numbing-cream-lasts` — **404**.
- **Help → Does numbing cream actually work** → `/pages/does-numbing-cream-work` — **404**.
- **Shop → By strength** → `/pages/choosing-your-strength` — **301** (resolves via redirect, not a direct 200).

These need their page resources created (same `pageCreate` pattern used for the awareness pages) or the links repointed — a separate task. **Left untouched per the brief's "Shop/About/Help untouched" instruction; flagging rather than silently shipping 404s.** Want me to create the missing supporting-page resources (About, FAQ, How-long-to-work, How-long-to-last, Does-numbing-cream-work) in a follow-up?

## Files / API
- API only: `menuUpdate` (senseless-main, "The System" branch), `urlRedirectCreate` ×3. No theme-file changes.
- Report file committed.

## HOLD
"The System" dropdown fixed + verified; stale system paths redirected. Pre-existing About/Help 404s flagged for a decision. (A separate dropdown-panel-background fix brief has just arrived — addressed next.)
