---
type: Tutorial
title: "Triggering Workflows in Detail: Common mistakes"
description: "Common mistakes, part 10 of 12 of Triggering Workflows in Detail."
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
  <a href="README.md">📂 <b>Triggering Workflows in Detail</b></a> &nbsp;·&nbsp; Lesson 13 · Part 10 of 12 &nbsp;·&nbsp; ⏱️ 2 min
</p>

# 🪤 Common mistakes

| Symptom | Cause | Fix |
|---|---|---|
| No **Run workflow** button | the workflow file isn't on the default branch | merge it to `main` first |
| Scheduled run is late or missing | top-of-the-hour load, or the repo was inactive for 60 days | use an odd minute; re-enable in the Actions tab |
| Schedule fires at the "wrong" hour | cron is UTC | convert, or set a `timezone:` |
| PR workflow ignores labels or closing | `pull_request` only defaults to `opened`, `synchronize`, `reopened` | add `types:` |
| Tag pushes stopped running CI | only `branches:` is set | add `tags:` too |
| `if: github.event.inputs.flag` is always true | the value is the string `'false'` | use `inputs.flag` |
| A bot's push doesn't start CI | the `GITHUB_TOKEN` loop guard | use a GitHub App token |
| Workflow edits on a branch don't affect `schedule` | schedule reads `main` | merge first |

---

<p align="center">
  <a href="09-which-trigger-do-i-need.md">⬅️ Which trigger do I need?</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="11-try-it-yourself.md"><b>Next: Try it yourself ➡️</b></a>
</p>
