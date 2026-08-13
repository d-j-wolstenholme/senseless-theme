# Tattoo build sweep — the executable manifest

**This is the build document. Start here.** The other three tattoo docs are evidence, not
instructions:

| Doc | What it is | When to open it |
|---|---|---|
| **`TATTOO-BUILD-SWEEP.md`** ← you are here | The ordered build. Exact paths, exact operations. | Always |
| `TATTOO-REPOSITIONING-2026-08-12.md` | Evidence base. Parts 1–4 + all verifier corrections. | When you need the *why* or a figure |
| `TATTOO-BEAT-THEM-PLAN-2026-08-12.md` | Competitor detail, target map, GEO property lists | When building a specific item |
| `TATTOO-90-DAY-PLAYBOOK-2026-08-12.md` | Channel strategy, off-SERP, paid, B2B | Post-build, for promotion |

**Do not re-run the four research strands.** They cost ~7.9M subagent tokens and are complete.

---

## Owner instruction that overrides project convention

Daniel, 2026-08-12: *"make sure the docs are set up so the next session can build all in a single
sweep."* **This deliberately overrides the `CLAUDE.md` one-task-per-session rule** for this work.
Record that in the Decisions DB at write-back. It does **not** override the verify-store gate, the
deploy rules, the reviews-guard, the injectable-clean invariant, or `compliance-check`.

---

## The shape of the sweep

Most of this work needs **no gate at all**. The gated part is *publishing tattoo-positive claims* —
not building the machinery underneath them.

**So: build everything, publish what is clear, stage what is gated.**

```
PHASE 0  Pre-flight ........................ no gate
PHASE A  Ungated build (the bulk) .......... no gate — 10 items, all shippable today
PHASE B  Staged, not published ............. built in the sweep, published when G1/G5/G6 clear
PHASE C  Blocked ........................... do not build until answered
PHASE Z  Verify + write-back ............... always
```

---

## The four gates, with defaults so the sweep is not blocked

| Gate | Question | Owner | Default if unanswered |
|---|---|---|---|
| **G1** | What does the CPSR declare as intended use / application site? Do Senseless CPSRs trace to Totally Numb's? | Safety assessor | **Build, do not publish.** Daniel's "the certs have been updated" is verbal; no written scope exists. One email may close it — if the CPSRs trace to Totally Numb formulations and TN is the tattoo brand, tattoo is likely already in scope. |
| **G2** | Can *"Apply to clean, unbroken skin"* change? | Safety assessor | **Assume NO.** Write every tattoo surface inside that limit: say nothing about broken skin or mid-session re-application. Silence is compliant; contradicting a locked warning is not. |
| **G5** | ~~Senseless or Totally Numb for the tattoo lane?~~ | — | **ANSWERED 2026-08-13 by the owner: "senseless and totally numb both target the same customer base now."** Both brands compete for the same customers deliberately. This is not a lane split and not an accident. **No longer a gate.** See "The two-brand position" below. |
| **G6** | Is the tattoo collection ad-facing? | Owner | **Assume YES.** Conservative and cannot be wrong: it means zero links to the three injectable collections. Costs nothing if the answer turns out to be "organic". |

**Two items outrank the entire build** and belong in the same conversation: the **bought-link
package** and the **shared review corpus**. Neither blocks Phase A. Both attach to the domain that
would host the tattoo pages. See `NEXT_SESSION.md`.

## The two-brand position (owner ruling, 2026-08-13)

> *"senseless and totally numb both target the same customer base now."*

Senseless and Totally Numb are **deliberately competing for the same customers**. Every reference in
these docs to "group-internal cannibalisation" as a *risk* is superseded — it is the intent. Act
accordingly:

- **"Beat Totally Numb" is literal.** The pain chart, the collection and the guides should out-perform
  theirs on merit. No pulled punches, no deference.
- **The repo canon is now wrong and must be corrected at write-back.**
  `build-reports/phase-6-close-does-it-hurt-by-treatment.md:24` says *"no tattoo content (excluded per
  spec — Totally Numb's lane)"*, and `docs/AUDIT-2026-06-12.md:31,:114` logs the lane as an open
  question. Both are superseded by this ruling.
