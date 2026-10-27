---
type: Tutorial
title: "Continuous Integration: The five habits of CI"
description: "Tools don't do CI. Teams do. These habits are what make it real:"
tags: [ci-cd, continuous-integration, testing, linting, pull-requests]
status: stable
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-07T00:00:00Z }
sources:
  - id: fowler-ci
    resource: https://martinfowler.com/articles/continuousIntegration.html
    title: Continuous Integration
    author: Martin Fowler
  - id: gh-ci
    resource: https://docs.github.com/en/actions/get-started/continuous-integration
    title: Continuous integration (GitHub Docs)
  - id: gh-protection
    resource: https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches
    title: About protected branches
---

<p align="center">
  <a href="README.md">📂 <b>Continuous Integration</b></a> &nbsp;·&nbsp; Lesson 2 · Part 6 of 8 &nbsp;·&nbsp; ⏱️ 2 min
</p>

# 🧘 The five habits of CI

Tools don't do CI. Teams do. These habits are what make it real:

| | Habit | Why |
|---|---|---|
| 1️⃣ | **Commit small, merge daily** | Small changes rarely conflict and are easy to review |
| 2️⃣ | **Every change triggers the build** | No exceptions means no surprises |
| 3️⃣ | **Keep the build fast** | Aim for under ten minutes; slow feedback gets ignored |
| 4️⃣ | **A red `main` is an emergency** | Fix or revert before doing anything else |
| 5️⃣ | **Test in a clean environment** | Kills "works on my machine" for good |

> [!WARNING]
> **The broken-window effect.** If `main` stays red for a day, people stop looking at the status. Then a second failure hides behind the first. Then nobody trusts the pipeline, and you're back to week 7. Treat red as "stop the line".

---

<p align="center">
  <a href="05-the-meaning-of-the-tick.md">⬅️ The meaning of the tick</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="07-how-it-maps-to-github-actions.md"><b>Next: How it maps to GitHub Actions ➡️</b></a>
</p>
