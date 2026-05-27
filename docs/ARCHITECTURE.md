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
| Procedure Collections | 8 | Aesthetic Hub, Lip Fillers, Injections, Botox, Microneedling, SPMU, Laser, Waxing |
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

### Header (Megamenu)
- Shop → Numbing Cream / Numbing Gel / Numbing Spray / All Products
- By Procedure → Lip Fillers / Botox / Microneedling / SPMU / Laser / Waxing
- Guides → Blog index
- About
- Contact / Trade

### Footer
- Shop links
- Procedure links
- Legal pages
- Contact details
- Social links

## Migration / Launch

At launch, 301 redirects from old URLs to new URLs are set up via the `redirects` skill. The old Senseless site will have all tattoo-focused URLs redirected to nearest aesthetics equivalents.
