---
type: Tutorial
title: "Continuous Delivery vs Continuous Deployment: Checkpoint"
description: "Continuous delivery. A human makes the final call."
tags: [ci-cd, continuous-delivery, continuous-deployment, environments, approvals]
status: stable
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-07T00:00:00Z }
sources:
  - id: fowler-cd
    resource: https://martinfowler.com/bliki/ContinuousDelivery.html
    title: Continuous Delivery
    author: Martin Fowler
  - id: gh-cd
    resource: https://docs.github.com/en/actions/get-started/continuous-deployment
    title: Continuous deployment (GitHub Docs)
  - id: gh-environments
    resource: https://docs.github.com/en/actions/how-tos/deploy/configure-and-manage-deployments/manage-environments
    title: Managing environments for deployment
---

<p align="center">
  <a href="README.md">📂 <b>Continuous Delivery vs Continuous Deployment</b></a> &nbsp;·&nbsp; Lesson 3 · Part 7 of 7 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# ✅ Checkpoint

<details>
<summary><b>A team's pipeline deploys to staging automatically, then waits for a manager to approve production. Which CD is that?</b></summary>

<br>

Continuous **delivery**. A human makes the final call.

</details>

<details>
<summary><b>Why is rebuilding the app separately for production a bad idea?</b></summary>

<br>

The production build is then a different artifact from the one you tested. Anything that changed between builds (a dependency, a base image, a compiler) ships untested.

</details>

<details>
<summary><b>Which GitHub Actions setting turns continuous deployment into continuous delivery?</b></summary>

<br>

**Required reviewers** on the environment the deploy job targets.

</details>

---

<p align="center">
  <a href="06-which-one-should-you-choose.md">⬅️ Which one should you choose?</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="../04-anatomy-of-a-pipeline/README.md"><b>Next topic ➡️</b></a>
</p>
