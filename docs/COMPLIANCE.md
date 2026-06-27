# UK Compliance Rules

Senseless is a UK cosmetic product. Not a medicine. Not a medical device. All copy, alt text, schema descriptions, marketing assets, and product descriptions must comply with:

- UK Cosmetic Products Enforcement Regulations 2013
- Consumer Protection from Unfair Trading Regulations 2008
- CAP Code (non-broadcast) — ASA enforcement
- MHRA Borderline Products Guidance

Any claim implying a medicinal purpose (treating, preventing, curing, relieving symptoms) reclassifies the product as a medicine. We do not want that.

## Hard Rule — Never Use

- "Numbs the skin", "numbs the area", "numbs the pain"
- "Pain relief", "relieves pain", "pain-free", "painless"
- "Anaesthetic", "anaesthetises", "local anaesthetic"
- "Blocks nerve signals", "blocks sensation"
- "Treats", "prevents", "cures", "heals"
- "Medical-grade", "clinical-grade", "prescription-strength"
- "Works in X minutes" (specific efficacy timing)
- "Lasts X hours" (specific duration claim)
- "X% effective", "99% of users", percentage strength claims
- Before/after imagery implying medicinal outcome
- "As strong as Emla" (direct efficacy comparison to a lidocaine product)

## Documented exception — legal-approved FAQ copy (2026-06-27)

The main-site FAQ (`templates/page.faq.json`) was **authored by Peter + the MHG legal team** and is published with their wording **verbatim**, per Daniel's instruction (2026-06-27). That copy contains phrasings the Hard Rules above and the 16 June "time-to-effect banned in every voice" decision would otherwise restrict:

- **Onset** — "Most users begin noticing the effects after approximately 30–45 minutes, with optimal comfort typically achieved after around 45–60 minutes…" (*How long does it take to work?*)
- **Duration** — "customer feedback suggests comfort typically lasts between one and three hours…" (*How long does the effect last?*)
- **Performance/effectiveness** — "reduce the perceived effectiveness of topical numbing products" / "reduced performance" (*alcohol & caffeine; how much to apply*)

**Authority + scope:** the legal team's sign-off governs **this FAQ copy** and supersedes the "Works in X minutes" / "Lasts X hours" Hard Rules and the 16 June time-to-effect ban **for `page.faq.json` only**. The Hard Rules remain in force on **every other surface** (PDPs, collections, guides, ads, social, alt text, meta). **Do NOT propagate this onset/duration/effectiveness wording to other surfaces** without explicit legal sign-off for those surfaces.

> **Open (for Daniel / MHG):** decide whether this override extends sitewide or stays FAQ-scoped; and confirm the 4 substantiation flags (comfort-duration data; all-SKU unbranded packaging; direct-to-client clinic retail; injectables references are organic-only). **Resolved 2026-06-27:** FAQ contact email switched from Peter's `support@` to `cs@senseless.uk` (site standard); Royal Mail confirmed as carrier.

## Approved Language Patterns

| Don't write | Do write |
|---|---|
| Numbs the skin | Supports comfort during treatment |
| Pain relief | Helps clients feel more comfortable |
| Works in 20 minutes | Apply ahead of your appointment |
| Lasts 2 hours | Designed for typical session lengths |
| Anaesthetic cream | Topical preparation cream |
| Strongest numbing cream | Our most concentrated formula |
| Stops the pain | Supports the experience |
| Will numb you | May support comfort |
| Effective on lip fillers | Designed for use before lip fillers |

## Three-Tier Language

| Tier | Approved | Avoid |
|---|---|---|
| Clinical Strength | "For shorter or less intensive treatments" | "Mild numbing", "low strength" |
| Advanced Strength | "For everyday aesthetic procedures" | "Medium-strength numbing" |
| Professional Strength | "Our most concentrated formula" | "Strongest numbing", "max strength" |

## SEO vs Body Copy Rule

