---
type: Tutorial
title: "The Core Components: Step: one task"
description: "Steps are the individual tasks inside a job. They run one after another, top to bottom, on the same machine, so each step can use what the previous one left behind."
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
  <a href="README.md">📂 <b>The Core Components</b></a> &nbsp;·&nbsp; Lesson 1 · Part 5 of 8 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# 👣 Step: one task

Steps are the individual tasks inside a job. They run **one after another, top to bottom**, on the same machine, so each step can use what the previous one left behind.

| | Our workflow's steps | Kind | Why it's there |
|---|---|---|---|
| 1 | `uses: actions/checkout@v7` | Action | Copies the repository onto the runner |
| 2 | `uses: actions/setup-python@v7` | Action | Installs the Python version we asked for |
| 3 | `run: python -m unittest discover` | Command | Runs the tests |

Order matters. Step 3 can only test the code because step 1 fetched it.

---

<p align="center">
  <a href="04-job-work-for-one-machine.md">⬅️ Job: work for one machine</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="06-runner-the-machine.md"><b>Next: Runner: the machine ➡️</b></a>
</p>
