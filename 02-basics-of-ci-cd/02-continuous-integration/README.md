---
type: Tutorial
title: Continuous Integration
description: What CI really means - merge small changes often and let an automated build prove each one - with the checks a CI run performs and the habits that make it work.
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
  <b>Lesson 2 of 6</b> &nbsp;·&nbsp; ⏱️ 9 min read &nbsp;·&nbsp; 🟢 Beginner
</p>

# 🧪 Continuous Integration

## 🗺️ In this topic

8 subtopics, about 12 minutes in all. Read them in order, or jump to the one you need.

| # | Subtopic | Time |
|---|---|---|
| 1 | 💡 [**The definition**](01-the-definition.md) | 1 min |
| 2 | 🎬 [**A day in the life of a change**](02-a-day-in-the-life-of-a.md) | 1 min |
| 3 | 👯 [**Two developers, one `main`**](03-two-developers-one-main.md) | 2 min |
| 4 | 🔍 [**What does a CI run check?**](04-what-does-a-ci-run-check.md) | 1 min |
| 5 | 🚦 [**The meaning of the tick**](05-the-meaning-of-the-tick.md) | 2 min |
| 6 | 🧘 [**The five habits of CI**](06-the-five-habits-of-ci.md) | 2 min |
| 7 | 🧩 [**How it maps to GitHub Actions**](07-how-it-maps-to-github-actions.md) | 1 min |
| 8 | ✅ [**Checkpoint**](08-checkpoint.md) | 2 min |

<p align="center">
  <a href="01-the-definition.md"><b>▶️ Start with The definition</b></a>
</p>

---

<p align="center">
  <a href="../01-what-is-ci-cd/README.md">⬅️ What is CI/CD?</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="../index.md">📚 Chapter 2</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="../03-delivery-vs-deployment/README.md"><b>Next: Delivery vs Deployment ➡️</b></a>
</p>
