# Articles hub + "Articles" nav item

**Date:** 2026-06-04 (BST) · **Branch:** dev · **Theme:** Senseless Dev `#199324434780` · **Commit:** `b737f25`. Token refreshed.

## What & why
The store had **two parallel "guide" systems** with no single home: blog **articles** at `/blogs/guides/*` (reachable only from inside an article) and guide **pages** at `/pages/*` (some surfaced in The System dropdown, some orphaned). Daniel asked for a new top-level **"Articles"** nav item → a custom hub that gathers all blog content + the orphaned guide pages, and grows as blogs/articles are added.

## Built
- **New nav item "Articles"** (top-level in `senseless-main`, between The System and About) → `/pages/articles`.
- **New page `/pages/articles`** (template_suffix `articles`, published) → **`senseless-articles-hub`** section, two card groups (site styling, #6B3FA0):
  - **From the blog** — *dynamic*: every article across the configured blogs (`blog_handles` setting, default `guides,news`). Auto-includes future articles. New blogs: add the handle to the setting (Liquid can't enumerate all blogs, so it's a one-field add).
  - **Guides** — curated guide-page cards (`guide_link` blocks): `does-it-hurt-by-treatment`, `does-microneedling-hurt`, `does-laser-hair-removal-hurt`.
- Emits **CollectionPage + BreadcrumbList** JSON-LD.

## Scope decisions (per Daniel)
- **best-numbing-cream excluded** — it's SEO / top-of-funnel commercial, not a guide.
- The **3 System guides** (`does-it-hurt`, `using-numbing-cream`, `faq`) are **not duplicated** here — they stay in The System dropdown only, per the "not currently in The System" rule.

## Verify
- **theme-check: 0 errors.** Password render: `/pages/articles` 200, h1 "Articles", **From the blog** = 5 article cards → `/blogs/guides/*`, **Guides** = 3 cards → `/pages/*`; nav "Articles" → `/pages/articles` present. All targets resolve 200.
- Future-proof: adding a Guides article makes it appear in the hub automatically (dynamic loop).

## Files / API
- New: `sections/senseless-articles-hub.liquid`, `templates/page.articles.json`.
- API: pageCreate (articles, published) + `menuUpdate` (added "Articles").

## Notes / fixes hit
- `for blog in blogs` does **not** iterate blogs in Liquid (handle-access only) — switched to a `blog_handles` list. Also `blogs[h | strip]` is invalid (no filters inside `[ ]`) — stripped into a var first.
- Pre-existing flag (unchanged): `/pages/senseless-vs-ametop` + `/pages/best-emla-alternative-uk` have theme templates but no published page resource (would 404). Not part of this task.

## HOLD
Articles hub + nav item live + verified.
