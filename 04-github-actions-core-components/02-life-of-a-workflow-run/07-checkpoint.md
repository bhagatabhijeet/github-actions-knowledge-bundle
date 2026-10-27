---
type: Tutorial
title: "Life of a Workflow Run: Checkpoint"
description: "Not yet. The run is only marked successful once every job has finished successfully. Until then it shows as in progress."
tags: [github-actions, workflow-run, matrix, logs, artifacts, hands-on]
status: stable
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-07T00:00:00Z }
sources:
  - id: gh-workflow-syntax
    resource: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
    title: Workflow syntax for GitHub Actions
  - id: gh-logs
    resource: https://docs.github.com/en/actions/how-tos/monitor-workflows/use-workflow-run-logs
    title: Using workflow run logs
  - id: gh-artifacts
    resource: https://docs.github.com/en/actions/concepts/workflows-and-actions/workflow-artifacts
    title: Workflow artifacts
---

<p align="center">
  <a href="README.md">📂 <b>Life of a Workflow Run</b></a> &nbsp;·&nbsp; Lesson 2 · Part 7 of 7 &nbsp;·&nbsp; ⏱️ 2 min
</p>

# ✅ Checkpoint

<details>
<summary><b>The Ubuntu job has finished and is green. Is the workflow run green?</b></summary>

<br>

Not yet. The run is only marked successful once every job has finished successfully. Until then it shows as in progress.

</details>

<details>
<summary><b>Why did the artifacts disappear when you broke the test?</b></summary>

<br>

The test step failed, so the steps after it were skipped, including the upload. No upload, no artifact.

</details>

<details>
<summary><b>A runner is destroyed when its job ends. How can you still read its output an hour later?</b></summary>

<br>

Logs are streamed to GitHub while the job runs, and artifacts are uploaded to GitHub's storage. Both are kept after the machine is gone.

</details>

<details>
<summary><b>What does <code>fail-fast: false</code> change?</b></summary>

<br>

With the default (`true`), one failing matrix job cancels the others still in progress. With `false`, every matrix job runs to the end, so you see results for all of them.

</details>

---

<p align="center">
  <a href="06-where-everything-lives.md">⬅️ Where everything lives</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md#-what-you-learned"><b>Wrap up: What you learned ➡️</b></a>
</p>
