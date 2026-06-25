# Senseless — Compliance Source Sweep (READ-ONLY)
**Date:** 2026-06-24 · **Auditor:** CC · **Mode:** read-only (no edits/commits/pushes; no Notion; no replacement copy)

## Step 1 — Store verification (HARD GATE) — PASS
- `shopify theme list --store senseless-numbing.myshopify.com` → **live theme = `#199324434780` ("Senseless Dev")** ✓ matches expected.
- Admin token (`.env SHOPIFY_ACCESS_TOKEN`) `{ shop { myshopifyDomain } }` → **`senseless-numbing.myshopify.com` (name "Senseless")** ✓. No Totally Numb / matrix-group leakage.

## Step 2 — Source
- Pulled the live published theme to `./_audit_live` (throwaway): 68 templates / 85 sections / 117 snippets. **All theme findings below cite `_audit_live/…` (= the live published source).** Judge.me review text (Step 4) fetched from Judge.me's public `reviews_for_widget` feed (token-free) since it is JS-injected and not in the theme.

## Product → template map (16 products)
- 9 strength SKUs → `templates/product.<handle>.json` (clinical/advanced/professional × cream/gel/spray)
- `foaming-cleanser` → `templates/product.foaming-cleanser.json` (aftercare)
- `vitamin-a-d-ointment-4-pack` → **default `templates/product.json`** (no dedicated template) (aftercare)
- 5 bundles (clinical/advanced kits small/large + professional kit large) → shared `templates/product.bundle.json`

---

# BUCKET A — Clear breach (must fix)

### A1 — Live Judge.me review text: medicinal / efficacy / %-strength claims (131 hits)
The on-page review widget displays customer text that makes pain-relief, total-numbness, and percentage claims — a live compliance surface on the PDP. Counts (full pagination):
- **clinical-strength-cream** — 13 reviews, **5 hits**
- **advanced-strength-cream** — 11 reviews, **6 hits**
- **professional-strength-cream** — 207 reviews, **120 hits**
- (gels, sprays, cleanser, all 5 bundles, vitamin A&D — **0 reviews**, clean)

Representative hits (reviewer — text):
- `pain-free/painless`: "…my procedure was **pain free**…completely numb…" — Rebecca Parsons (clinical-cream); "**Pain free**. Was great worked for about 4 hours" — Raymond Pring (advanced-cream); "**painless**" — Cameron A (professional-cream).
- `completely/total numbness`: "it was **completely numb** for ar…" — Rebecca Parsons; "**Completely Numb** …didn't feel a thing" — Matthew Murray (professional-cream).
- `no pain / felt nothing`: "**Didn't feel a thing** for hours" — Katie Dedman; "with **no pain**" — Gordon Millar; "felt absolutely **no pain** at all" — helen jones.
- `percentage / %-strength`: "**80 %** cream is amazing" — helen jones; "Senseless numbing cream **80**" — Sam; "**100%** recommend" — Karen (professional-cream).
- `duration/onset`: "**Lasted 1**.5hours" — Taya Odonohue; "still numb **6 hours** after application" — Liz Fisher.

Note: legal "cleared the 46 reviews" — but the **current live corpus is ~231 review texts** (13+11+207), the bulk on professional-strength-cream, and many post-date a 46-item set. The cleared scope likely does **not** cover the full current corpus (see B-note B5). Full per-review list available on request; capped at 40 examples/product in the scan.

### A2 — Required safety warnings absent across all product pages
Per the brief's required-warnings set, checked in each product's template/source. **Only "patch test" appears anywhere; the other five lines are absent from every product.**

| Warning line | Where found |
|---|---|
| for external use only | **ABSENT — all 16** |
| keep out of reach of children | **ABSENT — all 16** |
| avoid contact with eyes | **ABSENT — all 16** |
| discontinue if irritation occurs | **ABSENT — all 16** |
| patch test ≥24h before first use | PRESENT on the **9 strength SKUs** (FAQ answer in each `product.<tier>-strength-<format>.json`); **ABSENT** on `product.bundle.json` (5 bundles), `product.foaming-cleanser.json`, `product.json` (vitamin A&D) |
| do not apply to broken, inflamed or sunburnt skin | **ABSENT — all 16** (see carve-out note below) |

Per-product warning score: **9 strength SKUs = 1/6** (patch test only); **5 bundles + cleanser + vitamin = 0/6**.
*Context for owner:* cosmetic warnings are legally required on the **pack/label**; whether the **website** must reproduce them is a judgement (the brief defines them as "required per product page", hence A). The "do not apply to broken skin" carve-out: the **spray** intentionally omits the broken-skin caution (confirmed: 0 broken-skin references in `collection.numbing-spray.json`) — see A-note vs B3.

---

# BUCKET B — Judgement call (owner / MHG)

### B1 — Spray framed as a *different class* (apply-DURING-session) vs cream/gel (apply-before, clean skin)  *(priority c + b)*
`templates/collection.numbing-spray.json`:
- L69–70: `"eyebrow": "During your session"` / `"body": "Easy to re-apply during your appointment — many customers tell us they top up with the spray through longer sessions to stay comfortable."`
- L192 (uses link): `"note": "Many customers report topping the spray up mid-session to help keep an area comfortable — check with your practitioner first."`
- L303: `"…the spray suits larger or broader areas and is easy to re-apply — many customers tell us they top up with it during longer sessions."`
- L327–331: FAQ `"question": "Can I re-apply numbing spray during my session?"` / `"answer": "Many customers report re-applying the spray during a longer session… easy to top up mid-appointment without disturbing the area. Always check with your practitioner first, as not every procedure allows re-application mid-session."`

