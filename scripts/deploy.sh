#!/usr/bin/env bash
# Senseless — one-command scoped deploy (live theme only, via the durable CLI token-auth path).
#
# Authenticates `shopify theme push` non-interactively with the write_themes-scoped shpca_ Admin
# token (SHOPIFY_CLI_THEME_TOKEN=$SHOPIFY_ACCESS_TOKEN). The deploy runs ENTIRELY through the Shopify
# CLI — it does NOT use the Admin Asset API (Hard Rule #11 bars Asset-API deploys, not CLI token-auth).
#
# Scoped pushes ONLY: every path arg becomes an --only flag. No args => usage + exit 1 (never a blind
# whole-theme push).
#
# USAGE:
#   ./scripts/deploy.sh sections/foo.liquid templates/index.json
#
set -euo pipefail

STORE="senseless-numbing.myshopify.com"
THEME="199324434780"   # live "Senseless Dev"

# Run from repo root (so ./scripts/refresh-token.sh + its relative `source .env` resolve).
cd "$(dirname "$0")/.."

# Require at least one file path — never push the whole theme.
if [[ $# -eq 0 ]]; then
  echo "usage: ./scripts/deploy.sh <file> [<file> ...]" >&2
  echo "  e.g. ./scripts/deploy.sh sections/foo.liquid templates/index.json" >&2
  exit 1
fi

# 1. Mint a fresh shpca_ token.
./scripts/refresh-token.sh

# 2. Load it.
set -a; source .env; set +a

# 3. Guard: token must be present after refresh.
if [[ -z "${SHOPIFY_ACCESS_TOKEN:-}" ]]; then
  echo "deploy: no token after refresh (SHOPIFY_ACCESS_TOKEN empty)" >&2
  exit 1
fi

# Build --only flags (array => safe with spaces and multiple flags).
only=()
for f in "$@"; do
  only+=(--only "$f")
done

# 4. Show exactly what's about to push.
echo "deploy: store=$STORE theme=$THEME (live)"
echo "deploy: pushing ${#} file(s):"
for f in "$@"; do echo "  - $f"; done

# 5. Push (CLI token-auth). Surface the raw error and exit non-zero on failure.
if SHOPIFY_CLI_THEME_TOKEN="$SHOPIFY_ACCESS_TOKEN" shopify theme push \
     --store "$STORE" --theme "$THEME" --allow-live "${only[@]}"; then
  echo "deploy: success"
else
  rc=$?
  echo "deploy: shopify theme push FAILED (exit $rc)" >&2
  exit "$rc"
fi
