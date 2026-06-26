#!/usr/bin/env node
// Senseless — OpenAI image generator (gpt-image-1)
// Generates an image from a prompt and drops the PNG in assets/images/inbox/, ready for the
// Sharp pipeline (scripts/image-pipeline.mjs) which compresses + uploads it to Shopify Files.
//
// Requires OPENAI_API_KEY in .env (or the environment). The key is read locally and never logged.
// IMPORTANT: rotate any key that has been pasted into chat / shared — treat shared keys as burned.
//
// Usage:
//   node scripts/openai-image-gen.mjs \
//     --prompt "A single Senseless-style apothecary tube on a marble ledge" \
//     --name   senseless-about-shop \
//     --size   1024x1024 \          # 1024x1024 (square) | 1536x1024 (landscape) | 1024x1536 (portrait)
//     --quality high \              # low | medium | high
//     --brand                       # append the Senseless brand-style suffix (recommended)
//
// gpt-image-1 returns PNG (base64). After generating, integrate via the existing pipeline, e.g.:
//   node scripts/image-pipeline.mjs --source ./assets/images/inbox/senseless-about-shop.png \
//     --name senseless-about-shop --type illustration \
//     --alt "Editorial Senseless-style still life" --platform shopify --page about --section shop
//
// NOTE (brand fidelity): AI cannot reproduce the REAL Senseless packaging — never use it for actual
// product shots (use real photography). Use it for abstract/editorial/brand-mark/texture imagery only.

import { promises as fs } from 'fs';
import { parseArgs } from 'util';

const BRAND_STYLE =
  ' Editorial, premium, calm aesthetic-clinic mood. Warm off-white (#f7f7f5) background, soft natural' +
  ' directional light, generous negative space, restrained neutral palette with a single muted purple' +
  ' (#6B3FA0) accent. Centred composition. No text, no words, no logos, no watermarks, no labels.' +
  ' No real product packaging. Not a medical/clinical procedure scene.';

const { values } = parseArgs({
  options: {
    prompt:  { type: 'string' },
    name:    { type: 'string' },
    size:    { type: 'string', default: '1024x1024' },
    quality: { type: 'string', default: 'high' },
    brand:   { type: 'boolean', default: false },
  },
});

if (!values.prompt || !values.name) {
  console.error('Usage: node scripts/openai-image-gen.mjs --prompt "..." --name senseless-x [--size 1024x1024] [--quality high] [--brand]');
  process.exit(1);
}

// Resolve API key: environment first, then parse .env (gitignored).
let key = process.env.OPENAI_API_KEY;
if (!key) {
  try {
    const env = await fs.readFile('.env', 'utf8');
    const m = env.match(/^\s*OPENAI_API_KEY\s*=\s*(.+)$/m);
    if (m) key = m[1].trim().replace(/^["']|["']$/g, '');
  } catch { /* no .env */ }
}
if (!key) {
  console.error('OPENAI_API_KEY not found in environment or .env. Add a (rotated) key to .env and retry.');
  process.exit(1);
}

const prompt = values.brand ? `${values.prompt}.${BRAND_STYLE}` : values.prompt;
const outPath = `assets/images/inbox/${values.name}.png`;

console.log(`\n🎨 Generating "${values.name}"  (size ${values.size}, quality ${values.quality}, brand-style ${values.brand ? 'on' : 'off'})`);

const res = await fetch('https://api.openai.com/v1/images/generations', {
  method: 'POST',
  headers: { Authorization: `Bearer ${key}`, 'Content-Type': 'application/json' },
  body: JSON.stringify({ model: 'gpt-image-1', prompt, size: values.size, quality: values.quality, n: 1 }),
});

if (!res.ok) {
  console.error(`❌ OpenAI API error ${res.status}: ${(await res.text()).slice(0, 500)}`);
  process.exit(1);
}

const data = await res.json();
const b64 = data?.data?.[0]?.b64_json;
if (!b64) {
  console.error(`❌ No image in response: ${JSON.stringify(data).slice(0, 300)}`);
  process.exit(1);
}

await fs.mkdir('assets/images/inbox', { recursive: true });
await fs.writeFile(outPath, Buffer.from(b64, 'base64'));
console.log(`✅ Saved ${outPath}`);
console.log(`   Next: node scripts/image-pipeline.mjs --source ./${outPath} --name ${values.name} --type illustration --alt "<compliant alt>" --platform shopify --page <page> --section <section>\n`);
