---
type: Tutorial
title: "GitHub-Hosted vs Self-Hosted Runners: The difference in one picture"
description: "In the workflow file, the whole decision is one line:"
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
  <a href="README.md">📂 <b>GitHub-Hosted vs Self-Hosted Runners</b></a> &nbsp;·&nbsp; Lesson 3 · Part 1 of 8 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# 🎯 The difference in one picture

<p align="center">
  <img src="../../assets/images/hosted-vs-self-hosted.svg" alt="GitHub-hosted runners are maintained by GitHub, give a clean VM per job and run in the public cloud. Self-hosted runners are maintained by you, keep their state between jobs and run inside your network" width="100%">
</p>

In the workflow file, the whole decision is one line:

```yaml
runs-on: ubuntu-latest     # GitHub-hosted
```

```yaml
runs-on: self-hosted       # a machine you registered
```

Everything else about the workflow stays the same.

---

<p align="center">
  <a href="README.md">⬅️ Overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="02-github-hosted-runners.md"><b>Next: GitHub-hosted runners ➡️</b></a>
</p>
