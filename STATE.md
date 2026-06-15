# Senseless — STATE (repo mirror)

Repo-side mirror of the Notion 📍 STATE page (`37358bc375ea81ac9451f6b07bdf4e6e`). Newest update at top.
Created 2026-06-15 (the mirror was previously missing — see DECISIONS-LOG / audit 2026-06-12).

Canonical: live store `senseless-numbing.myshopify.com` (domain `senseless.uk`), live theme **Senseless Dev #199324434780**, branch `main`. Storefront password ON (pre-public).

---

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
