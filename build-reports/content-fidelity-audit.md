# Content-Fidelity Audit (READ-ONLY)

- **Machine:** MacBook Pro · **Date:** 2026-06-01 (BST) · **Branch:** `dev` @ `e7e20f0`
- **Mode:** Read-only. No theme writes, nothing fixed. Report only.
- **Method:** Diffed the **section defaults in `templates/*.json`** (page bodies are empty by design) against **Production Copy v2** in the Notion Master Page Database (`86948dad77bd4b1cbe4bf994b022fee5`), plus a locked-standards spot-check. 29 senseless-composed templates audited via 5 parallel readers; cross-cutting claims re-verified directly against the code.

> **Scope of truth:** the built copy lives in the section default settings + the senseless section Liquid (some lines are rendered by the section, not stored in the template JSON). Findings below reflect what actually renders, not just the JSON.

---

## ⚠️ Audit caveats — corrected false positives

The per-page readers audited template JSON in isolation and produced three **systematic false positives**. Verified directly and corrected here:

1. **"Key Facts closing line missing" — FALSE.** `sections/senseless-key-facts.liquid:55` **hardcodes** the verbatim line `UK cosmetic product, by Matrix Health Group Ltd. Not a medicine.` and always renders it (non-editable). It is **present + verbatim** on all **14** templates that include the section: product, numbing-cream/gel/spray, choosing-your-strength, choosing-your-format, how-it-works, how-long-…-takes-to-work, how-long-…-lasts, does-numbing-cream-work, best-numbing-cream, strongest-numbing-cream, best-emla-alternative-uk, senseless-vs-ametop. It is **genuinely absent only where the section isn't wired** (see Real finding #5).
2. **"Trust bar should say Cruelty-free" — FALSE.** The trust bar follows the **locked 2026-05-29 decision** (UK formulated · Cosmetic product · CPSR assessed · Made for aesthetics); "cruelty-free" was dropped (MHG blocker). Comparing to v2's "cruelty-free" compares against superseded copy.
3. **"Homepage should say four formats" — FALSE.** Built "three formats" (cream/gel/spray) is **correct**; v2's "four formats" predates the range correction (the 4th was the aftercare cleanser, not a numbing format).

One more reversal: **Lip Fillers grid** — Notion v2 lists "Clinical gel 35ml" (a range-correction violation; no Clinical gel exists). The **built** template correctly uses Advanced Gel — **built is right, Notion v2 is stale.**

---

## Cross-cutting REAL findings (priority order)

1. **Banned tier-descriptor copy (systematic).** Built tier cards still use the retired v1 wording the locked banned-words list now prohibits — **"The everyday formula" / "the everyday Senseless" / "considered upgrade"** — in **8 templates**: `index`, `page.choosing-your-strength`, `page.best-numbing-cream`, `page.strongest-numbing-cream`, `page.best-emla-alternative-uk`, `page.senseless-vs-ametop`, `collection.numbing-cream`, `collection.aesthetic-numbing-cream` (and likely the FAQ tier descriptions). **Fix:** rewrite to compliant tier language ("The Senseless default" / "A higher-strength formula" etc.). *Note: "flagship" and "concentration" do NOT appear as visible copy — "flagship" is only a boolean styling key; "concentrated" (adjective) is used, which is not the banned "concentration".*
2. **FAQ section absent where v2 specifies it.** `index` (homepage), `page.choosing-your-strength`, `page.choosing-your-format` have **no `senseless-faq-accordion`** → no FAQ content and **no FAQPage schema**, though v2 specs FAQ on the two guides. **Fix:** add FAQ blocks (incl. "Is this a medicine? No.") to the two guides; decide on homepage.
3. **"Is this a medicine? No." not a standalone FAQ** on `page.best-emla-alternative-uk` and `page.senseless-vs-ametop` — they carry comparison FAQs only. **Fix:** add the explicit medicine-Q item.
4. **Injectable-clean risk on an ad-facing surface.** `collection.numbing-spray` surfaces an **Injections** procedure card/link. Spray is an ad-facing format collection → Google-Ads injectable-clean risk. **Fix:** remove/repoint the Injections card on the format collections. (The aesthetic hub legitimately links injectable collections as the SEO umbrella; the 3 injectable collections remain unlinked + under noindex/redirect review.)
5. **Key Facts coverage gap.** The GEO build wired `senseless-key-facts` into 14 templates; it is **absent** on `index`, `aesthetic-numbing-cream`, the **7 procedure collections**, `about`, `faq`, `contact`, `trade`, `how-to-apply`, `foaming-cleanser`. Where v2 specs a GEO Key Facts block (procedure collections, homepage), that's a coverage gap. **Fix:** wire key-facts into the procedure collections + homepage if required.
6. **Gel/spray range-rework pending (not scored).** Built `collection.numbing-gel` and `collection.numbing-spray` still render the **old two-strength model** (Advanced + Professional only). Per the 31 May reversal the range is now **all three strengths**. Flagged as **range-rework pending** — built copy needs Clinical gel/spray added; not scored against (possibly-stale) v2.

