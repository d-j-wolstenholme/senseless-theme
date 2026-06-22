#!/usr/bin/env python3
"""
Senseless site-wide content lint (repo-resident copy only). Mechanical/automated checks.
REPORTS, does not fix. Out of scope (handled in planning chat via Shopify Admin API): product
descriptions, metafields, /pages/* bodies, blog articles, collection descriptions, and
meta/OG/title fields set in Shopify admin.

Scope IN: *.liquid (sections/snippets/blocks/templates/layout), JSON templates, section/settings
schema label+default strings, English locale files (locales/en.default*.json), theme JSON-LD.

Checks: 1 COMPLIANCE [BLOCK]; 2 AI-vocab [WARN]; 3 AI-rhythm [WARN]; 4 US->UK spelling [WARN];
5 GEO/schema [WARN]; 6 linking/handles [WARN].

Scoping notes (also printed in the .md report):
 - Compliance runs on RAW lines of every in-scope file (phrases are specific; safe in code/CSS).
 - Prose checks (2,3,4) run only on extracted COPY: JSON string values for copy-bearing keys,
   {% schema %} label/default/info/content/placeholder values, and .liquid HTML text nodes with
   {%- style/comment -%}, <style>, <script> and {% schema %} regions skipped — so CSS/JS never
   false-positives.
 - Non-English locale files are skipped for text checks (vendor Horizon translations).
 - Bare "numbing" is an ALLOWED capture term and is never flagged.

Usage: python3 scripts/content-lint.py [--fail-on-block]
  Exits 0 by default (WARN-only first run). With --fail-on-block, exits 2 if any BLOCK hit.
"""
import os, re, csv, sys, json, datetime, statistics

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPORTS = os.path.join(ROOT, "reports")
TODAY = datetime.date.today().isoformat()

SCOPE_DIRS = ["sections", "snippets", "blocks", "templates", "layout"]
# Locale text checks: English source strings only.
LOCALE_FILES = ["locales/en.default.json", "locales/en.default.schema.json"]
HEADER_FOOTER = ("senseless-header.liquid", "senseless-footer.liquid", "header.liquid", "footer.liquid")

findings = []  # dict: file,line,dimension,rule_id,severity,snippet,suggestion

def add(fp, line, dim, rid, sev, snippet, suggestion):
    s = re.sub(r"\s+", " ", (snippet or "")).strip()
    if len(s) > 120:
        s = s[:117] + "..."
    findings.append({
        "file": os.path.relpath(fp, ROOT), "line": line, "dimension": dim,
        "rule_id": rid, "severity": sev, "snippet": s, "suggestion": suggestion,
    })

def rel(fp):
    return os.path.relpath(fp, ROOT)

def iter_scope_files():
    for d in SCOPE_DIRS:
        base = os.path.join(ROOT, d)
        if not os.path.isdir(base):
            continue
        for dirpath, _, names in os.walk(base):
            for n in sorted(names):
                if n.endswith(".liquid") or n.endswith(".json"):
                    yield os.path.join(dirpath, n)
    for lf in LOCALE_FILES:
        p = os.path.join(ROOT, lf)
        if os.path.isfile(p):
            yield p

def read_lines(fp):
    with open(fp, encoding="utf-8", errors="replace") as f:
        return f.read().split("\n")

# ---------------------------------------------------------------- copy extraction
SKIP_KEY_RE = re.compile(r"(_url|_id|_handle)$")
SKIP_KEYS = {
    "type", "id", "url", "link", "image", "scheme", "color", "anchor_id", "handle",
    "collection", "product", "columns", "band", "background", "direction", "layout",
    "align", "style", "size", "position", "mode", "accent_word", "tag", "badge_text",
    "icon", "video", "page", "menu", "format", "current_format", "current_strength",
    "comfort_tier", "force_tier", "scale_current", "level",
}

def is_copy(v):
    if not v or "://" in v or v.startswith("/") or v.startswith("#") or v.startswith("shopify://"):
        return False
    if "|" in v or "~" in v:  # delimited data blobs (selector tables etc.)
        return False
    if "{" in v or "}" in v or ";" in v:  # liquid/css fragments
        return False
    if not re.search(r"[A-Za-z]", v):
        return False
    if " " not in v.strip():  # single token (enum/handle/label-word) -> skip
        return False
    return True

