# Next session — Senseless (Canon v2.20)

Read `CLAUDE.md` → run `scripts/reconcile.sh` → read the Project Instance + State Surface first.
**Machine last used:** MacBook Pro — 12 Aug (`Daniels-MacBook-Pro.local`). Clock is **UTC+3 (EEST)**.

Session ended abruptly (battery). **Research only — nothing was edited, deployed, or written back to
Notion.** No theme file changed, so there is nothing to deploy.

---

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
3. **MHRA Guidance Note 8 is UNSOURCED.** Exists only in the `f940b05` commit body; zero other
   occurrences across 200 revisions. Do not quote it as authority. (Nothing is lost — the Hard Rules
   already ban that presentation.)
4. **"tattoo pain chart" = 6,900/mo GB at KD 1** (global 60,000) and the SERP is soft — a DR 3 site
   ranks #8, a 1-refdomain page ranks #10. Senseless is DR 7. Best beachhead on the site.
5. **Tattoo aftercare = 9,700/mo at KD 2**, products already in range (A&D ointment + Foaming
   Cleanser), far less MHRA exposure, no page exists. Possibly the best risk-adjusted first move.

## Corrections on record

- **"tattoo numbing cream" is 10,000/mo GB, not 14,800.** The `f940b05` figure was Keyword Planner,
  not Ahrefs. 24-month GB range 8,540–11,764. Global 51,000.
- **"tattoo numbing cream" and "numbing cream for tattoos" share one SERP** (identical AI Overview,
  same top results). Ahrefs' different parent topics are a modelling artefact. **One collection.**
- The compliance ceiling costs ~650/mo directly (~2.5%), but the real cost is **CTR and dwell**:
  competitors state onset/duration in hours and we cannot, in any voice, even where we rank.

## THREE WORKFLOWS DIED UNFINISHED — re-run them

Background research was still running when the session ended. Resume is same-session-only, so these
must be **re-run**, not resumed. Scripts are saved on disk and can be re-invoked directly with
`Workflow({scriptPath: ...})`:

```
~/.claude/projects/-Users-matrix-code-senseless-theme/3d587116-c801-4b77-b745-5f8663c99bcb/workflows/scripts/
  tattoo-competitive-deep-research-wf_3b8f34ea-3b5.js       (competitor teardowns + gaps)
  senseless-challenger-traction-playbook-wf_0db71e3c-7be.js (what's winnable in 90 days)
  tattoo-pain-chart-and-guides-spec-wf_9a050867-6c3.js      (pain chart build spec)
```

Strand 1 (blast radius) COMPLETED and is fully captured in the doc — do not re-run it.

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
