---
type: Reference
title: "Chapter 4 Cheat Sheet and Quiz: How results roll up"
description: "A step passes when it exits cleanly, a job when every step passes, and a run when every job passes."
tags: [github-actions, core-components, runners, cheat-sheet, quiz, recap]
status: stable
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-26T00:00:00Z }
sources:
  - id: gh-understand
    resource: https://docs.github.com/en/actions/get-started/understand-github-actions
    title: Understanding GitHub Actions
  - id: gh-workflow-syntax
    resource: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
    title: Workflow syntax for GitHub Actions
---

<p align="center">
  <a href="README.md">📂 <b>Chapter 4 Cheat Sheet and Quiz</b></a> &nbsp;·&nbsp; Lesson 14 · Part 3 of 9 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# 🚦 How results roll up

| Level | Passes when |
|---|---|
| 👣 Step | Its command or action exits successfully |
| 📦 Job | Every step passes |
| 📜 Workflow run | Every job passes |

---

<p align="center">
  <a href="02-a-run-in-six-stages.md">⬅️ A run in six stages</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="04-matrix-in-four-lines.md"><b>Next: Matrix in four lines ➡️</b></a>
</p>
