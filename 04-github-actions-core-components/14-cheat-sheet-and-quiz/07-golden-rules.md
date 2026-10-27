---
type: Reference
title: "Chapter 4 Cheat Sheet and Quiz: Golden rules"
description: "Jobs in parallel, steps in series. Most surprises come from forgetting one half."
tags: [github-actions, core-components, runners, cheat-sheet, quiz, recap]
status: stable
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-07T00:00:00Z }
sources:
  - id: gh-understand
    resource: https://docs.github.com/en/actions/get-started/understand-github-actions
    title: Understanding GitHub Actions
  - id: gh-workflow-syntax
    resource: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
    title: Workflow syntax for GitHub Actions
---

<p align="center">
  <a href="README.md">📂 <b>Chapter 4 Cheat Sheet and Quiz</b></a> &nbsp;·&nbsp; Lesson 14 · Part 7 of 9 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# 🏆 Golden rules

> [!IMPORTANT]
> 1. **Jobs in parallel, steps in series.** Most surprises come from forgetting one half.
> 2. **One job, one runner, nothing shared.** Pass files between jobs with artifacts.
> 3. **The runner is disposable.** Only logs and artifacts survive.
> 4. **Write the job once, multiply it with a matrix.**
> 5. **Start hosted.** Self-host for a named reason, and not on public repositories.

---

<p align="center">
  <a href="06-finding-your-way-in-the-actions-tab.md">⬅️ Finding your way in the Actions tab</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="08-quiz.md"><b>Next: Quiz ➡️</b></a>
</p>
