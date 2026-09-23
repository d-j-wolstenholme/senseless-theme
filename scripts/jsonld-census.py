#!/usr/bin/env python3
"""JSON-LD census of every sitemap URL on senseless.uk (read-only GETs).

Usage: python3 scripts/jsonld-census.py <out.json>

Per URL it records every ld+json block (parsed), HTML entities left inside JSON strings (with the
JSON path), run-together sentences ("left.If"), Offers and whether they carry priceValidUntil, every
node declared at <page>#webpage with its name/description, the Organization @type, and dangling
@id references. Run it before and after a structured-data change and diff the two files; match
nodes by @type/@id, never by @graph index. Written for the 23 Sep 2026 schema-quality batch
(7224825), where it measured 34 -> 0 entity leaks and 0 -> 188 priceValidUntil.
The ad-facing two-pass check (.claude/rules/ad-facing.md) is separate.
"""
import json, re, sys, time, urllib.request, html
from concurrent.futures import ThreadPoolExecutor

BASE = "https://senseless.uk"
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36"
ENT = re.compile(r"&(#\d+|#x[0-9a-fA-F]+|[a-zA-Z][a-zA-Z0-9]{1,8});")
JOIN = re.compile(r"[a-z0-9\)%][\.\?\!:][A-Z][a-z]")
LD = re.compile(r'<script[^>]*type="application/ld\+json"[^>]*>(.*?)</script>', re.S | re.I)


def get(url):
    sep = "&" if "?" in url else "?"
    req = urllib.request.Request(f"{url}{sep}_cb={int(time.time()*1000)}", headers={"User-Agent": UA})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=40) as r:
                return r.status, r.read().decode("utf-8", "replace")
        except Exception as e:  # noqa
            err = e
            time.sleep(1.5 * (attempt + 1))
    return 0, f"ERR {err}"


def sitemap_urls():
    _, idx = get(BASE + "/sitemap.xml")
    subs = re.findall(r"<loc>([^<]+)</loc>", idx)
    urls = []
    for s in subs:
        _, body = get(html.unescape(s))
        urls += [html.unescape(u) for u in re.findall(r"<url>\s*<loc>([^<]+)</loc>", body)]
    return sorted(set(urls))


def walk(node, path, out):
    if isinstance(node, dict):
        for k, v in node.items():
            walk(v, f"{path}.{k}", out)
    elif isinstance(node, list):
        for i, v in enumerate(node):
            walk(v, f"{path}[{i}]", out)
    elif isinstance(node, str):
        for m in ENT.finditer(node):
            out.append({"path": path, "entity": m.group(0), "context": node[max(0, m.start()-40):m.end()+40]})
        if not node.startswith("http"):
            for m in JOIN.finditer(node):
                out.append({"path": path, "entity": "JOIN", "context": node[max(0, m.start()-30):m.end()+20]})


def nodes(doc):
    """Yield every dict node with an @type or @id, recursively."""
    if isinstance(doc, dict):
        if "@type" in doc or "@id" in doc:
            yield doc
        for v in doc.values():
            yield from nodes(v)
    elif isinstance(doc, list):
        for v in doc:
            yield from nodes(v)


def types(n):
    t = n.get("@type")
    return t if isinstance(t, list) else ([t] if t else [])


def census(url):
    status, body = get(url)
    rec = {"url": url, "status": status, "blocks": 0, "parse_errors": [], "entities": [],
           "offers": 0, "offers_with_pvu": 0, "pvu_values": [], "webpage_decls": [], "org_types": [],
           "org_return_policy": None, "raw_escapes": {}, "return_policy_node": False, "dangling": []}
    if status != 200:
        return rec
    blocks = LD.findall(body)
    rec["blocks"] = len(blocks)
    canon = re.search(r'<link rel="canonical" href="([^"]+)"', body)
    canon = canon.group(1) if canon else url
    ids_declared, ids_referenced = set(), set()
    for bi, raw in enumerate(blocks):
        for esc in ("\\u0026", "\\u003c", "\\u003e", "\\u0027", "\\/"):
            if esc in raw:
                rec["raw_escapes"][esc] = rec["raw_escapes"].get(esc, 0) + raw.count(esc)
        try:
            doc = json.loads(raw)
        except Exception as e:
            rec["parse_errors"].append(f"block {bi}: {e}")
            continue
        rec.setdefault("docs", []).append(doc)
        walk(doc, f"b{bi}", rec["entities"])
        for n in nodes(doc):
            ts = types(n)
            nid = n.get("@id")
            if nid and len(n) > 1:
                ids_declared.add(nid)
            elif nid and len(n) == 1:
                ids_referenced.add(nid)
            if "Offer" in ts:
                rec["offers"] += 1
                if "priceValidUntil" in n:
                    rec["offers_with_pvu"] += 1
                    rec["pvu_values"].append(n["priceValidUntil"])
            if nid and nid.endswith("#webpage") and len(n) > 1:
                rec["webpage_decls"].append({"block": bi, "type": ts, "name": n.get("name"),
                                             "description": (n.get("description") or "")[:120]})
            if nid and nid.endswith("/#organization") and len(n) > 1:
                rec["org_types"] = ts
                rec["org_return_policy"] = n.get("hasMerchantReturnPolicy")
            if "MerchantReturnPolicy" in ts:
                rec["return_policy_node"] = True
    rec["dangling"] = sorted(i for i in ids_referenced - ids_declared if i.startswith(BASE))
    rec["canonical"] = canon
    return rec


def main():
    out = sys.argv[1]
    urls = sitemap_urls()
    with ThreadPoolExecutor(6) as ex:
        recs = list(ex.map(census, urls))
    json.dump(recs, open(out, "w"), indent=1)
    ent = [(r["url"], e) for r in recs for e in r["entities"] if e["entity"] != "JOIN"]
    joins = [(r["url"], e) for r in recs for e in r["entities"] if e["entity"] == "JOIN"]
    print(f"urls={len(recs)} non200={sum(r['status']!=200 for r in recs)} blocks={sum(r['blocks'] for r in recs)} "
          f"parse_errors={sum(len(r['parse_errors']) for r in recs)}")
    print(f"entities={len(ent)} on {len({u for u,_ in ent})} urls")
    print(f"run-together sentences={len(joins)} on {len({u for u,_ in joins})} urls")
    print(f"offers={sum(r['offers'] for r in recs)} with_priceValidUntil={sum(r['offers_with_pvu'] for r in recs)}")
    multi = [r for r in recs if len(r["webpage_decls"]) > 1]
    conflict = [r for r in multi if len({(d['name'], d['description']) for d in r['webpage_decls'] if d['name'] or d['description']}) > 1]
    print(f"pages with >1 #webpage declaration={len(multi)}  with conflicting name/description={len(conflict)}")
    print(f"org @type seen={sorted({tuple(r['org_types']) for r in recs if r['org_types']})}")
    print(f"org hasMerchantReturnPolicy seen on {sum(1 for r in recs if r['org_return_policy'])} urls")
    print(f"dangling @id refs: {sum(len(r['dangling']) for r in recs)} on {sum(1 for r in recs if r['dangling'])} urls")
    esc = {}
    for r in recs:
        for k, v in r["raw_escapes"].items():
            esc[k] = esc.get(k, 0) + v
    print(f"raw escapes in JSON-LD: {esc}")


if __name__ == "__main__":
    main()
