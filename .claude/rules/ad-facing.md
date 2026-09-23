# Rule — Ad-facing surfaces & the injectable-clean invariant (Senseless)

**The three injectable collections are organic-only. No ad-facing surface may link to them.**
Enforced in practice since Phase 8; promoted to canon 2026-08-06 after a full live re-verification.

## Why

Botulinum toxin ("Botox") and dermal fillers are prescription-only / regulated interventions in the UK.
Advertising them to the public is restricted, and Google Ads applies its own healthcare and
"prescription drugs" policies to the **landing page and its destination experience**, not just the ad.
A paid landing page that routes into injectable-procedure content puts the ads account at risk and puts
Matrix Health Group Ltd on the wrong side of the medicines advertising rules.

Senseless sells a **cosmetic topical preparation** — never the procedure. Injectable-procedure content is
a legitimate **organic/SEO** cluster and stays indexable. It simply must not sit on a paid path.

## The three protected collections

- `/collections/numbing-cream-for-injections`
- `/collections/numbing-cream-for-lip-fillers`
- `/collections/numbing-cream-for-botox`

All three are **indexable on purpose** (they are SEO landing pages). Indexable ≠ ad-facing. Do not
"fix" their indexability.

## Ad-facing surfaces — zero inbound links to the three, ever

Header + footer menus (all) · homepage · every product page · every format collection
(cream/gel/spray) · every procedure collection · every strength collection (Clinical/Advanced/
Professional) · the procedures hub `/pages/aesthetic-procedures` · the Senseless Selector ·
and the three commercial landing pages `/pages/strongest-numbing-cream`,
`/pages/senseless-vs-ametop`, `/pages/best-emla-alternative-uk`
(Daniel confirmed these three ARE ad-facing — `build-reports/phase-8-cleanup-meta-and-stale-links.md:4`).

## Organic surfaces — MAY link the three

Blog articles under `/blogs/guides/*` and the guide pages under `/pages/*` that form the
does-it-hurt / procedure-explainer cluster. This is deliberate and documented:
`build-reports/sitewide-linking-audit.md:24` — *"Blogs link injectable collections — organic, allowed,
not flagged."*

## How to check it (run before any nav, collection, homepage or landing-page change)

Two passes — **both are required**. Any hit on a non-blog, non-guide surface is a breach.

1. **Anchors.** Fetch every URL in `sitemap.xml`, strip `<script>` blocks, and count `<a href>`
   anchors to the three handles.
2. **Structured data.** Fetch the same URLs and count the three handles inside
   `<script type="application/ld+json">` too — `BreadcrumbList` `item` URLs above all. Google
   follows these *and* renders them as the visible SERP breadcrumb, so they are ad-facing links in
   everything but syntax.

Pass 1 alone is not sufficient, and believing it was cost us a live breach. Verified clean
2026-08-06 by pass 1 only: **0 anchor breaches** — the only inbound links are the 5 guide articles,
the does-it-hurt guide cluster, and the three collections cross-linking each other (they are the
cluster, not an ad-facing surface). That anchor result still held on 2026-09-23, but pass 2 caught
`/products/foaming-cleanser` declaring `"name": "Numbing Cream for Botox"` as its breadcrumb parent,
because `snippets/senseless-breadcrumbs-jsonld.liquid` took `product.collections.first`. Fixed the
same day by filtering the three handles in that snippet; 12 products belong to an injectable
collection, so re-run pass 2 after any change to collection membership or ordering.

## Known two-hop path — accepted, but re-check it if the nav changes

`/pages/does-it-hurt-by-treatment` links all three. It is an organic guide page, is **not** in any
navigation menu, and is reached from the Articles hub and from the SPMU + waxing procedure collections.
The invariant is written in terms of **direct** links, so this is not a breach — but it is the shortest
path from a nav destination to injectable content. If that page is ever promoted into the primary nav
or used as a paid landing page, the classification changes and the links must come out.

## When adding a procedure card, related-row, or "see all"

Default to excluding injectables. `build-reports/header-hub-anchor-fixes-batch.md:12` records a
"See all" being deliberately dropped from the by-format column for exactly this reason. When in doubt,
leave the link out and ask.
