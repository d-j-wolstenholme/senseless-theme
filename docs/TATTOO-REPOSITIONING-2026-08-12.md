# Tattoo repositioning — research record (2026-08-12)

**Status: RESEARCH ONLY. Nothing edited, committed, deployed or written back to Notion.**
Machine: MacBook Pro. `main` @ `f940b05`, clean, level with origin.

## What triggered this

Daniel, 2026-08-12: *"Drastic changes to Senseless as a brand incoming. All products are now
formulated for tattooing application, as well as the original applications."* Follow-ups: all site
content, SEO and **GEO** must reflect it to customers and bots; beat `getnumbd.com`,
`totally-numb.com` and "Tattoo Numbing Co"; add **tattoo pain guides** and an **interactive pain
chart / body diagram** better than Totally Numb's; *"senseless is new so it needs to outperform them
to gain traction"*; new tattoo collections needed for SEO.

Asked whether the CPSR now covers tattooing, Daniel confirmed: **"yeah the certs have been updated."**
See G1 below for why that confirmation still needs a written scope.

Four research strands were run (read-only, multi-agent, each with an adversarial verifier).
This document records **strand 1 (blast radius)** plus **first-party Ahrefs research**.
Strands 2–4 (competitor teardown, challenger playbook, pain-chart spec) append below when complete.

---

## Part 1 — Ahrefs, gathered first-party

Country GB, August 2026. Tool + params recorded against each table in the session transcript.

### Correction to the record

The **14,800/mo** for "tattoo numbing cream" in the `f940b05` commit body is **wrong for Ahrefs GB**.
Correct GB volume is **10,000/mo**; the 24-month GB range is 8,540–11,764 and never approached
14,800. That number is a standard Google Keyword Planner bucket, so the source was almost certainly
Keyword Planner, not Ahrefs. Global is 51,000.

### The clusters

| Cluster | ~UK vol/mo | KD | Notes |
|---|---|---|---|
| Commercial ("tattoo numbing cream" and variants) | ~20,400 | 0–1 | Head term 10,000 at **KD 0** |
| Pain chart / pain scale | ~10,600 | 0–6 | "tattoo pain chart" **6,900 at KD 1**, global 60,000 |
| Body-part pain + "does X hurt" | ~4,200 | 0–4 | ~50 terms, 40–150 each |
| **Tattoo aftercare** | **9,700** | **2** | Traffic potential 6,400. No page exists. |

Sums of terms pulled, not deduplicated traffic forecasts.

A wider 61-term sweep put the **cluster floor at ~25,930/mo GB**, of which ~1,290/mo is
competitor-branded or local (TKTX 450, "boots" 200, "near me" 300, "emla tattoo numbing cream" 80,
"superdrug" 60) — **net addressable ≈ 23,930/mo**.

### The compliance ceiling — corrected, and it is not only about volume

~**650/mo** cannot be served compliantly at all: "how long does tattoo numbing cream last" (200),
"does tattoo numbing cream work" (150), "long lasting…" (90), "painless…" (80), "8 hour…" (60).
Each asks for a banned claim class.

By volume that is ~2.5% of the cluster — small. **But volume understates the cost.** Competitors on
this SERP state onset and duration in hours. Senseless cannot, in any voice. Expect to lose on CTR
and dwell **even where we rank**. That should be accepted up front, not discovered later as
underperformance. (An earlier in-session note put the unaddressable slice at ~260/mo and framed the
constraint as near-costless; that figure came from a narrower pull and the framing was too
optimistic on both counts.)

### The head-term SERPs — "tattoo numbing cream" vs "numbing cream for tattoos"

**They are the same SERP.** Identical AI Overview with the same nine sources; Amazon #2,
TattooNumbx #4, Superdrug/Emla, `tattoonumbingcream.com`, Valhalla in both. Ahrefs assigns them
different parent topics — that is a modelling artefact. **One collection, not two.**

### Page-level strength — this SERP is soft

| Term | Position | Site | DR | Refdomains to URL | Traffic |
|---|---|---|---|---|---|
| tattoo numbing cream | 4 | tattoonumbx.com | 11 | 24 | 2,422 |
| tattoo numbing cream | 5 | tattoonumbingcream.com | 40 | 3 | 1,492 |
| tattoo numbing cream | 8 | inkkingztattoostudio.co.uk | **0** | — | 1,038 |
| tattoo pain chart | 3 | healthline.com | 92 | 263 | 2,915 |
| tattoo pain chart | 8 | vessoart.com | **3** | — | 94 |
| tattoo pain chart | 10 | stretchitbodyjewellery.co.uk | 38 | **1** | 587 |

Only Healthline has a real link profile. Everything else is Reddit, Instagram reels and tattoo-studio
Shopify blogs on single-digit links. Senseless is **DR 7** — this is enterable without authority.

### Two structural findings

1. **The AI Overview owns position 1 on both commercial head terms — above Amazon.** Its nine cited
   sources include `valhallastudio.co.uk` (**DR 0**) and a single product page from INK'D London.
   Low-authority pages are being cited on a 10,000/mo commercial term. Strongest available evidence
   that GEO is the fast lane for a new brand.
2. **Position 1 on "tattoo pain chart" is an image pack.** An interactive SVG will not appear there.
   The chart must also ship a properly named, alt-texted, indexable raster image or the top slot goes
   to studio blogs by default.

### Competitors surfaced by the data

- **"Tattoo Numbing Cream Co." = `tattoonumbingcream.com`** — almost certainly the "Tattoo Numbing
  Co" named by Daniel. DR 40, **3 referring domains**, ~1,492 traffic. Not a fortress.
- **"No Tattoo Pain" is a brand, not a phrase** — 150/mo on the name plus "no tattoo pain reviews"
  and "no tattoo pain numbing cream". Was not on the original list.
- **Emla is the real incumbent** — cited twice in the AI Overview, ranking via Superdrug and Boots.
  Senseless already has `/pages/best-emla-alternative-uk` and `/pages/senseless-vs-ametop`; they are
  aimed at the right competitor but not yet at the tattoo audience.

---

## Part 2 — Blast radius (strand 1, 8 agents, complete)

Store gate passed on every Admin-API sweep (`myshopify_domain = senseless-numbing.myshopify.com`).

### The headline

1. The site is no longer anti-tattoo — `f940b05` fixed that and it is confirmed live. "Tattoo"
   appears in exactly **2 lines** of shipping code, both FAQ *questions*, both answers neutral.
2. The obstacle is **aesthetics-only positioning**: 204 lines in `templates/`, 8 in `sections/`, 4 in
   `snippets/`, plus every PDP description and page SEO field in Admin, plus two URLs.
