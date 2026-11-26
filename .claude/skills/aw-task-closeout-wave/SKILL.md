---
name: aw-task-closeout-wave
description: Use when running an Autumn & Wool plan-execution wave — verifying whether a branch is already merged, spinning up scoped subagents on different OpenCode models, writing evidence-based closeout notes for owner-blocked tasks, regenerating rollups, and opening the PR.
---

# Autumn & Wool task closeout wave

Use for "do the open tasks", "close out overdue tasks", "merge this branch and start a new one", or any multi-worker execution wave in `/Users/ebrahim/autumnandwool`. Read `AGENTS.md` and `AGENT-CONTEXT.md` first; this skill adds the mechanical lessons from the 2026-11-26 wave.

## Hard rules (from AGENTS.md; never relax)

- Markdown/CSV planning repo. No test suite, lint or CI — do not add them.
- Never invent owner-provided numbers (stock, costs, sessions, revenue, carriers, bank balance), dates, or decisions. Use `[FILL]`.
- No live store / Etsy / Merchant Center / ad-platform / email changes, no spend, no sends, no external API calls from workers.
- Squarespace plan gates: no Code Injection, no inline `<script>`, no waitlists. The `.sqs-widgets-confirmation-overlay` `pointer-events:none !important;` rule is load-bearing.
- Outputs are drafts/notes only. The repo is the decision record; live actions need the owner logged in via ego-browser from an ordinary Terminal.

## 1. Verify the merge before merging

The user may believe a branch is unmerged when it is already merged upstream.

```sh
git fetch origin
git merge-base --is-ancestor <branch-head> origin/main && echo "already merged"
git log --oneline main..origin/main          # remote may be AHEAD of local main
gh pr list --state open
```

On 2026-11-26 `feat/en-lv-multilingual` (60fb604) was already in `origin/main` via PR #142 (merge e3b97de), while local `main` was 20 commits behind remote. Do **not** re-merge or force-push `main`.

To preserve uncommitted work while basing a new branch on the current remote main:

```sh
git stash push -u -m "<reason>"
git checkout -B main origin/main
git checkout -b claude/<wave-name>
git stash pop
git add -A && git commit -m "docs: commit <preserved work>"
```

## 2. Worker design

- One department per worker; give exact allowed file paths and forbid everything else (especially `STATUS.md`, `OPEN-TASKS.md`, `AGENT-CONTEXT.md`, `AGENTS.md` and other departments' files).
- Use a different `opencode/*` model per worker. Available as of 2026-11-26 include `seaglass-alpha-free`, `tidepool-alpha-free`, `hy4-flash-free`, `iceman-free`, `flint-40b-free`, `deepseek-v4.1-flash-free`, `nemotron-3.5-super-vl-free`, `beam-free`, `mimo-v2.6-flash-free`, `nemotron-3.5-lightning-free`, `big-pickle`.
- Keep worker prompts short and bounded. Long prompts plus broad exploration cause failures.
- Expect intermittent model failures: `tidepool-alpha-free` → "Model is unavailable"; `deepseek-v4.1-flash-free` → "Compaction summary reached the output token limit"; `mimo-v2.6-flash-free` → "Nothing to compact yet". **Reassign to a different model rather than retrying the same one.**
- Workers may land edits *after* you take over a stuck department. Re-read the files and `git status` before editing anything yourself.

## 3. Closeout note template

For overdue TODO tasks whose inputs are owner exports or live actions, write `<output-folder>/closeout-2026-11-26-<TASK-ID>.md`:

```markdown
# <TASK-ID> — closeout check 2026-11-26
## Task (verbatim text + due date from the status file)
## What the deliverable requires
## Repo evidence found (relative paths; name the prepared draft)
## Verdict: HELD — owner/live data not in repo
## Missing inputs (exact, actionable)
## Next action (one sentence)
```

Only write `DONE on repo evidence` if the deliverable was actually produced from in-repo data. Aggregate all rows into `business-os/CLOSEOUT-YYYY-MM-DD-OWNER-UNBLOCK.md` with links relative to that file (`../business-os/...`, `../campaign-assets/...`) and verify links resolve.

## 4. Status-file edit pitfall

Append the reference to the **Notes/Out cell of the table row**, not to an appendix section — only table rows flow into the generated rollups:

```
| CX-26 | ... | 26 Oct | TODO | Prepared: ... — 2026-11-26: closeout note in business-os/customer-experience/closeout-2026-11-26-CX-26.md — HELD on repo evidence. |
```

- Do not change the Status column, row order or other cells. Totals should stay 122 done / 44 assumed / 42 blocked / 88 to-do / 296.
- Two target rows are usually **not adjacent** — use one edit per row.
- One worker appended a `## Notes/Out` section at the end of `customer-experience.md`; move those lines into the rows and delete the section before regenerating.

## 5. Verification

```sh
cd plans/2026-2027/status && python3 rollup.py && python3 rollup.py --selftest
python3 business-os/unit_economics.py --selftest
python3 build_google_feed.py products_Oct-17_10-46-00PM.csv "$TMP/google.tsv"
diff -q autumnandwool-google-feed.tsv "$TMP/google.tsv"
python3 build_google_feed.py products_Oct-17_10-46-00PM.csv "$TMP/google.tsv" \
  --openai "$TMP/openai.tsv" --targets LV,EE,LT
diff -q business-os/seo-marketplace/feed/2026-11-25-openai-feed-DRAFT-do-not-upload.tsv "$TMP/openai.tsv"
```

`rollup.py --selftest` is read-only; plain `rollup.py` rewrites `STATUS.md` and `OPEN-TASKS.md`. The OpenAI run prints a STOP-CHECK about unconfirmed target countries but still writes the file — never upload it.

## 6. Commit and PR

The active `gh` account (`ebrahim-castai`) is **not a collaborator** on `itumor/autumnandwool`; plain `gh pr create` fails with `must be a collaborator`. Use the repo-owning account:

```sh
git push -u origin claude/<wave-name>
GH_TOKEN="$(gh auth token --user itumor)" gh pr create \
  --base main --head claude/<wave-name> --title "..." --body-file <body.md>
```

## Example (2026-11-26 wave, PR #143)

Branch `claude/task-closeout-wave4`; ten notes: `CRE-24/25`, `GRO-17/20`, `CX-26/27`, `FIN-11/23`, `SEO-11/18`. All HELD on owner/live data. Rollups regenerated, feed byte-identical, PR opened. Remaining tasks are gated on G0–G9 — a filled draft is not a gate passing.
