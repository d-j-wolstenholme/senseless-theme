# Stage C / Step 2a — Collections (senseless-numbing)

**Date:** 2026-06-01 (BST)
**Machine:** MacBook Pro
**Branch:** dev
**Store:** senseless-numbing.myshopify.com (confirmed via `{ shop }` before any mutation)
**Scope:** Create the 5 catalogue smart collections (3 format + Shop All + Aesthetic hub), all published to Online Store. **No procedure collections (Step 2b). No product-page content (Stage D).**

> Source: runbook "Stage C collection mechanic (1 June)" + Strand 3 collection rules. Strand 3's product-structure section ignored (stale — variant model locked in Stage C1). SEO descriptions for the three format collections pulled from the Master Page Database Meta Description fields; the hub uses the runbook's verbatim text; Shop All left blank (no matching page) — refined in Stage D.

---

## Result — ✅ all checks pass

- **5 smart collections** created, exact handles, **single rule each** (`appliedDisjunctively=false`).
- **All published to Online Store** (`gid://shopify/Publication/354304655708`).
- Membership resolves exactly as expected: **numbing-cream 3 · numbing-gel 3 · numbing-spray 3 · shop-all 10 · aesthetic-numbing-cream 9**.
- Foam (`foaming-cleanser`, type Cleanser) correctly **in shop-all**, **excluded from aesthetic-numbing-cream**.
- Every numbing product joined its format collection — **no join failures**.

### Method
`collectionCreate` (smart, single rule, `seo.description`) → `publishablePublish` to Online Store per collection. Verified by an independent `collections` query: `productsCount`, member handles, `publishedOnPublication`, plus a per-product format-collection membership cross-check.

---

## Collections — GIDs / handles / rules / counts / publish

| # | Title | Handle | Collection GID | Rule (single, AND) | Members | Online Store | SEO desc |
|---|---|---|---|---|---|---|---|
| 1 | Numbing Cream | numbing-cream | gid://shopify/Collection/690349932892 | `TYPE == Cream` | **3** | ✅ | set |
| 2 | Numbing Gel | numbing-gel | gid://shopify/Collection/690349965660 | `TYPE == Gel` | **3** | ✅ | set |
| 3 | Numbing Spray | numbing-spray | gid://shopify/Collection/690349998428 | `TYPE == Spray` | **3** | ✅ | set |
| 4 | Shop All | shop-all | gid://shopify/Collection/690350031196 | `VARIANT_PRICE > 0` | **10** | ✅ | blank |
| 5 | Aesthetic Numbing Cream | aesthetic-numbing-cream | gid://shopify/Collection/690350063964 | `TYPE != Cleanser` | **9** | ✅ | set |

### Membership detail
- **numbing-cream (3):** clinical-strength-cream, advanced-strength-cream, professional-strength-cream
- **numbing-gel (3):** clinical-strength-gel, advanced-strength-gel, professional-strength-gel
- **numbing-spray (3):** clinical-strength-spray, advanced-strength-spray, professional-strength-spray
- **shop-all (10):** all 9 numbing products + foaming-cleanser
- **aesthetic-numbing-cream (9):** all 9 numbing products (foaming-cleanser excluded ✓)

### SEO descriptions (collection record `seo.description`)
- **numbing-cream:** "UK-formulated numbing cream in three strengths. Clinical for routine appointments, Advanced for longer sessions, Professional for clinicians." *(Master Page DB)*
- **numbing-gel:** "UK-formulated numbing gel in two strengths — Advanced and Professional. A different application for procedures that suit a gel over a cream." *(Master Page DB)*
- **numbing-spray:** "UK-formulated numbing spray in Advanced and Professional strengths. For body areas, broader coverage, and injection preparation." *(Master Page DB)*
- **shop-all:** *(blank — no matching Master Page DB page; refine in Stage D)*
- **aesthetic-numbing-cream:** "UK-formulated numbing for aesthetic procedures. Made for lip fillers, Botox, microneedling, laser, SPMU, and waxing." *(runbook verbatim — SEO umbrella; "numbing" category-noun + procedure mentions permitted on this background hub)*

## Notes
- The default "Home page" (`frontpage`) collection pre-existed on the store; untouched. No handle conflicts (`all` reserved → used `shop-all`).
- The Notion Numbing Gel page Meta Description says "two strengths"; the locked range (Stage C1) has **3 gel products** incl. Clinical Strength Gel. Per the runbook, the meta text was pulled verbatim and is refined in Stage D — flagged, not a blocker.

## Also this session
- **Correctness fix:** `commit-and-deploy` skill (`.claude/skills/commit-and-deploy/SKILL.md`) Shopify-push step updated `senseless-tattooing` → `senseless-numbing`.

## Not done (by design)
- No procedure collections (Step 2b — awaiting confirmation).
- No product-page content / images (Stage D).
- No collection bodies (`descriptionHtml` left empty; only `seo.description` set).

## Next
- **Await confirmation** before Step 2b (procedure collections).
