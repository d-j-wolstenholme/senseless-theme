# /session-end

Run at the end of every Claude Code session. No exceptions.

## Steps

1. Confirm the working branch is `dev` (`git branch --show-current`). Never commit directly to `main` during build sessions.
2. Invoke the `commit-and-deploy` skill — commits to `dev` and pushes to `origin/dev`.
3. Generate the full build report
4. Display the report ready to paste into the planning chat

## Output

Build report (see commit-and-deploy skill for full format).
