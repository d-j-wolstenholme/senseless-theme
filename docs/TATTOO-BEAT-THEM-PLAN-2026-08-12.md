# Tattoo — the beat-them plan (2026-08-12)

**Source:** final synthesis agent of the competitor deep-research workflow (19 of 20 agents
completed; both adversarial verifiers ran). Evidence base is
`docs/TATTOO-REPOSITIONING-2026-08-12.md`, which outranks this document where they disagree.

**Status: PLAN ONLY. Nothing here has been built, and two items in `NEXT_SESSION.md` — the bought
link package and the review corpus — outrank all of it.**

---

# Beating the incumbents on tattoo — content, SEO and GEO plan

**Read this alongside `docs/TATTOO-REPOSITIONING-2026-08-12.md`.** That document is the evidence base and it outranks the agent reports that fed this plan: its Parts 1–3 are first-party and passed two adversarial verifiers; its Part 4 was single-sourced and has now been verified by the pass attached to this brief. Where a report and the repo record disagree, I say which I trust and why.

Two things in `NEXT_SESSION.md` outrank the tattoo work and are carried into Section 7 as Session 1: the **bought-link package pointed at senseless.uk**, and the **review corpus being Totally Numb's with "tattoo" edited to "procedure"**. Do not start building around either of them.

---

## 1. WHERE SENSELESS ACTUALLY STANDS

Senseless is at absolute zero on tattoo and close to zero on everything else: `site-explorer-metrics` and `batch-analysis` (target `senseless.uk`, mode `subdomains`, country `gb`, 2026-08-12) both return **DR 7.0, 0 organic keywords, 0 organic traffic**, the paid footprint is **$5.81/month on 2 keywords across 1 landing page**, the site appears on **none of the 16 tattoo SERPs pulled**, and **zero of its 58 live indexable URLs contain the word "tattoo"** — the word appears in exactly two lines of shipping code, both FAQ *questions*, both answered without saying yes (`templates/collection.aesthetic-numbing-cream.json:282`, `templates/page.strongest-numbing-cream.json:177`). Against that, the incumbents' advantages are narrower than they look: the head term **"tattoo numbing cream" is 10,000/mo GB at keyword difficulty 0** (`keywords-explorer-overview`, gb — and the 14,800 in commit `f940b05` is a Keyword Planner bucket, not an Ahrefs figure), a **DR 0 site with 0 backlinks holds position 6** for "best tattoo numbing cream" (`serp-overview`, gb), the **typical page cited by Google's AI Overview on that 10,000/mo term has one referring domain**, and **links are demonstrably not what gates entry — having no tattoo page is**. The realistic read, and the one the repo record already reached: **organic on tattoo terms is a 90-day channel, not a twelve-month one**, but only after four owner/legal gates clear, because the change being made is not "add some pages" — it is **reversing the declared intended use of a CPSR-assessed cosmetic**, and three of the four gates (CPSR scope, the unbroken-skin warning, and Senseless-vs-Totally-Numb) cannot be answered by anyone in this repo.

---

## 2. THE COMPETITORS, RANKED

All figures `batch-analysis` / `site-explorer-metrics`, mode `subdomains`, country `gb`, 2026-08-12. Paid values are USD, converted from cents.

| # | Domain | DR | GB organic /mo | Wins on | Structural weakness | Can Senseless copy? |
|---|---|---|---|---|---|---|
| 1 | **emla.co.uk** | 22.0 | **5,001** (244 kw) | Pharmaceutical authority. Cited twice in the head-term AI Overview; `/emla-for-tattoos/` earns 1,242 GB visits from 5 referring domains | No cart, no prices, no reviews, pharmacy gate, cream only. **Declining −46% YoY** | **No — and don't try.** It is a licensed medicine and may lawfully say pain relief. Route around it: format range, purchase route, session-day prep |
| 2 | **hushanesthetic.com** | 35.0 | **4,903** (1,273 kw, 557 in top 3) | The GEO benchmark. GB AI citations: AI Mode 102/53 pages, Perplexity 72/29, AIO 43/27, Gemini 36/22 — all earned by `/blogs/community/` editorial, not product pages | Flagship cream **sold out and telling Google so**. Its highest-authority backlink cluster is a **2019 US CPSC recall of 275,000 units** (cpsc.gov, DR 90, 35 dofollow, permanent). UK essentially undefended | **Yes — the mechanism.** Depth of question-shaped editorial. Not the claims ("Painless", "Lasts up to 4 hours pain free") |
| 3 | **tktxoriginal.co.uk** | 59.0 | **4,795** (36 kw) | Brand demand — "tktx numbing cream" 6,600/mo KD 17 | **93% of traffic is the homepage, on a trademark they don't own.** 3 pages, 8 blog URLs. No informational layer at all, so invisible in AI answers | Can't out-brand it. Can out-publish it trivially. A factual UK-safety comparison page is compliant and persuasive |
| 4 | **tattoonumbx.com** | 11.0 | **3,658** (83 kw) | Exact-match relevance. One PDP does 2,679 GB visits and outranks Amazon, TKTX and Superdrug. Its delivery page holds **#1 for "tattoo numbing cream next day delivery"** with 0 backlinks and 0 refdomains | 73% on one URL. Zero ingredient transparency. **No FAQPage, HowTo, Review or Breadcrumb schema anywhere**. Repo Part 4 records the #1 delivery page as *a 404* — unresolved, see §8 | **Page-for-page target.** DR 11 / 505 refdomains vs our DR 7 / 160. Its onset+duration copy ("starts working in as little as 30 minutes… three and five hours", "Enjoy, Pain free!") is banned for us |
| 5 | **tattoonumbingcream.com** — *"Tattoo Numbing Co"* | 40.0 | **1,733** (98 kw) | The content moat: **302 blog articles** (303 sitemap locs incl. hub) and **245 global ChatGPT citations across 72 pages** — 142 of them from `/blogs/`, and **0 from `/products/`** | **Every PDP serves an empty `<main>` behind a Locksmith spinner** — no h1, no meta description, no server-rendered Product schema; the 4.8/8,259 rating is Loox-injected client-side. 302 articles → ~300 visits/mo. Freshness is faked: 198 of 303 sitemap URLs share one `lastmod` | **Yes — the article volume and the question-shape.** That is the one incumbent tactic that is 100% legally copyable. Never the voice ("F\*CK PAIN", "pain-free", "5% Lidocaine / 5% Prilocaine / 1% Epinephrine", "a triple-action formula combining a nerve deadener, nerve blocker, and vasoconstrictor") |
| 6 | **getnumbd.com** | 5.0 | **0** (0 keywords, GB *and* global) | Nothing organic. Pure Google Ads arbitrage: 84 paid keywords, 1,284 paid visits, **$1,063/mo**, peaking at **$10,415 in July 2026** | #1 paid landing page is ~156–160 words of Shopify filter chrome, H1 "Collection: Numbing Creams". **Running live ads to a 404.** Two of five nav categories are empty collections they are buying traffic into. 423 refdomains, effectively all spam. **Zero AI citations on all seven engines (GB)** | Copy the *channel* and the *format × procedure architecture*. Never the copy — "it numbs the skin quickly, ensuring you experience no pain", "Lasts up to 5 hours!", "30% More Effective than Leading Competitors" |

**Group-internal — not a share target:**

| Domain | DR | GB organic | Paid | The problem |
|---|---|---|---|---|
| **totally-numb.com** | 30.0 | **80/mo** (20 kw), worth $54 | **$1,161/mo**, 39 kw, top keyword **"tattoo numbing cream"** | **Same legal entity.** Footer and JSON-LD both publish company **17099304** and VAT **GB 523 7816 82** — identical to `sections/senseless-footer.liquid:177` and `templates/page.contact.json:140`. Shopify store key `matrix-group-totally-numb.myshopify.com` is the CLI default named in `.claude/rules/deploy-and-store.md:6`. Ownership is **established**, not inferred |

