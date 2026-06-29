# Senseless — Claude Code instructions

Thin front door. **Notion is the single source of truth** — structure lives in the **Project Instance** (`38e58bc3-75ea-8198-9ed7-de73bc48f2b5`), current state in the **State Surface** (`38e58bc3-75ea-81ad-87eb-e20fcfc22406`), blueprints in the **Canonical Reference Library v2.15** (`38158bc3-75ea-81ef-abd2-ded10fd726a7`). Don't restate their structure here.

## On session start, before any work
1. **Run `scripts/reconcile.sh`** — establishes ground truth (machine, git `main` local+remote, live theme, store), then checks Notion against it. Review the report before acting. (Auto-runs via the SessionStart hook.)
2. Read the **Project Instance** — DB registry, repo/env, how live state is read.
3. Read the **State Surface** header — what's true now.
4. Follow Reference Library blueprints **01 Structure · 02 Interaction · 03 Lifecycle · 04 Integration**.

## Rules (enforced by hooks — see `.claude/settings.json`)
- Write **outcomes, not plans**; write back to Notion at each task boundary.
- **Reconcile on change:** update the canonical record in place + sweep the blast radius.
- Memory points to Notion; never treat a private copy as truth.
- **One task per session.**
- On `/compact`, preserve: decisions + rationale, outcomes (what's live, commit hashes), modified files, open blockers.
- A `PreToolUse` hook validates writes against `.claude/schema-contract.json`; a `Stop`/`SessionEnd` hook flags a missing write-back or a decision that landed without a chore-file update.

## Senseless specifics (detail in `.claude/rules/`)
- **Verify-store gate (first, every Shopify action):** Shopify MCP `get-shop-info` **must** equal `senseless-numbing.myshopify.com` — the MCP/CLI default is **Totally Numb**; mismatch ⇒ **STOP**. CLI always `--store senseless-numbing.myshopify.com`. → `.claude/rules/deploy-and-store.md`
- **Deploy = `scripts/deploy.sh` only** (Shopify CLI; token-refresh + `--allow-live` + scoped `--only`). A **`git push` does NOT deploy** — nothing reaches the theme without `deploy.sh`. Verify (theme-check 0 + Asset-API diff + live curl) before every push.
- **Branches:** `main` is the single working branch → it **is** the live theme. Live theme = **Senseless Dev `#199324434780`** (MAIN). **No rollback theme** — old Horizon `#199321977180` is **deleted**; rollback = git history / re-deploy.
- **Reviews-guard:** `reviews-guard.manifest`/`.lock` gate every deploy (Judge.me markers must survive); editing review files needs `--reviews-changed` + a lock commit.
- **Two-auditor split:** chat/Daniel audits the source (copy, SEO, intent); Claude Code audits the render (UI, a11y, deploy) — never claim a render fact you can't observe live.
- **Compliance (UK, [Regulated] — non-negotiable):** MHRA/ASA/CPSR Hard Rules; no medicinal/effect/time-to-effect claims; "numbing" is a category noun only. Run `compliance-check` before any user-facing copy; honour the Compliance Holds DB. → `.claude/rules/compliance.md`
- **Range:** 15 single SKUs + Foaming Cleanser (**35ml**) + 5 bundles (three strengths × three formats). Brand `#6B3FA0`.
- **Machine (hard rule #1):** ask which machine (Mac mini / MacBook Pro) at session start; reconcile prints it.

## Response style
Concise; lead with the answer; one or two steps at a time. Define any system term once.

## Session handoff
At task end, after write-back, write `NEXT_SESSION.md` (done · next Work Item · gotcha); a `Stop` hook flags if missing. Situational rules live in `.claude/rules/*.md` — keep this file thin.

*This file is regenerated from the Project Instance at Bootstrap-parity (Decision #41). It maps 1:1 to that page; change config there, not here.*
