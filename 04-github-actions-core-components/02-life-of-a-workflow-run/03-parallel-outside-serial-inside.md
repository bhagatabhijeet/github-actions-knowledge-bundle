---
type: Tutorial
title: "Life of a Workflow Run: Parallel outside, serial inside"
description: "Two rules explain the shape of the picture."
tags: [github-actions, workflow-run, matrix, logs, artifacts, hands-on]
status: stable
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-26T00:00:00Z }
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
  - id: gh-limits
    resource: https://docs.github.com/en/actions/reference/limits
    title: Actions limits
---

<p align="center">
  <a href="README.md">📂 <b>Life of a Workflow Run</b></a> &nbsp;·&nbsp; Lesson 2 · Part 3 of 7 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# ⏱️ Parallel outside, serial inside

Two rules explain the shape of the picture.

| | Rule | In the picture |
|---|---|---|
| ↔️ | **Jobs run in parallel** | Three lanes start together |
| ➡️ | **Steps run in series** | Boxes in a lane follow one another |

The three runners don't wait for each other and don't finish together. Windows usually takes the longest to start. That's fine: each job is judged on its own.

> [!NOTE]
> **📘 From the GitHub docs:** "Parallel" has a ceiling. On the Free plan you get up to **20 concurrent jobs** on standard GitHub-hosted runners. Extra jobs wait in the queue until a slot frees up. ([Actions limits](https://docs.github.com/en/actions/reference/limits))

---

<p align="center">
  <a href="02-six-stages.md">⬅️ Six stages</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="04-how-results-roll-up.md"><b>Next: How results roll up ➡️</b></a>
</p>
