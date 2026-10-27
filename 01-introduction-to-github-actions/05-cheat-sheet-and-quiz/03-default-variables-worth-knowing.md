---
type: Reference
title: "Chapter 1 Cheat Sheet and Quiz: Default variables worth knowing"
description: "The default GITHUB_* and RUNNER_* environment variables you will use most often, with example values."
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
  <a href="README.md">📂 <b>Chapter 1 Cheat Sheet and Quiz</b></a> &nbsp;·&nbsp; Lesson 5 · Part 3 of 6 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# 🧾 Default variables worth knowing

| Variable | Example value |
|---|---|
| `GITHUB_EVENT_NAME` | `push` |
| `GITHUB_REPOSITORY` | `octocat/hello-world` |
| `GITHUB_REF_NAME` | `main` |
| `GITHUB_SHA` | `8f3a1c...` |
| `GITHUB_ACTOR` | `octocat` |
| `GITHUB_WORKSPACE` | where checkout puts your code |
| `RUNNER_OS` | `Linux` |
| `GITHUB_STEP_SUMMARY` | file to append Markdown summaries to |

---

<p align="center">
  <a href="02-yaml-keys.md">⬅️ YAML keys</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="04-golden-rules.md"><b>Next: Golden rules ➡️</b></a>
</p>
