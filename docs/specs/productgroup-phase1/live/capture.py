#!/usr/bin/env python3
"""Capture what the render harness reads, from the LIVE site (read-only GETs).

Run from this directory:  python3 capture.py
Writes, for every [label, url] in targets.json:
  raw/<label>__0_graph.jsonld   the body of the page's <script ... class="jdgm-server-jld"> (verbatim)
  js/<handle>.js                /products/<handle>.js (variants, prices, barcodes, images)
Take it IMMEDIATELY before editing (the 23 Sep GS1 barcode load changed gtin13 on 16 variants, so an
older capture is stale). Add the 12 single-variant ?variant= URLs to targets.json first (spec §7).
"""
import json
import os
import re
import time
import urllib.request

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36"
GRAPH = re.compile(r'<script type="application/ld\+json" class="jdgm-server-jld">\n?([\s\S]*?)\n?</script>')


def get(url):
    sep = "&" if "?" in url else "?"
    req = urllib.request.Request(f"{url}{sep}cb={int(time.time() * 1000)}", headers={"User-Agent": UA})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=40) as r:
                return r.read().decode("utf-8", "replace")
        except Exception as e:  # noqa
            err = e
            time.sleep(2 * (attempt + 1))
    raise SystemExit(f"FAILED {url}: {err}")


def main():
    os.makedirs("raw", exist_ok=True)
    os.makedirs("js", exist_ok=True)
    handles = set()
    for label, url in json.load(open("targets.json")):
        m = GRAPH.search(get(url))
        if not m:
            raise SystemExit(f"no jdgm-server-jld graph on {url}")
        open(f"raw/{label}__0_graph.jsonld", "w").write(m.group(1))
        if "/products/" in url:
            handles.add(url.split("/products/")[1].split("?")[0])
    for h in sorted(handles):
        open(f"js/{h}.js", "w").write(get(f"https://senseless.uk/products/{h}.js"))
    print(f"captured {len(json.load(open('targets.json')))} graphs and {len(handles)} product .js files")


if __name__ == "__main__":
    main()
