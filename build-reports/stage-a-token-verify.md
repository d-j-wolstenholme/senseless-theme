# Stage A — Token + Verify (senseless-numbing)

**Date:** 2026-06-01 (BST)
**Machine:** MacBook Pro
**Branch:** dev (up to date with origin/dev)
**Scope:** Mint a working `shpca_` Admin API token for the new store and verify scopes. **No store writes.**

---

## Result summary

- **Token OK?** ✅ Yes — `shpca_84af77…` minted via client_credentials grant (`scripts/refresh-token.sh`), written to `.env` (gitignored, not committed). 24h lifetime.
- **Store confirmed?** ✅ Yes — `{ shop }` returns `name: senseless-numbing`, `myshopifyDomain: senseless-numbing.myshopify.com`.
- **Scopes:** 20 of 22 required granted. **2 gaps** (see below).

## `.env` changes

| Key | Value |
|---|---|
| SHOPIFY_STORE | senseless-numbing.myshopify.com |
| SHOPIFY_CLIENT_ID | 00e1ce410255463eb174aef4997be275 (senseless-api) |
| SHOPIFY_CLIENT_SECRET | shpss_… (senseless-api, created 2026-06-01) |
| SHOPIFY_ACCESS_TOKEN | shpca_… (minted this session) |
| SHOPIFY_DEV_THEME_ID | *cleared* — old value `196680057167` belonged to the old store; new store's dev theme is created in a later stage |

All old `senseless-tattooing` / old-app values removed.
`scripts/refresh-token.sh` already reads store + creds from `.env` (not hardcoded) — no repoint needed.

## Granted scopes (verified via `currentAppInstallation`)

read_content, read_files, read_inventory, read_legal_policies, read_metaobjects,
read_online_store_navigation, read_online_store_pages, read_products, read_publications, read_themes,
write_content, write_files, write_inventory, write_legal_policies, write_metaobjects,
write_online_store_navigation, write_online_store_pages, write_products, write_publications, write_themes

## Gaps (action required before Stage B)

- ❌ **read_metaobject_definitions**
- ❌ **write_metaobject_definitions**

Impact: creating/editing metaobject *definitions* (e.g. per-SKU Key Facts) will fail until granted.
Fix: add both scopes to the `senseless-api` app config, update/reinstall the app on senseless-numbing, then re-run `scripts/refresh-token.sh` to mint a fresh token and re-verify.

## Not done (by design — Stage A is read-only)

- No theme push.
- No resource creation (products, collections, metafields, metaobjects, pages, etc.) — Stage B.
