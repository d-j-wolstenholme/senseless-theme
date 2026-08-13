# Next session — Senseless (Canon v2.20)

Read `CLAUDE.md` → run `scripts/reconcile.sh` → read the Project Instance + State Surface first.
**Machine last used:** MacBook Pro — 12–13 Aug (`Daniels-MacBook-Pro.local`). Clock is **UTC+3
(EEST)** — consoles render timestamps in EEST, not UK time.

**Research only — no theme file was changed, nothing was deployed, and nothing was written back to
Notion.** Four research strands ran to completion; all findings are recorded in `docs/`.

**Handle question is closed:** measured, and slug construction has no measurable effect in this SERP
(the exact-match URL is the worst performer in the set by 65×). See "The slug question is settled" in
the build sweep. Do not re-open it and do not spend Ahrefs units re-testing it.

---

<!-- ON-CONTINUE:START -->
## ▶ IF THE USER SAYS ONLY "CONTINUE" — do this, don't ask

Run **Phase A** of `docs/TATTOO-BUILD-SWEEP.md`, end to end, in this one session.

- **The one-task-per-session rule in `CLAUDE.md` is deliberately overridden for this work** by owner
  instruction (2026-08-12: *"so the next session can build all in a single sweep"*). Do not build one
  item and stop.
- **Phase A needs no answer from anyone.** Ten items, all shippable today. Start with the aftercare
  cluster (9,700/mo, KD 2, products already in range, no page exists) and `/pages/delivery` (all four
  candidate URLs 404 while a competitor holds #1 on the tattoo variant with zero backlinks).
- **Phase 0 pre-flight first.** The verify-store gate is never optional — the CLI default account is
  Totally Numb.
- **Do NOT re-run the tattoo research.** Four strands are complete (~7.9M subagent tokens). Ahrefs
  was at ~105k/400k units; resets 2026-09-09.
- **Finish with Phase Z**: `theme-check` 0 → commit → push → deploy **under bash** → Asset-API
  per-file diff → 14-surface injectable-clean re-sweep → Notion write-back → rewrite this file.

Phase B is written but held on G1/G2/G6. Phase C is blocked. Both are marked in the sweep.
<!-- ON-CONTINUE:END -->

---

## ⚠️ TWO THINGS THAT OUTRANK THE TATTOO WORK — raise with Daniel first

**1. A bought-link package is pointed at senseless.uk and it is live.** DR went 14 (13 Jul) → **27**
(20 Jul) → 21 → 10 → **7** (10 Aug). Referring domains jumped **+95 in the week to 13 Jul**.
**158 of 160 live referring domains are Ahrefs-flagged spam**; the only two non-spam are
`creativeposts.top` (0 dofollow) and the group's own `matrixhealthgroup.co.uk`. **Earned editorial
refdomains: zero.** Placements are still arriving — `backlinkshop.site` first seen **30 Jul 2026**,
`backlinksplace.site` **3 Aug 2026**, plus `norskcasinos.net` (dofollow), `seoflox.io`,
`trafficspike.shop` — and a third non-spam-count entrant, **`backlinkengine.shop`, first seen
`2026-08-12T18:09:50Z`, i.e. DURING the session that found this.** Nothing in the repo records
anyone commissioning it. **Ask who is paying for it, stop it, consider a disavow.**

**2. Senseless and Totally Numb share a review corpus.** **CONFIRMED at aggregate level** by an
adversarial verifier, from server-rendered JSON-LD on both stores: TN `comfort-cream-bronze`
**4.85 / 13** is identical to SL `clinical-strength-cream` **4.85 / 13**; TN `comfort-cream-platinum`
**4.88 / 216** against SL `professional-strength-cream` **4.88 / 207**. Also confirmed: 234 reviews
across 16 PDPs, **88.5% on one SKU**, **11 of 16 PDPs emit no `aggregateRating`**.
**NOT CONFIRMED — do not repeat as fact:** the claim that review *texts* were edited from "tattoo" to
"procedure", the 227-review dedup, the date distribution (184 in 2023) and the "3 of 227 verified
buyers" figure. The verifier could reproduce **none** of it — the Judge.me widget endpoint 404s for
both shops and `api.judge.me` 401s. **Re-extract from the Judge.me admin before this goes near
legal.**
Mitigation to check: `DECISIONS-LOG.md:119` says Senseless CPSR coverage was assumed from *"the same
certifications as Totally Numb"* — if these are the same formulations, transplanted reviews are
arguable. The **editing** is separate, and DMCC Act 2024 fake-review provisions are in force.
**Owner + legal. Do not touch the reviews unilaterally.**

Both are in `docs/TATTOO-REPOSITIONING-2026-08-12.md` Part 4 with full evidence.

## THE BRAND CHANGE (this is the whole context)

Daniel, 12 Aug: **all Senseless products are now formulated for tattooing** as well as the original
aesthetic applications. He wants all site content, SEO and **GEO** to reflect it to customers and
bots; to beat `getnumbd.com` / `totally-numb.com` / "Tattoo Numbing Co"; **tattoo pain guides** and an
**interactive pain chart / body diagram** better than Totally Numb's; new **tattoo collections** for
SEO. Framing: *"senseless is new so it needs to outperform them to gain traction."*

**Daniel confirmed verbally: "the certs have been updated"** — CPSR intended use now covers
tattooing. That is the gate that permits tattoo-positive copy. It is verbal only; no written scope
exists anywhere in the repo or Notion.

## ▶ START HERE — `docs/TATTOO-BUILD-SWEEP.md`

**That is the build document.** Owner instruction, 12 Aug: *"make sure the docs are set up so the
next session can build all in a single sweep"* — which **deliberately overrides the one-task-per-
session rule** for this work (log it in the Decisions DB at write-back). It does not override the
store gate, the deploy rules, the reviews-guard, the injectable-clean invariant or `compliance-check`.

The sweep is structured **Phase 0 pre-flight → Phase A ungated build (10 items, shippable today) →
Phase B built-but-held-for-gates → Phase C blocked → Phase Z verify + write-back**, with a default
for every open gate so nothing stalls. Exact file paths and operations are in it.

Supporting evidence, in order of usefulness — **do not re-run the research, it cost ~7.9M tokens**:

| Doc | Use it for |
|---|---|
| `docs/TATTOO-REPOSITIONING-2026-08-12.md` | Evidence base, Parts 1–4 + all verifier corrections |
| `docs/TATTOO-BEAT-THEM-PLAN-2026-08-12.md` | Competitor detail, target map, GEO property lists |
| `docs/TATTOO-90-DAY-PLAYBOOK-2026-08-12.md` | Channel strategy, off-SERP, paid, artist B2B |

## The five findings that shape the plan

1. **Totally Numb already owns the tattoo lane.** `totally-numb.com` = 720 backlinks / 540 refdomains,
   ranks GB ("strongest tattoo numbing cream" pos 8), and
   **`totally-numb.com/collections/tattoo-numbing-cream` is LIVE**. Repo canon assigns tattoo to
   Totally Numb (`build-reports/phase-6-close-does-it-hurt-by-treatment.md:24`);
   `docs/AUDIT-2026-06-12.md:31,:114` logs it as an OPEN strategic call. Two MHG brands in one SERP
   and one ads account = ASA consistency exposure. **Owner decision, blocks everything downstream.**
2. **Unbroken-skin conflict.** `sections/senseless-safety-warnings.liquid:22` — *"Apply to clean,
   unbroken skin"*, hardcoded/non-editable, 9 SKUs + 5 kits, duplicated in Admin `body_html`.
   Tattooing breaks skin. Needs the safety assessor, not a copy edit.
3. **MHRA Guidance Note 8 IS REAL — binding primary authority.** An earlier finding in this session
   called it unsourced; that was based on a repo-only search and **is superseded**. The PDF was
   fetched: `assets.publishing.service.gov.uk/media/6a035312e71c4cdf4026bac6/GN8_FINAL_20260512.pdf`,
   now 301ing to **`GN8_FINAL_20260806.pdf`** (6 Aug 2026). §13 verbatim: *"Topical anaesthetics
   which are administered to reduce sensibility to pain e.g. lidocaine, prilocaine, epinephrine prior
   to carrying out a procedure, including non-medicinal procedures, are regarded to be medicinal
   products. **Examples of non-medicinal procedures include tattoos**, and cosmetic procedures such
   as semi-permanent makeup."* Commit `f940b05` was right. **Cite by section/appendix, never by line
   number.**
   - **Two mitigating facts:** Senseless is **lidocaine-free, eugenol-based** (`DECISIONS-LOG.md:176`),
     so the *function* limb is weak against us — the entire exposure is the **presentation** limb.
     And GN8 §13 already names **semi-permanent makeup**, which we already sell a collection for, so
     tattoo creates **no new category** of exposure.
   - **CPSR ≠ claims permission.** Daniel's "the certs have been updated" clears intended use. It
     does not license pain claims: a CPSR presupposes the product is a cosmetic, and if presentation
     makes it medicinal, GN8 §13 applies regardless.
4. **"tattoo pain chart" = 6,900/mo GB at KD 1** (global 60,000) and the SERP is soft — a DR 3 site
   ranks #8, a 1-refdomain page ranks #10. Senseless is DR 7. Best beachhead on the site.
5. **Tattoo aftercare = 9,700/mo at KD 2**, products already in range (A&D ointment + Foaming
   Cleanser), far less MHRA exposure, no page exists. Possibly the best risk-adjusted first move.
6. **The pain-chart build thesis is REVERSED — the winning asset is a static image.** Healthline's
   **static PNG** has 263 referring domains and 2,915 GB traffic. **Totally Numb's interactive chart
   has 0 refdomains, 0 backlinks, 0 traffic, 0 keywords** (verified exactly). No interactive pain
   chart anywhere has earned a genuine link. Build the tool for users; build a **properly-made static
   graphic** for links and the image pack (position 1 for the head term is a 12-slot image pack).
   "tattoo pain chart **female**" at 900/mo means a **gender toggle is a ranking feature**.
7. **No published dataset of tattoo pain by body region exists.** The only large study — Witkoś 2020,
   n=1,092 — found **body area NOT a significant predictor** of pain intensity (p=0.094 during,
   p=0.742 after). Every chart online, Healthline's included, asserts a ranking the evidence does not
   support. **But** GN8 §4/App.10 make publishing clinical research a *listed* implied medicinal
   claim on a selling domain — so "cite the studies" cannot be the differentiator as first planned.

## Corrections on record

- **"tattoo numbing cream" is 10,000/mo GB, not 14,800.** The `f940b05` figure was Keyword Planner,
  not Ahrefs. 24-month GB range 8,540–11,764. Global 51,000.
- **"tattoo numbing cream" and "numbing cream for tattoos" share one SERP** (identical AI Overview,
  same top results). Ahrefs' different parent topics are a modelling artefact. **One collection.**
- The compliance ceiling costs ~650/mo directly (~2.5%), but the real cost is **CTR and dwell**:
  competitors state onset/duration in hours and we cannot, in any voice, even where we rank.

## Research strand status

| Strand | Status | Where it lives |
|---|---|---|
| 1 — Blast radius (8 agents) | **COMPLETE** | Part 2 of the doc. Do not re-run. |
| 4 — Pain chart & guides (9/10 agents) | **SALVAGED** — final synthesis agent stalled, all research + 3 audits finished | Part 3 of the doc. Do not re-run. |
| 2 — Competitor deep research (19/20 agents) | **COMPLETE** — both verifiers ran (34 + 70 checks) | Part 4 + `docs/TATTOO-BEAT-THEM-PLAN-2026-08-12.md` |
| 3 — Challenger playbook (7 agents) | **SALVAGED** — research done, verifier + synthesis never ran | Part 4 |

All four strands are captured. **Do not re-run any of them.**

**`docs/TATTOO-BEAT-THEM-PLAN-2026-08-12.md`** is strand 2's final synthesis: competitors ranked,
the compliance ceiling, and content/SEO/GEO plans with a build order. It is a PLAN — nothing built.

**Caveat:** strand 3 alone is single-sourced (no verifier ran). Strand 2's verifiers corrected eight
figures and flagged six aggregates as unsupported — all recorded at the end of Part 4. Notably:
**getnumbd's paid spend was overstated 3.4× (actual $1,063/mo)**, and the **263-term / 36,190-per-month
universe and the 4.6% unaddressable split are UNSUPPORTED — use ~650/mo (~2.5%) instead.**

**Before re-running: Ahrefs was at ~105k of 400k monthly units** (resets 2026-09-09) and these
workflows query it heavily. Check `subscription-info-limits-and-usage` first.

## Next Work Item

**Run the sweep: `docs/TATTOO-BUILD-SWEEP.md`, Phase 0 then Phase A.** Phase A needs no answer from
anyone — 10 items, all shippable today, including the aftercare cluster (9,700/mo at KD 2, products
already in range) and `/pages/delivery` (a competitor holds #1 on the tattoo variant with a page
carrying zero backlinks, while all four of our candidate URLs 404).

**In parallel, put four questions to their owners** — they gate Phase B, not Phase A:
G1 CPSR declared scope (safety assessor — one email may close it if the CPSRs trace to Totally
Numb's) · G2 can the unbroken-skin warning change (safety assessor) · G6 ad-facing or organic (owner,
and the sweep defaults to "yes" which cannot be wrong).

**G5 is ANSWERED — 2026-08-13, owner: *"senseless and totally numb both target the same customer base
now."*** Both brands deliberately compete for the same customers. "Beat Totally Numb" is literal.
Repo canon still says tattoo is TN's lane (`build-reports/phase-6-close-does-it-hurt-by-treatment.md:24`,
`docs/AUDIT-2026-06-12.md:31,:114`) — **correct both at write-back.** What this does NOT dissolve: the
two brands publish different claim sets under one company number and one VAT number, which is a
regulatory exposure for MHG legal, not a cannibalisation question.

