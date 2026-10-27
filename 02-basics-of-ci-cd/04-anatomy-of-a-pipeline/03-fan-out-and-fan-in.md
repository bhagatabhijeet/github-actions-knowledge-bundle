---
type: Tutorial
title: "Anatomy of a Pipeline: Fan-out and fan-in"
description: "needs takes a list, so stages can run side by side and then join up."
tags: [ci-cd, pipeline, stages, artifacts, matrix, needs, caching]
status: stable
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-07T00:00:00Z }
sources:
  - id: gh-syntax
    resource: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
    title: Workflow syntax for GitHub Actions
  - id: gh-artifacts
    resource: https://docs.github.com/en/actions/concepts/workflows-and-actions/workflow-artifacts
    title: Workflow artifacts
  - id: gh-cache
    resource: https://docs.github.com/en/actions/concepts/workflows-and-actions/dependency-caching
    title: Dependency caching
---

<p align="center">
  <a href="README.md">📂 <b>Anatomy of a Pipeline</b></a> &nbsp;·&nbsp; Lesson 4 · Part 3 of 7 &nbsp;·&nbsp; ⏱️ 2 min
</p>

# 🔀 Fan-out and fan-in

`needs` takes a list, so stages can run side by side and then join up.

```yaml
  package:
    needs: [lint, test]
```

```mermaid
flowchart LR
    S((🔔 push)):::yellow --> L[🧹 lint]:::blue
    S --> T[🧪 test]:::purple
    L --> P[📦 package]:::pink
    T --> P
    P --> D[🚀 deploy]:::green

    classDef yellow fill:#3d2a00,stroke:#e3b341,color:#fff,stroke-width:2px
    classDef blue fill:#0c1d3a,stroke:#58a6ff,color:#fff,stroke-width:2px
    classDef purple fill:#22123f,stroke:#bc8cff,color:#fff,stroke-width:2px
    classDef pink fill:#3a0f2b,stroke:#f778ba,color:#fff,stroke-width:2px
    classDef green fill:#0f2d17,stroke:#3fb950,color:#fff,stroke-width:2px
```

| Shape | Good for | Trade-off |
|---|---|---|
| **Serial** (`lint → test`) | Failing fast, saving minutes | Slower when everything passes |
| **Parallel** (`lint` + `test`) | Fastest total time | Runs tests even when lint would fail |

Neither is right in general. Fast checks first in serial, slow checks in parallel, is a sensible default.

📎 Full example: [assets/snippets/job-dependencies.yml](../../assets/snippets/job-dependencies.yml)

---

<p align="center">
  <a href="02-pipelines-in-github-actions.md">⬅️ Pipelines in GitHub Actions</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="04-the-matrix-one-job-many-variations.md"><b>Next: The matrix: one job, many variations ➡️</b></a>
</p>
