---
type: Tutorial
title: "Configuring the Checkout Action: Try it yourself"
description: "This repository ships the before-and-after as a live workflow: 04-checkout.yml."
tags: [github-actions, actions, checkout, hands-on, fetch-depth, sparse-checkout]
status: stable
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-25T00:00:00Z }
sources:
  - id: checkout-repo
    resource: https://github.com/actions/checkout
    title: actions/checkout README
  - id: gh-workflow-syntax
    resource: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
    title: Workflow syntax for GitHub Actions
---

<p align="center">
  <a href="README.md">📂 <b>Configuring the Checkout Action</b></a> &nbsp;·&nbsp; Lesson 5 · Part 5 of 7 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# 🛠️ Try it yourself

This repository ships the before-and-after as a live workflow: [`04-checkout.yml`](../../.github/workflows/04-checkout.yml).

1. Open the **Actions** tab and pick **04 - Checkout**
2. Click **Run workflow**
3. Open **without-checkout**: `ls -la` shows an empty folder, and **Read file** fails (the job is allowed to fail with `continue-on-error`)
4. Open **with-checkout**: the same steps list your files and print the README
5. **Stretch:** fork the repo, add `fetch-depth: 0` and a step running `git log --oneline | wc -l`. Compare the count with and without it.

---

<p align="center">
  <a href="04-configuring-it-with-with.md">⬅️ Configuring it with `with:`</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="06-something-went-wrong.md"><b>Next: Something went wrong? ➡️</b></a>
</p>
