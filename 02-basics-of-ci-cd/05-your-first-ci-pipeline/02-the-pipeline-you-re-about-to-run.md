---
type: Tutorial
title: "Your First CI Pipeline: The pipeline you're about to run"
description: "Three stages, five jobs, one artifact."
resource: /.github/workflows/02-ci-basics.yml
tags: [ci-cd, hands-on, pipeline, matrix, artifacts, python, pull-requests]
status: stable
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-07T00:00:00Z }
sources:
  - id: gh-python
    resource: https://docs.github.com/en/actions/tutorials/build-and-test-code/python
    title: Building and testing Python
  - id: gh-artifacts
    resource: https://docs.github.com/en/actions/tutorials/store-and-share-data
    title: Store and share data with workflow artifacts
  - id: gh-concurrency
    resource: https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/control-workflow-concurrency
    title: Control the concurrency of workflows and jobs
---

<p align="center">
  <a href="README.md">📂 <b>Your First CI Pipeline</b></a> &nbsp;·&nbsp; Lesson 5 · Part 2 of 9 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# 🗺️ The pipeline you're about to run

```mermaid
flowchart LR
    E((🔔 push or PR)):::yellow --> L[🧹 lint]:::blue
    L --> T1[🧪 test 3.12]:::purple
    L --> T2[🧪 test 3.13]:::purple
    L --> T3[🧪 test 3.14]:::purple
    T1 --> P[📦 package]:::pink
    T2 --> P
    T3 --> P
    P --> A[(🎁 greeter artifact)]:::green

    classDef yellow fill:#3d2a00,stroke:#e3b341,color:#fff,stroke-width:2px
    classDef blue fill:#0c1d3a,stroke:#58a6ff,color:#fff,stroke-width:2px
    classDef purple fill:#22123f,stroke:#bc8cff,color:#fff,stroke-width:2px
    classDef pink fill:#3a0f2b,stroke:#f778ba,color:#fff,stroke-width:2px
    classDef green fill:#0f2d17,stroke:#3fb950,color:#fff,stroke-width:2px
```

Three stages, five jobs, one artifact.

---

<p align="center">
  <a href="01-the-cast.md">⬅️ The cast</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="03-the-workflow-piece-by-piece.md"><b>Next: The workflow, piece by piece ➡️</b></a>
</p>
