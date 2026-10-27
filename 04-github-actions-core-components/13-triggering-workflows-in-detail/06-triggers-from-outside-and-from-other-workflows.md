---
type: Tutorial
title: "Triggering Workflows in Detail: Triggers from outside and from other workflows"
description: "Any system with a token can start a workflow through the API: a CMS, a monitoring tool, a script on your laptop."
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
  <a href="README.md">📂 <b>Triggering Workflows in Detail</b></a> &nbsp;·&nbsp; Lesson 13 · Part 6 of 12 &nbsp;·&nbsp; ⏱️ 3 min
</p>

# 🔗 Triggers from outside and from other workflows

## 🌐 `repository_dispatch`: an outside system knocks

Any system with a token can start a workflow through the API: a CMS, a monitoring tool, a script on your laptop.

```yaml
on:
  repository_dispatch:
    types: [deploy-request, cache-purge]
```

```bash
gh api repos/OWNER/REPO/dispatches \
  -f event_type=deploy-request \
  -F 'client_payload[version]=1.4.2'
```

Inside the job, `github.event.action` is the `event_type` and `github.event.client_payload` holds your data. Limits: `event_type` is at most **100 characters**, `client_payload` has at most **10** top-level properties and **65,535** characters.

> [!TIP]
> `workflow_dispatch` or `repository_dispatch`? Use `workflow_dispatch` to start **one specific** workflow with **typed** inputs and a button. Use `repository_dispatch` to announce an **event**, so that any number of workflows listening for that `type` can react with a free-form payload.

## ⛓️ `workflow_run`: after another workflow

```yaml
on:
  workflow_run:
    workflows: [CI]               # the other workflow's name:
    types: [completed]
    branches: [main]              # the branch the CI run was on

jobs:
  deploy:
    if: ${{ github.event.workflow_run.conclusion == 'success' }}
    runs-on: ubuntu-latest
    steps:
      - run: echo "CI passed on ${{ github.event.workflow_run.head_branch }}"
```

- `completed` fires **whatever the result**, including failures. Always check `conclusion`.
- You can chain at most **three levels** of `workflow_run`.
- The triggered workflow runs with the **default branch's** file and has **access to secrets and a write token**, even if the run that triggered it came from a fork and had neither. So never run code from that earlier run here without checking it.

> [!NOTE]
> Within one workflow, use `needs:` (Lesson 9) to order jobs. Use `workflow_run` only when the pieces must be **separate workflows**, for example when the second one needs permissions the first shouldn't have.

## ♻️ `workflow_call`: a workflow other workflows can use

```yaml
on:
  workflow_call:
    inputs:
      node-version:
        type: string
        default: '22'
```

This makes the file a **reusable workflow**: another workflow calls it like a job with `uses: ./.github/workflows/build.yml`. The called workflow receives the caller's event, `GITHUB_SHA` and `GITHUB_REF`. Reusable workflows get a chapter of their own later.

---

<p align="center">
  <a href="05-schedules-with-cron.md">⬅️ Schedules with cron</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="07-the-loop-guard-github-token-doesn-t.md"><b>Next: The loop guard: `GITHUB_TOKEN` doesn't start new runs ➡️</b></a>
</p>
