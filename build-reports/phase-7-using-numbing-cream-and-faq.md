# Phase 7 — Using numbing cream guide + FAQ/knowledge base

**Date:** 2026-06-03 (BST) · **Branch:** dev · **Theme:** Senseless Dev `#199324434780` (store `senseless-numbing`)
Token refreshed (`./scripts/refresh-token.sh` → shpca_eefb99…). Build source: spec `37458bc375ea8185ade2cc3d0c0cb9e8`, copy verbatim. **This is Phase 7 — fills the flagged faq / how-long-lasts / how-long-to-work / does-numbing-cream-work 404s.**

## Pages built (both via Admin API, published, suffix set)
1. **`/pages/using-numbing-cream`** (template `page.using-numbing-cream`, page id `711028867420`) — usage guide; owns "how long does numbing cream last" (600). Order: hero → §1 honest answer → §2 how to use (steps) → §3 how long to leave on → §4 how long it lasts → §5 route to System → §6 Key Facts → §7 FAQ (4 Q&As, FAQPage) → §8 route forward.
2. **`/pages/faq`** (template `page.faq`, page id `711028900188`) — FAQ/knowledge base; hero → intro band → FAQ (10 Q&As in 3 groups) → Key Facts → route forward.

Both modules reused (guide hero, editorial band, rich-text, Key Facts via rich-text, FAQ accordion, link row, page-schema). Schema on both: **WebPage + BreadcrumbList + FAQPage**.

## FAQ accordion enhancement (single FAQPage + visual groups)
Added an optional `group` field to `senseless-faq-accordion` `faq_item` blocks: a group sub-heading renders when the group changes, while the FAQPage JSON-LD stays **one** block over all items. The FAQ page shows 3 groups (About the products / Safety & skin / Using it with treatments) but emits a single FAQPage with all 10 questions. Additive + backward-compatible (no default → existing FAQ sections unchanged).

## Meta (global.* metafields)
- Usage guide: title 56 (≤60); description **159** (spec verbatim — 4 over the 155 guideline; flagged).
- FAQ: title 59 (≤60); description 146 (≤155).

## Nav + redirects
- **The System dropdown** → added **Using numbing cream** → `/pages/using-numbing-cream` (3rd item, after Does it hurt?).
- **Help dropdown** repointed the stale 404 slots (menuUpdate): "How long to work" + "How long to last" → `/pages/using-numbing-cream`; "Does numbing cream actually work" → `/pages/faq`; "FAQ" → `/pages/faq` (now built/live).
- **301 redirects** created so the old paths resolve everywhere (sitewide inbound links too): `/pages/how-long-numbing-cream-takes-to-work` + `/pages/how-long-numbing-cream-lasts` → `/pages/using-numbing-cream`; `/pages/does-numbing-cream-work` → `/pages/faq`.

## §11 / compliance gate (critical on this cluster)
- **No product-specific minutes/hours/onset/% anywhere** — all timing framed general + "follow the product's instructions" + practitioner-routed (verified by scan). Reduce-not-eliminate throughout; "formulated in the United Kingdom"; cosmetic, not a medicine. 0 banned words. Every FAQ lead sentence is compliant standalone.
- **Sensitive-topic line present** in the side-effects answer: "…if you have a reaction or any concern, stop and speak to a professional."

## Verify
- **theme-check: 0 errors** (24 pre-existing Horizon warnings; none on changed files).
- **Asset-API diff:** section + both templates landed. Caught the known **combined-push pruning** — the new `group` block values were stripped when the section's new field + the template shipped together; **re-pushed `page.faq.json` alone** (section field already live) → group values confirmed on remote (`About the products` / `Safety & skin` / `Using it with treatments`).
- **Render-verify (Playwright, live preview):** both pages **200**; schema **WebPage + BreadcrumbList + FAQPage** on each; usage guide FAQ = 4, links resolve (Selector); FAQ page = **single FAQPage with 10 questions**, **3 group headings**, 10 items, side-effects sensitive line present. **All 3 repointed nav slots + the 3 old paths resolve 200** (old paths 301 → the new pages).

## Notes / flags
- **Replaced a stale `page.faq.json` draft.** A prior, more elaborate `page.faq.json` existed (6 topic groups, multiple separate FAQPage sections, `format_card` blocks, and links to retired/404 paths — `how-it-works`, `choosing-your-strength`, `does-numbing-cream-work`, `how-to-apply-numbing-cream`, `collections/aesthetic-numbing-cream`). It was never wired to a page resource (faq was 404). Replaced with the Phase 7 spec version (single FAQPage, current links). If any of the old Q&As (sizes, pregnancy, contraindications, trade, aftercare) should be folded back in later, they're in git history (pre-`<this commit>`).
- **Help dropdown redundancy (minor):** "How long to work" + "How long to last" both now point to the usage guide; "FAQ" + "Does numbing cream actually work" both point to /pages/faq. Repointed as the brief instructed (kill the 404s); a future Help-dropdown cleanup could dedupe/relabel.
- Remaining flagged 404: **About** (`/pages/about`) — per spec, Phase 9.

## Files / API
- New: `templates/page.using-numbing-cream.json`. Replaced: `templates/page.faq.json`. Edited: `sections/senseless-faq-accordion.liquid` (+group field).
- API: `pageCreate` ×2, `metafieldsSet` ×2, `menuUpdate`, `urlRedirectCreate` ×3.

## HOLD
Both pages live + verified; flagged 404s (faq, how-long-lasts, how-long-to-work, does-numbing-cream-work) now resolve. Phase 7 complete.
