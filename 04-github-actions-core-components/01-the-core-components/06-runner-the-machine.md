---
type: Tutorial
title: "The Core Components: Runner: the machine"
description: "A runner is a virtual machine that executes a job. You never create it. You ask for one with runs-on, and GitHub provisions it when the job starts."
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
  <a href="README.md">📂 <b>The Core Components</b></a> &nbsp;·&nbsp; Lesson 1 · Part 6 of 8 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# 🖥️ Runner: the machine

A runner is a virtual machine that executes a job. You never create it. You **ask for one** with `runs-on`, and GitHub provisions it when the job starts.

```yaml
runs-on: ubuntu-latest      # or windows-latest, macos-latest
```

Because GitHub is doing the hosting, these are called **GitHub-hosted runners**. [Lesson 3](../03-github-hosted-vs-self-hosted-runners/README.md) compares them with machines you host yourself.

---

<p align="center">
  <a href="05-step-one-task.md">⬅️ Step: one task</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="07-one-job-three-machines.md"><b>Next: One job, three machines ➡️</b></a>
</p>
