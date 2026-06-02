# Wave 3 — Stage 2 batch 2: 4 procedure collections + format-page retrofit (§5b) + fixes

**Date:** 2026-06-02 (BST) · **Machine:** MacBook Pro (continued) · **Branch:** dev
**Theme:** Senseless Dev `#199324434780` · **Store:** senseless-numbing.myshopify.com
**Commits:** `d3e3169` (A+B: editorial fix + §5b retrofit), `8cdccf1` (C: 4 procedure collections)
**Scope:** (A) spray Editorial dark-band fix, (B) NEW §5b "What [format] is for" retrofit on cream/gel/spray + spray FAQ/meta additions, (C) build the 4 procedure collections. **HOLD** after all four.

## A · Spray Editorial dark-band fix
- `senseless-editorial-band`: removed the **`dark` background option + its CSS** entirely (brand purple/dark is an accent, never a section background). Default stays `white` (safe).
- Neutralised both dark instances: `collection.numbing-spray.json` §6 and `page.about.json` → `canvas`. Verified live: `ss-ed--dark` absent across all pages; spray Editorial now light/legible.

## B · §5b "What [format] is for" (NEW light module) + spray additions
- **New section `senseless-link-row`** — a light compact list (procedure name + one-line why + optional per-row link), NOT a card grid. Link only where the procedure collection exists; descriptive otherwise. Strength not repeated.
- Inserted §5b between §5 format-check and §6 philosophy on **cream / gel / spray**, copy verbatim:
  - Cream → all 4 procedures link (microneedling, laser, SPMU, waxing).
  - Gel → microneedling + SPMU link; "precise facial work" + "lip work" descriptive (no link).
  - Spray → waxing + laser link; "large or contoured areas" descriptive.
  - All injectable-clean (zero injectable links/terms).
- Cream §3 eyebrow aligned to **"The Senseless Scale"**.
- **Spray** (verbatim to current model): +2 FAQs — "Can I use numbing spray before injections?" + "Can I re-apply numbing spray during my session?" (customer-reported framing, not a brand claim) → **FAQPage = 10**; meta description updated to carry "injection preparation" (148 chars).
- Render-verified all three: §5b present + correctly ordered + right links + injectable-clean; spray 10 Q&As.

## C · 4 procedure collections (Microneedling, Laser, SPMU, Waxing)
Built verbatim from the model pages; **bespoke order** — unique procedure-intro §3, **no philosophy band, no §5b** (procedure pages keep the see-all-procedures cross-link). Reuses Stage-1 modules + the §8 quick-add card; **no new sections**. Composition varied (intro bg, callout styles, bands) so no two clone each other or the format pages; SPMU intro is centre-aligned.

**Section order (all four):** hero → trust → procedure-intro (editorial) → The Senseless Scale (tile, metaobject) → grid → format-check (callout + see-all-procedures) → the honest bit (callout) → what makes it Senseless (key-facts) → FAQ.

**Format leads → membership (Track B, via `senseless.recommended_procedures` metafield on the smart collections):**
| Collection | Cards (adv + pro only, no Clinical) | Membership fix applied |
|---|---|---|
| Microneedling | Gel + Cream | none (already correct) |
| Laser | Cream + Spray | removed "Laser" from both gel products |
| SPMU | Gel + Cream | none (already correct) |
| Waxing | Spray + Cream | removed "Waxing" from clinical-cream; added to adv+pro cream |

Each: **MANUAL sort** in the model card order (gel/cream/spray-first per lead, Advanced row then Professional); `templateSuffix` set to its `collection.[handle].json`; SEO title + ≤155 desc set.

### §11 gate + A–K Master Rubric + Standard-bar A — per page (render-verified)
All four PASS unless noted. Shared: theme-check **0**; Asset-API diff clean (use_metaobject + tile layout survived, no dark); editorial light/legible; "see all procedures" → `/pages/aesthetic-procedures` (now **200**).

| Dimension | Microneedling | Laser | SPMU | Waxing |
|---|---|---|---|---|
| **A** voice (verbatim) | ✅ | ✅ | ✅ | ✅ |
| **B** compliance: 0 banned · no hours/% · **0 made-in** · **0 painless/pain-free** · hurt-FAQ reduce-not-eliminate | ✅ | ✅ | ✅ | ✅ |
| **C** primary KW (H1 + §3 + Scale heading + grid heading + meta) | ✅ *for microneedling* | ✅ *for laser* | ✅ *for SPMU* | ✅ *for waxing* |
| **D** long-tail FAQ (7 Q&As) | ✅ does-microneedling-hurt | ✅ does-laser-hair-removal-hurt | ✅ microblading/lip-blush hurt | ✅ bikini/brazilian cluster |
| **E** GEO/schema | ✅ CollectionPage+ItemList+BreadcrumbList+**FAQPage(7)** | ✅ | ✅ | ✅ |
| **F** injectable-clean (no related row; no Botox/filler/injection links) | ✅ | ✅ | ✅ | ✅ |
| **G** format lead correct (no Clinical card; excluded format absent) | ✅ no spray, no Clinical | ✅ no gel, no Clinical | ✅ no spray, no Clinical | ✅ no gel, no Clinical |
| **H** trust 4 signals | ✅ | ✅ | ✅ | ✅ |
| **I** de-suffixed slugs | ✅ | ✅ | ✅ | ✅ |
| **J** §8 card (4 cards, 2 `--pro`, qty stepper, Sold out @0 stock, no "flagship") | ✅ | ✅ | ✅ | ✅ |
| **K** build (suffix↔deployed file, MANUAL sort, live prices, theme-check 0, Asset-API diff) | ✅ | ✅ | ✅ | ✅ |
| **Scale** tile + metaobject C→A→P | ✅ | ✅ | ✅ | ✅ |
| **Standard-bar A** (decision-led: decide-then-buy; Scale above grid; procedure-intro frames the page) | ✅ | ✅ | ✅ | ✅ |

**Grid default prices (entry size):** micro/SPMU gel£24.99·cream£24.99·proGel£29.99·proCream£55.99 · laser cream£24.99·spray£24.99·proCream£55.99·proSpray£29.99 · waxing spray£24.99·cream£24.99·proSpray£29.99·proCream£55.99. Inventory 0 → "Sold out" (correct).

## Page stub
`/pages/aesthetic-procedures` created + published — minimal injectable-clean hub (by-procedure ×4 + by-format ×3 links; no injectable links). Kills the sitewide 404. (Bespoke template deferred to Wave 4.)

## Flags
- **Per-card descriptors** from the models' §5 (e.g. "the usual microneedling pick") are **not rendered** — the §8 quick-add card has no per-card copy field, and "no new sections" was required. The strength label + product title + format-check section carry the meaning. Flagged for planning (would need a card-caption field if wanted).
- **Spray §5b "During-session use" tag** (mentioned in the brief) is **not in the current spray model §5b** (3 items + closing line) — not invented (do-not-recompose). The during-session content is on the page via the verbatim re-application FAQ. Add to the model §5b if a row item is wanted.
- Add-to-cart not exercisable until stock set; Judge.me per-card stars pending app install (launch-gates).

## HOLD
Batch 2 complete (4 procedure collections). **Nothing else started** — holding per instruction.
