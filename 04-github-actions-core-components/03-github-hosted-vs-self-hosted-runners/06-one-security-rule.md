---
type: Tutorial
title: "GitHub-Hosted vs Self-Hosted Runners: One security rule"
description: "Be very careful with self-hosted runners on public repositories. Anyone can open a pull request against a public repository. If that pull request's workflow runs on your machine, a stranger's code is executing inside..."
tags: [github-actions, runners, github-hosted, self-hosted, comparison]
status: stable
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-26T00:00:00Z }
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
  <a href="README.md">📂 <b>GitHub-Hosted vs Self-Hosted Runners</b></a> &nbsp;·&nbsp; Lesson 3 · Part 6 of 8 &nbsp;·&nbsp; ⏱️ 2 min
</p>

# 🛡️ One security rule

> [!WARNING]
> **Be very careful with self-hosted runners on public repositories.** Anyone can open a pull request against a public repository. If that pull request's workflow runs on your machine, a stranger's code is executing inside your network, on a machine that doesn't reset afterwards. GitHub recommends using self-hosted runners with private repositories.

The [Secure use reference](https://docs.github.com/en/actions/reference/security/secure-use) is blunter: self-hosted runners **"should almost never be used for public repositories."** Two reasons:

- 🦠 **Compromise can stick.** Untrusted workflow code can leave something behind that the next job inherits. The machine is never wiped clean for you.
- 🎲 **No one-job guarantee.** GitHub says there is no way to guarantee a self-hosted runner only runs one job. Assume jobs can see each other's leftovers.

---

<p align="center">
  <a href="05-two-myths.md">⬅️ Two myths</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="07-which-should-you-choose.md"><b>Next: Which should you choose? ➡️</b></a>
</p>