KV_RE = re.compile(r'^\s*"([A-Za-z0-9_]+)"\s*:\s*"((?:[^"\\]|\\.)*)"\s*,?\s*$')

def html_strip(s):
    s = re.sub(r"\{\{.*?\}\}", " ", s)
    s = re.sub(r"\{%.*?%\}", " ", s)
    s = re.sub(r"<[^>]+>", " ", s)
    s = (s.replace("&amp;", "&").replace("&nbsp;", " ").replace("&rsquo;", "'")
           .replace("&mdash;", "—").replace("&pound;", "£").replace("&times;", "x")
           .replace("&#39;", "'").replace("&rarr;", "->"))
    return s

CODE_CHARS_RE = re.compile(r"[{}:;=|#()<>\[\]]")
COPY_KEYS = ("label", "default", "info", "content", "value", "heading", "headline", "title",
             "body", "answer", "question", "subhead", "intro", "closer", "note", "image_alt",
             "placeholder", "lead", "matched", "subtitle", "eyebrow", "text", "tagline",
             "success_message", "fine_print", "submit_label", "cta_label", "field_label")

def extract_copy_units(fp, lines):
    """Yield (lineno, text) copy units for prose checks (vocab/spelling/rhythm).
    Sources: JSON key:value copy, .liquid {% schema %} key:value copy, .liquid assign-literal
    prose, and .liquid HTML text nodes — with all code regions skipped and HTML residual required
    to be a clean sentence (no code chars), so CSS/JS/markup never leaks in."""
    units = []
    is_json = fp.endswith(".json")
    in_style = in_comment = in_script = in_schema = False
    for i, raw in enumerate(lines, 1):
        line = raw
        # JSON key:value copy (templates + locales) AND .liquid {% schema %} key:value copy.
        m = KV_RE.match(line)
        if m:
            key, val = m.group(1), m.group(2)
            if (not SKIP_KEY_RE.search(key)) and key not in SKIP_KEYS:
                txt = html_strip(val)
                if (is_copy(txt) or (key in COPY_KEYS and " " in txt.strip() and re.search(r"[A-Za-z]", txt))):
                    units.append((i, txt))
            if not is_json:
                continue
        if is_json:
            continue
        # ---- .liquid only below ----
        # open code regions (no-dash and dash forms)
        if re.search(r"\{%-?\s*(style|stylesheet|javascript)\s*-?%\}", line): in_style = True
        if re.search(r"\{%-?\s*comment\s*-?%\}", line): in_comment = True
        if re.search(r"\{%-?\s*schema\s*-?%\}", line): in_schema = True
        if "<style" in line: in_style = True
        if "<script" in line: in_script = True
        skipping = in_style or in_comment or in_script or in_schema
        if not skipping:
            # assign-literal prose
            for am in re.finditer(r"assign\s+\w+\s*=\s*'([^']{25,})'", line):
                t = html_strip(am.group(1))
                if is_copy(t):
                    units.append((i, t))
            # HTML text node — residual must be a clean sentence
            txt = html_strip(line).strip()
            if (txt and not CODE_CHARS_RE.search(txt) and len(txt.split()) >= 5
                    and re.search(r"[a-z]{3,}\s+[a-z]{3,}", txt)):
                units.append((i, txt))
        # close code regions
        if re.search(r"\{%-?\s*end(style|stylesheet|javascript)\s*-?%\}", line): in_style = False
        if re.search(r"\{%-?\s*endcomment\s*-?%\}", line): in_comment = False
        if re.search(r"\{%-?\s*endschema\s*-?%\}", line): in_schema = False
        if "</style" in line: in_style = False
        if "</script" in line: in_script = False
    return units

