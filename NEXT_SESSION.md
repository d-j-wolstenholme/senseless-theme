# Next session — Senseless (Canon v2.19)

Read `CLAUDE.md` → run `scripts/reconcile.sh` → read the Project Instance + State Surface first.
**Machine last used:** MacBook Pro — confirmed 30 Jul. NOTE: hostname can display as `Daniels-MBP.Home` (network-dependent); canon's `Daniels-MacBook-Pro.local` is the same machine.

## Done last session (2026-07-30, Claude Code · Opus 5) — VAT number GB 523 781 682 added site-wide

Commit `6ba73a1`, pushed to `origin/main`, deployed to live `#199324434780`.

**Parity check FIRST, before any edit** (Daniel: live is the most up-to-date; don't lose add-ons). Store verified `senseless-numbing.myshopify.com`. Pulled live, semantic diff vs local: **0 real diffs**. The 104 raw file diffs were 100% Shopify's auto-generated header comment (366 bytes prepended to every `templates/*.json` and `locales/*.json`) — cosmetic, not drift. `config/settings_data.json` byte-identical, so all 6 app embeds intact (Klaviyo, Judge.me ×2, Dondy WhatsApp, Google/YouTube, Inbox).

**Legal basis** (verified against legislation.gov.uk, adversarially checked): **Electronic Commerce (EC Directive) Regulations 2002, reg 6(1)(g)** — a VAT-registered service provider must make its VAT number "easily, directly and permanently accessible" on the website. The duty is **conditional on being registered**: it did not apply before, and does now. The statute prescribes **no location**; a site-wide footer satisfies it.

*Checked and do NOT require a VAT number — don't cite them:* Companies Act 2006 s.82 / Trading Disclosures Regs 2015 (company number + registered office only — already satisfied), Consumer Contracts Regs 2013 (VAT-**inclusive prices**, not a number), Price Marking Order 2004. VAT Regs 1995 reg 13 requires it on a VAT **invoice**, but only B2B — a B2C store has no standing duty to issue one.

**Theme (5 files, deployed):**
- `sections/senseless-footer.liquid:169` — site-wide legal band. **This is the placement that discharges the duty**; the rest is consistency.
- `templates/page.contact.json:140` — statutory details list. Closes the P1 in `build-reports/phase13-full-site-audit.md`.
- `snippets/senseless-structured-data.liquid` — homepage Organization `vatID`.
- `sections/senseless-org-schema.liquid` — about/contact Organization `vatID` + editable `vat_id` setting.
- `templates/page.llms-txt.liquid:33` — machine-readable company record.

**Admin (NOT theme — written via Admin API this session):**
- Native shop policies `CONTACT_INFORMATION` + `TERMS_OF_SERVICE`. **These render at checkout, which the theme cannot reach**, and are a *separate record set* from the `/pages/*` metafields — they drift silently. Worth re-checking whenever company details change.
- Page metafields `policy.prose_policy_body` + `policy.faq` on `terms-conditions`, `prose_policy_body` on `rewards-terms`. The 7 legal pages are metafield-driven, so theme edits alone would not have touched them.
- `scripts/policy-metafields.py` updated to match so the repo's record of policy copy doesn't rot.

**Format:** `GB 523 781 682` visible / `GB523781682` unspaced in JSON-LD (schema.org `vatID` convention). **The divergence is deliberate — don't "align" them in a future audit.**

**Not touched, on purpose:** compliance-locked copy (`senseless-key-facts.liquid:57`, `senseless-credentials.liquid:20` — MHRA/CPSR statements); privacy policy (data-controller identity only; a VAT number has no place in a privacy notice); `page.contact.json:230` Key Facts (same page → would print the number twice); per-variant `Offer.seller` nodes (would repeat 2–3× per PDP).

## Next Work Item

**Shopify admin UI — the one thing left, and it cannot be done by API or theme:**
`Settings → Taxes and duties → Tax regions → United Kingdom → VAT collection → Collect VAT → VAT number: GB523781682 → Collect VAT.`
Nothing in the theme reads this — there is no `shop.vat_number` Liquid object. It drives tax rates and the VAT ID on Shopify-generated invoices.

While in there: check `Settings → General` legal business name reads **Matrix Health Group Ltd**, not "Senseless". Shopify's auto-generated VAT invoice falls back to the store name, which would print a trading name rather than the registered entity.

Optional, convention not law: order-confirmation email (`Settings → Notifications`) and packing slips have no VAT variable — they'd need hardcoding.

### Gotchas earned this session (don't re-derive)

1. **`snippets/senseless-structured-data.liquid` is a reviews-guard file** (carries `product.metafields.reviews.rating`). Editing it blocks the first deploy — that is the guard working correctly, not a bug. Confirm the reviews accessor is untouched, then re-run with `--reviews-changed` and commit the rewritten `reviews-guard.lock`. Post-deploy verify confirmed all 6 live markers (Judge.me ×4, GA4, Google Tag) still render.

2. **Two live-only orphans — deliberately deleted from the repo, left alone on purpose. Do NOT "restore" them:**
   - `blocks/footer-copyright.liquid` — removed in `313f788` ("unused, single source of truth"); bespoke `senseless-footer` replaced it.
   - `templates/page.how-long-numbing-cream-takes-to-work.json` — removed in `64fcfdc` (takes-to-work merge); the URL 301-redirects.
   Stale live leftovers, not content drift. Deleting them from live would be tidier but is destructive and wasn't in scope.

3. **The VAT number passes the UK mod-97-55 checksum** (weighted sum 154 + 82 + 55 = 291 = 97×3), so the format is valid — but that only proves internal consistency, **not** that HMRC issued it to Matrix Health Group Ltd. HMRC's lookup API needs auth (returns `MISSING_CREDENTIALS` unauthenticated); confirm at https://www.gov.uk/check-uk-vat-number if not already done.

4. **`templates/page.contact.json` is theme-editor editable.** If anyone adds VAT copy in admin, the next `deploy.sh` overwrites it. Repo is source of truth.

5. **Locale/template files pulled from live always carry a 366-byte Shopify auto-gen header comment.** Strip it before diffing (regex `^\s*/\*.*?\*/\s*`) or you get ~100 phantom diffs and will wrongly conclude local and live have drifted.

6. **`ShopPolicyInput` has no `id` field** — `shopPolicyUpdate` takes `{type, body}` only. Passing `id` fails with `INVALID_VARIABLE`.