---

## Per-page table

Legend — Matches v2: ✅ yes · 🟡 partial · ❌ no · ⏸ N/A (range-rework). KF line = hardcoded verbatim closing line present (✓ where key-facts section is wired).

### Homepage, system guides
| Template | Matches v2 | Deviations | Standards flags | Fix needed |
|---|---|---|---|---|
| `index.json` (Homepage) | 🟡 | Tier card copy uses retired wording; no "By procedure" non-injectable card row (v2 specs it); subhead "three formats" (correct, v2 stale). KF section **not** wired. | **Banned: "everyday", "considered upgrade"**; **no FAQ/FAQPage**; KF line absent (no KF section); verify trust bar = locked 4-signal set (one read saw only 3) | Rewrite tier copy; add By-procedure (non-injectable) row; consider KF + FAQ |
| `page.choosing-your-strength.json` | 🟡 | Professional heading = "Developed with practitioners" vs v2 "The flagship" (built **avoids** banned "flagship" → keep built); rest matches | **Banned: "The everyday formula", "considered upgrade"** (tier headings); **no FAQ section** (v2 specs it); KF line ✓ (present) | Rewrite tier headings; add FAQ block |
| `page.choosing-your-format.json` | 🟡 | Body matches v2 closely; bold lead-ins added (minor) | **No FAQ section** (v2 specs 3 FAQs); KF line ✓ | Add FAQ block |
| `page.how-it-works.json` | ✅ | Full match incl. FAQ (5 items) | KF line ✓; FAQ ✓ | none |

### Guides (how/does/apply) + about
| Template | Matches v2 | Deviations | Standards flags | Fix needed |
|---|---|---|---|---|
| `page.how-long-numbing-cream-takes-to-work.json` | 🟡 | Hero subhead compressed vs v2 (drops "anyone giving you a specific number…" beat) | KF line ✓; FAQ ✓ ("Is this a medicine?" present); no banned words | Optional: restore fuller subhead |
| `page.how-long-numbing-cream-lasts.json` | 🟡 | Hero subhead compressed vs v2 | KF line ✓; FAQ ✓; clean | Optional: restore fuller subhead |
| `page.does-numbing-cream-work.json` | 🟡 | Hero subhead minor compression; failure-modes section present ✓ | KF line ✓; FAQ ✓; clean | Optional |
| `page.how-to-apply-numbing-cream.json` | ✅ | Instructional HowTo; no KF block (correct for type) | FAQ ✓; clean | none |
| `page.about.json` | ❓ | v2 row not retrieved (Notion rate-limit) | No banned words; cosmetic positioning ✓; no KF/FAQ (acceptable for brand page) | Re-check v2 when available |

### Landing / comparison + supporting
| Template | Matches v2 | Deviations | Standards flags | Fix needed |
|---|---|---|---|---|
| `page.best-numbing-cream.json` | 🟡 | Hero/body match | **Banned: "everyday"** (×2, tier/sub-label); KF line ✓; FAQ ✓ incl. medicine-Q | Rewrite "everyday" |
| `page.strongest-numbing-cream.json` | 🟡 | Matches intent | **Banned: "considered upgrade"** (Advanced tier); KF line ✓; FAQ ✓ | Rewrite "upgrade" |
| `page.best-emla-alternative-uk.json` | 🟡 | Category-distinction framing correct (no efficacy comparison) | **Banned: "considered upgrade"**; **standalone "Is this a medicine? No." FAQ missing**; KF line ✓ | Rewrite "upgrade"; add medicine-Q |
| `page.senseless-vs-ametop.json` | 🟡 | Category-distinction framing correct | **Banned: "considered upgrade"**; **medicine-Q FAQ missing**; KF line ✓ | Rewrite "upgrade"; add medicine-Q |
| `page.faq.json` | 🟡 | 6-section FAQ structure matches | **Banned: "everyday Senseless"** in tier descriptions (per reader); medicine-Q ✓; FAQ ✓ | Rewrite "everyday" |
| `page.contact.json` | ✅ | Contact/MHG company info; no product copy | clean (N/A product standards) | none |
| `page.trade.json` | ✅ | B2B; trade FAQ present | clean | none |

