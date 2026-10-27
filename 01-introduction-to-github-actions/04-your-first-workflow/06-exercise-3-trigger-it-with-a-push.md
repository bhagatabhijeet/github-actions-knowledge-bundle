---
type: Tutorial
title: "Your First Workflow: Exercise 3: Trigger it with a push"
description: "Push a small commit to main and watch the push event start the workflow on its own."
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
  <a href="README.md">📂 <b>Your First Workflow</b></a> &nbsp;·&nbsp; Lesson 4 · Part 6 of 8 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# ⚡ Exercise 3: Trigger it with a push

Events, not buttons, are the real power. Make any small edit (add a line to a file) and push it to `main`:

```bash
git commit --allow-empty -m "Wake up the robot"
git push
```

Back in the Actions tab a new run has started on its own, and this time **Look around** reports `Triggered by : push`.

> [!TIP]
> Notice the greeting says `World`. A push has no form, so `inputs.who` is empty and the expression `${{ inputs.who || 'World' }}` falls back to the default.

---

<p align="center">
  <a href="05-exercise-2-read-the-logs.md">⬅️ Exercise 2: Read the logs</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="07-exercise-4-break-it-on-purpose.md"><b>Next: Exercise 4: Break it on purpose ➡️</b></a>
</p>
