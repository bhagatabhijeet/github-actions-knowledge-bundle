---
type: Reference
title: "Chapter 2 Cheat Sheet and Quiz: Pipeline stages"
description: "The five pipeline stages, the question each one answers and the commands that typically run there."
tags: [ci-cd, cheat-sheet, quiz, recap]
status: stable
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-26T00:00:00Z }
sources:
  - id: gh-ci
    resource: https://docs.github.com/en/actions/get-started/continuous-integration
    title: Continuous integration (GitHub Docs)
  - id: gh-cd
    resource: https://docs.github.com/en/actions/get-started/continuous-deployment
    title: Continuous deployment (GitHub Docs)
---

<p align="center">
  <a href="README.md">📂 <b>Chapter 2 Cheat Sheet and Quiz</b></a> &nbsp;·&nbsp; Lesson 6 · Part 2 of 6 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# 🚉 Pipeline stages

| Stage | Question | Typical commands |
|---|---|---|
| 📥 Source | What changed? | `actions/checkout` |
| 🏗️ Build | Does it assemble? | `pip install`, `npm ci`, `mvn compile` |
| 🧪 Test | Does it behave? | `ruff check`, `unittest`, `npm test` |
| 📦 Package | What do we ship? | `tar`, `docker build`, `upload-artifact` |
| 🚀 Deploy | Is it live? | Your cloud's CLI or action |

---

<p align="center">
  <a href="01-the-three-practices.md">⬅️ The three practices</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="03-idea-github-actions.md"><b>Next: Idea → GitHub Actions ➡️</b></a>
</p>
