# Next session — Senseless (Canon v2.20)

Read `CLAUDE.md` → run `scripts/reconcile.sh` → read the Project Instance + State Surface first.
**Machine last used:** MacBook Pro — confirmed 5 Aug (`Daniels-MacBook-Pro.local`). Hostname can display as `Daniels-MBP.Home` (network-dependent); same machine.

## Done last session (2026-08-05, Claude Code · Opus 5) — commit `81ae8b7`, deployed + live-verified

Daniel supplied a 23-page agency **SEO Audit** PDF and an **On-Page Recommendations** Google Doc and asked for every issue verified and fixed.

### The audit is mostly wrong — do not re-litigate these
Verified live, claim by claim:

| Agency claim | Reality |
|---|---|
| Product / FAQ / Article / Review / WebSite schema **missing** | **False.** 34 valid JSON-LD blocks across 12 URLs. They tested the homepage only, where Product/Article legitimately don't belong. |
| Site has **LocalBusiness** schema | **False — no such node exists anywhere.** Google's test tool labels our address-bearing `Organization` as "Local businesses". That's their screenshot. |
| TTFB 658 ms | **False.** Measured median **117 ms** over 5 runs. FCP 954 ms / LCP 1.4 s are *good* CWV, which they list as defects. |
| Some articles lack featured images | **False.** 5 of 5 have images (1600×900 WebP, alt set). |
| 77 blocked internal resources | **One** — a stock Shopify `/checkouts/` preload. The "77" is the homepage resource count re-reported per page. |
| 77 blocked external resources | Real but **vendor-owned**: `cdn.judge.me/robots.txt` is `Disallow: /`. Unfixable, and irrelevant to indexing our pages. |
| 11 pages blocked from crawling | **True and all deliberate** — our 11 intentional noindexes (`layout/theme.liquid:43-57`). |
| 77 pages low text-HTML ratio | True as a measurement, **not a content problem**: ~80% of every page is inline script/CSS/SVG. Main-content word counts are 381–1,416. Not a ranking factor. |
| CTAs "limited and inconsistent" | **False.** 21 anchors + 4 buttons on the homepage; labels already consistent by destination ("View range" 7/7, "View product" 3/3, "Add to cart" 3/3). Their own Recommendation line says "No Action Required". |
| "Update and resubmit the XML sitemap" | **Impossible.** Shopify generates it; the file says so itself. |

