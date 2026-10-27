---
type: Tutorial
title: "Continuous Delivery vs Continuous Deployment: Deploying without fear"
description: "A few release strategies you'll hear named. You don't need them yet, but you should recognise the words."
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
  <a href="README.md">📂 <b>Continuous Delivery vs Continuous Deployment</b></a> &nbsp;·&nbsp; Lesson 3 · Part 5 of 7 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# 🛟 Deploying without fear

A few release strategies you'll hear named. You don't need them yet, but you should recognise the words.

| | Strategy | Idea in one line |
|---|---|---|
| 🔄 | **Rolling** | Replace servers a few at a time |
| 🔵🟢 | **Blue-green** | Run old and new side by side, then flip the traffic switch |
| 🐤 | **Canary** | Send 1% of users to the new version and watch before widening |
| 🚩 | **Feature flags** | Ship the code switched off; turn it on later without a deploy |

All of them answer the same question: *how do we find out it's broken while it only affects a few people, and undo it quickly?*

---

<p align="center">
  <a href="04-build-once-deploy-many.md">⬅️ Build once, deploy many</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="06-which-one-should-you-choose.md"><b>Next: Which one should you choose? ➡️</b></a>
</p>
