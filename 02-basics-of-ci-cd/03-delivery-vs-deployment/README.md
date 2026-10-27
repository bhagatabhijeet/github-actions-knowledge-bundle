---
type: Tutorial
title: Continuous Delivery vs Continuous Deployment
description: The two meanings of CD untangled - one keeps a human approval before production, the other removes it - with environments, artifacts and how to choose.
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
  <b>Lesson 3 of 6</b> &nbsp;·&nbsp; ⏱️ 7 min read &nbsp;·&nbsp; 🟢 Beginner
</p>

# 🚚 Delivery vs 🚀 Deployment

CI told you a change is *good*. CD is about getting that good change *to users*. And "CD" hides two different promises.

## 🗺️ In this topic

7 subtopics, about 9 minutes in all. Read them in order, or jump to the one you need.

| # | Subtopic | Time |
|---|---|---|
| 1 | 🎯 [**The difference in one picture**](01-the-difference-in-one-picture.md) | 1 min |
| 2 | 🪜 [**Three rungs of one ladder**](02-three-rungs-of-one-ladder.md) | 1 min |
| 3 | 🏗️ [**Environments: the rehearsal stages**](03-environments-the-rehearsal-stages.md) | 2 min |
| 4 | 📦 [**Build once, deploy many**](04-build-once-deploy-many.md) | 2 min |
| 5 | 🛟 [**Deploying without fear**](05-deploying-without-fear.md) | 1 min |
| 6 | 🧭 [**Which one should you choose?**](06-which-one-should-you-choose.md) | 1 min |
| 7 | ✅ [**Checkpoint**](07-checkpoint.md) | 1 min |

<p align="center">
  <a href="01-the-difference-in-one-picture.md"><b>▶️ Start with The difference in one picture</b></a>
</p>

---

<p align="center">
  <a href="../02-continuous-integration/README.md">⬅️ Continuous Integration</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="../index.md">📚 Chapter 2</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="../04-anatomy-of-a-pipeline/README.md"><b>Next: Anatomy of a Pipeline ➡️</b></a>
</p>
