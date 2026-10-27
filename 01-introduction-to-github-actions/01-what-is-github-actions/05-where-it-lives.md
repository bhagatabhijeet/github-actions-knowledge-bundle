---
type: Tutorial
title: "What is GitHub Actions?: Where it lives"
description: "Where GitHub Actions lives: workflow files in .github/workflows/ and run history in the repository"s Actions tab."
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
  <a href="README.md">📂 <b>What is GitHub Actions?</b></a> &nbsp;·&nbsp; Lesson 1 · Part 5 of 8 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# 🧭 Where it lives

There is nothing to install and no server to rent. Two places matter:

```text
your-repo/
├── .github/
│   └── workflows/        👈 your instructions live here, as .yml files
│       └── ci.yml
├── src/
└── README.md
```

and the **Actions** tab at the top of every repository on GitHub, where you watch runs happen live.

> [!TIP]
> Because workflows are just files in your repo, they get everything code gets: version history, code review, branches, and blame. Your automation is no longer a mystery living on one person's laptop.

---

<p align="center">
  <a href="04-what-can-it-actually-do.md">⬅️ What can it actually do?</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="06-what-does-it-cost.md"><b>Next: What does it cost? ➡️</b></a>
</p>
