// Offline render harness: renders snippets/senseless-structured-data.liquid (ORIG and DRAFT) with liquidjs
// against product data mocked from the live /products/<h>.js payloads captured 23 Sep 2026, then:
//   1. fidelity: ORIG render vs the live served ld+json bytes (same URL)
//   2. identity: DRAFT render vs ORIG render, per URL
//   3. validity: JSON.parse of every DRAFT render
// Shopify-only filters (json, image_url, asset_url) are emulated to Shopify's observed output.
import { Liquid } from 'liquidjs';
import fs from 'fs';
import path from 'path';

const HERE = path.dirname(new URL(import.meta.url).pathname);
// Paths (repo layout: docs/specs/productgroup-phase1/harness/). Override with env vars if needed.
const REPO = process.env.PG_REPO || path.resolve(HERE, '../../../..');
const LIVE = process.env.PG_LIVE || path.resolve(HERE, '../live');           // live/capture.py output
const THEME = process.env.PG_THEME || REPO;     // dir holding snippets/ (unchanged helpers)
const OUT = path.join(HERE, 'out');
fs.mkdirSync(OUT, { recursive: true });

function mkEngine() {
  const engine = new Liquid({ root: [path.join(THEME, 'snippets')], extname: '.liquid', jsTruthy: false });
  // Shopify's {% doc %} (theme-check doc tag) -- swallow it.
  engine.registerTag('doc', {
    parse(token, remainTokens) {
      this.tpls = [];
      let t;
      while ((t = remainTokens.shift())) { if (t.name === 'enddoc') return; }
      throw new Error('enddoc not found');
    },
    render() { return ''; }
  });
  engine.registerFilter('json', v => {
    let s = JSON.stringify(v === undefined ? null : v);
    return s.replace(/\//g, '\\/').replace(/&/g, '\\u0026').replace(/</g, '\\u003c').replace(/>/g, '\\u003e');
  });
  engine.registerFilter('image_url', (img, ...args) => {
    const src = typeof img === 'string' ? img : img.src;
    const m = src.match(/\/([^\/?]+)\?v=(\d+)/);
    let w = null;
    for (const a of args) if (Array.isArray(a) && a[0] === 'width') w = a[1];
    return `//senseless.uk/cdn/shop/files/${m[1]}?v=${m[2]}${w ? '&width=' + w : ''}`;
  });
  engine.registerFilter('asset_url', n => `//senseless.uk/cdn/shop/t/2/assets/${n}?v=71083694133951457661782154056`);
  const origDate = engine.filters['date'];
  engine.registerFilter('date', function (v, fmt, ...rest) {
    if (v === 'now' && fmt === '%z') return '+0100';   // BST, as served on 23 Sep
    return origDate.call(this, v, fmt, ...rest);
  });
  return engine;
}

function loadGraphLive(label) {
  const f = path.join(LIVE, 'raw', `${label}__0_graph.jsonld`);
  return fs.existsSync(f) ? fs.readFileSync(f, 'utf8') : null;
}

function mkProduct(handle, selectedId) {
  const js = JSON.parse(fs.readFileSync(path.join(LIVE, 'js', `${handle}.js`), 'utf8'));
  // rating + breadcrumb parent from the live base capture
  const live = JSON.parse(loadGraphLive(`${handle}__base`));
  const prodNode = live['@graph'].find(n => n['@type'] === 'Product' || n['@type'] === 'ProductGroup');
  const crumb = live['@graph'].find(n => n['@type'] === 'BreadcrumbList');
  const ar = prodNode.aggregateRating;
  const collections = [];
  if (crumb.itemListElement.length === 3) {
    const c = crumb.itemListElement[1];
    collections.push({ handle: c.item.split('/collections/')[1], title: c.name, url: '/collections/' + c.item.split('/collections/')[1] });
  }
  const images = js.images.map(src => ({ src }));
  const variants = js.variants.map(v => ({
    id: v.id, title: v.title, sku: v.sku, barcode: v.barcode || null, price: v.price, available: v.available,
    url: `/products/${handle}?variant=${v.id}`, options: v.options,
    featured_image: v.featured_image ? { src: v.featured_image.src } : null,
  }));
  const selected = selectedId ? variants.find(v => String(v.id) === String(selectedId)) : null;
  const firstAvail = variants.find(v => v.available) || variants[0];
  return {
    id: js.id, title: js.title, handle, url: `/products/${handle}`, description: js.description, type: js.type,
    images, featured_image: images[0] || null, variants,
    options_with_values: js.options.map(o => ({ name: o.name, position: o.position, values: o.values })),
    selected_variant: selected || undefined,
    selected_or_first_available_variant: selected || firstAvail,
    price: js.price, available: js.available, collections,
    metafields: { reviews: ar ? { rating: { value: { rating: ar.ratingValue } }, rating_count: { value: Number(ar.reviewCount) } } : { rating: null, rating_count: null } },
  };
}

function ctxFor(handle, selectedId) {
  return {
    shop: { url: 'https://senseless.uk', currency: 'GBP', name: 'Senseless' },
    cart: { currency: { iso_code: 'GBP' } },
    canonical_url: `https://senseless.uk/products/${handle}`,
    request: { page_type: 'product' },
    page_title: 'x', page_description: 'x',
    settings: {},
    product: mkProduct(handle, selectedId),
  };
}

function extractScriptBody(html) {
  const m = html.match(/<script type="application\/ld\+json" class="jdgm-server-jld">\n?([\s\S]*?)\n?<\/script>/);
  return m ? m[1] : null;
}

const targets = JSON.parse(fs.readFileSync(path.join(LIVE, 'targets.json'), 'utf8')).filter(([l]) => !l.startsWith('collection'));
const orig = fs.readFileSync(process.env.PG_ORIG || path.join(REPO, 'snippets', 'senseless-structured-data.liquid'), 'utf8');
const draft = fs.readFileSync(process.env.PG_DRAFT || path.join(HERE, 'draft', 'senseless-structured-data.liquid'), 'utf8');
const engine = mkEngine();
const rows = [];
for (const [label, url] of targets) {
  const handle = label.split('__')[0];
  const vm = label.match(/__v(\d+)_/);
  const ctx = ctxFor(handle, vm ? vm[1] : null);
  const o = await engine.parseAndRender(orig, ctx, { globals: ctx });
  const d = await engine.parseAndRender(draft, ctx, { globals: ctx });
  fs.writeFileSync(path.join(OUT, `${label}.orig.html`), o);
  fs.writeFileSync(path.join(OUT, `${label}.draft.html`), d);
  const ob = extractScriptBody(o), db = extractScriptBody(d);
  const live = loadGraphLive(label);
  let parsed = null, err = null;
  try { parsed = JSON.parse(db); } catch (e) { err = e.message; }
  fs.writeFileSync(path.join(OUT, `${label}.draft.json`), parsed ? JSON.stringify(parsed, null, 2) : 'PARSE ERROR ' + err);
  const top = parsed ? parsed['@graph'].find(n => /Product/.test(JSON.stringify(n['@type'])) && n['@id'] && n['@id'].endsWith('#product')) : null;
  const offers = [];
  const walk = n => { if (Array.isArray(n)) n.forEach(walk); else if (n && typeof n === 'object') { if (n['@type'] === 'Offer') offers.push(n); Object.values(n).forEach(walk); } };
  if (parsed) walk(parsed);
  rows.push({
    label,
    orig_eq_live: live !== null && ob.trim() === live.trim(),
    draft_eq_orig: db === ob,
    draft_json_ok: !!parsed, err,
    type: top && top['@type'],
    offers: offers.map(x => `${x.sku || '-'}@${x.price}${x.gtin13 ? ' gtin ' + x.gtin13 : ''}`).join(' | '),
  });
}
console.table(rows);
fs.writeFileSync(path.join(OUT,'report.json'),JSON.stringify(rows,null,1));
