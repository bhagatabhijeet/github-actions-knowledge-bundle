---
type: Tutorial
title: "Life of a Workflow Run: The whole run in one picture"
description: "The whole run in one picture, part 1 of 7 of Life of a Workflow Run."
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
  <a href="README.md">📂 <b>Life of a Workflow Run</b></a> &nbsp;·&nbsp; Lesson 2 · Part 1 of 7 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# 🎯 The whole run in one picture

<p align="center">
  <img src="../../assets/images/workflow-run-timeline.svg" alt="One push starts three jobs in parallel on Ubuntu, Windows and macOS runners. Each runs its steps in series and finishes at a different time. The workflow passes only when all three pass" width="100%">
</p>

---

<p align="center">
  <a href="README.md">⬅️ Overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="02-six-stages.md"><b>Next: Six stages ➡️</b></a>
</p>