# ---------------------------------------------------------------- 1) COMPLIANCE [BLOCK]
COMPLIANCE = [
    ("CMP-NUMBS",       r"numbs?\s+(the\s+)?(skin|area|pain)", "Remove effect claim; describe preparation for comfort, not an effect on skin/pain."),
    ("CMP-PAIN-RELIEF", r"pain[-\s]?relief", "Banned. Use 'helps clients feel more comfortable'."),
    ("CMP-RELIEVES",    r"relieves?\s+pain", "Banned. Reframe as comfort, not pain relief."),
    ("CMP-PAINFREE",    r"pain[-\s]?free", "Banned medicinal claim."),
    ("CMP-PAINLESS",    r"painless", "Banned medicinal claim."),
    ("CMP-LOCAL-ANAES", r"local\s+anaesthetic", "Banned. Senseless is a cosmetic, not an anaesthetic."),
    ("CMP-ANAES",       r"anaesthetis(e|es|ed|ing)", "Banned anaesthetic claim."),
    ("CMP-ANAESTHETIC", r"\banaesthetic\b", "Hard-rule term. (If 'not an anaesthetic' disclaimer, verify it's permitted in context.)"),
    ("CMP-BLOCK-NERVE", r"blocks?\s+nerve\s+signals", "Banned mechanism claim."),
    ("CMP-BLOCK-SENS",  r"blocks?\s+sensation", "Banned mechanism claim."),
    ("CMP-TREATS",      r"\btreats\b", "Banned medicinal verb. Use 'prepares' / 'for use before'."),
    ("CMP-PREVENTS",    r"\bprevents\b", "Banned medicinal verb."),
    ("CMP-CURES",       r"\bcures\b", "Banned medicinal verb."),
    ("CMP-HEALS",       r"\bheals\b", "Banned medicinal verb."),
    ("CMP-MED-GRADE",   r"medical[-\s]?grade", "Banned. Implies medicine."),
    ("CMP-CLIN-GRADE",  r"clinical[-\s]?grade", "Banned. Implies medicine."),
    ("CMP-RX-STRENGTH", r"prescription[-\s]?strength", "Banned. Implies medicine."),
    ("CMP-WORKS-MIN",   r"works?\s+in\s+\d+\s*(?:-\s*\d+\s*)?minute", "Banned specific efficacy timing. Use 'apply ahead of your appointment'."),
    ("CMP-LASTS-HRS",   r"lasts?\s+\d+\s*(?:-\s*\d+\s*)?hour", "Banned specific duration claim."),
    ("CMP-PCT-EFFECT",  r"\d+%\s*effective", "Banned percentage efficacy claim."),
    ("CMP-99-USERS",    r"99%\s*of\s*users", "Banned percentage claim."),
    ("CMP-AS-STRONG",   r"\bas\s+strong\s+as\b", "Banned efficacy comparison (esp. to lidocaine products)."),
    ("CMP-X-AS-STRONG", r"\b\w+\s+as\s+strong\s+as\b", "Banned 'X as strong as' efficacy-comparison pattern."),
    ("CMP-CRUELTY",     r"cruelty[-\s]?free", "Avoid 'cruelty-free' (substantiation/claim risk)."),
    ("CMP-LIDO-FREE",   r"lidocaine[-\s]?free", "'lidocaine-free' only allowed in designated Lidocaine-Free blog files."),
]
COMPILED_CMP = [(rid, re.compile(pat, re.I), sug) for rid, pat, sug in COMPLIANCE]

ANAES_RULES = {"CMP-ANAESTHETIC", "CMP-LOCAL-ANAES", "CMP-ANAES"}
NEG_RE = re.compile(r"(not\s+an?|isn'?t\s+an?|rather\s+than\s+an?|never\s+an?|n't\s+an?)\s*$", re.I)

