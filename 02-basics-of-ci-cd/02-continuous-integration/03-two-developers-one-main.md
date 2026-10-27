---
type: Tutorial
title: "Continuous Integration: Two developers, one `main`"
description: "Real teams have several changes in flight at once. Follow two of them."
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
  <a href="README.md">📂 <b>Continuous Integration</b></a> &nbsp;·&nbsp; Lesson 2 · Part 3 of 8 &nbsp;·&nbsp; ⏱️ 2 min
</p>

# 👯 Two developers, one `main`

Real teams have several changes in flight at once. Follow two of them.

```mermaid
sequenceDiagram
    autonumber
    actor D1 as 🧑‍💻 Developer 1
    actor D2 as 👩‍💻 Developer 2
    participant M as 🌳 main
    participant CI as 🤖 CI

    D1->>CI: Pull request from branch A
    CI-->>D1: ✅ A passes
    D2->>CI: Pull request from branch B
    CI-->>D2: ✅ B passes
    D1->>M: Merge A
    M->>CI: push event
    CI-->>M: ✅ main with A passes
    D2->>M: Merge B
    M->>CI: push event
    CI-->>M: ✅ or ❌ main with A and B
```

Every pull request was tested. So why does CI run **again** after each merge?

| | Run | What it actually tested |
|---|---|---|
| 1 | Pull request A | `main` as it was, plus A |
| 2 | Pull request B | `main` as it was, plus B |
| 3 | After both merges | `main` plus A **plus B**: a combination nobody has tested before |

Developer 1 renamed a function. Developer 2 added a new call to the old name. Each branch is green on its own. Together they're broken, and only the run on `main` can see it.

> [!IMPORTANT]
> **A pull request run tests one change. A run on `main` tests how the changes work together.** That second run is the "integration" in continuous integration, which is why the minimal workflow below listens for both `pull_request` and `push`.

---

<p align="center">
  <a href="02-a-day-in-the-life-of-a.md">⬅️ A day in the life of a change</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="04-what-does-a-ci-run-check.md"><b>Next: What does a CI run check? ➡️</b></a>
</p>
