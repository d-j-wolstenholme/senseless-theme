# Cookie consent banner — global component (Canonical State §6)

**Date:** 2026-06-01 (BST) · **Machine:** MacBook Pro · **Branch:** dev
**Theme:** Senseless Dev `#199324434780` (unpublished) · **Checkpoint:** discrete task before Wave 3 — STOP after.

## Source read
- 🟢 Canonical State §6 — https://www.notion.so/37258bc375ea813e895ccbe38c0cadc8

## What was built
- **New snippet `snippets/senseless-cookie-consent.liquid`** rendered globally from `layout/theme.liquid` (before `</body>`) → on every page.
- **Footer "Cookie settings"** control added to the `senseless-footer` legal band (`data-ss-cookie-settings`) — re-opens the preferences panel.
- Brand-styled: purple `#6B3FA0` / cream `#f7f7f5` / ink `#2B2730`, Montserrat; **bottom banner** (not a full-screen wall); responsive (actions become a 2-col grid on mobile). theme-check **0 errors**.

## Render check — home + product + collection (storefront password)
Verified identical on `/`, `/products/clinical-strength-cream`, `/collections/numbing-cream`:

| Requirement | Result |
|---|---|
| (e) Renders on home / product / collection | ✅ banner markup present on all three |
| (d) Equal-prominence actions | ✅ **Accept all** and **Reject non-essential** are both `ss-cc__btn--primary` (same size + visual weight, side by side); "Manage preferences" is a tertiary text control |
| Manage Preferences panel | ✅ category toggles — **Necessary** (checked + **disabled**), **Analytics**, **Marketing** + "Save preferences" |
| (a) Consent gating wired | ✅ Shopify **Customer Privacy API**: `Shopify.loadFeatures([{name:'consent-tracking-api',version:'0.1'}], …)` then `customerPrivacy.setTrackingConsent({analytics, marketing, preferences, sale_of_data})` on Accept/Reject/Save |
| (a) Deny-by-default | ✅ on first load with no saved choice, init calls `setTrackingConsent({analytics:false, marketing:false, preferences:false})` → non-essential **denied** until the visitor chooses |
| (b) Persistence + no re-show | ✅ choice stored in `localStorage['ss_cookie_consent_v1']`; banner shows **only** when no saved choice; returning visitors re-apply the saved state to the API and the banner stays hidden |
| (c) Footer re-open | ✅ `[data-ss-cookie-settings]` → `show()` + `openPanel()` |
| (f) theme-check | ✅ 0 errors |
| Policy link | ⚠ interim `/policies/privacy-policy` — **flagged for repoint** when the Stage F Cookie/Privacy page lands |

### Accessibility
- Banner `role="region"` aria-label; panel `role="dialog" aria-modal="true"` aria-label; `aria-haspopup`/`aria-controls` on the Manage trigger; per-toggle `aria-label`.
- Keyboard operable (real `<button>`/`<input>`); **focus moves into the panel** on open and returns to the trigger on close; **ESC closes** the panel; **Tab is contained** within the open panel; **visible focus** via `:focus-visible` (purple outline).

## Honest note on runtime verification
The render checks above are deterministic (markup + JS wiring confirmed on all three page types via the rendered HTML). The **runtime behaviour** — the live `setTrackingConsent` state actually flipping on click, and persistence surviving navigation — is **wired per the Customer Privacy API and verified by code path, but not click-tested in a live browser** (the curl render harness can't execute JS). A quick browser smoke-test (click Accept → `Shopify.customerPrivacy.currentVisitorConsent()` shows analytics/marketing granted; reload → banner stays hidden) is recommended to confirm end-to-end. Actual pixel/marketing enforcement also depends on the shop's Customer Privacy/consent configuration in admin (region / "require consent"), which is an admin setting — the theme wiring is correct.

## Flags
- **Policy link** `/policies/privacy-policy` is interim → repoint to the Stage F Cookie/Privacy page when built.
- Consider an admin-side check that **Customer Privacy / consent collection** is enabled for the target regions so the API genuinely blocks pre-consent (launch-gate).

## Not done (by design)
- Wave 3 (collections) not started — this was the discrete pre-Wave-3 component.

---
## Live browser smoke-test (Playwright headless Chromium) — results

Ran a real click-through against the preview theme (storefront password). The custom banner's UI/UX is fully working; the test also caught two **store-side** issues the static render couldn't.

**✅ Working (verified live):**
- Custom banner shows on first visit; **equal-prominence** Accept/Reject; Manage panel with toggles.
- Choice **persists** — `localStorage['ss_cookie_consent_v1']` = `{"analytics":true,"marketing":true,"preferences":true}` after Accept; banner hides after choice and **stays hidden on reload**.
- Footer **"Cookie settings" re-opens** the preferences panel (`reopen_panel: true`).
- **Gating is genuinely active:** before any choice, `Shopify.customerPrivacy.userCanBeTracked() === false`, `currentVisitorConsent()` empty, and `shouldShowBanner() === true` — i.e. non-essential is denied until consent.

**⚠️ Found (store-side — NOT the banner's code):**
1. **`setTrackingConsent` fails** with `Error while setting storefront API consent: Cannot read properties of undefined (reading 'consentManagement')`. So clicking Accept/Reject does **not** flip `currentVisitorConsent()` yet — Shopify's **Customer Privacy / consent management isn't fully provisioned on this dev store**. The banner code is correct (documented API, errors caught); the write will succeed once consent management is set up in admin. (Shopify's own native banner hits the same backend.)
2. **Shopify's native cookie banner is also enabled** (`#shopify-pc__banner` renders) → **two banners** show at once, and the native one overlays/intercepts clicks.

**→ Admin actions for Daniel (launch-gate, account settings — not Claude-changeable):**
- **Settings → Customer privacy:** finish setting up **consent management / the Customer Privacy API** (resolves the `consentManagement` error so `setTrackingConsent` records consent), and **turn OFF Shopify's built-in cookie banner** so the brand-styled custom banner is the sole UI (both use the same consent API). Re-run this smoke-test after.

**Net:** the custom banner is built correctly and its UX is verified live; making it *genuinely gate* end-to-end is blocked on the two admin settings above, now flagged.