3. **The copy cannot go first.** Widening "Made for aesthetics" *is* the intended-use change.

### The gates

**G1 — What does the CPSR actually declare?** Daniel has confirmed the certificates are updated. What
is not recorded anywhere is the **declared scope**: no application site, no exposure assumption, no
target population. `rg -in "intended use"` returns nothing relevant. The only prior record is a
verbal Notion Confirmed Fact (`39158bc3-75ea-813b`, 2 Jul). Note `DECISIONS-LOG.md:119` — original
coverage was *assumed* from Totally Numb's certifications before being confirmed. **Possible fast
win:** if Senseless CPSRs trace to Totally Numb formulations and Totally Numb is the tattoo brand,
tattoo may already be squarely in scope. One email could close this.

**G2 — The unbroken-skin conflict (new; not previously raised).** The locked PDP safety block reads
**"Apply to clean, unbroken skin."** — `sections/senseless-safety-warnings.liquid:22`, the numbing
variant, covering **9 cream/gel/spray SKUs + 5 kit PDPs**. It is deliberately hardcoded and
non-editable so warnings always render as approved. Tattooing is the deliberate breaking of skin, and
the category norm — already published by Totally Numb — is re-application **during** the session onto
open skin. The same restriction is duplicated in Admin product copy (`docs/product-descriptions.json`,
in 10 of 16 `body_html`), so a theme-only fix would leave it live. Related open defect: three
collection FAQs say *"Take extra care on sensitive or broken skin"* on the same page as the locked
warning (`docs/SITE-ASSESSMENT-2026-08-06.md:295`).

**G3 — Does tattoo presentation reopen medicines classification?** The MHRA gate was closed *on the
product as presented* (Decision `39158bc3-75ea-8194`). Tattoo search intent **is pain intent**; the
same words carry more medicinal weight in a tattoo context.

**G4 — MHRA "Guidance Note 8" is unsourced.** The claim exists in **one place only**: the `f940b05`
commit body. A search of the working tree, `git log --all --grep` and `git grep` across 200 revisions
found **zero** other occurrences. It is in no rules file and no doc, so a future session will not see
it. Note the direction: as written it makes affirmative tattoo marketing **higher** risk, not lower —
it was used to justify silence and cannot also justify the opposite. Nothing is lost by treating it
as unsourced, because the Hard Rules already ban that presentation for every procedure.

**G5 — Senseless or Totally Numb? (the big one).** `totally-numb.com` has **720 live backlinks / 540
referring domains** and already ranks GB: "numbing cream for tattoos" pos 27, "tattoo numbing cream
uk" pos 29, "strongest tattoo numbing cream" pos 8 — and
**`https://totally-numb.com/collections/tattoo-numbing-cream` is live and returns 200**. The exact
collection proposed for Senseless already exists on the sister brand. (`totally-numb.co.uk` is a 301
shell with 6 backlinks — an earlier sweep queried it and wrongly concluded the lane was unclaimed.)
Repo canon assigns the lane away: `build-reports/phase-6-close-does-it-hurt-by-treatment.md:24`
*"no tattoo content (excluded per spec — Totally Numb's lane)"*; `docs/AUDIT-2026-06-12.md:31, :114`
records it as **still open**. Going tattoo-positive puts two Matrix Health Group brands in one SERP
and one ads account, with two claim sets from one legal entity — an **ASA consistency exposure**, not
just a commercial one.

**G6 — Ad-facing or organic-only?** Every sweep hit this; none could answer it. It decides internal
linking, injectable-cluster contact, and whether Google Ads healthcare policy applies to the
destination. `.claude/rules/ad-facing.md` lists *every procedure collection* as ad-facing, so a
tattoo collection built on the procedure pattern inherits that by default.

**G7 — No Compliance Hold was raised.** The Holds DB has exactly 2 rows, neither mentioning tattoo.
Direct precedent exists: row `3b158bc3-75ea-8183-ae67-c6d305610682`, Status **Applied**, 2026-08-03 —
an EMLA keyword target restricted on MHRA/ASA grounds. The process that exists for this decision was
never run.

