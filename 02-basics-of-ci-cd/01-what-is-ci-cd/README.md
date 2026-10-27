---
type: Tutorial
title: What is CI/CD?
description: The problem CI/CD solves - integration hell and scary releases - and the simple idea behind it - make small changes and let machines verify and ship them.
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
  <img src="../../assets/images/chapter-02-banner.svg" alt="Chapter 2: Basics of CI/CD" width="100%">
</p>

<p align="center">
  <b>Lesson 1 of 6</b> &nbsp;·&nbsp; ⏱️ 7 min read &nbsp;·&nbsp; 🟢 No experience needed
</p>

# 🔄 What is CI/CD?

In Chapter 1 you learned *how* to make GitHub run things. This chapter is about *what's worth running*, and why an entire industry reorganised itself around two short abbreviations.

## 🗺️ In this topic

6 subtopics, about 8 minutes in all. Read them in order, or jump to the one you need.

| # | Subtopic | Time |
|---|---|---|
| 1 | 😱 [**Life before CI/CD**](01-life-before-ci-cd.md) | 2 min |
| 2 | 💡 [**The big idea**](02-the-big-idea.md) | 1 min |
| 3 | 🔤 [**Decoding the letters**](03-decoding-the-letters.md) | 1 min |
| 4 | 🏭 [**The assembly line**](04-the-assembly-line.md) | 1 min |
| 5 | 🎁 [**What you get out of it**](05-what-you-get-out-of-it.md) | 1 min |
| 6 | 🚫 [**Three myths**](06-three-myths.md) | 2 min |

<p align="center">
  <a href="01-life-before-ci-cd.md"><b>▶️ Start with Life before CI/CD</b></a>
</p>

## 🎯 What you learned

- Big, rare merges and releases create a vicious circle of fear
- CI/CD breaks it: **small changes, verified and shipped automatically**
- **CI** verifies; **CD** delivers
- A **pipeline** is the assembly line a change travels down
- CI/CD is a practice first and a toolset second

---

<p align="center">
  <a href="../../01-introduction-to-github-actions/05-cheat-sheet-and-quiz/README.md">⬅️ Chapter 1 Quiz</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="../index.md">📚 Chapter 2</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="../02-continuous-integration/README.md"><b>Next: Continuous Integration ➡️</b></a>
</p>