The word "numbing" appears only in:
- URL slugs (`/collections/numbing-cream-for-lip-fillers`)
- Page titles (`<title>Numbing Cream for Lip Fillers | Senseless</title>`)
- Meta tags
- Internal navigation labels

It does NOT appear in:
- Body copy
- Headlines (H1, H2)
- Product descriptions
- Marketing emails
- Social posts
- Alt text describing product effect

### Exception — "numbing" as a category descriptor

"Numbing cream / gel / spray" may be used as a **category / product-type noun** on the matching category (collection) pages and their **Key Facts** blocks — e.g. "Numbing cream in three strengths: Clinical, Advanced, Professional." There it names the product category (which is literally what the page is), not a claim about what the product does. This narrow exception does **not** loosen the Hard Rule: "numbing" / "numbs" used as an **effect or efficacy claim** ("numbs the skin", "a numbing effect", "how much it numbs") remains banned everywhere, including those same pages. Rule of thumb: the category noun is fine; the moment it describes an effect on skin or sensation, it's a violation.

### Exception scope (extended 2026-06-12)

The category-noun exception above is extended to two further surfaces, owner-approved 2026-06-12:

- **Product (PDP) short descriptions** — "numbing cream / gel / spray" may be used as the product-type noun.
- **Guide / SEO page body copy whose `<title>` targets the term** — the noun may appear in running copy on pages built to rank for "numbing cream" and its variants (e.g. the system/choosing/how-to guides), where the page is unreadable without naming the product type.

This does **not** loosen the Hard Rule. "numbing" / "numbs" used as an **effect or efficacy claim** — "numbs the skin", "a numbing effect", "arriving already numbed", "numbing reduces sensation/discomfort", "how numbing fits in" — remains **banned everywhere**, including PDPs and guide pages. The noun names the product type; the moment it describes an effect on skin or sensation, it's a violation.

> **Open gate (2026-06-12):** the full-site audit found live *effect-use* of "numbing/numbed" that breaches the Hard Rule. Per owner instruction that copy is **routed to MHG/legal review** and was not rewritten; it remains a pre-public-go-live gate. See `DECISIONS-LOG.md` 2026-06-12.

### Product naming — UK cosmetics compliance

The word "numbing" must not appear as or within a Senseless product name, product description attributing an effect to the product, or any copy that implies the product produces a numbing or anaesthetic effect on the skin. This constitutes a medicinal efficacy claim under UK cosmetics law and risks reclassification of the product as a medicine requiring MHRA licensing.

Senseless product names use **"Comfort"** — **Comfort Cream, Comfort Gel, Comfort Spray**. These describe the user experience without asserting a physiological mechanism.

"Numbing cream/gel/spray" may appear as a **search category term** on SEO-facing surfaces (collections, meta descriptions using it as a keyword, guide body copy, article copy) where it describes consumer search intent and does not attribute a numbing effect to the Senseless product specifically.

**The test:** does the copy claim or imply that the Senseless product numbs the user? If yes → rewrite. If the copy describes a search category or generic consumer intent → permitted.

This rule connects to the standing "numbing" effect-claim ban already in this document. The product naming rule is its application to titles, descriptions, and brand copy.

## Compliance Checklist (run before any user-facing copy ships)

- [ ] No hard-rule phrases in headline, body, alt text, meta, or CTA
- [ ] All efficacy claims rewritten as observational/preparation language
- [ ] Three-tier names used correctly (Clinical / Advanced / Professional)
- [ ] No percentage claims
- [ ] No specific timing claims
- [ ] No comparisons to lidocaine products on efficacy
- [ ] No before/after imagery implying medicinal outcome
- [ ] Product described as "preparation before treatment", not "treatment itself"
- [ ] Schema markup uses "Product" type, not "Drug" or "Medicine"
- [ ] Testimonials use observational language only

## Voice

- Professional but warm
- Confident without being clinical-cold
- Empowering — comfort as confidence
- Female-oriented without being exclusionary
- Premium
- Never casual, never hype
- UK spelling throughout (aesthetic, colour, neighbour, organisation)
