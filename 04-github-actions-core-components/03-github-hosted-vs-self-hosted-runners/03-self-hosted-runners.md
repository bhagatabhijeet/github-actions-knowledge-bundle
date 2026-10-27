---
type: Tutorial
title: "GitHub-Hosted vs Self-Hosted Runners: Self-hosted runners"
description: "You install GitHub's small runner application on a machine you control: a server, a VM, a cloud instance, even a laptop. It connects to GitHub and waits for jobs."
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
  <a href="README.md">📂 <b>GitHub-Hosted vs Self-Hosted Runners</b></a> &nbsp;·&nbsp; Lesson 3 · Part 3 of 8 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# 🏢 Self-hosted runners

You install GitHub's small runner application on a machine you control: a server, a VM, a cloud instance, even a laptop. It connects to GitHub and waits for jobs.

| | What you get | Detail |
|---|---|---|
| 🎛️ | **Full control** | Your operating system, your tools, your hardware |
| 🌐 | **Your network** | Jobs can reach internal databases and services directly |
| 💪 | **Special hardware** | GPUs, large memory, unusual CPU architectures |
| 💾 | **A machine that remembers** | Files and caches stay between jobs |
| 🧹 | **All the upkeep** | Patching, cleaning, monitoring and scaling are yours |

That last pair is two sides of one coin. A machine that keeps its state is faster to warm up, and it is also how builds start to depend on leftovers.

---

<p align="center">
  <a href="02-github-hosted-runners.md">⬅️ GitHub-hosted runners</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="04-side-by-side.md"><b>Next: Side by side ➡️</b></a>
</p>
