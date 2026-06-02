# Track B — Store integrity pass (audit + fix + injectable confirmation)

**Date:** 2026-06-02 (BST) · **Machine:** MacBook Pro (continued) · **Branch:** dev
**Theme:** Senseless Dev `#199324434780` · **Store:** senseless-numbing.myshopify.com
**Scope:** audit-first (read-only) → fix only what's genuinely broken → confirm injectable link-isolation. Ran parallel to Stage-2 collection copy; coordinated so no template-JSON collision (Stage-2 gel/spray committed first in `75c9eb2`).
**Headline:** the store is in better shape than the 1-June report implied — products **are** in collections, all 10 product template-suffixes are **correct**, and there are **zero broken collection/product links**. The real gap is unbuilt interim pages.

## Part 1 — AUDIT

### 1.1 Products → collections (15 SKUs / 10 products)
| Product | suffix | key collection memberships |
|---|---|---|
| clinical/advanced/professional-strength-cream | ✅ correct | **numbing-cream** ✓, shop-all, aesthetic-numbing-cream (legacy), + injectable/procedure |
| clinical/advanced/professional-strength-gel | ✅ correct | **numbing-gel** ✓, shop-all, aesthetic-numbing-cream, + some procedure |
| clinical/advanced/professional-strength-spray | ✅ correct | **numbing-spray** ✓, shop-all, aesthetic-numbing-cream, + some procedure |
| foaming-cleanser | ✅ correct | shop-all only ✓ (aftercare; not in any numbing/procedure grid) ✓ |

**Empty collections:** none. **Core format collections correct:** numbing-cream/gel/spray = exactly their 3 strengths each.
**Procedure collections are non-empty but inconsistent** (microneedling 4, laser 6, spmu 4, waxing 3 — most lack the Clinical strength and some formats). Per the brief these are finalised against the Stage-2 batch-2 plan; deferred (see Fixes).
**Legacy umbrella `aesthetic-numbing-cream`** holds all 9 numbing products, suffix None, **not linked anywhere** → orphan (flag).

### 1.2 Template-suffix assignment
- **Products:** all 10 have the correct bespoke `product.<handle>` suffix, and each matches a deployed template file ✅.
- **Collections with correct bespoke template:** numbing-cream / numbing-gel / numbing-spray ✅ (suffix set + file deployed).
- **Collections with blank suffix (render Horizon default):** shop-all, aesthetic-numbing-cream, the 4 procedure collections, the 3 injectable collections, frontpage. Repo HAS template files for the procedure + injectable + aesthetic-umbrella collections, but their suffixes are intentionally unset (see Fixes — stale/deferred/HOLD). `shop-all` has no bespoke template (default is acceptable for a catch-all).

### 1.3 Sitewide link integrity
Crawled `senseless-main`, the 3 `senseless-footer-*` menus, `index.json`, and in-body links on built collection/product templates. (Horizon's default `main-menu`/`footer`/`customer-account` menus also exist but aren't used by the senseless header/footer sections.)

- **(a) Resolves live:** every `/collections/*` target (numbing-cream/gel/spray, shop-all, the 4 procedure collections, the 3 injectable collections, aesthetic-numbing-cream), all 10 `/products/*`, `/`, `/collections/all`, `/search`, `/pages/contact`. Spot-checked 200s on the 4 procedure collections + shop-all + numbing-cream-for-botox.
- **(b) Interim — unbuilt pages (intended; only `contact` exists as a page resource):**
  - Brief's expected four: `/pages/aesthetic-procedures`, `/pages/choosing-your-strength`, `/pages/choosing-your-format`, `/pages/how-it-works` (404 confirmed).
  - Additional intended-but-unbuilt: `/pages/about`, `/pages/faq`, `/pages/trade`, `/pages/how-to-apply`, `/pages/how-long-numbing-cream-takes-to-work`, `/pages/how-long-numbing-cream-lasts`, `/pages/does-numbing-cream-work`.
  - **15 page *templates* exist in repo** (about, best-emla-alternative-uk, best-numbing-cream, choosing-your-format, choosing-your-strength, contact, does-numbing-cream-work, faq, how-it-works, how-long-numbing-cream-lasts, how-long-numbing-cream-takes-to-work, how-to-apply-numbing-cream, senseless-vs-ametop, strongest-numbing-cream, trade) — but **no page resources** back them (except contact). Wave 4 must create the page resources + assign suffixes.
