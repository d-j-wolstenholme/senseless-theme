# Next session — Senseless (Canon v2.20)

Read `CLAUDE.md` → run `scripts/reconcile.sh` → read the Project Instance + State Surface first.
**Machine last used:** MacBook Pro — 7 Aug (`Daniels-MacBook-Pro.local`). The machine clock is
**UTC+3 (EEST)** — matters for anything timestamped or latency-measured.

## 7 Aug 2026 — Cannibalisation phase 4. SHIPPED.

`main` is clean at `6af876b`, pushed to `origin/main`. One theme file deployed and verified live.
Full record in `DECISIONS-LOG.md` (top entry).

### What shipped

**The owner ruling.** Daniel ruled that **collection SEO carries the category keywords and PDP SEO
does not** — collections are the funnel entry, PDPs sit below them and are the more
compliance-constrained surface. That is the **per-cluster owner ruling** the 2026-06-15 entry was
waiting on, and it **closes the SEO-RISK hold** on the 8 PDP `title_tag`s. Note the ruling is
*subtractive* where that entry recommended an *additive* pattern — the hold is superseded, not
satisfied. **`senseless-vs-ametop`'s title was held by the same entry and is NOT covered — it stays held.**

**Admin API writes (10) — no deploy needed.**
- 9 core-SKU `seo.title`s now match their existing H1s: `Clinical/Advanced/Professional Strength
  Cream|Gel|Spray`. `clinical-strength-cream` keeps `| UK-Formulated`.
