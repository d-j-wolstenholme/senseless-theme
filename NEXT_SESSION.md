# Next session — Senseless (Canon v2.20)

Read `CLAUDE.md` → run `scripts/reconcile.sh` → read the Project Instance + State Surface first.
**Machine last used:** MacBook Pro — 8 Aug (`Daniels-MacBook-Pro.local`). Clock is **UTC+3 (EEST)**:
consoles like Bing and Google render timestamps in EEST, not UK time. Bit us once tonight reading an
IndexNow export.

`main` is clean at **`f2483be`**, level with `origin/main`. Everything below is committed, pushed and
live-verified. Nothing is deployed-but-uncommitted.

---

## Session ran in two halves

### Half 1 — Cannibalisation phase 4 (7 Aug)

**Owner ruling (Daniel):** collection SEO carries the category keywords, PDP SEO does not — collections
are the funnel entry, PDPs sit below them and are more compliance-constrained. This **closes the
2026-06-15 SEO-RISK hold** on the 8 PDP `title_tag`s. That entry recommended an *additive* pattern; the
ruling is *subtractive*, so it **supersedes** rather than satisfies it. **`senseless-vs-ametop`'s title
was held by the same entry and is NOT covered — still held.**

Shipped: 9 core-SKU `seo.title`s rewritten to match their existing H1s · `aesthetic-numbing-cream` →
"Aesthetic Numbing Cream — Built for the Procedure" · one theme edit linking the unlinked "SPMU" on the
laser collection.

**Task 3 was NOT done — the premise failed, it wasn't skipped.** Three independent angles all returned
PREMISE_FAILS. Inside `<main>`: laser has **waxing ×0, scalp ×0**; injections has **waxing ×0, laser ×0,
spray ×0**. The counts a whole-page scan sees are the **site-wide nav**, byte-identical on every page.
**"scalp" appears nowhere on senseless.uk at all.** Second time this agency's data hasn't survived
contact — see `7567f80`.

**Expected, not a regression:** PDP impressions on bare category terms ("numbing gel", "numbing spray")
should FALL. Judge on *collection* impressions and total non-brand clicks. Give it 4–6 weeks.

### Half 2 — Bing, Clarity, and a deploy bug (8 Aug)

- **`91e29b1` — `deploy.sh` was reporting SUCCESS on a failed push.** See gotcha 1.
- **`276bd8c` — Bing ownership meta tag** (`msvalidate.01` in `snippets/meta-tags.liquid`), live sitewide.
  Bing ownership was inherited from a **Google Search Console import done by Peter**, which Microsoft
  documents as an *ongoing* dependency — if his GSC access lapses, Bing verification lapses and takes
  Daniel's delegated admin with it. The tag makes ownership provable independently. **The agency's
  "Missing Bing Webmaster Code" item was right**; two of my earlier answers calling it redundant were
  wrong.
- **`248a21f` — Bing URL submission**, wired into `deploy.sh` as a non-fatal step.
- **`a0b1c54` + `f2483be` — Microsoft Clarity**, consent-gated.
- **`bf891e6` — Notion write-back done**, and a stale pointer found and fixed.

---

## ⚠️ Read before touching the cookie banner

**Clarity's consent gate spans two files.** `snippets/senseless-clarity.liquid` reads
`localStorage['ss_cookie_choice_v1']` and listens for the **`ss:consent`** CustomEvent, which
`snippets/senseless-cookie-consent.liquid` dispatches from `choose()`.

**Refactoring the banner without preserving both will silently start recording UK visitors without
consent.** That is a PECR exposure, not a bug report. After any change to either file, re-run the
three-state live test: no decision → Accept → Reject-then-reload, checking `typeof window.clarity` and
`document.querySelectorAll('script[src*="clarity.ms"]')` each time.

---

## New in the toolchain

- **`scripts/bing-submit.py`** — submits sitemap URLs to Bing. Runs automatically at the end of
  `deploy.sh`, non-fatal, 6h per-URL cooldown. **`bing-submit:` lines in deploy output are normal.**
  Run manually with `--all` after a big content push; `--dry-run` shows quota without submitting.
  A full run costs **58 of 100** daily quota.
- **`BING_API_KEY`** is in `.env` (gitignored, untracked). `.bing-submit-state.json` is gitignored.
- **Clarity project `xz8e5qri1p`** — dashboard via Bing Webmaster Tools → Microsoft Clarity.
  Expect no data until real consented traffic accumulates.

---

## Next Work Item

1. **The 5 bundle `seo.description`s still promise a "vanity bag"** removed from on-page copy on 6 Aug.
   Live in Google now, advertising an item that is not in the box. **The most customer-facing thing
   outstanding.** Fix the copy or restore the bag.
