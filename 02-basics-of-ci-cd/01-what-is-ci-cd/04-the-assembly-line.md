---
type: Tutorial
title: "What is CI/CD?: The assembly line"
description: "The mental model is a factory line. Raw material (a commit) goes in one end. It passes a series of stations. Each station either stamps it ✅ and passes it on, or pulls the cord and stops the line. What comes out the far..."
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
  <a href="README.md">📂 <b>What is CI/CD?</b></a> &nbsp;·&nbsp; Lesson 1 · Part 4 of 6 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# 🏭 The assembly line

The mental model is a factory line. Raw material (a commit) goes in one end. It passes a series of stations. Each station either stamps it ✅ and passes it on, or pulls the cord and stops the line. What comes out the far end is a product you'd trust in a customer's hands.

That line is called a **pipeline**, and you'll build one by the end of this chapter.

---

<p align="center">
  <a href="03-decoding-the-letters.md">⬅️ Decoding the letters</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="05-what-you-get-out-of-it.md"><b>Next: What you get out of it ➡️</b></a>
</p>
