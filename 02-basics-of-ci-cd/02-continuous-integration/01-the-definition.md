---
type: Tutorial
title: "Continuous Integration: The definition"
description: "Continuous Integration is the habit of merging small changes into the shared branch frequently, with every change automatically built and tested."
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
  <a href="README.md">📂 <b>Continuous Integration</b></a> &nbsp;·&nbsp; Lesson 2 · Part 1 of 8 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# 💡 The definition

> [!IMPORTANT]
> **Continuous Integration is the habit of merging small changes into the shared branch frequently, with every change automatically built and tested.**

Two halves, and both matter:

| | Half | Who does it |
|---|---|---|
| 🧑‍💻 | **Integrate often**: small changes, merged at least daily | People |
| 🤖 | **Verify automatically**: build and test every single change | Machines |

A team with a beautiful test pipeline and month-old branches is not doing CI. They have automated testing. The *continuous* part is the humans' job.

---

<p align="center">
  <a href="README.md">⬅️ Overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="02-a-day-in-the-life-of-a.md"><b>Next: A day in the life of a change ➡️</b></a>
</p>
