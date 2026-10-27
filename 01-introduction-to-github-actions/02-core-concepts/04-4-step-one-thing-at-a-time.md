---
type: Tutorial
title: "The Six Core Concepts: 4. Step: one thing at a time"
description: "Steps are the individual tasks inside a job. They run in order, top to bottom, and because they share a runner, they share its files. Step 1 checks out the code, so step 2 can test it."
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
  <a href="README.md">📂 <b>The Six Core Concepts</b></a> &nbsp;·&nbsp; Lesson 2 · Part 4 of 8 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# 👣 4. Step: one thing at a time

Steps are the individual tasks inside a job. They run **in order, top to bottom**, and because they share a runner, they share its files. Step 1 checks out the code, so step 2 can test it.

If a step fails, the remaining steps are skipped and the job is marked ❌.

A step does exactly one of two things:

```yaml
steps:
  - uses: actions/checkout@v7          # use an action
  - run: python -m unittest discover   # run a command
```

---

<p align="center">
  <a href="03-3-job-a-unit-of-work-on.md">⬅️ 3. Job: a unit of work on one machine</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="05-5-action-a-reusable-building-block.md"><b>Next: 5. Action: a reusable building block ➡️</b></a>
</p>