**And escalate the two items at the top of this file first.** Neither blocks Phase A; both attach to
the domain that would host every tattoo page.

## Gotchas

- **Do not build a tattoo collection without its template first** — `templates/collection.json` is
  bare Horizon and a live URL would render a stock grid. Clone
  `collection.numbing-cream-for-microneedling.json` (injectable-clean). Never clone the Botox one.
- **Do not point a tattoo collection at `/pages/does-it-hurt-by-treatment`** — it links all three
  injectable collections. SPMU and waxing already do this. Injectable-clean baseline is currently
  **0 breaches across 14 surfaces**; any breach after this work is attributable to it.
- **7 of 16 products have no `senseless.recommended_procedures` metafield** — the cleanser, the A&D
  ointment and all 5 bundles. A metafield-driven tattoo collection silently excludes the highest-AOV
  items.
- **`.claude/skills/redirects/SKILL.md:17-18`** uses `/collections/tattoo-numbing-cream` as a worked
  example from-path. That is a **live Totally Numb URL**. Do not action it literally.
- **`templates/page.faq.json` is legal-signed** — excluded from any copy pass, goes back to legal.
- **Leave the review corpus alone.** It is already tattoo-native ("my whole 7 hour procedure", "a leg
  piece"). Legal ruled published reviews stay as-is.
- Cookie-banner / Clarity consent coupling from 8 Aug still applies — see git history for `f2483be`.

## Notion write-back — NOT DONE

Nothing was written back. The State Surface (`38e58bc3-75ea-81ad-87eb-e20fcfc22406`) and the
Decisions DB (`d5ce9514-257c-4e02-aced-acba800e89d9`) have no record of this brand change. Also
needs its own edit: Notion `35e58bc3-75ea-8148-b0c3-cf9d2fa53e3a` (21 May, *"aesthetics-only… NOT for
tattooing"*) sits in the **Matrix Health Group** tree and a Senseless write-back will not sweep it.
