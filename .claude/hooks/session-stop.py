#!/usr/bin/env python3
# Stop / SessionEnd — write-back reminder + decision-without-chore-update flag.
# Advisory only: prints findings to stderr and exits 0 (never traps the session).
# The agent performs the Notion write-back at each task boundary; this hook flags omissions so
# nothing lands silently. Per the enforcement loop (Reference scaffold + Project Instance).
import sys, os, subprocess

proj = os.environ.get("CLAUDE_PROJECT_DIR", os.getcwd())
SESSION_LOG_DS = "37b14860-2152-4813-ac8f-1a9e2034564c"
STATE_SURFACE = "38e58bc3-75ea-81ad-87eb-e20fcfc22406"


def git(*a):
    try:
        return subprocess.run(["git", "-C", proj, *a], capture_output=True, text=True, timeout=10).stdout.strip()
    except Exception:
        return ""


flags = []

# 1) NEXT_SESSION.md present + fresher than the latest commit
nsp = os.path.join(proj, "NEXT_SESSION.md")
head_epoch = git("log", "-1", "--format=%ct")
if not os.path.exists(nsp):
    flags.append("NEXT_SESSION.md missing — write the handoff brief (done · next Work Item · gotcha).")
elif head_epoch:
    try:
        if os.path.getmtime(nsp) < int(head_epoch):
            flags.append("NEXT_SESSION.md is older than the latest commit — refresh the handoff brief.")
    except Exception:
        pass

# 2) decision-without-chore-update: last commit reads like a decision but didn't touch the chore files
msg = git("log", "-1", "--format=%s%n%b").lower()
files = git("show", "--name-only", "--format=", "HEAD")
if any(k in msg for k in ("decision", "supersede", "locked", "canon", "bootstrap-parity")):
    if "CLAUDE.md" not in files and "schema-contract.json" not in files:
        flags.append(
            "Last commit reads like a decision but didn't update the chore file (CLAUDE.md) or schema-contract — "
            "confirm the canonical record (Project Instance / Decisions DB) was updated in place + the blast radius swept."
        )

# 3) standing write-back reminder
flags.append(
    "Write-back check: this task's outcome belongs in the Session Log (ds %s) and the State-Surface "
    "sync-status must be current (page %s). Write outcomes, not plans." % (SESSION_LOG_DS, STATE_SURFACE)
)

if flags:
    print("## Session-end checks (advisory — not blocking):", file=sys.stderr)
    for f in flags:
        print("- " + f, file=sys.stderr)
sys.exit(0)
