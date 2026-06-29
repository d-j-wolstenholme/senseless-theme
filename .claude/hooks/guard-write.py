#!/usr/bin/env python3
# PreToolUse(Edit|Write|MultiEdit) — validate writes against the schema contract.
# Per Decision #41. The contract is .claude/schema-contract.json (DB -> data_source_id -> fields).
#   1) blocks edits to FROZEN canon paths (frozen_globs) — frozen canon changes by SUPERSEDE, never in place;
#   2) keeps schema-contract.json itself structurally valid when rewritten;
#   3) validates writes to contract-bound JSON files (file_bindings) against the declared field names.
# Exit 2 = blocked (message returned to Claude). Fail-closed on a corrupt contract; allow if no contract yet.
import sys, json, os, fnmatch


def block(msg):
    print("BLOCKED by enforcement loop: " + msg, file=sys.stderr)
    sys.exit(2)


try:
    data = json.load(sys.stdin)
    ti = data.get("tool_input") or {}
    path = ti.get("file_path") or ti.get("path") or ""
    content = ti.get("content")  # present for Write; absent for Edit/MultiEdit
    proj = os.environ.get("CLAUDE_PROJECT_DIR", os.getcwd())
    cpath = os.path.join(proj, ".claude", "schema-contract.json")
    contract = None
    if os.path.exists(cpath):
        try:
            contract = json.load(open(cpath))
        except Exception as e:
            block("schema-contract.json is unparseable (%s) — fix the contract before writing." % e)
except Exception as e:
    block("guard-write error (%s); failing closed." % e)

if not path or contract is None:
    sys.exit(0)  # nothing to validate, or repo not yet bootstrapped — allow

rel = os.path.relpath(path, proj) if os.path.isabs(path) else path
rel = rel.replace(os.sep, "/")

# 1) frozen canon — supersede-only
for pat in contract.get("frozen_globs", []):
    if fnmatch.fnmatch(rel, pat):
        block("`%s` is frozen canon — supersede it with a new decision; never edit it in place." % rel)

# 2) the contract itself must stay structurally valid
if rel.endswith(".claude/schema-contract.json") and content is not None:
    try:
        nc = json.loads(content)
        assert isinstance(nc.get("databases"), dict) and nc.get("canon_version")
    except Exception as e:
        block("rewriting schema-contract.json with an invalid shape (%s) — need {canon_version, databases{...}}." % e)

# 3) contract-bound JSON files validated against their database's declared fields
for b in contract.get("file_bindings", []):
    if fnmatch.fnmatch(rel, b.get("glob", "")) and content is not None:
        db = contract.get("databases", {}).get(b.get("db", ""), {})
        allowed = {f["name"] for f in db.get("fields", [])}
        try:
            rows = json.loads(content)
            rows = rows if isinstance(rows, list) else [rows]
        except Exception as e:
            block("`%s` must be valid JSON to bind to %s (%s)." % (rel, b.get("db"), e))
        for r in rows:
            if isinstance(r, dict):
                unknown = [k for k in r if k not in allowed and not k.startswith("_")]
                if unknown:
                    block("`%s` writes fields not in the %s schema: %s" % (rel, b.get("db"), unknown))

sys.exit(0)
