---
type: Tutorial
title: "What is CI/CD?: Three myths"
description: "It's a practice. GitHub Actions, Jenkins, GitLab CI and CircleCI are tools that help you do it. You can own every tool and still not practise CI, for example if branches live for a month before merging."
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
  <a href="README.md">📂 <b>What is CI/CD?</b></a> &nbsp;·&nbsp; Lesson 1 · Part 6 of 6 &nbsp;·&nbsp; ⏱️ 2 min
</p>

# 🚫 Three myths

<details>
<summary><b>"CI/CD is a tool you install"</b></summary>

<br>

It's a **practice**. GitHub Actions, Jenkins, GitLab CI and CircleCI are tools that help you do it. You can own every tool and still not practise CI, for example if branches live for a month before merging.

</details>

<details>
<summary><b>"It's only for big companies"</b></summary>

<br>

A solo developer benefits on day one. The first time a workflow catches a typo that would have broken your site, it has paid for itself. And it costs nothing on a public repo.

</details>

<details>
<summary><b>"We need lots of tests before we can start"</b></summary>

<br>

Start with a pipeline that only checks the code builds. That alone catches a surprising number of mistakes. Add tests one at a time. A small pipeline today beats a perfect one next quarter.

</details>

---

<p align="center">
  <a href="05-what-you-get-out-of-it.md">⬅️ What you get out of it</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md#-what-you-learned"><b>Wrap up: What you learned ➡️</b></a>
</p>