def check_compliance(fp, lines):
    fname = os.path.basename(fp).lower()
    lido_ok = "lidocaine-free" in fname  # designated exception files (none in-repo currently)
    is_liquid = fp.endswith(".liquid")
    in_comment = in_style = in_script = False
    for i, line in enumerate(lines, 1):
        # Skip non-rendered regions (dev comments / CSS / JS) — phrases there aren't published copy.
        if is_liquid:
            if re.search(r"\{%-?\s*(comment)\s*-?%\}", line): in_comment = True
            if re.search(r"\{%-?\s*(style|stylesheet|javascript)\s*-?%\}", line) or "<style" in line: in_style = True
            if "<script" in line: in_script = True
        skip = in_comment or in_style or in_script
        if not skip:
            for rid, rx, sug in COMPILED_CMP:
                if rid == "CMP-LIDO-FREE" and lido_ok:
                    continue
                for m in rx.finditer(line):
                    if rid == "CMP-X-AS-STRONG" and re.search(r"\bas\s+strong\s+as\b", line, re.I) and re.match(r"as\b", m.group(0).strip(), re.I):
                        continue
                    sev, frid, fsug = "BLOCK", rid, sug
                    # Negated/disclaimer use of anaesthetic ("...not an anaesthetic") -> WARN to verify, not a hard BLOCK.
                    if rid in ANAES_RULES:
                        pre = line[:m.start()]
                        if NEG_RE.search(pre):
                            sev, frid = "WARN", rid + "-DISCLAIMER"
                            fsug = "Negated/disclaimer use ('not an anaesthetic') — compliant disclaimer; verify context."
                    add(fp, i, "compliance", frid, sev, line, fsug)
        if is_liquid:
            if re.search(r"\{%-?\s*endcomment\s*-?%\}", line): in_comment = False
            if re.search(r"\{%-?\s*end(style|stylesheet|javascript)\s*-?%\}", line) or "</style" in line: in_style = False
            if "</script" in line: in_script = False

# ---------------------------------------------------------------- 2) AI vocab [WARN]
AI_VOCAB = [
    (r"\bdelve\b", "Cut 'delve'."), (r"\bleverage\b", "Use 'use'."),
    (r"\brobust\b", "AI-tell; use a concrete word."), (r"\bseamless(ly)?\b", "AI-tell; cut or be specific."),
    (r"\bcomprehensive\b", "AI-tell; cut or be specific."), (r"\btapestry\b", "Cut 'tapestry'."),
    (r"\bnavigat(e|es|ing)\b", "Figurative 'navigate' is an AI-tell — verify literal use."),
    (r"in\s+today'?s\b", "Cut 'in today's …'."), (r"in\s+the\s+realm\s+of", "Cut 'in the realm of'."),
    (r"it'?s\s+worth\s+noting", "Cut 'it's worth noting'."), (r"\bultimately\b", "Cut 'ultimately'."),
    (r"that\s+being\s+said", "Cut 'that being said'."),
    (r"not\s+just\b.{1,50}?\bbut\b", "AI 'not just X but Y' construction — rewrite."),
    (r"the\s+moments\s+that\s+matter", "Cut cliché."), (r"your\s+journey", "Cut 'your journey'."),
    (r"designed\s+for\s+you", "Cut 'designed for you'."), (r"\btransformative\b", "AI-tell; cut."),
    (r"\belevate\b", "AI-tell; use plain verb."), (r"\bunlock\b", "AI-tell; cut."),
    (r"\bdiscover\b", "AI-tell; consider 'see/find/shop'."), (r"\bembark\b", "Cut 'embark'."),
    (r"\bcurated\b", "AI-tell; cut or be specific."), (r"thoughtfully\s+crafted", "Cut cliché."),
    (r"meticulously\s+formulated", "Cut cliché."),
]
COMPILED_VOCAB = [(re.compile(p, re.I), s) for p, s in AI_VOCAB]

def check_vocab(fp, units):
    for ln, txt in units:
        for rx, sug in COMPILED_VOCAB:
            m = rx.search(txt)
            if m:
                add(fp, ln, "ai-vocab", "AIV-" + re.sub(r"[^a-z]", "", m.group(0).lower())[:10], "WARN", txt, sug)

# ---------------------------------------------------------------- 3) AI rhythm [WARN]
def split_sentences(t):
    parts = re.split(r"(?<=[.!?])\s+", t.strip())
    return [p for p in parts if len(p.split()) >= 1]

def check_rhythm(fp, units):
    for ln, txt in units:
        words = txt.split()
        if len(words) <= 40:
            continue
        dashes = txt.count("—")
        if dashes > 1:
            add(fp, ln, "ai-rhythm", "RHY-EMDASH", "WARN", txt, f"{dashes} em-dashes in one block (>1) — vary punctuation.")
        sents = split_sentences(txt)
        if len(sents) >= 4:
            lens = [len(s.split()) for s in sents]
            sd = statistics.pstdev(lens)
            if sd < 3:
                add(fp, ln, "ai-rhythm", "RHY-UNIFORM", "WARN", txt, f"Sentence-length stdev {sd:.1f} (<3) across {len(sents)} sentences — too uniform.")
        for s in sents:
            segs = [x.strip() for x in s.split(",")]
            if len(segs) >= 3 and re.search(r",\s*(and|or)\s+\w", s):
                short = [x for x in segs if 0 < len(x.split()) <= 6]
                if len(short) >= 3:
                    add(fp, ln, "ai-rhythm", "RHY-TRICOLON", "WARN", s, "Possible tricolon (3 parallel comma phrases) — human review.")
                    break

