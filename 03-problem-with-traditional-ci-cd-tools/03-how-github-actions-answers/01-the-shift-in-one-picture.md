---
type: Tutorial
title: "How GitHub Actions Answers the Problem: The shift in one picture"
description: "On the left, every layer is yours. On the right, you keep the one layer that is actually about your product: the pipeline definition. That is the workflow file you learned to read in Chapter 1."
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
  <a href="README.md">📂 <b>How GitHub Actions Answers the Problem</b></a> &nbsp;·&nbsp; Lesson 3 · Part 1 of 11 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# 🎯 The shift in one picture

<p align="center">
  <img src="../../assets/images/who-maintains-what.svg" alt="With a self-hosted CI server you maintain all seven layers, from machines up to the pipeline definition. With GitHub Actions on hosted runners you maintain only the pipeline definition" width="100%">
</p>

On the left, every layer is yours. On the right, you keep the one layer that is actually about your product: **the pipeline definition**. That is the workflow file you learned to read in [Chapter 1](../../01-introduction-to-github-actions/03-anatomy-of-a-workflow/README.md).

---

<p align="center">
  <a href="README.md">⬅️ Overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="02-abhijeet-s-install-list-revisited.md"><b>Next: Abhijeet's install list, revisited ➡️</b></a>
</p>