**G8 — The naming frame.** The whole procedure axis is named *aesthetic*
(`/pages/aesthetic-procedures`, `/collections/aesthetic-numbing-cream`, hero *"Aesthetic
Procedures"*). Tattooing does not fit inside it. Options: (a) widen and 301 — costs 20 internal links
across 18 files; (b) parallel tattoo lane; (c) fold in — free but incoherent. Recommendation: do
**not** re-slug indexed URLs; widen copy and add a tattoo destination.

### What is being reversed

Not "remove an exclusion" — `f940b05` already did that. What is being reversed is **the declared
intended use of a CPSR-assessed cosmetic product.**

Earliest dated statement, 21 May 2026, Notion `35e58bc3-75ea-8148-b0c3-cf9d2fa53e3a`: *"Senseless is
now positioned as an aesthetics-only numbing brand. NOT for tattooing."* This page sits in the
**Matrix Health Group** tree, not Senseless — a Senseless write-back will not sweep it.
**There is no decision row to supersede**: the live Decisions DB (37 rows) and `DECISIONS-LOG.md`
contain zero decisions about tattooing.

**Both original reasons still stand.** (1) The lane was given to Totally Numb — which now has 720
backlinks there. (2) The SERP demands claims a CPSR-assessed cosmetic cannot make.

### Change map — headline items

**Sitewide (highest reach per character):**
- Footer tagline, a section **default**, renders on every page — `sections/senseless-footer.liquid:210`
- **"Made for aesthetics" — 33 occurrences across 26 files**; triple-homed in `docs/SECTIONS.md:15`,
  `DECISIONS-LOG.md:125` and Notion Confirmed Fact `38e58bc3-75ea-8109-a8b6-fbb8b2df9d2b`
- Homepage meta title + description — `snippets/meta-tags.liquid:41, :45`
- `templates/page.llms-txt.liquid:4` — the brand definition served to AI crawlers. Disproportionate
  GEO leverage per character.

**Active refusals still live:**
- `templates/page.trade.json:85` — tells non-aesthetic practices *"Senseless isn't formulated for
  that context — Emla, Ametop, or another medical preparation is the right product."* A tattoo studio
  is not an aesthetic clinic; this currently sends the exact B2B buyer this pivot targets to a
  competitor.
- `templates/page.senseless-vs-ametop.json:44` — closed list, *"the aesthetic catalogue"*.
- `templates/page.about.json:8` — *"Aesthetics is the specialism — not the side category."*

**Do NOT touch:** the compliance-safety layer. `sections/senseless-comfort-compare.liquid:22` (*"It is
a cosmetic preparation, not an anaesthetic"*) is what keeps the product on the cosmetic side of the
MHRA line. `templates/page.faq.json` is legal-signed and goes back to legal separately.

**Already tattoo-native — leave alone:** the review corpus. `professional-strength-cream` (207
reviews) includes *"I just got my neck done, 4 hour the cream was amazing"*;
`clinical-strength-cream` includes *"used it for a leg piece"* and *"lasted my whole 7 hour
procedure"*. Legal already ruled published reviews stay as-is. **The tattoo audience is already
buying.**

### IA — how a tattoo collection actually gets built

- **Cheapest lever in the project:** product metafield `senseless.recommended_procedures`
  (definition `429332955484`, `list.single_line_text_field`, no validations). Six values in use.
  Adding **"Tattooing"** needs no schema change — just `metafieldsSet`.
- **It is safe:** the metafield renders nowhere in the theme (`rg -n "recommended_procedures"` → zero
  hits in `templates/`, `sections/`, `snippets/`), so extending it cannot leak an injectable link.
- **Gap:** 7 of 16 products carry **no** procedure metafield — the Foaming Cleanser, the A&D ointment
  and **all 5 bundles**. A metafield-driven tattoo collection would silently exclude the highest-AOV
  products, and the ones a multi-session tattoo client most needs.
- **Template first, or it renders as stock Horizon.** Clone
  `templates/collection.numbing-cream-for-microneedling.json` (10 sections, injectable-clean). Do
  **not** clone the Botox template. Or create the collection unpublished.
- **Handle fork, open:** `/collections/numbing-cream-for-tattoos` matches the existing pattern;
  `/collections/tattoo-numbing-cream` matches the head term. Both 404 today — and note the latter is
  live on `totally-numb.com`.
- **Two block caps already full:** procedures hub `senseless-trio-card-row` at `max_blocks: 4`
  (component used by 24 sections across 15 templates); `/pages/does-it-hurt` `senseless-link-row` at
  8/8, with two more rows at 7/8.
- **The one real ad-facing risk:** `/pages/does-it-hurt-by-treatment` links all three injectable
  collections (live-verified). SPMU and waxing collections already link to it. Mitigation: give
  tattoo its own guide instead of pointing a tattoo collection there.
- **Injectable-clean baseline: 0 breaches** across 14 live surfaces. Re-run that set after any change.
- **Blog:** one blog (`guides`), 5 articles, all Botox/filler. Articles hub auto-includes new blog
  articles; guide *pages* need a manual block + deploy — so a blog article is the cheaper home.

### SEO targets and cannibalisation

- **Primary (~18,400/mo):** one collection — "tattoo numbing cream" 10,000 + "numbing cream for
  tattoos" 5,800 + "tattoo numbing cream uk" 1,900 + long-tails.
- **Cannibalisation 1 (sharpest):** ~2,240/mo of "best/strongest tattoo numbing cream" is contested
  between the new collection and `/pages/strongest-numbing-cream`, whose live title is already
  *"Best & Strongest Numbing Cream UK | Senseless"*. The 7 Aug ruling covers **collection vs PDP**,
  not **collection vs landing page**. Needs an explicit call.
- **Cannibalisation 2:** do **not** put tattoo terms on PDPs.
- **Cannibalisation 3:** "tattoo numbing spray/gel" (~730/mo) should be **sections inside the one
  collection** — Ahrefs gives them the parent topic "tattoo numbing cream".
- **Most likely to be missed — tattoo aftercare.** 9,700/mo GB at **KD 2**, traffic potential 6,400,
  plus "tattoo aftercare cream" 1,400 and "best tattoo aftercare" 600. **We already sell the two
  products that serve it compliantly** — the Vitamin A&D ointment 4-pack and the Foaming Cleanser.
  Aftercare and cleansing are cosmetic functions with far less MHRA exposure than numbing. No page
  exists. Nobody has costed this.
- **Reality check:** Senseless ranks nowhere today. Best non-brand GSC positions over 90 days are
  33–64 with **zero clicks**. **0 tattoo impressions in 90 days** (filter positive-controlled against
  "botox", which returned 5 rows).
- **No legacy equity, at any layer.** 15 redirects, 0 tattoo. 0 tattoo URLs in the 60-URL sitemap.
  6 plausible legacy paths all bare 404s. `senseless.uk` was a **Sedo parked lot** as recently as
  2021-12-24 and the 25 earliest backlinks are link-farm spam — treat the headline 216 backlinks /
  160 refdomains with caution. The old `senseless-tattooing.myshopify.com` still exists, password
  locked, 0 backlinks, 0 Wayback captures.

### Canon defects found in passing

- `docs/BRAND.md:3` names an **archive-sealed** Notion page as its source of truth — same fault class
  fixed for `DECISIONS-LOG.md` in `bf891e6`.
- `docs/ARCHITECTURE.md:63` states old tattoo URLs "will have" been redirected. **This never happened
  and could not have.** Recommend deleting the sentence.
- `.claude/skills/redirects/SKILL.md:17-18` uses `/collections/tattoo-numbing-cream` →
  `/collections/aesthetic-numbing-cream` as a worked example. That from-path is a **live Totally Numb
  URL**. A future session actioning it literally would pre-empt the tattoo build.
- Notion Pages DB already leaks the gap: the Advanced Strength Spray row carries *"tattoo numbing
  spray (NOTE: no tattoo page exists — see gap list)"*, and the A&D ointment already targets *"tattoo
  aftercare ointment"*.

---

## Open — nobody verified these

1. **What the CPSR declares.** Certificates are not in the repo; no scope field exists anywhere. Only
   the safety assessor can answer.
2. **MHRA Guidance Note 8 s.13.** Nobody fetched the document. It exists in one commit message.
3. **Ad-facing or organic.** Three sweeps flagged this as the question that determines everything
   downstream.
4. **What is inside the password-locked `senseless-tattooing.myshopify.com`** — possibly portable
   tattoo copy and imagery. Requires Daniel to lift the password.

---

## Part 3 — Pain chart & guides (strand 4: 9 of 10 agents completed; final synthesis agent stalled)

The workflow errored on its last step. All research agents and all three auditors finished, so the
findings below are complete; only the auto-synthesis is missing. Two adversarial verifiers ran
(47 and 64 checks) and their corrections are applied.

### THE BIG CORRECTION — MHRA GN8 is real, and it names tattoos

Strand 1 concluded GN8 was unsourced because it searched only the repo. **Strand 4 fetched the
primary document.** `https://assets.publishing.service.gov.uk/media/6a035312e71c4cdf4026bac6/GN8_FINAL_20260512.pdf`
— which the compliance auditor confirmed now 301s to the current **`GN8_FINAL_20260806.pdf`**
(830,613 bytes, dated 6 August 2026). Extracted with `pdftotext -layout`. §13, verbatim:

> "Topical anaesthetics which are administered to reduce sensibility to pain e.g. lidocaine,
> prilocaine, epinephrine prior to carrying out a procedure, including non-medicinal procedures, are
> regarded to be medicinal products. **Examples of non-medicinal procedures include tattoos**, and
> cosmetic procedures such as semi-permanent makeup."

**Commit `f940b05`'s citation was correct.** Two agents quoted it independently; the auditor
re-fetched both cited URLs and re-verified every load-bearing quote against the current text. Treat
GN8 as binding primary authority. **Supersedes the "unsourced" finding in Part 2 / G4.**

### Two facts that make this far less alarming than it sounds

1. **Senseless is lidocaine-free — eugenol-based** (`DECISIONS-LOG.md:176`, 2026-05-27). GN8 §13
   names lidocaine, prilocaine and epinephrine. The *function* limb of the medicinal test is much
   harder to run against Senseless than against a typical competitor.
2. **GN8 §13 already names semi-permanent makeup — and we already run
   `/collections/numbing-cream-for-semi-permanent-makeup`.** Tattoo does **not** create a new
   *category* of legal exposure. It raises volume, lowers audience age, and creates a very linkable
   page. "Tattoo is a new legal risk" is wrong; "so nothing changes" is also wrong.

**The whole exposure is therefore limb one — presentation.** There is no ingredient defence to fall
back on. The copy *is* the defence.

### CPSR ≠ claims permission

> An updated CPSR does **not** license pain claims. A CPSR is a safety assessment made *under* the
> Cosmetics Regulation — it presupposes the product is a cosmetic. If presentation makes it
> medicinal, GN8 §13 applies whatever the CPSR says.

Daniel's "the certs have been updated" is a **safety** fact and it does clear the intended-use gate
for widening the range's stated applications. It is not a claims permission and does not soften any
Hard Rule.

### The build thesis is REVERSED — the winning asset is a static image

| Asset | Build | Refdomains | GB traffic |
|---|---|---|---|
| healthline.com/…/pain-tattoos-chart | **Static PNG** | **263** | 2,915 (SERP #3) |
| totally-numb.com/pages/tattoo-pain-chart | Interactive SVG, 29 zones | **0** | **0** |
| applestan.com/tools/tattoo-pain-chart/ | Interactive SVG, 31 regions | 0 | 0 |
| tattoo-pain-chart.com | Interactive, 20 regions | 486 — **all PBN spam** | 0 |
| tattoopains.com | Client-rendered | 400 — **all PBN spam** | 0 |
| removery.com/blog/tattoo-pain-chart/ | Static PNG | 38 | 64 |

Verified exactly: **Totally Numb's chart is UR 4.6, 0 refdomains, 0 backlinks, 0 organic traffic,
0 organic keywords**, on a DR 30 domain, and absent from the domain's top-pages list.

**No interactive pain chart anywhere has earned a single genuine link.** Healthline's 263 refdomains
are editorial — BuzzFeed (DR 91), Today.com (DR 90), Bustle (DR 88), Mental Floss (DR 86), Bored
Panda (DR 84), The List (DR 75, 11 links). Lifestyle and tattoo press link to pain charts readily —
**they have only ever had static images to link to.**

Implication: build the interactive tool for users, but **the linkable, rankable artefact is a
properly-made static graphic** (position 1 for "tattoo pain chart" GB is a 12-slot image pack; the
first organic result is position 3). "tattoo pain chart **female**" at 900/mo GB means a **gender
toggle is a ranking feature, not a nicety**.

The UK bar is low: `stretchitbodyjewellery.co.uk` ranks #10 on **DR 38 with exactly 1 referring
domain**, pulling 587–610/mo.

### There is no published dataset of tattoo pain by body region

PubMed searched exhaustively; all four real studies opened and verified by an adversarial verifier.

**Witkoś J, Hartman-Petrycka M. "Gender Differences in Subjective Pain Perception during and after
Tattooing." *Int J Environ Res Public Health* 2020;17(24):9466.** doi:10.3390/ijerph17249466,
PMID 33348763, PMC7767267. The only large tattoo-pain dataset in existence, n=1,092 (863 F, 229 M),
NRS 0–10.

- Mean pain during tattooing **4.35** (SD 2.60); after 2.07 (SD 2.02).
- **Body area was NOT a significant predictor of pain intensity: p = 0.094 during, p = 0.742 after.**
- Significant only for *radiating* pain (p = 0.012).
- No sex difference during tattooing (p = 0.359); women higher after (p = 0.028).
- Strongest predictors were **time, bleeding and stress** — not location.

**So every tattoo pain chart on the internet, Healthline's included, asserts a regional pain ranking
the best available evidence does not support.** Supporting literature (Mancini 2014 whole-body
spatial acuity, n=26; Park 2019 heat pain thresholds, 14 regions, n=16 young males; Olsen 1995 skin
thickness, n=18) measures something else and is extrapolated.

> **A fabrication was caught in flight.** WebSearch's summariser produced *"a 2018 study in the
> Journal of Pain Research found average tattoo pain around 5.5 out of 10."* It does not exist. If
> that number appears in this project again, it has no source. The real published mean is **4.35**.

### The four GN8 passages that constrain the design

The compliance auditor re-derived the law from primary source and found four passages the research
agents missed. These change the build.

1. **The region-panel mechanic is enumerated, not inferred** (App.10):
   > "Lists of adverse medical conditions which take a consumer to a page **displaying a product** or
   > group of products when selected."

   That is exactly "tap a body region → see a product." Note **"displaying"**, not "linking" — so
   Totally Numb's panels containing no `<a>` element does *not* save them. A panel that renders the
   word "Platinum" is displaying a product on selection.

2. **Adjacency is named, not inferred** (§4): the list of marketing forms suggesting a medicinal
   product ends with *"**juxtaposing with any examples of the above**"*. This is a far stronger
   citation than "the ASA assesses overall impression" and is the one to put in front of legal.

3. **A same-domain editorial firewall does not work** (App.10):
   > "If you are using the internet to sell products that are not medicines, you should ensure that
   > your **entire website** or social media content is free of all direct and implied medicinal
   > claims."

   **Entire website.** Putting the evidence layer on a separate URL inside `senseless.uk` buys
   page-level tidiness, not classification safety. This kills the "editorial section architecturally
   separated from commerce" plan that two agents independently proposed.

4. **Publishing clinical research is itself a listed trigger** (§4, App.10): *"references to medical
   and/or clinical research and testing"* · *"Publication of third-party articles, reports, clinical
   data, medical research."*

   **This is the painful one.** The differentiator — "be the only chart that cites real studies,
   publish DOIs and p-values with `Dataset` JSON-LD" — is itself a listed implied medicinal claim
   when performed on the selling domain.

### Design rulings that follow

- **No region → product mapping. No compliant version exists** — not with softer words, not via the
  Selector, not with the tier renamed. The mechanism *is* the claim. **Worse for us than for Totally
  Numb:** their tiers are Bronze/Silver/Gold/Platinum (semantically empty metals); ours are
  **Clinical / Advanced / Professional**, an explicit ascending ladder. "Ribs → Professional" states
  a dose-for-pain relationship in two words.
- **Qualitative bands only, no 0–10 scale.** Three agents proposed numeric; one opposed. The
  opposition wins on project precedent: `build-reports/phase-6-interactives-comfort-compare.md` —
  *"Numeric version not built (de-scoped per the locked 2 June decision — qualitative ships, numeric
  only if cited data is later gathered)."* Reuse the live vocabulary from
  `sections/senseless-comfort-compare.liquid:4-5` — **Mild · Moderate · Sharper**.
- **No distress imagery** (App.10 "Graphics"): *"Negative images such as depictions of people looking
  unwell or showing apparent areas of pain or inflammation may create an impression that products are
  medicinal and such images should not be used."* **A red pain heat-map on a human figure is exactly
  this.** Neutral line-art, brand palette, no red, no wincing figure, no medical crosses.
- **Never merchandise it as a category** (App.10): `/pages/tattoo-pain-chart`, never
  `/collections/tattoo-pain-relief`.
- **No reviews module on the chart page.**
- **Note the theme's own history:** `sections/senseless-pain-scale-slot.liquid` was **deleted** and
  its anchor renamed `#pain-scale` → `#comfort`. "Pain" was deliberately removed from this theme's
  interactive surface. Precedent, not law — but flag it before naming a file
  `senseless-pain-chart.liquid`.

### Totally Numb's chart — teardown (group-internal; same parent, so this is improving our own concept)

`https://totally-numb.com/pages/tattoo-pain-chart`. Ownership confirmed from the footer
(`matrix-health-group-logo` beside "© 2026 Totally Numb").

Custom Shopify section, hand-written, no app, no third-party embed. Two inline SVGs
`viewBox="0 0 200 520"` (front + back), one `<path>` per zone, `role="button"`, `tabindex="0"`,
Enter/Space handled, panel `aria-live="polite"`. **29 zones**, 3-band ordinal scale.
~230 lines of vanilla JS plus two hand-drawn silhouettes — **rebuildable in an afternoon.**

**Where it's beatable:**

| Failure | Detail |
|---|---|
| No source, anywhere | Rationale is "skin thickness, nerve density, proximity to bone" — plausible, unattributed. The reason it earns no links. |
| Pain level is **colour-only** | `aria-label="Rib cage"` — the band exists only as a CSS class. Screen-reader users get no sensitivity information at all. |
| Bands not visually distinguishable | Composited fills give **1.31:1** (high↔moderate) and **1.12:1** (moderate↔lower). WCAG 1.4.11 needs **3:1**. All pairs fail. |
| Dead CSS rule — a live bug | CSS styles `[aria-selected=true]`; HTML/JS set `aria-pressed`. `grep -c 'aria-selected'` → **0**. The active Front/Back tab never highlights. |
| Tap targets fail WCAG 2.5.8 | Body renders at max-width **200px desktop / 240px mobile** for a 29-region diagram. Spine 10×120px, neck 24×16px. |
| No-JS fails completely | All zone data lives in JS arrays, and the back SVG carries a literal `hidden` attribute — **with JS off the back of the body is unreachable.** |

Verifier note: an agent claimed the back view is only 3 of 29 zones — **corrected, that was wrong.**
Front/back parity is not the easy win it looked like.

### Theme build constraints (verified)

- **Schema `name` is capped at 25 characters** — undocumented locally; three sections sit exactly at
  25. Safe candidates: `Senseless — Body map` (20), `Senseless — Comfort map` (23).
- **Precedent to copy: `sections/senseless-selector.liquid`** (171 lines). Native radios in a
  `fieldset`/`legend` — the DOM *is* the state, no JS state object; free arrow-key nav and
  radiogroup semantics; one inline IIFE scoped via `document.currentScript.closest()`; ES5, no
  framework, no build step.
- **CSS: unique class prefix per section, inline `{%- style -%}`, no stray `z-index`.** Locked after
  a real collision — the cookie banner's `.ss-cc` leaked onto comfort-compare and pinned it to the
  viewport (`docs/ARCHITECTURE.md:67`).
- **Every text setting needs a non-empty `default`** — `theme push` rejects `default:""` and
  **theme-check does not catch it** (`DECISIONS-LOG.md:137`).
- **Two BRAND.md drift items — do not trust it blindly:** `BRAND.md:27` says `--text-muted #8E8A82`;
  the live token is **`#6E6A63`**. And the brand asterisk strokes **`#984AE8`**, not `#6B3FA0`,
  despite `BRAND.md:104`.

### Verifier corrections applied

- Totally Numb domain: **19** organic keywords (not 23), **79** organic visits/mo (not 81),
  org_cost $54.40 (not $55.65). The 21× paid-vs-organic ratio is unchanged.
- Reddit holds organic position **4 only** on "tattoo pain chart" GB (not 3–5). Position 3 is
  Healthline, position 5 is kingpintattoosupply.
- `hushanesthetic.com` least-painful page: **UR 0, 0 traffic** (not UR 4.5 / 98).
- `tattoopains.com`: 400 refdomains (not 399).
- The `tattoo-pain-chart.com` PBN campaign is **ongoing**, not confined to Apr–Jun 2026 — its 15 most
  recent referring domains are `*.shop` link farms first seen 3–12 Aug 2026.
- **Cite GN8 by section and appendix, never by line number** — line numbers are an artefact of one
  `pdftotext` run and are not reproducible.

### Still unverified after two adversarial passes

- The ~22,500/mo GB informational cluster total (a floor; 15 largest components individually
  confirmed, the summation not reproduced).
- Per-body-part GB volumes beyond "rib tattoo pain" (80, confirmed).
- The "$18k/mo equivalent paid clicks" valuation — the agent's own arithmetic, not a tool output.
- Totally Numb's chart build measurements (29 zones, contrast ratios, tap targets) — curl/grep
  arithmetic, **no browser was driven**, so rendered appearance and focus behaviour are unobserved.
- Whether the TN chart page is indexed by Google at all.
- Pan 2024 thenar pressure-pain figures — **do not publish** until someone opens the full text.

---

---

## Part 4 — Competitor research + challenger playbook (strands 2 & 3, salvaged)

Both workflows died when the machine slept at 21:29. Strand 2 completed **16 agents**, strand 3
completed **7** (both research phases; the verifiers and final syntheses did not run). Findings below
are the agents' own, **not adversarially verified** — treat figures as single-sourced.

### ⚠️ URGENT 1 — A bought-link package is pointed at senseless.uk, and it is live

Nothing to do with tattoos. Found while measuring authority.

**Domain Rating history** (`site-explorer-domain-rating-history`, weekly):

```
13 Jul  DR 14
20 Jul  DR 27   ← peak
27 Jul  DR 21
03 Aug  DR 10
10 Aug  DR  7   ← today
```

**Referring domains** (`site-explorer-refdomains-history`, weekly): 8 at launch week (8 Jun) → 52
(29 Jun) → **147 (13 Jul, +95 in a single week)** → 178 (20 Jul) → 163 (10 Aug).

**158 of 160 live referring domains are Ahrefs-flagged spam.** The only two non-spam are
`creativeposts.top` (DR 42, 0 traffic, 0 dofollow links) and `matrixhealthgroup.co.uk` (the group's
own parent site). **Earned editorial referring domains: zero.**

Named domains, with first-seen dates: `backlinksplace.site` (DR 48, **first seen 3 Aug 2026**),
`backlinkshop.site` (DR 48, **30 Jul 2026**), `trafficspike.shop` (DR 47), `seoflox.io` (DR 49),
`seodaro.com` (DR 42), `norskcasinos.net` (DR 45, **dofollow**), `idenihtercepat.com` (DR 51),
`haspersonals.com` (DR 53).

**This is ongoing, not historical** — placements landed within the last two weeks. DR nearly doubled
then fell by three quarters in three weeks: the signature of a link package being ingested and then
devalued. Nothing in the repo records anyone commissioning this.

**Questions for the owner:** is this being paid for? By whom — an agency, a marketplace order? It
should stop, and a disavow may be warranted.

### ⚠️ URGENT 2 — The review corpus is Totally Numb's, republished with "tattoo" edited out

Measured via the Judge.me widget JSON endpoint (`judge.me/reviews/reviews_for_widget?shop_domain=…`),
not a plain curl — the known false-reading trap was avoided. The endpoint agrees exactly with the
PDP JSON-LD, so both are real.

**Senseless: 234 product-attached reviews, weighted average 4.881** (the theme's "4.9" is honest).
Deduplicated pull of 227 (97% coverage):

| | |
|---|---|
| Dated 2023 | **184** |
| 2024 / 2025 / 2026 | 25 / 15 / **3** |
| Reviews in trailing 12 months | **8** |
| Reviews dated after the 7 June 2026 launch | **3** |
| `verified_buyer: true` | **3 of 227** |
| Photos / videos / brand replies | **0 / 0 / 0** |
| Products with zero reviews | **11 of 16** |
| Share of all reviews on one SKU (`professional-strength-cream`) | **88.5%** (207) |

**Tier-by-tier against Totally Numb's Judge.me** (245 reviews, 4.88): TN `comfort-cream-bronze`
**13 @ 4.85** ↔ SL `clinical-strength-cream` **13 @ 4.85**; TN `comfort-cream-platinum` 216 @ 4.88 ↔
SL `professional-strength-cream` 207 @ 4.88. The agent pulled both sets: **same 10 reviewer names,
same 10 dates.** Four texts identical, six edited:

> TN: *"My wife went through a four hour back **tattoo**…"*
> SL: *"My wife went through a four hour back **procedure**…"*

> TN: *"**Totally Numb Comfort Cream Bronze** — Bought this cream…"*
> SL: *"**Senseless numbing cream** — Bought this cream…"*

Across a 150-review Senseless sample, "tattoo" appears **0 times**, "procedure" **65 times**, and
**31 of 150 still contain tattoo vocabulary the edit missed** — *back piece, half sleeve, cover up,
sitting, shading, outline, rib, forearm, full leg, ink* — plus *"A 6 hour procedure"* and *"Amazing 7
hour procedure felt nothing for 6!"*. No aesthetic procedure runs seven hours.

**Context that may mitigate, and needs checking:** `DECISIONS-LOG.md:119` records that Senseless's
CPSR coverage was originally assumed from *"the same certifications as Totally Numb"*. If these are
literally the same formulations under two brands, transplanted reviews are arguable. **The editing of
review text is a separate matter** — and UK law changed here: the DMCC Act 2024 provisions on fake
and misleading reviews are in force. **3 verified buyers out of 227** is the number that will be
asked about.

**This is also self-solving in one direction:** if Senseless is now tattoo-positive, the edits were
unnecessary. The reviews describe tattoo sessions because they are about tattoo sessions.

**Owner + legal decision. Not a copy edit, and not one to make quietly.**

### The competitors — none of them is what they look like

| Domain | DR | GB organic | Reality |
|---|---|---|---|
| **getnumbd.com** | 5 | **0 keywords, 0 traffic** | Pure Google Ads arbitrage. 84 paid keywords, $1,059/mo GB, scaled to **$10,415 in July**. |
| **totally-numb.com** *(group)* | 30 | 79 visits, 19 keywords | $54/mo organic vs **$1,160/mo paid**. Declining from a 157-visit May peak. |
| **tattoonumbingcream.com** ("Tattoo Numbing Co") | 40 | 1,731 visits | The real leader. +118% YoY globally — but **94% of UK traffic is one URL**. |
| **tattoonumbx.com** | 11 | 3,671 visits | **73% on one PDP.** Outranks Amazon, TKTX and Superdrug on exact-match relevance alone. |
| **emla.co.uk** | — | 4,954 visits | The category authority. **Declining −46% YoY.** |
| **hushanesthetic.com** | 35 | 4,894 visits | Tattoo-culture publisher, weak retailer. UK essentially undefended. |
| **tktxoriginal.co.uk** | 59 | 4,942 visits | **93% homepage, on a trademark they don't own.** DR is manufactured. |

**Every one of them has an exploitable structural defect:**

- **getnumbd** — #1 paid landing page is 156 words, all Shopify filter chrome, H1 *"Collection:
  Numbing Creams"*. **Running live ads to a 404.** Two of five nav categories are empty collections
  they are actively buying traffic into. 8 products, only 2 numbing. 423 refdomains, 100% spam
  (one vendor testimonial anchor across 220 domains). **Zero AI citations on all seven engines.**
- **tattoonumbingcream.com** — **every product page serves an empty `<main>` behind a Locksmith
  spinner**: no h1, no meta description, no body copy, no server-rendered Product schema, verified
  under a Googlebot UA. AggregateRating is injected client-side by Loox, invisible to non-JS
  crawlers. 302 blog posts → ~300 visits/mo total. **Shipping a 1-star `aggregateRating` on a $100
  SKU.** Review count contradicts itself three ways on the same site (10,000+ / 8,259 / 11,000+).
- **tattoonumbx** — its **#1-ranking delivery page is a 404** (position 1 for "tattoo numbing cream
  next day delivery", 350/mo). Zero ingredient transparency. No FAQPage/HowTo/Review/Breadcrumb
  schema anywhere.
- **hush** — **flagship numbing cream is sold out and telling Google so.** A 2019 US CPSC recall of
  275,000 units is their single highest-authority backlink cluster: cpsc.gov, DR 90, 35 dofollow
  links, permanent.
- **emla** — no cart, no prices, no reviews anywhere, pharmacy gate on the purchase, cream only.
  `/emla-for-tattoos/` earns **1,242 GB visits/mo from 5 referring domains**.

**The claims picture:** getnumbd (*"no pain"*, *"Lasts up to 5 hours!"*, *"30% More Effective than
Leading Competitors"*), TNC (*"5% Lidocaine / 5% Prilocaine / 1% Epinephrine"*, *"blocks pain
receptors"*), TKTX (*"temporarily block nerve signals"*, *"Numbs skin for up to 6 hours"*), Hush
(*"Painless"*, *"Lasts up to 4 hours pain free"*). **All are GN8 medicinal presentations Senseless
cannot copy — and all are why those competitors are fragile.**

### Group exposure, now concrete

`totally-numb.com`'s footer publishes **company number 17099304 and VAT GB 523 7816 82 — identical to
Senseless.** Under that same entity it publishes onset (*"begins to take effect within 30–45
minutes"*), duration (*"typically lasts between 1–3 hours"*), comparative efficacy, and a
mechanism-of-action passage (*"reducing nerve signal transmission… the result is reduced or absent
sensation"*). Its **paid** landing page carries a practitioner testimonial: *"Four hours of clean work
with no breaks"* — a duration claim in a third-party voice, banned in every voice under Senseless's
own 16 Jun rule (`docs/COMPLIANCE.md:21`).

**Two claim sets, one VAT number, both live, one of them in the paid channel.**

And on paid specifically: Totally Numb's homepage runs **53 ads**, 39 paid keywords, 1,250 paid
visits, **$1,149/mo**, top keyword **"tattoo numbing cream"**. Its landing page is already
substantially the compliant tattoo page Senseless would build — *"Topical numbing products for tattoo
and aesthetic procedures"*, badges for *"Formulated in the United Kingdom" / "CPSR Assessed"*, 247
reviews, and a **"Shop for tattoo"** CTA, with no onset or duration claim in the brand voice.
**Senseless bidding the same term means one legal entity bidding against itself**, splitting budget
and lifting the group's own blended CPC. (A Google double-serving policy breach was investigated and
is **UNVERIFIED**; the commercial self-competition is verified and is the real cost.)

### GEO — the hypothesis is confirmed, with a twist

15 distinct AI-Overview-cited URLs pulled from `serp-overview` and run through `batch-analysis` (GB):

| Across the 15 AI-cited pages | Value |
|---|---|
| Median Domain Rating | **23** (range 0.8 → 77) |
| **Median referring domains to the cited page** | **1** |
| Pages with zero referring domains | **5 of 15** |
| Most referring domains any cited page had | **5** |
| Pages under 20 organic visits/month | **8 of 15** |

**The typical page cited by Google's AI Overview for a 10,000/mo commercial keyword has one link
pointing at it.** `valhallastudio.co.uk` — **DR 0.8, 1 referring domain** — a Kilmarnock tattoo
studio, is cited for "tattoo numbing cream". **Citation is decoupled from ranking.**

Domain-level AI citations (`site-explorer-ai-responses-count`, 7 engines):
hushanesthetic.com **2,154** · tattoonumbingcream.com **320** · **valhallastudio.co.uk (DR 0.8) 56** ·
totally-numb.com 27 · **senseless.uk 2** · getnumbd.com 2.

**A DR 0.8 tattoo studio out-cites the DR 30 commercial store 56 to 27.**

**The honest counter-finding:** classic ranking is *also* cheap here (KD 0–1 across the cluster). GEO
is **not** asymmetric versus SEO in this niche — the same asset wins both. **Do not build two
programmes.**

**And the biggest GEO lesson comes from Emla:** it is the most-cited domain in the category (ChatGPT
51, AI Mode 68, AI Overviews 41, Copilot 28, Perplexity 23) with **zero FAQPage, Product, Review or
HowTo schema** — purely question-shaped headings and direct prose answers.

### Where Senseless actually stands, and what gates entry

- **Zero organic keywords, zero organic traffic, on every query shape tried** (GB, global,
  `mode=domain`, `mode=subdomains`, and a `keyword isubstring "tattoo"` filter). Homepage URL Rating
  4.5, flat since 13 July. Paid footprint: **$5.81/month**, and not on tattoo terms.
- **Senseless appears on none of the 16 tattoo SERPs pulled.**
- **Live indexable inventory = 58 URLs**, not the 63 the repo implies — 4 page templates 301 away
  (`best-numbing-cream`, `choosing-your-format`, `choosing-your-strength`, `how-it-works`) and
  `page.contact.json` is `noindex,follow`.
- **The competitor link-gap play does not exist.** The intersect of domains linking to two or more
  competitors is **15 domains, every one a platform artefact, scanner profile or junk directory.**
  There is no shared editorial ecosystem to mine.
- **Links are not gating entry.** `skinartdepot.co.uk` ranks **position 6** for "best tattoo numbing
  cream" on **DR 0, 0 backlinks, 0 referring domains**. What gates entry is having no tattoo page.
- **Verdict: organic on tattoo terms is a 90-day channel, not a 12-month one.**

### Two gaps nobody was looking for

1. **No indexable delivery page.** `/pages/delivery`, `/pages/shipping`, `/pages/shipping-returns`,
   `/pages/delivery-returns` all **404**; only the native `/policies/shipping-policy` exists, and it
   is absent from the sitemap. Meanwhile "tattoo numbing cream next day delivery" is **250/mo** — and
   TattooNumbx ranks **#1** for it with a page that returns 404.
2. **No social presence at all.** The homepage has **no Instagram, TikTok, YouTube, Facebook or
   Pinterest link**. UGC occupies **7 of the top 30** results on the GB money terms, and the entry bar
   is trivial — an Instagram Reel with **56 likes** ranks #24; a brand YouTube video with 6,694 views
   ranks #9.

**Where the conversation is:** `r/tattooadvice` (1,607,713 subscribers) is the venue; demand renews
roughly monthly. **There is no viable UK tattoo subreddit** (`r/uktattoo` has 3 subscribers,
`r/TattooUK` has 4), so Reddit is a global play, not a UK one — which matters for a UK-shipping
brand. Standalone forums are dead (`bigtattooplanet.com` refuses connections, 0 GB organic). The UK
conversation lives in Facebook groups — "Tattoos UK" (`441256126225022`) and "beginners tattoo club"
(`532327551070323`) both surface in GB SERPs.

**Brand share-of-voice across five tattoo subreddits** (Reddit search API, all-time): TKTX 100
(capped), Bactine 100 (capped), Emla 49, Hush 41, Zensa 30, Dr Numb 11, Anesten 8 — **Numbd 0,
Senseless 0.**

### Senseless's real GEO gap (it is not schema coverage)

**Senseless already emits more schema than every competitor in the set** — and is cited twice. The
gap is four specific things:

1. **No entity graph** — zero `sameAs`, zero `@id` linkage; `Organization` on only 2 of 9 page types.
2. **Product node has no identity or composition properties** — no product-level `sku`, no `gtin`,
   no INCI, no tier/format properties.
3. **11 of 26 page templates emit no `WebPage` node at all** — including all three ad-facing
   commercial landing pages.
4. **Thin extraction surface** — across 9 live pages: **0 `<table>`, 0 `<time>`, 0 author markers**,
   and FAQ questions render inside `<summary>`, not headings.

### Keyword universe (strand 2's independent build)

263 deduplicated terms, **36,190/mo GB**: commercial 79 terms / 23,260 · comparison 58 / 6,450 ·
informational 58 / 3,120 · brand 57 / 2,940 · removal adjacency 9 / 370 · aftercare-inside-numbing
2 / 50.

On the 14,800 correction, strand 2 went further: `keywords-explorer-volume-history` shows the UK
figure for "tattoo numbing cream" **has never been 14,800 in Ahrefs' record back to Sep 2015** —
all-time peak 11,863 (Jul 2023). Most plausible origin: Google Keyword Planner reporting the head
pair grouped (10,000 + 5,800 = 15,800, bucketed to 14,800). **Use 10,000 for the single term,
~15,800 for the pair.**

### Verification status — corrected

**Strand 2 did complete** (19 of 20 agents; the machine woke and it ran on). Both its adversarial
verifiers ran — 34 and 70 checks — and its final synthesis is saved separately as
**`docs/TATTOO-BEAT-THEM-PLAN-2026-08-12.md`**. An earlier note in this file said strand 2 died
unverified; that was wrong.

**Strand 3 did not complete.** 7 agents (both research phases); no verifier, no synthesis. The
challenger-playbook findings above — the bought-link package, the review corpus, the off-SERP and
AI-citation numbers — are **single-sourced**. The link-package and review findings were partially
corroborated by strand 2's verifier (see below), but treat strand-3-only figures with care.

### Corrections from strand 2's verifiers — apply these

- **getnumbd.com paid spend was overstated ~3.4×.** Not $3,644/mo / 4,509 visits. **Actual: 84 paid
  keywords, 1,284 paid visits, $1,063.08/mo.** The same inflation hit the recon agent's
  totally-numb figure; the **$1,161/mo** for Totally Numb is correct. The "$10,415 in July 2026"
  peak came from a different endpoint and was not re-run — treat as indicative.
- **A THIRD spam referring domain appeared mid-session:** `backlinkengine.shop`, `first_seen
  2026-08-12T18:09:50Z` — during this session. Refdomains 164, not 163; non-spam count is now 3, not
  2. **The link package is landing in real time.**
- senseless.uk all-time backlinks 411 / 260 refdomains (not 410 / 259). Live 216 / 160 exact.
- tattoonumbx GB traffic: PDP 2,679 (not 2,688), homepage 424, delivery page 132. Positions all
  confirmed.
- Totally Numb's Product node **does** carry `gtin13: 10795847725977` — the "no gtin" finding was
  wrong.
- **Totally Numb ownership is established, not inferred** — the verifier upgraded it from
  UNVERIFIED. Footer and JSON-LD both publish company **17099304** / VAT **GB 523 7816 82**,
  identical to `sections/senseless-footer.liquid:177` and `templates/page.contact.json:140`.
- getnumbd's empty collection page is 160 words, not 156. Immaterial.

### Flagged UNSUPPORTED by strand 2's verifier — do not quote these

- **The 263-term / 36,190-per-month universe** and its addressability split (176 addressable /
  55 constrained / 32 unaddressable at 1,680, 4.6%). Derived sums over an unaudited manual
  classification. **Use the repo's ~650/mo (~2.5%) unaddressable figure instead** — first-party,
  components individually named.
- The tattoo-pain (17,400/mo) and tattoo-aftercare (18,050/mo) **cluster totals**. The anchor terms
  are exact ("tattoo pain chart" 6,900 KD 1; "tattoo aftercare" 9,700 KD 2); the sums were not
  reproduced.
- **The "15 domains linking 2+ competitors, all junk" link-gap intersect** and the named gap targets
  with their DRs. Not re-run. The conclusion may hold; the list is unverified.
- The "16 SERPs mapped" detail — 4 were re-run and were exact; the other 12 were not.
- The GSC figures (0 tattoo rows, and the per-term impression/position numbers).
- Per-term long-tail body-part volumes beyond the spot-checked heads.

### One live compliance trap already sprung

**`strongest numbing cream` is already live as an inbound backlink anchor on 2 referring domains,
first seen 2026-07-16, with no sign-off.** The superlative is permitted in slug/title/meta only, and
using it as anchor text needs Daniel's written approval. It is already out there.

