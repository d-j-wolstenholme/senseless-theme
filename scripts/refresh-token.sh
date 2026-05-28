#!/usr/bin/env bash
set -euo pipefail

# Load credentials from .env
set -a
source .env
set +a

# Request a new token using client credentials grant
RESPONSE=$(curl -s -X POST \
  "https://$SHOPIFY_STORE/admin/oauth/access_token" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "grant_type=client_credentials" \
  -d "client_id=$SHOPIFY_CLIENT_ID" \
  -d "client_secret=$SHOPIFY_CLIENT_SECRET")

# Extract the token using Python (avoids jq dependency)
NEW_TOKEN=$(echo "$RESPONSE" | python3 -c \
  "import sys,json; d=json.load(sys.stdin); print(d.get('access_token',''))")

# Validate — token must start with shpca_
if [[ "$NEW_TOKEN" == shpca_* ]]; then
  # Write new token to .env in place
  sed -i '' "s/^SHOPIFY_ACCESS_TOKEN=.*/SHOPIFY_ACCESS_TOKEN=$NEW_TOKEN/" .env
  echo "Token refreshed: ${NEW_TOKEN:0:12}..."
else
  echo "Token refresh failed. Response:"
  echo "$RESPONSE"
  exit 1
fi
