---
type: Tutorial
title: "The Problem Statement: What \"traditional CI/CD tool\" means here"
description: "In this guide, a traditional CI/CD tool is a CI server that you install and operate yourself. Jenkins is the best-known example. TeamCity and Bamboo are in the same family when run on your own machines."
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
  <a href="README.md">📂 <b>The Problem Statement</b></a> &nbsp;·&nbsp; Lesson 1 · Part 6 of 9 &nbsp;·&nbsp; ⏱️ 2 min
</p>

# 🧱 What "traditional CI/CD tool" means here

In this guide, a **traditional CI/CD tool** is a CI server that you install and operate yourself. Jenkins is the best-known example. TeamCity and Bamboo are in the same family when run on your own machines.

They share a shape:

| | Part | Job |
|---|---|---|
| 🧠 | **A central server** | Stores the pipeline configuration, schedules builds, shows the dashboard |
| 💪 | **Build agents** | The machines that actually run your builds |
| 🧩 | **Plugins** | Add-ons that teach the server to talk to Git, Docker, Slack, your cloud |

Every one of those parts is software running on a machine that **somebody on your team has to keep alive**.

> [!NOTE]
> This is not a claim that these tools are bad. They are powerful, flexible and proven at enormous scale. The problem is the amount of care they need, and who ends up providing it.

---

<p align="center">
  <a href="05-the-bill-before-the-first-build.md">⬅️ The bill before the first build</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="07-the-problem-statement.md"><b>Next: The problem statement ➡️</b></a>
</p>
