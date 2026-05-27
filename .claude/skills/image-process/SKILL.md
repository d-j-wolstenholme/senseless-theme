---
name: image-process
description: Use this skill when the user has placed a raw image in assets/images/inbox/ and wants it processed and integrated. Runs the full image pipeline — names the file per convention, classifies the image type (photograph/illustration/hero/thumbnail/icon-badge/logo), compresses with Sharp at type-appropriate settings, uploads to Shopify Files via GraphQL staged upload, sets alt text, appends to image-manifest.json, and updates the relevant template to reference the new CDN URL. Trigger phrases include "process this image", "run the image pipeline", "upload [filename] to Shopify".
---

# Image Process

## When to Use

- User has dropped a source file in `assets/images/inbox/`
- A new section or page needs imagery uploaded
- /build-page workflow reaches an image step

## Inputs

- **Source file path** (required) — in `assets/images/inbox/`
- **Name** (required) — `senseless-[page-or-context]-[descriptor]`
- **Type** (required) — photograph / illustration / hero / thumbnail / icon-badge / logo
- **Alt text** (required) — compliant, descriptive
- **Page** (required) — page handle for the manifest entry
- **Section** (required) — section identifier

## Process

1. Read `image-manifest.json` to confirm name isn't already used
2. Run `compliance-check` on the alt text
3. Run the pipeline script:
   ```
   node scripts/image-pipeline.mjs \
     --source ./assets/images/inbox/[source] \
     --name [name] \
     --type [type] \
     --alt "[alt text]" \
     --platform shopify \
     --page [page] \
     --section [section]
   ```
4. The script: detects format → compresses with Sharp at type-appropriate settings → uploads via stagedUploadsCreate → sets alt during fileCreate → polls READY → returns CDN URL
5. Append entry to `image-manifest.json`
6. Move source file from `inbox/` to `processed/`
7. If a section file needs the image, update the relevant Liquid file to reference the new CDN URL

## Outputs

- Compressed file in `assets/images/processed/`
- Shopify Files CDN URL
- Updated `image-manifest.json` entry
- Updated section file (if applicable)
- Build report line: "Processed image [name] — [CDN URL]"

## Compression Settings

| Type | Output | Quality | Max Width | Target Size |
|---|---|---|---|---|
| photograph | JPEG (mozjpeg) | 82% | 2048px | <200KB |
| illustration | JPEG (mozjpeg) | 85% | 2048px | <200KB |
| hero | JPEG (mozjpeg) | 87% | 1920px | <200KB |
| thumbnail | JPEG (mozjpeg) | 72% | 800px | <50KB |
| icon-badge | PNG | Lossless | Source | As small as possible |
| logo | SVG preferred, PNG fallback | Lossless | Source | As small as possible |

## Constraints

- Upload JPEG to Shopify (CDN auto-converts to WebP/AVIF per browser). Don't upload WebP yourself.
- Alt text must pass compliance-check
- Never delete from `processed/` — it's the audit trail
- Mobile art direction variants append `-mobile` and are processed as separate runs
