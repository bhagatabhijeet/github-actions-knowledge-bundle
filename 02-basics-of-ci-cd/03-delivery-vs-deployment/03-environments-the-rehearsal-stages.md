---
type: Tutorial
title: "Continuous Delivery vs Continuous Deployment: Environments: the rehearsal stages"
description: "You don't perform a play for the first time on opening night. Code gets rehearsals too, in a series of environments."
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
  <a href="README.md">📂 <b>Continuous Delivery vs Continuous Deployment</b></a> &nbsp;·&nbsp; Lesson 3 · Part 3 of 7 &nbsp;·&nbsp; ⏱️ 2 min
</p>

# 🏗️ Environments: the rehearsal stages

You don't perform a play for the first time on opening night. Code gets rehearsals too, in a series of **environments**.

| | Environment | Audience | Purpose |
|---|---|---|---|
| 💻 | **Development** | You | Try things |
| 🎭 | **Staging** | The team | A production look-alike for a final rehearsal |
| 🌍 | **Production** | Real users | The real thing |

In GitHub Actions, an environment is a named target you attach to a job:

```yaml
jobs:
  deploy:
    runs-on: ubuntu-latest
    environment: production
    steps:
      - run: ./deploy.sh
```

That one line unlocks three things, configured under **Settings → Environments**:

| | Feature | What it does |
|---|---|---|
| ✋ | **Required reviewers** | The job pauses until a named person approves |
| 🔑 | **Environment secrets** | Production credentials only exist for production jobs |
| 🌿 | **Branch restrictions** | Only `main` may deploy here |

> [!IMPORTANT]
> **Required reviewers is the switch between the two CDs.** Turn it on and you have continuous *delivery*. Turn it off and you have continuous *deployment*. The workflow file doesn't change.

---

<p align="center">
  <a href="02-three-rungs-of-one-ladder.md">⬅️ Three rungs of one ladder</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="04-build-once-deploy-many.md"><b>Next: Build once, deploy many ➡️</b></a>
</p>
