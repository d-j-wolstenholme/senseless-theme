# Next session — Senseless (Canon v2.20)

Read `CLAUDE.md` → run `scripts/reconcile.sh` → read the Project Instance + State Surface first.
**Machine last used:** MacBook Pro — confirmed 6 Aug (`Daniels-MacBook-Pro.local`). Hostname can display as `Daniels-MBP.Home`; same machine.

## Done 2026-08-05/06 (Claude Code · Opus 5) — commits `81ae8b7` → `eb0be3d`, all deployed + live-verified

### 1. Third-party SEO audit — verified claim by claim, mostly wrong
An agency delivered a 23-page **SEO Audit** PDF + an **On-Page Recommendations** doc. Do not re-investigate these:

| Claim | Reality |
|---|---|
| Product/FAQ/Article/Review/WebSite schema **missing** | **False.** 34 valid JSON-LD blocks across 12 URLs. They tested the homepage only. |
| Site has **LocalBusiness** schema | **False — no such node exists.** Google's tool labels our address-bearing `Organization` as "Local businesses". |
| TTFB 658 ms | **False.** Median **117 ms**. Their own FCP 954 ms / LCP 1.4 s are *good* CWV, reported as defects. |
| Articles missing thumbnails | **False.** 5 of 5 have images. |
| 77 blocked internal / external resources | **One** stock Shopify `/checkouts/` preload; the external half is Judge.me's own CDN. |
| 11 pages blocked from crawling | **True and all deliberate** (`layout/theme.liquid:43-57`). |
| 77 low text-HTML ratio | True as a number, **not a content problem** — ~80% of each page is inline script/CSS/SVG. |
| CTAs limited/inconsistent | **False.** Their own Recommendation says "No Action Required". |

**Genuinely true:** no Bing tag · no social links · nothing published in 61 days · homepage thin in *answer-shaped fact*.

### 2. Shipped
- **4 theme fixes** — related-guides module on articles (two guides had a single indexable inbound link; now all 5 give 3 and receive 3), asterisk cards no longer cropped, `/blogs/guides` cards 16/9, duplicate `fly-to-cart.js` tag removed.
- **Nav "Help" → "FAQ"** (Daniel approved). Full 6-item menu re-sent deliberately — `menuUpdate` is a REPLACE and a partial list silently drops Articles + Rewards.
- **46 compliance rewrites across 25 templates + 5 kit descriptions**, every one reusing a construction already shipped. content-lint **BLOCK 0**.
- **10 product descriptions written and published** — see §3.
- **Canon fixes** — `schema-contract.json` was still v2.19; the deploy skill and `STATE.md` both said the storefront password was ON when the site is public; `CLAUDE.md` range double-counted the cleanser.
- **Ad-facing invariant promoted to canon** — Notion Decision + `.claude/rules/ad-facing.md` + `CLAUDE.md` pointer.

### 3. Product descriptions (the 10 core SKUs)
Empty since 1 June, so their Product JSON-LD was boilerplate. Now written, adversarially reviewed, published, live-verified. Canonical copy: **`docs/product-descriptions.json`** — keep it in step with admin.
- `body_html` feeds **both** the Product JSON-LD and the **Merchant Center feed**, so it is **ad-facing**. No injectable procedure is named in any description, even though several SKUs list Botox/lip fillers in `recommended_procedures`.
- Schema truncate raised **480 → 1200** (`senseless-structured-data.liquid`): at 480 every strength SKU was cut mid-sentence, losing sizes and the CPSR credential.
- Hero renders the **first two paragraphs only** — buy-box copy came down from 126–142 words to 94–110 (kits are 68) while the full text still reaches schema + feed.
- `shortdesc` section removed from all 10 templates — it duplicated the description's opening sentence verbatim.
- **"Antibacterial" on the cleanser is substantiated** (Daniel, 6 Aug; Confirmed Fact logged). Do not re-raise.

## ⏳ PUT THE VANITY BAG BACK WHEN STOCK ARRIVES

Daniel confirmed (6 Aug) the bag **does** ship with all five bundles, but stock had not landed while the bundles were on sale with 19–20 units each — so every bundle sold was promising something that couldn't be supplied. His call was to remove it until stock lands, rather than qualify it or pause sales.

**To restore:** `git revert db6d6fc`, or re-add *"and a reusable vanity bag"* to the three prose strings in `templates/product.bundle.json` (:71, :83) and `templates/collection.bundles.json` (:25), and restore the label at `product.bundle.json:45` to *"Cream, gel, spray, cleanser + vanity bag"*.

