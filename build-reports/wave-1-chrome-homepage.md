# Wave 1 — Chrome (header/menu/footer) + Homepage

**Date:** 2026-06-01 (BST) · **Machine:** MacBook Pro · **Branch:** dev
**Theme:** Senseless Dev `#199324434780` (unpublished) on senseless-numbing · MAIN Horizon untouched
**Checkpoint:** Wave 1 — render + Daniel sign-off. **Stopped here; Wave 2 not started.**

## Notion sources read in full before building
1. Master Rebuild Brief (global rules + wave plan + protocol) — https://www.notion.so/37258bc375ea8109813ff0857e42903c
2. Homepage v3 spec (built to the Production Copy v3 map at the top) — https://www.notion.so/36c58bc375ea81a2a4a3cadf143e3136
3. Strand 2 — Global Components — https://www.notion.so/36d58bc375ea81a58487e15dec0252d3
4. Master Build Plan runbook (state + locked decisions) — https://www.notion.so/37258bc375ea815f9a4cfb6abc7eea4d

## Result — ✅ all checks pass
- **theme check:** 0 errors (24 pre-existing Horizon warnings).
- **Render (storefront password, preview theme):** homepage HTTP 200.
- **Nav populated** — desktop mega (Shop → By format · By procedure · By strength · Shop All, 4 columns) + The System / Help dropdowns; mobile drawer accordion (Shop/The System/About/Trade/Help). 20 mega sublinks. Empty-header issue cleared.
- **Footer** renders — band `ss-ft--sunken` (warm-light + hairline + ink text + purple hover); columns Shop (5) / The system (5) / Brand (3) wired to the new footer menus + legal band.
- **All 8 homepage sections present**, in v3 order.
- **Trust bar** = the 4 locked signals (UK formulated · Cosmetic product · CPSR assessed · Made for aesthetics).
- **Injectable-clean:** no Botox / Lip Fillers / Injections in nav, footer, or homepage visible text.
- **Banned words in visible copy:** 0 (everyday / considered upgrade / concentration / concentrated / clinical-grade all 0; "flagship" appears only as the internal CSS class `.ss-card--flagship`, no visible text — allowed).
- **Schema:** Organization (legalName "Matrix Health Group Ltd", brand "Senseless") + WebSite + SearchAction + BreadcrumbList all emitted on `/`.

## What was built
- **Menus (Admin API):** `senseless-main` (header, nested mega) + `senseless-footer-shop` / `-explore` / `-company`.
  - Header binds to `senseless-main` (already configured in header-group) → nav now fills.
- **Footer:** changed band from Stage-B `ink` (dark) → **`sunken`** (warm-light `#efece4`, ink text, hairline top border, purple hover) per the locked footer-band decision; footer menus now drive the columns (placeholders replaced).
- **Homepage `index.json`:** rebuilt to the v3 8-section map (was the Stage-B interim layout).
- **Schema:** added the `index` case to `senseless-structured-data.liquid` (Organization + WebSite/SearchAction + BreadcrumbList) — the previous emitter (Horizon `header.liquid`) is no longer rendered since the bespoke header replaced it.

## Spec → build audit

