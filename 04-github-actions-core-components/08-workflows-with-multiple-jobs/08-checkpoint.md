---
type: Tutorial
title: "Workflows with Multiple Jobs: Checkpoint"
description: "All at the same time, each on its own runner. There is no order."
tags: [github-actions, jobs, needs, parallel, artifacts, hands-on]
status: stable
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-25T00:00:00Z }
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
  <a href="README.md">📂 <b>Workflows with Multiple Jobs</b></a> &nbsp;·&nbsp; Lesson 8 · Part 8 of 8 &nbsp;·&nbsp; ⏱️ 2 min
</p>

# ✅ Checkpoint

<details>
<summary><b>A workflow has three jobs and no <code>needs:</code>. In what order do they run?</b></summary>

<br>

All at the same time, each on its own runner. There is no order.

</details>

<details>
<summary><b><code>test_job</code> has <code>needs: build_job</code> but still can't find the file <code>build_job</code> created. Why?</b></summary>

<br>

`needs:` only controls timing. Each job runs on a fresh machine, so the file must be passed with `upload-artifact` and `download-artifact`.

</details>

<details>
<summary><b><code>test_job</code> fails. What happens to <code>deploy_job</code>, which needs it?</b></summary>

<br>

It's skipped, and the workflow run is marked as failed. Add `if: ${{ always() }}` to a job only if it must run regardless.

</details>

<details>
<summary><b>You need to pass a version string like <code>1.4.27</code> from build to deploy. Artifact or output?</b></summary>

<br>

A job output. Artifacts are for files; outputs are for small strings, read as `needs.<job>.outputs.<name>`.

</details>

---

<p align="center">
  <a href="07-try-it-yourself.md">⬅️ Try it yourself</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md#-what-you-learned"><b>Wrap up: What you learned ➡️</b></a>
</p>
