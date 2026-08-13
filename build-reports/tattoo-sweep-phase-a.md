# Tattoo build sweep — Phase A, all ten items

**Date:** 2026-08-14 (machine clock UTC+3/EEST) · **Branch:** `main` · **Theme:** Senseless Dev `#199324434780` (store `senseless-numbing`) · **Commits:** `2937072` (theme), `b565e84` (reviews re-lock), `d954fb5` (Shopify resources)

Ran `docs/TATTOO-BUILD-SWEEP.md` Phase A end to end. The owner instruction of 12 Aug — *"make sure the docs are set up so the next session can build all in a single sweep"* — deliberately overrides the `CLAUDE.md` one-task-per-session rule for this work. It overrode nothing else: the verify-store gate, the deploy rules, the reviews-guard, the injectable-clean invariant and `compliance-check` all held.

---

## Phase 0 — pre-flight

- **Store gate PASS** via Admin API before every write: `myshopify_domain = senseless-numbing.myshopify.com`.
- **Ahrefs at 245,876 / 400,000 units**, not the ~105k the handoff recorded. Resets 2026-09-09. No research strand was re-run.
- **Injectable-clean baseline re-measured, not trusted.** The recorded "0 breaches across 14 surfaces" had no reproducible definition anywhere in the repo, so the sweep is now `scripts/injectable-clean-sweep.py`: fetches every sitemap URL, strips `<script>`/`<noscript>`, counts anchors to the three protected handles, and classifies each surface **default-deny** (an unclassified surface is treated as ad-facing). Baseline: **0 breaches across 41 ad-facing surfaces**, with organic hits exactly matching the documented allow-list in `.claude/rules/ad-facing.md`.
- **`scripts/content-lint-text.py` written before any copy.** `content-lint.py` walks the repo itself and ignores any path passed to it; it is scoped to theme files and explicitly skips product descriptions, page bodies, blog articles, collection descriptions and admin meta — which is most of what this sweep authored. Tested against a deliberately failing string before being trusted, per the 8 Aug standing lesson.

---

## A1 · `/pages/delivery` — LIVE

`/pages/delivery`, `/pages/shipping`, `/pages/shipping-returns`, `/pages/delivery-returns` all 404'd; `/pages/shipping-delivery` exists but is `noindex,follow` **and** carries `seo.hidden = 1`, so it is absent from the sitemap. The new page is the indexable customer surface; the policy page stays the noindexed legal record, and the new page links to it.

Every fact is taken verbatim from the two published sources: free standard UK delivery over £40, free next-day over £80, 1pm working-day cut-off for same-day dispatch, Royal Mail, UK only, tracking on dispatch, plain unbranded packaging, 14-day window to report problems. **No paid-tier price and no transit-day count was invented** — neither published page states one, so the table says "Rate shown at checkout".

## A2 + A3 · GEO — one `@id`-linked `@graph`

The site emitted three to four **free-standing** JSON-LD documents per page with no relationship between them. Coverage was never the gap — a third-party audit already confirmed Senseless emits more schema than every competitor. The gap was that nothing connected the page an engine was reading back to the company publishing it.

| | before | after |
|---|---|---|
| Organization | homepage + 2 of 32 `/pages/*` | **every page type, including the 404** |
| WebPage-family node | **none, on any page type** | every page type |
| `@id` linkage | none | `#organization`, `#website`, `#webpage`, `#breadcrumb`, `#product`, `#itemlist`, `#article` |
| Product identifiers | `sku` on Offer only | product-level `sku`, `mpn`, `gtin13`, `productID`, `identifier[]` |
| ItemList entries | name + url | full nested `Product` with image, sku, brand, offer |
| Collection description | `truncate: 300` | `truncate: 1200` |
| FAQ questions | plain `<summary>` text | real headings — h3, or **h4 under a group heading** (level computed) |
| Article dates | `dateModified` = publish date | real edit date, plus visible `<time datetime>` |

`senseless-org-schema.liquid` now renders nothing (kept, because two templates still reference it, and removing a referenced section type is a storefront error). `senseless-page-schema.liquid` re-declares the **same** `@id` with a narrower type, so `/pages/about` emits one node typed `["WebPage","AboutPage"]` rather than two nodes competing to describe the page — verified live.

**A defect corrected rather than carried forward.** `Offer.shippingDetails` claimed a flat `£1.99` rate and a **4–6 day** transit. Neither figure appears in any human-readable copy on the site, and a 4–6 day transit directly contradicts the next-day delivery offered on both policy surfaces. A delivery representation the shopfront does not honour is a CPUT 2008 problem before it is an SEO one. Replaced with the two options the site actually publishes; standard delivery carries **no** `transitTime`, because none is published.

## A4 · Tattoo collection — BUILT, UNPUBLISHED

