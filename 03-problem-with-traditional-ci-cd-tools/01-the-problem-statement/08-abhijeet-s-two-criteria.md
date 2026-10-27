---
type: Tutorial
title: "The Problem Statement: Abhijeet's two criteria"
description: "So he goes looking again, this time with two requirements written at the top of the page:"
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
  <a href="README.md">📂 <b>The Problem Statement</b></a> &nbsp;·&nbsp; Lesson 1 · Part 8 of 9 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# 🎯 Abhijeet's two criteria

So he goes looking again, this time with two requirements written at the top of the page:

| | Criterion | What it rules out |
|---|---|---|
| 1️⃣ | **Simple to set up and start**, with no long list of services to install and configure | The seven-task list above |
| 2️⃣ | **Lets the team focus on building pipelines**, not on managing infrastructure or worrying about scale | Owning servers and agents |

After evaluating several tools against those two lines, he decides to explore and adopt **GitHub Actions**.

The next two lessons explain why. [Lesson 2](../02-hidden-costs-of-self-hosted-ci/README.md) shows that his list was only the down payment. [Lesson 3](../03-how-github-actions-answers/README.md) holds GitHub Actions up against it, line by line.

---

<p align="center">
  <a href="07-the-problem-statement.md">⬅️ The problem statement</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="09-checkpoint.md"><b>Next: Checkpoint ➡️</b></a>
</p>
