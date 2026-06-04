# Policy pages — metafield-driven rebuild (TN/Strand 5) + redirects + shipping reconciliation + footer

**Date:** 2026-06-04 (BST) · **Branch:** dev · **Theme:** Senseless Dev `#199324434780` (store `senseless-numbing`) · **Commit:** `d31ee57`
Token refreshed. Reference: Strand 5 (`36d58bc375ea81c1b4c0cb8c7ee3fdd9`).

## STEP 0 — Audit (findings before building)
- **What Daniel saw:** the native **`/policies/shipping-policy`** renders **plain prose** (Shopify's native policy template — 0 `ss-` sections, no hero/FAQ). The custom **`/pages/shipping-delivery`** already rendered the designed layout. Confirmed in-browser: `/pages/shipping-delivery` = 15 `ss-` sections + hero + FAQ; `/policies/shipping-policy` = 0 sections, h1 "Shipping policy".
- **Metafield architecture: ABSENT.** No `policy` PAGE-metafield namespace, **0** PAGE metafield definitions, no `prose_policy_body`. Phase 9 Track 1 built the 5 pages on **per-page templates with inline `senseless-rich-text` sections** (hardcoded content) — i.e. dropped-in sections, not the TN metafield-driven model.
- **Template suffixes:** all 5 pages had their own suffix (shipping-delivery, returns-refunds, …) → so the custom pages did render the designed layout; they just weren't metafield-driven.
- **Redirects:** none (`/policies/*` → `/pages/*` did not exist).
- **Native policies:** REFUND/PRIVACY/SHIPPING/TERMS/CONTACT all populated (Track 1) — left as-is. PRIVACY still on Shopify auto-management (not retried).
- **Footer:** menu-driven. Legal band **looped `shop.policies`** → linked the native `/policies/*` plain pages (a second route to what Daniel saw). "THE SYSTEM" column (`senseless-footer-explore`) held 4 retired 301 paths (choosing-your-strength/format, how-it-works, how-to-apply). Nav `senseless-main` "By strength" → retired `/pages/choosing-your-strength`.

## Build — target architecture reached
1. **Custom metafield-driven template.** New `sections/senseless-policy-page.liquid` + `templates/page.policy.json` (one shared template). Reads PAGE metafields (`policy` namespace): `prose_policy_body` (rich_text_field), `faq` (json → accordion), `see_also` (json → links), `last_updated` (date). Renders designed layout: hero (title + Last-updated) → prose → FAQ accordion → see-also → WebPage JSON-LD. **Rich text rendered via `| metafield_tag`** (the plain `{{ metafield }}` drop leaked raw JSON — caught and fixed in verify).
2. **Definitions + values** via `scripts/policy-metafields.py`: created the 4 PAGE definitions; ported the vetted Track 1 copy into the metafield values through an HTML→rich-text-JSON converter (headings/paragraphs/lists/links/bold). All 5 pages switched to `templateSuffix: policy`. Old per-page templates deleted.
3. **Native policies** left as-is (Strand 5 dual-layer: native = compliant checkout policy; custom `/pages/*` = designed on-site page).
4. **Redirects** `/policies/* → /pages/*` created (shipping/refund/privacy/terms/contact) via `scripts/policy-menus-redirects.py`.

## Shipping-copy reconciliation
Shipping page now **states the free-shipping tiers** (free standard over £40, free next-day over £80) + same-day-before-1pm dispatch; **paid tiers kept** (Standard £1.99 / Express £2.99 / Next day £7.99, now marked free over the thresholds); the stale **"all orders carry a delivery charge" line removed**; the **"Free shipping?" FAQ corrected** → "Is delivery free?" describing the £40/£80 tiers. **Returns checked** — only *return-postage* references (customer pays unless faulty); no free-shipping conflict, left as-is.

## Footer / nav
- Legal-band policy links repointed from `shop.policies` (native `/policies/*`) → explicit designed `/pages/*` (shipping-delivery, returns-refunds, privacy-policy, terms-conditions, cookie-policy).
- THE SYSTEM column rebuilt to live pages (System, Find your strength `#selector`, Using numbing cream, Does it hurt?, FAQ) — retired paths gone.
- Nav "By strength" → `/pages/the-senseless-system#selector`.

## Verify
- **theme-check: 0 errors** (399 files, down from 404 — 5 templates removed).
- **Asset-API diff:** policy section/template, footer, theme.liquid all MATCH remote; the 5 old per-page templates confirmed GONE.
- **Render (Playwright):** all 5 pages render `.ss-pol` designed layout with prose `<h2>`s (5/4/7/8/4), paragraphs, FAQ (5/6/5/4/3), no JSON leak. Shipping: free £40 ✓, free £80 ✓, before-1pm ✓, stale line absent ✓, paid tiers present ✓. Footer policy links = 5× `/pages/*` ✓; no stale system paths ✓; no native `/policies/` links in footer ✓.
- **Grep:** zero "all orders carry a delivery charge" in repo.

## Flags / decisions
- **⚠ Redirect is a DORMANT safety net (matches TN).** `/policies/shipping-policy` still returns **200 (native plain page)** because Shopify serves active native policies and URL redirects only fire on 404. So the redirect does **not** currently send `/policies/* → /pages/*`. This is by design (Strand 5 dual-layer: native policy is required for the **checkout** footer). The user-facing fix is that the **storefront footer/nav now point at the designed `/pages/*`**; the only remaining place the plain page appears is Shopify's checkout footer (unavoidable, and correct). To make `/policies/shipping-policy` itself show the designed page you would have to **delete the native policy** — not recommended (loses the compliant checkout policy). Decision needed from Daniel if he wants that trade-off.
- **⚠ Free-shipping rules still need Admin confirmation** (token lacks read_discounts/read_shipping) — the shipping page now *states* £40/£80; confirm the actual Shopify discount rules exist so copy matches checkout.
- **Metafield schema:** used a focused 4-key `policy` set (not TN's 79 defs) — covers the designed layout (prose + faq + see_also + last_updated). Extendable if more structured fields are wanted.
- PRIVACY native policy still blocked on Shopify auto-management toggle (Daniel) — not retried.

## Files
- New: `sections/senseless-policy-page.liquid`, `templates/page.policy.json`, `scripts/policy-metafields.py`, `scripts/policy-menus-redirects.py`.
- Edited: `sections/senseless-footer.liquid`. Deleted: 5 `templates/page.*` policy templates.
- API: 4 metafield definitions, 20 metafield values, 5 page templateSuffix updates, 2 menu updates, 5 redirects.

## HOLD
Policy pages are metafield-driven and render the designed layout at `/pages/*`; footer/nav cleaned; shipping copy reconciled. Awaiting Daniel on the redirect/native-policy trade-off + free-shipping rule confirmation.
