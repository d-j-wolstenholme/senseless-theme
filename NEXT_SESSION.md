# Next session — Senseless (Canon v2.19)

Read `CLAUDE.md` → run `scripts/reconcile.sh` → read the Project Instance + State Surface first.

## Done last session (2026-07-03, MacBook Pro)
Two tasks landed:

**1. Canon re-stamp v2.17 → v2.19** (commit `ee9959c`) — repo stamps bumped to match Notion; label-only, no theme change.

**2. Registered address → Skelmersdale** (commit `d5f3e67`, deployed live) — Companies House registered office moved `128 City Road, London EC1V 2NX` → `Paddock Business Centre, Paddock Road, Skelmersdale, WN8 9PL`. Updated **every brand-authored Senseless location**:
- **Theme (deployed #199324434780):** footer legal bar · Contact page company details · llms.txt company line · **Organization JSON-LD ×2** (org-schema section + structured-data snippet) — schema/rich-results PostalAddress validated live on homepage + Contact.
- **Live via Admin API:** terms-conditions page metafields (`prose_policy_body` + `faq`, `last_updated`→2026-07-03) · native **TERMS_OF_SERVICE** + **CONTACT_INFORMATION** shop policies.
- **Generator:** `scripts/policy-metafields.py` Terms body + FAQ.
- **Notion source-of-truth:** Project Instance §1 · Confirmed Facts "Parent company" · Terms & Conditions master page.
- **Verified:** full-surface Shopify sweep (pages/policies/metaobjects/shop-mf/articles/16 products/collections) = **0 remaining hits**; live curls show new address, 0 old; reviews-guard 5/5 markers intact (`reviews-guard.lock` checksum bumped for structured-data snippet).

## Open follow-ups (flagged, NOT done — need decision / separate pass)
- **Cross-brand carriers still show the OLD address** (same legal entity, but separate stores/sites — need their own store-gated pass, do NOT edit from a Senseless session):
  - **Totally Numb** — /pages/about §5, /pages/terms-conditions §2+§10 (Notion Content DB + the TN store `matrix-group-totally-numb`).
  - **MHG Holding Site** (matrixhealthgroup.co.uk) — Website Content Plan, Director's Brief, README; MHG Confirmed Facts "Legal entity".
- **Store billing/registered-address setting** = `2 Paddock Road, Skelmersdale, WN8 9PL` (line-1 differs from the `Paddock Business Centre, Paddock Road` wording used on pages). Decide the canonical Companies House format and reconcile the two. Not editable via the pages pass — Settings → General.
- **Notion Contact brief** (`36c58bc3-75ea-8160-…`) still has `Registered address: ⚠ TBC` placeholders — now resolvable to the Skelmersdale address (left as-is: it's a planning brief; live page already correct).
- Historical `build-reports/*` + `DECISIONS-LOG.md` retain the old address by design (history — do not rewrite).

## Backlog (unchanged)
- ntn write-back wiring · Phase 12 nav/link wiring · Phase 10 photography · optional GPay-at-checkout payment-customization function (Daniel undecided). Launch-gate: **CLEAR**.

## Gotchas
- `.env` Admin token expires (401s) — run `./scripts/refresh-token.sh` (non-interactive client-credentials) before any Admin-API script; the MCP Shopify connector works independently.
- Policies live in **two places**: native shop policies (`/policies/*`, checkout) AND page metafields (`/pages/*`, `policy` namespace). Change both.
- Safety-warnings copy is HARDCODED in the section (compliance-locked). No rollback theme. Store gate: MCP/CLI default is Totally Numb — verify `senseless-numbing.myshopify.com` first.
