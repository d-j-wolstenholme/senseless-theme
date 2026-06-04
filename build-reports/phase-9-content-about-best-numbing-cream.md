# Phase 9 content — About + Best numbing cream

**Date:** 2026-06-04 (BST) · **Branch:** dev · **Theme:** Senseless Dev `#199324434780` (store `senseless-numbing`) · **Commit:** `e276d6c`
Token refreshed. Build sources (verbatim): About `36c58bc375ea81479b56fe51a36c5a78` (Production Copy, 7 sections); Best numbing cream `37558bc375ea81559515e104b4cd3fb0` (7 sections).

## Page 1 — About (`/pages/about`) — closes the last flagged 404
Resource created (published, suffix `about`), indexed. 7 sections, copy verbatim, built from existing modules:
- hero (`senseless-hero-brand-led`, about variant — CTAs left blank, no primary CTA) → §2–§5 `image-text-band` (alternating text-left/right) → §6 "What you'll notice" (`trio-card-row` + `format_card` with blank CTA = label+body principle cards) → §7 "Where to go next" cards → **Organization schema** (`senseless-org-schema`: legalName "Matrix Health Group Ltd", name "Senseless", GB) + WebPage (`senseless-page-schema`) + BreadcrumbList.
- **Stale cross-links repointed** (the one correction): §7 "How Senseless works" + "Choose your strength" → **`/pages/the-senseless-system`** (were retired how-it-works / choosing-your-strength 301s). `/pages/trade` (§5 CTA) + `/collections/aesthetic-numbing-cream` (§7) kept.
- **Clinic line kept verbatim** ("Stocked in clinics across the UK." — Daniel confirmed, not softened). Parent disclosure (Matrix Health Group Ltd, §3) kept as drafted.
- Meta: title "About Senseless — UK Aesthetic Numbing, Built for the Chair" (59); description trimmed to 155 (avoids the banned "made in the UK" phrasing).

## Page 2 — Best numbing cream (`/pages/best-numbing-cream`) — SEO
Resource created (published, suffix `best-numbing-cream`), **indexed**. 7 sections, copy verbatim, existing modules: guide-hero → §2 "honest answer" editorial band → §3 framework (trio cards: treatment / area / you) → §4 Senseless approach (System + cream + Selector links) → §5 Key Facts → §6 FAQ (FAQPage) → §7 next cards → WebPage + BreadcrumbList + FAQPage.
- **Angle:** "no single best — best = matched to treatment/area/sensitivity" (System logic). **"Strongest" appears only as reframe-away** ("rather than just choose the strongest", "not the strongest thing you can find", "Is the strongest…? Not necessarily") — never positions any product as strongest; Professional never flagship/strongest.
- **Ad-facing → injectable-clean** (zero inbound links to the 3 injectable collections) + **System-guide links direct 200** (no 301 hops): `/pages/the-senseless-system`, `/collections/numbing-cream`, Selector `…#selector`.
- Meta: title "Best Numbing Cream — How to Choose the Right One | Senseless" (60); description 143.

## Compliance
Both: reduce-not-eliminate; no efficacy/onset/duration/% claims; "formulated in the United Kingdom"; cosmetic not medicine; practitioner-routed; 0 banned words; FAQ leads compliant standalone; Professional never flagship/strongest. (Grep clean.)

## Verify
- **theme-check: 0 errors.**
- **Render-verify (Playwright, desktop + mobile):**
  - About 200; H1 "A UK brand built for one thing."; schema **Organization + WebPage + BreadcrumbList** (Organization legalName "Matrix Health Group Ltd"); **clinic line present**; **0 body stale links**; indexed.
  - Best numbing cream 200; H1 "Best numbing cream"; **WebPage + BreadcrumbList + FAQPage**; indexed; **injectable-clean (0 inbound)**; **no tattoo refs**; System + cream links resolve **200 direct**.
- **Grep:** About has no `how-it-works`/`choosing-your-strength`; best-numbing has no injectable-collection links; no banned/`made in the UK` terms.

## Deviations / flags
- **best-numbing §2 "tattoos" removed:** the verbatim §2 said "forum opinions built for tattoos"; the brief's hard "no tattoo refs" gate overrides → reworded to "forum opinions built for other contexts." Minimal deviation; flagged.
- **About "four formats" kept verbatim** (hero + §2 say "four formats"; elsewhere the brand uses "three formats: cream/gel/spray" — the spec counts the cleanser as a 4th). Kept per "verbatim"; flag if you want it aligned to "three formats".
- Meta descriptions trimmed to ≤155 (spec values were 171/156).
- About sign-off blockers remain external: Director/MHG parent-disclosure sign-off, ops confirmation of the clinic-stocking claim, photography.
- **About closes the last flagged 404** — the Trade page's `/pages/about` card (flagged in Track 1) now resolves.

## Files / API
- Edited: `templates/page.about.json` (rebuilt verbatim + stale-link repoint + org/WebPage schema), `templates/page.best-numbing-cream.json` (rebuilt per new SEO spec).
- API: `pageCreate` ×2 (about, best-numbing-cream), `metafieldsSet` (meta titles/descriptions, trimmed).

## HOLD
Phase 9 content complete + verified. About closes the last flagged 404; best-numbing-cream live + indexed + injectable-clean.
