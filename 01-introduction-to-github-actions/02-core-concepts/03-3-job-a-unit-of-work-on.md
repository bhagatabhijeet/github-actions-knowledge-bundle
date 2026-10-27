---
type: Tutorial
title: "The Six Core Concepts: 3. Job: a unit of work on one machine"
description: "A job is a group of steps that run on the same runner."
tags: [github-actions, concepts, workflow, job, step, action, runner, event]
status: stable
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-07T00:00:00Z }
sources:
  - id: gh-understand
    resource: https://docs.github.com/en/actions/get-started/understand-github-actions
    title: Understanding GitHub Actions
  - id: gh-runners
    resource: https://docs.github.com/en/actions/concepts/runners/github-hosted-runners
    title: GitHub-hosted runners
  - id: gh-events
    resource: https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows
    title: Events that trigger workflows
---

<p align="center">
  <a href="README.md">📂 <b>The Six Core Concepts</b></a> &nbsp;·&nbsp; Lesson 2 · Part 3 of 8 &nbsp;·&nbsp; ⏱️ 2 min
</p>

# 📦 3. Job: a unit of work on one machine

A job is a group of steps that run **on the same runner**.

Two rules to memorise:

> [!IMPORTANT]
> 1. **Jobs run in parallel by default.** Add `needs:` to put them in order.
> 2. **Jobs do not share files.** Each one starts on a brand-new machine.

```mermaid
flowchart LR
    L[🧹 lint]:::blue --> P[📦 package]:::pink
    T[🧪 test]:::purple --> P
    P --> D[🚀 deploy]:::green

    classDef blue fill:#0c1d3a,stroke:#58a6ff,color:#fff,stroke-width:2px
    classDef purple fill:#22123f,stroke:#bc8cff,color:#fff,stroke-width:2px
    classDef pink fill:#3a0f2b,stroke:#f778ba,color:#fff,stroke-width:2px
    classDef green fill:#0f2d17,stroke:#3fb950,color:#fff,stroke-width:2px
```

Here `lint` and `test` run side by side, `package` waits for both, and `deploy` waits for `package`. The YAML for exactly this shape is in [assets/snippets/job-dependencies.yml](../../assets/snippets/job-dependencies.yml).

---

<p align="center">
  <a href="02-2-workflow-the-recipe.md">⬅️ 2. Workflow: the recipe</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="04-4-step-one-thing-at-a-time.md"><b>Next: 4. Step: one thing at a time ➡️</b></a>
</p>