2. **Notion — the richer write-back.** The phase-4 log + Decision landed, but the **State Surface header
   and its Sync status line** were out of scope for a log append and still describe the 7 Aug agency
   session. Also wants: a Decisions entry for the Bing verification ruling, and a build report for the
   Bing + Clarity work.
3. **The agency reply** — never drafted. Material is in `scratchpad/agency_*.txt`.
4. **Ask Peter whether he should see the Clarity terms retrospectively** — Daniel accepted them, and
   Peter is the Bing property owner of record.

---

## Gotchas earned — don't re-derive

1. **`if ! cmd; then rc=$?` captures the NEGATION's status, always 0.** A failed `shopify theme push`
   set `rc=0`, printed "FAILED (exit 0)" and exited **0** — reporting success and skipping the
   post-deploy verify. Use `cmd || rc=$?`. **Third variant of this family** after the zsh no-word-split
   no-op push and the `productUpdate` false-pass verify. **Always test a deploy/verify path against a
   deliberately failing case, not just a passing one.**
2. **Shopify's `visitorConsentCollected` does NOT fire for this site's custom banner** — even though
   `Shopify.customerPrivacy.setTrackingConsent` is available. Clarity relied on it and silently never
   loaded until the next pageview. **Every static check passed; only a live behavioural test caught it.**
3. **`productUpdate` DELETES `global.title_tag`** when `seo.title` is byte-identical to `product.title`.
   8 of 9 PDPs now read `seo.title = null` and inherit. Output is correct and this is the SAFER form —
   **do not fill those fields in.**
4. **A verification that compares against the value a MUTATION RETURNED will false-pass** — it returns the
   post-normalisation value. Compare against the **intended** string, then re-read as a separate call.
5. **Verify a cannibalisation premise against `<main>`, not the whole document.** Whole-page term counts
   include the site-wide nav, so every page looks like it cannibalises every other one.
6. **Self-hosted IndexNow is impossible on Shopify.** Needs a key file at the domain root; a key hosted
   elsewhere only authorises URLs under that prefix. Don't re-investigate — use the Bing URL Submission
   API (JSON/REST, unaffected by the 31 Aug SOAP/POX retirement). Live method name is **`SubmitUrlbatch`**,
   lowercase b.
7. **`DECISIONS-LOG.md` pointed at an ARCHIVED Notion page** for ~6 weeks — "Vol 1 — May 2026" under
   *Archive (pre-migration)*. Repointed to the live Decisions DB
   `d5ce9514-257c-4e02-aced-acba800e89d9`. **Trust the Project Instance §2 registry over any pointer in
   a repo doc.**
8. **This machine is UTC+3.** Bing/Google consoles render EEST. An IndexNow export read as "all 6 Aug"
   when two rows were actually 5 Aug.
9. **`deploy.sh` under `bash`, never zsh** (no word-splitting → silent no-op push). Follow with a per-file
   Asset-API compare.
10. **COMMIT → PUSH → THEN DEPLOY.** `?_fd=0` to bust the edge cache, not `?cb=`.

---

## Standing, unchanged

- **Never hand an agent a loop.** Deterministic collection is a script's job; agents get judgement and
  writing, in bounded units, handed finished data. Followed tonight; worked.
- **Never apply a subagent's correction without opening the source yourself.** Tonight a subagent's
  "facts B and F are WRONG" was an artifact of it reading post-write state mid-workflow. **Snapshot before
  you write, and date-stamp what you hand agents**, or you will be talked out of work you already did.
- **Ahrefs volumes are country-specific and they move.** Every figure needs country, date and endpoint.

## Still open from 6 Aug

1. **⏳ VANITY BAG — restore when stock lands.** `git revert db6d6fc`, plus the
   `senseless.bundle_contents` metafield on all five kits, plus the 5 meta descriptions (item 1 above).
2. **Social profile URLs** — footer settings wired and empty; then `sameAs` on both Organization nodes.
3. **Judge.me floating reviews tab** — ~90 KB every page. `config/settings_data.json:106`.
4. **Three chat widgets at once** — Dondy, Shopify Inbox, Google.
5. **GSC → Page Indexing export** — still cannot produce a dated index count.
6. **Editorial cadence** — 5 articles, all 4 June.
7. **Articles hub imagery** — 8 of 13 cards use the brand asterisk.
8. ~~Bing Webmaster~~ — **DONE**, and it turned out to have been set up since 13 July.

## Key artefacts

- `DECISIONS-LOG.md` — top two entries are tonight's full record.
- `scratchpad/agency_schema.txt` · `agency_competitor.txt` · `agency_recommendations.txt` ·
  `agency_keywords.csv` — the agency's four deliverables, exported and reviewed.
- `scratchpad/bing-submit.DRAFT.py` — a superseded draft; the shipped one is `scripts/bing-submit.py`.
