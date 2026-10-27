---
type: Tutorial
title: "Continuous Delivery vs Continuous Deployment: Environments: the rehearsal stages"
description: "You don't perform a play for the first time on opening night. Code gets rehearsals too, in a series of environments."
tags: [ci-cd, continuous-delivery, continuous-deployment, environments, approvals]
status: stable
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-26T00:00:00Z }
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
  - id: gh-deploy-env-ref
    resource: https://docs.github.com/en/actions/reference/workflows-and-actions/deployments-and-environments
    title: Deployments and environments
---

<p align="center">
  <a href="README.md">📂 <b>Continuous Delivery vs Continuous Deployment</b></a> &nbsp;·&nbsp; Lesson 3 · Part 3 of 7 &nbsp;·&nbsp; ⏱️ 3 min
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

### 🔍 The fine print on approvals

- 👥 You can name up to **six** users or teams as required reviewers. **Only one** of them needs to approve.
- 🙅 Turn on **Prevent self-reviews** and the person who triggered the deployment can't approve their own job, even if they are on the list.
- ⏳ A **wait timer** can hold the job for 1 to 43,200 minutes (30 days) before it starts.
- 🔑 A job that waits for approval can't read the environment's secrets until a reviewer approves it.

> [!NOTE]
> **📘 From the GitHub docs:** Environment secrets are only available to jobs that reference the environment. A test job without `environment: production` simply never sees production credentials. ([Deployments and environments](https://docs.github.com/en/actions/reference/workflows-and-actions/deployments-and-environments))

---

<p align="center">
  <a href="02-three-rungs-of-one-ladder.md">⬅️ Three rungs of one ladder</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="04-build-once-deploy-many.md"><b>Next: Build once, deploy many ➡️</b></a>
</p>