By contrast cream/gel are framed apply-before on clean/unbroken skin (e.g. `page.how-to-apply-numbing-cream.json` L88 "A thin, even layer on clean, healthy, unbroken skin"; `collection.numbing-cream.json` L310 / `collection.numbing-gel.json` L315 patch-test "Take extra care on sensitive or broken skin"). The spray's patch-test FAQ omits the broken-skin caution line. **Mid-session / top-up-during-treatment implies application onto skin already worked on (potentially broken)** — owner/MHG call on whether the during-session positioning is acceptable.

### B2 — "during the procedure / reapply at the chair / during the session" framing on guide pages  *(priority b)*
- `templates/page.how-long-numbing-cream-lasts.json` L62: "Some reapply at the chair. **Some use additional numbing during the procedure.** Some pause briefly."; L51 (SPMU) "…with reapplication sometimes used during the session"; L100 "Some reapply, some use additional preparation at the chair."
- `templates/page.how-to-apply-numbing-cream.json` L48 (SPMU) "Some artists reapply during the session."; L27 "They may also do this themselves at the chair."
- `templates/page.does-numbing-cream-work.json` L75 (SPMU) "Many also reapply during the session."
- `templates/page.how-long-numbing-cream-takes-to-work.json` L62 (SPMU) "Many artists also reapply during the session."
- `sections/senseless-comfort-compare.liquid` L22: "Numbing is commonly used to help you feel more comfortable **during treatment**. It is a cosmetic preparation, not an anaesthetic." (during-treatment framing; paired with compliant disavowal)

All are practitioner-attributed/observational, not a direct product instruction — judgement call on whether they imply mid-procedure (broken-skin) use.

### B3 — "most concentrated" retired framing in the strongest-page H1
- `templates/page.strongest-numbing-cream.json` L16: `"headline": "Senseless Professional. Our most concentrated formula."` → renders as the page **H1** on `/pages/strongest-numbing-cream`.
- "most concentrated" is a **retired framing** (banned per the comfort reposition). It sits in an H1; the brief's SEO carve-out covers "strongest"/"numbing" in title/H1, **not** "most concentrated". (Same page L30 H2 "Looking for the strongest numbing cream?" = allowed keyword.) This was a previously-parked owner/MHG decision — flagging it remains live.

### B4 — Origin wording: "produced in" vs "formulated in"
- `templates/page.about.json` L239: `"value": "Formulated and produced in the United Kingdom."` → "**produced in** the United Kingdom" reads as a manufacture/origin claim; rule requires "formulated in the UK". (42 other "formulated in" instances are compliant.) Owner/MHG call on "produced in".

### B5 — Review corpus vs cleared scope (process flag)
Legal cleared "the 46 reviews"; the live corpus is now ~231 review texts (professional-cream alone = 207, growing — `metafield_updated_at` 2026-06-23). New reviews carry the same A1 phrasing and may fall outside the cleared 46. Owner/MHG should confirm whether clearance covers the **current** corpus and ongoing new reviews.

---

# Reported but NOT a breach (compliant / allowed — for completeness)

- **Broken-skin DISAVOWALS (compliant):** `page.faq.json` L81–82 "Can I use it on broken or irritated skin?" → "No — apply only to clean, healthy, unbroken skin"; L61 "Used as directed on healthy, unbroken skin…"; `page.how-to-apply-numbing-cream.json` L88 "clean, healthy, unbroken skin"; `collection.numbing-cream-for-waxing.json` L271 "never on broken or irritated skin"; cream/gel/microneedling patch-test lines "Take extra care on sensitive or broken skin." These correctly steer AWAY from broken-skin use.
- **"not an anaesthetic" disavowals (compliant):** `page.does-numbing-cream-work.json` L27 "They're not anaesthetics. They're not medicines."; `sections/senseless-comfort-compare.liquid` L22. No "anaesthetic" used as a product descriptor.
- **No hard-rule CLAIM phrases in theme body copy:** no "numbs the skin", "pain relief", "pain-free", "painless", "blocks sensation", "works in X minutes", "lasts X hours", "as strong as Emla", or percentage claims in theme copy. (All `%` hits were CSS/gradient values, e.g. `theme-styles-variables.liquid`, `header-actions.liquid`.)
- **No named active / lidocaine / eugenol** in numbing-product or general theme copy. `page.how-it-works.json` L75 explicitly says it "doesn't lead with the active ingredient"; INCI references (`collection.numbing-cream/gel/spray.json` "full ingredients (INCI) listed on the pack") point to the pack. **No ingredient lists for the cleanser or vitamin A&D appear in the theme** (they'd be in the admin product description / on-pack, not the pulled theme) — nothing to flag in source.
- **`flagship` settings = `false`** everywhere (inert; the de-flagship is in place) — not a breach.
- **"strongest" as allowed SEO:** `rel_strongest` link label "Strongest numbing cream" → `/pages/strongest-numbing-cream` (`collection.numbing-cream.json` L189–193, `collection.numbing-spray.json` L196–200) is a nav/anchor to the keyword page; `page.strongest-numbing-cream.json` L30 H2 is the keyword question. The collection editorial bodies use "strongest" only to argue *against* maxing ("not by whatever's labelled 'strongest'") — `collection.numbing-cream/gel/spray.json` ~L218/216/225.

---

## Scope / caveats
- Read-only: nothing edited, committed, or pushed; no Notion; no replacement copy drafted.
- Theme findings are from the **pulled live theme** (`_audit_live`), not the repo working copy. `./_audit_live` is a throwaway pull dir.
- Review-text scan paginated fully (Judge.me public feed); patterns are inclusive — each item lists the matched phrase + reviewer + context for human judgement.
- The literal regulatory call on each item (A vs B borderline, esp. A2 web-vs-pack and B1/B2 during-session) is for the owner/MHG.
