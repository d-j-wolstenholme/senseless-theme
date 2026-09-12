# NEXT_SESSION — handoff

**Last session (12 Sep 2026, MacBook Pro):** Same-day dispatch cut-off moved **3:30pm → 3pm** on
Senseless (and Totally Numb, same session). Theme deployed and verified live; every Shopify-side
statement and both checkout rate names changed. Then fixed the Shop mega-menu layout (Merchandise
column + column feet). Repo == origin/main @ `daa52f7`, clean.

## ON-CONTINUE — do these first

<!-- ON-CONTINUE:START -->
1. **The Senseless app still says "Same-day dispatch before 3:30pm"** — iOS
   `senseless-app/ios/Senseless/Brand/BrandProduct.swift:203`, Android
   `senseless-app/android/app/src/senseless/res/values/strings.xml:66`. Ask Daniel whether to change
   it and cut 1.0.7. (`matrix-health-ecommerce/brands/senseless` says "before 1pm" — same fix.)
2. **Daniel to check by hand for a 3:30pm cut-off:** Google Merchant Center → Shipping (order
   cut-off time → 15:00 Europe/London); Shopify Settings → Shipping and delivery → delivery dates;
   Klaviyo flows/forms; Shopify Inbox instant answers; Dondy WhatsApp auto-replies; Google Ads
   assets; notification emails.
3. **Notion write-back not yet done** for the cut-off change — Decisions DB entry + State Surface
   sync-status. The local mirror (`DECISIONS-LOG.md`, 2026-09-12) is written.
4. **Carried over from 4 Sep, status unknown:** Rich Results Test on
   `https://senseless.uk/products/professional-strength-cream` (expect ONE aggregate rating);
   Search Console "Validate fix" on the 3 issues; ask Daniel whether the Google Ads conversation
   with Martin has happened.
<!-- ON-CONTINUE:END -->

## Done 12 Sep — dispatch cut-off 3:30pm → 3pm (`01544e5`, `5dc687b`, lock `fbcbb59`)

- **Theme:** shipping banner (3 states), `page.delivery.json` (12), `page.tktx-numbing-cream-uk.json`
  (2), structured-data `cutoffTime` `15:00:00` (offset still from the shop clock). Deployed via
  `deploy.sh --reviews-changed`; Asset API 584 files before and after, only these 4 updated.
- **Shopify:** both rate names "Next Working Day (Order by 3pm)" (prices + conditions diffed
  unchanged), `SHIPPING_POLICY`, page `shipping-delivery` (SEO tag + `policy.prose_policy_body`),
  page `delivery` (SEO tag), article `where-to-buy-numbing-cream-for-tattoos-uk` (body + `custom.faq`).
- **Stale 1pm** removed from `docs/tattoo-cluster-content.json`, `scripts/build-tattoo-resources.py`,
  `scripts/policy-metafields.py` so a re-run can't republish it.
- **Live:** crawl of 81 URLs 0 × 3:30; Admin re-sweep 0 × 3:30. Detail in `DECISIONS-LOG.md`.

## Done 12 Sep — Shop mega-menu layout (`daa52f7`)

- `sections/senseless-header.liquid`, CSS only: Merchandise had a narrower track, so its heading broke
  "MERCHANDIS/E" and footer links wrapped, knocking the column feet out of line. Nav columns are now
  `minmax(min-content, 1fr)`; headings + footer links `nowrap`; footers 14px + 16px column bottom
  padding so they share one line with the card's "Shop the kit →"; Bundles rows `min-height: 28px`;
  card 200px at 1200–1279px.
- Verified live in Chrome at 1712px (no injected CSS): no overflow, only "Semi-permanent makeup"
  wraps (as before), footers level, first rows level.
- **Gotcha:** to preview CSS in the browser, append the test `<style>` to the END of `<body>` — the
  section's own `{% style %}` block renders in the body, so a `<style>` in `<head>` loses on equal
  specificity and the preview silently half-applies.

**Gotchas (12 Sep):**
- **Renaming a delivery method re-issues its `DeliveryCondition` ids.** A raw before/after diff of
  the rate card flags it "changed"; compare price + field/operator/amount instead.
- **The Admin writes landed ~30 min before the theme deploy.** The first deploy attempt was blocked
  by Claude Code's auto-mode permission check, so checkout and the policy said 3pm while the banner
  said 3:30pm until Daniel confirmed. Next time: deploy the theme first, then the Admin writes.