Three consequences, all owner-level:

1. **`https://totally-numb.com/collections/tattoo-numbing-cream` is live.** The exact collection proposed for Senseless already exists on the sister brand. Repo canon assigns the lane away — `build-reports/phase-6-close-does-it-hurt-by-treatment.md:24`, *"no tattoo content (excluded per spec — Totally Numb's lane)"*.
2. **One entity is about to bid against itself.** Totally Numb's top paid keyword is the term Senseless would buy. That splits budget and lifts the group's own blended CPC.
3. **Two claim sets, one VAT number.** Under 17099304, Totally Numb publishes onset (*"begins to take effect within 30–45 minutes"*), duration (*"the effect typically lasts between 1–3 hours"*), comparative efficacy (*"helps reduce discomfort during waxing compared to untreated skin"*) and mechanism of action (*"reducing nerve signal transmission… the result is reduced or absent sensation"*) — and a duration claim in a practitioner's voice on its **paid** landing page (*"Four hours of clean work with no breaks"*). That is an ASA consistency exposure for the group, not just a commercial one.

**What to steal from the group's own store, because it works and is compliant:** the *"There is no regulated definition of 'strongest' in the UK cosmetic numbing market"* refusal frame; the CPSR trust chips; and the session-matching architecture (but matched to **procedure, area size and format**, never to hours).

---

## 3. THE COMPLIANCE CEILING

**Size of the disadvantage, honestly.** Roughly **650 searches a month cannot be served compliantly at all** — `how long does tattoo numbing cream last` (200), `does tattoo numbing cream work` (150), `long lasting tattoo numbing cream` (90), `painless tattoo numbing cream` (80), `8 hour tattoo numbing cream` (60); the five named terms sum to 580 and the ~650 figure includes further tail. Against a cluster floor of ~25,930/mo GB that is **~2.5%**.

> **I am using the repo's ~650/mo (~2.5%) figure, not the 1,680/mo (4.6%) in the input research.** The repo figure is first-party, its components are individually named and re-verifiable. The 1,680/4.6% number was flagged **unsupported** by the adversarial pass — derived arithmetic over an unaudited 263-term classification that nobody has rebuilt. Do not put 4.6% in front of the owner. An earlier in-session note put it at ~260/mo; that was too optimistic and is also superseded.

**But volume badly understates the cost, and this is the part to accept up front rather than discover as underperformance.** Every competitor on this SERP states onset and duration in hours. Senseless cannot, **in any voice**, including customer-attributed — `.claude/rules/compliance.md` binds the Hard Rules "in every voice, incl. testimonials/reviews". Expect to lose CTR and dwell **even where we rank**.

**MHRA Guidance Note 8 is real and binding — this is settled.** Gate G4 in the repo record called it unsourced; that is **superseded**. The PDF was fetched (`assets.publishing.service.gov.uk`, now `GN8_FINAL_20260806.pdf`, 6 Aug 2026). §13 verbatim: *"Topical anaesthetics which are administered to reduce sensibility to pain e.g. lidocaine, prilocaine, epinephrine prior to carrying out a procedure, including non-medicinal procedures, are regarded to be medicinal products. **Examples of non-medicinal procedures include tattoos**, and cosmetic procedures such as semi-permanent makeup."* Cite by section and appendix, never by line number.

**Two facts that make this far less alarming than it reads:**
- Senseless is **lidocaine-free, eugenol-based** (`DECISIONS-LOG.md:176`). The *function* limb of GN8 is weak against us. The entire exposure is the **presentation** limb — which is exactly what the Hard Rules already control.
- GN8 §13 **already names semi-permanent makeup**, and Senseless already sells an SPMU collection. **Tattoo creates no new category of exposure.**

**Four GN8 passages that constrain the build** (derived from primary source, verified twice):

| Passage | What it kills |
|---|---|
| App.10 — *"Lists of adverse medical conditions which take a consumer to a page **displaying a product**… when selected"* | **Region → product mapping on a pain chart.** Note "displaying", not "linking" — a panel with no `<a>` in it does not save you |
| §4 — the list of medicinal-suggesting marketing forms ends *"**juxtaposing with any examples of the above**"* | Adjacency is enumerated, not inferred. This is the citation to put in front of legal |
| App.10 — *"you should ensure that your **entire website**… is free of all direct and implied medicinal claims"* | **A same-domain editorial firewall does not work.** Putting the evidence layer on a separate URL inside senseless.uk buys page tidiness, not classification safety |
| §4 / App.10 — *"references to medical and/or clinical research and testing"*, *"Publication of third-party articles, reports, clinical data, medical research"* | **"Be the only chart that cites real studies with DOIs and p-values" is itself a listed implied medicinal claim** on a selling domain. The planned differentiator is unusable as planned |

**Banned as page copy, banned as anchor text, banned in reviews:** *numbs · anaesthetic · pain relief · pain-free · painless · blocks/reduces sensation · works in X minutes · lasts X hours · X% effective · strongest · as strong as Emla · desensitise · nerve deadener / nerve blocker / vasoconstrictor · completely safe.* Percentage-strength positioning (the 80/100 convention TKTX and Totally Numb Platinum use) is out. Ingredient terms are permanently out — `benzocaine` (7,800/mo) and `lidocaine cream` (5,900/mo) are what GetNumbd buys, and "anaesthetic" is a named Hard Rule word.

**Constrained, not banned — rank on it, then decline it.** `best tattoo numbing cream` (1,500, KD 1) and `strongest tattoo numbing cream`. The SEO-vs-body-copy rule permits the superlative in slug/title/meta only. Live precedent on both stores: `templates/page.strongest-numbing-cream.json` — *"We don't make that comparative claim… The comparison isn't ours to make"* — and Totally Numb's *"There is no regulated definition of 'strongest'"*. **Needs Daniel's written sign-off before use as backlink anchor text**, and note the trap has already sprung: `strongest numbing cream` is already live as an inbound anchor on 2 referring domains, first seen 2026-07-16, unsigned-off.

### The positioning angle — the constraint is the differentiator

**Every competitor answers "does tattoo numbing cream work?" with a claim. Senseless is the only brand structurally obliged to answer with a framework.** Framework answers are what AI Overviews cite, and AI Overview holds **position 1 on both commercial head terms, above Amazon**.

Four assets nobody in this category can copy back:

1. **UK company, UK CPSR, real INCI.** GetNumbd's entire disclosure is *"Anestoderm, Aloe Vera Gel, Lecthin, Vitamin E"* — not INCI, misspelled, no concentration. Totally Numb publishes none. Tattoo Numbing Cream Co. publishes 5% lidocaine / 5% prilocaine / **1% epinephrine** and is registered in Dubai. Senseless is a UK entity with a VAT number and a safety assessor.
2. **Honest expectation-setting.** The best sentence in the whole competitive set is Tattoo Numbing Cream Co.'s: *"Numbing cream doesn't remove the piercing sensation entirely — it simply makes it less intense."* Compliant, trust-building, and they only say it once. Senseless can build a whole voice on it.
3. **"Is this legal?" answered properly.** `serp-overview` (gb) surfaces *"Is tattoo numbing cream illegal in the UK?"* in the People-Also-Ask on the head term. No claim-heavy competitor can publish a credible answer.
4. **The refusal pattern as a content format.** `/pages/does-numbing-cream-work` and `/pages/how-long-numbing-cream-lasts` already rank on the query and satisfy it with a framework. Extending that to tattoo converts the banned ~650/mo from "lost" to "answerable honestly by us and dishonestly by everyone else".