| Component / Section | Notion spec page | Spec said | Built | Global-Rule override applied |
|---|---|---|---|---|
| **Header (5 items)** | Strand 2 | Shop · The System · About · Trade · Help | `senseless-main`: Shop · The System · About · Trade · Help; binds to header | Trade kept in header per Master Brief "header 5 items" (Strand 2's later "Trade removed" note not applied — Brief is the override) |
| **Mega menu (Shop)** | Master Brief #3 (overrides Strand 2 axes) | By format · By procedure · By strength · Shop All | 4-column mega exactly | Decision #3 overrides Strand 2's older 2-column / category→hub models |
| — By format | #3 | Cream / Gel / Spray | → /collections/numbing-cream, -gel, -spray | — |
| — By procedure | #3 + injectable-clean | Non-injectable only: Microneedling, Laser, SPMU, Waxing | 4 procedure collections; **no Botox/Lip Fillers/Injections** | Injectable-clean rule (Strand 2's old 7-item list with injectables overridden) |
| — By strength | #3 (interim) | Clinical/Advanced/Professional → strength-filtered URLs | → /collections/numbing-cream?strength=… | Interim per #3; **repoint Wave 5 → /pages/choosing-your-strength** (flagged below) |
| — Shop All | #3 | → /collections/shop-all | column → "Shop the full range" → /collections/shop-all | `all` reserved → `shop-all` |
| **Mobile drawer** | Strand 2 | Accordion; Shop expands to format+procedure | Accordion renders all top-level + Shop sub-axes | Same injectable-clean override |
| **Footer** | Strand 2 + footer-band decision | 4-col (Shop/The system/Brand/Newsletter) + legal band; bg/sunken + hairline, ink text, purple hover | Bespoke `senseless-footer`, band `sunken`, 3 menus wired + legal band (© + MHG attribution + policies + social) | Footer-band decision (1 June) → `sunken` not dark `ink`; injectable-clean columns |
| **Home §1 Hero** | Homepage v3 | Brand promise; Primary Shop the range → /collections/numbing-cream; Secondary Find your strength → /pages/choosing-your-strength | hero-brand-led, both CTAs | Subhead "three strengths, **three** formats" (override v2 "four") |
| **Home §2 By strength** | v3 §2 + v2 tier copy | 3 tier cards → strength-filtered URLs; no section "find your strength"; Professional border+CTA, no badge | trio-card-row, 3 tier cards, closer "The system does the rest.", section CTA empty; Professional 2px border + purple CTA, no badge text | Banned-word scrub: dropped "everyday"/"considered upgrade"/"concentration"/"clinical-grade"; Layer-1 "clinics"→"studios"; "flagship" CSS-class only |
| **Home §3 By procedure** | v3 §3 | Non-injectable cards (Microneedling, Laser, SPMU, Waxing); no section "see all" | procedure-grid, 4 cards → procedure collections; no section CTA | Injectable cards (Lip Fillers, Botox) dropped; section "See all" dropped (v3) |
| **Home §4 By format** | v3 §4 | 3 cards Cream/Gel/Spray → format collections; optional terminal Shop all | format-row, 3 cards | Terminal "Shop all" **omitted** (section has no terminal-CTA slot; optional per spec) — flagged |
| **Home §5 The product** | v3 §5 / v1 copy | image-text-band → How Senseless works (/pages/how-it-works) | image-text-band (text-left) | Cosmetic positioning held; no pharma/ingredient |
| **Home §6 Trust bar** | v3 §6 + global rule | 4 signals | UK formulated · Cosmetic product · CPSR assessed · Made for aesthetics | **CPSR** overrides spec's "Cruelty-free" |
| **Home §7 For practitioners** | v3 §7 / v1 copy | image-text-band → Trade (/pages/trade) | image-text-band (text-right) | Layer-1: "clinics"→"studios / professional settings" |
| **Home §8 Newsletter** | v3 §8 | Single-field, GDPR double opt-in, no discount | newsletter-signup, double opt-in fine print | Layer-1: "clinics that stock us"→"studios that stock us" |
| **Home schema** | v3 GEO + global rule | Organization + WebSite/SearchAction + BreadcrumbList | added `index` case to structured-data snippet | — |

## Interim / future-wave links (render check accounts for these)

**Interim-pointed (repoint in Wave 5):**
- By-strength menu items → `/collections/numbing-cream?strength=clinical|advanced|professional` (resolve 200 to the unfiltered collection now; strength filter lands Wave 3; repoint to `/pages/choosing-your-strength` in Wave 5 per #3).

**Links that 404 on dev until their wave (pages built Wave 4):** these render as nav/footer links now but their targets don't exist yet —
`/pages/choosing-your-strength`, `/pages/choosing-your-format`, `/pages/how-it-works`, `/pages/how-to-apply`, `/pages/about`, `/pages/trade`, `/pages/contact`, `/pages/faq`, `/pages/how-long-numbing-cream-takes-to-work`, `/pages/how-long-numbing-cream-lasts`, `/pages/does-numbing-cream-work`, `/pages/aesthetic-procedures` (the last is the "By procedure" column-title parent URL — non-clickable column header, so no live 404 exposure).

**Slug-coordination flag (Wave 4/5):** menu + footer use the repo's current page handles (`how-it-works`, `how-long-numbing-cream-takes-to-work`, `how-long-numbing-cream-lasts`, `does-numbing-cream-work`). Strand 2 locks the *final* slugs to `how-senseless-works`, `how-long-does-numbing-cream-take-to-work`, `how-long-does-numbing-cream-last`, `does-numbing-cream-actually-work`. The task explicitly specified `/pages/how-it-works`, so Wave 1 uses the current handles; coordinate menu link + page handle together when the pages are built.

## Notes / minor flags
- **Footer policy links** render as 4 placeholders (Privacy/Terms/Refund/Shipping) until store policies are set in Stage F; social links are placeholders until URLs provided.
- **§4 terminal "Shop all" CTA** omitted (format-row section has no terminal-CTA setting); the format cards already route to the three collections. Add a CTA slot if desired.
- **Images:** all card/section image slots use neutral fallback (no external image source) per global rule; real shots swap in via the custom system later.

## Not done (by design — Wave 1 checkpoint)
- Product pages (Wave 2), collections build (Wave 3), guides/pages (Wave 4), repoint pass (Wave 5).

---
**Hero fix (follow-up, commit pending):** Homepage hero rebuilt to the spec's two-column layout — text-left / image-right on desktop, stacked with full-width CTAs on mobile — and the secondary CTA "Find your strength" changed from a black border to a brand-purple (`#6B3FA0`) outline + purple text per the Master Rebuild Brief no-neutral-CTA-borders rule; copy/hrefs unchanged; theme-check 0; re-rendered on the preview theme and confirmed.

---
**Polish pass (header + footer, follow-up):** Header — wordmark reduced (desktop 48→30px, mobile 34→28px) and the three top-right actions (search · account · cart) normalised to uniform 40×40 centred hit-areas with equal 19px icon height + even spacing (fixes the vertical stagger). Footer — SENSELESS wordmark reduced (64→40px); the "Stay in the loop" newsletter column removed entirely (markup, CSS, and schema settings) so the homepage "Stay close." is the single newsletter; footer rebalanced to a clean 3-column row (Shop / The system / Brand) with even 40px gutters. Policy + social stay placeholders (Stage F). Hero unchanged. theme-check 0; re-rendered on preview and confirmed.

---
**Procedures-hub links (follow-up):** Added a "See all procedures →" link to the bottom of the Shop ▸ By procedure mega column (purple + arrow + hairline foot treatment matching the mega CTA; added a "See all" child to senseless-main and a `ss-hdr__sublink--foot` style), and a single larger "See all procedures →" CTA below the four homepage procedure cards (new optional section-CTA on senseless-procedure-grid). Both point at the injectable-clean hub `/pages/aesthetic-procedures` (404s on dev until Wave 4) — never the SEO-only `aesthetic-numbing-cream` collection. theme-check 0; re-rendered and confirmed. (Note: the first combined push silently skipped templates/index.json; re-pushed explicitly and verified the deployed asset.)
