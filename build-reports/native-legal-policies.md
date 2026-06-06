# Native legal policies — populate from bespoke (Privacy) + Refund 30-day amendment

**Date:** 2026-06-06 (BST) · **Branch:** dev · **Theme:** Senseless Dev `#199324434780` (UNPUBLISHED). All changes were **Admin API** (`shopPolicyUpdate`, write_legal_policies) — **no theme files changed**; theme-check **0 errors**. Privacy auto-management is now OFF (Daniel), so the native Privacy slot is writable.

## What was written (native Shopify policy slots — these are what checkout links)

| Native slot | Action | Source | State |
|---|---|---|---|
| **PRIVACY_POLICY** | **Rewritten** (was Shopify boilerplate + `d.j.wolstenholme@icloud.com`) | bespoke `/pages/privacy-policy` content, **verbatim** (rich-text → HTML + FAQ) | MHG data-controller named; contact `cs@senseless.uk`; **no boilerplate, no iCloud** |
| **REFUND_POLICY** | **Rewritten** to canon (replaces the earlier remediation body) | bespoke `/pages/returns-refunds`, verbatim | **30-day** window; returns address (Paddock Business Centre, Paddock Road, Skelmersdale, WN8 9PL); 10-working-day refund; customer pays return postage unless damaged/defective/incorrect; 14-day only in the EU-conditional FAQ line |
| **TERMS_OF_SERVICE** | Confirmed — already bespoke MHG (not boilerplate/iCloud) | — | unchanged, CLEAN |
| **SHIPPING_POLICY** | Confirmed — canon (set in the shipping brief) | — | unchanged, CLEAN |
| **CONTACT_INFORMATION** | Confirmed — MHG | — | unchanged, CLEAN |

### Privacy (the ask)
The native Privacy policy now holds the bespoke Senseless/MHG content verbatim — Introduction naming **Matrix Health Group Ltd** as controller with `cs@senseless.uk`, "What we collect", how it's used, sharing, retention, your UK-GDPR rights, plus the 5-question FAQ (data controller, no data sale, marketing opt-out, deletion within 30 days, ICO complaint). Well-formed HTML (8× h2, 12× p, 8 links). **The iCloud boilerplate is gone.**

### Refund 30-day amendment
The bespoke `/pages/returns-refunds` was **already canonical** (30-day, returns address, 10-working-day refund, EU-only 14-day FAQ). The native slot — which the earlier Phase-13 remediation had given a **standalone 14-day UK cooling-off paragraph** — was **rewritten from the bespoke page**, so:
- The 30-day window is the only UK return window.
- The **standalone 14-day UK cooling-off line is REMOVED.**
- 14-day now appears **only** in the EU-conditional FAQ line: *"UK only at present; if that changes, EU customers get the additional 14-day cooling-off period."* (verified — it's the sole 14-day reference).
- No `[SENSELESS CS EMAIL]` placeholder anywhere (bespoke + native both use `cs@senseless.uk`).

## Duplicate-content reconciliation
- **Footer legal links → `/pages/*`** (the canonical bespoke pages): `/pages/privacy-policy`, `/pages/terms-conditions`, `/pages/cookie-policy`.
- **All `/policies/*` → 301 → `/pages/*`** (privacy, refund, shipping, terms, contact) — so the native URLs don't serve a competing indexable copy on the storefront.
- **`/pages/*` policy pages are `noindex`** via the theme robots mechanism added in Phase 13 (canon: policy pages noindex).
- **Checkout** always links the native `/policies/*` — which is exactly why the native **bodies** now hold the real MHG content (checkout renders the native policy regardless of the storefront redirect).
- **Net:** no duplicate-content issue — the non-canonical `/policies/` URLs 301 to the canonical `/pages/`, and the `/pages/` are noindex anyway.

## Verification
- Native policy sweep: **0 iCloud, 0 Shopify boilerplate, 0 placeholders/raw-liquid**; `cs@senseless.uk` present in privacy/refund/terms/contact.
- Bespoke policy pages sweep (all 5): clean, no `[SENSELESS CS EMAIL]`/iCloud/`{{ }}`.
- Refund: `30 days` present; the only `14-day` string is the EU FAQ line.
- theme-check 0 errors; git clean (no theme files changed).

## Note for Daniel
- The returns address used (Paddock Business Centre, Paddock Road, Skelmersdale, WN8 9PL) was taken **from the bespoke `/pages/returns-refunds`** (already present there) — assumed to be the confirmed address. If a different returns address was intended in your "confirmation below", say the word and I'll update both the native slot + the bespoke page.

## HOLD
Native Privacy + Refund populated from the bespoke pages; all native slots confirmed canonical MHG content; no boilerplate/iCloud remains. theme unpublished.
