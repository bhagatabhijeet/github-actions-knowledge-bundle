---
type: Tutorial
title: "Workflows with Multiple Jobs: Fix 1: put the jobs in order with `needs`"
description: "Use needs: with one job ID or a list to make jobs wait for each other."
tags: [github-actions, jobs, needs, parallel, artifacts, hands-on]
status: stable
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-26T00:00:00Z }
sources:
  - id: gh-workflow-syntax
    resource: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
    title: Workflow syntax for GitHub Actions
  - id: gh-artifacts
    resource: https://docs.github.com/en/actions/tutorials/store-and-share-data
    title: Store and share data with workflow artifacts
  - id: upload-artifact
    resource: https://github.com/actions/upload-artifact
    title: actions/upload-artifact
  - id: download-artifact
    resource: https://github.com/actions/download-artifact
    title: actions/download-artifact
---

<p align="center">
  <a href="README.md">📂 <b>Workflows with Multiple Jobs</b></a> &nbsp;·&nbsp; Lesson 8 · Part 3 of 8 &nbsp;·&nbsp; ⏱️ 2 min
</p>

# ⏩ Fix 1: put the jobs in order with `needs`

```yaml
  test_job:
    needs: build_job          # wait for build_job to succeed
    runs-on: ubuntu-latest
    ...

  deploy_job:
    needs: test_job           # wait for test_job to succeed
    runs-on: ubuntu-latest
    ...
```

`needs:` takes one job ID or a list:

| You write | What happens |
|---|---|
| *(nothing)* | Starts immediately, in parallel with the others |
| `needs: build_job` | Starts after `build_job` **succeeds** |
| `needs: [lint, unit_tests]` | Starts after **both** succeed. A **fan-in** |
| Two jobs each with `needs: build_job` | Both start together after build. A **fan-out** |

> [!IMPORTANT]
> **If a needed job fails, the jobs after it are skipped**, not failed. That's the whole point: never deploy something whose tests didn't pass. To run a job anyway, for example to send a failure alert, add `if: ${{ always() }}` or `if: ${{ failure() }}` to it.

👉 [Lesson 9](../09-executing-jobs-in-sequence/README.md) goes deeper into `needs`: failure handling, status functions and job results.

Now the jobs run in order, but `test_job` still fails. It waited for build, then started on a **new** runner that has never seen `dragon.txt`.

---

<p align="center">
  <a href="02-attempt-1-just-split-it.md">⬅️ Attempt 1: just split it</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="04-fix-2-carry-the-file-with-artifacts.md"><b>Next: Fix 2: carry the file with artifacts ➡️</b></a>
</p>
