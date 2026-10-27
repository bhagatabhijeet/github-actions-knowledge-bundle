---
type: Reference
title: "Chapter 3 Cheat Sheet and Quiz: Golden rules"
description: "A free licence is not a free tool. Count the hours, not the invoice."
tags: [ci-cd, github-actions, self-hosted, cheat-sheet, quiz, recap]
status: stable
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-07T00:00:00Z }
sources:
  - id: gh-hosted-runners
    resource: https://docs.github.com/en/actions/concepts/runners/github-hosted-runners
    title: GitHub-hosted runners
  - id: gh-migrate-jenkins
    resource: https://docs.github.com/en/actions/tutorials/migrate-to-github-actions/manual-migrations/migrate-from-jenkins
    title: Migrating from Jenkins to GitHub Actions
---

<p align="center">
  <a href="README.md">📂 <b>Chapter 3 Cheat Sheet and Quiz</b></a> &nbsp;·&nbsp; Lesson 4 · Part 6 of 8 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# 🏆 Golden rules

> [!IMPORTANT]
> 1. **A free licence is not a free tool.** Count the hours, not the invoice.
> 2. **Describe the machine, don't point at one.** `python-version: '3.13'` beats "the agent with Python on it".
> 3. **Clean beats fast.** A fresh machine per job is why builds are repeatable.
> 4. **Hosted first.** Add self-hosted runners only when you hit a specific wall.
> 5. **Actions are other people's code.** Treat them with the care you'd give any dependency.

---

<p align="center">
  <a href="05-jenkins-github-actions-dictionary.md">⬅️ Jenkins → GitHub Actions dictionary</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="07-quiz.md"><b>Next: Quiz ➡️</b></a>
</p>
