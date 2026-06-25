# Senseless — Launch-Readiness Verification (READ-ONLY)
**Date:** 2026-06-24 · **Mode:** strictly read-only (only write = this file) · **Store:** senseless-numbing.myshopify.com · **Live theme:** `199324434780` (the single [live] theme; legacy name "Senseless Dev")
Legend: ✅ verified done · ❌ verified gap · ⚠️ admin-only · 🔒 not-API-checkable · 🟡 flag-for-decision

## 0. Store identity + environment guard — PASS
| Item | Checked | Finding | Verdict |
|---|---|---|---|
| Admin token store | `{shop{myshopifyDomain}}` | Senseless / senseless-numbing.myshopify.com | ✅ |
| CLI store | `theme list --store senseless-numbing` | authed Senseless | ✅ |
| Live theme | exactly one [live] | `199324434780` "Senseless Dev" (legacy name only) | ✅ |
| Dev/preview themes | full theme list | **none** (only the live theme) | ✅ |
| Git branch | current = main | `main` current | ✅ |
| Leftover branches | branch -a | `dev` (local + `origin/dev`), `build/phase-0-foundations`, `feature/docs-architecture-compliance`, `feature/geo-schema-keyfacts`, `feature/quickadd-cards` (local + remote) | 🟡 model says "all dev branches deleted" — these remain |
| Live pull | /tmp/sl-live | 554 files; layout/templates(68)/sections(86)/snippets(117) present | ✅ |

## 1. Commerce (Admin API)
| Item | Finding | Verdict |
|---|---|---|
| £0.00 variants | none | ✅ |
| Non-ACTIVE products | none (all 16 ACTIVE) | ✅ |
| Tracked inventory ≤ 0 | none | ✅ |
| `senseless.tier`/`senseless.format` | 9 strength singles ✅, 5 bundles ✅; **foaming-cleanser tier=∅** (no strength tier — expected), format ✅; vitamin-a-d-ointment-4-pack tier/format=∅ (extra aftercare product, outside canon set) | ✅ / note |
| productType=Bundle | all 5 kits = Bundle | ✅ |
| Placeholder gate | `image_placeholder=true`: none · alt `[PLACEHOLDER]`: none | ✅ |
| Redirects (9 total) | 5× `/policies/*→/pages/*` ✅; `/pages/how-to-apply→/pages/the-senseless-system`, `/llms.txt→/pages/llms-txt`, `/collections/frontpage→/`, `/blogs/news→/blogs/guides` | ✅ |
| 4× `/pages/*` (choosing-strength, choosing-format, how-it-works, how-to-apply-numbing-cream) | no redirect needed — all resolve **200** | ✅ |
| Default Home/frontpage collection | none (16 collections, no frontpage) | ✅ |
| webPixel (GA4/Ads) | ACCESS_DENIED (`read_pixels` scope) | ⚠️ verify Settings → Customer events |
| shop.brand logo/cover | not API-exposed | ⚠️ verify Settings → Brand |

