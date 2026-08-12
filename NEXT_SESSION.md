# Next session — Senseless (Canon v2.20)

Read `CLAUDE.md` → run `scripts/reconcile.sh` → read the Project Instance + State Surface first.
**Machine last used:** MacBook Pro — 12 Aug (`Daniels-MacBook-Pro.local`). Clock is **UTC+3 (EEST)**.

Session ended abruptly (battery). **Research only — nothing was edited, deployed, or written back to
Notion.** No theme file changed, so there is nothing to deploy.

---

## ⚠️ TWO THINGS THAT OUTRANK THE TATTOO WORK — raise with Daniel first

**1. A bought-link package is pointed at senseless.uk and it is live.** DR went 14 (13 Jul) → **27**
(20 Jul) → 21 → 10 → **7** (10 Aug). Referring domains jumped **+95 in the week to 13 Jul**.
**158 of 160 live referring domains are Ahrefs-flagged spam**; the only two non-spam are
`creativeposts.top` (0 dofollow) and the group's own `matrixhealthgroup.co.uk`. **Earned editorial
refdomains: zero.** Placements are still arriving — `backlinkshop.site` first seen **30 Jul 2026**,
`backlinksplace.site` **3 Aug 2026**, plus `norskcasinos.net` (dofollow), `seoflox.io`,
`trafficspike.shop`. Nothing in the repo records anyone commissioning this. **Ask who is paying for
it, stop it, consider a disavow.**

**2. The review corpus is Totally Numb's, republished with "tattoo" edited to "procedure".**
Verified via the Judge.me widget JSON endpoint (not the curl false-reading trap). Same 10 reviewer
names and same 10 dates across TN `comfort-cream-bronze` and SL `clinical-strength-cream`; four texts
identical, six edited (*"a four hour back **tattoo**"* → *"a four hour back **procedure**"*).
Of 227 reviews: **184 dated 2023**, only **3 after the 7 June 2026 launch**, and **3 of 227 are
`verified_buyer`**. 88.5% sit on one SKU; 11 of 16 products have zero. **31 of 150 sampled still
contain tattoo vocabulary the edit missed** (*back piece, half sleeve, rib, full leg, ink*, *"Amazing
7 hour procedure"*).
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

## What exists — read this first

**`docs/TATTOO-REPOSITIONING-2026-08-12.md`** — the full research record. Everything below is a
pointer into it. Do not redo this work.

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
| 2 — Competitor deep research (16 agents) | **SALVAGED** — research complete, verifier + synthesis never ran | Part 4 |
| 3 — Challenger playbook (7 agents) | **SALVAGED** — both research phases complete, verifier + synthesis never ran | Part 4 |

All four strands are captured. **Do not re-run any of them.**

**Caveat on Part 4:** strands 2 and 3 died before their adversarial verifiers ran, so everything in
Part 4 is single-sourced agent output. Parts 2 and 3 were verified (the Part 3 pass caught seven
errors). Re-verify any Part 4 number before acting on it.

**Before re-running: Ahrefs was at ~105k of 400k monthly units** (resets 2026-09-09) and these
workflows query it heavily. Check `subscription-info-limits-and-usage` first.

## Next Work Item

**Session 1 is the gate pack — no code, no copy, no deploy.** Get written answers on: (a) the CPSR's
declared scope, and whether it traces to Totally Numb's certifications; (b) whether the unbroken-skin
warning can change; (c) the Senseless-vs-Totally-Numb lane decision; (d) ad-facing or organic-only.
Same session: raise a **Compliance Hold** on the tattoo keyword set (precedent: the Applied EMLA hold,
row `3b158bc3-75ea-8183-ae67-c6d305610682`) and log a Decisions row capturing both the historical
aesthetics-only position and its reversal — **there is no predecessor row to supersede**.

Full 12-session sequence is in the doc.

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
