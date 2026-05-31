# Build Report — Phase 0: Foundations (verify + reconcile)

- **Machine:** MacBook Pro
- **Date:** 2026-05-31 (BST)
- **Branch:** `build/phase-0-foundations` (off `dev`)
- **Mode:** Reconcile + verify only — **no code teardown, no superseded decision.** (Owner-selected.)
- **Session duration:** ~0.5h

---

## TL;DR

The Phase-0 brief described a clean-slate foundation build (self-host Montserrat `.woff2`,
create `assets/senseless-tokens.css`, introduce a 1.25 major-third scale). **The repo is
already past this.** Phases 0–3 are committed (`0b41e23`→`5df2e71`) and the design-token +
Montserrat foundation already exists via a *locked* decision
(`DECISIONS-LOG.md` 2026-05-29 14:00 BST), using a **different, deliberately-chosen mechanism**:
Montserrat self-hosted through **Shopify's font CDN** (Horizon native font picker) rather than
manual `@font-face`, with tokens in `snippets/senseless-typography.liquid` rather than a separate
CSS file.

Executing the brief literally would have superseded a locked decision, risked double-loading
Montserrat, and re-flowed every heading on the already-built site. Owner chose **option 1 —
treat Phase 0 as satisfied, keep existing names/scale canonical, verify, and document reality
so the planning docs can sync.** That is what this report does.

---

## Environment state

| Check | Result |
|---|---|
| Repo path | `/Users/matrix/code/senseless-theme` ✅ |
| Shopify CLI | v3.94.3 ✅ |
| Auth store | `senseless-tattooing.myshopify.com` ✅ |
| Dev theme | "Senseless Dev" `#196680057167` — **unpublished** ✅ |
| Live theme (untouched) | "Horizon" `#195280437583` `[live]` — not touched, not published |
| Branch | `build/phase-0-foundations` created off `dev` |
| Working tree at start | dirty (`M sections/senseless-header.liquid`, `?? assets/senseless-logo-header.svg`) — **unrelated to Phase 0; left uncommitted, not pulled over** |
| Theme pull | Did **not** sync-pull (uncommitted changes present; foundation already committed). Instead pulled foundation files to a temp dir for read-only diff (below). |

---

## Verification results (grounded against the live dev theme `#196680057167`)

The three foundation Liquid files were pulled from the dev theme and diffed against local —
**byte-identical** — so what is verified below is exactly what renders on Senseless Dev:

- `snippets/senseless-typography.liquid` — identical ✅
- `snippets/fonts.liquid` — identical ✅
- `snippets/theme-styles-variables.liquid` — identical ✅
- `config/settings_data.json` — differs only in non-font / non-scheme settings (theme-editor write-back). Font settings (`montserrat_n4/n6/n7`) and all 7 color-scheme backgrounds are **identical** to local.

| Brief criterion | Result | Detail |
|---|---|---|
| No `googleapis` / `gstatic` anywhere | ✅ PASS | `0` matches across all source globs. Already stripped in `0b41e23`. |
| Montserrat self-hosted (no Google requests) | ✅ PASS | Served from `fonts.shopifycdn.com` via Shopify font picker. |
| `@font-face` present for the loaded weights | ✅ PASS | Emitted by Horizon `snippets/theme-styles-variables.liquid` via `… | font_face: font_display: 'swap'` for all 4 font roles + bold/italic variants. **`font-display: swap` satisfied.** |
| Body renders Montserrat | ✅ PASS | `body { font-family: var(--font-sans) }` in `senseless-typography.liquid`, loaded after Horizon CSS. |
| Headings render Montserrat | ✅ PASS | `h1–h6 { font-family: var(--font-sans) }` + `.ss-h*` classes. |
| Body text `#2B2730` | ✅ PASS | `body { color: var(--text-body) }`, `--text-body: #2B2730`. |
| A primary element uses `#6B3FA0` | ✅ PASS | `--brand-primary: #6B3FA0`; brand purple literal/used in **26** section/snippet files (eyebrows, Professional-tier border + filled CTA). |
| Page background `#f7f7f5` | ⚠️ **FAIL** | `--bg-canvas: #f7f7f5` is **defined but never consumed** — no `body { background }` rule, no section reference, and **none of Horizon's 7 color schemes use `#f7f7f5`** (they are `#ffffff`, `#f5f5f5`, `#eef1ea`, `#e1edf5`, `#333333`, transparent ×2). Actual rendered canvas = Horizon `scheme-1` `#ffffff`. The brand "warm off-white" background described in `BRAND.md` is **not rendering.** See Open Questions. |

