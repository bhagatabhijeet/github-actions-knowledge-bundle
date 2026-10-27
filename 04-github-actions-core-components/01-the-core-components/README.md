---
type: Tutorial
title: The Core Components
description: Workflow, job, step and runner seen inside one real workflow file - what each part is, how they nest, and how a small matrix turns one job into three machines.
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
  <img src="../../assets/images/chapter-04-banner.svg" alt="Chapter 4: GitHub Actions Core Components" width="100%">
</p>

<p align="center">
  <b>Lesson 1 of 14</b> &nbsp;·&nbsp; ⏱️ 7 min read &nbsp;·&nbsp; 🟢 Beginner
</p>

# 🧱 The Core Components

In [Chapter 3](../../03-problem-with-traditional-ci-cd-tools/01-the-problem-statement/README.md), Abhijeet chose GitHub Actions because it let his team build pipelines without running servers. Now it's time to open the box.

You met the vocabulary in [Lesson 1.2](../../01-introduction-to-github-actions/02-core-concepts/README.md). This chapter puts it in motion. We'll take **one small workflow** and follow it for three lessons: what it's made of, what happens when it runs, and what kind of machine runs it.

## 🗺️ In this topic

8 subtopics, about 10 minutes in all. Read them in order, or jump to the one you need.

| # | Subtopic | Time |
|---|---|---|
| 1 | 🎯 [**Four components, one picture**](01-four-components-one-picture.md) | 1 min |
| 2 | 🪆 [**They nest like boxes**](02-they-nest-like-boxes.md) | 1 min |
| 3 | 📜 [**Workflow: the process**](03-workflow-the-process.md) | 1 min |
| 4 | 📦 [**Job: work for one machine**](04-job-work-for-one-machine.md) | 1 min |
| 5 | 👣 [**Step: one task**](05-step-one-task.md) | 1 min |
| 6 | 🖥️ [**Runner: the machine**](06-runner-the-machine.md) | 1 min |
| 7 | ✖️ [**One job, three machines**](07-one-job-three-machines.md) | 2 min |
| 8 | ✅ [**Checkpoint**](08-checkpoint.md) | 2 min |

<p align="center">
  <a href="01-four-components-one-picture.md"><b>▶️ Start with Four components, one picture</b></a>
</p>

## 🎯 What you learned

- The core components are **workflow, job, step and runner**, set off by an **event**
- They nest: a workflow holds jobs, a job holds steps, and each job has one runner
- **Jobs run in parallel; steps run in series**
- You don't create runners. You **ask for them** with `runs-on`
- A **matrix** turns one job definition into several jobs on several machines

---

<p align="center">
  <a href="../../03-problem-with-traditional-ci-cd-tools/04-cheat-sheet-and-quiz/README.md">⬅️ Chapter 3 Quiz</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="../index.md">📚 Chapter 4</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="../02-life-of-a-workflow-run/README.md"><b>Next: Life of a Workflow Run ➡️</b></a>
</p>
