# Shipping reconciliation + cart feedback + homepage SEO/title (3 briefs)

**Date:** 2026-06-06 (BST) · **Branch:** dev · **Theme:** Senseless Dev `#199324434780` (UNPUBLISHED). Pre-launch store (no live customers) — checkout-config changes safe. theme-check **0 errors**. Commit `3ab240f`.

---

## BRIEF 1 — Shipping reconciliation to locked canon (Admin API)

**Canon:** free UK standard over £40 · free UK next-day over £80 · paid rates kept but never in copy · same-day dispatch before 1pm · UK only.

### Shipping rates / rules / zones — exactly what changed
| Action | Before | After |
|---|---|---|
| **EU zone** (AT/BE/DE/FR/…) | Standard international £14.99 | **DELETED** |
| **International zone** | Standard international £23.99 | **DELETED** |
| **UK "Express"** | Express £6.99 | **Renamed → "Next-day delivery" £6.99** |
| **UK Standard** | £4.99 + free-over-**£50** price-tier | **Rebuilt flat £4.99** (stale £50 tier removed) |
| **Free-shipping discount A** (new, automatic) | — | **"Free UK standard delivery over £40"** — min subtotal £40, max shipping price £5.00 (so only Standard £4.99 qualifies) · ACTIVE |
| **Free-shipping discount B** (new, automatic) | — | **"Free UK next-day delivery over £80"** — min subtotal £80, max shipping price £7.00 (covers both rates) · ACTIVE |

**Net checkout behaviour (matches canon):** under £40 → Standard £4.99 / Next-day £6.99 (both paid); £40–£80 → **Standard FREE**, Next-day £6.99; £80+ → **both FREE**. UK only.

> *Why discounts not rate-level tiers:* the existing free-over-£50 was a Shopify "price-based rate" with a synthetic condition id that `conditionsToDelete` wouldn't cleanly remove; per the brief I used the automatic free-shipping discount mechanism (the TN approach) and rebuilt Standard as a clean flat rate. The paid £4.99/£6.99 rates remain (per canon) but are never referenced in copy.

### Copy aligned to canon
- **Native Shopify Shipping policy** — rewrote: removed the paid "Delivery options" list (£1.99/£2.99/£7.99); now states free standard over £40, free next-day over £80, order before 1pm for same-day dispatch (after 1pm/weekends/bank holidays → next working day), UK delivery, tracking. **No paid-price references.**
- **/pages/shipping-delivery** (metafield-driven) — rewrote 3 metafields: `prose_policy_body` (dropped the £1.99/£2.99/£7.99 "Express" options list → Standard free-over-£40 + Next-day free-over-£80 only), `faq` ("Is delivery free?" answer stripped of paid prices), `description_tag` (was "Standard delivery from £1.99" → canon, no price). *Verified live: free£40 ✓ free£80 ✓ paidPrices=false ✓ "Express" tier gone ✓.*
- **Header progress banner** — already canon (£40 → free standard, £80 → free next-day, order before 1pm); confirmed, no drift.

---

## BRIEF 2 — Cart feedback = header count badge only (no drawer on add)

- **`auto_open_cart_drawer` → false** (was enabled in the Phase 13 pass). The drawer's open-on-add is gated on that setting's `auto-open` attribute, so turning it off drops the open-on-add path entirely. No race-fix pursued (not wanted). The cart drawer remains reachable via the **header cart icon** (normal click) — untouched.
- **Verified — badge updates immediately via cart AJAX, no drawer, no reload, on all FOUR paths:**
  | Path | Count | Drawer opens | Redirect |
  |---|---|---|---|
  | PDP add (desktop) | 0 → 1 | **no** | **no** (stay on page) |
  | Quick-add card (desktop) | 1 → 2 | **no** | **no** |
  | PDP add (mobile) | 2 → 3 | **no** | **no** |
  | Quick-add card (mobile) | 3 → 4 | **no** | **no** |
- No leftover add-to-cart redirect — the page is retained; the header count badge is the sole feedback.

---

## BRIEF 3 — Homepage SEO + global title suffix (theme-side)

Reworked `snippets/meta-tags.liquid` to be **brand-independent** (survives the shop rename):
- **Homepage** (`request.page_type == 'index'`) now emits a bespoke `<title>` **"Senseless — UK Numbing Cream, Gel & Spray for Aesthetics"** + bespoke meta description ("UK-formulated topical numbing creams, gels and sprays… microneedling, laser, SPMU and waxing. Developed with practitioners.") — independent of Online Store Preferences / `shop.name`. *Verified.*
- **Global suffix** — the title now appends **"Senseless"** (a `brand_name` literal) instead of `shop.name`, with `unless page_title contains brand_name` so titles that already include "Senseless" don't double up. `og:site_name` + og fallbacks also use the brand. *Verified across templates:*
  - home → `Senseless — UK Numbing Cream, Gel & Spray for Aesthetics`
  - product → `Clinical Numbing Cream | UK-Formulated | Senseless`
  - collection → `Numbing Cream | Three Strengths, UK-Formulated | Senseless`
  - page → `About Senseless — UK Aesthetic Numbing, Built for the Chair`
  - article → `Does Botox Hurt? What to Expect & How to Prepare – Senseless`
  - **No "– senseless-numbing" anywhere.** Correct now and after the shop rename.

---

## Notes / flags
- **Deploy caution:** the comma-separated `shopify theme push --only "a,b"` silently skipped a file again — pushed each file with a single `--only` to deploy reliably (verified by render).
- Compliance: homepage title/meta are clean (UK-formulated, cosmetic framing, no pain/% /onset claims, no banned words) and consistent with the locked homepage positioning.

## HOLD
All three reconciliations live + verified on the dev theme. theme-check 0; unpublished.
