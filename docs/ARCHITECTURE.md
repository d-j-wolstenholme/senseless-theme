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
| Products | 10 | One per SKU (S30CL, S30AD, S30PR, S10CL, S10AD, SG35CL, SG35AD, SG35PR, SSPAD, SSPPR) |
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

### Footer — `senseless-footer-shop` / `-explore` / `-company`
- **Shop**: Cream / Gel / Spray / The full range
- **The system**: How it works / Choosing your strength / Choosing your format / How to apply / FAQs
- **Company**: About / Contact / Trade enquiries
- **Legal band** (footer-utilities): copyright + Matrix Health Group Ltd parent-company attribution (→ matrixhealthgroup.co.uk) + policy links + social links

## Migration / Launch

At launch, 301 redirects from old URLs to new URLs are set up via the `redirects` skill. The old Senseless site will have all tattoo-focused URLs redirected to nearest aesthetics equivalents.
