---
type: Reference
title: "Chapter 3 Cheat Sheet and Quiz: Trade-offs to remember"
description: "Trade-offs to remember, part 4 of 8 of Chapter 3 Cheat Sheet and Quiz."
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
  <a href="README.md">📂 <b>Chapter 3 Cheat Sheet and Quiz</b></a> &nbsp;·&nbsp; Lesson 4 · Part 4 of 8 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# ⚖️ Trade-offs to remember

| | Trade-off | Mitigation |
|---|---|---|
| 🔒 | Tied to GitHub | Keep real logic in scripts; let the workflow just call them |
| 🌐 | No private-network access | Self-hosted runners |
| 🔧 | Limited machine choice | Larger or self-hosted runners |
| ⏱️ | 6-hour job limit on hosted runners | Split the job, or self-host |
| 💰 | Per-minute cost on private repos | Caching, path filters, concurrency |
| 🛡️ | Third-party action risk | Vet actions; pin to a commit SHA |

---

<p align="center">
  <a href="03-six-pains-six-answers.md">⬅️ Six pains → six answers</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="05-jenkins-github-actions-dictionary.md"><b>Next: Jenkins → GitHub Actions dictionary ➡️</b></a>
</p>