- `aesthetic-numbing-cream` → `Aesthetic Numbing Cream — Built for the Procedure`, so it no longer
  mirrors the main cream collection. Em dash, per house style (the brief's hyphen was corrected).

**Theme (1 file, deployed + Asset-API verified).**
- `collection.numbing-cream-for-laser-treatment.json:160` — "SPMU" was the only unlinked
  cross-procedure noun on either procedure collection; now links to the SPMU collection.

**Verification.** Store gate PASS before every write. All 10 re-read from the Admin API and diffed
against a pre-write snapshot: **0 of 32 `seo.description`s changed** — the 6 Aug Foaming-Cleanser
null-trap did NOT recur. All 10 curled live with `?_fd=0`: titles correct, **H1s unchanged**, meta
descriptions present. Laser page pulled 4× with varied UA post-deploy: SPMU link renders,
**0 links to the three injectable collections** — invariant intact. theme-check 0 errors.

### Expected, not a regression

**PDP impressions on the bare category terms ("numbing gel", "numbing spray") should FALL.** That is
the intended outcome — those terms now belong to `/collections/numbing-gel` and `/collections/numbing-spray`
uncontested. Judge the change on *collection* impressions and on total non-brand clicks, not on PDP
impressions. Give it 4–6 weeks before reading anything into it.

## ⛔ Outstanding from this session

1. **Notion write-back never happened.** The Notion MCP connector did not come up, and there is no
   API token in `.env` and no `ntn` on PATH — so the **State Surface log and the phase-4 Decision
   were not written**. `DECISIONS-LOG.md` is the only record. **Mirror it when the connector is back.**
   Unlike Shopify MCP, there is no documented fallback path for Notion — worth fixing properly.

## Next Work Item

1. **Mirror the phase-4 decision to Notion** (above) — do this first, it is the open loop.
2. **Daniel: supply the agency contact name** so the 7 Aug review document can go.

## Flagged this session — Daniel's call, not actioned

1. **The three spray PDP descriptions all say "suited to broad areas such as laser and waxing
   appointments."** This — not the collection copy — is the only real laser/waxing keyword overlap on
   the site, and it also leaks through the laser collection's `.atom` and `.oembed` feeds. Admin edit,
   not a theme edit. Wants a real ranking source first.
2. **All 5 bundle `seo.description`s still promise a "vanity bag."** The bag was pulled from the four
   on-page surfaces on 6 Aug pending stock; the meta descriptions are a **5th surface that was missed**
   and are live in SERPs now, promising an item that is not in the box. Fix when the bag lands (see
   the restore note below) or edit the descriptions in the interim.
3. `UK-Formulated` in the clinical cream title vs `UK-formulated` everywhere else — descriptions
   outvote the title 10:1.
4. The laser hero alt says "Comfort Spray and Comfort **Gel** — laser treatment" while the body copy
   three sections later says "Gel isn't the laser format." They disagree. Cheap fix.

## Gotchas earned this session — don't re-derive

1. **`productUpdate` DELETES `global.title_tag` when `seo.title` is byte-identical to `product.title`.**
   8 of the 9 PDPs now read `seo.title = null` and inherit `product.title` at render. Output is exactly
   right, and this is the **safer** form — inheritance tracks a future rename, a frozen duplicate would
   not — so it was **left as-is deliberately**. Do not "fix" it back.
2. **A write-verification that compares against the value the mutation RETURNED will false-pass.**
   `productUpdate` returns the *post-normalisation* value, so `returned == returned` is always true.
   My first verify pass reported 10/10 OK while 8 titles had actually been nulled. **Compare against the
   INTENDED string, then re-read from the API as a separate call.** This is the same class of error as
   the 6 Aug "deploy: success" that pushed nothing.
3. **A mid-workflow agent will report the state it sees, not the state you started from.** The
   compliance agent ran after the writes landed and concluded "facts B and F are WRONG — Tasks 1 and 2
   are already achieved." They were not wrong; it was reading the post-write world. **Snapshot before
   you write, and date-stamp what you hand agents**, or you will be talked out of work you already did.
4. **Verify a cannibalisation premise against `<main>`, not the whole document.** A whole-page term
   count on this site returns `waxing ×4` on *every* page because the header/footer nav links all
   procedure collections sitewide. Strip header/footer/nav first, or every page looks like it
   cannibalises every other one.

## Still open from 6 Aug — unchanged

1. **⏳ VANITY BAG — restore when stock lands.** `git revert db6d6fc`, or re-add *"and a reusable vanity
   bag"* to the prose at `templates/product.bundle.json:71,83` and `templates/collection.bundles.json:25`,
   and restore the label at `product.bundle.json:45`. **Also add the bag to the
   `senseless.bundle_contents` metafield on all five kits**, and fix the 5 bundle meta descriptions
   (item 2 above). Note `:83` also feeds the FAQPage JSON-LD.
2. **Social profile URLs** — footer settings wired (`senseless-footer.liquid:180-184`) and empty. Then add
   `sameAs` to both Organization nodes. No placeholder links.
3. **Judge.me floating reviews tab** — ~90 KB on every page. `config/settings_data.json:106`.
4. **Three chat widgets at once** — Dondy, Shopify Inbox, Google. Which is actually answered?
5. **GSC → Page Indexing export.** Still needed: we cannot produce a dated, exportable index count.
6. **Bing Webmaster** — conceded in writing to the agency. Actually do it.
7. **Editorial cadence** — 5 articles, all 4 June, nothing since.
8. **Articles hub imagery** — 8 of 13 cards use the brand asterisk.

## Standing gotchas — still true

1. **Never hand an agent a loop.** Deterministic collection is a script's job; agents get judgement and
   writing, in bounded units, handed finished data. (This session followed that and it worked.)
2. **Never apply a subagent's correction without opening the source yourself.** An audit agent
   previously fabricated a citation in full detail. See gotcha 3 above for this session's variant.
3. **Ahrefs volumes are country-specific and they move.** Every figure needs its country, its date and
   its endpoint.
4. **`deploy.sh` under `bash`, never zsh** — zsh does not word-split `$FILES`, so it reports success and
   pushes nothing. Always follow with a per-file Asset-API compare.
5. **COMMIT → PUSH → THEN DEPLOY.** An interruption after a deploy leaves the store running code that
   exists nowhere in git.
6. **`?_fd=0` to bust the edge cache, not `?cb=`.**

## Key artefacts

- `DECISIONS-LOG.md` — top entry is the full phase-4 record, incl. the premise-failure evidence.
- `~/Documents/MHG-agency-review/…-2026-08-07.pdf` — the agency review document, still awaiting a contact name.
- `scratchpad/VERIFIED_FACTS.md` · `census.json` — the 7 Aug verified fact base.