Cloned from `collection.numbing-cream-for-microneedling.json`, **not** SPMU/waxing: those link `/pages/does-it-hurt-by-treatment`, which links all three injectable collections. Zero injectable links, zero two-hop paths. `"Made for aesthetics"` was replaced with `"Three strengths"` in the trust bar and a factual range statement in Key Facts, so the template asserts no intended-use claim beyond the one the collection itself makes.

Collection created **unpublished**, 16 members, 404 live.

## A5 · Tattoo aftercare cluster — LIVE

`/collections/tattoo-aftercare`, smart rules `TYPE = Cleanser OR TYPE = Aftercare` (disjunctive) → exactly the Foaming Cleanser and the Vitamin A&D 4-pack. No new metafield needed. Plus two guides: *The First 48 Hours* and *Healing Stages, Day by Day*.

Compliance: `heals`/`treats`/`prevents` are BLOCK terms, so the copy uses *settle*, *barrier*, *comfortable*, *protected* — the vocabulary already live on the ointment. Every stage defers to the artist's instructions, and the "when to seek medical advice" list routes to a pharmacist, GP or NHS 111 rather than diagnosing anything.

**"Fragrance-free" was drafted and removed.** Neither aftercare product carries an INCI or ingredients metafield and nothing in the repo or the admin substantiates it.

## A6 · `/pages/how-to-apply-numbing-cream` — LIVE

Sixth cream step (the stencil needs a completely clear surface; tell the artist at booking), a `Tattooing` row in the by-procedure rich-text band, and a tattoo FAQ using the artist's-window phrasing permitted by Decision `39158bc3-75ea-8181`. `creamgel` 5/8 → 6/8 steps (the sixth becomes a `HowToStep` automatically), FAQ 7/50 → 8/50. Headline changed from "Five steps." to "The routine, step by step." so it does not contradict the step count.

## A7 · Five objection Q&A articles — LIVE

*Does Numbing Cream Affect a Tattoo?* · *Can You Use Numbing Cream Before a Tattoo?* · *Do Tattoo Artists Use Numbing Cream?* · *What to Tell Your Artist About Numbing Cream* · *Where to Buy Numbing Cream for Tattoos in the UK*.

**Structure** was pattern-matched to the live corpus; **claims language deliberately was not.** `docs/SITE-ASSESSMENT-2026-08-06.md:50-52` records five open Hard-Rule breaches inside the existing article bodies — *"numbing can help"*, *"any numbing takes hold"*, *"feel less of the process"*, *"take the edge off"* — all still live, and all originating in `scripts/build-articles.py`, so a live-only fix would revert on the next run of that script.

The lead article answers *"does numbing cream affect a tattoo?"* with **"nobody selling numbing cream is in a position to tell you it has no effect, and you should be wary of any brand that does."** That is the framework answer the strategy documents identify as the only position Senseless can structurally hold — and it is also simply true: no published body of work exists, and GN8 §4/App.10 make citing clinical data on a selling domain an implied medicinal claim, so research could not have been the differentiator either.

## A8 · Piercings collection — BUILT, UNPUBLISHED

**A deliberate departure from the sweep**, flagged here and in the Compliance Hold. A8 is marked "no tattoo gate", which means it does not depend on the *lane* question — not that it is ungated. G1 asks what the CPSR declares as intended use, and that question covers piercing exactly as it covers tattooing; G1's own stated default is "build, do not publish". One line reverses this if Daniel disagrees.

The copy leads with *"a lobe piercing probably doesn't need this"* — the honest position, and the one no competitor takes.

## A9 · TKTX page — LIVE, and built on verified ground

A competitor comparison falls under the **Business Protection from Misleading Marketing Regulations 2008** and must be objective and verifiable. No substantiated TKTX product data exists in this project, so a side-by-side table would have been invented.

Instead, two TKTX domains were **fetched directly** on 14 Aug. Each claims to be *"the only certified distributor of TKTX numbing cream"*, and neither publishes a UK company number, VAT number or ingredients list. Several such sites also carry their own guidance on spotting counterfeit stock. That is a checkable fact about the market, not a claim about the product — and it is the most useful thing a UK buyer can be told.

The page therefore compares **nothing on efficacy**. It gives seven checks the reader can run on any listing, with the Senseless answer to each, and a concession band for people already happy with what they use.

**`INCI disclosure` was left OFF**, though the sweep names it as an axis: Senseless publishes no ingredients list either. Claiming that axis would have asserted a transparency we do not practise.

## A10 · Canon and doc fixes — each verified before editing