# ---------------------------------------------------------------- 4) US->UK spelling [WARN]
US_UK = {
    "color": "colour", "colors": "colours", "colored": "coloured", "coloring": "colouring",
    "organization": "organisation", "organizations": "organisations", "organize": "organise",
    "organized": "organised", "organizing": "organising", "behavior": "behaviour",
    "behaviors": "behaviours", "anesthetic": "anaesthetic", "anesthesia": "anaesthesia",
    "fulfill": "fulfil", "fulfillment": "fulfilment", "center": "centre", "centers": "centres",
    "centered": "centred", "maximize": "maximise", "optimize": "optimise", "customize": "customise",
    "customized": "customised", "realize": "realise", "realized": "realised", "recognize": "recognise",
    "analyze": "analyse", "analyzed": "analysed", "catalog": "catalogue", "defense": "defence",
    "traveling": "travelling", "traveled": "travelled", "jewelry": "jewellery", "gray": "grey",
    "favorite": "favourite", "favorites": "favourites", "favor": "favour", "honor": "honour",
    "labor": "labour", "neighbor": "neighbour", "neighbors": "neighbours", "odor": "odour",
    "flavor": "flavour", "flavors": "flavours", "fiber": "fibre", "liter": "litre", "liters": "litres",
    "specialize": "specialise", "specialized": "specialised", "prioritize": "prioritise",
    "minimize": "minimise", "emphasize": "emphasise", "apologize": "apologise", "summarize": "summarise",
    "modeling": "modelling", "canceled": "cancelled", "labeled": "labelled", "labeling": "labelling",
    "fulfilled": "fulfilled", "moisturize": "moisturise", "moisturizer": "moisturiser",
    "moisturizing": "moisturising", "minimizing": "minimising", "personalize": "personalise",
    "personalized": "personalised",
}
US_UK_RE = re.compile(r"\b(" + "|".join(sorted(US_UK, key=len, reverse=True)) + r")\b", re.I)

def apply_case(src, repl):
    if src.isupper():
        return repl.upper()
    if src[:1].isupper():
        return repl[:1].upper() + repl[1:]
    return repl

def check_spelling(fp, units):
    for ln, txt in units:
        for m in US_UK_RE.finditer(txt):
            src = m.group(1)
            uk = apply_case(src, US_UK[src.lower()])
            add(fp, ln, "spelling", "SPELL-USUK", "WARN", txt, f"US spelling '{src}' -> UK '{uk}'.")

# ---------------------------------------------------------------- 5) GEO / schema [WARN]
def check_schema_geo(all_text_by_file):
    # Drug/Medicine @type anywhere
    for fp, lines in all_text_by_file.items():
        for i, line in enumerate(lines, 1):
            if re.search(r'"@type"\s*:\s*"(Drug|Medicine)"', line):
                add(fp, i, "geo-schema", "GEO-DRUGTYPE", "WARN", line, 'Schema @type must be "Product", not Drug/Medicine.')
    # Organization + exact legalName present somewhere
    org_ok = False
    legal_ok = False
    for fp, lines in all_text_by_file.items():
        blob = "\n".join(lines)
        if re.search(r'"@type"\s*:\s*"Organization"', blob):
            org_ok = True
        if re.search(r'"legalName"\s*:\s*(\{\{[^}]*\}\}|"Matrix Health Group Ltd")', blob) and "Matrix Health Group Ltd" in blob:
            legal_ok = True
    if not org_ok:
        add(os.path.join(ROOT, "snippets/senseless-structured-data.liquid"), 1, "geo-schema", "GEO-NO-ORG", "WARN", "Organization JSON-LD", "No Organization JSON-LD found in theme files.")
    if not legal_ok:
        add(os.path.join(ROOT, "snippets/senseless-structured-data.liquid"), 1, "geo-schema", "GEO-LEGALNAME", "WARN", "legalName", 'Organization legalName must be exactly "Matrix Health Group Ltd".')
    # Required @types emitted somewhere in theme
    required = {
        "FAQPage": "FAQPage JSON-LD (FAQ sections).",
        "Product": "Product JSON-LD (product templates).",
        "Offer": "Offer JSON-LD (product templates).",
        "CollectionPage": "CollectionPage JSON-LD (collection templates).",
        "ItemList": "ItemList JSON-LD (collection templates).",
        "BreadcrumbList": "BreadcrumbList JSON-LD.",
        "Article": "Article JSON-LD (blog/article templates).",
    }
    full = "\n".join("\n".join(l) for l in all_text_by_file.values())
    for t, desc in required.items():
        if not re.search(r'"@type"\s*:\s*"' + t + r'"', full):
            add(os.path.join(ROOT, "snippets/senseless-structured-data.liquid"), 1, "geo-schema", "GEO-MISSING-" + t.upper(), "WARN", desc, f'No "{t}" @type emitted in theme JSON-LD — {desc}')

