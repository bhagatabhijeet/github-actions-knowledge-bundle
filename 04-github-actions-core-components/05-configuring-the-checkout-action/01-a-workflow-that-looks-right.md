---
type: Tutorial
title: "Configuring the Checkout Action: A workflow that looks right"
description: "Here is a first workflow many people write. It greets you, lists the files and prints the README:"
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
  <a href="README.md">📂 <b>Configuring the Checkout Action</b></a> &nbsp;·&nbsp; Lesson 5 · Part 1 of 7 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# 🧪 A workflow that looks right

Here is a first workflow many people write. It greets you, lists the files and prints the README:

```yaml
name: My First Workflow

on: push

jobs:
  first_job:
    runs-on: ubuntu-latest
    steps:
      - name: Welcome message
        run: echo "My first GitHub Actions job"

      - name: List files
        run: ls

      - name: Read file
        run: cat README.md
```

Push it, and the run goes ❌ red on the last step.

---

<p align="center">
  <a href="README.md">⬅️ Overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="02-why-it-fails.md"><b>Next: Why it fails ➡️</b></a>
</p>
