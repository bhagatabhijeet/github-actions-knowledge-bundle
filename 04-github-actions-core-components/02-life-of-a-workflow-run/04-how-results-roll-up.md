---
type: Tutorial
title: "Life of a Workflow Run: How results roll up"
description: "Every level gets its own verdict."
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
  <a href="README.md">📂 <b>Life of a Workflow Run</b></a> &nbsp;·&nbsp; Lesson 2 · Part 4 of 7 &nbsp;·&nbsp; ⏱️ 2 min
</p>

# 🚦 How results roll up

Every level gets its own verdict.

```mermaid
flowchart LR
    S["👣 Every step passes"]:::pink --> J["📦 The job passes"]:::purple
    J --> W["📜 Every job passes"]:::blue
    W --> R["✅ The workflow run passes"]:::green

    classDef pink fill:#3a0f2b,stroke:#f778ba,color:#fff,stroke-width:2px
    classDef purple fill:#22123f,stroke:#bc8cff,color:#fff,stroke-width:2px
    classDef blue fill:#0c1d3a,stroke:#58a6ff,color:#fff,stroke-width:2px
    classDef green fill:#0f2d17,stroke:#3fb950,color:#fff,stroke-width:2px
```

| | If... | Then... |
|---|---|---|
| 👣 | A step fails | The steps after it are skipped and its job fails |
| 📦 | The Ubuntu job finishes first | It is marked ✅ straight away, while the others are still running |
| 📜 | All three jobs pass | The workflow run is marked ✅ |
| ❌ | Any one job fails | The workflow run is marked ❌ |

> [!NOTE]
> **Matrix jobs have one extra habit.** By default, when one matrix job fails, GitHub cancels the others that are still running, to save time. That setting is called `fail-fast`. The workflow in this lesson sets `fail-fast: false` so that you always see a result for all three operating systems.

---

<p align="center">
  <a href="03-parallel-outside-serial-inside.md">⬅️ Parallel outside, serial inside</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="05-run-it-yourself.md"><b>Next: Run it yourself ➡️</b></a>
</p>
