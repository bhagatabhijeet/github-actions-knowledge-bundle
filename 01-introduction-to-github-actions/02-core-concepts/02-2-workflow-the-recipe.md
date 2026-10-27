---
type: Tutorial
title: "The Six Core Concepts: 2. Workflow: the recipe"
description: "A workflow is one YAML file in .github/workflows/. It names the events it listens for and the jobs to run when they fire."
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
  <a href="README.md">📂 <b>The Six Core Concepts</b></a> &nbsp;·&nbsp; Lesson 2 · Part 2 of 8 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# 📜 2. Workflow: the recipe

A workflow is one YAML file in `.github/workflows/`. It names the events it listens for and the jobs to run when they fire.

- One repository can have **many** workflows (one for tests, one for deploys, one for issue triage)
- Each time a workflow is triggered, you get a **workflow run** with its own logs and its own ✅ or ❌

---

<p align="center">
  <a href="01-1-event-the-trigger.md">⬅️ 1. Event: the trigger</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="03-3-job-a-unit-of-work-on.md"><b>Next: 3. Job: a unit of work on one machine ➡️</b></a>
</p>
