# Homepage System update + System-guide gap-fill + retire Choosing Your Strength

**Date:** 2026-06-02 (BST) · **Branch:** dev · **Commits:** `cf516d1` (T1), `59dec97` (T2), redirect via API (T3) · **Theme:** Senseless Dev `#199324434780`
Token refreshed (`./scripts/refresh-token.sh`); shop = senseless-numbing.

## Task 1 — Homepage System-language update v4 (theme)
Source: Homepage model v4 block (`36c58bc375ea81a2a4a3cadf143e3136`). Applied verbatim to `templates/index.json`:
- **Hero subhead** → "Senseless is a system — match the strength and the format to the appointment you've booked. Three strengths, three formats, formulated in the UK."
- **Hero secondary CTA** → "How the System works" → **/pages/the-senseless-system** (was /pages/choosing-your-strength).
- **Section 2** (`senseless-trio-card-row`): eyebrow **unchanged** ("The Senseless system"); headline → "Match the strength to your session."; body → new "Strength is the first half of your selection…" copy; closer → "Together, they're your Senseless Selection." **linking to /pages/the-senseless-system** (trio gained an optional `closer_url`). Tier cards + section structure unchanged.
- **Render-verified (200):** subhead, "three formats", secondary CTA label+href, §2 headline/body, closer link, eyebrow kept, no choosing-your-strength in hero. theme-check 0.

## Task 2 — System guide gap-fill (theme)
Source: System guide model (`37358bc375ea81b6a070e7e2145c7bf7`). Added the three missing things verbatim to `templates/page.the-senseless-system.json`:
- **§4 reassurance line** (after the pull-quote): "Clinical isn't a weaker version of Professional…" — `senseless-strength-ladder` gained an optional `reassurance` field.
- **§7 Key Facts** (NEW, GEO-extractable): `senseless-rich-text`, eyebrow "The essentials", 4 bullets (verbatim). Head clean (no accent).
- **§8 FAQ** (NEW): `senseless-faq-accordion`, "Common questions", 4 Q&As (verbatim) — **emits FAQPage JSON-LD**. Head clean.
- **§9 route to shop** renumbered (order: hero → what → dial1 → dial2 → matrix → honest → **keyfacts → faq → route** → schema).
- **Render-verified (200):** reassurance renders; Key Facts 4 bullets + "The essentials"; FAQ "Common questions" + 4 Q&As; **JSON-LD = WebPage + BreadcrumbList + FAQPage**; accents intact (Selection · System · format · strength · procedure · skip), Key Facts + FAQ heads clean. theme-check 0; Asset-API diff (caught Shopify pruning the new `reassurance` setting on the combined push — re-pushed the template; confirmed present on remote).

## Task 3 — Retire Choosing Your Strength (admin/API) — after Task 2 verified live
- **301 redirect created:** `/pages/choosing-your-strength` → `/pages/the-senseless-system` (`urlRedirectCreate`, id `…/UrlRedirect/1681505091932`). **No scope error.** Verified live: requesting the old path lands on the guide (200).
- **Unpublish: N/A** — there is **no `choosing-your-strength` page resource** (it only ever existed as the stale `templates/page.choosing-your-strength.json` file; the URL was 404ing). Nothing to unpublish. The stale template file remains in the repo (harmless without a page resource) — retire in a cleanup pass if wanted.
- Other sitewide links **not repointed** (Phase 12), per the brief.

## §11 gate (guide-applicable) + compliance
- **0 banned words**; reduce-not-eliminate; no efficacy/duration/onset/% claims; "formulated in the United Kingdom" (no "made in the UK").
- Injectable-clean: homepage stays injectable-clean (links to format collections + guide); the guide matrix names injectables (RELAXED per model — guide, not ad surface).
- GEO: guide now carries Key Facts (extractable bullets) + FAQPage schema + WebPage + the named "The Senseless System."
- theme-check **0**; Asset-API diff clean (after the reassurance re-push); render-verified 200 on homepage + guide + redirect.

## Files / API
- `templates/index.json` (hero + §2), `sections/senseless-trio-card-row.liquid` (+closer_url) — Task 1.
- `templates/page.the-senseless-system.json` (+reassurance/keyfacts/faq), `sections/senseless-strength-ladder.liquid` (+reassurance field) — Task 2.
- API: urlRedirectCreate — Task 3.

## Build-process note
Adding a new section setting + setting it in a template in the **same push** can have Shopify prune the unknown setting (the template validates before the section schema commits) — seen again on `reassurance`. Always Asset-API-diff after, and re-push the template once the section schema is live.

## HOLD
All three tasks done, verified live (homepage 200, guide 200 with FAQPage, redirect resolves). Nothing else started.
