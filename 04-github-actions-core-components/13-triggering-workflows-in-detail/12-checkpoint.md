---
type: Tutorial
title: "Triggering Workflows in Detail: Checkpoint"
description: "The button only appears when the workflow file is on the default branch. Merge it to main first. After that you can choose the feature branch in the form."
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
  <a href="README.md">📂 <b>Triggering Workflows in Detail</b></a> &nbsp;·&nbsp; Lesson 13 · Part 12 of 12 &nbsp;·&nbsp; ⏱️ 3 min
</p>

# ✅ Checkpoint

<details>
<summary><b>You added <code>workflow_dispatch</code> on a feature branch, but there's no Run workflow button. Why?</b></summary>

<br>

The button only appears when the workflow file is on the **default branch**. Merge it to `main` first. After that you can choose the feature branch in the form.

</details>

<details>
<summary><b>Your PR workflow should re-run when someone adds a <code>ready-for-review</code> label. Nothing happens. What's missing?</b></summary>

<br>

`pull_request` with no `types:` only runs for `opened`, `synchronize` and `reopened`. Add `types: [opened, synchronize, reopened, labeled]`.

</details>

<details>
<summary><b><code>if: github.event.inputs.dry-run</code> runs even when the box is unticked. Why?</b></summary>

<br>

`github.event.inputs` gives the **string** `'false'`, and a non-empty string is truthy. Use `inputs.dry-run`, which is a real boolean.

</details>

<details>
<summary><b>A workflow pushes a version bump with <code>GITHUB_TOKEN</code>. Will CI run on that commit?</b></summary>

<br>

No. Events caused by `GITHUB_TOKEN` don't start new runs, except `workflow_dispatch` and `repository_dispatch`. This prevents infinite loops. Use a GitHub App token if you really want CI to run.

</details>

<details>
<summary><b>With both <code>branches: [main]</code> and <code>paths: ['src/**']</code>, does a push to <code>main</code> that only changes <code>README.md</code> run the workflow?</b></summary>

<br>

No. Filters combine with AND. The branch matches but no changed file matches `src/**`, so the workflow doesn't run.

</details>

<details>
<summary><b>What does <code>17 6 * * 1</code> mean, and why 17?</b></summary>

<br>

06:17 UTC every Monday. Runs at the start of an hour are the most likely to be delayed or dropped, so an odd minute is more reliable.

</details>

---

<p align="center">
  <a href="11-try-it-yourself.md">⬅️ Try it yourself</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md#-what-you-learned"><b>Wrap up: What you learned ➡️</b></a>
</p>