- **(c) Genuinely broken (wrong handle):** **none in collection/product links.** One nav handle mismatch flagged: nav "How to apply" → `/pages/how-to-apply` while the repo template is `page.how-to-apply-numbing-cream.json` (handle differs) — unfixable now (neither page exists); reconcile at Wave-4 page build. The `/collections/numbing-cream?strength=clinical|advanced|professional` nav links resolve to numbing-cream but the `strength` param is **inert** (the grid's filter is off) — flag, not broken.

## Part 2 — FIX
After the audit, **no API mutations were warranted** — every item is already correct, intentionally deferred, or a planning decision:
1. **Products → collections:** core format collections already correct; foaming-cleanser correct. Procedure-collection membership is **deferred to Stage-2 batch 2** (the brief defers the per-procedure set to the finalised plan; grids are already non-empty so nothing is broken now). Injectables: HOLD (Part 3).
2. **Template assignment:** products + format collections already correct. Procedure collection templates in the repo are **stale** ("two strengths" residue) and are being rebuilt + assigned in batch 2 — assigning them now would activate stale copy, so they're left unset. Injectable + legacy-umbrella suffixes left unset (deferred / legacy). **No wrong assignment to correct.**
3. **Broken links:** list (c) is empty for collection/product links → nothing to repoint. The one nav/template handle mismatch (how-to-apply) and the inert strength params are flagged for Wave-4 / a nav tidy, not auto-changed.
4. **Interim-page stub — PLANNING DECISION (flagged, not auto-created):** `/pages/aesthetic-procedures` is linked from every collection's "see all procedures" + nav "By procedure" + homepage, and currently 404s. **Stub a minimal placeholder now, or accept the 404 until Wave 4?** Recommend a minimal stub (it's the most-linked interim target).

## Part 3 — Injectable templates (closes built-state punch-list #5)
Injectable collections: `numbing-cream-for-botox`, `numbing-cream-for-injections`, `numbing-cream-for-lip-fillers` (exist, URL-reachable — botox spot-checked 200 — with products + bespoke template files, suffix unset).
**Confirmed ZERO inbound links from any ad-facing surface:**
- `senseless-main`: "By procedure" lists Microneedling / Laser / SPMU / Waxing only — **no botox/injections/lip-fillers** ✓
- `senseless-footer-shop/-explore/-company`: no injectable links ✓
- `index.json` (homepage): procedure links are microneedling/laser/spmu/waxing only ✓
- Ad-facing collection related-rows: cream→gel+spray, gel→cream+spray, spray→cream+gel; "see all procedures" → `/pages/aesthetic-procedures` — **no injectable links** ✓
- Built product templates: no injectable-collection links ✓

Per Canonical §2 #5 they are kept (intentional Wave-3b SEO scaffolds), not deleted. **Flag for planning:** apply `noindex` until Wave-3b? (content/SEO decision — not actioned here).

## Other flags for planning
- **Legacy `aesthetic-numbing-cream` umbrella** (9 products, template file, unlinked) — retire, relink, or leave as background? Not in the new "By format / By procedure" map.
- **Inert `?strength=` nav links** under "By strength" — either wire a strength filter into the grid or repoint these to the per-strength experience when built.
- **15 page templates ready, 0 page resources** (except contact) — Wave 4 needs to create the page resources (and reconcile the how-to-apply handle).

## Build / verification
- **No code or template-file changes** in this pass → theme-check unchanged (**0 errors**); no Asset-API diff needed.
- Render spot-check (preview theme): procedure collections + shop-all + injectable-botox = **200**; aesthetic-procedures / how-it-works / about = **404** (expected interim).
- This report is the only committed artefact.