# ---------------------------------------------------------------- 6) linking / handles [WARN]
LINK_RE = re.compile(r"/(pages|collections|products|blogs)/([a-z0-9][a-z0-9-]*)")

def check_links(all_text_by_file):
    # wrong canonical handles
    for fp, lines in all_text_by_file.items():
        for i, line in enumerate(lines, 1):
            if "senseless-foaming-cleanser" in line:
                add(fp, i, "linking", "LNK-CLEANSER-HANDLE", "WARN", line, "Use canonical handle 'foaming-cleanser' (not 'senseless-foaming-cleanser').")
            for m in re.finditer(r"/collections/([a-z0-9-]*spmu[a-z0-9-]*)", line):
                add(fp, i, "linking", "LNK-SPMU-HANDLE", "WARN", line, f"Collection handle '{m.group(1)}' -> use '...-semi-permanent-makeup'.")
    # >3 internal links in one section (JSON templates: count per top-level section)
    for fp, lines in all_text_by_file.items():
        if "/templates/" not in fp.replace("\\", "/") or not fp.endswith(".json"):
            continue
        try:
            data = json.loads("\n".join(lines))
        except Exception:
            continue
        secs = data.get("sections", {})
        for skey, sec in secs.items():
            blob = json.dumps(sec)
            n = len(LINK_RE.findall(blob))
            if n > 3:
                # find a line near the section key for citation
                ln = next((i for i, l in enumerate(lines, 1) if '"' + skey + '"' in l), 1)
                add(fp, ln, "linking", "LNK-TOOMANY", "WARN", f'section "{skey}" has {n} internal links', f"{n} internal links in one section (>3) — consider trimming.")
    # inbound link map (exclude header/footer sources)
    targets = {}  # path -> template file
    for fp in iter_scope_files():
        b = os.path.basename(fp)
        rp = rel(fp)
        # Skip bare/fallback + generic shared templates (not handle-specific URLs).
        GENERIC = {"page.json", "collection.json", "product.json", "product.bundle.json",
                   "blog.json", "article.json", "list-collections.json", "page.policy.json"}
        if b in GENERIC:
            continue
        if b.startswith("page.") and b.endswith(".json"):
            h = b[len("page."):-len(".json")]
            if h: targets["/pages/" + h] = rp
        elif b.startswith("collection.") and b.endswith(".json"):
            h = b[len("collection."):-len(".json")]
            if h: targets["/collections/" + h] = rp
        elif b.startswith("product.") and b.endswith(".json"):
            h = b[len("product."):-len(".json")]
            if h: targets["/products/" + h] = rp
    inbound = {}
    for fp, lines in all_text_by_file.items():
        if os.path.basename(fp) in HEADER_FOOTER:
            continue
        blob = "\n".join(lines)
        for kind, handle in LINK_RE.findall(blob):
            inbound.setdefault("/%s/%s" % (kind, handle), 0)
            inbound["/%s/%s" % (kind, handle)] += 1
    for path, tfile in sorted(targets.items()):
        if inbound.get(path, 0) == 0:
            add(os.path.join(ROOT, tfile), 1, "linking", "LNK-ORPHAN", "WARN", path,
                "0 inbound links from non-header/footer theme sources (INCOMPLETE: Shopify-resident page links added later by planning chat).")

