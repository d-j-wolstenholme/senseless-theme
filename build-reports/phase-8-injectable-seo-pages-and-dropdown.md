# Phase 8 — Injectable SEO pages + Shop dropdown dedupe + The System eyebrows

**Date:** 2026-06-04 (BST) · **Branch:** dev · **Theme:** Senseless Dev `#199324434780` (store `senseless-numbing`) · **Commit:** `ddfacb3`
Token refreshed (`./scripts/refresh-token.sh` → shpca_8515a5…). Build source: spec `37458bc375ea81cb863ffa5503910254` (PRODUCTION COPY verbatim).

## PART A — header dropdown tweaks
- **A1 — Shop dedupe:** removed the redundant "Shop All / Shop the full range" group from the Shop mega (menuUpdate). Shop now shows 3 columns (By format / By procedure / By strength); the filled purple **"Shop all" button** (bottom) remains the single shop-all entry → `/collections/shop-all`.
- **A2 — The System eyebrows:** restructured The System dropdown into two eyebrow-grouped columns (same `.ss-hdr__col-title` styling as Shop): **THE SYSTEM** → The Senseless System; **GUIDES** → Does it hurt? · Using numbing cream. The column layout emits the `mega_cta` button, so I **scoped that button to the Shop item only** (`link.title == 'Shop'`) — no "Shop all" leak under The System. Verified.

## PART B — Phase 8: three injectable collections as organic-only SEO pages
Rebuilt the 3 collections with clean SEO templates (replacing the old elaborate templates that used a hardcoded product-grid incl. spray + outbound to other procedure ranges). Each: hero (H1 = primary kw + intro, kw early) → §8 quick-add grid (cream + gel) → "What to know" editorial band → Key Facts → FAQ → route forward (outbound) + Related cross-links. Copy verbatim.

| Page | Handle / suffix | Grid | Primary kw |
|---|---|---|---|
| Injections | `numbing-cream-for-injections` | 3 cream + Advanced Gel | numbing cream for injections (1,100/KD3) |
| Lip fillers | `numbing-cream-for-lip-fillers` | 3 cream + Advanced Gel | numbing cream for lip fillers |
| Botox | `numbing-cream-for-botox` | 2 cream (gel not apt per copy) | numbing cream for botox |

- **Grids cream+gel (no spray):** the collections were smart (rule on `senseless.recommended_procedures`) and cream-only. Added "Lip Fillers" to **Advanced Gel**'s `recommended_procedures` (`["Microneedling","SPMU","Lip Fillers"]`) → it joins the lip-fillers + injections grids. **Safe:** that metafield is **not rendered anywhere in the theme** (admin/smart-rule only), and the "Lip Fillers" rule is used only by the two injectable (organic-only) collections — no ad-facing ripple. Botox left cream-only (gel not in its copy/route).
- **Schema:** added **ItemList** JSON-LD to `senseless-collection-grid` (iterates `collection.products`); collections already auto-emit CollectionPage + BreadcrumbList, FAQ emits FAQPage → all four present. Set `templateSuffix` + meta on each (GraphQL).
- **Indexed:** confirmed (no `seo.hidden`, robots null) — opposite of Shop All.

## ⚠ INJECTABLE-CLEAN — the critical gate (baseline was VIOLATED; now fully clean)
The spec assumed "zero inbound links" but the audit was stale — grep found **pre-existing inbound links** to the injectable collections. Cleaned every one so the graph holds:
- **`collection.aesthetic-numbing-cream`** (procedure-hub collection) — removed the 3 injectable procedure cards (kept micro/laser/SPMU/waxing).
- **`page.does-it-hurt-by-treatment`** (nav-reachable) — repointed its 2 injectable links (lip-fillers, injections) → `/collections/numbing-cream`. *(These were my Phase 6 links; the Phase 8 absolute gate supersedes.)*
- **3 commercial landing pages** (`best-numbing-cream`, `senseless-vs-ametop`, `best-emla-alternative-uk`) — removed the Lip Fillers + Botox procedure cards from each (kept the storefront procedure cards). *(Explicit assumption: treated as ad-facing — they're classic paid-search landing pages; flagging for confirmation.)*

**Post-cleanup grep (templates/sections/snippets) = ZERO inbound links** to any of the 3 injectable collections from any other file. Enumerated ad-facing surfaces all clean: senseless-main (all menus), footer menus, homepage `index.json`, every product page, every format + procedure collection, the procedures hub, the Selector. The 3 pages link OUT (cream/gel/System) + cross-link each other only.

## §11 / compliance
- Reduce-not-eliminate; practitioner-routed hard in intro + editorial + FAQ on all 3; **Botox keeps "optional, not required"**; no efficacy/onset/duration/% ; "formulated in the United Kingdom"; cosmetic not a medicine; 0 banned words; every FAQ lead sentence compliant standalone. (Scan clean.)

## Verify
- **theme-check: 0 errors.**
- **Render-verify (Playwright, live preview, desktop + mobile):**
  - 3 injectable pages: **200**; H1 = primary kw; **JSON-LD = CollectionPage + ItemList + BreadcrumbList + FAQPage**; grids populated (injections + lip-fillers = 4 cards incl. 1 gel; botox = 2) with working quick-add; **INDEXED** (robots null); "What to know" band present. Mobile: 200, single-column grid.
  - A1: Shop mega = 3 columns, redundant block gone, filled "Shop all" → /collections/shop-all.
  - A2: The System = eyebrows "The System" + "Guides", correct links, no "Shop all" leak; Shop dropdown unchanged; mobile drawer shows the System groups.
- **Injectable-clean grep evidence:** zero inbound (above).

## Flags / assumptions
- **Meta descriptions over the 155 guideline** (spec-verbatim): injections 156, lip-fillers 160, botox 165. Kept per "meta per spec"; trim if you want them ≤155.
- **Gel handle:** spec's route-forward used `/collections/numbing-cream-gel` (doesn't exist) → used the real handle **`/collections/numbing-gel`**.
- **Commercial pages treated as ad-facing** (injectable cards removed) — confirm that's right; if they're not ad-facing, the cards can be restored. They also still carry stale `/pages/choosing-your-strength` + `/pages/how-it-works` links (301s) — broader Phase 12 link-cleanup.
- **Advanced Gel metafield** gained "Lip Fillers" (safe, not theme-rendered) to populate the cream+gel grids.

## Files / API
- Edited: `sections/senseless-collection-grid.liquid` (+ItemList), `sections/senseless-header.liquid` (mega_cta scoped to Shop), `templates/collection.numbing-cream-for-{injections,lip-fillers,botox}.json` (rebuilt), `collection.aesthetic-numbing-cream.json` + `page.does-it-hurt-by-treatment.json` + `page.{best-numbing-cream,senseless-vs-ametop,best-emla-alternative-uk}.json` (injectable-clean cleanup).
- API: `menuUpdate` ×2 (Shop dedupe + The System groups), `collectionUpdate` ×3 (suffixes), `metafieldsSet` (3 collection metas + Advanced Gel recommended_procedures).

## HOLD
Phase 8 complete + verified; Shop deduped; The System eyebrows added; **site fully injectable-clean** (zero ad-facing inbound to the 3 indexed injectable SEO pages).
