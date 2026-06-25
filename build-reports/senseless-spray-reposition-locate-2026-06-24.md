# Senseless — Spray Reposition: Locate Pass (READ-ONLY)
**Date:** 2026-06-24 · **Mode:** locate-only (only write = this file; no edits/commits/push/Notion/copy/dev-theme)
**Source:** live published theme `#199324434780` pulled to `./_audit_live` (554 files). All citations are from that pull.
**Gate:** [live] = `199324434780` ✅ · Admin token store = senseless-numbing.myshopify.com ✅
**Orienting decision (not acted on):** the spray becomes a BEFORE-AND-DURING, intact-skin SUPPORT format — same class as cream/gel (applied to clean, intact skin), cream still leads; no longer an "apply-onto-the-work / during-the-procedure adjunct."

---

## GROUP A — During-session / worked-skin / reapply strings (the copy to rewrite)
Tags: **[SPRAY]** spray-specific · **[GEN]** numbing generally · **[REPORTAGE]** practitioner-reportage · **[OCCASION]** "top-up" = appointment-type, likely out of scope (judge).

### [SPRAY] — `templates/collection.numbing-spray.json` → /collections/numbing-spray
- **L69** — eyebrow: « During your session »
- **L70** — « Easy to re-apply during your appointment — many customers tell us they top up with the spray through longer sessions to stay comfortable. »
- **L192** — note: « Many customers report topping the spray up mid-session to help keep an area comfortable — check with your practitioner first. »
- **L303** — FAQ answer: « Pick the format for the area: the spray suits larger or broader areas and is easy to re-apply — many customers tell us they top up with it during longer sessions. »
- **L327 / L330 / L331 / L363** — the dedicated re-apply FAQ block `qreapply`:
  - L330 question: « Can I re-apply numbing spray during my session? »
  - L331 answer: « Many customers report re-applying the spray during a longer session to help extend comfort where their practitioner is happy for them to — its quick, hands-off application makes it easy to top up mid-appointment without disturbing the area. »
  - L331 (cont.): « Always check with your practitioner first, as not every procedure allows re-application mid-session. »
  - L327 `"qreapply": {` (block def) · L363 `"qreapply"` (block_order ref)

### [SPRAY] — spray PDP patch-test divergence (during-class residue in the warning line)
All three spray PDPs end the patch-test line with "proceed or remove as your practitioner directs" — cream/gel say "remove before your appointment" (see Group C):
- `templates/product.clinical-strength-spray.json:110` — « Patch test 24 hours ahead first, then proceed or remove as your practitioner directs. »
- `templates/product.advanced-strength-spray.json:110` — « Patch test 24 hours ahead first, then proceed or remove as your practitioner directs. »
- `templates/product.professional-strength-spray.json:112` — « Patch test 24 hours ahead first, then proceed or remove as your practitioner directs. »

### [GEN] / [REPORTAGE] — numbing-general "during the procedure / reapply at the chair" (guides + shared section)
- `sections/senseless-comfort-compare.liquid:22` [GEN] — « Numbing is commonly used to help you feel more comfortable during treatment. » (hardcoded; renders on does-laser / does-microneedling)
- `templates/page.does-microneedling-hurt.json:30` [GEN] — « Numbing is commonly used to help you feel more comfortable during the session. »
- `templates/page.does-microneedling-hurt.json:59` [GEN] — « Where you're preparing at home, or topping up comfort with your practitioner's agreement, a topical numbing gel is the usual choice for facial work because it stays where it's placed. »
- `templates/page.does-numbing-cream-work.json:27` [GEN] — « They support comfort during the appointment — that's their purpose, and it's the language regulators recognise. »
- `templates/page.does-numbing-cream-work.json:63` [GEN] — « Clients who go in expecting comfort during the appointment tend to be more satisfied than clients who expect complete absence of sensation. »
- `templates/page.does-numbing-cream-work.json:75` [REPORTAGE] — « Many practitioners also apply additional numbing at the chair. » / « Many also reapply during the session. »
- `templates/page.does-numbing-cream-work.json:97` [GEN] — FAQ question: « Will I feel anything during the procedure? »
- `templates/page.how-long-numbing-cream-lasts.json:51` [REPORTAGE] — « Advanced or Professional, with reapplication sometimes used during the session. »
- `templates/page.how-long-numbing-cream-lasts.json:62` [REPORTAGE] — « Some reapply at the chair. » / « Some use additional numbing during the procedure. »
- `templates/page.how-long-numbing-cream-lasts.json:100` [REPORTAGE] — « Some reapply, some use additional preparation at the chair. »
- `templates/page.how-long-numbing-cream-takes-to-work.json:62` [REPORTAGE] — « …many practitioners use additional numbing at the chair. » / « Many artists also reapply during the session. »
- `templates/page.how-to-apply-numbing-cream.json:27` [REPORTAGE] — « They may also do this themselves at the chair. »
- `templates/page.how-to-apply-numbing-cream.json:48` [REPORTAGE] — « Some artists reapply during the session. »
- `templates/page.how-to-apply-numbing-cream.json:66` [REPORTAGE] — « Most practitioners will tell you how long to leave the product on, whether to bring your own or use theirs, and what they prefer to do at the chair themselves. »
- `templates/page.how-to-apply-numbing-cream.json:76` [GEN] — « If you're early, ask your practitioner whether to reapply or wait. »
- `templates/page.how-it-works.json:168` [GEN] — « Specific duration varies — your practitioner is the best guide for what to expect during your session. »