### Format + hub collections, products
| Template | Matches v2 | Deviations | Standards flags | Fix needed |
|---|---|---|---|---|
| `collection.numbing-cream.json` | 🟡 | Professional card terser than v2; formats-section angle differs (minor) | **Banned: "everyday Senseless cream"** (Clinical card); KF line ✓ | Rewrite "everyday" |
| `collection.numbing-gel.json` | ⏸ range-rework | Built shows **two-strength** (Adv+Pro); v2 "when_gel" section absent | KF line ✓; clean | Range-rework to 3 strengths (pending) |
| `collection.numbing-spray.json` | ⏸ range-rework | Built shows **two-strength**; **Injections procedure card present** | **Injectable-clean risk (Injections on ad-facing format collection)**; KF line ✓ | Remove Injections card; range-rework (pending) |
| `collection.aesthetic-numbing-cream.json` | ✅ (hub) | Full 7-procedure umbrella (injectable links OK here — SEO umbrella) | **Banned: tier "everyday"**; **no KF section** (gap if v2 wants it) | Rewrite "everyday"; consider KF |
| `product.json` (shared SKU) | 🟡 | Generic range-level copy; KF generic (per-SKU pending) | KF line ✓; clean | Per-SKU facts via metafield (carryover) |
| `product.foaming-cleanser.json` | ✅ | System-completion framing matches v2 | Outside 10-SKU numbing range (aftercare/11th SKU — confirm); "antibacterial" claim-safe; no KF section | Confirm range intent |

### Procedure collections (non-injectable)
| Template | Matches v2 | Deviations | Standards flags | Fix needed |
|---|---|---|---|---|
| `collection.numbing-cream-for-microneedling.json` | ✅ | H1 "more intensive" vs v2 "deeper" (minor); grid uses size-agnostic variant model vs v2 per-size cards | FAQ ✓ medicine-Q; no KF section; clean | Optional H1 align; KF if v2 wants |
| `collection.numbing-cream-for-laser-treatment.json` | ✅ | H1 broader vs v2 format-led (minor); size-agnostic grid | FAQ ✓; no KF section; clean | Optional |
| `collection.numbing-cream-for-semi-permanent-makeup.json` | ✅ | "sittings" terminology correct; size-agnostic grid | FAQ ✓; no KF section; clean | Optional |
| `collection.numbing-cream-for-waxing.json` | ✅ | Spray-leading correct; H1 category vs v2 format-led (minor) | FAQ ✓; no KF section; clean | Optional |

### Injectable collections (built, **unlinked**, under noindex/redirect review)
| Template | Matches v2 | Deviations | Standards flags | Fix needed |
|---|---|---|---|---|
| `collection.numbing-cream-for-botox.json` | ✅ | Anti-upsell beat present ("Professional is overkill… we say so plainly"); "Botox optional, not required" ✓ | INJECTABLE SURFACE — unlinked; FAQ ✓ medicine-Q; clean | Resolve noindex/redirect (policy) |
| `collection.numbing-cream-for-lip-fillers.json` | 🟡 | Built grid = Advanced Gel (**correct**); **Notion v2 lists "Clinical gel" — v2 is stale/wrong** | INJECTABLE SURFACE — unlinked; FAQ ✓; clean | Fix Notion v2 (not the build); resolve noindex/redirect |
| `collection.numbing-cream-for-injections.json` | ✅ | Sub-procedure routing + medical-injection decline present | INJECTABLE SURFACE — unlinked; FAQ ✓; minor: spray grid lacks "100ml" size note | Resolve noindex/redirect |

---

## Schema spot-check
- **FAQPage** renders wherever `senseless-faq-accordion` is present — ✅ on the guides/landings/collections that have it; ❌ on homepage, choosing-your-strength, choosing-your-format (no FAQ section).
- **Product/Offer, CollectionPage/ItemList, BreadcrumbList** are emitted globally by `snippets/senseless-structured-data.liquid` (PR #2) on product/collection/page types — not per-template; **inert for Product/Offer until real products exist** (£TBC/0 stock).

## Priority fix list (for a future WRITE session — not done here)
1. **Rewrite banned tier-descriptor copy** ("everyday"/"considered upgrade") across the 8 templates → compliant tier language. *(highest volume)*
2. **Add FAQ blocks** (+ medicine-Q) to choosing-your-strength, choosing-your-format; add standalone medicine-Q FAQ to best-emla & senseless-vs-ametop.
3. **Remove the Injections card** from `collection.numbing-spray` (ad-facing injectable-clean).
4. **Gel/spray range-rework** to all-three-strengths (gel + spray collections + any dependent copy).
5. **Key Facts coverage** — wire into procedure collections + homepage if v2 requires.
6. **Correct Notion v2** Lip-Fillers grid (remove "Clinical gel") — the build is already right.
7. Optional: restore fuller hero subheads on the two "how long" guides; align procedure H1 phrasing.

## Notes
- About-page v2 not retrieved (Notion rate-limit during the run) — re-pull to finish that row.
- Trust-bar 4-signal set: confirm every page instance carries the locked 4 (one homepage read saw 3).
