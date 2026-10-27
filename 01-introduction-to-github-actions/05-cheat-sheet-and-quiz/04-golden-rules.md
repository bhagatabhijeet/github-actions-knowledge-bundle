---
type: Reference
title: "Chapter 1 Cheat Sheet and Quiz: Golden rules"
description: "Checkout first. The runner starts empty."
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
  <a href="README.md">📂 <b>Chapter 1 Cheat Sheet and Quiz</b></a> &nbsp;·&nbsp; Lesson 5 · Part 4 of 6 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# 🏆 Golden rules

> [!IMPORTANT]
> 1. **Checkout first.** The runner starts empty.
> 2. **Jobs are parallel and isolated.** Use `needs` to order, artifacts to share.
> 3. **Non-zero exit = failure.** That's how a workflow knows.
> 4. **Quote your versions.** `'3.10'`, not `3.10`.
> 5. **Pin your actions.** `@v7`, never `@main`.
> 6. **Least privilege.** Start with `permissions: contents: read`.

---

<p align="center">
  <a href="03-default-variables-worth-knowing.md">⬅️ Default variables worth knowing</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="05-quiz.md"><b>Next: Quiz ➡️</b></a>
</p>
