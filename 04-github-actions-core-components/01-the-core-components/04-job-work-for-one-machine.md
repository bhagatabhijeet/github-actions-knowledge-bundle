---
type: Tutorial
title: "The Core Components: Job: work for one machine"
description: "Inside a workflow you define one or more jobs. A job is a list of steps that all run on the same runner."
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
  <a href="README.md">📂 <b>The Core Components</b></a> &nbsp;·&nbsp; Lesson 1 · Part 4 of 8 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# 📦 Job: work for one machine

Inside a workflow you define one or more jobs. A job is a list of steps that all run **on the same runner**.

```yaml
jobs:
  unit-testing:          # the job's id, chosen by you
    runs-on: ubuntu-latest
    steps:
      - ...
```

> [!IMPORTANT]
> **Jobs run in parallel unless you say otherwise**, and each one starts on its own clean machine. Nothing is shared between jobs by default.

---

<p align="center">
  <a href="03-workflow-the-process.md">⬅️ Workflow: the process</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="05-step-one-task.md"><b>Next: Step: one task ➡️</b></a>
</p>
