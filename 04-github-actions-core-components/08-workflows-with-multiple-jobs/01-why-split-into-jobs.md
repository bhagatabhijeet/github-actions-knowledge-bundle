---
type: Tutorial
title: "Workflows with Multiple Jobs: Why split into jobs?"
description: "Why split into jobs?, part 1 of 8 of Workflows with Multiple Jobs."
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

---

<p align="center">
  <a href="README.md">⬅️ Overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="02-attempt-1-just-split-it.md"><b>Next: Attempt 1: just split it ➡️</b></a>
</p>