---

## Token inventory (canonical — `snippets/senseless-typography.liquid` `:root`)

Tokens are defined globally and referenced by the global typography classes in the same snippet.
Sections mirror the **values** into scoped `--ss-*` tokens / literal hexes rather than reading the
globals directly — so `var(--token)` consumption counts below reflect the global-class layer only.

| Token | Value | Role | `var()` consumed |
|---|---|---|---|
| `--text-primary` | `#1A1816` | Headings / display | yes |
| `--text-body` | `#2B2730` | Running body | yes |
| `--text-secondary` | `#5C5853` | Lead / captions | yes |
| `--text-muted` | `#8E8A82` | Disabled / tertiary | **0 — defined, unused** |
| `--brand-primary` | `#6B3FA0` | Accent (eyebrow, Professional tier) | yes (+26 files use the literal) |
| `--bg-canvas` | `#f7f7f5` | Intended page background | **0 — defined, unapplied** |
| `--bg-surface` | `#ffffff` | Card / panel surface | **0 — defined, unused as var** |
| `--font-sans` | `'Montserrat', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif` | Sole typeface | yes |

**Note:** the brief's proposed names (`--senseless-purple`, `--senseless-bg`, `--font-body`)
are **not** present and **no aliases were added** (owner instruction) — nothing in the repo
references them, so they are not needed.

---

## Type scale (canonical — fluid `clamp()`, not the brief's 1.25 scale)

The locked scale was kept. The brief's 1.25 major-third scale (`--fs-*`) was **not** introduced
(it differs numerically — e.g. brief H1 max `3.052rem` vs canonical `4rem` — and would re-flow
every heading on the built site).

| Element | Size | Line-height | Weight | Letter-spacing |
|---|---|---|---|---|
| `.ss-h1` / `h1.senseless` | `clamp(2.5rem, 1.5rem + 4vw, 4rem)` | 1.04 | 700 | -0.03em |
| `.ss-h2` / `h2.senseless` | `clamp(1.875rem, 1.2rem + 3vw, 2.75rem)` | 1.1 | 700 | -0.025em |
| `.ss-h3` / `h3.senseless` | `clamp(1.25rem, 1.18rem + 0.3vw, 1.375rem)` | 1.25 | 600 | -0.01em |
| `.lead` | `clamp(1.125rem, 0.95rem + 0.8vw, 1.375rem)` | 1.55 | 400 | — |
| body | `clamp(1rem, 0.98rem + 0.13vw, 1.0625rem)` | 1.7 | 400 | -0.003em |
| `.body-small` | `0.875rem` | 1.6 | 400 | — |
| `.caption` | `0.8125rem` | 1.45 | 400 | — |
| `.eyebrow` | `0.75rem` | 1.2 | 600 | 0.2em, uppercase, brand-primary |
| `.t-em` | (inherits) | — | 600 italic | — |

---

## Fonts actually loaded

- **Source:** Shopify font library (`fonts.shopifycdn.com`) via Horizon font picker. **Not** Google Fonts. **Not** hand-hosted `.woff2` in `assets/` (none present, by design).
- **Subset:** latin (Shopify-managed; no latin-ext requested).
- **`font-display`:** `swap` (all roles).
- **Weights wired** (`config/settings_data.json`): body `montserrat_n4` (400), subheading `montserrat_n6` (600), heading `montserrat_n7` (700), accent `montserrat_n6` (600). Horizon also auto-emits each role's bold/italic/bold-italic `@font-face`.
- **Preloaded** (`snippets/fonts.liquid`): weight **400** (body) + **700** (heading) only.
- **Weight 500 (`montserrat_n5`):** **not loaded** — not referenced by the locked type scale; the brief's 400/500/600/700 request is satisfied as 400/600/700 (500 unused).

