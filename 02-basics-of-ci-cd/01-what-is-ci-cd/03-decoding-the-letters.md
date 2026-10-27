---
type: Tutorial
title: "What is CI/CD?: Decoding the letters"
description: "Yes, CD means two different things, and people mix them up constantly. Lesson 3 untangles them. For now:"
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
  <a href="README.md">📂 <b>What is CI/CD?</b></a> &nbsp;·&nbsp; Lesson 1 · Part 3 of 6 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# 🔤 Decoding the letters

| | Letters | Stands for | The question it answers |
|---|---|---|---|
| 🧪 | **CI** | Continuous Integration | *Is this change safe to merge?* |
| 📦 | **CD** | Continuous Delivery | *Could we release this right now?* |
| 🚀 | **CD** | Continuous Deployment | *Why isn't it live already?* |

Yes, **CD means two different things**, and people mix them up constantly. Lesson 3 untangles them. For now:

- **CI** is about *merging and verifying* code
- **CD** is about *getting verified code to users*

<p align="center">
  <img src="../../assets/images/cicd-pipeline.svg" alt="CI covers commit, build, test and package. CD covers deploying to staging and production" width="100%">
</p>

---

<p align="center">
  <a href="02-the-big-idea.md">⬅️ The big idea</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="04-the-assembly-line.md"><b>Next: The assembly line ➡️</b></a>
</p>
