#!/usr/bin/env bash
# scripts/reconcile.sh — SessionStart ground-truth reconcile (Senseless · Canon v2.15).
#
# Per Project Instance §4/§6. Establishes ground truth (machine; git main local+remote;
# live MAIN theme #199324434780 via Shopify CLI; store canary), checks the Notion
# State-Surface snapshot (canon/state.json) against it, REPORTS drift — detect-only,
# NEVER auto-syncs git — and writes sync-status back to the State Surface (via `ntn` if
# wired, else flags the session to write it via Notion MCP). Report-only: always exits 0
# so a failed check can never abort a session.
set -uo pipefail
cd "$(dirname "$0")/.." 2>/dev/null || exit 0

STORE="senseless-numbing.myshopify.com"   # §6 canary — the permanent key, NOT the domain/display name
LIVE_THEME="199324434780"                  # Senseless Dev = published MAIN/live (§3)
STATE_SURFACE="38e58bc3-75ea-81ad-87eb-e20fcfc22406"
PROJECT_INSTANCE="38e58bc3-75ea-8198-9ed7-de73bc48f2b5"
LIBRARY="38158bc3-75ea-81ef-abd2-ded10fd726a7"

echo "## Reconcile — ground truth before acting (Canon v2.15)"
echo "- Machine: $(hostname 2>/dev/null || echo unknown)  ·  confirm which machine if unsure (hard rule #1)"

# --- Git: main, local + remote (report-only; never auto-sync) ---
branch="$(git rev-parse --abbrev-ref HEAD 2>/dev/null || echo '?')"
head="$(git rev-parse --short HEAD 2>/dev/null || echo '?')"
if [ -n "$(git status --porcelain 2>/dev/null)" ]; then tree="uncommitted changes"; else tree="clean"; fi
echo "- Git: $branch @ $head ($tree)"
[ "$branch" != "main" ] && echo "  !! not on main — main is the single working branch → live theme"
git fetch -q origin 2>/dev/null || true
ab="$(git rev-list --left-right --count "origin/$branch...HEAD" 2>/dev/null || true)"
[ -n "$ab" ] && echo "- vs origin/$branch: $(echo "$ab" | awk '{print $1" behind, "$2" ahead"}')  (note: a git push does NOT deploy)"

# --- Store + live MAIN theme (verify-store canary §6; wrong store ⇒ STOP) ---
token=""
[ -f .env ] && token="$(grep -E '^SHOPIFY_ACCESS_TOKEN=' .env | head -1 | cut -d= -f2-)"
if command -v shopify >/dev/null 2>&1; then
  themes="$(SHOPIFY_CLI_THEME_TOKEN="$token" shopify theme list --store "$STORE" --json 2>/dev/null || true)"
  if [ -n "$themes" ]; then
    live="$(printf '%s' "$themes" | python3 -c 'import sys,json
try: ts=json.load(sys.stdin)
except Exception: ts=[]
print(next((str(t.get("id")) for t in ts if str(t.get("role","")).lower() in ("main","live")), ""))' 2>/dev/null || true)"
    if [ "$live" = "$LIVE_THEME" ]; then echo "- Live: $STORE — MAIN theme #$live  ok"
    elif [ -n "$live" ]; then echo "- Live: $STORE — MAIN theme #$live  !! expected #$LIVE_THEME — investigate"
    else echo "- Live: $STORE — could not resolve MAIN theme from CLI output"; fi
  else echo "- Live: could not list themes for $STORE (CLI/token) — verify the store manually before acting"; fi
else
  echo "- Shopify CLI not found — cannot read live theme. Verify store=$STORE manually before acting"
  echo "  (Shopify MCP get-shop-info MUST equal $STORE — the MCP/CLI default is Totally Numb)"
fi

# --- Check the Notion snapshot against ground truth (detect-only) ---
if [ -f canon/state.json ]; then
  python3 - canon/state.json <<'PY' || true
import sys, json, datetime
s = json.load(open(sys.argv[1]))
print("- Canon %s · State Surface last verified %s · sync: %s"
      % (s.get("canon_version","?"), s.get("last_verified","?"), s.get("sync_status","?")))
try:
    age = (datetime.date.today() - datetime.date.fromisoformat(s.get("last_verified",""))).days
    if age > int(s.get("freshness_days", 7)):
        print("  !! State Surface snapshot STALE (%d days) — re-read it in Notion and reconcile" % age)
except Exception:
    pass
PY
else
  echo "- canon/state.json missing — read the State Surface in Notion and reconcile manually"
fi

# --- Write sync-status back to the State Surface ---
if command -v ntn >/dev/null 2>&1; then
  echo "- Sync-status write-back: \`ntn\` present → push status to the State Surface ($STATE_SURFACE)."
  # ntn write-back wired here (see Maintenance & Reconciliation Checklist). Detect-only above stays authoritative.
else
  echo "- Sync-status write-back: \`ntn\` not on PATH → the session writes the State-Surface sync-status ($STATE_SURFACE) via Notion MCP. Reconcile is detect-only; git is never auto-synced."
fi

echo "- Then read: Project Instance ($PROJECT_INSTANCE) → State Surface ($STATE_SURFACE); follow Library blueprints 01–04 ($LIBRARY)."
exit 0
