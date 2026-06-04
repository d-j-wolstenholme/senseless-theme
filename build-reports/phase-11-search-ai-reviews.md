# Phase 11 — Search/AI technical + reviews

**Date:** 2026-06-04 (BST) · **Branch:** dev · **Theme:** Senseless Dev `#199324434780` · **Commit:** `d6cbb01`. Token refreshed.

## PART A — robots.txt (AI-crawler access)
`templates/robots.txt.liquid` created. Renders Shopify's `robots.default_groups` verbatim (preserves the standard Disallow rules for cart/checkout/account/orders/search + the sitemap reference) then adds an explicit group per AI crawler — **GPTBot, ChatGPT-User, OAI-SearchBot, ClaudeBot, Claude-SearchBot, Claude-User, anthropic-ai, Google-Extended, PerplexityBot, Bytespider, CCBot, Meta-ExternalAgent** — each `Allow: /` + the same sensitive-path disallows as the default `*` group (so cart/account/checkout stay blocked for them too).
- **⚠ FLAG:** `robots.txt.liquid` only takes effect on the **published** theme. The dev theme is unpublished, so live `/robots.txt` still serves the published theme's default (verified: GPTBot absent). It will activate at launch when this theme is published. Template logic verified by inspection.

## PART B — llms.txt (GEO)
- `/pages/llms-txt` page created (templateSuffix `llms-txt`), rendered by `templates/page.llms-txt.liquid` via a minimal `layout/llms.liquid` (head with `content_for_header` so the noindex meta emits, but no nav/footer chrome).
- `/llms.txt → /pages/llms-txt` redirect created.
- **noindex:** `seo.hidden=1` metafield (number_integer — same native pattern shop-all uses; the brief's `global.noindex` isn't the theme's mechanism, `seo.hidden` is). Verified: page emits `robots: noindex,nofollow` + excluded from sitemap.
- **Content (verified):** brand summary, The Senseless System (named framework), the range (3 strengths × 3 formats + cleanser), guides, procedures, trust/safety (UK cosmetic, CPSR, cosmetic-not-medicine), MHG company details — all `{{ shop.url }}` links. Compliant, no claims.
- **Verified:** `/llms.txt` 200; raw HTML body is clean markdown (`# Senseless\n\n> …`, no cookie-banner markup — the consent banner is JS-injected only); content correct.

## PART C — Schema matrix + gap-fill
Live JSON-LD extracted per page type (all blocks parse valid — no malformed JSON). The official **Google Rich Results Test could not be run live** — it can't fetch a password-protected store; validated structurally instead (FLAG: re-run Google's tester once the store is public, or via pasted code).

| Page type | Schema emitted (after fix) |
|---|---|
| index | **Organization** (now telephone E.164 +443330495549, areaServed GB, contactPoint), WebSite/SearchAction, BreadcrumbList |
| product | Product + Offer (live price/stock), BreadcrumbList, FAQPage |
| collection | CollectionPage + ItemList, BreadcrumbList, FAQPage |
| about | **AboutPage** (was WebPage), Organization, BreadcrumbList |
| contact | **ContactPage** (added), Organization (+ContactPoint), BreadcrumbList |
| trade | **Service** (was WebPage, +provider+areaServed), FAQPage, BreadcrumbList |
| 5 policy pages | WebPage, BreadcrumbList ✓ |
| guides | WebPage, FAQPage, BreadcrumbList |

- Gap-fills via a new `schema_type` setting on `senseless-page-schema` (WebPage/AboutPage/ContactPage/Service) — no duplication (replaces the type on those pages). Homepage Organization enriched in the dispatcher.
- **sameAs:** omitted — no real social profiles exist yet (footer Instagram/TikTok are placeholders). Add `sameAs` once social URLs are live.
- **Guides → Article/HowTo:** the guides are `/pages/*` and currently emit WebPage+FAQPage (valid). Upgrading them to Article + HowTo (e.g. using-numbing-cream steps) is a content-modeling enhancement — recommend doing it alongside the blog Article template rather than retrofitting now. Flagged, not done.

## PART D — Judge.me reviews (audit)
**Judge.me is NOT installed** on senseless-numbing. Evidence: no `judgeme` product metafields (only `global`/`senseless`), no app blocks, no PDP review widget, no all-reviews page or floating tab. The theme has **one placeholder hook** ready — `data-judgeme-card` (empty star slot) in the collection grid. (`read_script_tags` denied, but metafield absence is conclusive.)
- **Daniel/ops action:** install the Judge.me app + choose a plan tier. Once installed: use the **app block** for the PDP widget (not a snippet `<div>` — Judge.me CSS suppresses `[data-from-snippet]`), set star colour **#6B3FA0**, and add the all-reviews page + floating tab per plan. Not attempted (per brief).

## Verify
- **theme-check: 0 errors.** **Asset-API diff:** all 8 changed files MATCH/semantic-match remote.
- Live render: robots template inspected (publish-gated); llms page noindex + clean content; schema matrix re-verified (AboutPage/Service/ContactPage/Org E.164 all live).

## Flags
1. robots.txt activates only on the published theme (relaunch verify at publish).
2. Google Rich Results Test pending public store / pasted code.
3. `sameAs` pending real social profile URLs.
4. Judge.me install + config is a Daniel/ops action.
5. Guides → Article/HowTo deferred to the blog Article work.

## Files
New: `templates/robots.txt.liquid`, `templates/page.llms-txt.liquid`, `layout/llms.liquid`. Edited: `sections/senseless-page-schema.liquid`, `snippets/senseless-structured-data.liquid`, `templates/page.{about,trade,contact}.json`. API: llms-txt page + seo.hidden + /llms.txt redirect.

## HOLD
Search/AI-technical layer in place + schema gaps filled + verified. Awaiting Daniel on: publish-time robots check, public Rich Results run, social sameAs, Judge.me install.
