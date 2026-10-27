---
type: Tutorial
title: "The Problem Statement: Checkpoint"
description: "A CI server that you install and run on your own machines, made of a central server, build agents and plugins. Jenkins is the classic example."
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
  <a href="README.md">📂 <b>The Problem Statement</b></a> &nbsp;·&nbsp; Lesson 1 · Part 9 of 9 &nbsp;·&nbsp; ⏱️ 2 min
</p>

# ✅ Checkpoint

<details>
<summary><b>What do we mean by a "traditional CI/CD tool" in this guide?</b></summary>

<br>

A CI server that you install and run on your own machines, made of a central server, build agents and plugins. Jenkins is the classic example.

</details>

<details>
<summary><b>Was anything wrong with Abhijeet's four-step plan?</b></summary>

<br>

No. Version control, automated tests, containerised deploys and integration tests are exactly right. The problem was the cost of the tool that would run the plan.

</details>

<details>
<summary><b>Why did the install list keep growing?</b></summary>

<br>

Every new language, cloud and security tool the company adopts has to be installed and maintained on the build machine: Java and Maven, Python, cloud CLIs, scanners.

</details>

<details>
<summary><b>What were Abhijeet's two criteria for a better tool?</b></summary>

<br>

Simple to set up without installing and configuring many services, and a focus on building pipelines instead of managing infrastructure and scale.

</details>

---

<p align="center">
  <a href="08-abhijeet-s-two-criteria.md">⬅️ Abhijeet's two criteria</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md#-what-you-learned"><b>Wrap up: What you learned ➡️</b></a>
</p>
