---
type: Tutorial
title: "Continuous Integration: What does a CI run check?"
description: "Checks are ordered cheapest first, so obvious mistakes fail fast."
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
  <a href="README.md">📂 <b>Continuous Integration</b></a> &nbsp;·&nbsp; Lesson 2 · Part 4 of 8 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# 🔍 What does a CI run check?

Checks are ordered cheapest first, so obvious mistakes fail fast.

| Order | Check | Catches | Typical time |
|---|---|---|---|
| 1 | 🧹 **Lint / format** | Typos, unused code, style drift | seconds |
| 2 | 🏗️ **Build / compile** | Code that doesn't even assemble | seconds to minutes |
| 3 | 🧪 **Unit tests** | Broken logic in small pieces | seconds to minutes |
| 4 | 🔗 **Integration tests** | Pieces that don't work together | minutes |
| 5 | 🛡️ **Security scans** | Vulnerable dependencies, leaked secrets | minutes |

> [!TIP]
> **Fail fast.** If a 5-second lint check would fail, there's no point waiting 10 minutes for tests to tell you something else is also wrong. Put quick checks first.

---

<p align="center">
  <a href="03-two-developers-one-main.md">⬅️ Two developers, one `main`</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="05-the-meaning-of-the-tick.md"><b>Next: The meaning of the tick ➡️</b></a>
</p>
