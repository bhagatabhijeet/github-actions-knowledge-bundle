---
type: Tutorial
title: "The Core Components: One job, three machines"
description: "Look again at the picture. The job doesn't name one operating system. It names a matrix of three:"
tags: [github-actions, core-components, workflow, job, step, runner, matrix]
status: stable
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-07T00:00:00Z }
sources:
  - id: gh-understand
    resource: https://docs.github.com/en/actions/get-started/understand-github-actions
    title: Understanding GitHub Actions
  - id: gh-workflow-syntax
    resource: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
    title: Workflow syntax for GitHub Actions
  - id: gh-hosted-runners
    resource: https://docs.github.com/en/actions/concepts/runners/github-hosted-runners
    title: GitHub-hosted runners
---

<p align="center">
  <a href="README.md">📂 <b>The Core Components</b></a> &nbsp;·&nbsp; Lesson 1 · Part 7 of 8 &nbsp;·&nbsp; ⏱️ 2 min
</p>

# ✖️ One job, three machines

Look again at the picture. The job doesn't name one operating system. It names a **matrix** of three:

```yaml
jobs:
  unit-testing:
    runs-on: ${{ matrix.os }}
    strategy:
      matrix:
        os: [ubuntu-latest, windows-latest, macos-latest]
```

GitHub reads that as three jobs, identical except for the value of `matrix.os`:

```mermaid
flowchart LR
    D["📦 unit-testing<br/>written once"]:::purple --> U["🐧 unit-testing<br/>ubuntu-latest"]:::green
    D --> W["🪟 unit-testing<br/>windows-latest"]:::green
    D --> M["🍎 unit-testing<br/>macos-latest"]:::green

    classDef purple fill:#22123f,stroke:#bc8cff,color:#fff,stroke-width:2px
    classDef green fill:#0f2d17,stroke:#3fb950,color:#fff,stroke-width:2px
```

You wrote the job once. GitHub provisions **three virtual machines** and runs the same three steps on each.

> [!TIP]
> This is Abhijeet's "several versions without conflicts" problem from Chapter 3, solved in four lines. Swap `os` for `node-version` and the same idea tests three Node.js releases.

---

<p align="center">
  <a href="06-runner-the-machine.md">⬅️ Runner: the machine</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="08-checkpoint.md"><b>Next: Checkpoint ➡️</b></a>
</p>
