---
type: Tutorial
title: "What is GitHub Actions?: What does it cost?"
description: "What GitHub Actions costs: free on standard runners in public repositories, a monthly minute allowance in private ones, plus the storage and time limits that apply either way."
tags: [github-actions, introduction, automation, beginner]
status: stable
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-26T00:00:00Z }
sources:
  - id: gh-understand
    resource: https://docs.github.com/en/actions/get-started/understand-github-actions
    title: Understanding GitHub Actions
  - id: gh-billing
    resource: https://docs.github.com/en/billing/concepts/product-billing/github-actions
    title: GitHub Actions billing
  - id: gh-limits
    resource: https://docs.github.com/en/actions/reference/limits
    title: Actions limits
---

<p align="center">
  <a href="README.md">📂 <b>What is GitHub Actions?</b></a> &nbsp;·&nbsp; Lesson 1 · Part 6 of 8 &nbsp;·&nbsp; ⏱️ 2 min
</p>

# 💸 What does it cost?

| Repository | Standard GitHub-hosted runners |
|---|---|
| 🌍 **Public** | Free |
| 🔒 **Private** | A monthly allowance of free minutes (2,000 on the Free plan), then pay per minute |

A few details worth knowing before your first private-repo bill:

- 🐧 **Linux is the cheapest.** Jobs on GitHub-hosted Windows and macOS runners cost more per minute than Linux jobs.
- 🗄️ **Storage has its own allowance.** The Free plan includes 500 MB of artifact storage (shared with GitHub Packages) and, separately, 10 GB of cache per repository.
- 💪 **Larger runners are always billed**, even in public repositories. Only *standard* hosted runners are free there.
- 🏠 **Self-hosted runners are free** to use with Actions. You pay for the machine, not the minutes.

> [!NOTE]
> **📘 From the GitHub docs:** free does not mean unlimited. Each job on a GitHub-hosted runner can run for at most **6 hours**, a whole workflow run for at most **35 days**, and the Free plan runs up to **20** standard hosted jobs at once. ([Actions limits](https://docs.github.com/en/actions/reference/limits))

Billing details change over time, so treat the [official billing page](https://docs.github.com/en/billing/concepts/product-billing/github-actions) as the source of truth. For following this guide in a public repository, you will pay nothing.

---

<p align="center">
  <a href="05-where-it-lives.md">⬅️ Where it lives</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="07-why-not-just-use-a-script.md"><b>Next: Why not just use a script? ➡️</b></a>
</p>