**True:** Bing Webmaster tag absent · zero social links anywhere · nav says "Help" while the page is `/pages/faq` · nothing published in 61 days · homepage thin in *answer-shaped fact* (690 words is normal — what's missing is range/sizes/delivery facts, not word count).

### Shipped (theme, live-verified)
- `sections/senseless-article.liquid` — **related-guides module**. Guides were reachable only from `/pages/articles`; two had a single indexable inbound link. The window is offset from each article's own index and **wraps**, so all 5 give 3 and receive 3 (verified live: 3/3 each). Anchor text = article titles verbatim, so no new claim surface.
- `sections/senseless-articles-hub.liquid` — the 8 square asterisk cards were `object-fit:cover` in a 16:9 frame, clipping ~44% of the mark. Now contained.
- `sections/senseless-article-hub.liquid` — `/blogs/guides` framed 1600×900 photos at `1/1`. Now `16/9`.
- `snippets/scripts.liquid` — duplicate `fly-to-cart.js` script tag removed (the global one already covers PDPs).

### Canon drift found by an independent parity/canary pass, fixed in the same commit
- `.claude/schema-contract.json` still read **v2.19** — the version invariant was broken and nothing caught it.
- `commit-and-deploy/SKILL.md` + `STATE.md` both said the storefront password is **ON**. It is **OFF**; the store has been public since 7 Jun. The skill was telling future sessions their live deploys weren't customer-visible.
- `CLAUDE.md` range double-counted the cleanser. Live re-count: **16 products / 21 variants = 14 single SKUs + Foaming Cleanser (15)**, plus the Vitamin A&D 4-pack cart add-on and 5 bundles.

## Next Work Item — put these to Daniel, in this order

**1. TWO LIVE COMPLIANCE BREACHES (regulatory, outranks every SEO item).** Found during verification; the agency missed both. Deliberately **not** edited — `.claude/rules/compliance.md` reserves content-language calls to the founder.
   - **(a) All 5 kit product descriptions** carry: *"Numbing reduces discomfort rather than removing it — follow the product instructions and your practitioner's guidance."* This makes "numbing" the subject of an effect verb and asserts discomfort reduction. A mitigating clause is still a claim. It is being broadcast **machine-readably** into SERPs and answer engines via the Product JSON-LD. Admin-owned (`body_html`), no theme change.
   - **(b) PDP + collection FAQ blocks** carry *"while it takes effect"* and *"so it's working through the part that matters"*. **CORRECTED — the 45–60-minute timing on PDPs is NOT a breach:** `docs/COMPLIANCE.md:40` and `.claude/skills/compliance-check/SKILL.md:42` both record the PDP customer-attributed 45–60 line as **operator-accepted under Decision `39158bc3-75ea-81f7`** and explicitly "not a regression". An earlier note here cited `…-8181` and mis-stated its scope; rewriting the PDP line would have reversed a live operator decision. Only the **collection** surface was uncovered (no decision names a shop surface) and only that one was rewritten. ⚠️ Editing `product.*.json` requires `--reviews-changed` + a lock commit.

**2. 10 of 16 products have an entirely empty `body_html`** (all 9 cream/gel/spray SKUs + foaming cleanser), so their Product JSON-LD description falls back to `"<title> — a topical cosmetic preparation by Senseless."` The Product node is the highest-value LLM-extraction surface on the site and says nothing about 10 of 16 products. Admin-owned; picked up automatically once written. Ask whether Daniel drafts or Claude drafts to the CPSR envelope for his sign-off.

**3. Questions only Daniel can answer** (each blocks a real fix):
   - Which official social profiles exist, exact URLs? Footer already has Instagram/TikTok/Facebook settings wired (`sections/senseless-footer.liquid:180-184`) and they're empty. Adding `sameAs` to both Organization nodes is the defensible version of the agency's "thin entity data" point. **Do not add placeholder links.**
   - Rename nav "Help" → "FAQ" (menu item `835629973852`, admin-only, no deploy), or keep "Help" as a dropdown parent with FAQ/Contact/Shipping/Returns under it? UX call.
   - Judge.me's floating reviews tab injects **~90 KB into every page** including the FAQ and cart (17–23% of each document). Disabling `reviews_tab` (`config/settings_data.json:106`) keeps PDP reviews and star badges. Best byte-win available. Willing to lose the tab?
   - Three chat widgets run at once (Dondy WhatsApp, Shopify Inbox, Google store widget). Which one do you actually answer?
   - Bing: try **BWT → "Import from Google Search Console"** — GSC is already verified so it needs no code at all.
   - GSC → Page Indexing → export "Discovered/Crawled – currently not indexed". Nothing on the site blocks indexing (58 indexable URLs, all 200, canonicals clean), so only GSC can settle the "17 pages indexed" claim.

## Gotchas earned this session (don't re-derive)

1. **`assets/images/**` DOES deploy.** The standing assumption that those working dirs never reach the theme is **false** — 18 of them (~7.5 MB of unreferenced source PNGs) are live theme assets, uploaded 1–6 Jun. Any checksum verifier built on that premise mis-counts. Cleanup is a deliberate, destructive act — not done.
2. **Verify local↔live with the Admin Asset API, not just `theme pull`.** `GET /admin/api/2024-10/themes/199324434780/assets.json` returns an MD5 `checksum` per asset. Strip the leading `/* */` header and normalise `\/` escaping first or you get 4 phantom diffs (only 4 JSON files carry a committed pull header; the other 69 don't).
3. **One cheap check replaces a full re-audit:** `themes.json` → `updated_at`. If it hasn't moved since the last verified parity, no Theme-Editor write happened and the previous verdict still holds.
4. **The version invariant has no repo-side enforcement.** `.claude/hooks/guard-write.py:47` only asserts `canon_version` is truthy — it never compares it to `canon/state.json`. That's why `schema-contract.json` sat at v2.19 through a version sweep. Worth wiring properly.
5. **Liquid raises on a nil comparison.** `image.aspect_ratio` can be nil for SVGs, so `{% if img.aspect_ratio < 1.2 %}` renders a `Liquid error` inline. Guard with `| default: 0`, and detect SVGs off the `image_url` string.
6. **The clinical gel SKUs are the anomaly, not the docs.** Live: `S15CL`/`S35CL`, while both other gels are `SG15AD`/`SG35AD` and `SG15PR`/`SG35PR`. `docs/ARCHITECTURE.md` is internally consistent; "correcting" it to match live would codify a data-entry slip. Daniel decides whether live gets renamed.
7. **Two repo scripts are destructive if re-run** (found by the parity pass, not fixed — they are records, and fixing them is its own task): `scripts/policy-menus-redirects.py` does a full `menuUpdate` replace against a stale record and would **wipe Articles + Rewards from the primary nav**; `scripts/policy-metafields.py` would publish shipping prices **£1 under** what checkout actually charges (repo says £2.99/£7.99, checkout charges £3.99/£8.99).
8. **The State Surface log is past its rollover point** — 64 entries against Blueprint 01 §4.7's ~20 (last rolled over 3 Jul). It is ~29k tokens, 94% of the page, and every session pays to read it. The operator deliberately deferred the existing backlog at v2.19; worth raising again.
