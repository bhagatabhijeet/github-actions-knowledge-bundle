---
type: Tutorial
title: Configuring the Checkout Action (Hands-On)
description: Why a fresh runner has none of your code, how actions/checkout fixes it, and the inputs you'll actually use - fetch-depth, ref, path, repository, token, submodules, sparse-checkout and persist-credentials.
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
  <b>Lesson 5 of 14</b> &nbsp;·&nbsp; ⏱️ 15 min &nbsp;·&nbsp; 🛠️ Hands-on
</p>

# 📥 Configuring the Checkout Action

You've seen `actions/checkout` at the top of almost every workflow. This lesson shows what goes wrong without it, and how to configure it.

## 🗺️ In this topic

7 subtopics, about 12 minutes in all. Read them in order, or jump to the one you need.

| # | Subtopic | Time |
|---|---|---|
| 1 | 🧪 [**A workflow that looks right**](01-a-workflow-that-looks-right.md) | 1 min |
| 2 | 🔎 [**Why it fails**](02-why-it-fails.md) | 2 min |
| 3 | ✅ [**The fix: one line**](03-the-fix-one-line.md) | 2 min |
| 4 | ⚙️ [**Configuring it with `with:`**](04-configuring-it-with-with.md) | 3 min |
| 5 | 🛠️ [**Try it yourself**](05-try-it-yourself.md) | 1 min |
| 6 | 🧯 [**Something went wrong?**](06-something-went-wrong.md) | 1 min |
| 7 | ✅ [**Checkpoint**](07-checkpoint.md) | 2 min |

<p align="center">
  <a href="01-a-workflow-that-looks-right.md"><b>▶️ Start with A workflow that looks right</b></a>
</p>

## 🎯 What you learned

- A fresh runner is **empty**. Your code arrives only through **`actions/checkout`**
- Put checkout **first** in any job that reads your files
- By default it fetches **one commit**, at the **triggering ref**, into the **workspace root**
- Configure it with **`with:`**: `fetch-depth`, `ref`, `path`, `repository`, `token`, `sparse-checkout` and more
- Prefer **`persist-credentials: false`** when later steps don't need git auth

---

<p align="center">
  <a href="../04-what-are-actions/README.md">⬅️ What Are Actions?</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="../index.md">📚 Chapter 4</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="../06-multiline-commands-and-third-party-tools/README.md"><b>Next: Multi-line Commands ➡️</b></a>
</p>
