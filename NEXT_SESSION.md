# Next session — Senseless (Canon v2.20)

Read `CLAUDE.md` → run `scripts/reconcile.sh` → read the Project Instance + State Surface first.
**Machine last used:** MacBook Pro — 14 Aug (`Daniels-MacBook-Pro.local`). Clock is **UTC+3
(EEST)** — consoles render timestamps in EEST, not UK time.

**Phase A of `docs/TATTOO-BUILD-SWEEP.md` is DONE — all ten items, shipped, deployed and
live-verified.** `main` @ `d954fb5` == `origin/main`, clean. Notion write-back complete
(State Surface, Decisions row `3bb58bc3-75ea-81b2-9c32-c0e2d8b577e0`, Compliance Hold
`3bb58bc3-75ea-8147-ad45-e77a97ac8ddc`).

---

<!-- ON-CONTINUE:START -->
## ▶ IF THE USER SAYS ONLY "CONTINUE" — do this, don't ask

**Fix the five bundle SEO descriptions. They are live in SERPs promising an item that is not in
the box.**

All five still read *"cream, gel, spray, cleanser and vanity bag"* in `seo.description`. The
vanity bag was **removed from all four on-page surfaces on 6 Aug pending stock** — so Google is
currently advertising a component the customer will not receive. Verified still true 14 Aug via
the Admin API. This is a consumer-protection problem (CPUT 2008) rather than an SEO one, it
needs **no gate and no answer from anyone**, and it has been carried on the flagged list since
7 Aug.

- The five: `clinical-numbing-kit-small`, `clinical-numbing-kit-large`,
  `advanced-numbing-kit-small`, `advanced-numbing-kit-large`, `professional-numbing-kit-large`.
- **Read the on-page bundle copy first** and match it — the descriptions must agree with what
  the PDP now says, not with what it used to.
- **Trap, cost a whole field on 7 Aug:** `productUpdate` **deletes** `global.title_tag` when
  `seo.title` is byte-identical to `product.title`, and it silently nulls `seo.description` if
  you send a `seo` object without it. Send both fields, then **re-read from the API separately**
  and diff against the INTENDED string — never against what the mutation returned.
- Daniel's instruction stands: **restore the bag everywhere when stock lands.** Do not delete
  the wording from a note somewhere it can be recovered from.

Then, if there is time, take the rest of the still-open flagged list in the same pass: the three
spray PDP descriptions saying "laser and waxing" (needs a ranking source first),
`UK-Formulated` vs `UK-formulated` casing, and the laser hero alt text contradicting the body
copy about gel.
<!-- ON-CONTINUE:END -->

---

## ⚠️ TWO THINGS THAT STILL OUTRANK ALL BUILD WORK — raise with Daniel

Neither was touched this session. Both are unchanged from the 13 Aug handoff and both attach to
the domain now hosting the tattoo cluster.

**1. A bought-link package is pointed at senseless.uk and it is live.** DR 14 → 27 → 21 → 10 →
**7**. **158 of 160 live referring domains are Ahrefs-flagged spam**; earned editorial
refdomains: **zero**. Placements were still arriving during the session that found it
(`backlinkengine.shop`, first seen `2026-08-12T18:09:50Z`). Nothing in the repo records anyone
commissioning it. **Ask who is paying for it, stop it, consider a disavow.**

**2. Senseless and Totally Numb share a review corpus.** Confirmed at aggregate level from
server-rendered JSON-LD on both stores (TN `comfort-cream-bronze` 4.85/13 == SL
`clinical-strength-cream` 4.85/13; TN `comfort-cream-platinum` 4.88/216 vs SL
`professional-strength-cream` 4.88/207). **NOT confirmed — do not repeat as fact:** the claim
that review *texts* were edited from "tattoo" to "procedure", the 227-review dedup, the date
distribution, and the "3 of 227 verified buyers" figure. Re-extract from the Judge.me admin
before this goes near legal. **Owner + legal. Do not touch the reviews unilaterally.**

Full evidence: `docs/TATTOO-REPOSITIONING-2026-08-12.md` Part 4.

---

## What shipped on 14 Aug

**Live now**
- `/pages/delivery` — all four candidate URLs previously 404'd while `/pages/shipping-delivery`
  is noindexed. Every fact matches the published policy; no rate or transit window invented.
- `/pages/tktx-numbing-cream-uk` — a checklist, not a comparison (see "Decisions taken" below).
- `/collections/tattoo-aftercare` — 2 products, disjunctive TYPE rules.
- **7 guide articles** (5 objection Q&A, 2 aftercare). Sitemap 60 → 70 URLs.
- `/pages/how-to-apply-numbing-cream` widened: tattoo step, tattoo row, tattoo FAQ.
- **Sitewide entity graph** — one `@id`-linked `@graph` replacing four free-standing documents.

**Built, deliberately NOT published — 404 live, 16 members each**
- `/collections/numbing-cream-for-tattoos` and `/collections/numbing-cream-for-piercings`.
- **To publish either:** flip `"published": True` on that entry in `COLLECTIONS` in
  `scripts/build-tattoo-resources.py`, re-run with `--apply`, then **re-run
  `python3 scripts/injectable-clean-sweep.py`** — publishing adds an ad-facing surface and the
  invariant must be re-measured against the current baseline of **0 breaches across 44**.

---

## The gates, current state

| Gate | State |
|---|---|
| **G1** — what do the CPSRs declare as intended use / application site? | **STILL OPEN. The only thing blocking publication of two finished collections.** Daniel's "the certs have been updated" is verbal; no written scope exists anywhere in the repo or Notion. One email to the safety assessor may close it. |
| **G2** — can *"Apply to clean, unbroken skin"* change? | **STILL OPEN.** Assume NO. Everything written this session stays inside that limit and says nothing about broken skin or mid-session re-application. |
| **G5** — Senseless or Totally Numb for tattoo? | **ANSWERED** 2026-08-13. Both target the same customer base. Repo canon corrected this session. |
| **G6** — is the tattoo collection ad-facing? | **Assumed YES and built that way.** Costs nothing if the answer turns out to be "organic". |

