# Phase 9 Track 1 — Legal/policy pages + Contact + Trade (dual-layer)

**Date:** 2026-06-04 (BST) · **Branch:** dev · **Theme:** Senseless Dev `#199324434780` (store `senseless-numbing`) · **Commit:** `68a48d8`
Token refreshed. Build sources (verbatim): Shipping `36c58bc375ea813fb444f76f587ed11e`, Returns `36c58bc375ea8179862feeead1d1f5e4`, Privacy `36c58bc375ea811495bbea80a1db5b76`, Terms `36c58bc375ea81f8b1bbd3fdd255a863`, Cookie (TN `34f58bc375ea81c9aae7d39b03a3c076` adapted), Contact `36c58bc375ea81608067ea8b51cb3079`, Trade `36c58bc375ea815da5b7eca9ec8bc29a`. Dual-layer per Strand 5.

## Custom pages built (7) — all resources created/confirmed, published, suffixed
- `/pages/shipping-delivery` (FAQPage) · `/pages/returns-refunds` (FAQPage) · `/pages/privacy-policy` (WebPage+FAQPage) · `/pages/terms-conditions` (WebPage+FAQPage) · `/pages/cookie-policy` (WebPage+FAQPage, TN adapted → Senseless) · `/pages/contact` (rebuilt) · `/pages/trade` (rebuilt).
- Built from existing modules (guide-hero, rich-text, faq-accordion, image-text-band, callout-band, trio-card-row, contact-form, page-schema + new org-schema). Copy verbatim; `[SENSELESS CS EMAIL]` → **cs@senseless.uk**; cross-links to retired `choosing-your-strength`/`how-it-works` repointed → `/pages/the-senseless-system`.

## Native policies (shopPolicyUpdate → checkout footer)
- **REFUND_POLICY ✓ · SHIPPING_POLICY ✓ · TERMS_OF_SERVICE ✓ · CONTACT_INFORMATION ✓** set (prose versions, same substance + entity facts + cs@senseless.uk + phone). All resolve at `/policies/*` (200) and now render in the theme/checkout footer.
- **⚠ PRIVACY_POLICY blocked:** `shopPolicyUpdate` returned *"Automatic management for Privacy Policy must be turned off in order to make changes."* Shopify's auto-privacy-policy feature (Settings → Privacy/Policies) must be **disabled in admin** before the API can set our prose body. Until then the checkout shows Shopify's auto-generated privacy policy (link resolves). **Action for Daniel:** toggle off automatic privacy-policy management, then re-run shopPolicyUpdate for PRIVACY_POLICY (prose is ready in the build script / privacy page).

## Resolved values applied throughout
- **Emails = senseless.uk:** cs@ (policies), hello@/press@/legal@ (Contact cards). No `.co.uk` anywhere (grep clean).
- **Phone 0333 049 5549 — public:** footer (tel link), Contact §2 consumer card + §4 company details, Organization/ContactPoint schema `telephone`, native CONTACT_INFORMATION. **Old TN 07899 663527 appears nowhere** (grep clean).
- **Company:** Matrix Health Group Ltd, no. **17099304**, registered address **128 City Road, London, EC1V 2NX** (Terms intro + Contact §4). VAT = clearly-marked placeholder (Daniel to supply).
- **Returns address:** Paddock Business Centre, Paddock Road, Skelmersdale, WN8 9PL.

## Forms
- Reused `senseless-contact-form` (native `{% form 'contact' %}`, block-driven) for both — added a **multiselect** field type for the trade "products" field. Consumer form: name*/email*/order no./enquiry type*/message*/GDPR consent*. Trade form: practice*/name*/email*/phone/practice type*/monthly volume*/products(multiselect)/about*/GDPR consent*. Required-field validation (HTML5 `required` + native) + **GDPR consent checkbox (required)** on both.
- **Handoff (config flag for Daniel):** the native contact form routes to the store's contact-notification email (Settings → Notifications). Separating consumer vs trade pipelines + CRM integration needs a Shopify Flow/app webhook — flagged as Daniel's config; GDPR consent copy pending legal verification.

## Indexing (per Strand 5)
- Policies (shipping/returns/privacy/terms/cookie) + Trade = **indexed** (WebPage schema, robots null). Contact = **noindex** (`seo.hidden=1`).

## Cookie banner
- Repointed the interim consent-banner link `/policies/privacy-policy` → **`/pages/cookie-policy`**.

## Verify
- **theme-check: 0 errors** (401 files; pre-existing Horizon warnings only).
- **Render-verify (Playwright, desktop + mobile):** all 7 pages **200**; policy/trade schema = WebPage+BreadcrumbList+FAQPage + **indexed**; contact = Organization+ContactPoint (telephone present) + **noindex**; footer shows phone + native policy links (Privacy/Refund/Shipping/Terms/Contact); `/policies/refund-policy|shipping-policy|terms-of-service` → 200; cookie banner → /pages/cookie-policy; contact form GDPR-required + 5 required fields; trade form 4 multiselect checkboxes; senseless.uk rendered; mobile forms visible.
- **Grep:** no old TN number / `.co.uk` / totally-numb in theme.

## Flags / open items
- **PRIVACY_POLICY native** — blocked on Shopify auto-management toggle (above).
- **Meta lengths (spec-verbatim, over guideline):** Trade title 69 / Contact title 32 ok; all policy descriptions ≤155. Trade title >60 (spec verbatim) — trim if wanted.
- **VAT number** + form CRM handoff destination + office-hours + GDPR consent copy = pending Daniel/ops/legal (placeholders/sensible defaults in place).
- **Trade `/pages/about` card** links to About, which isn't built yet (Phase 9 Track 2) — will resolve when About ships; currently 404. Flagged.
- All policy copy still pending solicitor sign-off (external gate, per Strand 5).

## Files / API
- New: `sections/senseless-org-schema.liquid`, `templates/page.{shipping-delivery,returns-refunds,privacy-policy,terms-conditions,cookie-policy}.json`. Edited: `senseless-contact-form.liquid` (+multiselect), `senseless-footer.liquid` (phone), `senseless-cookie-consent.liquid` (link), `page.contact.json` + `page.trade.json` (rebuilt).
- API: `pageCreate` ×6, `metafieldsSet` (metas + contact noindex), `shopPolicyUpdate` ×4 (REFUND/SHIPPING/TERMS/CONTACT_INFORMATION).

## HOLD
Phase 9 Track 1 complete + verified (both layers). One native-policy item (PRIVACY) blocked on a Shopify admin toggle — flagged for Daniel.
