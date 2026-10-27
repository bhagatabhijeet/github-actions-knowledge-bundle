---
type: Tutorial
title: "Triggering Workflows in Detail: Repository events and activity types"
description: "Most of the 35 or so events have activity types: the different things that can happen to the same object. An issue can be opened, edited, labeled, closed and more. Without types: you get every activity type, which is..."
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
  <a href="README.md">📂 <b>Triggering Workflows in Detail</b></a> &nbsp;·&nbsp; Lesson 13 · Part 2 of 12 &nbsp;·&nbsp; ⏱️ 3 min
</p>

# 🔔 Repository events and activity types

Most of the 35 or so events have **activity types**: the different things that can happen to the same object. An issue can be `opened`, `edited`, `labeled`, `closed` and more. Without `types:` you get **every** activity type, which is rarely what you want.

```yaml
on:
  issues:
    types: [opened, labeled]      # only these two
  release:
    types: [published]            # not created, edited, deleted...
  pull_request:                   # no types: means the default set below
```

> [!WARNING]
> `pull_request` is the exception that catches everyone. With no `types:`, it does **not** run for every activity. It runs only for **`opened`, `synchronize` and `reopened`**. `synchronize` means "new commits were pushed to the PR". If you want a workflow to react to labels or to a PR being closed, list those types yourself.

## 🎛️ Three ways to write `on:`

```yaml
on: push                             # one event, every activity type

on: [push, pull_request]             # several events, defaults for each

on:                                  # a map: each event can have its own settings
  push:
    branches: [main]
  pull_request:
    types: [opened, synchronize, reopened, labeled]
```

If **any** listed event happens, the workflow runs. Two events in the same instant start **two** runs. Use `github.event_name` inside the job to tell them apart.

## 🧾 What a few common events give you

| Event | `GITHUB_SHA` is... | `GITHUB_REF` is... |
|---|---|---|
| `push` | the tip commit that was pushed | the branch or tag pushed to, e.g. `refs/heads/main` |
| `pull_request` | a **test merge commit** of the PR into its target | `refs/pull/<number>/merge` |
| `pull_request_target` | the last commit on the **default branch** | the default branch |
| `workflow_dispatch` | the last commit on the chosen branch or tag | the branch or tag you picked |
| `schedule` | the last commit on the default branch | the default branch |

> [!TIP]
> For a `pull_request` run, the code you check out is **what the repo would look like after merging**, not the PR branch alone. Need the PR's own latest commit? It's `github.event.pull_request.head.sha`. Also from the docs: if a PR has a **merge conflict**, `pull_request` workflows don't run at all until it's fixed.

---

<p align="center">
  <a href="01-four-doors-into-a-workflow.md">⬅️ Four doors into a workflow</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="03-filters-branches-tags-and-paths.md"><b>Next: Filters: branches, tags and paths ➡️</b></a>
</p>
