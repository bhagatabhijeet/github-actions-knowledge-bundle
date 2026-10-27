---
type: Tutorial
title: "Your First Workflow: What each part teaches"
description: "A fresh runner is an empty machine. Your repository is not on it until actions/checkout puts it there. Forgetting checkout is the classic first-week mistake."
resource: /.github/workflows/01-hello-world.yml
tags: [github-actions, hands-on, hello-world, workflow-dispatch, logs]
status: stable
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-07T00:00:00Z }
sources:
  - id: gh-quickstart
    resource: https://docs.github.com/en/actions/get-started/quickstart
    title: Quickstart for GitHub Actions
  - id: gh-summary
    resource: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-commands
    title: Workflow commands (job summaries)
---

<p align="center">
  <a href="README.md">📂 <b>Your First Workflow</b></a> &nbsp;·&nbsp; Lesson 4 · Part 3 of 8 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# 🔎 What each part teaches

| Lines | Concept | Why it's there |
|---|---|---|
| `on.push` | Event | Runs on every push to `main` |
| `on.workflow_dispatch` | Event + input | Adds a **Run workflow** button with a text box |
| `permissions` | Security | The run's token can only read the repo |
| `Greet` | `run` + `env` | The form input reaches the shell safely through an environment variable |
| `Check out` | `uses` | Without it, the runner has **no copy of your code** |
| `Look around` | Default variables | GitHub hands every step facts like `$GITHUB_SHA` |
| `Write a job summary` | `$GITHUB_STEP_SUMMARY` | Markdown appended to this file appears on the run page |

> [!IMPORTANT]
> A fresh runner is an empty machine. Your repository is **not** on it until `actions/checkout` puts it there. Forgetting checkout is the classic first-week mistake.

---

<p align="center">
  <a href="02-the-workflow.md">⬅️ The workflow</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="04-exercise-1-run-it-with-the-button.md"><b>Next: Exercise 1: Run it with the button ➡️</b></a>
</p>
