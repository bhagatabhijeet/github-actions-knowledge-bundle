---
type: Tutorial
title: "Your First Workflow: Exercise 1: Run it with the button"
description: "Start the Hello, Actions workflow by hand from the Actions tab with the Run workflow button, and why that button needs the file on the default branch."
resource: /.github/workflows/01-hello-world.yml
tags: [github-actions, hands-on, hello-world, workflow-dispatch, logs]
status: stable
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-26T00:00:00Z }
sources:
  - id: gh-quickstart
    resource: https://docs.github.com/en/actions/get-started/quickstart
    title: Quickstart for GitHub Actions
  - id: gh-summary
    resource: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-commands
    title: Workflow commands (job summaries)
  - id: gh-events
    resource: https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows
    title: Events that trigger workflows
---

<p align="center">
  <a href="README.md">📂 <b>Your First Workflow</b></a> &nbsp;·&nbsp; Lesson 4 · Part 4 of 8 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# ▶️ Exercise 1: Run it with the button

1. Open the **Actions** tab of your fork
2. In the left sidebar, click **01 - Hello, Actions**
3. Click **Run workflow** (right side)
4. Type your name in **Who should we greet?**
5. Click the green **Run workflow** button

A new run appears with a spinning 🟡. Within about twenty seconds it turns ✅.

> [!TIP]
> **No Run workflow button?** The workflow file must be on your **default branch** (usually `main`). A `workflow_dispatch` workflow that only exists on a feature branch can't be started from the button. Once it's on the default branch, you can pick any branch or tag to run it against. ([Events that trigger workflows](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows))

---

<p align="center">
  <a href="03-what-each-part-teaches.md">⬅️ What each part teaches</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="05-exercise-2-read-the-logs.md"><b>Next: Exercise 2: Read the logs ➡️</b></a>
</p>
