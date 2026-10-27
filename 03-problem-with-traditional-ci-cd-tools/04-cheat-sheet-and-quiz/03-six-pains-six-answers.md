---
type: Reference
title: "Chapter 3 Cheat Sheet and Quiz: Six pains → six answers"
description: "The six hidden costs of self-hosted CI, their root causes and how GitHub Actions answers each one."
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
  <a href="README.md">📂 <b>Chapter 3 Cheat Sheet and Quiz</b></a> &nbsp;·&nbsp; Lesson 4 · Part 3 of 8 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# 🧊 Six pains → six answers

| | Pain | Cause | GitHub Actions answer |
|---|---|---|---|
| 1️⃣ | Server upkeep | You run the CI server | No server; it's a service |
| 2️⃣ | Snowflake agents | Long-lived machines, hand-installed tools | Fresh VM per job; versions declared in YAML |
| 3️⃣ | Queues and idle cost | Capacity fixed in advance | A runner per job, billed per minute |
| 4️⃣ | Fragile plugins | Installed server-wide, tied to server version | Actions versioned per workflow |
| 5️⃣ | Integration glue | Code and CI are separate systems | CI lives in the repository |
| 6️⃣ | Knowledge in one head | Config set through an admin screen | Workflows are reviewed files in Git |

---

<p align="center">
  <a href="02-anatomy-of-a-traditional-ci-cd-tool.md">⬅️ Anatomy of a traditional CI/CD tool</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="04-trade-offs-to-remember.md"><b>Next: Trade-offs to remember ➡️</b></a>
</p>