- **The handle argument weakens but the answer holds.** "Avoid two MHG stores on identical paths" was
  already the weaker half of the case, and slug construction is measurably irrelevant here anyway.
  `numbing-cream-for-tattoos` stands on sibling consistency alone.

**Three things this ruling does NOT dissolve, because none of them are cannibalisation problems:**

1. **The claim-set asymmetry is a regulatory exposure, not a commercial one.** Under company
   **17099304** / VAT **GB 523 7816 82**, Totally Numb publishes onset (*"begins to take effect within
   30–45 minutes"*), duration (*"typically lasts between 1–3 hours"*), comparative efficacy and
   mechanism of action (*"reducing nerve signal transmission… the result is reduced or absent
   sensation"*) — plus a duration claim in a practitioner testimonial on a **paid** landing page.
   Senseless is forbidden every one of these in every voice. Two brands, one legal entity, one
   customer base, two claim sets. If a regulator looks at either brand it reaches the same company.
   **This is for the owner and MHG legal — it is not a Senseless copy decision and nothing in this
   sweep changes it.**
2. **Paid self-competition is a real cost whatever the strategy.** Totally Numb runs 53 ads with
   *"tattoo numbing cream"* as its top paid keyword, $1,161/mo. Senseless bidding the same term means
   one entity in both sides of the auction, lifting the group's own blended CPC. That is a budget
   decision, not a compliance one — but it should be made on purpose.
3. **The shared review corpus gets *more* material, not less.** If both brands sell to the same
   customers, the same review set appearing under both with different product names is more likely to
   be noticed, not less. Aggregate match is confirmed; the alleged text edits still need re-extracting
   from the Judge.me admin.

---

## Decisions already resolved — do not re-litigate

| Question | Ruling | Source |
|---|---|---|
| One tattoo collection or several? | **ONE.** "tattoo numbing cream" and "numbing cream for tattoos" return the same SERP — identical AI Overview, same nine sources. Format terms become *sections inside it*. | Evidence doc Part 1 |
| Which handle? | **`/collections/numbing-cream-for-tattoos`** — but see "The slug question is settled" below. The deciding fact is that **slug construction has no measurable effect in this SERP**, so the choice falls to IA consistency and group-collision avoidance by default. | Measured, see below |
| Interactive pain chart or static? | **Both — but the static graphic is the linkable artefact.** Healthline's static PNG: 263 refdomains. Every interactive chart measured: 0. Position 1 on the head term is a 12-slot image pack. | Evidence doc Part 3 |
| Numeric pain scale? | **No.** Qualitative bands only — reuse **Mild · Moderate · Sharper** from `senseless-comfort-compare.liquid:4-5`. Locked 2 June decision de-scoped numeric. | Part 3 |
| Region → product mapping on the chart? | **Banned. No compliant version exists.** GN8 App.10 enumerates "lists… which take a consumer to a page **displaying** a product when selected" — "displaying", not "linking". | Part 3 |
| Cite the research as the differentiator? | **No.** GN8 §4/App.10 list publishing clinical data as an implied medicinal claim on a selling domain. | Part 3 |
| Tattoo terms on PDPs? | **No.** Breaches the 7 Aug collection-carries-category-keywords ruling. | Part 4 |
| Re-slug `/pages/aesthetic-procedures`? | **No.** 20 internal links across 18 files, indexed URLs. Widen copy, add a destination. | Part 2 |
| A separate GEO programme? | **No.** KD 0–1 and the AI-cited pages are the same pages. One asset wins both. | Part 4 |

---

## The slug question is settled — and the answer is "it doesn't matter"

The owner challenged the handle recommendation on the grounds that it should be decided with Ahrefs,
not with naming-pattern reasoning. He was right, and the measurement inverted the reasoning.

`batch-analysis`, country=gb, mode=exact, 2026-08-12:

| URL path | Slug vs head term | DR | Refdomains | Organic KWs | GB traffic/mo | Value/mo |
|---|---|---|---|---|---|---|
| `tattoonumbx.com/products/tattoonumbx-numbing-cream` | PARTIAL (brand token) | 11 | 24 | 46 | **2,679** | $2,680.83 |
| `superdrug.com/emla/b/404041` | **NONE — a numeric ID** | 77 | 1 | 105 | **2,489** | $1,892.55 |
| `tattoonumbingcream.com/en-gb` | NONE — locale homepage | 40 | 3 | 53 | 1,615 | $1,553.48 |
| `emla.co.uk/emla-for-tattoos/` | **FOR-X reordered** | 22 | 5 | 84 | 1,208 | $845.96 |
| `inkkingztattoostudio.co.uk/product/extreme-numbing-cream/` | PARTIAL — no "tattoo" at all | **0.1** | **0** | 50 | 1,096 | $952.85 |
| `totally-numb.com/collections/tattoo-numbing-cream` | **EXACT MATCH** | 30 | 0 | **4** | **38** | **$23.31** |
| `senseless.uk/collections/aesthetic-numbing-cream` | — (our best-linked collection) | 7 | 3 | **0** | **0** | $0 |
| `senseless.uk/collections/numbing-cream-for-microneedling` | — (our sibling pattern) | 7 | 0 | **0** | **0** | $0 |

**Three conclusions:**

1. **The exact-match slug is the worst performer in the set.** A perfect match on a 10,000/mo, KD-0
   term earns 38 visits and 4 keywords. A URL made of a numeric ID earns **65× more**.
2. **The Totally Numb "collision" is notional, not real.** That URL is *built*, not *occupied* —
   38 visits, 4 keywords, 0 backlinks. It is a brand and ads-auction consideration, not a ranking
   one. An earlier note in this project overstated it.
3. **The closest structural analogue favours the for-X form anyway.** `emla-for-tattoos/` — a for-X
   path that does *not* match the head-term word order — earns 1,208 visits on 84 keywords from
   **5 referring domains**, and holds position 1 on several tattoo terms phrased the other way round.

**Therefore: do not spend time on the handle.** Pick `numbing-cream-for-tattoos` for sibling
consistency and move on. What the table actually shows is that **page-level referring domains and
on-topic depth decide these SERPs** — a DR 0.1 studio page with zero links still takes 1,096 visits
because it exists and is on-topic. Senseless's two existing collections take **zero** because
nothing points at them and nothing ranks.

A workflow to quantify the null result systematically (slug-class correlation across 10 SERPs × top
10) was started and **deliberately stopped** — the eight-point sample is decisive and a larger one
would only confirm it. Do not spend Ahrefs units re-running it.

---

# PHASE 0 — Pre-flight

1. `scripts/reconcile.sh` — confirm machine, `main` clean and level with origin.
2. **Verify-store gate.** `bash ./scripts/refresh-token.sh`, then confirm
   `myshopify_domain == senseless-numbing.myshopify.com`. The CLI default is **Totally Numb** —
   mismatch means STOP. This is the one rule that never relaxes.
3. `subscription-info-limits-and-usage` — Ahrefs was at ~105k/400k units; resets **2026-09-09**.
4. **Capture the injectable-clean baseline: 0 breaches across 14 live surfaces.** You must re-run the
   identical set in Phase Z. Any breach afterwards is attributable to this work.
5. Note `f940b05` is already **deployed and live-verified** — do not re-deploy it.

---

# PHASE A — Ungated build

Nothing here needs an answer from anyone. Ship it.

### A1 · `/pages/delivery` — net-new, zero compliance surface
`/pages/delivery`, `/pages/shipping`, `/pages/shipping-returns`, `/pages/delivery-returns` **all
404**; only `/policies/shipping-policy` exists and it is **not in the sitemap**. TattooNumbx holds
**#1** for "tattoo numbing cream next day delivery" (250/mo) with a page carrying **0 backlinks** —
and the repo record notes that page returns 404.
- Target `numbing cream next day delivery` (200, KD 0). No tattoo word yet — widen in Phase B.
- Link from footer + the PDP shipping accordion. Add to sitemap.

### A2 · GEO batch 1 — the entity graph
Senseless already emits **more schema than every competitor** and is cited twice. Coverage is not the
gap. These four are:
- `@graph` with `@id` linkage; `Organization` on every page type (currently **2 of 9**).
- Product-level `sku`, `gtin`, `identifier`; INCI deferred to A10.
- Default `WebPage` node — **11 of 26 templates emit none**, including all three ad-facing landing
  pages.
- `sameAs` — leave as a stub; no social profiles exist yet (see A9).

Property lists are in `TATTOO-BEAT-THEM-PLAN-2026-08-12.md` §6. No copy, no claims, zero compliance
surface.

### A3 · GEO batch 2 — the extraction surface
Across 9 live pages: **0 `<table>`, 0 `<time>`, 0 author markers**, and FAQ questions render inside
`<summary>` instead of headings.
- `<summary>` → `<h3>`; `dateModified` + `<time datetime>`; named `Person` author; `ItemList.item`;
  collection description truncate **300 → 1200**.
- **Why this matters more than schema:** Emla is the most-cited domain in the category (ChatGPT 51,
  AI Mode 68, AI Overviews 41) with **zero FAQPage, Product, Review or HowTo schema** — purely
  question-shaped headings and direct prose. And of Tattoo Numbing Cream Co's 245 ChatGPT citations,
  **142 come from `/blogs/` and zero from `/products/`.**

### A4 · Tattoo collection scaffolding — built, created UNPUBLISHED
**Order is not optional.** A collection created before its template renders as a stock Horizon grid
on a live URL.
1. Clone `templates/collection.numbing-cream-for-microneedling.json` (10 sections, injectable-clean,
   links only to `/pages/aesthetic-procedures`, a does-it-hurt guide, and
   `/pages/the-senseless-system#selector`) → `templates/collection.numbing-cream-for-tattoos.json`.
   **Never clone the Botox template** — different shape, cross-links the injectables.
2. Deploy the template.
3. `metafieldsSet` — add `"Tattooing"` to `senseless.recommended_procedures` (definition
   `429332955484`, `list.single_line_text_field`, no validations). **Close the 7-product gap in the
   same pass**: the Foaming Cleanser, the A&D ointment and **all 5 bundles** carry no procedure
   metafield, so a rule-driven collection silently drops the highest-AOV items.
4. Create the smart collection **unpublished**. Rule: metafield equals `Tattooing`.
5. **Do not point it at `/pages/does-it-hurt-by-treatment`** — that page links all three injectable
   collections. Give tattoo its own guide instead (A7).

The metafield renders nowhere in the theme (`rg -n "recommended_procedures"` → 0 hits in
`templates/`, `sections/`, `snippets/`), so this step cannot leak an injectable link.

### A5 · Tattoo aftercare cluster — the best risk-adjusted item on the list
**9,700/mo GB at KD 2**, traffic potential 6,400, plus "tattoo aftercare cream" 1,400. **No page
exists anywhere on the site.** Washing, moisturising and healing never touch the anaesthetic line.
- 1 collection + 2 guides: *Tattoo Aftercare UK* · *Tattoo Aftercare: The First 48 Hours* ·
  *Tattoo Healing Stages, Day by Day*.
- Merchandise the **Foaming Cleanser 35ml** and the **Vitamin A&D ointment 4-pack** — both already in
  range. The Notion Pages DB row for the ointment **already targets "tattoo aftercare ointment"**.
- Compliance: **clear.**

### A6 · Widen `/pages/how-to-apply-numbing-cream`
The only template with `"emit_howto": true` (`:64`). It already has cream/spray/gel step blocks, a
"By procedure" band and 7 FAQs.
- Add a tattoo row, a tattoo FAQ, a tattoo HowTo step.
- **Uniquely permitted:** Decision `39158bc3-75ea-8181` allows concrete timing framed as directions
  for use **on application-guide surfaces**. Use *"as a general guide, allow 45–60 minutes… your
  **artist's** window takes precedence."*
- **Do not migrate that timing to a PDP direction block** — needs its own decision.

### A7 · Objection Q&A cluster — 5 blog articles
Blog articles auto-list in the Articles hub (`senseless-articles-hub.liquid:65`); guide *pages* need
a manual block plus a deploy. Blog is cheaper. All five are answerable from formulation, safety and
etiquette fact — **no effect claim required**.
1. **Does Numbing Cream Affect a Tattoo?** ← best item on the list: it is the question the *artist*
   asks, and no competitor answers it properly
2. Can You Use Numbing Cream Before a Tattoo?
3. Do Tattoo Artists Use Numbing Cream? ← the only search-visible door into the artist conversation
4. Where to Buy Numbing Cream for Tattoos in the UK
5. What to Tell Your Artist About Numbing Cream ← zero competitor coverage

FAQPage on each. Verdict-first answers — that shape is what gets cited.

### A8 · Piercings collection
`numbing cream for piercings` — **450/mo, KD 0, traffic potential 19,000**, the highest TP of any
single term measured. Missing 9th procedure collection, same studio audience, no tattoo gate.

### A9 · TKTX comparison page
`tktx numbing cream` **6,600/mo, KD 17** — the real category incumbent, and it was not among the
three competitors named. Match the `/pages/best-emla-alternative-uk` pattern. Compare **only** on:
UK CPSR assessment, INCI disclosure, registered UK company, format range, pack sizes, price per gram,
delivery. **Never on how well it works.**

### A10 · Canon and doc fixes
- `docs/BRAND.md:3` — points at an **archive-sealed** Notion page as its source of truth. Same fault
  class fixed for `DECISIONS-LOG.md` in `bf891e6`.
- `docs/ARCHITECTURE.md:63` — claims old tattoo URLs "will have" been redirected. **Never happened
  and could not have.** Delete the sentence.
- `.claude/skills/redirects/SKILL.md:17-18` — worked example uses `/collections/tattoo-numbing-cream`
  as a from-path. **That is a live Totally Numb URL.** Fix before someone actions it literally.
- `.claude/skills/seo-meta/SKILL.md:45-46` — bakes the aesthetics meta pattern.
- `README.md:3`, `package.json:4` — "UK aesthetics-focused".
- **BRAND.md drift, verified:** `:27` says `--text-muted #8E8A82`; the live token is **`#6E6A63`**.
  The brand asterisk strokes **`#984AE8`**, not `#6B3FA0`, despite `:104`.

---

# PHASE B — Built in the sweep, published only when gates clear

Write it, `compliance-check` it, commit it, **hold the publish**.

### B1 · Publish the tattoo collection — needs G1 + G5 + G6
Copy pass, `compliance-check`, publish, then **re-run the 14-surface injectable-clean sweep**.
Category noun in slug/title/meta only; the H1 must not use "numbing" as an effect.
Working title: `Tattoo Numbing Cream UK — Three Strengths | Senseless` (mirrors the live
`Numbing Cream UK — Three Strengths | Senseless`).
Format terms live as **sections inside this page**: "tattoo numbing spray" (400, KD 0) and "tattoo
numbing gel" (100, KD 0, TP 4,100) both carry the parent topic "tattoo numbing cream". Worth noting:
**no top-10 result for "tattoo numbing gel" is actually about a gel**, and Senseless ships real gels
and a real spray while GetNumbd's spray URL 404s and TNC sells no gel.

### B2 · Sitewide positioning pass — needs G1
**Widening "Made for aesthetics" *is* the intended-use change.** That is why this cannot go first.
- `sections/senseless-footer.liquid:210` — tagline **default**, renders on every page
- **"Made for aesthetics" — 33 occurrences across 28 files**, triple-homed in `docs/SECTIONS.md:15`,
  `DECISIONS-LOG.md:125` and Notion Confirmed Fact `38e58bc3-75ea-8109-a8b6-fbb8b2df9d2b`. All four
  must move together.
- `snippets/meta-tags.liquid:41, :45` — the only meta the repo controls
- `templates/page.llms-txt.liquid:4` — the brand definition served to AI crawlers. Highest GEO
  leverage per character on the site.
- `templates/page.trade.json:85` — **currently routes non-aesthetic practices to Emla or Ametop.** A
  tattoo studio is not an aesthetic clinic; this page sends the exact B2B buyer this pivot targets to
  a competitor.
- `templates/page.senseless-vs-ametop.json:44`, `templates/page.about.json:8`
- **DO NOT TOUCH:** `sections/senseless-comfort-compare.liquid:22` (*"It is a cosmetic preparation,
  not an anaesthetic"*) — that line is what keeps the product on the cosmetic side of the MHRA line.
  `templates/page.faq.json` is legal-signed; it goes back to legal separately.

### B3 · The two tattoo FAQ deflections — needs G1
`templates/collection.aesthetic-numbing-cream.json:282` and
`templates/page.strongest-numbing-cream.json:177`. **These two fields are the site's only tattoo
signal and both currently read as "no".** One field each — the cheapest edit on the site. But the
answer is an intended-use statement inside the CPSR envelope, so it is gated on G1, not on a
`compliance-check` pass.

### B4 · Widen the two refusal pages — needs G1
`/pages/does-numbing-cream-work` and `/pages/how-long-numbing-cream-lasts` already rank on a question
and answer it with a framework. Tattoo-qualified variants are the **only** mechanism that converts
the banned ~650/mo into something we can honestly compete for.

### B5 · Widen `/pages/aesthetic-procedures` — needs G6, blocked on a block cap
Adding a Tattooing card is what connects the new collection to the procedure axis. But
`senseless-trio-card-row` is at `max_blocks: 4` and **full**, and that component is used by 24
sections across 15 templates — raising the cap has a blast radius and needs a regression check on the
columns CSS (only 2/3/4 grids exist). `/pages/does-it-hurt` `senseless-link-row` is at **8/8** with
two more rows at 7/8.
Same phase: the header's **four** hardcoded procedure lists
(`sections/senseless-header.liquid:416-420, 482-486, 596-600, 627-630`) and the Selector string
(`senseless-selector.liquid:62`) — which must move **in lockstep** with the four suitability matrices
(`page.the-senseless-system.json`, `page.choosing-your-strength.json`,
`page.choosing-your-format.json`, `templates/product.json`). Needs a product call: format, base
strength, ceiling and honest note for tattooing.

---

# PHASE C — Do not build until answered

### C1 · The unbroken-skin resolution — G2
`sections/senseless-safety-warnings.liquid:22` — *"Apply to clean, unbroken skin."* Hardcoded and
deliberately non-editable, covering **9 SKUs + 5 kit PDPs**, and duplicated in Admin `body_html` on
**10 of 16 products**, so a theme-only fix leaves it live. Either the assessor changes it, or it
stays and **every tattoo page is written inside that limit**.
Close the related defect in the same pass: three collection FAQs say *"Take extra care on sensitive
or broken skin"* on the same page as the locked warning
(`docs/SITE-ASSESSMENT-2026-08-06.md:295`).

### C2 · Tattoo pain chart — needs legal sign-off on the *page concept*
Not a `compliance-check` on sentences — a sign-off on the concept, because GN8 App.10 enumerates the
region-panel mechanic itself.
- **Static graphic first** — that is the linkable, rankable artefact and the image-pack entry.
  Gender toggle (`tattoo pain chart female` = 900/mo, so it is a ranking feature).
  **Mild · Moderate · Sharper** bands. Neutral line-art, brand palette, **no red heat-map, no wincing
  figure** (GN8 App.10 bans imagery showing "apparent areas of pain").
- **Interactive tool second**, on the `sections/senseless-selector.liquid` pattern: native radios in
  a `fieldset`/`legend` so the DOM *is* the state, one inline IIFE scoped by
  `document.currentScript.closest()`, ES5, no framework, no build step.
- **Watch the undocumented 25-character schema `name` cap.** `Senseless — Comfort map` fits at 23.
- **Beat Totally Numb on what it fails:** their bands are colour-only (`aria-label="Rib cage"` carries
  no sensitivity information); contrast is **1.31:1 and 1.12:1** against WCAG 1.4.11's 3:1; a dead CSS
  rule means the active Front/Back tab never highlights (`[aria-selected=true]` styled, `aria-pressed`
  set); tap targets fail WCAG 2.5.8; and **with JS off the back of the body is unreachable**.
- URL: `/pages/tattoo-pain-chart`. **Never** `/collections/tattoo-pain-relief` — GN8 App.10 warns
  against categories referring to adverse medical conditions. No reviews module on the page.

---

# PHASE Z — Verify, then write back

Per `.claude/rules/deploy-and-store.md`, in this order, every time:

1. `theme-check` → **0 errors**. Never chain a deploy to an ungated check — a comment inside a liquid
   tag shipped a syntax error live on 6 Aug.
2. **Commit → push → THEN deploy.** Deploying first opens a window where live is ahead of the repo.
3. **Run `deploy.sh` under `bash`.** zsh does not word-split, so `./scripts/deploy.sh $FILES` passes
   every path as one `--only` argument, reports "success" and pushes **nothing**.
4. **Asset-API per-file diff** — the only thing that catches a false success. `deploy.sh`'s exit code
   does not. Strip the leading `/* */` header and normalise `\/` before comparing JSON.
5. **Reviews-guard** — Judge.me markers must survive. Editing a review file needs `--reviews-changed`
   plus a lock commit.
6. **Re-run the 14-surface injectable-clean sweep** against the Phase 0 baseline of **0 breaches**.
7. Live curl with `?_fd=0` (never `?cb=`), several URLs, varied UA — the edge cache is per URL.
8. **Notion write-back.** The State Surface (`38e58bc3-75ea-81ad-87eb-e20fcfc22406`) and Decisions DB
   (`d5ce9514-257c-4e02-aced-acba800e89d9`) currently have **no record of this brand change**.
   Log a Decisions row capturing **both** the 21 May aesthetics-only position **and** its reversal —
   there is no predecessor row to supersede. Raise a **Compliance Hold** on the tattoo keyword set
   (precedent: the Applied EMLA hold, `3b158bc3-75ea-8183-ae67-c6d305610682`). And note Notion
   `35e58bc3-75ea-8148-b0c3-cf9d2fa53e3a` (21 May, *"NOT for tattooing"*) sits in the **Matrix Health
   Group** tree — a Senseless write-back will not sweep it.
9. Rewrite `NEXT_SESSION.md`.

---

## Copy rules — apply to every string in this sweep

**Banned in every voice, including customer, artist and influencer:** numbs · anaesthetic · pain
relief · pain-free · painless · blocks/reduces sensation · works in X minutes · lasts X hours ·
X% effective · strongest · as strong as Emla · desensitise · nerve deadener/blocker/vasoconstrictor ·
completely safe. Percentage-strength positioning is out. `benzocaine` and `lidocaine cream` are
permanently out as targets.

**Constrained — rank on it, then decline it:** "best" and "strongest" are permitted in
slug/title/meta only. Live precedent on both group stores. **Using either as backlink anchor text
needs Daniel's written sign-off — and the trap has already sprung:** `strongest numbing cream` is
already an inbound anchor on 2 referring domains, first seen 2026-07-16, unsigned-off.

**The positioning that only Senseless can hold:** every competitor answers *"does tattoo numbing
cream work?"* with a claim. Senseless is the only brand structurally obliged to answer with a
**framework** — and framework answers are what AI Overviews cite. The AI Overview holds **position 1
on both commercial head terms, above Amazon**. The constraint is the differentiator.

Run `compliance-check` before any user-facing string ships. It is non-negotiable.