---

## Decisions taken this session that a reviewer might question

- **Piercings collection created UNPUBLISHED**, departing from sweep item A8's "shippable
  today". A8 says "no tattoo gate", which means it does not depend on the *lane* question — not
  that it is ungated. G1 asks what the CPSR declares as intended use, and that covers piercing
  exactly as it covers tattooing. G1's own default is "build, do not publish". One line reverses
  this if Daniel disagrees.
- **The TKTX page compares nothing on efficacy.** A competitor comparison falls under BPMMR 2008
  and must be objective and verifiable, and no substantiated TKTX product data exists here. Two
  TKTX domains were fetched directly on 14 Aug: each claims to be "the only certified
  distributor", and neither publishes a UK company number, VAT number or ingredients list. The
  page gives the reader seven checks they can run themselves instead.
- **"INCI disclosure" was left OFF that page** — see the flagged list below.
- **The phase-6 build report got an appended correction, not a rewrite.** A build report is
  evidence of what shipped and when; rewriting one to match a later decision destroys the audit
  trail.

---

## Flagged, not actioned — needs Daniel or the safety assessor

1. **Senseless publishes no INCI list anywhere.** No ingredients metafield on any product, no
   PDP renders one. This is why the "INCI disclosure" axis was left off the TKTX page rather
   than claimed — we would have been asserting a transparency we do not practise. **Publishing
   the INCI list is the single cheapest way to make that page's strongest axis real**, and it is
   a reasonable thing for a buyer in this category to expect.
2. **The Foaming Cleanser contradicts itself, live.** Its description says *"For use on unbroken
   skin"*; its own safety block (`sections/senseless-safety-warnings.liquid:18`) says *"Suitable
   for use before treatment and on freshly treated skin"*. Material to all aftercare copy — the
   new copy follows the safety block. Needs a ruling.
3. **No named author on any guide.** The `Person` byline mechanism is built on
   `sections/senseless-article.liquid` (settings `author_name` / `author_role`) but left empty:
   Shopify's author field is the organisation "Senseless". On a regulated site an author credit
   is a claim about who stands behind the copy, so it needs a real person's agreement.
4. **Ahrefs is at 245,876 / 400,000 units**, not the ~105k the last handoff recorded. Resets
   **2026-09-09**. Check `subscription-info-limits-and-usage` before any research.

---

## Gotchas earned this session

- **`snippets/senseless-structured-data.liquid` IS a reviews-guard file** (manifest marker
  `product.metafields.reviews.rating` — it carries the Judge.me `aggregateRating`). The first
  deploy aborted on guard (c). Editing it needs `--reviews-changed` **plus a lock commit**. The
  guard was right and the markers survived.
- **`scripts/content-lint.py` ignores any path you pass it.** It walks the repo itself and is
  scoped to theme files — it skips product descriptions, page bodies, blog articles, collection
  descriptions and admin meta, which is *most* of what a content session authors. Use
  **`scripts/content-lint-text.py`** for anything bound for the Admin API.
- **Do NOT use `scripts/build-articles.py`.** It is POST-only with no existence check and
  re-posts the original five articles as duplicates on every run. Its bodies also still carry
  five open Hard-Rule breaches (`docs/SITE-ASSESSMENT-2026-08-06.md:50-52`), so a "fix" applied
  live reverts the next time anyone runs it. Use **`scripts/publish-articles.py`**, which is
  idempotent by handle.
- **`metafieldsSet` replaces the whole value of a `list.single_line_text_field`.** Writing
  `["Tattooing"]` onto `professional-strength-cream` would have destroyed its six existing
  procedures. Always read-modify-write, pass `compareDigest`, and verify against a snapshot
  taken *before* the write — never against what the mutation returned.
- **`meta-tags.liquid` appends `" | Senseless"`** unless the title already contains the brand.
  Two article meta titles rendered at 64 and 63 chars before this was caught. Budget for it.
- Cookie-banner / Clarity consent coupling from 8 Aug still applies — see `f2483be`.

---

## New tooling (all committed)

| Script | What it is for |
|---|---|
| `scripts/injectable-clean-sweep.py` | The ad-facing invariant, as a reproducible script. Full sitemap, default-deny classification. **Current baseline: 0 breaches across 44 ad-facing surfaces.** Re-run after any nav, collection, homepage or landing-page change. |
| `scripts/content-lint-text.py` | Compliance lint for Shopify-resident copy. Same rule set as `content-lint.py`. Exit 2 on any BLOCK. |
| `scripts/publish-articles.py` | Idempotent article publish/update from a JSON content file. Dry run by default. |
| `scripts/build-tattoo-resources.py` | Pages, product procedure metafields and the three collections. Idempotent, store-gated, dry run by default. |
| `docs/tattoo-cluster-content.json` | Source of truth for the 7 articles. Edit here, re-run the publisher. |

---

## Next Work Item

**Phase B of `docs/TATTOO-BUILD-SWEEP.md` is written and ready but held on G1.** B2 (the
sitewide "Made for aesthetics" pass — 33 occurrences across 26 files, plus `docs/SECTIONS.md`
and `DECISIONS-LOG.md`) is the largest remaining piece and **must not start before G1 clears**:
widening that tagline *is* the intended-use change.

So the order is: the bundle SERP fix above (ungated, do it now) → chase G1 and G2 with the
safety assessor → Phase B. Phase C stays blocked.
