---
type: Tutorial
title: "The Core Components: They nest like boxes"
description: "They nest like boxes, part 2 of 8 of The Core Components."
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
  <a href="README.md">📂 <b>The Core Components</b></a> &nbsp;·&nbsp; Lesson 1 · Part 2 of 8 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# 🪆 They nest like boxes

```mermaid
flowchart TB
    subgraph W["📜 Workflow: unit-tests.yml"]
        direction TB
        subgraph J["📦 Job: unit-testing"]
            direction LR
            S1[👣 Step 1<br/>checkout]:::pink --> S2[👣 Step 2<br/>setup-python]:::pink --> S3[👣 Step 3<br/>run tests]:::pink
        end
        R[🖥️ Runner<br/>a fresh VM]:::green
        J -. runs on .-> R
    end
    E[🔔 Event: push]:::yellow --> W

    classDef yellow fill:#3d2a00,stroke:#e3b341,color:#fff,stroke-width:2px
    classDef pink fill:#3a0f2b,stroke:#f778ba,color:#fff,stroke-width:2px
    classDef green fill:#0f2d17,stroke:#3fb950,color:#fff,stroke-width:2px
```

| A... | contains... | How many |
|---|---|---|
| 🗂️ Repository | Workflows | As many as you like |
| 📜 Workflow | Jobs | One or more |
| 📦 Job | Steps | One or more |
| 📦 Job | A runner | Exactly one |

---

<p align="center">
  <a href="01-four-components-one-picture.md">⬅️ Four components, one picture</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="03-workflow-the-process.md"><b>Next: Workflow: the process ➡️</b></a>
</p>