---

## Horizon variable names (for `BRAND.md` / planning-doc sync)

The Senseless token layer is **parallel** to Horizon's native system, not mapped onto it:

- **Fonts** — Horizon exposes `--font-body--family`, `--font-body--weight`, `--font-heading--family`, `--font-heading--weight` (and subheading/accent) in `snippets/theme-styles-variables.liquid`, sourced from `settings.type_body_font` / `type_heading_font` (= Montserrat). Senseless additionally declares `--font-sans` and applies it directly on `body` + `h1–h6`. Both resolve to Montserrat.
- **Colour** — Horizon has **no global `:root` brand hexes**; colour is driven by **per-section color schemes** (`scheme-1`…`scheme-6` + custom) with keys `background` / `foreground` / `primary` / `primary_button_background` etc. The Senseless brand hexes (`#6B3FA0`, `#f7f7f5`) are **not wired into these schemes** — which is exactly why `--bg-canvas` does not render as the page background.

---

## grep results

```
grep -rI "googleapis\|gstatic" (all source globs)  →  0 matches
```

---

## Files added / changed this session

- **Added:** `build-reports/phase-0-foundations.md` (this file).
- **No code changes** — reconcile-only. `senseless-typography.liquid`, `fonts.liquid`, `settings_data.json` left as-is (already correct + in sync with the dev theme).
- The pre-existing uncommitted `sections/senseless-header.liquid` / `assets/senseless-logo-header.svg` are **unrelated** and were deliberately **not** committed on this branch.

---

## Open questions / discrepancies to resolve

1. **`--bg-canvas: #f7f7f5` is defined but not applied.** `BRAND.md` calls it the "warm off-white page background," but the rendered canvas is white (`scheme-1 #ffffff`). Decide one of:
   - (a) wire `#f7f7f5` into the default color scheme background(s) so the brand canvas actually renders, **or**
   - (b) downgrade the `BRAND.md` wording to "defined token, not currently applied as page background."
   *(Not actioned this session — changing color schemes is a design change affecting the whole built site and needs sign-off.)*
2. **`--bg-surface` and `--text-muted` are defined but unconsumed** (as `var()`). Confirm whether they are reserved-for-later or should be removed/wired.
3. **Branch naming:** brief specified `build/phase-0-foundations`; `CLAUDE.md` convention is `feature/<desc>` / `fix/<desc>`. Used `build/` as the brief asked — confirm whether `build/*` should be added to the naming convention.

---

## Deferred / not done (by design)

- Self-hosting Montserrat `.woff2` in `assets/` — **not done.** Google-Fonts-removal goal already met via Shopify CDN; hand-hosting would supersede a locked decision and risk double-loading. Revisit only if true Shopify-font-library independence is required.
- `assets/senseless-tokens.css` — **not created.** Tokens already live in `senseless-typography.liquid`.
- 1.25 major-third `--fs-*` scale — **not introduced** (conflicts with locked scale).

---

## To push to Notion (Decisions Log mirror)

> **2026-05-31 (MacBook Pro — Phase-0 verification).** Confirmed the design-token + Montserrat
> foundation is complete and live on Senseless Dev `#196680057167`, matching the locked 2026-05-29
> decision (Montserrat via Shopify font CDN + `senseless-typography.liquid` tokens; 0 Google-Font
> requests; `font-display: swap`; preload 400/700). **No teardown** — a clean-slate Phase-0 rebuild
> brief was reconciled against existing locked state per owner choice. **One open discrepancy:**
> `--bg-canvas #f7f7f5` is defined but not applied — page background renders white (`scheme-1`);
> `BRAND.md` describes it as the page background. Needs an owner decision (wire into color schemes
> vs. amend doc).

## Sync status

- Code ↔ dev theme: **PASS** (foundation files byte-identical).
- Code ↔ `BRAND.md`: **WARN** — `BRAND.md` asserts `#f7f7f5` "page background"; not actually applied (see Open Q1).

## Next steps

1. Owner decision on Open Q1 (`--bg-canvas` wiring vs. doc amendment).
2. If keeping reconcile-only: open PR `build/phase-0-foundations` → `dev` (report-only) and continue feature work.
