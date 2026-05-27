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

const COMPRESSION_PROFILES = {
  photograph: { quality: 82, maxWidth: 2048, format: 'jpeg' },
  illustration: { quality: 85, maxWidth: 2048, format: 'jpeg' },
  hero: { quality: 87, maxWidth: 1920, format: 'jpeg' },
  thumbnail: { quality: 72, maxWidth: 800, format: 'jpeg' },
  'icon-badge': { format: 'png' },
  logo: { format: 'png' }, // SVG preferred but PNG fallback
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
  if (profile.format === 'jpeg') {
    pipeline = pipeline.jpeg({ quality: profile.quality, mozjpeg: true });
    outputExt = 'jpg';
  } else if (profile.format === 'png') {
    pipeline = pipeline.png({ compressionLevel: 9 });
    outputExt = 'png';
  }

  const outputPath = path.join('./assets/images/processed', `${name}.${outputExt}`);
  await pipeline.toFile(outputPath);

  const processedStats = await fs.stat(outputPath);
  console.log(`   Output: ${outputPath} (${(processedStats.size / 1024).toFixed(1)}KB)`);

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
    },
  });

  if (!values.source || !values.name || !values.type || !values.alt) {
    console.error('Usage: node scripts/image-pipeline.mjs --source <path> --name <name> --type <type> --alt <alt> --page <page> --section <section>');
    process.exit(1);
  }

  await processImage(values);
}

main().catch(err => {
  console.error('❌ Pipeline failed:', err.message);
  process.exit(1);
});
