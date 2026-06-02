# Phase 6a follow-up — Selector link-ins (hub page + boundary confirmations)

**Date:** 2026-06-02 (BST) · **Branch:** dev · **Theme:** Senseless Dev `#199324434780` (store `senseless-numbing`)
Token refreshed (`./scripts/refresh-token.sh` → shpca_a1a581…); shop = senseless-numbing.

## 1. Added — Selector link-in on the aesthetic-procedures hub
The page resource **exists** (`Aesthetic Procedures`, `gid://shopify/Page/710999867740`) — the earlier audit flag ("template with no backing resource") was the reverse: a live resource with **no custom template**, rendering via the default `page.json` (`templateSuffix: null`). Not blocked, so the link-in was added:

- Created **`templates/page.aesthetic-procedures.json`** — replicates the default `main` (`main-page`) section verbatim so the existing page body is preserved unchanged (intro + "By procedure" 4 storefront links + "By format" 3 links — already injectable-clean), and appends a `selectorlink` `senseless-callout-band` (neutral) → `/pages/the-senseless-system#selector`. Order: `main → selectorlink`.
- Pushed the template, then set the page **`templateSuffix` → `aesthetic-procedures`** via `pageUpdate` (no userErrors). Follows the established per-page-suffix pattern (`the-senseless-system`, `contact`).

## 2. Confirmed — injectable collections stay link-clean
The 3 injectable collection templates — `collection.numbing-cream-for-botox`, `-for-injections`, `-for-lip-fillers` — carry **zero** Selector references (Asset-API grep = 0 each; rendered-page Playwright count = 0 each). No Selector link-in added, per Canonical §2 #5 + Google Ads non-medical policy.

## 3 & 4. Deferred (no action this session)
- Pain pages (Phase 6) + FAQ (Phase 7) get the Selector link-in **built in when those pages are built** — not now.
- `?strength=` grid filter **not** touched — logged for Phase 12 (build the grid filter once, sitewide).

## Verify
- **theme-check: 0 errors** (24 pre-existing Horizon snippet warnings only; none on the new template).
- **Asset-API diff:** hub template landed; `order: [main, selectorlink]`; `selectorlink` settings intact (no pruning). Injectable collections = 0 selector references.
- **Render-verify (Playwright, live preview):** hub page renders with body preserved (by-procedure + by-format links present); link-in band present (heading "Not sure which to choose?", `href=/pages/the-senseless-system#selector`); clicking it lands on the live Selector (`#selector` present). All 3 injectable collections render with 0 Selector links.

## Compliance
Hub link-in uses the same recommendation framing as the collection link-ins ("we'd reach for"); no efficacy/duration/onset/% claims; injectable surfaces kept link-clean.

## Files / API
- New: `templates/page.aesthetic-procedures.json`.
- API: `pageUpdate` set templateSuffix on the aesthetic-procedures page.

## Note
`templateSuffix` is a page-resource property (global across themes), not theme-scoped. The dev theme now has `page.aesthetic-procedures.json`; at launch the published theme must also carry this template (it will, being the same repo). Consistent with the existing `the-senseless-system` / `contact` suffixes.

## HOLD
Follow-up complete and verified live. Nothing else started.
