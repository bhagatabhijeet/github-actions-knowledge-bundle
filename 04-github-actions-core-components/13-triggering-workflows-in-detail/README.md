---
type: Tutorial
title: Triggering Workflows in Detail (Hands-On)
description: Everything that can start a workflow - repository events and their activity types, branch, tag and path filters, manual runs with workflow_dispatch and typed inputs, cron schedules, repository_dispatch, workflow_run and workflow_call, which commit a run uses, and the loop guard on GITHUB_TOKEN.
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
  <b>Lesson 13 of 14</b> &nbsp;·&nbsp; ⏱️ 26 min &nbsp;·&nbsp; 🛠️ Hands-on
</p>

# 🚦 Triggering Workflows in Detail

So far almost every workflow in this course started with `on: push`. That works, but it's like a doorbell that rings on every footstep: a typo fix in the README starts the same 10-minute pipeline as a change to the payment code. This lesson is about the `on:` block. It decides **what** starts a run, **when**, **on which commit**, and **with which values**.

You'll learn the four ways a run can start, how to make triggers precise, and the rules that surprise people, such as "my Run workflow button is missing" and "my scheduled job runs 20 minutes late".

## 🗺️ In this topic

12 subtopics, about 31 minutes in all. Read them in order, or jump to the one you need.

| # | Subtopic | Time |
|---|---|---|
| 1 | 🚪 [**Four doors into a workflow**](01-four-doors-into-a-workflow.md) | 3 min |
| 2 | 🔔 [**Repository events and activity types**](02-repository-events-and-activity-types.md) | 3 min |
| 3 | 🎯 [**Filters: branches, tags and paths**](03-filters-branches-tags-and-paths.md) | 3 min |
| 4 | 🖱️ [**Manual runs with `workflow_dispatch`**](04-manual-runs-with-workflow-dispatch.md) | 4 min |
| 5 | ⏰ [**Schedules with cron**](05-schedules-with-cron.md) | 3 min |
| 6 | 🔗 [**Triggers from outside and from other workflows**](06-triggers-from-outside-and-from-other-workflows.md) | 3 min |
| 7 | 🔁 [**The loop guard: `GITHUB_TOKEN` doesn't start new runs**](07-the-loop-guard-github-token-doesn-t.md) | 1 min |
| 8 | ⚖️ [**`pull_request` vs `pull_request_target`**](08-pull-request-vs-pull-request-target.md) | 2 min |
| 9 | 🧭 [**Which trigger do I need?**](09-which-trigger-do-i-need.md) | 2 min |
| 10 | 🪤 [**Common mistakes**](10-common-mistakes.md) | 2 min |
| 11 | 🛠️ [**Try it yourself**](11-try-it-yourself.md) | 2 min |
| 12 | ✅ [**Checkpoint**](12-checkpoint.md) | 3 min |

<p align="center">
  <a href="01-four-doors-into-a-workflow.md"><b>▶️ Start with Four doors into a workflow</b></a>
</p>

## 🎯 What you learned

- A run starts through one of **four doors**: repository events, schedules, manual runs, or other systems and workflows
- The run uses the workflow file **at the event's commit**, and several events only look at the **default branch**
- **`types:`** picks activity types; **`pull_request`** defaults to `opened`, `synchronize`, `reopened`
- **`branches`, `tags`, `paths`** filters combine with AND; use `!` to exclude inside a list
- **`workflow_dispatch`** gives a Run workflow button and up to 25 typed inputs. Read them with **`inputs`**
- **`schedule`** is cron in UTC, at most every 5 minutes, may run late, and sleeps after 60 idle days in public repos
- **`repository_dispatch`**, **`workflow_run`** and **`workflow_call`** connect outside systems and other workflows
- **`GITHUB_TOKEN`** events don't start new runs, except the two dispatch events

---

<p align="center">
  <a href="../12-working-with-repository-secrets/README.md">⬅️ Secrets</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="../index.md">📚 Chapter 4</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="../14-cheat-sheet-and-quiz/README.md"><b>Next: Cheat Sheet & Quiz ➡️</b></a>
</p>
