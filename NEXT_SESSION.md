# NEXT_SESSION — handoff

**Last session (27–28 Aug 2026, MacBook Pro):** two strands — (1) diagnosed why
Senseless email lands in junk and briefed Peter to fix the DNS, (2) audited all 17
product pages and cut the copy the founder objected to. Everything below is live.

## Done

### Strand 1 — email authentication (senseless.uk)

- **Diagnosed the real cause.** Four systems send as `@senseless.uk`; DMARC is at
  `p=quarantine`, so anything that does not **align** is junked by our own policy.
  Only Microsoft 365 aligns, and it does so on SPF alone.
  - **Klaviyo** is on the SHARED sending domain → cannot align → campaigns fail
    DMARC deterministically. This is the cause of campaigns in junk.
  - **M365** has NO DKIM published (`selector1/2._domainkey` absent). DMARC rests
    on SPF only, with no fallback on forwarded or mailing-list mail.
  - **Shopify** (`cs@senseless.uk`) is very likely unauthenticated, but this is
    **NOT provable from DNS** — host names are per-store and the Admin API does not
    expose the status. Must be read in the admin.
  - **DMARC `rua` points at GoDaddy's aggregator**, so nobody here has ever seen a
    failure report. Confirmed the authorisation record exists at
    `senseless.uk._report._dmarc.onsecureserver.net`.
- **Corrected a wrong claim before it went to the agency.** "SPF only authorises
  GoDaddy" is FALSE: `include:secureserver.net` chains through `spf-0.secureserver.net`
  to `include:spf.protection.outlook.com` in **3 of 10 lookups**. `-all` inside an
  included record does not end the outer evaluation (RFC 7208 §5.2).
  **Do not edit the apex SPF record** — it is the only mechanism currently producing a
  DMARC pass, and the lookup headroom is load-bearing.
- **`scripts/email-auth-check.sh`** (commit `ae4e3cc`) — reads live DNS, pass/fail per
  sender. Refuses to report a clean run if any lookup errored (exit 2 = UNRELIABLE),
  per the `injectable-clean-sweep.py` false-zero lesson.
  **Current state: 6 pass · 4 fail · 1 warn · 0 resolver errors.**
- **Peter briefed.** Five-job runbook written for someone with no email knowledge,
  rendered to PDF (`~/Documents/senseless-briefs/`) and emailed to
  peter@matrixhealthgroup.co.uk from Outlook web. Confirmed in Sent Items.

### Strand 2 — product page copy

- **Audit:** 13 agents over a corpus of all 17 products (live Admin API + repo
  templates). 81 findings survived a hostile verification pass; 33 were dropped as
  fabricated, misquoted or taste-only.
- **Descriptions (live, Admin API):** second paragraph removed from **16 products** —
  every one was either defensive steering ("Most sessions don't need the practitioner
  tier") or a duplicate of the same page's own Key Facts/FAQ. Then the duplicated
  sizes/directions/CPSR paragraph removed from the **9 range products** (all three
  facts already render in Key Facts, the safety block and the trust bar).
  Backups: `build-reports/product-description-p2-removal-backup-2026-08-27.json` and
  `…-p3-removal-backup-2026-08-27.json` — every original recoverable.
- **Templates (`46a6dcc`):** cream FAQ repetition cut (the 45–60 minute sentence pair
  appeared verbatim in two adjacent accordion items); gel/spray duplicated clause cut;
  spray "How long does it last?" no longer describes CREAM technique; bag added to
  bundle contents; bundle cross-sell no longer offers items already inside the bundle.
- **Cart (`e064731`):** cart upsell is now bundle-aware (reads each item's own
  `bundle_contents`), and the stale-empty-class bug is fixed at the root.

## Next Work Item

1. **Peter works jobs 1–5 in the brief.** NOTHING IN DNS HAS BEEN CHANGED. Order is
   reports → M365 DKIM → Shopify → Klaviyo → then resume sending.
2. After each job, re-run `bash scripts/email-auth-check.sh` and check it moves.
3. Only when it is clean does the September send plan (max 5, tight segments) start.

## Gotchas

- **Safety gate G2 is BLOCKED, not done.** The founder says the product is fine on
  broken skin and asked to remove "Apply to clean, unbroken skin." and add in-session
  "extend" wording. **Not actioned.** That block is the approved launch-gate compliance
  set, hardcoded and non-editable by design (Decision 2 Jul 2026); broken-skin
  suitability sits in the CPSR claim envelope, so it needs the CPSR/MHG owner, not a
  content call. "Extend" would also be a duration claim under the Hard Rules.
- **FULFILMENT MUST SHIP A BAG WITH EVERY BUNDLE.** The founder confirmed bundles
  contain the Cosmetics Bag, so the metafield, body copy, FAQ and collection page now
  all say so. If the pick list does not include it, the site is now misdescribing.
- **"Numbing is a cosmetic preparation that supports comfort" is STILL LIVE** in the
  bundle rich-text section. Removing it from the descriptions did NOT close that
  flagged effect claim.
- **"Antibacterial" appears 11× across 7 pages.** Not a Hard Rule breach, but it is a
  biocidal claim needing substantiation — a question for MHG.
- **73 audit findings remain open.** Only the items the founder named were actioned.
  Full verified set in the workflow output; highest-value untouched item is
  "What it's used for." × 24 across 9 pages.
- **`config/settings_data.json` drifts 42 bytes from live — whitespace only.**
  Semantically identical. It is NOT the cause of anything. Do not chase it again.
- **The cart drawer "keeps reverting" was never a revert.** `cart-drawer--empty` is
  written once server-side from `cart.empty?` and nothing removed it, so the first
  AJAX add left a stale class and the empty-state layout slid the heading under the
  close button. Fixed in `cart-drawer.js` + a `:has()` CSS guard.
- **Storefront cache is per URL.** Use `?_fd=0` plus a random param; a plain fetch can
  serve a stale page and read as a failed change.
