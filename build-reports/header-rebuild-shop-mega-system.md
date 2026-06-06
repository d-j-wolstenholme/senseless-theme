# Header rebuild — Shop mega-menu + The System learning hub (one pass)

**Date:** 2026-06-06 (BST) · **Branch:** dev · **Theme:** Senseless Dev `#199324434780` · **Commit:** `01a4afc`. Token refreshed.

Both dropdowns rebuilt in a single header pass so the section is touched once. They are now **bespoke** (keyed on the top-level title — "Shop" / "The System"), not menu-driven, so they render the exact required structure regardless of the linklist's child items. Any *other* top-level item with menu children (e.g. Help) still renders a generic dropdown. Top-level nav order stays menu-driven (`senseless-main`). No menu API changes were made.

## PART 1 — Shop mega-menu (4 columns + featured card + Shop-all CTA)
- **Col 1 — By product:** format headings → collections (`/collections/numbing-{cream,gel,spray}`). Each format reveals its **3 strengths** (direct to size-agnostic product pages `/products/{clinical,advanced,professional}-strength-{cream,gel,spray}`) + "Shop all [format]". **Hybrid interaction:** desktop = sub-panel opens on **hover OR keyboard-focus** (`aria-expanded`, not hover-only); mobile = nested **tap accordion**. **Foaming Cleanser** = flat product link, no sub-menu.
- **Col 2 — By procedure:** Microneedling · Laser hair removal · Semi-permanent makeup · Waxing → procedure collections + **"See all procedures →"** `/pages/aesthetic-procedures`.
- **Col 3 — By strength:** Clinical · Advanced · Professional **+ "Find your strength →"** — **all four → `/pages/the-senseless-system`** (the help-me-choose hub). Per the mid-brief update, the `?strength=` filter is **cancelled**; direct strength→product shopping lives in Col 1.
- **Col 4 — Bundles:** the 5 kit products iterated from the `bundles` collection (**live titles, rename-proof**) + **"Shop all bundles →"** `/collections/bundles`.
- **Featured card:** swappable via new section settings (image / eyebrow / title / text / url / cta). Defaults to the Advanced "Complete" kit (`/products/advanced-numbing-kit-large`); **neutral brand placeholder** until bundle photography exists.
- **Shop-all button:** filled-purple CTA at the foot, kept (`mega_cta_*`, default `/collections/shop-all`).

## PART 2 — The System (Layout B learning hub)
- **Read-first card:** eyebrow "The System", title "The Senseless System", line "How strength and format match what each appointment asks of the skin. Start here.", button **"Read the system"** → `/pages/the-senseless-system`.
- **Understand by procedure:** Microneedling · Laser hair removal · Semi-permanent makeup · Waxing → the 4 procedure **collections** (the educational read of the same pages Shop links transactionally).
- **Application guides:** Using numbing cream · How long it takes to work · How long it lasts → `/pages/using-numbing-cream`; Does it actually work? → `/pages/faq` (intended duplicates kept).
- **Comfort & pain:** **"Does it hurt?" as a single door** → `/pages/does-it-hurt` + descriptor "Comfort by treatment — full breakdown inside." (no per-procedure pain children — the hub fans out).

## Verify (theme-check + password render, desktop + mobile)
- **theme-check: 0 errors** (52 warnings — `ValidScopedCSSClass` on new BEM classes, the standing theme baseline).
- **Injectable-clean grep = 0** on the section source *and* on the rendered header+drawer DOM (only the doc-comment names the rule).
- **Desktop:** Shop + System panels open; format flyout opens on **click and keyboard-focus**; Shop trigger opens on **keyboard-focus** (not hover-only).
- **Mobile drawer:** Shop accordion → 4 groups; format sub-accordion «Numbing Cream» expands → Clinical/Advanced/Professional/Shop all cream; System accordion → 3 groups.
- **All 29 unique targets resolve 200, no 301** — incl. `/pages/the-senseless-system` direct, `/pages/aesthetic-procedures`, `/pages/does-it-hurt`, all 9 strength products, 3 format + 4 procedure + bundles + shop-all collections.
- **does-it-hurt hub fan-out confirmed:** links to `does-microneedling-hurt`, `does-laser-hair-removal-hurt`, `does-it-hurt-by-treatment` (per-procedure pain pages) — so the single-door reliance is sound.
- **Compliance:** new copy clean — no claim/onset/duration words, no "avoid" tier phrases, Professional not flagged strongest/flagship; "numbing" used only as the category descriptor (approved exception).

## Files
- Edited: `sections/senseless-header.liquid` (full rebuild — CSS, two bespoke desktop panels, two bespoke drawer accordions, flyout + nested-accordion JS, new featured-card settings).

## Open questions / explicit assumptions (Hard Rule #6)
1. **"By strength" targets** — the brief first said "keep targets as-is / existing ?strength= links," but the live menu actually pointed at product pages. Your mid-brief update resolved it: **all four → the System page, ?strength= cancelled.** Built that way.
2. **Injectable-clean on two mandated educational destinations.** The menu itself and every **commerce** destination are 100% injectable-clean. But two pages the brief *mandates* linking contain **educational, non-commerce** Botox/lip-filler text:
   - **The System page** (`/pages/the-senseless-system`) — its suitability matrix lists "Lip fillers" and "Botox" as **text-only rows** (recommendation guidance, no links).
   - **does-it-hurt hub** — body mentions "lip filler, Botox" and the by-treatment guide has `#lip-filler` / `#botox` **anchors** (intra-guide, not commerce).
   These are consistent with the established **organic/educational-exempt** doctrine (injectable-clean = no *ad-facing commerce* inbound to the injectable collections), and the brief itself requires linking both pages. **Proceeded** linking them as-is and flagging here, rather than silently editing two out-of-scope pages. If you want a strict reading (zero Botox/lip-filler even as educational text on menu-linked pages), that's a separate content/compliance edit to those two pages — say the word.

## Notes
- Shop/System panels are now decoupled from the menu's child links — editing those children in the Shopify menu editor won't change the panels (intended; prevents the past menu-rebuild regression). Settings (featured card, Shop CTA) remain editable in the theme editor.

## HOLD
Header rebuild live + verified on the dev theme. Awaiting next brief.
