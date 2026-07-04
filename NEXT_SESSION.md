# Next session — Senseless (Canon v2.19)

Read `CLAUDE.md` → run `scripts/reconcile.sh` → read the Project Instance + State Surface first.

## Done last session (2026-07-03 → 04, MacBook Pro)
Long multi-task session. Commits (newest first): `68e8926`, `801786b`, `0f138b0`, `d5f3e67`, `ee9959c`.

**1. Canon re-stamp v2.17 → v2.19** (`ee9959c`) — repo stamps matched to Notion; label-only.

**2. Registered address → Skelmersdale, then corrected to full form** (`d5f3e67` + `801786b`) — Companies House registered office moved. Final canonical address, live everywhere: **`Paddock Business Centre, 2 Paddock Road, Skelmersdale, WN8 9PL`** (the first pass omitted the `2`; corrected). Updated + live-verified across: footer · Contact page · llms.txt · Organization JSON-LD ×2 (schema/rich-results validated) · `scripts/policy-metafields.py` (Terms + FAQ + Returns) · live Shopify metafields (terms + returns pages) · native TERMS_OF_SERVICE / CONTACT_INFORMATION / REFUND_POLICY shop policies · Notion (Project Instance §1, Confirmed Facts, Terms master). Full Shopify sweep = 0 stale hits.

**3. Rewards/loyalty page** (`68e8926`) — new `/pages/rewards` live (Work Item `39258bc3-75ea-8130` → **Built**; Decision `-814c`). Hero + how-it-works + rates table + app-vs-web comparison + FAQ + terms + sign-in CTA; **no live balance** (link-out to hosted account page). Rates per Senseless App ADR-009 (1pt/£1, 2× app, 200pt app welcome, 100pt=£1, no expiry, guest doesn't earn). New `senseless-rewards` section (block-driven). New top-level **Rewards** nav in `senseless-main`. **compliance-check PASS.**

**4. Header + guide button** (`68e8926`) — `how-to-apply` added as the **lead** item in the header Application-guides group (desktop + mobile); `senseless-rich-text` gained a filled-button CTA variant (`cta_style`) and the using-numbing-cream "full routine" link is now a standout button.

**5. Store business address (Settings → General)** — saved via admin UI: company → `Matrix Health Group Ltd`, address → `Paddock Business Centre, 2 Paddock Road`, Skelmersdale WN8 9PL. API-verified.

## Open follow-ups / flags
- **Store province = "England" (should be Lancashire) — UNFIXABLE via admin UI or API.** Neither the Store-address form nor the Business-details entity form exposes a county field (UK addresses don't), and there's no shop-address Admin-API mutation. The value is **never rendered** (no county line in the address display) → invisible, harmless. Only Shopify Support can amend the underlying record. Left as-is.
- **Business-details legal entity** address is split differently (`2 Paddock Road` + `Paddock Business Centre` as apartment) vs the Store address. Left alone — editing the legal/tax entity can trigger Shopify business-verification.
- **Cross-brand carriers still on the OLD London address** (same legal entity, separate stores/sites → own gated pass, don't edit from a Senseless session): **Totally Numb** (store + /about + /terms) and **MHG Holding Site** (Content Plan, Director's Brief, README; MHG Confirmed Facts "Legal entity").
- **Rewards fast-follow (deferred, needs its own decision):** live-balance teaser on `/pages/rewards` — would call GET /summary but needs an auth-bridge (the storefront lacks the hosted-account auth context). Not built.
- Header mis-links (pre-existing): the "How long it takes to work" / "How long it lasts" items in the Application-guides menu still point to `/pages/using-numbing-cream` rather than the dedicated `how-long-*` pages. Not in scope this session.

## Backlog (unchanged)
- ntn write-back wiring · Phase 12 nav/link wiring · Phase 10 photography · optional GPay-at-checkout payment-customization function (Daniel undecided). Launch-gate: **CLEAR**.

## Gotchas
- `.env` Admin token expires (401s) — run `./scripts/refresh-token.sh` (non-interactive client-credentials) before any Admin-API script; the MCP Shopify connector works independently.
- Policies live in **two places**: native shop policies (`/policies/*`, checkout) AND page metafields (`/pages/*`, `policy` namespace). Change both.
- Reviews-guard: editing `senseless-structured-data.liquid` needs `deploy.sh --reviews-changed` (rewrites `reviews-guard.lock` — commit it).
- Canonical registered address string: **`Paddock Business Centre, 2 Paddock Road, Skelmersdale, WN8 9PL`** (footer variant drops the comma before the postcode). Store gate: MCP/CLI default is Totally Numb — verify `senseless-numbing.myshopify.com` first. No rollback theme.
