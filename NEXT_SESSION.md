# NEXT_SESSION — handoff

**Last session (1 Sep 2026, MacBook Pro, marathon):** funnel fixes shipped; two-session
collaboration with senseless-app (its handover items executed + its completion report
received); FOUR founder decisions taken and logged. Everything below is live and verified;
repo == origin/main, DECISIONS-LOG carries five 2026-09-01 entries.

## Founder decisions this session (all in DECISIONS-LOG.md)

1. **Naming:** "<Tier> Strength <Format>" stays; "Comfort <Format>" noun retired from
   store text (the relayed Comfort rename shipped and was reverted within the hour —
   direct word beats relay). Cleanser = "Foaming Cleanser". Handles never changed.
2. **No sale presentation on bundles:** no struck prices, no Save pills, anywhere
   (hero/cards/cart/contents). Savings live as ONE static plain-text line.
3. **Bundle value model:** compareAt = four-product sum; **the bag is a free inclusion,
   never priced into the comparison** (the +£9.99 correction was wrong and reverted).
   Line reads: "£71.99 for the set — the cream, gel, spray and cleanser are £79.96
   bought separately, and the Senseless Cosmetics Bag is included."
4. **Certification only:** ALL cosmetic-vs-medicine language is off the site — the 14 Aug
   removal completed (trust-line "Cosmetic product" items, self-classification sentences,
   medicine-FAQ pairs, comparison-page nouns) AND the 16 "not an anaesthetic" statements
   removed by standalone decision with the MHRA-boundary stake stated first. CPSR is the
   only credential. Canon vocabulary kept: "cosmetic brand/numbing range/topical
   preparation" + spelled-out Cosmetic Product Safety Report (verified intact, 19 instances).

## Also shipped this session

- **Review widget on all 14 PDP templates** — first review lists ever rendered on PDPs
  (renders as `jdgm-review-widget`; earlier "not rendering" was a wrong grep needle).
- Funnel batch: homepage highlights = real bestseller + category-noun hero; mobile sticky
  ATC; cart £40/£80 progress + trust row; Selector ?strength= handoff; PDP exit-row/size
  labels; chips side-by-side then in-pill stacked on mobile; comparison copy out of grid
  intros (FAQ keeps it).
- App-handover items: Contents eyebrow, five-item trust badge, approved per-bundle
  descriptions (verbatim, now the single source — the app drops its duplicate),
  build-bundles.py FENCED (stale 150ml/prices would corrupt data).
- Bundle SEO: "cosmetic prep" sentences replaced (UK-formulated claim now survives the
  app's sentence filter — its item 7), "vanity bag" → "cosmetics bag".

## Verification state

- Asset-API compare after the big pushes: 54/54 match (run it EVERY multi-file deploy —
  this session briefly mis-diagnosed cache because one batch skipped it).
- Served-output sweep for removed phrases: NOW CLEAN EVERYWHERE (llms.txt structured).
  The 2 "cached" guide pages were actually a 422-REJECTED deploy: the sweep's whitespace
  tidy flattened comfort-compare's {% liquid %} block (invalid), Shopify rejected it, and
  the CLI printed "deploy: success" TWICE. Repaired from git + surgical re-edit
  (`b3ed77d`→repair commit). NEW RULE: a DIFF after a "successful" scoped re-push means
  the FILE is invalid; and never regex-tidy whitespace across .liquid files.
- Injectable sweeps: genuine zeros (error-count checked).
- The senseless.uk edge cache holds pages ~10-30 min even with ?_fd=0&x= — judge
  "failed deploys" by Asset-API bytes + myshopify domain, and re-check later.


## Evening strand: SEO/GEO verification, Ahrefs sweep, outreach plan (all closed)

- **SEO/GEO regression after the day's surgery: ZERO structural harm** — 0 invalid JSON-LD
  across 7 page types, merchant-listings layer intact, FAQPage valid, titles/canonicals
  untouched, llms.txt structured. One self-inflicted find fixed same-day: orphaned
  AggregateRating microdata from server-rendered badges — sanitiser snippet + the PDP
  hero's Judge.me APP BLOCK retired entirely (guard manifest updated via --reviews-changed
  after the guard correctly ABORTED the unannounced contract change).
- **Ahrefs new issues all addressed** (200 units spent; ~16.8k left til 9 Sep; GSC
  endpoints are FREE): schema errors (58 URLs) fixed as above; links-to-redirect fixed
  (two sitewide sections linked the retired choosing-your-* paths); two short metas
  extended. Residual by design: Judge.me WIDGET rich snippet (Daniel: "Rich Snippets"
  toggle off in Judge.me dashboard), CSS bundle size, two n=1 slow flags.
- **Performance truth (GSC via Ahrefs project, free):** 4–11 organic clicks/WEEK; all
  commercial terms at pos 28–50; biggest asset /pages/strongest-numbing-cream 953 imp/wk
  @35. Diagnosis: AUTHORITY, not on-page. Fixed tonight: SEO titles/metas on the three
  near-page-1 pages (they had NONE), 6 internal "Strongest numbing cream, answered"
  anchors.
- **Outreach plan researched (38 verified prospects) and published:** "The Nerves Index
  Playbook" artifact — 15 ref domains/90 days, ≥70% brand anchors, 2 exact-match slots,
  Tier-1 ten, Appointment Nerves Index PR play, templates, Rules Card, cadence.
  Referring-domains baseline snapshot due 9–10 Sep after the unit reset. Free quick win
  flagged: Judge.me public shop page toggle (an indexed link, switched off).
- **Founder challenge resolved, no action:** the certification-only sweep does NOT damage
  the SEO funnel — FAQ rich results are dead for ordinary sites (2023) and lexical
  token-matching wasn't winning anything (those queries sat 45–55 with 0 clicks). I
  briefly overweighted word-level trims against my own authority diagnosis; corrected.
  Certification-only stands everywhere. Category noun ("numbing cream" ×171), strongest/
  EMLA/Ametop/TKTX keyword payloads all intact.

## From the app session's completion report (its 7 commits a8bb9c3..f66739d)

- App aligned on: naming, five bundle rows, no sale signals, size-correct deep links,
  certification-only filter (with CPSR/keep guards), duplicate-description drop.
- **URGENT for Daniel: Google Play developer verification, deadline 30 Sep 2026** —
  unverified apps are removed from Play globally. Needs his Play Console login.
- Its scripts/notion-write.py 404s: the "Code" Notion integration lost Session-Log DB
  access in the 28 Jul restructure — someone with Notion admin must re-share that DB.
- App-side still open: nothing installed on a physical device this session; on-screen
  recheck of final bundle copy owed.

## Open site-side

- Klaviyo popup suppression (Daniel, app-level) — still the biggest unfixed brake.
- Consent Mode v2 check (Daniel) — the measurement blackout stands (72/75 orders blind).
- Judge.me: 207 imported reviews still parked on Professional Strength Cream (his call on
  redistribution vs store-reviews move; legal check advised); badge metafield on only 7
  products so card stars cover ~6/16.
- templates/page.how-it-works.json is ORPHANED (no page uses it; /pages/how-it-works
  301s to the System page) — delete candidate.
- Funnel round-two deferred items: single-grid tabs consolidation, Selector embed,
  aggregate-rating hero line, cart-page suggestions collection, add-to-cart toast
  (needs Daniel), app-banner position (Daniel), one-chat-bubble choice (Daniel).
- G2 broken-skin gate: still BLOCKED on CPSR/MHG owner. "Antibacterial" ×11 still needs
  MHG substantiation. Email-auth strand: Peter's runbook, DNS untouched.
