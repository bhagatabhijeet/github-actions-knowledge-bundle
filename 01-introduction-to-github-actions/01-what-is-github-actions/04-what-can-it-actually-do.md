---
type: Tutorial
title: "What is GitHub Actions?: What can it actually do?"
description: "Most people meet GitHub Actions through CI/CD (testing and shipping code), and Chapter 2 is devoted to it. But it is a general-purpose automation tool. If it can be scripted, it can be an Actions workflow."
tags: [github-actions, introduction, automation, beginner]
status: stable
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-07T00:00:00Z }
sources:
  - id: gh-understand
    resource: https://docs.github.com/en/actions/get-started/understand-github-actions
    title: Understanding GitHub Actions
  - id: gh-billing
    resource: https://docs.github.com/en/billing/concepts/product-billing/github-actions
    title: GitHub Actions billing
---

<p align="center">
  <a href="README.md">📂 <b>What is GitHub Actions?</b></a> &nbsp;·&nbsp; Lesson 1 · Part 4 of 8 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# 🎁 What can it actually do?

Most people meet GitHub Actions through CI/CD (testing and shipping code), and [Chapter 2](../../02-basics-of-ci-cd/01-what-is-ci-cd/README.md) is devoted to it. But it is a general-purpose automation tool. If it can be scripted, it can be an Actions workflow.

| | You want to... | Triggered by |
|---|---|---|
| 🧪 | Run tests on every pull request | `pull_request` |
| 🚀 | Deploy the site when `main` changes | `push` |
| 📦 | Publish a package when you cut a release | `release` |
| 🏷️ | Label and triage new issues | `issues` |
| 🌙 | Run a nightly security scan | `schedule` |
| 🔘 | Give teammates a "Deploy" button | `workflow_dispatch` |
| 👋 | Welcome first-time contributors | `pull_request_target` |

👉 [Lesson 2](../02-core-concepts/01-1-event-the-trigger.md#-beyond-cicd-automating-the-repository-itself) maps the repository events you can automate, and their activity types.

---

<p align="center">
  <a href="03-an-analogy-that-sticks.md">⬅️ An analogy that sticks</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="05-where-it-lives.md"><b>Next: Where it lives ➡️</b></a>
</p>
