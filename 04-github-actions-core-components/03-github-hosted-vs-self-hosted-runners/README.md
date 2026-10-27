---
type: Tutorial
title: GitHub-Hosted vs Self-Hosted Runners
description: The two kinds of runner compared - who maintains them, what state they keep, how far you can customise them, what they cost - plus two common myths and a guide to choosing.
tags: [github-actions, runners, github-hosted, self-hosted, comparison]
status: stable
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-07T00:00:00Z }
sources:
  - id: gh-hosted-runners
    resource: https://docs.github.com/en/actions/concepts/runners/github-hosted-runners
    title: GitHub-hosted runners
  - id: gh-self-hosted-runners
    resource: https://docs.github.com/en/actions/concepts/runners/self-hosted-runners
    title: Self-hosted runners
  - id: gh-runner-images
    resource: https://github.com/actions/runner-images
    title: GitHub Actions runner images (preinstalled software lists)
  - id: gh-secure-use
    resource: https://docs.github.com/en/actions/reference/security/secure-use
    title: Secure use reference
  - id: gh-billing
    resource: https://docs.github.com/en/billing/concepts/product-billing/github-actions
    title: GitHub Actions billing
---

<p align="center">
  <b>Lesson 3 of 14</b> &nbsp;·&nbsp; ⏱️ 8 min read &nbsp;·&nbsp; 🟢 Beginner
</p>

# 🖥️ GitHub-Hosted vs Self-Hosted Runners

Every job needs a machine. So far GitHub has supplied it. You can also supply your own. This lesson is about the difference, and how to choose.

## 🗺️ In this topic

8 subtopics, about 13 minutes in all. Read them in order, or jump to the one you need.

| # | Subtopic | Time |
|---|---|---|
| 1 | 🎯 [**The difference in one picture**](01-the-difference-in-one-picture.md) | 1 min |
| 2 | ☁️ [**GitHub-hosted runners**](02-github-hosted-runners.md) | 4 min |
| 3 | 🏢 [**Self-hosted runners**](03-self-hosted-runners.md) | 1 min |
| 4 | ⚖️ [**Side by side**](04-side-by-side.md) | 1 min |
| 5 | 🚫 [**Two myths**](05-two-myths.md) | 2 min |
| 6 | 🛡️ [**One security rule**](06-one-security-rule.md) | 2 min |
| 7 | 🧭 [**Which should you choose?**](07-which-should-you-choose.md) | 2 min |
| 8 | ✅ [**Checkpoint**](08-checkpoint.md) | 2 min |

<p align="center">
  <a href="01-the-difference-in-one-picture.md"><b>▶️ Start with The difference in one picture</b></a>
</p>

## 🎯 What you learned

- **`runs-on`** is the single switch between the two kinds of runner
- **GitHub-hosted**: clean VM per job, preinstalled tools, no upkeep
- **Self-hosted**: your network and hardware, persistent state, all the upkeep
- You **can** install software on a hosted runner; it just doesn't persist
- Avoid self-hosted runners on **public repositories**
- **Start hosted**, and switch only for a named reason

---

<p align="center">
  <a href="../02-life-of-a-workflow-run/README.md">⬅️ Life of a Workflow Run</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="../index.md">📚 Chapter 4</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="../04-what-are-actions/README.md"><b>Next: What Are Actions? ➡️</b></a>
</p>
