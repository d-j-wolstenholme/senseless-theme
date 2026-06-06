# PHASE 13 — Remediation + completed admin audit

**Date:** 2026-06-06 (BST) · **Branch:** dev · **Theme:** Senseless Dev `#199324434780` (UNPUBLISHED — kept unpublished). Token refreshed with **expanded scopes**. **Image work excluded** (handled separately — the 7 placeholder product images + bundle featured images were NOT touched). theme-check **0 errors** throughout. Worklist = the Phase 13 audit (`37758bc375ea81799baec620017abd4e`).

**Effective token scopes now:** read/write for `content, products, themes, files, inventory, shipping, discounts, markets, script_tags, legal_policies, online_store_pages, online_store_navigation, metaobjects, publications, metaobject_definitions` + `read_locations`. **Not granted:** `read/write_orders`, customer/checkout scopes → those stay ADMIN-UI.

**Commits:** `4284390` (compliance), `a6ad9b4` (P0/P1/P2 batch 2), `886488f` (showPopover guard), `69c4f8c` (footer landmark). API/store-side writes (metafields, SEO meta, policies) are not in git.

---

## PART 1 — COMPLETED ADMIN AUDIT (now-readable APIs)

- **P0 [API now] Shipping — three-way mismatch.** Actual UK delivery profile: **Standard £4.99 (free over £50)**, **Express £6.99**, **NO next-day method**. Plus **EU £14.99 + International £23.99** zones exist. This contradicts (a) the cart banner copy "Free standard over £40 · Free next-day over £80", and (b) the Shipping policy ("Standard £1.99 / Express £2.99 / Next-day £7.99", "UK only"). **All three disagree.** → *Business/fulfilment decision: Daniel confirms the canonical rules; I did NOT guess thresholds or change live rates. Once confirmed I'll align the cart banner + Shipping policy copy to match.*
- **P2 [API] Markets vs shipping zones:** single market = United Kingdom (GBP, primary) — correct per canon — but EU + International **shipping zones are configured**, contradicting "UK only at present". Daniel: remove the EU/Intl zones or update the policy.
- **P3 [API] Locations:** one active location "Shop location" (fulfils online) with an **incomplete address** (city/zip null). Set the location address.
- **P3 [API] Discounts:** none configured (expected). **Script tags / web pixel:** none present (analytics via a web pixel app would not appear here — confirm in admin). **Tax:** `taxesIncluded=true` (VAT-inclusive, correct for UK); `taxShipping=false`.
- **Still ADMIN-UI (cannot read/write via API):** payment methods, checkout branding, email-notification templates, customer-account flow config, native cookie/consent banner toggle, "hide collection from search" flag, shop name. Listed in the checklist below.

---

## PART 2 — FIXES APPLIED (by domain)

### P0 / critical
- **using-numbing-cream — compliance gaps closed.** Added the **patch-test (24h)** beat, the **occlusion/cover (cling film)** step, and the **apply-before window** (cream ~45–60 min, with the "this varies — follow product/practitioner guidance" caveat; gel/spray "allow time to take effect") to both the "How to use it" steps and "The essentials". *Verified live.*
- **Cart drawer — partially fixed (see remaining).** Enabled `settings.auto_open_cart_drawer` (was off → root cause of no-open-on-add) and guarded `anchored-popover.js` `showPopover()` with an `isConnected` check. *Verified: the item now adds and the cart bubble updates, and the `auto-open` attribute renders — but the drawer still does not open on add (deeper Horizon cart-section-render race). Flagged below.*
- **Shop All — H1 added** (new `senseless-collection-hero` with H1 "Numbing cream, gel and spray — the full Senseless range") + **meta title/description set via API**. *The noindex ("hide from search") flag is NOT writable via the API → ADMIN-UI for Daniel.*
- **Compliance — banned tier-card copy replaced with Scale framing at source.** "everyday / considered upgrade / higher–most concentrated" → "standard / higher-strength / highest-strength" on the **live** aesthetic-numbing-cream collection, both SEO landers (senseless-vs-ametop, best-emla-alternative-uk), the `product.json` fallback, the semi-permanent-makeup collection FAQ, and the `complete-prep`/`strength-matrix`/`format-row` section **defaults**. Removed "used in clinics / available without restriction / trusted at the chair". Removed **"lip fillers, Botox"** use-case text from the two landers' tier cards. Gave each lander a **unique H1**. **"flagship"** removed from the Trade body. *Verified: `banned=false` on both landers.* The retired templates (choosing-your-strength/-format, how-it-works, how-to-apply, how-long-*, does-numbing-cream-work, strongest-numbing-cream) are confirmed **301'd/unpublished — their banned copy does not render** (orphan dead code; recommend pruning).

### Content
- **Bundle template** (`product.bundle.json`): "kit" → "bundle", "Small and Large" → "Starter and Ultimate", and the **vanity bag** added to the contents copy + FAQ.
- **Contact:** removed every visitor-facing "(placeholder — confirm before launch)" parenthetical and the visible "VAT number: to be confirmed before launch" line (VAT slot left for Daniel to supply the value).
- **numbing-spray FAQ:** reframed "before injections" → "before body treatments" (correct format positioning; spray = large/body areas, injectables → cream/gel).
- **£TBC trio-card prices** on the aesthetic collection + product.json fallback → linked to live products (price + quick-add now render).

