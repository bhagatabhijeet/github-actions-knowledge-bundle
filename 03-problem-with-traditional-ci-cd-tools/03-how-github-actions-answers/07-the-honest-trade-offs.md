---
type: Tutorial
title: "How GitHub Actions Answers the Problem: The honest trade-offs"
description: "A fair comparison has two columns. Here is what you give up."
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
  <a href="README.md">📂 <b>How GitHub Actions Answers the Problem</b></a> &nbsp;·&nbsp; Lesson 3 · Part 7 of 11 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# ⚖️ The honest trade-offs

A fair comparison has two columns. Here is what you give up.

| | Trade-off | What it means |
|---|---|---|
| 🔒 | **Tied to GitHub** | Workflow syntax is specific to GitHub. Moving to another platform means rewriting pipelines |
| 🌐 | **Hosted runners live on the public internet** | They can't reach a database or server inside your private network without extra setup |
| 🔧 | **Less control over the machine** | You pick from the runner sizes and images GitHub offers |
| ⏱️ | **Job time limit** | A job on a GitHub-hosted runner is stopped after 6 hours |
| 💰 | **Cost at very high volume** | Per-minute pricing can exceed the cost of your own machines if you build constantly |
| 🚨 | **Someone else's outage** | If the service has an incident, you wait. You can't log in and fix it |

---

<p align="center">
  <a href="06-what-is-still-your-job.md">⬅️ What is still your job</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="08-the-middle-path-self-hosted-runners.md"><b>Next: The middle path: self-hosted runners ➡️</b></a>
</p>
