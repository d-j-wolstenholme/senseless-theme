# Site Architecture

Mirrors the Site Architecture Notion page. See full details there.

## URL Structure

- Collections: `/collections/[handle]`
- Products: `/products/[handle]`
- Blog: `/blogs/guides/[handle]`
- Pages: `/pages/[handle]`
- Policies: `/policies/[handle]`

## Page Clusters

| Cluster | Count | Notes |
|---|---|---|
| Homepage | 1 | Brand-led, funnels to format + procedure collections |
| Format Collections | 3 | Numbing Cream, Numbing Gel, Numbing Spray |
| Procedure Collections | 8 | Aesthetic Hub + Microneedling, SPMU, Laser, Waxing surfaced in nav (**injectable-clean**). Lip Fillers, Botox, Injections collection templates exist but are **not linked from navigation** (injectable-clean decision; under review for noindex/redirect) |
| Products | 10 (+5 bundles) | 3 Cream / 3 Gel / 3 Spray / 1 Cleanser, sold as size variants → **15 single SKUs**: S10CL S30CL · S10AD S30AD · S30PR · SG15CL SG35CL · SG15AD SG35AD · SG15PR SG35PR · SSPCL SSPAD SSPPR · FOAM. Gel ships in **both 15ml and 35ml** across all three tiers; a **Clinical Spray (SSPCL)** now exists. Plus 5 bundles: SBUN-CL-S/-L, SBUN-AD-S/-L, SBUN-PR-L. |
| Commercial Landing | 3 | Strongest Numbing Cream, Best Numbing Cream, Best Emla Alternative |
| Blog Articles | 15+ | Procedure pain, aftercare, product education, retailer comparisons |
| Supporting | 4 | About, FAQ, Trade, Contact |
| Legal | 4 | Privacy, Terms, Refund, Shipping (NOINDEX) |

Full page list in Notion Master Page Database.

## Internal Linking Rules

- Every procedure collection links to the matching "does [procedure] hurt" blog post
- Every blog post links back to the relevant collection
- Product pages link to format collection and relevant procedure collections
- Comparison collections (strongest/best) link to all tier products
- Homepage links to top procedure collections and featured products
- No dead-end pages — every page has a clear next step

## Navigation

Re-synced 2026-05-31 to the **live store menus** (source of truth: Shopify admin nav). The model is a **hub** (Shop → By format / By procedure → hub pages), and it is **injectable-clean** — Botox / Lip Fillers / Injections are NOT surfaced anywhere in nav.

### Header megamenu — `senseless-main`
- **Shop** (→ `/collections/aesthetic-numbing-cream`)
  - By format → Cream / Gel / Spray
  - By procedure → Microneedling / Laser / Semi-permanent makeup / Waxing / See all procedures (`/pages/aesthetic-procedures`)
- **The system** (→ `/pages/how-it-works`) → Choosing your strength / Choosing your format / How it works / How to apply
- **About** (→ `/pages/about-us`)
- **Help** (→ `/pages/faq`) → FAQ / Contact / How long to work / How long to last / Does numbing cream actually work

> No "By strength" axis in nav (strength is taught under *The system → Choosing your strength*). `/pages/aesthetic-procedures` and `/pages/about-us` must exist in admin (verify template assignment). Stale Horizon `main-menu` exists but is unused.

### Footer — bespoke `senseless-footer.liquid` section (columns `senseless-footer-shop` / `-explore` / `-company`)
Bespoke `senseless-footer` section (replaces Horizon native `footer` + `footer-utilities`). Dense, large inlined wordmark; four columns over an in-section legal band:
- **Shop** (menu `senseless-footer-shop`): Cream / Gel / Spray / The full range
- **The system** (menu `senseless-footer-explore`): How it works / Choosing your strength / Choosing your format / How to apply / FAQs
- **Brand** (menu `senseless-footer-company`): About / Contact / Trade enquiries
- **Newsletter**: heading + blurb + native `{% form 'customer' %}` signup
- **Legal band** (in-section, not `footer-utilities`): copyright + Matrix Health Group Ltd parent-company attribution (→ matrixhealthgroup.co.uk) + `shop.policies` links + social links

> Until the three footer menus and store policies are created in admin (Stage D), the section renders an **injectable-clean** placeholder set per column (flagged in-code). Stage D must keep wired footer menus injectable-clean (no Botox/filler/injection links).

## Migration / Launch

At launch, 301 redirects from old URLs to new URLs are set up via the `redirects` skill. The old Senseless site will have all tattoo-focused URLs redirected to nearest aesthetics equivalents.

## Section build standards (CSS positioning + scoping)

Locked 2026-06-03 after a class-collision bug: `senseless-comfort-compare` used the `.ss-cc` prefix, which is owned by `senseless-cookie-consent` (`position:fixed; bottom:0; z-index:1000`). The cookie banner's positioning leaked onto the comfort section and pinned it to the viewport bottom, overlaying page content. Fixed by renaming the section's prefix to a unique `.ss-cmp`.

Standard for every `senseless-*` section/snippet:

- **Inline by default.** Sections render in normal document flow. `position: fixed` / `position: sticky` is opt-in only and never a default. The only deliberate exceptions today: `senseless-header` (sticky header + fixed mobile drawer/scrim) and `senseless-cookie-consent` (fixed bottom banner). Any new fixed/sticky use must be intentional and noted.
- **No stray `z-index`.** Don't add `z-index` unless the section genuinely stacks; the fixed exceptions above own the high z-indexes.
- **Scope CSS to a unique block.** Each section's `{% style %}` must use a prefix unique to that section (e.g. `.ss-cmp` for comfort-compare, `.ss-sel` for the selector, `.ss-cb` for the callout band) — or scope to `#shopify-section-{{ section.id }}`. Never reuse another section's prefix. `.ss-cc` is reserved for `senseless-cookie-consent`.
- **New sections** copy a corrected wrapper skeleton (inline flow, unique prefix, no z-index) so this class of leak cannot recur.

### Menu-surface standard (desktop dropdowns + mobile drawer)

Locked 2026-06-03 after the mobile drawer rendered transparent and showed the raw `shop.name`. Rules for every menu surface:

- **All menu surfaces are opaque.** Desktop dropdown panels (`.ss-hdr__panel` → solid `#ffffff`) AND the mobile drawer (`.ss-hdr__drawer` → solid `#f7f7f5`) and any submenu/accordion expansions must have a solid background over their full area, with adequate z-index above all page content (dropdowns 99, scrim 110, drawer 120).
- **The custom header renders at every breakpoint.** `senseless-header` is the only header section (no Horizon `header` fallback in the group). The brand logo is the inline `senseless-logo-header.svg` at all breakpoints — **never render raw `shop.name` as a visible wordmark** (it shows the store handle "senseless-numbing"). `shop.name` may appear only in non-visual `alt`/`aria-label`.
- **Sibling elements can't inherit header vars.** The drawer + scrim are rendered as siblings *outside* `.ss-hdr` (because `.ss-hdr`'s `backdrop-filter` would make their `position:fixed` resolve against the header box, not the viewport). Because they're not descendants, they do **not** inherit the `--ss-*` brand vars defined on `.ss-hdr` — so `var(--ss-bg)` etc. resolve to nothing (transparent). Any such sibling surface must **define the brand vars on itself** (or hardcode the values). Don't assume inheritance across the `.ss-hdr` boundary.
