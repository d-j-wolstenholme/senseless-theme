#!/usr/bin/env python3
"""Lint Shopify-RESIDENT copy (page bodies, blog articles, product/collection descriptions,
meta titles/descriptions) against the same compliance rules `content-lint.py` applies to
repo-resident theme copy.

`content-lint.py` is explicitly scoped to the repo and skips everything that lives in the
Shopify admin. Every string this sweep authors for the Admin API therefore has no automated
gate — this closes that hole by reusing the exact same COMPILED_CMP rule set.

Usage:
  python3 scripts/content-lint-text.py FILE [FILE ...]     # lint files (html/md/txt/json)
  echo "some copy" | python3 scripts/content-lint-text.py - # lint stdin
  python3 scripts/content-lint-text.py --json payload.json  # lint every string value in a JSON doc

Exit 0 = no BLOCK. Exit 2 = at least one BLOCK.
"""
import importlib.util
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_spec = importlib.util.spec_from_file_location(
    "senseless_content_lint", os.path.join(ROOT, "scripts", "content-lint.py"))
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)  # safe: content-lint.py only runs on __main__

COMPILED_CMP = _mod.COMPILED_CMP
ANAES_RULES = _mod.ANAES_RULES
NEG_RE = _mod.NEG_RE
US_UK_RE = _mod.US_UK_RE
US_UK = _mod.US_UK
COMPILED_VOCAB = _mod.COMPILED_VOCAB

TAG_RE = re.compile(r"<[^>]+>")


def strip_html(text):
    text = re.sub(r"<(script|style)\b.*?</\1>", " ", text, flags=re.S | re.I)
    text = TAG_RE.sub(" ", text)
    for a, b in (("&amp;", "&"), ("&nbsp;", " "), ("&rsquo;", "'"), ("&mdash;", "—"),
                 ("&pound;", "£"), ("&#39;", "'"), ("&quot;", '"')):
        text = text.replace(a, b)
    return text


def lint(label, text):
    """Return list of (severity, rule, line, snippet, suggestion)."""
    out = []
    for lineno, raw in enumerate(strip_html(text).split("\n"), 1):
        line = raw.strip()
        if not line:
            continue
        for rid, rx, sug in COMPILED_CMP:
            for m in rx.finditer(line):
                if rid == "CMP-X-AS-STRONG" and re.search(r"\bas\s+strong\s+as\b", line, re.I) \
                        and re.match(r"as\b", m.group(0).strip(), re.I):
                    continue
                sev = "BLOCK"
                frid, fsug = rid, sug
                if rid in ANAES_RULES and NEG_RE.search(line[:m.start()]):
                    sev, frid = "WARN", rid + "-DISCLAIMER"
                    fsug = "Negated/disclaimer use — verify context."
                out.append((sev, frid, lineno, line[:140], fsug))
        for m in US_UK_RE.finditer(line):
            src = m.group(1)
            out.append(("WARN", "SPELL-USUK", lineno, line[:140],
                        f"US spelling '{src}' -> UK '{US_UK[src.lower()]}'."))
        for rx, sug in COMPILED_VOCAB:
            m = rx.search(line)
            if m:
                out.append(("WARN", "AIV-" + re.sub(r"[^a-z]", "", m.group(0).lower())[:10],
                            lineno, line[:140], sug))
    return out


def walk_json(node, path="$"):
    if isinstance(node, dict):
        for k, v in node.items():
            yield from walk_json(v, f"{path}.{k}")
    elif isinstance(node, list):
        for i, v in enumerate(node):
            yield from walk_json(v, f"{path}[{i}]")
    elif isinstance(node, str):
        yield path, node


def main():
    args = [a for a in sys.argv[1:] if a != "--json"]
    as_json = "--json" in sys.argv
    if not args:
        print(__doc__)
        return 0

    blocks = warns = 0
    for arg in args:
        if arg == "-":
            payload = sys.stdin.read()
            units = [("<stdin>", payload)]
        else:
            with open(arg, encoding="utf-8") as fh:
                payload = fh.read()
            if as_json or arg.endswith(".json"):
                units = [(f"{arg}:{p}", s) for p, s in walk_json(json.loads(payload))]
            else:
                units = [(arg, payload)]
        for label, text in units:
            for sev, rid, lineno, snippet, sug in lint(label, text):
                if sev == "BLOCK":
                    blocks += 1
                else:
                    warns += 1
                print(f"{sev:5} {rid:24} {label}:{lineno}  {snippet}\n      -> {sug}")

    print(f"\ncontent-lint-text: BLOCK {blocks}, WARN {warns}")
    return 2 if blocks else 0


if __name__ == "__main__":
    sys.exit(main())