**The GEO lesson that settles the schema argument: Emla is the most-cited domain in the category** (ChatGPT 51, AI Mode 68, AI Overviews 41, Copilot 28, Perplexity 23) **with zero FAQPage, Product, Review or HowTo schema** — purely question-shaped headings and direct prose answers. Schema is table stakes. Structure and honesty are the lever.

---

## 4. CONTENT PLAN

Ordered by value-to-effort. "Widen" beats "net-new" wherever it appears.

### #1 — Delivery page · NET-NEW · unblocked by every gate
- **Type:** utility page, indexable · **Working title:** `Numbing Cream Delivery — UK Next Day Dispatch | Senseless`
- **Primary kw:** `numbing cream next day delivery` (200, KD 0, verified). Widen post-gate to `tattoo numbing cream next day delivery` (250, KD 0)
- **Intent:** transactional, zero product claim · **IA:** `/pages/delivery`, footer + PDP shipping accordion
- **Why first:** `/pages/delivery`, `/pages/shipping`, `/pages/shipping-returns`, `/pages/delivery-returns` **all 404**; only the native `/policies/shipping-policy` exists and it is **not in the sitemap**. TattooNumbx holds **#1** on the tattoo variant with a page carrying 0 backlinks. Pure logistics — the only page on this list with no compliance surface at all
- **Compliance:** clear

### #2 — The tattoo collection · NET-NEW · **ONE collection, not two** · gated on G1/G5/G6
- **Type:** collection, 8th sibling on the existing procedure axis
- **Working title:** `Tattoo Numbing Cream UK — Three Strengths | Senseless` (mirrors the live `Numbing Cream UK — Three Strengths | Senseless`)
- **Primary kw:** `tattoo numbing cream` 10,000 KD 0 · secondary `numbing cream for tattoos` 5,800 KD 1, `tattoo numbing cream uk` 1,900 KD 1
- **Why one page:** the head-term SERPs are **identical** — same AI Overview, same nine sources, Amazon #2, TattooNumbx #4, Superdrug/Emla and Valhalla in both. Ahrefs' different parent topics are a modelling artefact
- **Handle — open fork, needs a call:** `/collections/numbing-cream-for-tattoos` matches the seven live siblings; `/collections/tattoo-numbing-cream` matches the head term **and is a live Totally Numb URL**. Both 404 on senseless.uk today
- **Build order is not optional:** clone `templates/collection.numbing-cream-for-microneedling.json` (10 sections, injectable-clean) **before** the collection exists, or the live URL renders a stock Horizon grid. **Never clone the Botox template.** Alternative: create unpublished
- **Population — the cheapest lever in the project:** product metafield `senseless.recommended_procedures` (definition `429332955484`, `list.single_line_text_field`, no validations). Add `"Tattooing"` via `metafieldsSet` — no schema change. It renders nowhere in the theme (grep: 0 hits in `templates/`, `sections/`, `snippets/`) so it cannot leak an injectable link. **Gap to fix in the same pass: 7 of 16 products carry no procedure metafield** — the Foaming Cleanser, the A&D ointment and **all 5 bundles**, i.e. the highest-AOV items and the ones a multi-session client most needs
- **Format terms live as sections inside this page, not as separate pages:** `tattoo numbing spray` (400, KD 0) and `tattoo numbing gel` (100, KD 0, TP 4,100) both carry the parent topic "tattoo numbing cream". Senseless ships a real 35ml spray and 15ml/35ml gels; GetNumbd's spray URL 404s and Tattoo Numbing Cream Co. sells no gel. **No top-10 result for "tattoo numbing gel" is actually about a gel**
- **Compliance:** needs rewording. Category noun in slug/title/meta only; H1 must not use "numbing" as an effect. **This is a new ad-facing surface** — zero links to `numbing-cream-for-injections` / `-lip-fillers` / `-botox`, including in related rows, "see all", and schema `isSimilarTo`. Re-run the injectable-clean sweep after (baseline: **0 breaches across 14 surfaces**)

### #3 — Tattoo aftercare cluster · NET-NEW · lowest risk on the list
- **Type:** 1 collection + 2 guide articles
- **Working titles:** `Tattoo Aftercare UK | Senseless` · `Tattoo Aftercare: The First 48 Hours` · `Tattoo Healing Stages, Day by Day`
- **Primary kw:** `tattoo aftercare` **9,700, KD 2, CPC $0.07, traffic potential 6,400**, global 61,000 · secondary `tattoo aftercare cream` 1,400
- **IA:** aftercare axis off the tattoo collection. Merchandise the **Foaming Cleanser 35ml** and the **Vitamin A&D ointment 4-pack** — both already in range, both already imply this positioning (the Notion Pages DB row for the A&D ointment already targets *"tattoo aftercare ointment"*)
- **Compliance: clear.** Washing, moisturising and healing never touch the anaesthetic line. This is the single best risk-adjusted move on the list and nobody has costed it

### #4 — Widen `/pages/how-to-apply-numbing-cream` · WIDEN
- Template already has cream/spray/gel step blocks, a **"By procedure"** rich-text band, 7 FAQs and `"emit_howto": true` (`templates/page.how-to-apply-numbing-cream.json:64` — the only template with it)
- **Primary kw:** `how to use tattoo numbing cream` 70 · `how to apply tattoo numbing cream` 50 · `how long to leave numbing cream on for tattoo`
- **Add:** a tattoo row to the existing band, a tattoo FAQ, and a tattoo step in the HowTo
- **Compliance: clear, and uniquely so.** Decision `39158bc3-75ea-8181` permits concrete timing framed as directions for use **on application-guide surfaces**. Use *"as a general guide, allow 45–60 minutes… your **artist's** window takes precedence."* **Do not migrate timing to a PDP direction block** — `docs/COMPLIANCE.md` says that needs its own decision

### #5 — The two tattoo FAQ deflections · WIDEN · one field each · gated on G1
- `templates/collection.aesthetic-numbing-cream.json:282` — *"Can I use Senseless for tattoos?"* currently answered *"Senseless is a cosmetic topical preparation, formulated in the UK and CPSR assessed. Always follow the directions for use."* It never answers the question
- `templates/page.strongest-numbing-cream.json:177` — *"Is this the same as the strongest numbing cream for tattoos?"* pivots to the strength guide
- **These are the site's only tattoo signal and both currently read as no.** Cheapest edit on the site — but the answer is an **intended-use statement inside the CPSR claim envelope**, so it is gated on G1, not on a `compliance-check` pass

### #6 — Sitewide positioning copy pass · WIDEN · gated on G1
Highest reach per character. **The copy cannot go first — widening "Made for aesthetics" *is* the intended-use change.**
- `sections/senseless-footer.liquid:210` — tagline default *"UK-formulated topical preparation for aesthetic and cosmetic procedures."* renders on every page
- **"Made for aesthetics" — 33 occurrences across 28 files**; triple-homed in `docs/SECTIONS.md:15`, `DECISIONS-LOG.md:125` and Notion Confirmed Fact `38e58bc3-75ea-8109-a8b6-fbb8b2df9d2b`
- `snippets/meta-tags.liquid:41, :45` — homepage meta
- `templates/page.llms-txt.liquid:4` — *"formulated for aesthetic and cosmetic procedures"*. Disproportionate GEO leverage per character
- `templates/page.trade.json:85` — currently tells non-aesthetic practices *"Senseless is formulated for aesthetic procedures"* and routes them to Emla or Ametop. **A tattoo studio is not an aesthetic clinic; this page currently sends the exact B2B buyer this pivot targets to a competitor**
- `templates/page.senseless-vs-ametop.json:44` (closed list, *"the aesthetic catalogue"*), `templates/page.about.json:8` (*"Aesthetics is the specialism — not the side category"*)
- **Do NOT touch:** `sections/senseless-comfort-compare.liquid:22` (*"It is a cosmetic preparation, not an anaesthetic"*) — that line is what keeps the product on the cosmetic side of the MHRA line. `templates/page.faq.json` is legal-signed and goes back to legal separately
- **G8 — the naming frame.** The whole procedure axis is named *aesthetic* (`/pages/aesthetic-procedures`, `/collections/aesthetic-numbing-cream`). **Do not re-slug indexed URLs** — widen the copy and add a tattoo destination

