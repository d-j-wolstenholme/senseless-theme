# Next session — Senseless (Canon v2.20)

Read `CLAUDE.md` → run `scripts/reconcile.sh` → read the Project Instance + State Surface first.
**Machine last used:** MacBook Pro — 14 Aug (`Daniels-MacBook-Pro.local`). Clock is **UTC+3
(EEST)** — consoles render timestamps in EEST, not UK time.

**Phase A AND Phase B2 are DONE and fully live.** `main` @ `0ef44c4` == `origin/main`, clean; 60/60 theme files Asset-API verified against live. Notion write-back complete (State Surface, Decisions `3bb58bc3-75ea-81b2-9c32-c0e2d8b577e0` and `3bc58bc3-75ea-81d2-b505-e1b2a023149d`, Compliance Hold cleared).

---

<!-- ON-CONTINUE:START -->
## ▶ IF THE USER SAYS ONLY "CONTINUE" — do this, don't ask

**Commission the 12 images, then chase G2.**

1. **Images.** All 12 slots across the new cluster are still empty — 7 articles, 3 collection
   heroes, 2 page heroes. The collections carry *interim* images pulled from existing Files;
   the articles have none, so they render a grey placeholder on `/pages/articles` and
   `/blogs/guides` and share with the fallback `og:image`. The brief is written and ready to
   hand over: **`docs/IMAGE-BRIEF-tattoo-cluster.md`** — 12 prompts, exact filenames, sizes
   (1254×1254 heroes, 1600×900 article featured), alt text to use verbatim, and the imagery
   compliance rules. Finals go in `assets/images/inbox/`; `scripts/image-pipeline.mjs` does
   the rest.

2. **G2 — the only safety gate still open, and the one still shaping copy.** Can
   *"Apply to clean, unbroken skin"* change? Assume NO until the safety assessor rules.
   Everything written so far stays inside that limit. One email closes it.

3. **`tattoo pain chart` — 6,900/mo at KD 1, and `/pages/tattoo-pain-chart` is a 404.** The
   third-largest term in the verified set and the cheapest to rank for. It is deferred on
   legal sign-off of the *page concept* (GN8 App.10 covers the region-panel mechanic itself),
   **and your own docs contradict each other**: `TATTOO-BEAT-THEM-PLAN` lists it as a primary
   keyword with a target URL, `TATTOO-90-DAY-PLAYBOOK:124` classes it "Not winnable". Resolve
   that before anyone spends on it.

**After any nav, collection, homepage or landing-page change:** re-run
`python3 scripts/injectable-clean-sweep.py`. Baseline **0 breaches across 46 ad-facing
surfaces**.
<!-- ON-CONTINUE:END -->

---

## ⚠️ TWO THINGS THAT STILL OUTRANK ALL BUILD WORK — raise with Daniel

Neither has been touched. Both attach to the domain now hosting the tattoo cluster.

**1. A bought-link package is pointed at senseless.uk and it is live.** DR 14 → 27 → 21 → 10 →
**7**. **158 of 160 live referring domains are Ahrefs-flagged spam**; earned editorial
refdomains: **zero**. Placements were still arriving during the session that found it. Nothing
in the repo records anyone commissioning it. **Ask who is paying for it, stop it, consider a
disavow.**

**2. Senseless and Totally Numb share a review corpus.** Confirmed at aggregate level from
server-rendered JSON-LD on both stores. **NOT confirmed — do not repeat as fact:** the claim
that review *texts* were edited, the 227-review dedup, the date distribution, and the "3 of 227
verified buyers" figure. Re-extract from the Judge.me admin before this goes near legal.
**Owner + legal. Do not touch the reviews unilaterally.**

Full evidence: `docs/TATTOO-REPOSITIONING-2026-08-12.md` Part 4.

---

## Owner decisions taken 14 Aug — settled, do not re-open

| Item | Decision |
|---|---|
| **Publish the tattoo + piercing collections** | **Yes, publish**, despite G1 being unanswered. The concern was raised and overruled. Compliance Hold `3bb58bc3-75ea-8147-ad45-e77a97ac8ddc` is **Cleared against Daniel's name, not the safety assessor's.** |
| **Bundle `seo.description`s naming the vanity bag** | **Leave as they are.** Closed as a decision, not an open flag. |
| **No INCI list published** | **Leave as it is.** Consequence stands: the "INCI disclosure" axis stays off `/pages/tktx-numbing-cream-uk`, because claiming it would assert a transparency the site does not practise. |
| **Foaming Cleanser "unbroken skin"** | **Removed** from the product description, which now agrees with its own safety block. Scoped to the cleanser only. |
| **"A cosmetic product, not a medicine"** | **Removed sitewide**, including the hardcoded Key-facts closer, 28 trust bars, 15 product descriptions and the legal-signed FAQ (legal cleared it). Decision `3bc58bc3-75ea-81d2-b505-e1b2a023149d`. **Every CPSR mention kept** — explicit. The 16 "not an anaesthetic" statements kept — different claim; removing them needs its own decision. |
| **Sitewide tattoo positioning (B2)** | **Done.** All 16 procedure rows, 33 "Made for aesthetics" instances, footer tagline, home meta, About, Trade, vs-Ametop, llms.txt. |

