---
type: Tutorial
title: What Are Actions?
description: The reusable building blocks of GitHub Actions - what an action is, how to read a uses line, the three kinds of action, where to find them in the Marketplace, and how to pin them safely.
tags: [github-actions, actions, uses, marketplace, composite, docker, javascript, security]
status: stable
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-25T00:00:00Z }
sources:
  - id: gh-about-actions
    resource: https://docs.github.com/en/actions/concepts/workflows-and-actions/custom-actions
    title: About custom actions
  - id: gh-workflow-syntax
    resource: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
    title: Workflow syntax for GitHub Actions
  - id: gh-secure-use
    resource: https://docs.github.com/en/actions/reference/security/secure-use
    title: Secure use reference
  - id: gh-marketplace
    resource: https://github.com/marketplace?type=actions
    title: GitHub Marketplace - Actions
---

<p align="center">
  <b>Lesson 4 of 14</b> &nbsp;·&nbsp; ⏱️ 9 min read &nbsp;·&nbsp; 🟢 Beginner
</p>

# 🧩 What Are Actions?

The product is called GitHub *Actions*, yet so far we've talked about workflows, jobs, steps and runners. This lesson is about the piece that gives the product its name.

## 🗺️ In this topic

7 subtopics, about 10 minutes in all. Read them in order, or jump to the one you need.

| # | Subtopic | Time |
|---|---|---|
| 1 | 💡 [**The one-sentence definition**](01-the-one-sentence-definition.md) | 1 min |
| 2 | 🔬 [**Reading a `uses:` line**](02-reading-a-uses-line.md) | 1 min |
| 3 | ⚖️ [**Action vs command: the two kinds of step**](03-action-vs-command-the-two-kinds-of.md) | 1 min |
| 4 | 🧱 [**The three kinds of action**](04-the-three-kinds-of-action.md) | 1 min |
| 5 | 🛒 [**Where actions come from**](05-where-actions-come-from.md) | 2 min |
| 6 | 🔐 [**Pinning: which version should you use?**](06-pinning-which-version-should-you-use.md) | 2 min |
| 7 | ✅ [**Checkpoint**](07-checkpoint.md) | 2 min |

<p align="center">
  <a href="01-the-one-sentence-definition.md"><b>▶️ Start with The one-sentence definition</b></a>
</p>

## 🎯 What you learned

- An **action** is a reusable, packaged step called with **`uses:`**
- A reference reads **owner / repository @ version**, and **`with:`** passes inputs
- Steps either **call an action** (`uses:`) or **run a command** (`run:`)
- Three kinds: **JavaScript** (fast, every OS), **Docker** (own environment, Linux), **composite** (bundled YAML steps)
- Actions come from the **Marketplace**, other repositories, **your own repo**, or Docker images
- **Pin third-party actions to a full commit SHA**, and let Dependabot keep them fresh

---

<p align="center">
  <a href="../03-github-hosted-vs-self-hosted-runners/README.md">⬅️ Hosted vs Self-Hosted Runners</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="../index.md">📚 Chapter 4</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="../05-configuring-the-checkout-action/README.md"><b>Next: Configuring Checkout ➡️</b></a>
</p>
