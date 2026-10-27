---
type: Tutorial
title: "Continuous Delivery vs Continuous Deployment: The difference in one picture"
description: "The only difference is who presses the final button."
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
  <a href="README.md">📂 <b>Continuous Delivery vs Continuous Deployment</b></a> &nbsp;·&nbsp; Lesson 3 · Part 1 of 7 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# 🎯 The difference in one picture

<p align="center">
  <img src="../../assets/images/delivery-vs-deployment.svg" alt="Continuous delivery pauses for a human approval before production. Continuous deployment does not" width="100%">
</p>

**The only difference is who presses the final button.**

| | 🚚 Continuous Delivery | 🚀 Continuous Deployment |
|---|---|---|
| **Promise** | Every change *could* go live at any moment | Every change *does* go live |
| **Final step to production** | A human clicks **Approve** | Fully automatic |
| **Release frequency** | When the business chooses | Many times a day |
| **What you need** | A reliable, automated deploy | That, plus great tests and monitoring |
| **Fits** | Regulated industries, mobile apps, scheduled launches | Web apps and services with strong test coverage |

> [!TIP]
> **Memory hook:** *Delivery* brings the parcel to your door and waits for a signature. *Deployment* leaves it inside the house.

---

<p align="center">
  <a href="README.md">⬅️ Overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="02-three-rungs-of-one-ladder.md"><b>Next: Three rungs of one ladder ➡️</b></a>
</p>
