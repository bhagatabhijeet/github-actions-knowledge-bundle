---
type: Tutorial
title: How GitHub Actions Answers the Problem
description: The install list and the six pains checked against GitHub Actions line by line - hosted runners, fresh machines, actions instead of plugins - with the honest trade-offs and when a traditional tool is still the right call.
tags: [github-actions, ci-cd, hosted-runners, self-hosted-runners, jenkins, comparison, migration]
status: stable
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-07T00:00:00Z }
sources:
  - id: gh-hosted-runners
    resource: https://docs.github.com/en/actions/concepts/runners/github-hosted-runners
    title: GitHub-hosted runners
  - id: gh-self-hosted-runners
    resource: https://docs.github.com/en/actions/concepts/runners/self-hosted-runners
    title: Self-hosted runners
  - id: gh-runner-images
    resource: https://github.com/actions/runner-images
    title: GitHub Actions runner images (preinstalled software lists)
  - id: gh-migrate-jenkins
    resource: https://docs.github.com/en/actions/tutorials/migrate-to-github-actions/manual-migrations/migrate-from-jenkins
    title: Migrating from Jenkins to GitHub Actions
  - id: gh-secure-use
    resource: https://docs.github.com/en/actions/reference/security/secure-use
    title: Secure use reference
  - id: gh-billing
    resource: https://docs.github.com/en/billing/concepts/product-billing/github-actions
    title: GitHub Actions billing
---

<p align="center">
  <b>Lesson 3 of 4</b> &nbsp;·&nbsp; ⏱️ 9 min read &nbsp;·&nbsp; 🟢 Beginner
</p>

# 🛟 How GitHub Actions Answers the Problem

[Lesson 1](../01-the-problem-statement/README.md) ended with Abhijeet choosing GitHub Actions. [Lesson 2](../02-hidden-costs-of-self-hosted-ci/README.md) listed the six pains he avoided. They share one root: **you were running a tool**. GitHub Actions changes the deal. You stop running a tool and start using a service.

## 🗺️ In this topic

11 subtopics, about 18 minutes in all. Read them in order, or jump to the one you need.

| # | Subtopic | Time |
|---|---|---|
| 1 | 🎯 [**The shift in one picture**](01-the-shift-in-one-picture.md) | 1 min |
| 2 | 🧾 [**Abhijeet's install list, revisited**](02-abhijeet-s-install-list-revisited.md) | 3 min |
| 3 | ✅ [**Six pains, six answers**](03-six-pains-six-answers.md) | 2 min |
| 4 | 🧩 [**Plugins vs actions**](04-plugins-vs-actions.md) | 1 min |
| 5 | 🔍 [**Same pipeline, two worlds**](05-same-pipeline-two-worlds.md) | 2 min |
| 6 | 🧾 [**What is still your job**](06-what-is-still-your-job.md) | 1 min |
| 7 | ⚖️ [**The honest trade-offs**](07-the-honest-trade-offs.md) | 1 min |
| 8 | 🌉 [**The middle path: self-hosted runners**](08-the-middle-path-self-hosted-runners.md) | 2 min |
| 9 | 🧭 [**So which should you use?**](09-so-which-should-you-use.md) | 2 min |
| 10 | 🚚 [**Already on a traditional tool?**](10-already-on-a-traditional-tool.md) | 1 min |
| 11 | ✅ [**Checkpoint**](11-checkpoint.md) | 2 min |

<p align="center">
  <a href="01-the-shift-in-one-picture.md"><b>▶️ Start with The shift in one picture</b></a>
</p>

## 🎯 What you learned

- GitHub Actions swaps **running a tool** for **using a service**: you keep only the pipeline definition
- Abhijeet's seven-task install list collapses into **`runs-on`, a setup action and a matrix**
- Hosted runners answer the queue, snowflake and upkeep problems with a **fresh machine per job**
- **Actions** are versioned per workflow, so upgrades are local and safe
- You still own workflows, secrets, action hygiene and cost
- The trade-offs are real: **GitHub lock-in, no private-network access by default, less machine control**
- **Self-hosted runners** are the middle path, and they bring some upkeep back

---

<p align="center">
  <a href="../02-hidden-costs-of-self-hosted-ci/README.md">⬅️ The Hidden Costs</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="../index.md">📚 Chapter 3</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="../04-cheat-sheet-and-quiz/README.md"><b>Next: Cheat Sheet & Quiz ➡️</b></a>
</p>
