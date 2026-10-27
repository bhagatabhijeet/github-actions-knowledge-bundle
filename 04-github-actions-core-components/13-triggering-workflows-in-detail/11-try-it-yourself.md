---
type: Tutorial
title: "Triggering Workflows in Detail: Try it yourself"
description: "The companion workflow 04-triggers.yml listens on all four doors and prints what started it."
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
  <a href="README.md">📂 <b>Triggering Workflows in Detail</b></a> &nbsp;·&nbsp; Lesson 13 · Part 11 of 12 &nbsp;·&nbsp; ⏱️ 2 min
</p>

# 🛠️ Try it yourself

The companion workflow [`04-triggers.yml`](../../.github/workflows/04-triggers.yml) listens on all four doors and prints what started it.

1. **Push door.** Change a comment in `04-triggers.yml` and push to `main`. Then change any other file. Only the first push starts a run, because of the `paths:` filter.
2. **Manual door.** Go to **Actions → 04 - Triggers → Run workflow**. Pick `production`, type a version, untick **dry-run** and run it. In the log, the dry-run step is **skipped** because `inputs.dry-run` is a real `false`.
3. **From the CLI.** `gh workflow run 04-triggers.yml -f environment=staging -f version=2.0.0`
4. **Outside door.** `gh api repos/OWNER/REPO/dispatches -f event_type=deploy-request -F 'client_payload[from]=laptop'`, then read the payload in the log.
5. **Clock door.** Wait until Monday, or change the cron line to a time a few minutes from now in UTC (remember the 5-minute minimum, and that it may run late).

---

<p align="center">
  <a href="10-common-mistakes.md">⬅️ Common mistakes</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="12-checkpoint.md"><b>Next: Checkpoint ➡️</b></a>
</p>
