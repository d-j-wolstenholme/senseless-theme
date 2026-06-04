# Blog (Guides) + Article Hub + 6-draft port

**Date:** 2026-06-04 (BST) · **Branch:** dev · **Theme:** Senseless Dev `#199324434780` · **Commit:** `e1d712b`. Token refreshed.

## PART A — Blog infrastructure
- **Blog `guides`** created (`/blogs/guides/<slug>`); blog `template_suffix` set to `guides` (blog templates select by suffix, NOT handle — caught: the hub first rendered the default `blog.json` until the suffix was set).
- **Custom article template** `sections/senseless-article.liquid` + `templates/article.guides.json`: answer-first opener, **Key Facts** (the lead blockquote rendered as a purple callout), body (`article.content`), **FAQ accordion** (from the `custom.faq` json metafield), funnel CTAs (in body). Emits **Article + BreadcrumbList + FAQPage** JSON-LD. Brand tokens (#6B3FA0, Montserrat, canvas).
- **Article Hub** `sections/senseless-article-hub.liquid` + `templates/blog.guides.json` at `/blogs/guides`: intro + 1:1 article cards (title + one-line) + links up to the Does-it-hurt hub and Shop. **Blog + BreadcrumbList** schema.

## PART B — 6 drafts (highest volume first), verbatim
Ported **5** of 6 from the Master Page DB (`collection://67d15409-2989-4e29-996c-e51aeab6a8d7`), copy verbatim:
1. how-long-does-botox-take-to-work (6,200) ✓
2. lip-filler-aftercare (1,600) ✓
3. botox-for-jowls (1,300) ✓
4. does-botox-hurt (800) ✓
5. do-lip-fillers-hurt (350) ✓
- **does-microblading-hurt — NOT built (no draft).** There is no standalone "Does Microblading Hurt" draft in the DB; the topic was deliberately scoped as **FAQ-sized within the SPMU collection** ("does microblading hurt (350) … FAQ-sized, no standalone page"). Per the brief ("if a draft's full copy isn't present, report which and build the rest — don't compose"), I did not compose it. **Flagged for Daniel.**

## Funnel + port fixes
- Funnel CTAs wired per article: Botox articles → `/collections/numbing-cream-for-botox`; lip-filler articles → `/collections/numbing-cream-for-lip-fillers`; lip-filler-aftercare → `/products/foaming-cleanser`; all → "Find your strength" → `/pages/the-senseless-system`.
- **Stale `/pages/choosing-your-strength` → `/pages/the-senseless-system`** (and dropped the out-of-scope `/pages/how-it-works` reference) in every article.
- **Out-of-scope `/blogs/guides/botox-bruising` link dropped** from botox-for-jowls (that article isn't in scope → would 404).
- **Sibling cross-links** does-botox-hurt ↔ do-lip-fillers-hurt added (and do-lip-fillers-hurt → lip-filler-aftercare).
- FAQ stored as `custom.faq` json (powers both the accordion and FAQPage schema). Meta via `global.title_tag`/`global.description_tag` — all titles ≤60; **4 descriptions trimmed to ≤155**.

## Compliance
Botox/fillers referenced as procedure names only; timings are the *procedure's*, never Senseless's; Senseless = "topical preparation"; no efficacy/pain-elimination/timing claims; "formulated in the United Kingdom"; practitioner-routed; 0 banned words. (Blogs are organic — injectable links are intended and allowed here.) Pre-publish clinical/MHG review noted on the aftercare + procedure-description articles (draft compliance notes).

## Verify
- **theme-check: 0 errors.**
- **Render (Playwright + password):** hub `/blogs/guides` renders the custom hub (5 cards + Blog schema + links to does-it-hurt/Shop); all 5 articles render `.ss-art` (hero + Key Facts blockquote + body + FAQ accordion 5/5/5/5/6) with **Article + BreadcrumbList + FAQPage** schema; **no stale links** in any body.
- **Funnel resolve:** all targets 200 (numbing-cream-for-botox, numbing-cream-for-lip-fillers, foaming-cleanser, the-senseless-system, does-it-hurt, the 3 sibling articles).
- **Live Rich Results:** the official Google test still can't fetch the password-protected store (same Phase 11 flag) — JSON-LD validated structurally (all blocks parse; Article/FAQPage/BreadcrumbList present).

## Files / API
- New: `sections/senseless-article.liquid`, `sections/senseless-article-hub.liquid`, `templates/article.guides.json`, `templates/blog.guides.json`, `scripts/build-articles.py`.
- API: blogCreate (guides) + templateSuffix; 5× article create (body_html + 3 metafields each) via REST; 4 meta-description trims.

## Flags
- **does-microblading-hurt** has no draft → not built (build a draft first, or keep it as the SPMU FAQ).
- Reviews/Rich-Results: same standing flags (Judge.me install; public-store Rich Results run).
- Photography: article heroes use placeholder frames (editorial imagery deferred).

## HOLD
Guides blog + hub live; 5 articles ported, verified, schema valid. microblading flagged (no draft).
