# NEXT_SESSION — handoff

**Last session (19 Aug 2026, MacBook Pro):** fixed the three Merchant listings
structured-data issues Search Console reported on senseless.uk.

## Done

- **Diagnosed against live, not assumed.** GSC reported missing
  `hasMerchantReturnPolicy` (in `offers`), missing `shippingDetails` (in `offers`),
  and missing `description`. It was **not** the product pages — a PDP's Product node
  already had all three. The gap was the Product nested inside each collection's
  `ItemList`: it emitted `name/url/image/sku/brand` and a bare Offer of
  price + availability + seller. 19 collection URLs; `/collections/all` alone
  carried 16 such Products. No other page type emits a Product at all.
- **Fixed by reference, not repetition.** The five shipping methods and the return
  policy are now defined **once per page** as top-level `@graph` nodes with stable
  absolute `@id`s; every Offer — PDP and collection — points at them by `@id`.
  This is Google's own documented pattern
  (`search/docs/appearance/structured-data/product-variants`). Side effects worth
  knowing: the rate card now lives in **exactly one place** in
  `snippets/senseless-structured-data.liquid`, and the PDP `<head>` got *smaller*.
- Nested Product also gained `description` (300 chars — a listing entry is a
  summary, and a collection can carry 48) and `itemCondition`.
- **Live-verified 19/19 collections + PDPs**: every Product has a description, every
  Offer has both fields, every `@id` resolves in-graph, zero dangling refs.
- Commits `b19e710` (fix) + `c2ce068` (reviews-guard re-lock). Deployed via
  `deploy.sh`, Asset-API byte-identical, Judge.me markers 5/5 on every checked URL.
- **Injectable-clean invariant re-verified: 46/46 ad-facing surfaces, 0 breaches.**
  35 by the script, 11 by hand (see the gotcha below). The diff adds zero anchors.
- Written up: Decision `3c158bc3-75ea-8165-85e9-f5579b683663` (Decisions DB) +
  State Surface log entry + `canon/state.json`.
- **Owner action outstanding:** in Search Console, open each of the 3 Merchant
  listings issues and click **Validate fix**.

## Next

Unchanged from before — this was an interrupt, not a plan change:

1. **Commission the 12 images.** Brief is written and ready to hand over:
   `docs/IMAGE-BRIEF-tattoo-cluster.md`. Finals to `assets/images/inbox/`,
   `scripts/image-pipeline.mjs` does the rest.
2. **G2 — the only safety gate still open.** Can *"Apply to clean, unbroken skin"*
   change? Assume NO until the safety assessor rules. One email closes it.
   (**G1 is closed. Do not re-raise it.**)
3. **`tattoo pain chart`** — 6,900/mo at KD 1, `/pages/tattoo-pain-chart` is a 404,
   and the two strategy docs contradict each other on whether it is winnable.
   Resolve that before anyone spends on it.

## Gotchas earned this session

- **`shopify theme dev` is not usable in this repo.** It uploads the whole tree and
  Shopify rejects `assets/images/**` ("Theme files may not be stored in subfolders");
  `--ignore` didn't save it, and repeated attempts got the sync **Throttled**.
  `deploy.sh` avoids this only because it is scoped with `--only`. To validate
  rendered Liquid offline, use **python-liquid** instead —
  `scratchpad/render.py` pattern: `DictLoader` over `snippets/`, stub product +
  collection data, register the Shopify-only filters (`json`, `asset_url`,
  `image_url`, …). One catch: python-liquid chokes on prose inside a
  `comment … endcomment` **nested in a `{% liquid %}` block** — strip those before
  parsing; they emit nothing, so it cannot change the output.
- **The zsh word-split trap bites outside `deploy.sh` too.** `python3 verify.py $urls`
  passed all 19 newline-separated URLs as ONE argument and reported a false failure.
  Run anything taking a list of paths/URLs under `bash -c`.
- **`injectable-clean-sweep.py` prints `BREACHES: 0` even when every fetch returned
  HTTP 429.** It did so twice this session. **Read the ERROR count above it before
  trusting that zero.** The 11 product URLs it could not fetch were re-checked by
  hand at one request per 7s — all clean — so the invariant does hold, but only
  because the gap was noticed. Same family as the standing lesson on Decision
  `3bc58bc3`: a check that can only confirm its own assumptions is not a check.
- **Rate-limit yourself.** Auditing the storefront hard enough to diagnose a schema
  bug earns `HTTP 429` across the whole catalogue for the next quarter of an hour,
  which then contaminates every follow-up check.
- `snippets/senseless-structured-data.liquid` is a **reviews-guard file** (it reads
  `product.metafields.reviews.rating`), so any edit to it needs
  `deploy.sh --reviews-changed` plus a lock commit — even when the diff touches no
  reviews line.

**After any nav, collection, homepage or landing-page change:** re-run
`python3 scripts/injectable-clean-sweep.py`. Baseline **0 breaches across 46
ad-facing surfaces**.
