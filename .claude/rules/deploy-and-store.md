# Rule — Store, deploy & live-state (Senseless)

Detail behind the CLAUDE.md one-liners. Canon: Project Instance §3/§4/§6 (Notion `38e58bc3-75ea-8198-9ed7-de73bc48f2b5`).

## Verify-store gate — do this before ANY Shopify action
- The store **must** resolve to `senseless-numbing.myshopify.com`. The MCP/CLI default account is **Totally Numb** (`matrix-group-totally-numb`) — acting there is the classic incident. Mismatch ⇒ **STOP**.
- **Any of these satisfies the gate** — the requirement is *confirming the store*, not using one particular tool:
  1. Shopify MCP `get-shop-info` → must equal the key above.
  2. **Admin API** (the reliable fallback): `./scripts/refresh-token.sh`, then `curl -H "X-Shopify-Access-Token: $SHOPIFY_ACCESS_TOKEN" https://senseless-numbing.myshopify.com/admin/api/2024-10/shop.json` → check `myshopify_domain`.
  3. **Shopify CLI:** `SHOPIFY_CLI_THEME_TOKEN=$SHOPIFY_ACCESS_TOKEN shopify theme list --store senseless-numbing.myshopify.com` → MAIN theme must be `#199324434780`.
- **A failed/expired Shopify MCP connector is NOT a blocker and is NOT a stakeholder action.** It was wrongly logged as "Daniel needs to reconnect" on 27 + 28 Jul and again 30 Jul. `scripts/refresh-token.sh` + CLI/Admin API is the supported path, needs nothing from Daniel, and covers every Shopify action in this project (store gate, `theme list`/`pull`, `deploy.sh`, `shopPolicyUpdate`, `metafieldsSet`). Refresh the token and carry on — don't stall, and don't hand it back.
- This is the permanent store key, NOT the display name or the custom domain `senseless.uk`.
- Shopify CLI: always pass `--store senseless-numbing.myshopify.com`.

## Deploy = `scripts/deploy.sh` only
- Theme deploys go through Shopify CLI via `scripts/deploy.sh`: token refresh → `--allow-live` → scoped `--only <paths>`. Raw `shopify theme push` is not used.
- **A `git push` does NOT deploy.** Pushing to `origin/main` is version control only — nothing reaches the live theme without `deploy.sh`. (`git push` to origin is allowed and routine; it is decoupled from deploy.)
- Known recurring issue: a combined push can silently skip templates (deployed ≠ committed). Mitigation: per-file Asset-API remote diff after each push + `--only` re-push of any missing file.
- Verify before every deploy: `theme-check` 0 errors → Asset-API diff → independent live curl (4–6 sequential, varied UA + cache-bust) vs known byte-size baseline.

## Branches & theme identity
- `main` is the single working branch and **is** the live theme (live-and-main-only since 7 Jun launch; the dev-staging model is retired).
- Live theme = **Senseless Dev `#199324434780`** (published MAIN, re-verified 29 Jun).
- **No rollback theme.** Old Horizon `#199321977180` is **DELETED** — rollback = git history / re-deploy. (Do not look for or "protect" a Horizon rollback theme.)

## Reviews-guard
- `reviews-guard.manifest` + `reviews-guard.lock` gate every deploy: Judge.me embed markers must survive the push (repo assertion + live-vs-deploy + post-deploy live-marker verify).
- Changing a review file requires `--reviews-changed` and committing the rewritten lock.

## Reading "live" (Project Instance §4)
- Deployed theme observable via `shopify theme list --store senseless-numbing.myshopify.com` (role MAIN = live) + Asset-API remote file diff.
- "Live" also includes: storefront password status (currently OFF — site public), active theme name, live domain `senseless.uk`.

## Two-auditor split
- Daniel / planning chat audits the **source** (copy, SEO, branding, intent).
- Claude Code audits the **render** (UI, UX, a11y, performance, deploy). Never claim a render fact you cannot observe live.
