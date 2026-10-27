---
type: Reference
title: "Chapter 4 Cheat Sheet and Quiz: The four components"
description: "Every Chapter 4 building block on one page: workflow, job, step, runner and action, plus quick rules for scripts, jobs, artifacts, variables, secrets and triggers."
tags: [github-actions, core-components, runners, cheat-sheet, quiz, recap]
status: stable
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-26T00:00:00Z }
sources:
  - id: gh-understand
    resource: https://docs.github.com/en/actions/get-started/understand-github-actions
    title: Understanding GitHub Actions
  - id: gh-workflow-syntax
    resource: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
    title: Workflow syntax for GitHub Actions
---

<p align="center">
  <a href="README.md">📂 <b>Chapter 4 Cheat Sheet and Quiz</b></a> &nbsp;·&nbsp; Lesson 14 · Part 1 of 9 &nbsp;·&nbsp; ⏱️ 5 min
</p>

# 🧱 The four components

| | Component | It is... | In YAML | Rule to remember |
|---|---|---|---|---|
| 📜 | **Workflow** | An automated process in one file | `.github/workflows/*.yml` | Many per repository |
| 📦 | **Job** | Steps that share a machine | `jobs.<id>:` | Parallel by default |
| 👣 | **Step** | One action or command | `- uses:` / `- run:` | In series, top to bottom |
| 🖥️ | **Runner** | The machine for a job | `runs-on:` | One per job, fresh each time |
| 🧩 | **Action** | A reusable, packaged step | `- uses: owner/repo@version` | Pin third-party actions to a full SHA |

> [!IMPORTANT]
> **A runner starts empty.** Make `actions/checkout` the first step of any job that reads your files. Add `fetch-depth: 0` when you need full history.

> [!TIP]
> **`run: |`** keeps each line as its own command; **`run: >`** folds them into one. Lines in one step share a shell; separate steps do not. Tools you install vanish with the runner.

> [!TIP]
> **Long logic belongs in a script:** check out, then `run: ./scripts/x.sh`. Start it with `#!/usr/bin/env bash` and `set -euo pipefail`, commit the executable bit, and keep LF line endings.

> [!TIP]
> **Jobs run in parallel on separate runners.** `needs:` sets the order (a failed job skips what needs it). Files travel by `upload-artifact` then `download-artifact` with the same `name`; small strings travel as job outputs.

> [!TIP]
> **After a failure, jobs that need it are skipped.** Override with `if: ${{ failure() }}` or `if: ${{ !cancelled() }}` (prefer it to `always()`). Check one job with `needs.<job>.result`. Outputs are readable only from jobs listed directly in `needs:`.

> [!TIP]
> **Artifacts outlive the runner.** Names must be unique per run (put matrix values in them), use `if-no-files-found: error`, set `retention-days`, collect many with `pattern:` + `merge-multiple:`, and never upload secrets.

> [!TIP]
> **Variables:** `env:` at workflow, job or step level, and the most specific wins. `$VAR` in `run:`, `${{ env.VAR }}` in `with:`/`name:`/`if:`. `>> $GITHUB_ENV` for later steps. `${{ vars.NAME }}` for values kept in Settings (environment > repo > org). Passwords go in `secrets`, never in variables.

> [!TIP]
> **Secrets:** create in Settings or with `gh secret set` (let it prompt). Read as `${{ secrets.NAME }}`, pass to `run:` through `env:`, use stdin for passwords. Masking only hides the exact value: `::add-mask::` derived ones. Forks get no secrets. Limit `GITHUB_TOKEN` with `permissions:`. Leaked? Rotate at the source first.

> [!TIP]
> **Triggers:** events, `workflow_dispatch` (button, up to 25 inputs), `schedule` (cron in UTC, every 5 minutes at most, default branch only) and outside calls (`repository_dispatch`, `workflow_run`, `workflow_call`). `branches` and `paths` filters combine with AND; never pair `branches` with `branches-ignore`. Pushes made with `GITHUB_TOKEN` don't start new runs.

> [!NOTE]
> **📘 From the GitHub docs, limits worth knowing:** secrets and variables are each capped at 48 KB. A repository holds up to 100 secrets and 500 variables. Names use letters, digits and `_`, and can't start with a digit or `GITHUB_`. ([Secrets reference](https://docs.github.com/en/actions/reference/security/secrets), [Variables reference](https://docs.github.com/en/actions/reference/workflows-and-actions/variables))

---

<p align="center">
  <a href="README.md">⬅️ Overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="02-a-run-in-six-stages.md"><b>Next: A run in six stages ➡️</b></a>
</p>
