---
type: Tutorial
title: "Workflows with Multiple Jobs: Why split into jobs?"
description: "What you gain by splitting one big job into several: clearer logs, parallel speed, partial re-runs, and per-job runners and permissions."
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
  - id: gh-limits
    resource: https://docs.github.com/en/actions/reference/limits
    title: Actions limits
---

<p align="center">
  <a href="README.md">📂 <b>Workflows with Multiple Jobs</b></a> &nbsp;·&nbsp; Lesson 8 · Part 1 of 8 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# ✂️ Why split into jobs?

| | One big job | Several jobs |
|---|---|---|
| 👀 Reading the run | One long log | A job per stage, each with its own ✅ or ❌ |
| ⚡ Speed | Everything in series | Independent jobs run **at the same time** |
| 🔁 Re-running | Start from scratch | **Re-run failed jobs** only |
| 🖥️ Machines | One runner | Different runners per job (Linux build, Windows test, ...) |
| 🔐 Control | Same permissions throughout | Per-job `permissions`, `environment`, approvals |

> [!NOTE]
> **📘 From the GitHub docs:** Each job on a GitHub-hosted runner can run for up to **6 hours**. After that it's stopped and fails. A whole run can last up to 35 days. Parallel jobs are capped too: 20 at once on GitHub Free, 40 on Pro, 60 on Team. ([Actions limits](https://docs.github.com/en/actions/reference/limits))

---

<p align="center">
  <a href="README.md">⬅️ Overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="02-attempt-1-just-split-it.md"><b>Next: Attempt 1: just split it ➡️</b></a>
</p>
