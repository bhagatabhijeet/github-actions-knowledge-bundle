---
type: Tutorial
title: Life of a Workflow Run (Hands-On)
description: Follow one push from event to green tick - three runners provisioned in parallel, steps in series, how job results roll up - then run the Core Components workflow and read its logs and artifacts.
tags: [github-actions, workflow-run, matrix, logs, artifacts, hands-on]
status: stable
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-07T00:00:00Z }
sources:
  - id: gh-workflow-syntax
    resource: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
    title: Workflow syntax for GitHub Actions
  - id: gh-logs
    resource: https://docs.github.com/en/actions/how-tos/monitor-workflows/use-workflow-run-logs
    title: Using workflow run logs
  - id: gh-artifacts
    resource: https://docs.github.com/en/actions/concepts/workflows-and-actions/workflow-artifacts
    title: Workflow artifacts
---

<p align="center">
  <b>Lesson 2 of 14</b> &nbsp;·&nbsp; ⏱️ 20 min &nbsp;·&nbsp; 🛠️ Hands-on
</p>

# 🎬 Life of a Workflow Run

[Lesson 1](../01-the-core-components/README.md) showed the parts standing still. Now someone pushes a commit. What happens, in what order, and where do you look to see it?

## 🗺️ In this topic

7 subtopics, about 13 minutes in all. Read them in order, or jump to the one you need.

| # | Subtopic | Time |
|---|---|---|
| 1 | 🎯 [**The whole run in one picture**](01-the-whole-run-in-one-picture.md) | 1 min |
| 2 | 🪜 [**Six stages**](02-six-stages.md) | 2 min |
| 3 | ⏱️ [**Parallel outside, serial inside**](03-parallel-outside-serial-inside.md) | 1 min |
| 4 | 🚦 [**How results roll up**](04-how-results-roll-up.md) | 2 min |
| 5 | 🛠️ [**Run it yourself**](05-run-it-yourself.md) | 4 min |
| 6 | 🗺️ [**Where everything lives**](06-where-everything-lives.md) | 1 min |
| 7 | ✅ [**Checkpoint**](07-checkpoint.md) | 2 min |

<p align="center">
  <a href="01-the-whole-run-in-one-picture.md"><b>▶️ Start with The whole run in one picture</b></a>
</p>

## 🎯 What you learned

- A run goes through six stages: **event, queue, provision, execute, report, clean up**
- **Jobs in parallel, steps in series**, so runners finish at different times
- A job passes when all its steps pass; **a run passes when all its jobs pass**
- **Logs and artifacts outlive the runner** and are found in the Actions tab
- Matrix jobs cancel each other on failure unless you set `fail-fast: false`

---

<p align="center">
  <a href="../01-the-core-components/README.md">⬅️ The Core Components</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="../index.md">📚 Chapter 4</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="../03-github-hosted-vs-self-hosted-runners/README.md"><b>Next: Hosted vs Self-Hosted Runners ➡️</b></a>
</p>