### #7 — Tattoo objection Q&A cluster · NET-NEW · 5 blog articles
`/blogs/guides` has 5 articles, all Botox/filler. The articles hub auto-includes new blog articles; guide *pages* need a manual block plus deploy — **so a blog article is the cheaper home.**
1. `Does Numbing Cream Affect a Tattoo?` — the "affect the ink / the healing" sub-cluster. **Strategically the best item on the list**: it is the question the *artist* asks, it is answerable from formulation and CPSR fact with no effect claim, and no competitor answers it properly
2. `Can You Use Numbing Cream Before a Tattoo?`
3. `Do Tattoo Artists Use Numbing Cream?` — **the only search-visible door into the artist conversation**
4. `Where to Buy Numbing Cream for Tattoos in the UK`
5. `What to Tell Your Artist About Numbing Cream` — studio etiquette, no competitor coverage at all
- **Compliance: clear.** Formulation, safety and etiquette fact only

### #8 — Tattoo pain chart · NET-NEW · **the build thesis is reversed** · gated on legal
- **Primary kw:** `tattoo pain chart` **6,900, KD 1, TP 2,600**, global 60,000. `tattoo pain chart female` 900/mo means **a gender toggle is a ranking feature, not a nicety**
- **The linkable, rankable artefact is a properly-made static graphic, not the interactive tool.** Healthline's static PNG: **263 referring domains, 2,915 GB traffic**. Totally Numb's interactive SVG: **UR 4.6, 0 refdomains, 0 backlinks, 0 organic traffic, 0 organic keywords**. Applestan interactive: 0. **No interactive pain chart anywhere has earned a single genuine link** — lifestyle and tattoo press link to pain charts readily, they have only ever had static images to link to. Build the tool for users; ship the graphic for links and for the image pack (**position 1 on the GB head term is a 12-slot image pack**; the first organic result is position 3)
- **Design rulings, non-negotiable, all from GN8 primary source:** no region → product mapping in any form (no compliant version exists — the mechanism *is* the claim, and it is worse for us than for Totally Numb because Bronze/Silver/Gold/Platinum is semantically empty while Clinical/Advanced/Professional is an explicit ascending ladder: "Ribs → Professional" states a dose-for-pain relationship in two words). **Qualitative bands only, no 0–10 scale** — reuse the live vocabulary from `sections/senseless-comfort-compare.liquid:4-5`, **Mild · Moderate · Sharper**. **No distress imagery** — neutral line-art, brand palette, no red heat-map, no wincing figure. Never merchandise it as a category: `/pages/tattoo-pain-chart`, never `/collections/tattoo-pain-relief`. No reviews module on the page. And note the theme's own history: `sections/senseless-pain-scale-slot.liquid` was **deleted** and its anchor renamed `#pain-scale` → `#comfort`
- **Beat Totally Numb on the things it fails:** their bands are **colour-only** (`aria-label="Rib cage"` carries no sensitivity information — screen-reader users get nothing); band contrast is **1.31:1 and 1.12:1** against a WCAG 1.4.11 requirement of 3:1; a dead CSS rule means the active Front/Back tab never highlights (`[aria-selected=true]` styled, `aria-pressed` set); tap targets fail WCAG 2.5.8 at 200px desktop width for 29 regions; and **with JS off the back of the body is unreachable**
- **What we cannot do:** cite the research as the differentiator. GN8 §4/App.10 list *"publication of third-party articles, reports, clinical data, medical research"* as an implied medicinal claim on a selling domain. Separately: **there is no published dataset of tattoo pain by body region.** The only large study — Witkoś 2020, n=1,092 — found **body area was NOT a significant predictor** (p=0.094 during, p=0.742 after). Every chart online, Healthline's included, asserts a ranking the evidence does not support
- **The UK bar is low:** `stretchitbodyjewellery.co.uk` ranks #10 on **DR 38 with exactly 1 referring domain**, pulling 587–610/mo

### #9 — Piercings collection · NET-NEW · medium
`numbing cream for piercings` **450, KD 0, traffic potential 19,000** — the highest TP of any single term measured. Missing 9th procedure collection, same studio audience. Tattoo Numbing Cream Co.'s piercings page is 910 words and only reaches position 17.

### #10 — Widen the two refusal pages · WIDEN
`/pages/does-numbing-cream-work` and `/pages/how-long-numbing-cream-lasts` already rank on a question and answer it with a framework. Add tattoo-qualified variants. This is the only mechanism that converts the banned ~650/mo into something we can honestly compete for.

### #11 — Widen `/pages/aesthetic-procedures` · WIDEN · blocked on a block cap
Adding a Tattooing card is what connects the new collection to the procedure axis. **But `senseless-trio-card-row` is at `max_blocks: 4` and full** — and that component is used by 24 sections across 15 templates, so raising the cap has a blast radius. `/pages/does-it-hurt` `senseless-link-row` is at 8/8 with two more rows at 7/8.

### #12 — TKTX comparison page · NET-NEW · medium
`tktx numbing cream` 6,600 KD 17 — **the real category incumbent, and the owner named three competitors without naming it.** Match the existing `/pages/best-emla-alternative-uk` pattern. Compare only on UK CPSR assessment, INCI disclosure, registered UK company, format range, pack sizes, price per gram, delivery. **Never on how well it works.**

