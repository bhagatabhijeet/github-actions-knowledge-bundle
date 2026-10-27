---
type: Tutorial
title: "GitHub-Hosted vs Self-Hosted Runners: Side by side"
description: "Cost details change. The billing page is the source of truth."
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
  <a href="README.md">📂 <b>GitHub-Hosted vs Self-Hosted Runners</b></a> &nbsp;·&nbsp; Lesson 3 · Part 4 of 8 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# ⚖️ Side by side

| | | ☁️ GitHub-hosted | 🏢 Self-hosted |
|---|---|---|---|
| 🔧 | **Maintained by** | GitHub | You |
| 🧼 | **State** | New, clean VM for every job | Same machine reused, unless you rebuild it |
| 🎛️ | **Customising** | Choose image and size; install extras during the job | Unlimited |
| 🌐 | **Network** | Public cloud | Wherever you put it |
| 💰 | **Cost** | Free on public repositories; metered on private ones | You pay for and operate the machines |
| ⏱️ | **Longest job** | 6 hours | 5 days |
| 🏷️ | **`runs-on`** | `ubuntu-latest` and friends | `self-hosted`, plus your own labels |

Cost details change. The [billing page](https://docs.github.com/en/billing/concepts/product-billing/github-actions) is the source of truth.

---

<p align="center">
  <a href="03-self-hosted-runners.md">⬅️ Self-hosted runners</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="05-two-myths.md"><b>Next: Two myths ➡️</b></a>
</p>
