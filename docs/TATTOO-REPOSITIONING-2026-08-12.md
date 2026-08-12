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

Strands 2–4 append below on completion.
