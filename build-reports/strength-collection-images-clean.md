# Strength collection.image — swapped to clean range shots

**Date:** 2026-06-07 (BST) · **Branch:** dev · **Theme:** Senseless Dev `#199324434780` (UNPUBLISHED). theme-check **0 errors**. Commits `918dace`, `8ab1edc`.

Correction to step 3 of the strength-collections build: the interim **defective bundle shots** (cleanser carried a strength word) are replaced on the strength surfaces with the **3 clean 3-product range shots** from the inbox (cream/gel/spray, "[TIER] STRENGTH", **no cleanser**, marble, 1:1) — verified clean on view before assigning.

## Done
- Processed + uploaded `senseless-{clinical,advanced,professional}-strength-collection` (1:1, ~213–225KB); manifest updated; originals kept.
- Set each strength **`collection.image`** to its clean shot (clear-then-set — the API silently no-ops a replace when an image already exists, so the old bundle image was cleared first).
- Set the **hero template image** on `collection.{clinical,advanced,professional}.json` to the same clean shots so the collection heroes display them (were text-only).

## Verified (desktop + mobile)
- **Homepage strength cards** → clean shots (`senseless-<tier>-strength-collection.jpg`). ✅
- **Collection heroes** (`/collections/clinical|advanced|professional`) → clean shots. ✅
- theme-check 0; theme unpublished.

## Unchanged (still interim — awaiting the kit re-render)
- **Bundle PDPs** (×4) + **mega-menu Featured card** (Pro Ultimate) remain on the interim 4-product bundle shots with the defective cleanser label. Those still need the strength-less-cleanser kit re-render; the strength collections + homepage strength cards are now **fully clean, no interim, ungated**.

## HOLD
Strength surfaces fully clean. Bundle/mega kit shots still outstanding.