### [OCCASION] — "top-up" as an appointment TYPE (not during-session reapply — likely out of scope; judge)
- `templates/collection.aesthetic-numbing-cream.json:104`, `templates/collection.clinical.json:34`, `templates/page.choosing-your-strength.json:30` & `:123`, `templates/page.best-emla-alternative-uk.json:58`, `templates/page.senseless-vs-ametop.json:69`, `templates/product.json:214` — all use "top-ups / quick top-up" to mean *small routine appointments*, e.g. « Used for top-ups, routine microneedling, smaller laser zones… »
- `templates/collection.professional.json:36`, `templates/page.choosing-your-strength.json:54` — « Trusted at the chair. » (tagline, not reapply)

---

## GROUP B — Spray-as-different-class framing (the positioning to dissolve)
### `templates/collection.numbing-spray.json` → /collections/numbing-spray
- **L215** intro: « Spray suits large or awkward-to-reach areas you can cover quickly and evenly, without working a layer in by hand. »
- **L225** « Spray exists because some areas are too large or awkward to cover well any other way. »
- **L289** « Cream suits broad coverage on simpler areas; gel suits precise facial work; spray suits reach and larger zones. »
- **L303** « …the spray suits larger or broader areas and is easy to re-apply — many customers tell us they top up with it during longer sessions. » (also Group A)
- **L331** « …its quick, hands-off application makes it easy to top up mid-appointment without disturbing the area. » (also Group A)
- **L338** « Spray suits larger or broader areas — body laser, waxing and similar zones — where its even, hands-off coverage is easier to apply than a cream. »
- **L113** « None is "better" than another; each is formulated for a different kind of session. »
### spray PDPs
- `templates/product.clinical-strength-spray.json:16` subtitle — « For the body and broader areas. »
- `templates/product.clinical-strength-spray.json:209` keyfacts — « Clinical is the standard-strength Comfort Spray — even, hands-off coverage for larger or awkward areas. »
### `templates/page.choosing-your-format.json:17`
- « Gel and Spray each work on their own too — and because different appointments call for different formats, plenty of clients keep more than one. »

*(Note: the "larger/broader areas · hands-off coverage" framing is area-based, not stage-based — it may survive the reposition; the stage-based "apply-during / re-apply / mid-session" framing is the part being dissolved. Flagged for the planning layer to split.)*

---

## GROUP C — Cream/gel intact-skin reference language (to mirror onto the spray)
### "clean, healthy, unbroken skin" / before-application
- `templates/page.how-to-apply-numbing-cream.json:88` — « A thin, even layer on clean, healthy, unbroken skin. » (also L25 « Apply a thin, even layer. »)
- `templates/page.faq.json:61` — « Used as directed on healthy, unbroken skin, topical numbing cream is widely used for cosmetic treatments; always follow the product's instructions, patch test first, and check with your practitioner if you have sensitive skin or a skin condition. »
- `templates/page.faq.json:82` — « No — apply only to clean, healthy, unbroken skin, and follow the product's instructions. » (answer to L81 « Can I use it on broken or irritated skin? »)
- `templates/page.faq.json:130` — « Apply only to clean, healthy skin, patch test, and follow the product's instructions. »
- `templates/page.using-numbing-cream.json:48` — « Begin on clean, dry skin before you apply anything. »
- `templates/page.does-it-hurt.json:137` — « Apply to clean skin, patch test about 24 hours beforehand, and follow the product instructions and your practitioner's advice. »
- `templates/collection.numbing-cream-for-injections.json:48` — « Numbing is preparation for comfort, not part of the procedure itself, and it's applied to clean, healthy skin before your appointment. »
- collection FAQ "on clean, healthy skin … patch test first": `collection.numbing-cream-for-botox.json:64`, `collection.numbing-cream-for-injections.json:64`, `collection.numbing-cream-for-lip-fillers.json:64`

### Patch-test lines (verbatim)
- **Cream/gel PDPs** (the mirror target wording): `product.clinical-strength-cream.json:110`, `product.advanced-strength-cream.json:110`, `product.professional-strength-cream.json:112`, `product.clinical-strength-gel.json:110`, `product.advanced-strength-gel.json:110`, `product.professional-strength-gel.json:112` — all: « Patch test 24 hours ahead first, and remove before your appointment. »
- **Collection patch-test FAQ** (cream/gel/spray all identical): `collection.numbing-cream.json:310`, `collection.numbing-gel.json:315`, `collection.numbing-spray.json:324`, + procedure collections `…-laser-treatment.json:271`, `…-microneedling.json:264`, `…-semi-permanent-makeup.json:271`, `…-waxing.json:271` — « Yes — patch test 24 hours before on the inside of your wrist or behind your ear, and don't use it if you see any reaction. »
- `templates/page.using-numbing-cream.json:38` — « A patch test comes first — about 24 hours before your first use, apply a small amount to your inner wrist or behind the ear and check for any reaction. » (+ L160 « Patch test about 24 hours before first use and stop if your skin reacts. »)
- `templates/page.does-it-hurt.json:126` — « Patch test about 24 hours before first use and follow your practitioner's guidance. »

### Broken-skin warning lines (verbatim)
- `templates/page.faq.json:81-82` — « Can I use it on broken or irritated skin? » → « No — apply only to clean, healthy, unbroken skin… »
- `templates/collection.numbing-cream-for-waxing.json:271` — « Take extra care on sensitive areas like the bikini line, and never on broken or irritated skin. »

*(Cross-class note for the rewrite: cream/gel PDP patch-test = "…remove before your appointment"; spray PDP patch-test = "…then proceed or remove as your practitioner directs" — see Group A. To mirror the spray onto the cream/gel class, the spray's "proceed" residue would align to the cream/gel "remove before your appointment" form. No change made here.)*

---
**Read-only complete.** Nothing edited/committed/pushed; no dev theme; no copy composed; no Notion write. `./_audit_live` is the throwaway pull (safe to delete).