### Catalogue (Admin API)
- **`senseless.tier` + `senseless.format` populated on all 10 single SKUs** (were null — only bundles had them). The Scale/format system now binds to the core range.
- **`recommended_procedures` filled on clinical gel (Microneedling/SPMU/Lip Fillers) + clinical spray (Laser/Waxing)** — they now enter the correct procedure collections (were in zero).

### SEO (API + theme)
- **Meta title + description added** to the 5 bundles, the System page, aesthetic-procedures, articles, and trade; **over-length titles shortened** (waxing 63→36, trade 69→39); **Shop All meta** set. Bundle meta descriptions replaced the 320-char body leak.
- **Duplicate H1 fixed** — the two landers now have distinct, query-matched H1s.
- **Theme-side robots noindex** built in `layout/theme.liquid` for Contact + the 5 policy pages (+ llms-txt), independent of admin SEO flags.

### GEO
- **Structured Key Facts `<dl>`** added to the System page (the GEO/citation hub). **Key Facts + answer-first FAQ (FAQPage schema)** added to the does-it-hurt hub. *Verified: both render; FAQPage emits.*

### Accessibility
- **`role="table"` dropped** from the PDP `ss-sb__grid` Scale module (it had no row/cell children — critical `aria-required-children` resolved; it's now a plain styled grid of links).
- **Footer landmark fixed** — the inner `<footer role=contentinfo>` → `<div>` and the section `tag: footer` → `div`, leaving `theme.liquid`'s `<footer>` as the **single** contentinfo. *Verified: one `<footer>`, no duplicate.*
- **Mobile drawer `inert`** when closed (toggled in JS) — keyboard users no longer tab into the hidden drawer (`aria-hidden-focus` resolved).
- **Skip-link** already present (`skip-to-content-link` + `#MainContent`) — confirmed, no change needed.
- **showPopover pageerror** — guarded at the identified call site (anchored-popover `isConnected`).

### Legal
- **Refund policy:** appended the statutory **14-day right to cancel** (Consumer Contracts (Information, Cancellation and Additional Charges) Regulations 2013), distinct from the goodwill 30-day return, with the cosmetic-hygiene exemption. *Updated via API. Recommend a legal review of wording.*
- **Footer phone:** `tel:+443330495549` (0333 049 5549) + email added to the footer brand block.

---

## REMAINING / DEFERRED (with reasons)

- **P1 — Cart drawer open-on-add.** Auto-open is enabled + the pageerror is guarded, but the drawer still doesn't open on add — a Horizon **cart-section-render race** (the `<cart-drawer-component>`/dialog is re-rendered by the Section Rendering API around the `CartAddEvent`, so `showDialog()` doesn't land). The add itself works (bubble updates). Needs a focused fix (e.g. re-open the drawer after the section morph settles) — risky to attempt blind; recommend a dedicated brief.
- **Shipping copy reconciliation** — blocked on Daniel's decision on the canonical rules (see PART 1 P0). I won't change live shipping rates or guess thresholds.
- **Privacy policy MHG rewrite** — the native Privacy policy is on **Shopify auto-management**, which the API refuses to overwrite ("Automatic management … must be turned off"). Daniel turns off auto-management in admin to allow a bespoke MHG policy; note the customer-facing privacy is the custom `/pages/privacy-policy` (the native `/policies/*` 301 to the custom pages). Auto-managed text also improves once the shop name + email are branded.
- **Visual token consolidation (P2/P3)** — brand-dark `#241836` band + purple-tint option + off-token `#333030`/`#E5E2DC`/card-radii + article-body H2 weight, and **4 unused sections** (decision-band, product-showcase + 2): deferred to a focused visual/cleanup pass.
- **System-page colour-contrast pair (P2)** — needs the exact element identified against tokens; deferred.
- **Retired-template prune** — orphan template files carrying (non-rendered) banned copy; recommend deletion.

---

## ADMIN-UI CHECKLIST FOR DANIEL (cannot be done via API/theme)
1. **Shop All → untick "Hide from search results"** (P0 — money page noindex).
2. **Set shop name to "Senseless"** (fixes homepage title fallback + the "– senseless-numbing" suffix on every title).
3. **Set a homepage SEO title + meta description.**
4. **Confirm the canonical shipping rules** (free-standard + any next-day thresholds) so I can align the banner + policy; reconcile the EU/International zones vs "UK only".
5. **Customer accounts → Classic + branded** (currently NEW passwordless; off-domain account links).
6. **Cookie:** provision Customer Privacy/consent + **disable Shopify's native banner** (two banners currently).
7. **Provide the VAT number** (Contact + footer slots ready).
8. **Turn off Privacy-policy auto-management** if a bespoke MHG native policy is wanted; **brand the store email** (currently personal iCloud).
9. **Install Judge.me** (keep Review schema gated until reviews exist); **keep the theme unpublished** until the 7 placeholder images are replaced (image work, separate).

## HOLD
Remediation pass complete to the extent safely API/theme-fixable without images. theme-check 0; theme unpublished. Cart-drawer open-on-add + shipping reconciliation + the ADMIN-UI list remain.
