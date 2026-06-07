# Strength collections — build, wire + verbatim templates (audited)

**Date:** 2026-06-07 (BST) · **Branch:** dev · **Theme:** Senseless Dev `#199324434780` (UNPUBLISHED). theme-check **0 errors**. Commits `60c3449` (build+wire), `6a19b5d` (verbatim templates), `0398742` (title separator). ⚠ This **intentionally reverses the 6-June "no strength collections" decision** (Daniel authorised); the cancelled `?strength=` URL-filter stays dead — smart collections replace it.

## 1. Smart collections created + published
| Handle | Rule | Members | collection.image (interim) |
|---|---|---|---|
| `clinical` | `senseless.tier == Clinical` AND `type != Bundle` | 3 (clinical cream/gel/spray) | Clinical Ultimate bundle shot |
| `advanced` | `tier == Advanced` AND `type != Bundle` | 3 (advanced cream/gel/spray) | Advanced Ultimate bundle shot |
| `professional` | `tier == Professional` AND `type != Bundle` | 3 (professional cream/gel/spray) | Professional Ultimate bundle shot |

Cleanser excluded (no tier) + bundles excluded (type=Bundle). All published to Online Store. `collection.image` is the per-strength bundle shot — **interim** (those shots carry the defective cleanser label; on the re-render swap list).

## 2. Templates — verbatim from the canonical spec (`37858bc…`)
`collection.{clinical,advanced,professional}.json`, parity with the format collections, **6-section order**, compliance copy baked into section JSON (no editable drift):
1. **hero** — eyebrow + H1 + verbatim intro (per tier)
2. **trust bar** — reused 4-signal CPSR component
3. **product grid** — auto from the collection, site-standard quick-add cards
4. **"When to choose"** editorial band — verbatim (per tier)
5. **Selector callout** — shared; verbatim body "Strength matches the appointment, not the budget…" → "Find your strength"
6. **cross-link row** — the other 2 strengths + "Shop by format" (`/collections/shop-all`) + "Shop by procedure" (`/pages/aesthetic-procedures`)

SEO titles authored **bare** per spec; the theme's global suffix supplies "| Senseless" (separator aligned to a pipe this pass to match the format collections + spec). Metas verbatim. Guardrails honoured: observational, no efficacy/%/duration/active-ingredient, injectable-clean (microneedling/laser/SPMU/waxing only — no Botox/lip filler), no "flagship".

## 3. Wiring
- **Homepage strength cards** — `tier_card` gained an **empty-safe** `collection` binding (renders `collection.image` only; **no placeholder/grey box when unset**); bound clinical/advanced/professional; "Shop [Tier]" CTAs repointed → `/collections/<tier>` (dead `numbing-cream?strength=` links removed).
- **Mega "By Strength"** — each strength head now **links to `/collections/<tier>`** (By-Product pattern: link + chevron toggle + flyout of the 3 formats + "Shop all [tier]"); mobile drawer gains the same collection link.
- **Bundle PDPs** (option-2 interim) — the 4 held shots assigned to their products + flags set interim (`image_placeholder=false` + swap note); **Professional Ultimate now also feeds the mega Featured card**; Clinical Starter keeps its correct-label shot.

## Audit (read-only, this session — desktop + mobile)
| Check | clinical | advanced | professional |
|---|---|---|---|
| Page 200 + single H1 ("[Tier] Strength") | ✅ | ✅ | ✅ |
| Verbatim hero intro | ✅ | ✅ | ✅ |
| Verbatim "When to choose" | ✅ | ✅ | ✅ |
| Selector callout (verbatim body) | ✅ | ✅ | ✅ |
| Trust bar (CPSR) | ✅ | ✅ | ✅ |
| Grid = 3 correct-tier products, **cleanser absent** | ✅ | ✅ | ✅ |
| Cross-links (2 strengths + format + procedure) | ✅ | ✅ | ✅ |
| `<title>`×1, `<meta description>`×1, brand once, **no doubling** | ✅ | ✅ | ✅ |

- Rendered titles e.g. `Clinical Strength Numbing Cream, Gel & Spray | Senseless` (single, pipe, no doubling) — consistent with format collections, articles, products.
- **Nav/CTA resolution:** homepage "Shop [Tier]" cards → `/collections/<tier>`; mega "By Strength" heads → `/collections/<tier>`; all `/collections/{clinical,advanced,professional}` resolve **200**.
- **Homepage strength cards** now show the per-strength `collection.image` (interim bundle shots); empty-safe guard confirmed in code (`{% if tier_img != blank %}` — no media/placeholder when unset).
- **Bundle PDPs** ×4 + mega Featured card filled (Professional Ultimate).

## Interim / swap list
The strength `collection.image` + the 4 bundle PDP + mega Featured images are the **interim bundle shots with the defective cleanser strength-label**. On a clean strength-less-cleanser re-render: reassign the 4 bundle products + reset the 3 strength `collection.image` → the strength cards + mega card auto-update.

## HOLD
3 strength collections built, wired, templated verbatim + audited. theme-check 0; theme unpublished.
