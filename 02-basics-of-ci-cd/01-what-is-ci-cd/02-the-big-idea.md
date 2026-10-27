---
type: Tutorial
title: "What is CI/CD?: The big idea"
description: "If it hurts, do it more often, and let a machine do it."
tags: [ci-cd, continuous-integration, continuous-delivery, devops, beginner]
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
---

<p align="center">
  <a href="README.md">📂 <b>What is CI/CD?</b></a> &nbsp;·&nbsp; Lesson 1 · Part 2 of 6 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# 💡 The big idea

> [!IMPORTANT]
> **If it hurts, do it more often, and let a machine do it.**

It sounds backwards, but it works for the same reason washing one plate after dinner beats facing a week of dishes. Small things are easy. Merging ten lines is trivial; merging ten thousand is a project.

So we flip the loop:

```mermaid
flowchart LR
    A[🤏 Tiny changes]:::green --> B[🤖 Verified automatically]:::blue
    B --> C[🚀 Released often]:::purple
    C --> D[😌 Releases are boring]:::green
    D --> A

    classDef green fill:#0f2d17,stroke:#3fb950,color:#fff,stroke-width:2px
    classDef blue fill:#0c1d3a,stroke:#58a6ff,color:#fff,stroke-width:2px
    classDef purple fill:#22123f,stroke:#bc8cff,color:#fff,stroke-width:2px
```

**Boring releases are the goal.** A release so routine that nobody stays late for it.

---

<p align="center">
  <a href="01-life-before-ci-cd.md">⬅️ Life before CI/CD</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="03-decoding-the-letters.md"><b>Next: Decoding the letters ➡️</b></a>
</p>
