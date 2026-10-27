---
type: Tutorial
title: "The Core Components: Four components, one picture"
description: "Four components do the work. An event sets them off."
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
  <a href="README.md">📂 <b>The Core Components</b></a> &nbsp;·&nbsp; Lesson 1 · Part 1 of 8 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# 🎯 Four components, one picture

<p align="center">
  <img src="../../assets/images/workflow-yaml-annotated.svg" alt="A workflow file with each part labelled: the whole file is the workflow, the on key is the event, the unit-testing block is the job, runs-on and matrix choose the runner, and the list under steps holds the steps" width="100%">
</p>

Four components do the work. An **event** sets them off.

| | Component | In one line | In the file |
|---|---|---|---|
| 📜 | **Workflow** | An automated process, written as one YAML file | The whole file |
| 📦 | **Job** | A group of steps that share one machine | An entry under `jobs:` |
| 👣 | **Step** | A single task: an action or a command | An item under `steps:` |
| 🖥️ | **Runner** | The machine that executes a job | Chosen by `runs-on:` |

---

<p align="center">
  <a href="README.md">⬅️ Overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="02-they-nest-like-boxes.md"><b>Next: They nest like boxes ➡️</b></a>
</p>
