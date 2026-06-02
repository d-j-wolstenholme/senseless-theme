# Typography reweight (Strand 1) — heads 700→400 + italic-accent word-map

**Date:** 2026-06-02 (BST) · **Machine:** MacBook Pro (continued) · **Branch:** dev · **Commit:** `e7b2061`
**Theme:** Senseless Dev `#199324434780` · **Source:** Strand 1 design-system update (`36d58bc375ea8190b418f1fe7cd04ce2`) + italic word-map (`37358bc375ea81fbb88cefb276f24d19`)

## Token changes (global)
`snippets/senseless-typography.liquid` (rendered in `layout/theme.liquid` → site-wide):
- **`.ss-h1` / `h1.senseless`:** 700 → **400**; tracking -0.03em → **-0.02em**; line-height 1.04 → **1.06** (desktop) / **1.08** (≤749px).
- **`.ss-h2` / `h2.senseless`:** 700 → **400**; tracking -0.025em → **-0.02em**; line-height **1.1** / **1.12** (≤749px).
- **`.ss-h3` / eyebrow:** unchanged (**600**).
- **`.ss-accent` / `.t-em`:** italic **500**, `color: inherit` (was `.t-em` 600).

## Section-head reweight (scoped classes)
Every `senseless-*` section hardcodes its own head weight (the global tokens don't cascade to scoped classes), so all heads were reweighted: **26 single-line `__headline` heads + `ss-ph__title` (product H1)** via script, plus the **multi-line homepage hero** (`.ss-hero__headline`, the original "poster-like" 700) and the two `__heading` section heads (`callout-band`, `key-facts`) by hand → **400 + -0.02em**. **Card `__title`s, `__beat` subordinates, and eyebrows untouched (600/500).** Existing `em`/`i` accent rules (homepage hero, section-statement) → **500**.

## Italic-accent mechanism
- **New snippet `senseless-accent.liquid`** — wraps the FIRST occurrence of `word` in `<em class="ss-accent">` (italic 500, inherit colour); empty-safe (no word → plain escaped text); keeps the rest escaped (safe).
- **`accent_word` setting** added to 8 head sections (collection-hero, strength-ladder, collection-grid, format-row, link-row, editorial-band, callout-band, key-facts).
- **Word-map applied verbatim** to the 7 built pages. Italic lands on the positioning/decision word, never the keyword (`numbing [format]` stays roman + crawlable):

| Head | cream/gel/spray | micro | laser | spmu | waxing |
|---|---|---|---|---|---|
| Hero H1 | *matched* | *matched* | *matched* | *matched* | *matched* |
| Procedure-intro §3 | — | *more* | *area* | *sitting* | *sensitive* |
| Scale | *Match* | *Match* | *Match* | *Match* | *Match* |
| Grid | *strength* | *strength* | *strength* | *strength* | *strength* |
| Format-check | *right* | clean | clean | clean | clean |
| §5b suitability | clean | — | — | — | — |
| Philosophy | *average* | — | — | — | — |
| Honest bit | *skip* | *skip* | *skip* | *skip* | *skip* |
| Characteristics | *Senseless* | *Senseless* | *Senseless* | *Senseless* | *Senseless* |
| FAQ | clean | clean | clean | clean | clean |

## Verification (Playwright, preview theme)
- **Hero H1 computed weight = 400 on all 7 pages.**
- **Every italic accent renders at `500 / italic`**, exactly the mapped word, one per head (no doubles); clean heads carry no accent.
- **Cascade confirmed:** homepage hero ("Confidence starts with comfort.") = **400**; product-page hero title (`.ss-ph__title`) = **400**; sample section head (`.ss-db__headline`) = **400**.
- **Gel hero screenshot** captured (`/tmp/gel-hero.png`): "Numbing gel, *matched* to the appointment." — light H1, italic "matched" in ink (no purple), "Numbing gel" roman, eyebrow still 600 purple.
- theme-check **0**; Asset-API diff confirmed `.ss-h1`/`.ss-h2` = 400/-0.02em, `.ss-accent` = 500, accent snippet present, templates' `accent_word` + `use_metaobject` survived.

## Font preload (flag)
There is **no explicit `<link rel=preload>` font list** in the theme — Horizon loads fonts via `font_face` (display:swap), and `senseless-typography.liquid` self-hosts the 500 weight. So 400 (body) + 500 (medium) now cover the heads; **700 is retained** only for the header wordmark, footer column labels, and the pull-quote glyph (still referenced). No 700 "preload" exists to drop. If an explicit preload list is wanted for performance, that's a separate enhancement — flagged.

## Docs updated (same session, per Hard Rule #5/#9)
- `CLAUDE.md` Design Tokens (heading weights).
- `docs/BRAND.md` type section + scale table (H1/H2 → 400/-0.02em; italic accent 500; preload note).
- `DECISIONS-LOG.md` — dated entry (2026-06-02 14:10 BST).

## Flags / open items
- **Home / product / guide-stub italic words:** heads reweighted to 400, but those pages aren't in the word-map → **no italic word set** (the homepage hero keeps any existing `<em>` in its headline value). Per the map's rule, default to the positioning word — but I did **not guess**; flag for a home/product/guide word-map.
- Footer column label (`.ss-ft__colhead`) is a 0.75rem uppercase label still at 700 — left as-is (label, not a display head); flag if a reweight is wanted.

## HOLD
Reweight + italic accent complete and verified on the 7 built pages + cascade. Gel hero ready for sign-off. Nothing else started.
