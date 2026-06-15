# Senseless — STATE (repo mirror)

Repo-side mirror of the Notion 📍 STATE page (`37358bc375ea81ac9451f6b07bdf4e6e`). Newest update at top.
Created 2026-06-15 (the mirror was previously missing — see DECISIONS-LOG / audit 2026-06-12).

Canonical: live store `senseless-numbing.myshopify.com` (domain `senseless.uk`), live theme **Senseless Dev #199324434780**, branch `main`. Storefront password ON (pre-public).

---

## 2026-06-15 — Collection hero images (6: format + strength collections)

New collection-hero photography for the 3 format (numbing-cream/gel/spray) + 3 strength (clinical/advanced/professional) collections. Processed (Sharp, 1:1 white-bg master PNG + WebP + 400/800/1200 srcset; originals in `~/senseless/processed-sources/batch-collection-heroes/`) → uploaded to Shopify Files (staged PUT → fileCreate, all READY).

**Both layers updated per collection** (the gotcha — `collection.image` cleared first, then set):
- **`collection.image`** (API) cleared → set with Comfort alts — feeds the **homepage strength tier cards** + collection thumbnails.
- **Template hero `image` setting** (`shopify://shop_images/senseless-<x>-collection-hero.png`) + `image_alt` → Comfort alts — the on-page collection hero renders from the template, not `collection.image`.

`image-manifest.json`: 6 new `collection-hero` records; 7 prior collection records marked superseded. Commit `7de0643`; theme deployed (6 collection templates). theme-check 0. Tier-card data layer confirmed (clinical/advanced/professional `collection.image` set); live visual spot-check pending (storefront password ON).

## 2026-06-15 — Comfort vs Numbing Phase 3 (GREY-SEO ruled set applied + deployed)

Owner ruled the held GREY-SEO set; applied + **deployed live** (commit `b23ccf8`, theme push):
- **6 PDP short-descriptions** → "[strength]-strength **Comfort Cream/Gel/Spray**" (natural brand copy).
- **Bundle kit-contents ×2** → "**Comfort Cream, Comfort Gel and Comfort Spray**" (legal-hold "Numbing reduces discomfort" left verbatim).
- **image-manifest.json ×3** single-product lifestyle alts → Comfort (split rule); range / multi-format / kit records KEPT as category descriptors.

**KEEP (deliberate, unchanged):** 8 PDP SEO `title_tag`s + senseless-vs-ametop title (**SEO-RISK** — category keyword in the meta title, compliance-cleared as search-category use); STATE.md history.

**Migration status:** Comfort-vs-Numbing now complete across the CHANGE + GREY-SEO sets. Only the SEO-RISK meta-title surfaces remain as intentional "Numbing" (category-keyword) by design. theme-check 0.

## 2026-06-15 — Comfort vs Numbing naming (canonical rule + Phase 2 applied)

Locked the rule: **"Comfort [format]"** (Comfort Cream/Gel/Spray) = Senseless **product brand name**; **"Numbing [format]"** = **SEO category descriptor** only. (COMPLIANCE.md "Product naming" sub-rule + BRAND.md + DECISIONS-LOG.md 2026-06-15.)

Full read-only audit (theme repo + live Admin): **290 hits — CHANGE 12 · KEEP 247 · GREY 31**; key finding = the store never used "Numbing [format]" as a product brand name (titles are "[Tier] Strength [Format]"), so almost everything is legitimate category/SEO. SEO-protection layer cleared all 12 CHANGE; split the 31 GREY into 9 SEO-RISK + 22 GREY-SEO (all held).

**Phase 2 applied (SEO-cleared CHANGE only):** 3 cream PDP product-media alts → "Senseless [Tier] Strength **Comfort Cream**" (productUpdateMedia) + 9 `image-manifest.json` cream mirror records. Gel/spray live alts already used "Comfort"; JSON-LD name derives from title (clean). Commit `270c696`; **no theme files changed → no theme deploy.**

**HELD for owner ruling (no change):** 8 PDP SEO `title_tag`s + senseless-vs-ametop title (**SEO-RISK** — category keyword in the meta title; if adding Comfort, use the *additive* pattern, don't replace); 6 PDP short-descriptions, 2 bundle kit-contents, 14 manifest range/lifestyle records (**GREY-SEO**). Audit + SEO layer filed to Notion Build Reports hub.

## 2026-06-15 — Product imagery refresh (all 10 single-format PDPs)

Replaced the featured image on all 10 single-product PDPs (3 cream / 3 gel / 3 spray / 1 foam) with the new `batch-all-formats` pack shots. Bundles NOT touched (no new art supplied).

- **Processed** 10 sources (1254² PNG) → white-bg 1:1 master PNG (uploaded) + WebP master + 400/800/1200 WebP srcset, kept in `~/senseless/processed/`; originals in `~/senseless/processed-sources/batch-all-formats/`. (Sharp 0.33.5.)
- **Uploaded** to Shopify Files (stagedUploadsCreate PUT → fileCreate, all READY) via the authenticated Shopify MCP — the `.env` Admin token (`shpca_…`) is DEAD (401) and needs rotating.
- **Swapped** media per product: deleted all prior product media (creams had 3 each: white/warm/plain; gel/spray/foam 1 each) + created new featured image with alt, atomically (productDeleteMedia + productCreateMedia, 0 errors). Each PDP now has exactly 1 featured media (verified READY via Admin API).
- `image_placeholder` metafield: none were `true` → nothing to clear.
- Collections numbing-cream / -gel / -spray: trio `collection.image` intact, untouched (STEP 6 status-only).
- `image-manifest.json` updated with the 10 new CDN URLs + Files GIDs + assignments.
- No theme files changed → no theme deploy; images are live via Admin API. theme-check 0 errors.

**Open flags for Daniel:** (1) cream renders are plain-white-tube/text-only vs the new purple-asterisk X-pattern label on spray/gel/foam — formats read inconsistently; (2) gel pack label "Aesthetics Comfort Gel" ≠ store name "Numbing Gel"; (3) foam pack label "Aftercare Foam Cleanser" ≠ canonical "Foaming Cleanser"; (4) bundles excluded this pass; (5) `.env` Admin token expired — rotate; (6) live render not visually spot-checked (storefront password on) — verify in admin/preview.
