---
type: Tutorial
title: "The Core Components: Checkpoint"
description: "One to one. Every job runs on exactly one runner, and all of that job's steps share it."
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
  <a href="README.md">📂 <b>The Core Components</b></a> &nbsp;·&nbsp; Lesson 1 · Part 8 of 8 &nbsp;·&nbsp; ⏱️ 2 min
</p>

# ✅ Checkpoint

<details>
<summary><b>What is the relationship between a job and a runner?</b></summary>

<br>

One to one. Every job runs on exactly one runner, and all of that job's steps share it.

</details>

<details>
<summary><b>Steps run in series, jobs run in parallel. Why the difference?</b></summary>

<br>

Steps share a machine and build on each other's results, so order matters. Jobs are on separate machines with nothing in common, so there is no reason to make them wait.

</details>

<details>
<summary><b>A job has a matrix with three operating systems. How many runners does GitHub provision?</b></summary>

<br>

Three. The matrix expands one job definition into three jobs, and each job gets its own runner.

</details>

<details>
<summary><b>Where must a workflow file be saved?</b></summary>

<br>

In `.github/workflows/` in the repository, with a `.yml` or `.yaml` extension.

</details>

---

<p align="center">
  <a href="07-one-job-three-machines.md">⬅️ One job, three machines</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md#-what-you-learned"><b>Wrap up: What you learned ➡️</b></a>
</p>
