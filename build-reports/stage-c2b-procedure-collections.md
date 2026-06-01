# Stage C / Step 2b — Procedure Collections (senseless-numbing)

**Date:** 2026-06-01 (BST)
**Machine:** MacBook Pro
**Branch:** dev
**Store:** senseless-numbing.myshopify.com (confirmed via `{ shop }` before any mutation)
**Scope:** Define + populate the `senseless.recommended_procedures` product metafield and create 7 metafield-driven procedure smart collections, all published to Online Store. **No nav/menus (Stage D). No product-page content (Stage D). Not starting C3.**

> Source: runbook "Decision #10" + "Final senseless.recommended_procedures mapping" (1 June).

---

## Result — ✅ all checks pass

- Metafield definition created **under `write_products`** (no scope denial).
- 9 numbing products populated with exact tokens; clinical-gel + clinical-spray set to `[]`; foam not set.
- 7 procedure smart collections created + **published to Online Store**.
- Member counts exact: **lip-fillers 3 · botox 2 · injections 3 · microneedling 4 · laser-treatment 6 · semi-permanent-makeup 4 · waxing 3**.
- **Every** procedure collection contains ≥1 Professional product. ✓
- clinical-strength-gel + clinical-strength-spray are in **no** procedure collection, but remain in their format collection (numbing-gel / numbing-spray) + shop-all + aesthetic hub. ✓

## API mechanic notes (deviations from the runbook's literal spec — intent preserved)
The runbook's shorthand didn't match the live Admin API; three corrections were needed (none is a scope/STOP condition):
1. **Type name:** `list.single_line_text` → the valid API type is **`list.single_line_text_field`**.
2. **Rule relation:** `CONTAINS` is rejected for a metafield-definition condition (`"You can't set the condition 'product metafield definition contains'"`). The working relation is **`EQUALS`**, which for a **list** metafield means "the list contains this value" — verified against a throwaway collection (Botox → exactly clinical + professional cream = 2). The metafield GID is passed via `conditionObjectId`.
3. **Capability:** the definition must have **`smartCollectionCondition` enabled** to drive rules. It can't be set at create-time for a list type, so it was enabled via `metafieldDefinitionUpdate` afterward.

---

## Metafield definition
- **GID:** `gid://shopify/MetafieldDefinition/429332955484`
- namespace **`senseless`** · key **`recommended_procedures`** · type **`list.single_line_text_field`** · ownerType **PRODUCT**
- capability **`smartCollectionCondition` = enabled**

## Per-product values set (exact tokens)
| Product handle | recommended_procedures |
|---|---|
| clinical-strength-cream | `["Lip Fillers","Botox","Waxing"]` |
| advanced-strength-cream | `["Lip Fillers","Microneedling","Laser","SPMU"]` |
| professional-strength-cream | `["Lip Fillers","Botox","Microneedling","Laser","SPMU"]` |
| advanced-strength-gel | `["Microneedling","SPMU","Laser"]` |
| professional-strength-gel | `["Microneedling","SPMU","Laser"]` |
| advanced-strength-spray | `["Laser","Waxing"]` |
| professional-strength-spray | `["Laser","Waxing"]` |
| clinical-strength-gel | `[]` (none) |
| clinical-strength-spray | `[]` (none) |
| foaming-cleanser | *(not set — cleanser)* |

## Procedure collections — GIDs / rules / counts / publish

| Handle | Collection GID | Rule (metafield `senseless.recommended_procedures`) | Members | Online Store | SEO |
|---|---|---|---|---|---|
| numbing-cream-for-lip-fillers | gid://shopify/Collection/690352292188 | EQUALS "Lip Fillers" | **3** | ✅ | set |
| numbing-cream-for-botox | gid://shopify/Collection/690352357724 | EQUALS "Botox" | **2** | ✅ | set |
| numbing-cream-for-injections | gid://shopify/Collection/690352390492 | EQUALS "Lip Fillers" **OR** "Botox" (`appliedDisjunctively=true`) | **3** | ✅ | set |
| numbing-cream-for-microneedling | gid://shopify/Collection/690352423260 | EQUALS "Microneedling" | **4** | ✅ | set |
| numbing-cream-for-laser-treatment | gid://shopify/Collection/690352456028 | EQUALS "Laser" | **6** | ✅ | set |
| numbing-cream-for-semi-permanent-makeup | gid://shopify/Collection/690352488796 | EQUALS "SPMU" | **4** | ✅ | set |
| numbing-cream-for-waxing | gid://shopify/Collection/690352521564 | EQUALS "Waxing" | **3** | ✅ | set |

*(EQUALS on the list metafield = "list contains token".)*

### Membership detail
- **lip-fillers (3):** clinical-strength-cream, advanced-strength-cream, professional-strength-cream
- **botox (2):** clinical-strength-cream, professional-strength-cream
- **injections (3):** clinical-strength-cream, advanced-strength-cream, professional-strength-cream
- **microneedling (4):** advanced/professional cream + advanced/professional gel
- **laser-treatment (6):** advanced/professional × cream, gel, spray
- **semi-permanent-makeup (4):** advanced/professional cream + advanced/professional gel
- **waxing (3):** clinical-strength-cream, advanced-strength-spray, professional-strength-spray

### SEO descriptions (collection record `seo.description`, from Master Page DB Meta Description)
- **lip-fillers:** "UK-formulated numbing for lip filler appointments. Clinical Strength is the everyday choice. Cream and gel format, made for the chair."
- **botox:** "UK-formulated numbing for Botox appointments. Clinical Strength suits most bookings. Cream, made for the chair."
- **injections:** "UK-formulated numbing for aesthetic injections. Clinical for routine appointments, Advanced for longer sessions. Built for the chair."
- **microneedling:** "UK-formulated numbing for microneedling. Advanced Strength is the everyday recommendation. Cream and gel format, built for the chair."
- **laser-treatment:** "UK-formulated numbing for laser appointments. Advanced Strength is the recommendation. Cream for face, spray for body."
- **semi-permanent-makeup:** "UK-formulated numbing for SPMU appointments. Advanced and Professional strengths for sustained pigment work on sensitive skin."
- **waxing:** "UK-formulated numbing for waxing. Spray for body coverage, cream for smaller areas. Advanced Strength is the recommendation."

## Not done (by design)
- No nav/menus (Stage D).
- No product-page content / collection bodies (`descriptionHtml` empty; only `seo.description` set).
- Not starting C3.

## Next
- **Await confirmation** before C3.
