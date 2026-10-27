---
type: Tutorial
title: The Problem Statement
description: A new DevOps lead plans a pipeline for a Node.js project, picks a traditional CI server, and discovers how much he must install and maintain before the first build - the case that leads to GitHub Actions.
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
  <img src="../../assets/images/chapter-03-banner.svg" alt="Chapter 3: The Problem with Traditional CI/CD Tools" width="100%">
</p>

<p align="center">
  <b>Lesson 1 of 4</b> &nbsp;·&nbsp; ⏱️ 7 min read &nbsp;·&nbsp; 🟢 No experience needed
</p>

# 🧯 The Problem Statement

Chapter 2 convinced you that CI/CD is worth doing. It skipped one awkward question: **what does the pipeline run on?**

For years the answer was "a server we look after ourselves". This chapter is about what that costs. To make it concrete, we'll follow one person through the decision.

## 🗺️ In this topic

9 subtopics, about 15 minutes in all. Read them in order, or jump to the one you need.

| # | Subtopic | Time |
|---|---|---|
| 1 | 🏢 [**Meet Tessaloop Technologies**](01-meet-tessaloop-technologies.md) | 2 min |
| 2 | 🔎 [**What Abhijeet found**](02-what-abhijeet-found.md) | 1 min |
| 3 | 🗺️ [**His four-step plan**](03-his-four-step-plan.md) | 2 min |
| 4 | 🤔 [**Which tool will run all this?**](04-which-tool-will-run-all-this.md) | 1 min |
| 5 | 🧾 [**The bill before the first build**](05-the-bill-before-the-first-build.md) | 3 min |
| 6 | 🧱 [**What "traditional CI/CD tool" means here**](06-what-traditional-ci-cd-tool-means-here.md) | 2 min |
| 7 | 📝 [**The problem statement**](07-the-problem-statement.md) | 1 min |
| 8 | 🎯 [**Abhijeet's two criteria**](08-abhijeet-s-two-criteria.md) | 1 min |
| 9 | ✅ [**Checkpoint**](09-checkpoint.md) | 2 min |

<p align="center">
  <a href="01-meet-tessaloop-technologies.md"><b>▶️ Start with Meet Tessaloop Technologies</b></a>
</p>

## 🎯 What you learned

- A traditional CI/CD tool is a **server you operate**: central server, build agents, plugins
- A good pipeline plan can still stall on **the cost of the tool that runs it**
- The setup list grows with **every language, cloud and scanner** you add
- The practice of CI/CD was never the problem; **running the infrastructure** is
- Abhijeet's criteria: **easy to start**, and **pipelines, not infrastructure**

---

<p align="center">
  <a href="../../02-basics-of-ci-cd/06-cheat-sheet-and-quiz/README.md">⬅️ Chapter 2 Quiz</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="../index.md">📚 Chapter 3</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="../02-hidden-costs-of-self-hosted-ci/README.md"><b>Next: The Hidden Costs ➡️</b></a>
</p>
