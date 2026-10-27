---
type: Tutorial
title: "Triggering Workflows in Detail: The loop guard: `GITHUB_TOKEN` doesn't start new runs"
description: "Picture a workflow that runs on push and pushes a formatting fix. If that push started the workflow again, it would loop forever. GitHub prevents this:"
tags: [github-actions, triggers, events, on, workflow_dispatch, schedule, cron, repository_dispatch, workflow_run, filters, hands-on]
status: stable
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-26T00:00:00Z }
sources:
  - id: gh-workflows-concepts
    resource: https://docs.github.com/en/actions/concepts/workflows-and-actions/workflows#workflow-triggers
    title: Workflows - Workflow triggers
  - id: gh-events
    resource: https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows
    title: Events that trigger workflows
  - id: gh-workflow-syntax
    resource: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
    title: Workflow syntax for GitHub Actions
---

<p align="center">
  <a href="README.md">📂 <b>Triggering Workflows in Detail</b></a> &nbsp;·&nbsp; Lesson 13 · Part 7 of 12 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# 🔁 The loop guard: `GITHUB_TOKEN` doesn't start new runs

Picture a workflow that runs on `push` and pushes a formatting fix. If that push started the workflow again, it would loop forever. GitHub prevents this:

> **With the exception of `workflow_dispatch` and `repository_dispatch`, events triggered by the `GITHUB_TOKEN` do not create new workflow runs.**

| A workflow using `GITHUB_TOKEN`... | Starts a new run? |
|---|---|
| pushes a commit or tag | ❌ no |
| opens an issue or creates a release | ❌ no |
| calls `gh workflow run` (`workflow_dispatch`) | ✅ yes |
| calls the dispatches API (`repository_dispatch`) | ✅ yes |

Need a push from a workflow to trigger CI on purpose? Use a **GitHub App token** or a personal access token instead. Those events do create runs, so take care not to build a loop yourself.

---

<p align="center">
  <a href="06-triggers-from-outside-and-from-other-workflows.md">⬅️ Triggers from outside and from other workflows</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="08-pull-request-vs-pull-request-target.md"><b>Next: `pull_request` vs `pull_request_target` ➡️</b></a>
</p>