## 2. Theme greps (/tmp/sl-live)
| Item | Finding | Verdict |
|---|---|---|
| PAIN claims | 0 | ✅ |
| TIER ("clinical-grade","good-better-best") | 0 | ✅ |
| `flagship` | 45× — **all `"flagship": false`** (inert) | ✅ |
| "strongest" | only SEO-keyword (`/pages/strongest-numbing-cream`, `rel_strongest` nav link) + anti-maxing body ("not by whatever's labelled 'strongest'") — no tier claim | ✅ |
| AI-slop | 0 | ✅ |
| MANUFACTURE ("made in"/"manufactured in") | 0 | ✅ |
| Origin wording | `page.about.json:239` "Formulated and **produced in** the United Kingdom" (not in the literal ❌ list, but origin-adjacent) | 🟡 |
| Ingredients/efficacy | named actives 0 · hour-duration/onset 0 · "%" copy 0 | ✅ |
| "cruelty-free" | 0 | ✅ |
| Em-dash "—" | **909** total (templates/sections/snippets); top: collection.numbing-spray 29, the-senseless-system 22, collection.numbing-cream 22, numbing-cream-for-waxing 22 | report (rewrite pending) |
| 🟡 flag words | "everyday" ×8 (choosing-your-strength :29/:338, the-senseless-system :100, strongest :198…), "upgrade" ×3 (choosing-your-strength :41, strongest :208…), "concentrated" ×1 + "most concentrated" ×1 (`page.strongest-numbing-cream.json:16` H1 "Our most concentrated formula") | 🟡 for-decision |
| **Required safety warning per 10 product templates** | "broken/inflamed/sunburnt" warning **ABSENT on all 10**; "patch test" on the 9 strength SKUs only; foaming-cleanser has **none** | ❌ (caveat: cosmetic warnings are legally on-pack; web display is a judgement) |
| cream/gel "unbroken"/"clean, healthy" | present (how-to-apply :88, faq :61/:82, injectable collection FAQs) | ✅ |
| Spray "broken" | **0** across spray collection + spray products | ✅ (carve-out holds) |
| FOAM antibacterial claim | "Antibacterial…" ×4 (`product.foaming-cleanser.json` :16/:75/:102/:201) | 🟡 substantiation review |
| Trust bar | live = ★ **4.9 / 5** (+"230+ reviews") · UK Formulated · CPSR Assessed · Trusted by UK Practitioners · Free delivery over £40; **cruelty-free 0** ✅. Canon's 4 locked signals (UK formulated · Cosmetic product · CPSR assessed · Made for aesthetics) — only 2 present | 🟡 state mismatch (rating-led redesign shipped 2026-06-24; "Cosmetic product"/"Made for aesthetics" still appear elsewhere on home: eyebrow + callout) |
| Naming | "The Senseless Scale" on home ✅; "The Senseless System" in snippets/schema (×3) + `/pages/llms-txt` (×3) but **not literal in index.json** (home=0 — rendered via nav/sections) | ✅ / note |
| Injectable-clean (nav) | **no** injectable-collection hrefs in ad-facing templates | ✅ |
| robots AI crawlers | GPTBot/ClaudeBot/Google-Extended = standard path-disallows only; the sole `Disallow: /` is **User-agent: Nutch** (Shopify default scraper block) | ✅ |
| noindex | Contact + 5 policy + cookie-policy = noindex ✅; **/collections/all** = noindex ✅; **/collections/shop-all = NOT noindex** | 🟡 (brief expects shop-all noindex; live correctly indexes the curated shop-all and noindexes the `/collections/all` duplicate) |
| Canonical host | clean — no myshopify/wrong-domain in canonical/og/schema (only trivial `@context "http://schema.org"` in header.liquid:287; structured-data snippet uses https) | ✅ |
| Orphan assets | 117 assets; candidates: `icon-double-chevron.svg`, `icon-orders.svg`, `icon-shopify.svg`, `jsconfig.json` (stock/dev leftovers) | minor |

