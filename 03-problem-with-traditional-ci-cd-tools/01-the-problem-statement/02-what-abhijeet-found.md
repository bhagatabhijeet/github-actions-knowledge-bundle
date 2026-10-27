---
type: Tutorial
title: "The Problem Statement: What Abhijeet found"
description: "Before designing anything, he takes a quick look at how the Node.js project has been built so far."
tags: [ci-cd, problem-statement, devops, self-hosted, jenkins, beginner]
status: stable
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-07T00:00:00Z }
sources:
  - id: jenkins-install
    resource: https://www.jenkins.io/doc/book/installing/
    title: Installing Jenkins (Jenkins User Handbook)
  - id: jenkins-scale
    resource: https://www.jenkins.io/doc/book/scaling/architecting-for-scale/
    title: Architecting for Scale (Jenkins User Handbook)
  - id: gh-understand
    resource: https://docs.github.com/en/actions/get-started/understand-github-actions
    title: Understanding GitHub Actions
---

<p align="center">
  <a href="README.md">📂 <b>The Problem Statement</b></a> &nbsp;·&nbsp; Lesson 1 · Part 2 of 9 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# 🔎 What Abhijeet found

Before designing anything, he takes a quick look at how the Node.js project has been built so far.

| | What he found | What it leads to |
|---|---|---|
| 📂 | No shared version control. Code is combined by hand | Nobody is sure which copy is the real one |
| 🧪 | Tests are run by hand | They are slow, so they get skipped |
| 🏝️ | Developers work alone for long stretches | Their changes collide when they finally meet |
| 📦 | Integration and testing happen rarely | Every release is large, and risky |
| 🖐️ | Deployments to dev, staging and production are manual | Each environment ends up slightly different |

If that sounds like "life before CI/CD" from [Chapter 2](../../02-basics-of-ci-cd/01-what-is-ci-cd/README.md), it is. Same disease, different company.

---

<p align="center">
  <a href="01-meet-tessaloop-technologies.md">⬅️ Meet Tessaloop Technologies</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="03-his-four-step-plan.md"><b>Next: His four-step plan ➡️</b></a>
</p>
