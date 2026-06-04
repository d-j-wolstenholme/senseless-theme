# Phase 12 — quick link fixes

**Date:** 2026-06-04 (BST) · **Branch:** dev · **Theme:** `#199324434780` · **Commit:** `b877c48`. From the linking audit (`7f0b077`). No behaviour changes.

## 1. Repoint 3 stale 301 links (at source) — now resolve 200 DIRECT
- Homepage "How Senseless works": `/pages/how-it-works` → **`/pages/the-senseless-system`**
- `collection.aesthetic-numbing-cream`: `/pages/how-it-works` → **`/pages/the-senseless-system`**
- `best-emla-alternative-uk` "how long does numbing cream last": `/pages/how-long-numbing-cream-lasts` → **`/pages/using-numbing-cream`**
- Tidied the latent `/pages/how-it-works` in `product.json` (unused default template).
Verified: both targets resolve **200 direct** (maxRedirects:0); zero stale links remain on the 3 sources.

## 2. Thin over-repeated Selector anchors (SEO)
- `does-it-hurt-by-treatment`: "Use the Senseless Selector" **6 → 1** (kept the lip-filler section; the page also has its dedicated Selector callout).
- `using-numbing-cream`: choosing.l1 relabelled "The Senseless System" → one "Make your Selection" CTA (route.r1) = **2 → 1**.
- `faq`: q3 answer rephrased to "the Senseless System" → one "Make your Selection" CTA (route.r1) = **2 → 1**.
Verified live: each anchor now ×1.

## 3. Orphan inbounds
- `best-numbing-cream` "honest" body now links **EMLA** + **Ametop** comparison pages contextually ("pharmacy products built for medical procedures (like EMLA or Ametop)"). Each previously-orphan commercial page now has one inbound. Injectable-clean.

## Verify
theme-check **0 errors**; injectable-clean grep (8 templates) clean; live render confirmed all three categories.

## HOLD
