---
type: Tutorial
title: "What is GitHub Actions?: Why not just use a script?"
description: "Why a workflow beats running ./deploy.sh by hand: it runs when you forget, on a clean machine, visible to the team, and can block a bad merge."
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
  <a href="README.md">📂 <b>What is GitHub Actions?</b></a> &nbsp;·&nbsp; Lesson 1 · Part 7 of 8 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# 🆚 Why not just use a script?

A fair question. You could run `./deploy.sh` yourself. Here is what you'd be giving up:

| | A script on your laptop | GitHub Actions |
|---|---|---|
| Runs when you forget? | ❌ | ✅ |
| Clean machine every time? | ❌ "works on my machine" | ✅ |
| Visible to the whole team? | ❌ | ✅ |
| Blocks a bad merge? | ❌ | ✅ |
| Runs on Linux, Windows and macOS? | ❌ | ✅ |

The script is still valuable. GitHub Actions is what runs it reliably.

---

<p align="center">
  <a href="06-what-does-it-cost.md">⬅️ What does it cost?</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="08-checkpoint.md"><b>Next: Checkpoint ➡️</b></a>
</p>
