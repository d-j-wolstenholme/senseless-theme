#!/usr/bin/env node
// Senseless Image Pipeline
// Compresses source images with Sharp and uploads to Shopify Files via GraphQL.
// Adapted from the Totally Numb pipeline (proven 6 May 2026).
//
// Usage:
//   node scripts/image-pipeline.mjs \
//     --source ./assets/images/inbox/source.png \
//     --name senseless-home-hero-products \
//     --type hero \
//     --alt "Descriptive alt text" \
//     --platform shopify \
//     --page home \
//     --section hero

import { promises as fs } from 'fs';
import path from 'path';
import sharp from 'sharp';
import { parseArgs } from 'util';

// OUTPUT POLICY (revised 2026-06-15): photographic assets ship as WebP, NOT PNG.
// Shopify only serves resized/WebP derivatives at the widths the theme requests; the uploaded
// master is still the srcset fallback a crawler downloads and is served wherever no width is asked.
// A PNG master of photographic content is therefore both the wrong format AND ships at full size.
// Policy: photographic -> WebP q~88 (visually lossless), longest edge capped to the largest slot it
// fills (never upscale). QUALITY-FIRST IS OVERRIDING: never lower quality to hit a target — if an
// output exceeds its ceiling at q88 it is FLAGGED for manual review, not degraded. PNG kept only
// where transparency is genuinely needed (logos/icons; those are SVG anyway).
const COMPRESSION_PROFILES = {
  photograph:   { quality: 88, maxWidth: 1600, format: 'webp', ceilingKB: 300 },
  illustration: { quality: 88, maxWidth: 1600, format: 'webp', ceilingKB: 300 },
  hero:         { quality: 88, maxWidth: 2000, format: 'webp', ceilingKB: 400 }, // heroes/bands fill the widest slot
  collection:   { quality: 88, maxWidth: 1600, format: 'webp', ceilingKB: 300 }, // square collection/page heroes
  product:      { quality: 88, maxWidth: 1600, format: 'webp', ceilingKB: 300 }, // square product shots
  thumbnail:    { quality: 82, maxWidth: 800,  format: 'webp', ceilingKB: 80 },
  'icon-badge': { format: 'png' },  // transparency needed
  logo:         { format: 'png' },  // SVG preferred; PNG fallback (transparency)
};

async function processImage(args) {
  const { source, name, type, alt, page, section } = args;

  console.log(`\n📸 Processing: ${source}`);
  console.log(`   Name: ${name}`);
  console.log(`   Type: ${type}`);

  const profile = COMPRESSION_PROFILES[type];
  if (!profile) {
    throw new Error(`Unknown type: ${type}. Valid types: ${Object.keys(COMPRESSION_PROFILES).join(', ')}`);
  }

  const sourceBuffer = await fs.readFile(source);
  const metadata = await sharp(sourceBuffer).metadata();
  console.log(`   Source: ${metadata.width}x${metadata.height}, ${metadata.format}, ${(sourceBuffer.length / 1024).toFixed(1)}KB`);

  let pipeline = sharp(sourceBuffer);

  if (profile.maxWidth && metadata.width > profile.maxWidth) {
    pipeline = pipeline.resize({ width: profile.maxWidth, withoutEnlargement: true });
  }

  let outputExt;
  if (profile.format === 'webp') {
    pipeline = pipeline.webp({ quality: profile.quality });
    outputExt = 'webp';
  } else if (profile.format === 'jpeg') {
    pipeline = pipeline.jpeg({ quality: profile.quality, mozjpeg: true });
    outputExt = 'jpg';
  } else if (profile.format === 'png') {
    pipeline = pipeline.png({ compressionLevel: 9 });
    outputExt = 'png';
  }

  const outputPath = path.join('./assets/images/processed', `${name}.${outputExt}`);
  await pipeline.toFile(outputPath);

  const processedStats = await fs.stat(outputPath);
  const processedKB = processedStats.size / 1024;
  console.log(`   Output: ${outputPath} (${processedKB.toFixed(1)}KB)`);
  if (profile.ceilingKB && processedKB > profile.ceilingKB) {
    console.log(`   ⚠ QUALITY-FLAG: ${processedKB.toFixed(1)}KB exceeds the ${profile.ceilingKB}KB ceiling for '${type}' at q${profile.quality}. Do NOT lower quality to force the target — flag for manual review / consider a tighter crop.`);
  }

  // --local: produce the optimised file only; skip upload, manifest, and the inbox->processed move.
  if (args.local) {
    console.log(`\n✅ Local-only (no upload): ${outputPath}\n`);
    return { localPath: outputPath, sizeKB: processedKB, dimensions: `${metadata.width}x${metadata.height}`, flagged: !!(profile.ceilingKB && processedKB > profile.ceilingKB) };
  }

  // Upload to Shopify Files
  const shopifyResult = await uploadToShopify(outputPath, name, alt);

  // Update manifest
  await updateManifest({
    name,
    type,
    page,
    section,
    alt,
    sourceFile: source,
    processedFile: outputPath,
    cdnUrl: shopifyResult.url,
    shopifyFileId: shopifyResult.id,
    dimensions: `${metadata.width}x${metadata.height}`,
    fileSize: `${(processedStats.size / 1024).toFixed(1)}KB`,
    uploadedAt: new Date().toISOString(),
  });

  // Move source from inbox to processed
  const inboxToProcessed = source.replace('/inbox/', '/processed-sources/');
  await fs.mkdir(path.dirname(inboxToProcessed), { recursive: true });
  await fs.rename(source, inboxToProcessed);

  console.log(`\n✅ Done: ${shopifyResult.url}\n`);
  return shopifyResult;
}