# ---------------------------------------------------------------- run
def main():
    files = list(iter_scope_files())
    all_text = {fp: read_lines(fp) for fp in files}
    for fp in files:
        lines = all_text[fp]
        check_compliance(fp, lines)
        units = extract_copy_units(fp, lines)
        check_vocab(fp, units)
        check_rhythm(fp, units)
        check_spelling(fp, units)
    check_schema_geo(all_text)
    check_links(all_text)

    findings.sort(key=lambda r: (r["severity"] != "BLOCK", r["dimension"], r["file"], r["line"]))

    os.makedirs(REPORTS, exist_ok=True)
    csv_path = os.path.join(REPORTS, f"content-lint-{TODAY}.csv")
    md_path = os.path.join(REPORTS, f"content-lint-{TODAY}.md")
    cols = ["file", "line", "dimension", "rule_id", "severity", "snippet", "suggestion"]
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        for r in findings:
            w.writerow(r)

    # summary by dimension+severity
    dims = ["compliance", "ai-vocab", "ai-rhythm", "spelling", "geo-schema", "linking"]
    summ = {d: {"BLOCK": 0, "WARN": 0} for d in dims}
    for r in findings:
        summ.setdefault(r["dimension"], {"BLOCK": 0, "WARN": 0})
        summ[r["dimension"]][r["severity"]] += 1
    block_total = sum(1 for r in findings if r["severity"] == "BLOCK")
    warn_total = sum(1 for r in findings if r["severity"] == "WARN")

    with open(md_path, "w", encoding="utf-8") as f:
        f.write(f"# Senseless content lint — {TODAY}\n\n")
        f.write(f"Files scanned: **{len(files)}** · Findings: **{len(findings)}** "
                f"(BLOCK {block_total}, WARN {warn_total})\n\n")
        f.write("Scope: repo-resident copy only (Liquid, JSON templates, schema label/default strings, "
                "English locales, theme JSON-LD). OUT: product/collection/page/blog bodies & admin meta "
                "(planning chat handles via Admin API). Mechanical checks; REPORT not fix. "
                "Bare 'numbing' is allowed and never flagged.\n\n")
        f.write("Prose checks (ai-vocab/ai-rhythm/spelling) run on extracted copy only (JSON string "
                "values, schema labels/defaults, .liquid HTML text — style/script/comment/schema regions "
                "skipped); non-English locales skipped. Compliance runs on all raw lines.\n\n")
        f.write("## Summary by dimension + severity\n\n")
        f.write("| Dimension | BLOCK | WARN | Total |\n|---|---|---|---|\n")
        for d in dims:
            b, wn = summ[d]["BLOCK"], summ[d]["WARN"]
            f.write(f"| {d} | {b} | {wn} | {b+wn} |\n")
        f.write(f"| **TOTAL** | **{block_total}** | **{warn_total}** | **{len(findings)}** |\n\n")
        f.write("## Findings (file:line)\n\n")
        f.write("| file | line | dimension | rule_id | sev | snippet | suggestion |\n|---|---|---|---|---|---|---|\n")
        for r in findings:
            sn = r["snippet"].replace("|", "\\|")
            sg = r["suggestion"].replace("|", "\\|")
            f.write(f"| {r['file']} | {r['line']} | {r['dimension']} | {r['rule_id']} | {r['severity']} | {sn} | {sg} |\n")

    print(f"Senseless content lint — {TODAY}")
    print(f"  scanned {len(files)} files · {len(findings)} findings (BLOCK {block_total}, WARN {warn_total})")
    for d in dims:
        print(f"    {d:12} BLOCK {summ[d]['BLOCK']:>3}  WARN {summ[d]['WARN']:>3}")
    print(f"  CSV: {rel(csv_path)}")
    print(f"  MD : {rel(md_path)}")

    if "--fail-on-block" in sys.argv and block_total:
        sys.exit(2)
    sys.exit(0)

if __name__ == "__main__":
    main()