- `docs/BRAND.md:3` pointed at Notion `36c58bc3-75ea-8116…`, which has sat under **Archive (pre-migration)** since 29 Jun and still reads *"Must hold the aesthetics-only focus"* / *"Removed: all tattooing positioning"* — the upstream source of the repo's aesthetics-only framing. Repointed at the Project Instance + State Surface.
- `docs/ARCHITECTURE.md:63` claimed old tattoo URLs *"will have"* been redirected. **Verified false against the live store the same day**: `/redirects.json` returns 15 redirects, none tattoo-related. Sentence removed with the evidence recorded.
- `.claude/skills/redirects/SKILL.md:17` used `/collections/tattoo-numbing-cream` as a worked from-path — **a live Totally Numb URL**. Replaced with a real redirect from this store's own set.
- `.claude/skills/seo-meta/SKILL.md:45-46` baked an aesthetics-only procedure list — naming two injectable collections — into the one example every future meta gets modelled on. Replaced, with a warning not to treat the example as a house pattern.
- `README.md:3` / `package.json:4` — "UK aesthetics-focused" **dropped rather than replaced**: the declared CPSR scope is not confirmed in writing, so the line now states what is certain and asserts no procedure scope in either direction.
- `docs/BRAND.md:27` said `--text-muted #8E8A82`; the live token is **`#6E6A63`** (AA-contrast fix, 26 Jun). `DECISIONS-LOG.md:131` was the second stale copy — both corrected, the log entry by appending a supersession note rather than editing the historical decision.
- `docs/BRAND.md:104` said the brand asterisk is `#6B3FA0`. Both renderers say **`#984AE8`**. Corrected, with the distinction recorded: `#6B3FA0` is brand primary and CTA (81 uses), `#984AE8` is the asterisk mark.
- `docs/AUDIT-2026-06-12.md` items 10 and P3.5 closed on the G5 ruling, with two figure corrections.
- `build-reports/phase-6-close-does-it-hurt-by-treatment.md` got an **appended correction, not a rewrite** — a build report is evidence of what shipped and when.

---

## Phase Z — verification

| Check | Result |
|---|---|
| `theme-check --fail-level error` | **0 errors** (exit 0) |
| `content-lint.py --fail-on-block` | **BLOCK 0** |
| `content-lint-text.py` on every authored string | **BLOCK 0** |
| Asset-API per-file diff after deploy | **14 / 14 match** |
| Reviews-guard post-deploy live verify | **5/5 pulls, every marker** |
| JSON-LD parse across 14 page types | **every document parses** |
| Product metafields vs pre-write snapshot | **0 of 16 lost a value** |
| **Injectable-clean sweep** | **0 breaches / 44 ad-facing surfaces** (baseline 0 / 41) |

**The metafield write was the one that could have done real damage.** `metafieldsSet` replaces the entire value of a `list.single_line_text_field`, so writing `["Tattooing"]` onto `professional-strength-cream` would have destroyed its six existing procedures. Done read-modify-write with `compareDigest`, and verified by re-reading independently and diffing against a snapshot taken **before** the write — not against what the mutation returned, which is precisely the false-pass caught on 7 Aug.

**Two errors caught by verification rather than review:** two article meta titles rendered at 64 and 63 chars once `meta-tags.liquid` appends the brand, and the aftercare collection SEO description was 162. All three re-published through the idempotent path — which is why `scripts/publish-articles.py` exists rather than reusing `build-articles.py`.

**One of my own measurements was wrong and self-corrected:** a first pass reported `/pages/delivery` as missing its meta description. `meta-tags.liquid` writes that tag across multiple lines and my single-line regex missed it. The tag was present and correct; re-checked with a multiline-aware parser before reporting.

---

## New gotcha for the canon

**`snippets/senseless-structured-data.liquid` is a reviews-guard file** — `reviews-guard.manifest:33`, marker `product.metafields.reviews.rating`, because it carries the Judge.me `aggregateRating`. The first deploy **aborted on guard (c)**. Editing it requires `--reviews-changed` plus a lock commit. The guard was right, the markers survived the rewrite unchanged, and the emission condition (`rating_count > 0`, so kit PDPs still emit nothing) is byte-for-byte the same logic.

---

## Write-back

- Decisions row `3bb58bc3-75ea-81b2-9c32-c0e2d8b577e0` — records **both** the 21 May aesthetics-only position and its reversal, because no predecessor row existed to supersede.
- Compliance Hold `3bb58bc3-75ea-8147-ad45-e77a97ac8ddc` — **Applied**, on the two unpublished collections, with the exact command that releases them.
- State Surface `38e58bc3-75ea-81ad-87eb-e20fcfc22406` — header, Repo commit and Sync status updated; log entry appended. The prior Sync-status text was **prepended to, not overwritten**: it is 14.7k chars and its content is not duplicated in the log below it.
- `canon/state.json` updated so `scripts/reconcile.sh` reports the new state.
- Notion `35e58bc3-75ea-8148-b0c3-cf9d2fa53e3a` (21 May, *"NOT for tattooing"*) sits in the **Matrix Health Group** tree and was **not** swept — it needs its own edit and is recorded as such.