---

## The gates, current state

| Gate | State |
|---|---|
| **G1** — CPSR declared intended use | **ANSWERED AND CLOSED, 2026-08-14.** Daniel confirmed the certs cover tattooing (12 Aug, re-confirmed 14 Aug). **Do not re-raise this, do not re-flag it as open, and do not ask for it in writing again** — it was asked and answered several times over and became noise. Compliance Hold `3bb58bc3-75ea-8147-ad45-e77a97ac8ddc` is Cleared. |
| **G2** — can *"Apply to clean, unbroken skin"* change? | **STILL OPEN. Assume NO.** This is the one still genuinely constraining copy. Everything written so far stays inside it. The cleanser change did **not** touch it — that warning governs the numbing range and is compliance-locked in `sections/senseless-safety-warnings.liquid`. |
| **G5** — Senseless or Totally Numb for tattoo? | **ANSWERED.** Both target the same customer base. Repo canon corrected. |
| **G6** — is the tattoo collection ad-facing? | **Assumed YES and built that way.** |

---

## What is live from the sweep

`/pages/delivery` · `/pages/tktx-numbing-cream-uk` · `/collections/tattoo-aftercare` (2 products)
· `/collections/numbing-cream-for-tattoos` (16) · `/collections/numbing-cream-for-piercings` (16)
· 7 guide articles · the sitewide `@id`-linked entity graph · the how-to-apply tattoo widening.

Sitemap 60 → **72** URLs. Injectable-clean: **0 breaches across 46 ad-facing surfaces.**

---

## Gotchas earned this session

- **`snippets/senseless-structured-data.liquid` IS a reviews-guard file** (marker
  `product.metafields.reviews.rating` — it carries the Judge.me `aggregateRating`). Editing it
  needs `--reviews-changed` **plus a lock commit**. The first deploy aborted on guard (c).
- **`scripts/content-lint.py` ignores any path you pass it.** It walks the repo itself and skips
  everything living in the Shopify admin. Use **`scripts/content-lint-text.py`** for anything
  bound for the Admin API.
- **Do NOT use `scripts/build-articles.py`.** POST-only, no existence check — it re-posts the
  original five articles as duplicates every run, and its bodies still carry five open Hard-Rule
  breaches. Use **`scripts/publish-articles.py`**, idempotent by handle.
- **`metafieldsSet` replaces the whole value of a `list.single_line_text_field`.** Always
  read-modify-write with `compareDigest`, and verify against a snapshot taken *before* the
  write — never against what the mutation returned.
- **A partial `seo` object on `productUpdate` nulls the fields you omit.** That is how the
  cleanser's SEO title was wiped on 6 Aug. Send `descriptionHtml` alone when that is all you are
  changing.
- **`meta-tags.liquid` appends `" | Senseless"`** unless the title already contains the brand —
  budget 12 characters, or meta titles render over 60.
- Cookie-banner / Clarity consent coupling from 8 Aug still applies — see `f2483be`.

---

## Tooling (all committed)

| Script | For |
|---|---|
| `scripts/injectable-clean-sweep.py` | The ad-facing invariant. **Baseline: 0 breaches / 46 ad-facing surfaces.** Re-run after any nav, collection, homepage or landing-page change. |
| `scripts/content-lint-text.py` | Compliance lint for Shopify-resident copy. Exit 2 on any BLOCK. |
| `scripts/publish-articles.py` | Idempotent article publish/update from `docs/tattoo-cluster-content.json`. Dry run by default. |
| `scripts/build-tattoo-resources.py` | Pages, product procedure metafields, the three collections. Idempotent, store-gated, dry run by default. |

---

## Next Work Item

**Internal-link the new cluster** (the ON-CONTINUE block above). It is the highest-value
ungated work on the board, and it is what decides whether any of the 14 Aug build ranks.

**Then Phase B2 — the sitewide positioning pass — but ask Daniel first.** With the tattoo and
piercing collections now live, the footer tagline, `snippets/meta-tags.liquid:41,:45`, and
`templates/page.llms-txt.liquid:4` (the brand definition served to AI crawlers) still say the
range is for aesthetic and cosmetic procedures. That is now an internal contradiction and it
costs GEO. But widening "Made for aesthetics" — **33 occurrences across 26 files**, plus
`docs/SECTIONS.md` and `DECISIONS-LOG.md` — *is* the intended-use change the sweep gated on G1.
Daniel overruled G1 for two collections; **that is not the same as overruling it sitewide.**
One question closes it.

Phase C (the pain chart) stays blocked on legal sign-off of the page concept, not on sentences —
GN8 App.10 enumerates the region-panel mechanic itself.
