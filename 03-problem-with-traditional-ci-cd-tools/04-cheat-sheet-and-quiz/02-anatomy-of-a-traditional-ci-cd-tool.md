---
type: Reference
title: "Chapter 3 Cheat Sheet and Quiz: Anatomy of a traditional CI/CD tool"
description: "The three parts of a traditional CI/CD tool (server, agents, plugins) and the upkeep each one hands to you."
tags: [ci-cd, github-actions, self-hosted, cheat-sheet, quiz, recap]
status: stable
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-26T00:00:00Z }
sources:
  - id: gh-hosted-runners
    resource: https://docs.github.com/en/actions/concepts/runners/github-hosted-runners
    title: GitHub-hosted runners
  - id: gh-migrate-jenkins
    resource: https://docs.github.com/en/actions/tutorials/migrate-to-github-actions/manual-migrations/migrate-from-jenkins
    title: Migrating from Jenkins to GitHub Actions
---

<p align="center">
  <a href="README.md">📂 <b>Chapter 3 Cheat Sheet and Quiz</b></a> &nbsp;·&nbsp; Lesson 4 · Part 2 of 8 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# 🧱 Anatomy of a traditional CI/CD tool

| | Part | Job | Your burden |
|---|---|---|---|
| 🧠 | **CI server** | Schedules builds, stores config | Patch, upgrade, back up, monitor |
| 💪 | **Build agents** | Run the builds | Install tools, keep clean, decide how many |
| 🧩 | **Plugins** | Add integrations | Keep compatible, track advisories |

---

<p align="center">
  <a href="01-the-problem-statement.md">⬅️ The problem statement</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="03-six-pains-six-answers.md"><b>Next: Six pains → six answers ➡️</b></a>
</p>