- The custom-app token lacks `read_locales` / `read_translations`, so translations can't be swept
  (no locale is published today — `/fr`, `/de`, `/en-us` all 404).

---

## Previous handoff (4 Sep 2026) — kept for reference

**Session (4 Sep 2026, MacBook Pro):** Google Search Console raised three structured-data
alerts; root-caused, fixed on both layers, and verified. Separately, the Google Ads account was
audited for the first time and the picture there is bad. Repo == origin/main @ `6053eec`, clean.

## What was wrong, and what fixed it

GSC alerted 2026-09-04 ~09:20 (forwarded by Peter 09:30): "Review has multiple aggregate ratings" —
CRITICAL for Review snippets, non-critical for Product snippets and Merchant listings.

**Root cause.** Judge.me's v3 Vue widget (`ReviewWidgetManager`, `widget_version: 3.0`,
`review_widget_revamp_enabled: true`) injected a SECOND Product node onto our own `@id`
(`<page_url>#product`) carrying only name + aggregateRating. Its duplicate-suppressor `W()` parses
only TOP-LEVEL ld+json objects and our Product sits inside `@graph`, so it never saw the rating we
already emit — while its `@id` resolver DOES walk `@graph`, which is why the injected node landed on
our exact `@id`. That asymmetry is the entire bug.

**Blast radius: 6 of 17 products** — the ones carrying reviews (professional-strength-cream 207/4.88,
clinical-strength-cream 13/4.85, advanced-strength-cream 12/4.92, vitamin-a-d-ointment-4-pack 1/5.0,
professional-strength-gel 1/2.0, advanced-strength-spray 1/5.0). The other 11 were clean only for
want of a first review.

**Two independent layers now close it; either alone is sufficient:**
1. **Judge.me dashboard** (Daniel, 13:49) — Settings → Google, SEO and AI → SEO Rich Snippets →
   BOTH "Add microdata snippets" and "Add JSON-LD snippets" unticked. Live values are now
   `disable_json_ld: true`, `remove_microdata_snippet: true`. Outside git, outside reviews-guard.
2. **Theme** (`66aa9b8`) — `class="jdgm-server-jld"` on the JSON-LD tag at
   `snippets/senseless-structured-data.liquid:139`, satisfying `N()` in the injector's gate:
   `if(i.jldDisable||i.disable_json_ld||N()||W()||!o||!e) return null;`
   Deployed via `deploy.sh --reviews-changed`; lock re-committed (`6053eec`).

## Verification state

- theme-check 0 errors (1832 warnings = pre-existing baseline).
- deploy.sh reviews-guard: all markers present 5/5 pulls.
- Asset-API remote diff: class present on live theme, `updated_at 2026-09-04T15:22:53+01:00`.
- All 6 reviewed PDPs re-fetched live: exactly 1 aggregateRating each (ours).
- Headless-Chrome CDP experiment WITH A PLACEBO CONTROL (forcing `disable_json_ld` back to false to
  reproduce): no class → 2 Product/2 ratings/1 injection; DECOY class → 2/2/1; `jdgm-server-jld`
  → 1/1/0. The decoy row proves the effect comes from the exact class string.
- NOT yet done: Rich Results Test, and the 3 GSC "Validate fix" submissions.

## GOTCHAS — read before repeating this work

- **Two Judge.me bundles exist and only one is live here.** The legacy `widget/main.js`
  (cdn2.judge.me) defines `c()` for `script.jdgm-server-jld` but EXCLUDES it from the PDP gate. The
  v3 `ReviewWidgetManager` bundle DOES gate on it. Reading the wrong bundle produced a confident,
  wrong refutation mid-session. Confirm which bundle runs before reasoning about the gate.
- **`curl` cannot see this class of bug.** The duplicate is injected after load. Two PDPs
  (professional-/clinical-strength-cream) still carry a frozen `jdgm-rich-snippet` microdata blob in
  the `judgeme.widget` metafield (written 2026-06-08) which Judge.me's JS now strips at runtime.
  Server HTML therefore still shows 1 microdata hit on those two — that is expected, not a breach.
