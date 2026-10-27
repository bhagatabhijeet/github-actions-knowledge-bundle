---
type: Tutorial
title: "Your First Workflow: Exercise 2: Read the logs"
description: "How to open a run, expand each step"s log and find the output your workflow printed."
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
  <a href="README.md">📂 <b>Your First Workflow</b></a> &nbsp;·&nbsp; Lesson 4 · Part 5 of 8 &nbsp;·&nbsp; ⏱️ 2 min
</p>

# 📖 Exercise 2: Read the logs

Click the run, then click the **say-hello** job. You'll see this:

```text
✅ Set up job
✅ Greet
✅ Check out the repository
✅ Look around
✅ Write a job summary
✅ Post Check out the repository
✅ Complete job
```

Expand **Greet** and find your name. Then expand **Look around** and compare it to the file list of the repo.

<details>
<summary><b>🤔 Wait, I didn't write "Set up job" or "Post Check out the repository"</b></summary>

<br>

Correct. GitHub adds them.

- **Set up job** boots the runner and downloads the actions you referenced
- **Post Check out the repository** is cleanup that the checkout action registered for itself
- **Complete job** tears everything down

</details>

Now scroll to the bottom of the run's **Summary** page. That table is the job summary your last step wrote. 🎉

---

<p align="center">
  <a href="04-exercise-1-run-it-with-the-button.md">⬅️ Exercise 1: Run it with the button</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="06-exercise-3-trigger-it-with-a-push.md"><b>Next: Exercise 3: Trigger it with a push ➡️</b></a>
</p>
