---
type: Tutorial
title: "Continuous Integration: The meaning of the tick"
description: "What the pending, success and failure marks on a commit mean, and how required checks turn the green tick into a merge gate."
tags: [ci-cd, continuous-integration, testing, linting, pull-requests]
status: stable
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-26T00:00:00Z }
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
  - id: gh-limits
    resource: https://docs.github.com/en/actions/reference/limits
    title: Actions limits
---

<p align="center">
  <a href="README.md">📂 <b>Continuous Integration</b></a> &nbsp;·&nbsp; Lesson 2 · Part 5 of 8 &nbsp;·&nbsp; ⏱️ 2 min
</p>

# 🚦 The meaning of the tick

On every commit and pull request, GitHub shows the result:

| | Status | Means |
|---|---|---|
| 🟡 | Pending | Checks are running |
| ✅ | Success | Every check passed |
| ❌ | Failure | At least one check failed |

With a **branch protection rule** (or ruleset) you can make the tick mandatory: GitHub disables the **Merge** button until required checks pass. This turns CI from advice into a gate.

```mermaid
flowchart LR
    PR[📬 Pull request]:::blue --> C{🤖 CI passes?}:::yellow
    C -- ✅ yes --> M[🔓 Merge enabled]:::green
    C -- ❌ no --> B[🔒 Merge blocked]:::red
    B -. push a fix .-> PR

    classDef blue fill:#0c1d3a,stroke:#58a6ff,color:#fff,stroke-width:2px
    classDef yellow fill:#3d2a00,stroke:#e3b341,color:#fff,stroke-width:2px
    classDef green fill:#0f2d17,stroke:#3fb950,color:#fff,stroke-width:2px
    classDef red fill:#4a0d0d,stroke:#f85149,color:#fff,stroke-width:2px
```

> [!NOTE]
> **📘 From the GitHub docs:** A tick can't wait forever. A job that sits in the queue for **24 hours** is cancelled automatically, and a job on a GitHub-hosted runner is stopped after **6 hours** of running. If a check stays 🟡 for ages, look for a missing runner or a hung step. ([Actions limits](https://docs.github.com/en/actions/reference/limits))

---

<p align="center">
  <a href="04-what-does-a-ci-run-check.md">⬅️ What does a CI run check?</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="06-the-five-habits-of-ci.md"><b>Next: The five habits of CI ➡️</b></a>
</p>
