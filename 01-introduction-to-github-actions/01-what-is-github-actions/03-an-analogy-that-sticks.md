---
type: Tutorial
title: "What is GitHub Actions?: An analogy that sticks"
description: "A restaurant-kitchen analogy that maps orders, recipe cards, cooks, cooking steps and ready-made sauces onto events, workflows, runners, steps and actions."
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
  <a href="README.md">📂 <b>What is GitHub Actions?</b></a> &nbsp;·&nbsp; Lesson 1 · Part 3 of 8 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# 🍳 An analogy that sticks

Think of a restaurant kitchen.

| Kitchen | GitHub Actions |
|---|---|
| 🛎️ An order arrives | An **event** fires (a push, a pull request, a timer) |
| 📖 The recipe card | A **workflow** file you wrote in YAML |
| 👩‍🍳 A cook at a clean station | A **runner**: a fresh virtual machine |
| 🔪 Chop, sear, plate | **Steps**, performed in order |
| 🧂 A ready-made sauce from the pantry | An **action**: reusable logic someone already packaged |

The cook doesn't improvise and doesn't get tired. They follow the card exactly, every time, at 3 am on a Sunday if that's when the order comes in.

---

<p align="center">
  <a href="02-the-one-sentence-definition.md">⬅️ The one-sentence definition</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="04-what-can-it-actually-do.md"><b>Next: What can it actually do? ➡️</b></a>
</p>
