---
type: Tutorial
title: "Triggering Workflows in Detail: `pull_request` vs `pull_request_target`"
description: "These look alike but run in very different security contexts."
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
  <a href="README.md">📂 <b>Triggering Workflows in Detail</b></a> &nbsp;·&nbsp; Lesson 13 · Part 8 of 12 &nbsp;·&nbsp; ⏱️ 2 min
</p>

# ⚖️ `pull_request` vs `pull_request_target`

These look alike but run in very different security contexts.

| | `pull_request` | `pull_request_target` |
|---|---|---|
| Workflow file and code come from | the PR's merge commit | the **base repo's default branch** |
| Secrets for PRs from forks | ❌ none (read-only `GITHUB_TOKEN`) | ✅ **yes**, plus a write token |
| Runs if the PR has a merge conflict | ❌ no | ✅ yes |
| Good for | building and testing the PR's code | labelling, commenting, triaging |

> [!CAUTION]
> Never check out and run a fork's code inside `pull_request_target`. That would give a stranger's code your secrets and a write token. GitHub's docs warn about this directly: it can lead to cache poisoning and to the PR gaining secrets or write access it shouldn't have. Use `pull_request` to test code, and `pull_request_target` only to act on the PR's metadata.

---

<p align="center">
  <a href="07-the-loop-guard-github-token-doesn-t.md">⬅️ The loop guard: `GITHUB_TOKEN` doesn't start new runs</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="09-which-trigger-do-i-need.md"><b>Next: Which trigger do I need? ➡️</b></a>
</p>