**Do this at the same time:** add the bag to the `senseless.bundle_contents` metafield on all five kits. It currently lists four items — that mismatch is exactly what surfaced the problem. Get data and copy agreeing from the start this time.

Note `:83` is also the source of the FAQPage JSON-LD, so the claim reaches Google as well as the page.

## Next Work Item — open, needs Daniel

1. **Social profile URLs** — footer settings already wired (`senseless-footer.liquid:180-184`) and empty. Then add `sameAs` to both Organization nodes. **Do not add placeholder links.**
2. **Judge.me floating reviews tab** — ~90 KB injected into *every* page including the FAQ and cart (17–23% of each document). Disabling `reviews_tab` (`config/settings_data.json:106`) keeps PDP reviews and star badges. Best byte-win available.
3. **Three chat widgets at once** — Dondy WhatsApp, Shopify Inbox, Google store widget. Which is actually answered? The other two come off. This is where the post-onload tail lives, not the theme.
4. **GSC → Page Indexing export** — nothing on the site blocks indexing (58 indexable URLs, all 200, canonicals clean), so only GSC can settle the "17 pages indexed" claim.
5. **Editorial cadence** — 5 articles, all published within one second on 4 June, nothing since.
6. **Homepage factual depth** — 690 words is normal; what's missing is range/sizes/delivery facts, not word count. Four compliance-safe block shapes proposed (range table · credentials · delivery facts · signpost row).
7. **Bing** — try BWT "Import from Google Search Console"; GSC is already verified so it needs no code.

## Gotchas earned — don't re-derive

1. **COMMIT BEFORE YOU DEPLOY — the order is load-bearing.** On 6 Aug an API error landed between `deploy.sh` and `git commit`, leaving the footer fix **live and uncommitted**; it surfaced only because `git status` was re-checked rather than assumed. Commit → push → deploy means the worst case is an unshipped commit, which is visible and harmless. Now written into `.claude/rules/deploy-and-store.md` and the `commit-and-deploy` skill.
2. **`./scripts/deploy.sh $FILES` under zsh does NOT word-split.** deploy.sh received 25 paths as ONE `--only` argument, printed **"deploy: success"**, and pushed **nothing**. Run it under `bash`, and always verify per file via the Asset API — **deploy.sh's exit code does not catch this; only the Asset-API compare does.** This is the project's known deployed≠committed failure mode in a new disguise.
3. **The `commit-and-deploy` skill used to document raw `shopify theme push`**, contradicting the deploy rule's "`deploy.sh` only". Corrected 6 Aug — if you see raw `theme push` anywhere else, it is wrong.
4. **`assets/images/**` DOES deploy.** 18 files (~7.5 MB of unreferenced source PNGs) are live theme assets. Any verifier built on "they never deploy" mis-counts.
5. **Verify parity with the Admin Asset API, not just `theme pull`.** `themes.json` → `updated_at` is a one-call check: if it hasn't moved since the last verified parity, no Theme-Editor write happened.
6. **The version invariant has no repo-side enforcement.** `.claude/hooks/guard-write.py:47` only checks `canon_version` is truthy, never that it equals `canon/state.json`. That is why `schema-contract.json` sat at v2.19 through a version sweep.
7. **Liquid raises on a nil comparison** — `image.aspect_ratio` can be nil for SVGs. Guard with `| default: 0`.
8. **The PDP 45–60 minute line is NOT a breach** — operator-accepted under Decision `39158bc3-75ea-81f7`, recorded in `docs/COMPLIANCE.md:40` and the compliance-check skill as explicitly "not a regression". An earlier note cited `…-8181` and mis-stated its scope. Rewriting it would reverse a live operator decision.
9. **`/pages/choosing-your-format` is retired** (301, not in the sitemap). Do not harvest copy from it — its "gel spreads further" contradicts every live gel surface.
10. **Clinical gel SKUs are the anomaly, not the docs.** Live `S15CL`/`S35CL` vs `SG15AD`/`SG15PR` on the other gels. `docs/ARCHITECTURE.md` is internally consistent; Daniel decides whether live gets renamed.
11. **Two repo scripts are destructive if re-run:** `policy-menus-redirects.py` does a full `menuUpdate` replace against a stale record and would **wipe Articles + Rewards from the primary nav**; `policy-metafields.py` would publish shipping prices **£1 under** what checkout charges.
12. **The State Surface log is past its rollover point** — 66 entries against Blueprint 01 §4.7's ~20, ~94% of the page. The operator deferred the backlog at v2.19; worth raising again.
