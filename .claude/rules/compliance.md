# Rule — UK compliance (Senseless · [Regulated])

Senseless is a UK **cosmetic** topical preparation (Matrix Health Group Ltd) — **not a medicine**. Compliance is non-negotiable and load-bearing. Canonical detail: repo `docs/COMPLIANCE.md` + the **Compliance Holds** DB (Notion ds `6b005ef4-548a-470d-8c7e-34fdf4b95db7`). Run the `compliance-check` skill before shipping any user-facing copy.

## Hard Rules (banned in every voice, incl. testimonials/reviews)
- **No medicinal / anaesthetic claims:** never "numbs", "pain relief", "anaesthetic", "blocks/stops pain", "blocks/reduces sensation".
- **No time-to-effect or duration as a brand claim:** no "works in X minutes" / "lasts X hours" (16 Jun decision — banned in every voice).
- **"Numbing" is a category/SEO noun only** — never an effect claim. Allowed in slugs, titles, meta, collection/guide bodies as the product-type word; never "it numbs".
- **No before/after or efficacy framing** implying a medicinal effect.
- Subjective experience → **customer-attributed** framing only ("many customers tell us…"), genuine + substantiable; attribution never licenses an effect or safety claim.
- Intended-use / safety claims (e.g. suitability on broken skin) must sit inside the **CPSR claim envelope** — separate axis from medicinal claims.

## Authority & holds
- MHRA (medicines classification) / ASA (advertising) / CPSR (Cosmetic Product Safety Report) govern. Founder governs content-language calls; MHG/legal governs genuinely legal/borderline items.
- Honour the **Compliance Holds** state machine — held copy stays held until cleared by the named owner; never ship a held item.
- **Documented exception (FAQ only):** the main-site FAQ (`templates/page.faq.json`) ships legal-team-verbatim copy that contains onset/duration phrasings; the legal sign-off supersedes the Hard Rules **for that page only**. Do NOT propagate that wording to any other surface.

## Launch-gates — ALL CLEARED 2 Jul 2026 (launch gate CLEAR)
MHRA medicines classification (closed — cosmetic, Decision 39158bc3-75ea-8194) · CPSRs all SKUs (done, Confirmed Fact) · core safety warnings on PDPs (built + live, `senseless-safety-warnings`) · reviews banned-phrase scrub (legal: leave published reviews as-is, Decision logged). Ongoing duty: Hard Rules stay enforced on all brand-authored surfaces. Current state lives in the State Surface — always re-verify there.
