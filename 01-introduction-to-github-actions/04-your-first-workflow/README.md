---
type: Tutorial
title: Your First Workflow (Hands-On)
description: Run the Hello, Actions workflow that ships in this repository, read its logs, trigger it by hand, and break it on purpose.
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
  <b>Lesson 4 of 5</b> &nbsp;·&nbsp; ⏱️ 15 min hands-on &nbsp;·&nbsp; 🛠️ Keyboard required
</p>

# 🚀 Your First Workflow

Enough reading. Time to make a machine in the cloud do your bidding.

This repository ships with a real workflow, [`.github/workflows/01-hello-world.yml`](../../.github/workflows/01-hello-world.yml). You're going to run it, read it, and break it.

## 🗺️ In this topic

8 subtopics, about 9 minutes in all. Read them in order, or jump to the one you need.

| # | Subtopic | Time |
|---|---|---|
| 1 | 🎒 [**Before you start**](01-before-you-start.md) | 1 min |
| 2 | 📄 [**The workflow**](02-the-workflow.md) | 1 min |
| 3 | 🔎 [**What each part teaches**](03-what-each-part-teaches.md) | 1 min |
| 4 | ▶️ [**Exercise 1: Run it with the button**](04-exercise-1-run-it-with-the-button.md) | 1 min |
| 5 | 📖 [**Exercise 2: Read the logs**](05-exercise-2-read-the-logs.md) | 2 min |
| 6 | ⚡ [**Exercise 3: Trigger it with a push**](06-exercise-3-trigger-it-with-a-push.md) | 1 min |
| 7 | 💥 [**Exercise 4: Break it on purpose**](07-exercise-4-break-it-on-purpose.md) | 1 min |
| 8 | 🧯 [**Something went wrong?**](08-something-went-wrong.md) | 1 min |

<p align="center">
  <a href="01-before-you-start.md"><b>▶️ Start with Before you start</b></a>
</p>

## 🎯 What you learned

- How to run a workflow by **button** and by **push**
- How to read a run: jobs, steps, logs, summary
- Why **checkout** is almost always your first real step
- That a **non-zero exit code** is what makes a run fail

---

<p align="center">
  <a href="../03-anatomy-of-a-workflow/README.md">⬅️ Anatomy of a Workflow</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="../index.md">📚 Chapter 1</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="../05-cheat-sheet-and-quiz/README.md"><b>Next: Cheat Sheet & Quiz ➡️</b></a>
</p>
