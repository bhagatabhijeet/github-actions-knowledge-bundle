---
type: Tutorial
title: "Your First Workflow: Something went wrong?"
description: "A symptom-to-cause table for the common first-run problems: workflow not listed, invalid YAML, no Run workflow button, and nothing running on push."
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
  - id: gh-syntax
    resource: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
    title: Workflow syntax for GitHub Actions
---

<p align="center">
  <a href="README.md">📂 <b>Your First Workflow</b></a> &nbsp;·&nbsp; Lesson 4 · Part 8 of 8 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# 🧯 Something went wrong?

| Symptom | Likely cause |
|---|---|
| Workflow isn't listed in the Actions tab | File isn't in `.github/workflows/`, or doesn't end in `.yml` or `.yaml` |
| "Invalid workflow file" | Indentation. Check for tabs and misaligned keys |
| No **Run workflow** button | `workflow_dispatch` is missing, or the file isn't on the default branch |
| Nothing runs on push | You pushed to a branch other than `main` |
| Actions tab shows a big enable button | Workflows are disabled on your fork; click it |

---

<p align="center">
  <a href="07-exercise-4-break-it-on-purpose.md">⬅️ Exercise 4: Break it on purpose</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md#-what-you-learned"><b>Wrap up: What you learned ➡️</b></a>
</p>
