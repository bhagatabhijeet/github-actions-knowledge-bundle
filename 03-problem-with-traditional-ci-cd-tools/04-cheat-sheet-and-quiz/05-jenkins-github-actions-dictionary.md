---
type: Reference
title: "Chapter 3 Cheat Sheet and Quiz: Jenkins → GitHub Actions dictionary"
description: "Jenkins → GitHub Actions dictionary, part 5 of 8 of Chapter 3 Cheat Sheet and Quiz."
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
  <a href="README.md">📂 <b>Chapter 3 Cheat Sheet and Quiz</b></a> &nbsp;·&nbsp; Lesson 4 · Part 5 of 8 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# 🔁 Jenkins → GitHub Actions dictionary

| Jenkins | GitHub Actions |
|---|---|
| `Jenkinsfile` | `.github/workflows/*.yml` |
| `agent { label '...' }` | `runs-on:` |
| `stage` | Job |
| `steps` | `steps:` |
| Plugin | Action (`uses:`) |
| Credentials | Secrets |
| Build agent | Runner |

---

<p align="center">
  <a href="04-trade-offs-to-remember.md">⬅️ Trade-offs to remember</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="06-golden-rules.md"><b>Next: Golden rules ➡️</b></a>
</p>
