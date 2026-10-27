---
type: Tutorial
title: "Triggering Workflows in Detail: Schedules with cron"
description: "Run a workflow on a timer with five-field cron lines, and know the limits: UTC by default, 5-minute minimum, late or dropped runs, default branch only."
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
  <a href="README.md">📂 <b>Triggering Workflows in Detail</b></a> &nbsp;·&nbsp; Lesson 13 · Part 5 of 12 &nbsp;·&nbsp; ⏱️ 3 min
</p>

# ⏰ Schedules with cron

```yaml
on:
  schedule:
    - cron: '30 5 * * 1-5'     # 05:30 UTC, Monday to Friday
    - cron: '0 0 1 * *'        # midnight UTC on the 1st of every month
```

A cron line has five fields:

```text
┌───────────── minute        (0 - 59)
│ ┌─────────── hour          (0 - 23)
│ │ ┌───────── day of month  (1 - 31)
│ │ │ ┌─────── month         (1 - 12 or JAN - DEC)
│ │ │ │ ┌───── day of week   (0 - 6 or SUN - SAT)
│ │ │ │ │
* * * * *
```

| Operator | Meaning | Example |
|---|---|---|
| `*` | any value | `* * * * *` every minute (but see the limit below) |
| `,` | a list | `0 9,17 * * *` at 09:00 and 17:00 |
| `-` | a range | `0 9 * * 1-5` weekdays at 09:00 |
| `/` | a step | `*/15 * * * *` every 15 minutes |

[crontab.guru](https://crontab.guru) translates a cron line into English, and it's worth bookmarking.

**What the docs say about schedules:**

- ⏱️ **Every 5 minutes at most.** Shorter intervals aren't allowed.
- 🌍 **UTC by default.** `0 9 * * *` is 09:00 in London in winter but 10:00 in summer. The docs also describe an optional IANA `timezone:` value.
- 🐢 **Runs can start late.** The start of every hour is the busiest time, and at high load scheduled runs can be delayed or **dropped**. Pick an odd minute like `17` instead of `0`.
- 🌳 **Default branch only.** The schedule runs the workflow file from the latest commit on `main`.
- 💤 **Public repos go to sleep.** If a public repository has no activity for **60 days**, its scheduled workflows are disabled until someone turns them back on.
- 🚫 **No shortcuts.** `@daily` and `@hourly` aren't supported. Write the five fields.

Inside the job, `github.event.schedule` holds the cron line that fired, which helps when one workflow has several schedules.

---

<p align="center">
  <a href="04-manual-runs-with-workflow-dispatch.md">⬅️ Manual runs with `workflow_dispatch`</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="06-triggers-from-outside-and-from-other-workflows.md"><b>Next: Triggers from outside and from other workflows ➡️</b></a>
</p>
