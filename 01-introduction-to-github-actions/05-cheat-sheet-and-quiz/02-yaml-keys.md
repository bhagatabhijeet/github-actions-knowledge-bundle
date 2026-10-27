---
type: Reference
title: "Chapter 1 Cheat Sheet and Quiz: YAML keys"
description: "Quick reference of the workflow YAML keys used in Chapter 1 and what each one does."
tags: [github-actions, cheat-sheet, quiz, recap]
status: stable
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-07T00:00:00Z }
sources:
  - id: gh-syntax
    resource: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
    title: Workflow syntax for GitHub Actions
  - id: gh-variables
    resource: https://docs.github.com/en/actions/reference/workflows-and-actions/variables
    title: Variables reference
---

<p align="center">
  <a href="README.md">📂 <b>Chapter 1 Cheat Sheet and Quiz</b></a> &nbsp;·&nbsp; Lesson 5 · Part 2 of 6 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# ⌨️ YAML keys

| Key | Level | Does |
|---|---|---|
| `name` | workflow | Display name |
| `on` | workflow | Events that trigger it |
| `permissions` | workflow / job | Limits the run's token |
| `jobs.<id>` | workflow | Defines a job |
| `runs-on` | job | Picks the runner |
| `needs` | job | Waits for other jobs |
| `steps` | job | Ordered list of tasks |
| `uses` / `with` | step | Run an action with inputs |
| `run` | step | Run shell commands |
| `env` | any | Environment variables |
| `if` | job / step | Conditional execution |

---

<p align="center">
  <a href="01-vocabulary.md">⬅️ Vocabulary</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="03-default-variables-worth-knowing.md"><b>Next: Default variables worth knowing ➡️</b></a>
</p>