### Do NOT build
- **Tattoo terms on PDPs.** Cannibalisation, and it breaches the 7 Aug collection-carries-category-keywords ruling.
- **A trade/wholesale SEO strategy.** GB demand is effectively nil: `numbing cream wholesale` 0, `numbing cream for tattoo artists` 0, `tattoo numbing cream wholesale` 0. The only terms with volume (`tattoo supplies` KD 60, `tattoo supplies uk` KD 59) are the hardest in the dataset and belong to equipment distributors. `/pages/trade` gets fixed as copy (#6) and internally linked — it is not a search target.
- **Anything in `templates/page.faq.json`.** The legal exception is page-scoped. Adding tattoo Q&A there breaks the scope of the sign-off.
- **A second GEO programme.** KD is 0–1 across the cluster and the AI-cited pages are the same pages. **The same asset wins both.**

---

## 5. SEO PLAN

### Target map — one term, one page

| Term | GB vol | KD | Owning page | Type |
|---|---|---|---|---|
| tattoo numbing cream | 10,000 | 0 | `/collections/[tattoo handle]` | collection |
| numbing cream for tattoos | 5,800 | 1 | same collection (identical SERP) | collection |
| tattoo numbing cream uk | 1,900 | 1 | same collection | collection |
| best / strongest tattoo numbing cream | 1,500 + tail | 1 / 0 | **contested — needs a call** | see below |
| tattoo numbing spray | 400 | 0 | section + anchor inside the tattoo collection | collection |
| tattoo numbing gel | 100 | 0 | section + anchor inside the tattoo collection | collection |
| tattoo numbing cream next day delivery | 250 | 0 | `/pages/delivery` | utility page |
| numbing cream next day delivery | 200 | 0 | `/pages/delivery` | utility page |
| tattoo aftercare | 9,700 | 2 | `/collections/tattoo-aftercare` | collection |
| tattoo aftercare cream | 1,400 | 0 | same collection | collection |
| tattoo pain chart (+ female) | 6,900 + 900 | 1 / 4 | `/pages/tattoo-pain-chart` | guide page + image pack |
| how to use / apply tattoo numbing cream | 70 + 50 | 0 | `/pages/how-to-apply-numbing-cream` | widen |
| does numbing cream affect tattoos | ~310 cluster | 0–1 | blog article | net-new |
| do tattoo artists use numbing cream | 50 | 0 | blog article | net-new |
| numbing cream for piercings | 450 | 0 | `/collections/numbing-cream-for-piercings` | collection |
| tktx numbing cream | 6,600 | 17 | `/pages/senseless-vs-tktx` | landing page |

**The one unresolved conflict — resolve before building.** `~2,240/mo` of "best/strongest tattoo numbing cream" is contested between the new collection and `/pages/strongest-numbing-cream`, whose **live title is already "Best & Strongest Numbing Cream UK | Senseless"**. The 7 Aug ruling covers **collection vs PDP**; it says nothing about **collection vs commercial landing page**. My recommendation: the landing page keeps the superlative terms (it already has the refusal copy that makes them shippable) and the collection takes the category-noun terms. But that is a call to make explicitly, not by default.

### Internal linking

- Tattoo collection ← from nav, homepage, `/pages/aesthetic-procedures` (blocked on the block cap), format collections, articles hub.
- Tattoo collection → application guide, tattoo aftercare collection, delivery page, pain chart. **Zero links to the three injectable collections.**
- **Do not point the tattoo collection at `/pages/does-it-hurt-by-treatment`.** It links all three injectable collections and is the shortest path from a nav destination to injectable content. SPMU and waxing collections already link there. **Give tattoo its own guide instead.**
- Blog articles → collection, on the pattern Tattoo Numbing Cream Co. uses consistently (an inline "Shop" module high in the body).
- Re-run the `.claude/rules/ad-facing.md` sitemap anchor check after every nav, collection, homepage or landing-page change. **Baseline is 0 breaches across 14 surfaces — any breach after this work is attributable to it.**

### Authority

**Links are not what gates entry, and the standard link-gap play does not exist here.** `skinartdepot.co.uk` holds position 6 for "best tattoo numbing cream" on **DR 0, 0 backlinks, 0 referring domains**. And the intersect of domains linking to two or more competitors is **15 domains, every one a platform artefact, scanner profile or junk directory** — apple.com, myshopify.com, scamadviser.com, seogeko.shop, findit.co.in and similar. There is no shared editorial ecosystem to mine. **Sequence accordingly: build the pages first, chase roughly ten genuine links second.**

**Before any of that — deal with what is already pointed at the site.** `site-explorer-refdomains-history` (monthly): **May 8 → Jun 34 → Jul 120 → Aug 164**. The largest anchor by referring domains is a link-vendor solicitation on **43 domains / 54 links** (first seen 2026-06-22), and there is an exact-match commercial anchor burst all first seen **2026-07-14 to 07-16**. Of 160 live referring domains, **3 are non-spam**: `creativeposts.top` (0 dofollow), the group's own `matrixhealthgroup.co.uk`, and `backlinkengine.shop` — which appeared **on 2026-08-12**, i.e. it is still arriving. Nothing in the repo records anyone commissioning it. **Ask who is paying, stop it, consider a disavow.**

**The ten links worth pursuing** — all from Tattoo Numbing Cream Co.'s profile, since it is the only competitor with any earned links. **Flag: this target list is single-sourced and was not re-verified by the adversarial pass** (see §8).
1. **standard.co.uk ES Best** (DR 89) — the "Best tattoo numbing creams" roundup, author Tania Leslau, dated 2023-10-09. Three of its five featured products are lidocaine medicines, so "the UK CPSR-assessed cosmetic option" is genuinely differentiated. Supply a compliance-checked fact sheet and explicitly ask them not to attribute onset or duration to the brand
2. **inkl.com** (DR 73) — syndicates the Standard piece, comes free
3. **inkedmag.com** (DR 71) — "Inked Recommends" product seeding
4. **A UK tattoo-supply stockist** — one relationship gave them 81 dofollow links from a single DR 34 domain
5–8. **UK studios, artists and expos** — the largest structural gap. Their whole roster is Australian or tiny; Totally Numb and GetNumbd have **zero** domains of this type. Doubles as a GEO play: the head-term AI Overview cites tattoo-studio blogs
9. **Awin** — one merchant signup produced 192 dofollow links for them. Affiliate creatives are brand-controlled, so every one must clear `compliance-check`
10. **Trustpilot + ProvenExpert** — free, and `uk.trustpilot.com/review/extreme-numbing.com` **ranks position 7** for "best tattoo numbing cream". A profile is a link *and* a SERP slot. Senseless holds Judge.me 4.9 and it is invisible on the platforms that rank

**Do not pursue:** paid press-release syndication (18 domains from one release, all bare-URL anchors to the homepage, and after a year their top page still has 3 backlinks); paid guest posts on lifestyle blogs (this is the vendor category currently pointing 157 spam domains at senseless.uk, and one of their anchors is literally *"effective numbing cream for tattoo sessions"* — an efficacy claim published on the brand's behalf that cannot be retracted); hijacked .gov/.edu.

**Broken-backlink reclamation is a dead end.** Every "broken" row Ahrefs returns for all four domains actually resolves 200. `senseless.uk` returns an empty array — nothing to reclaim.

### The gap nobody costed: no social presence at all

The homepage has **no Instagram, TikTok, YouTube, Facebook or Pinterest link**. **UGC occupies 7 of the top 30 results on the GB money terms**, and the bar is trivial — an Instagram Reel with 56 likes ranks #24; a brand YouTube video with 6,694 views ranks #9. Brand share-of-voice across five tattoo subreddits: TKTX 100 (capped), Bactine 100 (capped), Emla 49, Hush 41, Zensa 30 — **Senseless 0**. Note `r/tattooadvice` (1.6m subscribers) is the venue but **there is no viable UK tattoo subreddit** (`r/uktattoo` has 3 subscribers), so Reddit is a global play, not a UK one. The UK conversation is in Facebook groups. **Do not seed Reddit** — it breaches CAP and platform rules. Social profiles are needed regardless, because `sameAs` cannot be written without them (§6).

---

## 6. GEO PLAN

**Start from the right premise: Senseless already emits more schema than every competitor in the set, and is cited twice.** Coverage is not the gap. Four things are.

### Gap 1 — No entity graph (highest priority, zero compliance surface)

`sameAs` count across 9 live pages: **0**. `@id` count: **1**, and it is incidental. `Organization` appears on only 2 of 9 page types.

Restructure `snippets/senseless-structured-data.liquid` to emit one `@graph` on every page type with stable `@id`s: `https://senseless.uk/#organization`, `#website`, `<page url>#webpage`, `<product url>#product`, `<page url>#faq`, `<page url>#breadcrumb`. Then cross-reference instead of duplicating — `WebPage.isPartOf` → `#website`, `Product.brand` / `Product.manufacturer` / `Offer.seller` / `Article.publisher` → `#organization`.

Organization properties to add (extend `:139` and keep `sections/senseless-org-schema.liquid:6` identical):

| Property | Value | Compliance |
|---|---|---|
| `@id` | `https://senseless.uk/#organization` | clear |
| `@type` | `["Organization","OnlineStore"]` | clear |
| `sameAs` | real profile URLs — **currently zero and none exist to write**; blocked on the social gap in §5 | clear |
| `identifier` | `[{"@type":"PropertyValue","propertyID":"GB-COH","value":"17099304"}]` | clear |
| `vatID` | `GB523781682` (already present) | clear |
| `foundingDate`, `foundingLocation`, `numberOfEmployees` | factual | clear |
| `logo` | upgrade string → `ImageObject` with width/height | clear |
| `knowsAbout` | `["Topical cosmetic preparations","Tattoo appointment preparation","Semi-permanent makeup preparation","UK Cosmetic Products Regulation","Cosmetic Product Safety Reports"]` | clear — category nouns only |
| `description` | see draft below | **⚠ gated on G1** |

**Draft `description` — machine-quotable, so treat it as ad copy. Spec, not final:**
> *"Senseless is a UK brand of topical cosmetic preparations — cream, gel and spray — in three strengths, designed for use before tattooing, semi-permanent makeup, waxing, laser and aesthetic appointments. Formulated in the United Kingdom by Matrix Health Group Ltd and assessed under a UK Cosmetic Product Safety Report. A cosmetic product, not a medicine."*

Adding tattooing here is an **intended-use statement inside the CPSR claim envelope** — it needs G1's answer, not a `compliance-check` pass. The same sentence is the one-line rewrite for `templates/page.llms-txt.liquid:4`, which currently reads *"formulated for aesthetic and cosmetic procedures"* and is the brand definition served to AI crawlers.

**Do not use `hasCredential` or `award` for the CPSR.**

### Gap 2 — Product node has no identity or composition

Keep everything present (Product, Brand, AggregateRating 4.88/207, Offer, OfferShippingDetails, MerchantReturnPolicy — this is already richer than either competitor). Add: `@id`, **`sku` at Product level** (currently Offer-level only), `gtin13` (guarded on `variant.barcode`), `category: "Health & Beauty > Personal Care > Cosmetics > Skin Care"`, `inLanguage: "en-GB"`, `countryOfOrigin`, `itemCondition`, `priceValidUntil`, `mainEntityOfPage`, `isSimilarTo` (tier ladder), and `additionalProperty` carrying Format, Strength tier, Size, **Ingredients (INCI)**, Regulatory status, Country of formulation.

**Blocking prerequisite: there is no INCI anywhere on the site, and the PDP promises one.** `templates/product.json:220` says *"Full ingredients list available on the packaging and below"* and nothing renders below. The theme reads only four product metafields — `reviews.rating`, `reviews.rating_count`, `senseless.bundle_contents`, `senseless.format`. Create `senseless.inci` per SKU, render it visibly, mirror it into `additionalProperty`. **This is the most defensible differentiator available and it needs content from the safety assessor, not code.**

**Never emit:** `Drug`, `MedicalEntity`, `Substance`, `activeIngredient`, `mechanismOfAction`, `TherapeuticProcedure`, `MedicalCondition`, or any medical Google product category. GetNumbd's Super Strength PDP declares `"category": "Medical Tape & Bandages"` — for Senseless that is a compliance incident, not a data-quality one, and `docs/COMPLIANCE.md` already forbids it. *(Correction applied: their Ultra+ PDP declares `"Makeup"`. The mistake is on one SKU, not their pattern.)*

**Never emit individual `Review` objects.** Keep `AggregateRating` only. A marked-up review body saying "I didn't feel a thing" is a Hard Rule breach in the most quotable possible form, and the 2 Jul legal decision to leave published reviews as-is governs *display*, not *structured emission*.

**`isSimilarTo` is a link.** On any tattoo-facing PDP it must not resolve to the three injectable collections.

### Gap 3 — 8 live page templates emit no `WebPage` node

13 of 26 page templates lack `senseless-page-schema`. Two are covered elsewhere (`page.policy.json`, `page.articles.json`) and three 301 away (`choosing-your-format`, `choosing-your-strength`, `how-it-works` — carried from the gap analysis, not re-verified by me). That leaves **8 live templates with no WebPage node**, including **all three ad-facing commercial landing pages** (`strongest-numbing-cream`, `best-emla-alternative-uk`, `senseless-vs-ametop`) and **both refusal pages**.

Fix in the `{%- when 'page' -%}` branch of `snippets/senseless-structured-data.liquid` (currently breadcrumb only, lines 134–135) so no template can be missed, with `senseless-page-schema.liquid` overriding rather than supplying.

### Gap 4 — Thin extraction surface (the one that actually earns citations)

Across 9 live pages: **0 `<table>`, 0 `<time>`, 0 author markers.** Question-shaped headings: article 2/16, collection 2/17, PDP 0/15, FAQ page 0/10, how-to 0/18.

| Change | File | Effect |
|---|---|---|
| `<summary class="ss-faq__q">` → `<summary><h3 class="ss-faq__q">` | `sections/senseless-faq-accordion.liquid:49` | **One edit turns 44 templates' worth of Q&A into question-shaped headings.** The FAQ page carries 26 marked-up questions and 0 question-shaped headings today |
| `dateModified` hardcoded to `published_at` | `sections/senseless-article.liquid:125` (identical to `:124`) | Genuine revision never registers. Point at an article metafield. Tattoo Numbing Cream Co. **fakes** freshness by re-stamping 198 of 303 sitemap URLs to one date — we can have the real thing and are discarding it |
| `"author": {"@type":"Organization"}` | `sections/senseless-article.liquid:126` | Change to `Person` + `reviewedBy`. **⚠ Do not title the reviewer "medical reviewer", "clinical reviewer" or "pharmacist"** — on a cosmetic that is medicinal-by-presentation framing. Use *"Reviewed for regulatory accuracy by [name], Regulatory & Compliance, Matrix Health Group Ltd"* |
| Visible "Last updated" has no `<time datetime>` wrapper | `sections/senseless-article.liquid:59` | Add it |
| Collection description truncated at 300, Product at 1200 | `snippets/senseless-structured-data.liquid:115` vs `:38` | Raise to 1200. The rationale documented at `:31-37` applies identically |
| `ItemList` carries name+url only | `snippets/senseless-structured-data.liquid:120-127` | Add a real `item` with Product `@id`, image, brand ref and an Offer with price/availability. Lets an engine answer "what does the tattoo range cost" in one fetch |
| No comparison table anywhere | tattoo collection | **First `<table>` on the site.** Axes: **strength tier × procedure × area size × format × pack size × price per gram.** Never onset, duration or intensity |
| `HowTo` has no `@id`, `supply`, `tool`, step URLs | `sections/senseless-how-to-use.liquid:80` | Add. `totalTime: "PT60M"` is **directions-timing in machine-readable form** — permitted on the application guide under Decision `39158bc3-75ea-8181`, gated by a section setting, **nowhere else**. `emit_howto` on PDPs is currently correctly **off**; leave it off |

### Two live PDP FAQ strings that need a ruling before they are copied to tattoo surfaces

1. *"Many customers tell us they **get their best results** applying around 45–60 minutes before their appointment."* The 45–60 timing has its own decision (`39158bc3-75ea-81f7`). **"Best results" is a separate problem** — an efficacy word, in structured data, customer-attributed, and `docs/COMPLIANCE.md` states attribution "never licenses an effect or safety claim". Suggested rewrite: *"Many customers tell us they apply around 45–60 minutes before their appointment. Timing varies — follow the product guidance and your practitioner, whose window takes precedence."*
2. *"the tiers are formulated to match the **session lengths** they're built for."* No number, but it asserts a duration relationship as a brand claim. Compliant alternative, verbatim from the approved three-tier table: *"Clinical for shorter, routine appointments; Advanced for longer or more sensitive work; Professional for the most demanding sessions."*

### Plumbing

**The bespoke llms.txt is unreachable by agents** — `/pages/llms-txt` carries `noindex,nofollow`, it is absent from the sitemap, and `/llms.txt` returns 200 serving Shopify's generated agent boilerplate instead of `templates/page.llms-txt.liquid`. Pure plumbing, no compliance surface. *(Single-sourced from the gap analysis; not re-verified by the adversarial pass.)*

**Do not chase `agents.md` / `sitemap_agentic_discovery.xml`.** It looks like a sophisticated competitor GEO play and it is Shopify platform boilerplate — senseless.uk already has the identical file.

**Robots is already right.** `templates/robots.txt.liquid:20` explicitly allows 12 AI crawlers. Tattoo Numbing Cream Co. has no AI-crawler rules at all. Crawlability is not the constraint.

---

## 7. THE ORDER OF WORK

One task per session. Gates in **bold** block everything downstream of them.

**SESSION 1 — the gate pack. No code, no copy, no deploy.** This is precisely: get written answers on (a) **G1** — what the CPSR actually declares as intended use, application site, exposure assumption and target population, and whether Senseless CPSRs trace to Totally Numb's certifications (if they do, and Totally Numb is the tattoo brand, tattoo may already be squarely in scope — **one email could close this**; Daniel's "the certs have been updated" is verbal only and no written scope exists anywhere in repo or Notion); (b) **G2** — whether `"Apply to clean, unbroken skin."` can change; (c) **G5** — the Senseless-vs-Totally-Numb lane decision; (d) **G6** — ad-facing or organic-only. In the same session: raise a **Compliance Hold** on the tattoo keyword set (precedent: the Applied EMLA hold, row `3b158bc3-75ea-8183-ae67-c6d305610682`), log a Decisions row capturing both the 21 May aesthetics-only position and its reversal (**there is no predecessor row to supersede** — the Decisions DB and `DECISIONS-LOG.md` contain zero tattoo decisions), and escalate the two items that outrank this work: **the bought-link package** and **the review corpus**. Notion write-back — the State Surface and Decisions DB currently have **no record of this brand change**, and the 21 May *"NOT for tattooing"* page sits in the **Matrix Health Group** tree where a Senseless write-back will not sweep it.

**SESSION 2 — `/pages/delivery`.** Generic, no tattoo word, gated on nothing. Ship the page that a competitor holds #1 with while we have no indexable equivalent.

**SESSION 3 — GEO batch 1: the entity graph.** `@graph`, `@id`s, `identifier`, `Organization` on every page, default `WebPage` node in the page branch. No copy, no claims. `sameAs` left as a stub until social profiles exist.

**SESSION 4 — GEO batch 2: the extraction surface.** `<summary>` → `<h3>`, `dateModified`, `<time datetime>`, named `Person` author, `ItemList.item`, collection truncate 300 → 1200. Structure only.

**SESSION 5 — tattoo collection scaffolding, unpublished.** Clone `collection.numbing-cream-for-microneedling.json` to the tattoo handle. Add `"Tattooing"` to `senseless.recommended_procedures` on all 16 products via `metafieldsSet`, closing the 7-product gap in the same pass. Create the collection **unpublished**. Nothing goes live.

**⛔ GATE — G2 must be answered before Session 6.**

**SESSION 6 — the unbroken-skin resolution.** `sections/senseless-safety-warnings.liquid:22` reads *"Apply to clean, unbroken skin."* — deliberately hardcoded and non-editable, covering **9 cream/gel/spray SKUs + 5 kit PDPs**, and duplicated in Admin `body_html` on **10 of 16 products**, so a theme-only fix leaves it live. Tattooing is the deliberate breaking of skin, and the category norm — already published by Totally Numb — is re-application **during** the session onto open skin. Either the safety assessor changes it, or it stays and **every tattoo page must be written inside that limit**. Also close the related defect: three collection FAQs say *"Take extra care on sensitive or broken skin"* on the same page as the locked warning.

**⛔ GATE — G1, G5, G6 must be answered before Session 7.**

**SESSION 7 — sitewide positioning copy pass.** Footer tagline default, the 33 "Made for aesthetics" occurrences across 28 files plus their three canon homes, homepage meta, `page.llms-txt.liquid:4`, the `page.trade.json` refusal, `senseless-vs-ametop`, `page.about.json`, and the two tattoo FAQ deflections. Every string through `compliance-check`. Do not touch `senseless-comfort-compare.liquid:22` or `page.faq.json`.

**SESSION 8 — publish the tattoo collection.** Copy pass, `compliance-check`, publish, re-run the injectable-clean sweep against the 14-surface baseline, and fix `.claude/skills/redirects/SKILL.md:17-18` which uses a **live Totally Numb URL** as a worked from-path.

**SESSION 9 — tattoo aftercare cluster.** Collection + two guides. Lowest MHRA exposure on the list, 9,700/mo at KD 2, products already in range.

**SESSION 10 — widen the application guide.** Tattoo row in the "By procedure" band, tattoo FAQ, tattoo HowTo step, "your artist's window takes precedence".

**SESSION 11 — the objection Q&A cluster.** Five blog articles in `/blogs/guides`. Verdict-first answers, FAQPage on each.

**⛔ GATE — legal sign-off on the GN8 design rulings before Session 12.** This is a sign-off on the *page concept*, not a `compliance-check` on the sentences.

**SESSION 12 — tattoo pain chart.** Static graphic first (that is the linkable, rankable artefact), gender toggle, Mild/Moderate/Sharper bands, **no region → product mapping**, no red heat-map, neutral line-art. Interactive tool second, built on the `sections/senseless-selector.liquid` pattern — native radios in a fieldset, DOM as state, one inline IIFE, ES5, no framework. Watch the 25-character schema `name` cap; `Senseless — Comfort map` fits at 23.

**SESSION 13 — INCI, then authority and social.** INCI metafield + visible PDP block + `additionalProperty` (needs the safety assessor's content). Then Trustpilot, ProvenExpert, Awin, the first social profiles to unblock `sameAs`, and UK studio/trade outreach.

**Two operational notes.** Ahrefs was at ~105k of 400k monthly units and resets **2026-09-09** — check `subscription-info-limits-and-usage` before any session that queries it heavily, and **do not re-run any of the four completed research strands.** Every session ends with `commit-and-deploy` and a Notion write-back; deploy runs under `bash`, never zsh.

---

## 8. WHAT IS STILL UNKNOWN

Carried through verbatim. Nothing here is resolved and nothing has been dropped.

### Corrections already applied to the numbers above (so they are not re-introduced)
- getnumbd.com GB paid was reported as *paid_keywords 85, paid_traffic 4,509, ~$3,644/mo* — **actual: 84 / 1,284 / $1,063.08**, identical with and without a country filter. Traffic overstated 3.5x, spend 3.4x.
- totally-numb.com GB paid was reported as *40 / 4,318 / ~$3,604/mo* — **actual: 39 / 1,263 / $1,161.05**.
- Tattoo Numbing Cream Co. blog slugs were reported as *251 "tattoo", 84 "numb", 123 question-shaped* — **actual: 250 / 83 / 114**. 53 containing "pain|hurt" is exact. A naive grep of the full URL returns 303/303 because the domain contains both words.
- hushanesthetic.com GB: reported *AI Mode 101/53, AIO 43/28* — **actual 102/53 and 43/27**. Crawl drift.
- senseless.uk refdomains Aug 2026 reported as 163 — **actual 164**, and there are now **3** non-spam referring domains, not 2: `backlinkengine.shop` appeared **2026-08-12T18:09:50Z**, i.e. the package is still arriving.
- senseless.uk all-time backlinks reported 410/259 — **actual 411/260**. Live 216/160 exact.
- tattoonumbx.com GB top pages reported *PDP 2,688, homepage 430, delivery 143* — **actual 2,679 / 424 / 132**. Spray PDP 284 exact.
- senseless.uk paid pages reported as two URLs — **`paid_pages` returns 1**. Low-confidence; `site-explorer-paid-pages` itself was not re-run.
- GetNumbd's `"category": "Medical Tape & Bandages"` is on the **Super Strength PDP only**; Ultra+ declares `"Makeup"`.
- The Totally Numb "bundle pricing is broken" finding is **false** — it compared Mini variants against Ultimate. Like-for-like, every configuration rises monotonically Bronze < Silver < Gold < Platinum. Deleted. The separate Spray Professional £24.99 vs Spray Platinum £29.99 anomaly **does** hold.
- Totally Numb's Product schema **does** carry `gtin13: "10795847725977"`. "No gtin" was wrong; the empty-string `description` finding is right.
- GetNumbd's *"deep numbing effect lasts up to 5 hours long"* is the **Ultra+ PDP only**; Super reads differently.
- GetNumbd's *"Numbing spray must never be used on unbroken skin"* is the **spray article only**; the gel article says gel.
- GetNumbd's collection word count is **~156–160**, not exactly 156 — methodology variance.

### Unsupported — do not launder these into any downstream document
- **"263 deduplicated terms / 36,190 per month GB", and the addressability split "ADDRESSABLE 176 terms / 28,200", "CONSTRAINED 55 / 6,310", "UNADDRESSABLE 32 / 1,680 / 4.6%".** Derived sums over multiple `keywords-explorer-matching-terms` calls plus a manual compliance classification. The method is stated and spot-checked volumes were accurate, but the totals are not reproducible from any single tool call and were not rebuilt. **The "4.6% of the market is unaddressable" headline is the single most decision-shaping number in the research pack and currently rests on unaudited arithmetic — rebuild it before it reaches the owner.** I have used the repo's first-party ~650/mo (~2.5%) instead.
- **The tattoo-pain (17,400/mo, 120 terms) and tattoo-aftercare (18,050/mo, 34 terms) cluster totals.** Anchor terms re-verified exactly; the cluster sums are floors over a volume threshold and were not reproduced.
- **The claim to have mapped "16 SERPs" with per-position detail.** Four were re-run and every position, DR and URL checked out exactly. The other twelve were not. Given that same report's paid metrics were inflated ~3.4x, its unverified SERPs deserve spot-checking.
- **The authority/backlink section beyond the senseless.uk figures** — the "15 domains linking 2+ competitors but not senseless.uk" intersect, and the 20–30 named link-gap targets with their DR values (standard.co.uk DR 89, inkedmag.com DR 71, awin.com 192 dofollow, elementtattoosupply.com 81 dofollow). The report body was truncated mid-sentence and `site-explorer-all-backlinks` was not re-run. **Unverified, not disproven.**
- **The Brand Radar provisioning claim** ("Missing addon" errors, Standard plan) — not re-tested. Self-consistent and low-risk, but the negative result was not independently reproduced.
- **The per-term long-tail listings** in the keyword reports (body-part clusters, the 32 named unaddressable terms with individual volumes). Head-term spot-checks were perfect; the long tail was not re-pulled term by term.
- **The GSC claims** — "0 GSC rows containing tattoo" (project_id 9963517) and the specific impression/position figures ("strong numbing cream uk" 120 impressions at position 37.6). The GSC endpoints were not queried. **Every report independently flagged that Ahrefs' 0-organic-keywords figure for senseless.uk should be cross-checked in Search Console before being presented as fact. That caveat is correct and still outstanding.**
- **Totally Numb's ~10% bundle saving.** The spot-check named the wrong variant (£68.99 is Bronze Mini/Spray, not Ultimate/Spray, and Ultimate/Spray at £81.99 exceeds the £75.97 component total). `products.json` does not publish per-variant bundle contents, so the saving could not be verified in either direction.
- **"Six of the fifteen visible entries reference tattoo explicitly"** on GetNumbd's review wall. The Judge.me widget rotates between fetches. The four individual quotes cited are present and confirmed; the ratio is not.
- **GetNumbd's review arithmetic** ("116 + 58 = 174 product-attributed; the 233 total includes the withdrawn gel and spray"). The 233 total and 4.4/5 aggregate are confirmed; attributing the remainder to withdrawn SKUs is inference — both URLs now 404 so the counts cannot be retrieved.

### Open from the repo record — nobody has verified these
1. **What the CPSR declares.** Certificates are not in the repo; no scope field exists anywhere. Only the safety assessor can answer.
2. **Ad-facing or organic.** Three sweeps flagged this as the question that determines everything downstream.
3. **What is inside the password-locked `senseless-tattooing.myshopify.com`** — possibly portable tattoo copy and imagery. Requires Daniel to lift the password.
4. **The ~22,500/mo GB informational cluster total** — a floor; 15 largest components individually confirmed, the summation not reproduced.
5. **Per-body-part GB volumes beyond "rib tattoo pain" (80, confirmed).**
6. **The "$18k/mo equivalent paid clicks" valuation** — the agent's own arithmetic, not a tool output.
7. **Totally Numb's chart build measurements** (29 zones, contrast ratios, tap targets) — curl/grep arithmetic, **no browser was driven**, so rendered appearance and focus behaviour are unobserved.
8. **Whether the Totally Numb chart page is indexed by Google at all.**
9. **Pan 2024 thenar pressure-pain figures — do not publish** until someone opens the full text.
10. **A Google double-serving policy breach** between the two group brands was investigated and is **UNVERIFIED**. The commercial self-competition is verified and is the real cost.
11. **Whether the two brands are actually in the same live auctions right now.** Both target "tattoo numbing cream" as top paid keyword, but Ahrefs paid data is sampled. Needs checking in the Google Ads accounts directly.
12. **Whether inbound third-party anchor text counts as brand-authored copy** under `docs/COMPLIANCE.md`. The ruleset does not answer it. `strongest numbing cream` and `professional strength numbing cream` are live as inbound anchors, unsigned-off.
13. **Whether the 157 spam refdomains warrant a disavow.** Not assessed. Real downside risk if judged wrongly.
14. **Whether tattoonumbx.com's #1-ranking delivery page is a 404.** The repo record says it is; the SERP data confirms it holds position 1 with 132 GB visits/mo. Unresolved — and it does not change the recommendation either way.
15. **Whether Senseless product variants carry barcodes** (the `gtin13` spec is guarded for this reason), whether an `article.metafields.custom.updated_at` exists for `dateModified`, and whether any age restriction applies. None confirmed.
16. **The Judge.me count discrepancy** — the live PDP `AggregateRating` reports 207 for Professional Strength Cream; project memory records 4.9/231 sitewide. Not reconciled.
17. **The llms.txt triple-lock** (noindex, absent from sitemap, root path hijacked by Shopify boilerplate) is single-sourced from one gap analysis and was not re-verified.
18. **Whether the three page templates said to 301** (`choosing-your-format`, `choosing-your-strength`, `how-it-works`) actually do. Carried from the gap analysis; I did not curl them.

### A fabrication caught in flight — flagged so it does not reappear
WebSearch's summariser produced *"a 2018 study in the Journal of Pain Research found average tattoo pain around 5.5 out of 10."* **It does not exist.** If that number appears in this project again, it has no source. The real published mean is **4.35** (Witkoś 2020, n=1,092).

### Canon defects to fix in passing
- `docs/BRAND.md:3` names an **archive-sealed** Notion page as its source of truth — same fault class fixed for `DECISIONS-LOG.md` in `bf891e6`.
- `docs/ARCHITECTURE.md:63` states old tattoo URLs "will have" been redirected. **This never happened and could not have.** Delete the sentence.
- `.claude/skills/redirects/SKILL.md:17-18` uses `/collections/tattoo-numbing-cream` as a worked from-path. That is a **live Totally Numb URL**. A session actioning it literally would pre-empt the build.
- `BRAND.md:27` says `--text-muted #8E8A82`; the live token is **`#6E6A63`**. The brand asterisk strokes **`#984AE8`**, not `#6B3FA0`, despite `BRAND.md:104`.
- The 34-anchor backlink list lives only in auto-memory, not in the repo, and its named source (`scratchpad/census.json`, `scratchpad/build_report.py`) **no longer exists** — the list cannot currently be regenerated or audited. Its "excluded, do not re-add" section lists the entire tattoo cluster on a premise Daniel has now reversed.

---

**Read-only throughout. No edits, commits, deploys, Shopify writes or Notion writes were made in producing this plan.**
