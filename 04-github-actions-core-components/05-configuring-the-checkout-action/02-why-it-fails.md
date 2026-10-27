---
type: Tutorial
title: "Configuring the Checkout Action: Why it fails"
description: "The runner does not have your code. It's a brand-new virtual machine. Your workflow file was read by GitHub to plan the run, but the repository itself is never copied onto the runner unless a step does it. That step is..."
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
  <a href="README.md">📂 <b>Configuring the Checkout Action</b></a> &nbsp;·&nbsp; Lesson 5 · Part 2 of 7 &nbsp;·&nbsp; ⏱️ 2 min
</p>

# 🔎 Why it fails

<p align="center">
  <img src="../../assets/images/checkout-before-after.svg" alt="Without checkout the runner's workspace is empty, ls prints nothing and cat README.md fails with exit code 1. With actions/checkout first, ls lists the repository files and cat prints the README" width="100%">
</p>

| Step | What happened | Why |
|---|---|---|
| 👋 Welcome message | ✅ Printed the text | `echo` doesn't need any files |
| 📂 List files | ✅ Printed **nothing** | The workspace folder exists, but it's empty |
| 📄 Read file | ❌ `No such file or directory` | There is no `README.md` on this machine |

> [!IMPORTANT]
> **The runner does not have your code.** It's a brand-new virtual machine. Your workflow file was read by GitHub to *plan* the run, but the repository itself is never copied onto the runner unless a step does it. That step is `actions/checkout`.

---

<p align="center">
  <a href="01-a-workflow-that-looks-right.md">⬅️ A workflow that looks right</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="03-the-fix-one-line.md"><b>Next: The fix: one line ➡️</b></a>
</p>
