---
type: Tutorial
title: "Anatomy of a Pipeline: Pipelines in GitHub Actions"
description: "GitHub Actions has no keyword called pipeline or stage. You build them from pieces you already know:"
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
  <a href="README.md">📂 <b>Anatomy of a Pipeline</b></a> &nbsp;·&nbsp; Lesson 4 · Part 2 of 7 &nbsp;·&nbsp; ⏱️ 2 min
</p>

# 🧩 Pipelines in GitHub Actions

GitHub Actions has no keyword called `pipeline` or `stage`. You build them from pieces you already know:

> [!IMPORTANT]
> **A stage is a job. The pipeline's order comes from `needs`.**

```yaml
jobs:
  lint:
    runs-on: ubuntu-latest
    steps: [...]

  test:
    needs: lint            # 👈 stage 2 waits for stage 1
    runs-on: ubuntu-latest
    steps: [...]

  package:
    needs: test            # 👈 stage 3 waits for stage 2
    runs-on: ubuntu-latest
    steps: [...]
```

GitHub draws that as a graph on the run page:

```mermaid
flowchart LR
    L[🧹 lint]:::blue --> T[🧪 test]:::purple --> P[📦 package]:::pink

    classDef blue fill:#0c1d3a,stroke:#58a6ff,color:#fff,stroke-width:2px
    classDef purple fill:#22123f,stroke:#bc8cff,color:#fff,stroke-width:2px
    classDef pink fill:#3a0f2b,stroke:#f778ba,color:#fff,stroke-width:2px
```

If `lint` fails, `test` and `package` are **skipped** automatically. That's the quality gate, for free.

---

<p align="center">
  <a href="01-the-five-stations.md">⬅️ The five stations</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="03-fan-out-and-fan-in.md"><b>Next: Fan-out and fan-in ➡️</b></a>
</p>
