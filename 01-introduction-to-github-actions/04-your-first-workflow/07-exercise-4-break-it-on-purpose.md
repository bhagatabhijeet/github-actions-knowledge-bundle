---
type: Tutorial
title: "Your First Workflow: Exercise 4: Break it on purpose"
description: "Add a failing step on purpose to see how a non-zero exit code turns a run red and stops the job."
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
  <a href="README.md">📂 <b>Your First Workflow</b></a> &nbsp;·&nbsp; Lesson 4 · Part 7 of 8 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# 💥 Exercise 4: Break it on purpose

You learn a tool properly when you see it fail. In `01-hello-world.yml`, add this as the **second** step, then push:

```yaml
      - name: Fail on purpose
        run: exit 1
```

Observe three things:

1. The run turns ❌ and GitHub emails you
2. Every step **after** the failing one is skipped
3. The log shows `Process completed with exit code 1`

> [!NOTE]
> This is the entire basis of CI. A command that exits with a non-zero code fails the step, which fails the job, which fails the run. Test runners exit non-zero when a test fails. That's all the magic there is.

Remove the failing step and push again to get back to green.

---

<p align="center">
  <a href="06-exercise-3-trigger-it-with-a-push.md">⬅️ Exercise 3: Trigger it with a push</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="08-something-went-wrong.md"><b>Next: Something went wrong? ➡️</b></a>
</p>