- **Headless Chrome left 32 orphan processes** and stopped Chrome opening for the user. If a
  workflow spawns headless browsers, kill them afterwards (`pkill -f "headless=new"`).
- The Claude Chrome extension disconnected three times during the session.
- `senseless-jdgm-badge.liquid` is now redundant (Judge.me no longer emits badge microdata at
  source). Harmless; remove only as deliberate cleanup.

## Google Ads — AUDIT ONLY, do not change anything

Standing instruction from Daniel, 4 Sep: **read and report, never edit.** Agency-run account
(`ads@colossalsearch.com` / Colossal Search; Martin is the contact). See memory
`ads-account-audit-only`.

Audited 4 Sep, account "Senseless" 368-965-4782, last 30 days (5 Aug – 3 Sep):

- **Spend £1,243.14 against £921.08 of TOTAL store revenue (all channels). ROAS 0.41.**
  Prior 30 days also loss-making: £2,332 spend → £1,182 value (0.51).
- PMax: Shopping - Cream = £1,017.71 of the spend, 10 conversions, **£101.77/conversion on a ~£38
  AOV**. Senseless Search £94.93 / 3 conv. Two new Search campaigns built 27 Aug, £0 spend so far.
- **"Shopping - All products" was PAUSED on 5 Aug 15:27 by `ads@colossalsearch.com`** — a month ago,
  not "yesterday".
- Impressions peaked ~8,500/day 18–19 Aug, **crashed to 59 on 21 Aug**, then decayed to near zero;
  down 171,938 (−59%) on the prior 30 days.
- Conversion tracking WORKS (13 purchases, £505 recorded). **The "Google Ads is blind / bidding is
  starving" note from 31 Aug is REFUTED** — that was Shopify's journey data being empty, a different
  system. Real gap: Goals → Diagnostics says "You haven't set up any measurement features yet"
  (no enhanced conversions).
- "Apply for healthcare certification" alert is showing on the account. Unresolved.
- Campaign view has 2 filters applied showing 5 campaigns; not confirmed there are only 5.

**Sales reality (Shopify, via `shopify store execute`):** weekly revenue ran £250–575 through July
and early Aug, then collapsed — w/c 24 Aug £28.99, w/c 31 Aug £21.98. 1 Jul – 4 Sep total
£2,485.86 / 68 orders. **The collapse began w/c 24 Aug — before the schema breach existed** (widget
went on 31 Aug), and there were NO theme commits 28–31 Aug. The schema bug did not cause it, and
`aggregateRating` is not a Merchant Center eligibility field.

**Four questions for Martin, not yet asked:** (1) why is PMax paying £100 for a £38 order, and what
is Target ROAS set to; (2) what caused the 21 Aug impressions crash; (3) Shopping has been paused
since 5 Aug — deliberate, and what replaced it; (4) on current numbers the account loses money daily
— what is the plan and the stop-loss.

## Tooling notes from this session

- Orders/ShopifyQL: the custom-app Admin API token LACKS `read_orders` and `read_reports` (403).
  `shopify store execute -s senseless-numbing.myshopify.com --query-file f.graphql --json` CAN read
  orders but NOT products; the custom-app token is the reverse. Use both.
- Shopify MCP connector is token-expired (re-auth needs a browser). Per the standing rule that is
  NOT a blocker — the CLI + Admin API cover everything.
- Ahrefs' GSC mirror ended 27–31 Aug, so the last week of organic data was invisible. Organic runs
  at ~1 click/day (34 clicks in 39 days) and is irrelevant to revenue.
- Order attribution is empty on all 74 orders since 1 Jul (`customerJourneySummary.firstVisit` null,
  zero gclids) — a measurement gap, NOT evidence about paid traffic.

## Still open (unchanged from before)

- G2 safety gate ("Apply to clean, unbroken skin"). G1 is CLOSED — do not re-raise.
- Consent Mode v2 check on the Google & YouTube app (Daniel) — open since 31 Aug.
- Klaviyo popup suppression on gclid sessions (Daniel) — flagged since 6 Aug.
- 12 images to commission (`docs/IMAGE-BRIEF-tattoo-cluster.md`).
- "tattoo pain chart" (6,900/mo, KD 1) is still a 404; two strategy docs still contradict each other
  on whether it is winnable.
- Judge.me: only 7 products carry `judgeme.badge`; sync the rest so stars cover all cards.