async function uploadToShopify(filePath, name, alt) {
  const SHOPIFY_STORE = process.env.SHOPIFY_STORE;
  const SHOPIFY_ACCESS_TOKEN = process.env.SHOPIFY_ACCESS_TOKEN;

  if (!SHOPIFY_STORE || !SHOPIFY_ACCESS_TOKEN) {
    throw new Error('SHOPIFY_STORE and SHOPIFY_ACCESS_TOKEN must be set in .env');
  }

  const apiUrl = `https://${SHOPIFY_STORE}/admin/api/2024-10/graphql.json`;
  const fileBuffer = await fs.readFile(filePath);
  const filename = path.basename(filePath);

  // 1. Stage the upload
  const stagedUploadMutation = `
    mutation stagedUploadsCreate($input: [StagedUploadInput!]!) {
      stagedUploadsCreate(input: $input) {
        stagedTargets {
          url
          resourceUrl
          parameters { name value }
        }
        userErrors { field message }
      }
    }
  `;

  const stagedResponse = await fetch(apiUrl, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-Shopify-Access-Token': SHOPIFY_ACCESS_TOKEN,
    },
    body: JSON.stringify({
      query: stagedUploadMutation,
      variables: {
        input: [{
          filename,
          mimeType: filename.endsWith('.png') ? 'image/png' : 'image/jpeg',
          fileSize: String(fileBuffer.length),
          httpMethod: 'POST',
          resource: 'FILE',
        }],
      },
    }),
  });

  const stagedData = await stagedResponse.json();
  const target = stagedData.data.stagedUploadsCreate.stagedTargets[0];

  // 2. Upload to staged URL
  const formData = new FormData();
  for (const param of target.parameters) {
    formData.append(param.name, param.value);
  }
  formData.append('file', new Blob([fileBuffer]), filename);

  const uploadResponse = await fetch(target.url, {
    method: 'POST',
    body: formData,
  });

  if (!uploadResponse.ok) {
    throw new Error(`Upload failed: ${uploadResponse.statusText}`);
  }

  // 3. Create file with alt text
  const fileCreateMutation = `
    mutation fileCreate($files: [FileCreateInput!]!) {
      fileCreate(files: $files) {
        files {
          id
          fileStatus
          ... on MediaImage {
            image { url }
          }
        }
        userErrors { field message }
      }
    }
  `;

  const createResponse = await fetch(apiUrl, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-Shopify-Access-Token': SHOPIFY_ACCESS_TOKEN,
    },
    body: JSON.stringify({
      query: fileCreateMutation,
      variables: {
        files: [{
          originalSource: target.resourceUrl,
          alt,
        }],
      },
    }),
  });

  const createData = await createResponse.json();
  const file = createData.data.fileCreate.files[0];

  // 4. Poll for READY status
  let attempts = 0;
  while (file.fileStatus !== 'READY' && attempts < 10) {
    await new Promise(r => setTimeout(r, 1000));
    const statusResponse = await fetch(apiUrl, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-Shopify-Access-Token': SHOPIFY_ACCESS_TOKEN,
      },
      body: JSON.stringify({
        query: `query { node(id: "${file.id}") { ... on MediaImage { fileStatus image { url } } } }`,
      }),
    });
    const statusData = await statusResponse.json();
    if (statusData.data.node.fileStatus === 'READY') {
      return {
        id: file.id,
        url: statusData.data.node.image.url,
      };
    }
    attempts++;
  }

  throw new Error('File did not reach READY status within 10 seconds');
}

async function updateManifest(entry) {
  const manifestPath = './image-manifest.json';
  const manifest = JSON.parse(await fs.readFile(manifestPath, 'utf-8'));
  manifest.images.push(entry);
  await fs.writeFile(manifestPath, JSON.stringify(manifest, null, 2));
}

async function main() {
  const { values } = parseArgs({
    options: {
      source: { type: 'string' },
      name: { type: 'string' },
      type: { type: 'string' },
      alt: { type: 'string' },
      platform: { type: 'string', default: 'shopify' },
      page: { type: 'string' },
      section: { type: 'string' },
      local: { type: 'boolean', default: false }, // produce optimised file only; no upload/manifest/move
    },
  });

  if (!values.source || !values.name || !values.type || (!values.alt && !values.local)) {
    console.error('Usage: node scripts/image-pipeline.mjs --source <path> --name <name> --type <type> --alt <alt> [--page <page>] [--section <section>] [--local]');
    process.exit(1);
  }

  await processImage(values);
}

main().catch(err => {
  console.error('❌ Pipeline failed:', err.message);
  process.exit(1);
});
