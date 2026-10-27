---
type: Reference
title: "Chapter 2 Cheat Sheet and Quiz: Idea → GitHub Actions"
description: "Each CI/CD idea from the chapter mapped to the GitHub Actions feature and snippet that implements it."
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
  - id: gh-limits
    resource: https://docs.github.com/en/actions/reference/limits
    title: Actions limits
---

<p align="center">
  <a href="README.md">📂 <b>Chapter 2 Cheat Sheet and Quiz</b></a> &nbsp;·&nbsp; Lesson 6 · Part 3 of 6 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# 🧩 Idea → GitHub Actions

| CI/CD idea | Feature | Snippet |
|---|---|---|
| Run on every change | Events | `on: [push, pull_request]` |
| Stage order | Job dependencies | `needs: test` |
| Multiple versions | Matrix | `strategy.matrix` |
| Pass files between stages | Artifacts | `upload-artifact` / `download-artifact` |
| Speed up installs | Cache | `cache: pip` |
| Skip irrelevant runs | Path filters | `paths: ['src/**']` |
| Cancel stale runs | Concurrency | `cancel-in-progress: true` |
| Approval before prod | Environments | `environment: production` |
| Block bad merges | Rulesets | Required status checks |

> [!TIP]
> **📘 Limits worth remembering:** 6 hours per job on hosted runners, 24 hours in the queue, 256 jobs per matrix. ([Actions limits](https://docs.github.com/en/actions/reference/limits))

---

<p align="center">
  <a href="02-pipeline-stages.md">⬅️ Pipeline stages</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="04-golden-rules.md"><b>Next: Golden rules ➡️</b></a>
</p>
