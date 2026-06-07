# /session-end

Run at the end of every Claude Code session. No exceptions.

## Steps

1. Confirm the working branch is `main` (`git branch --show-current`). `main` is the single working branch (the `dev`-staging model was retired 7 June 2026).
2. Invoke the `commit-and-deploy` skill — commits to `main`, pushes to `origin/main`, and deploys to the **live** theme (`#199324434780`, `--allow-live`) after verifying theme-check 0 + render.
3. Generate the full build report
4. Display the report ready to paste into the planning chat
5. **Write the build report to Notion (final step, AFTER the git commit and push).** Create a new sub-page under the Build Reports page (ID `36e58bc375ea8199a328f695a280e854`):
   - **Title:** `YYYY-MM-DD — [short summary]`
   - **Content:** the full build report in the standard format — Completed, Open Items, Decisions Logged, Token Status, Git Status.
   - Use the Notion MCP (`notion` project server, or the connected Notion connector). If Notion is unreachable, surface a warning in the report but do not block the session — the report has already been committed to git.

## Output

Build report (see commit-and-deploy skill for full format), plus a confirmation line with the URL of the Notion sub-page created under Build Reports.