## 3. Architecture / SEO / GEO (live)
| Item | Finding | Verdict |
|---|---|---|
| Canonical resolution | home/PDP/collection/guide all → `https://senseless.uk/...` | ✅ |
| Titles | present, branded; title-doubling guard **correct** (`meta-tags.liquid`: `brand_name='Senseless'`, appends `\| Senseless` *unless* title already contains it — e.g. guide "How Senseless Works…" correctly gets no suffix); `og:site_name=Senseless` hardcoded | ✅ |
| Meta uniqueness | sampled 4 types distinct; full site-wide dupe/length scan not run | ⚠️ recommend full dupe-scan |
| og:image | PDP ✅, collection ✅; **home ❌, guide (/pages/*) ❌** | ❌ |
| JSON-LD breadth | home: Organization+WebSite+BreadcrumbList ✅ · PDP: Product(+Offer w/ shippingDetails+MerchantReturnPolicy)+BreadcrumbList+FAQPage ✅ · collection: CollectionPage+BreadcrumbList+FAQPage (**ItemList absent** — deliberately removed in the 2026-06-12 dedup 🟡) · guide: BreadcrumbList+FAQPage, **Article absent** ❌ (these are `/pages/*`, not `/blogs/*` articles) | mixed |
| Sitemap | present; injectables (`numbing-cream-for-botox/-injections/-lip-fillers`) in sitemap, not in nav | ✅ |
| Internal 404 crawl | 68 sitemap URLs → **0 real non-200** (1 transient timeout on `numbing-cream-for-semi-permanent-makeup`; resolves 200 on retry) | ✅ |
| llms.txt / GEO | `/llms.txt` serves **Shopify's generic "Agent Instructions" (shop.app/SKILL.md)**, NOT the bespoke Senseless doc; bespoke GEO doc exists at **/pages/llms-txt** (mentions "Senseless System" ×3). The `/llms.txt→/pages/llms-txt` redirect is overridden by Shopify's native /llms.txt | ❌/🟡 — agents hitting /llms.txt get the generic file |
| Key Facts / FAQ answer-first | FAQPage on PDP/collection/guide | ✅ |

## 4. Image weight
| Item | Finding | Verdict |
|---|---|---|
| Manifest CDN URLs | `image-manifest.json` records **stale, oversized masters** (collection/page heroes logged 1.0–1.9 MB, homepage sections 1.7 MB, product records 320–557 KB) | 🟡 manifest stale |
| Actual served (spot-check) | real `senseless-homepage-hero.webp` = **166 KB** raw / 91 KB @ width=800; live srcset serves responsive WebP (480–1600); collection heroes serve ~98–195 KB (prior pass) | ✅ on-page weight within limits |
| Note | the manifest sizes predate the WebP conversion; they do **not** reflect what the theme serves (width-param variants). Recommend refreshing the manifest + a served-size audit. | — |

## 5. Honesty / not-API-checkable
- webPixel (GA4/Google Ads): 🔒 verify Settings → Customer events.
- shop.brand logo + cover image: 🔒 verify Settings → Brand.
- get-shop-info (chat MCP): not this run's job (planning layer); CLI + Admin token verified here instead.

## 6. Live checks (password OFF — confirmed: `/` 200, `/password` 302→home)
| Item | Finding | Verdict |
|---|---|---|
| SSL chain | valid Let's Encrypt, CN=senseless.uk, 2026-06-08 → 2026-09-06 | ✅ |
| www → non-www | `https://www.senseless.uk/` → 301 → `https://senseless.uk/` | ✅ |
| Served robots.txt | sitemap referenced; AI crawlers not disallowed | ✅ |
| PageSpeed / Core Web Vitals | external tool | 🔒 Daniel action (run PageSpeed Insights on home + a PDP) |
| Google Rich Results validation | external tool; JSON-LD validated structurally here (types present, all parse OK) | 🔒 Daniel action (run RRT on a PDP + collection) |
| Live test order | not read-only | 🔒 Daniel's separate action |

---

## Canon conflicts / state mismatches (🟡 — for the planning layer, not resolved here)
1. **Live theme name** — the [live] theme is still named "Senseless Dev" (legacy); it is the single published theme, not a dev theme. Rename for clarity (optional).
2. **Leftover Git branches** — `dev` (local + `origin/dev`), `build/phase-0-foundations`, and 3× `feature/*` remain (local + remote), contradicting the "all dev branches deleted" operating model.
3. **Trust bar** — rating-led redesign (★4.9, 230+ reviews, Trusted by UK Practitioners, Free delivery over £40) shipped 2026-06-24, vs the canon "4 locked signals" (UK formulated · Cosmetic product · CPSR assessed · Made for aesthetics). Update canon or reconcile.
4. **shop-all noindex** — brief expects `/collections/shop-all` noindex; live (deliberately) **indexes** the curated shop-all and **noindexes** `/collections/all`. Confirm canon.
5. **Flag words** — "everyday"/"upgrade"/"concentrated"/"most concentrated" present (incl. the strongest-page H1 "Our most concentrated formula") — canon disagrees with itself; owner ruling.
6. **Cleanser size** — live is **35ml** everywhere (PDP/keyfacts/schema/cart, bundle contents "Foaming Cleanser (35ml)"); the "150ml" canon note is stale.
7. **Origin wording** — "Formulated and produced in the United Kingdom" (`page.about.json:239`) — "produced in" vs the preferred "formulated in".
8. **/llms.txt** — Shopify-native generic file served at the canonical agent path instead of the bespoke `/pages/llms-txt`.

## Verified gaps to fix (❌)
- **Required safety warning** ("do not apply to broken/inflamed/sunburnt skin") absent from all 10 product templates (patch-test present on 9 strength SKUs only; cleanser none). [on-pack vs on-web is a judgement call]
- **og:image** missing on home + guide (/pages/*) page types.
- **Article** JSON-LD absent on guide pages (`/pages/*`); **ItemList** absent on collections (deliberate June dedup — confirm intent).
- **FOAM "antibacterial"** claim (×4) needs substantiation review.
- **/llms.txt** serves the generic Shop-app file, not the bespoke Senseless GEO doc.

## Daniel's separate actions (not read-only)
- Verify GA4/Google Ads web pixel (Settings → Customer events) + Brand logo/cover (Settings → Brand).
- Run PageSpeed/CWV + Google Rich Results Test on home/PDP/collection.
- Place one live test order end-to-end before public go-live.
