---
type: Tutorial
title: "What Are Actions?: Where actions come from"
description: "The GitHub Marketplace lists tens of thousands of actions. A few you will meet almost everywhere:"
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
  <a href="README.md">📂 <b>What Are Actions?</b></a> &nbsp;·&nbsp; Lesson 4 · Part 5 of 7 &nbsp;·&nbsp; ⏱️ 2 min
</p>

# 🛒 Where actions come from

| | Source | How you write it | Example |
|---|---|---|---|
| 🏪 | **GitHub Marketplace**, a public repository | `owner/repo@version` | `actions/checkout@v7` |
| 📁 | **A subfolder** of a public repository | `owner/repo/path@version` | `github/codeql-action/init@v4` |
| 🏠 | **Your own repository** | `./path/to/action` | `./.github/actions/greet` |
| 🐳 | **A Docker image** on a registry | `docker://image:tag` | `docker://alpine:3.20` |

The [GitHub Marketplace](https://github.com/marketplace?type=actions) lists tens of thousands of actions. A few you will meet almost everywhere:

| Action | What it does |
|---|---|
| `actions/checkout` | Copies your repository onto the runner |
| `actions/setup-node`, `setup-python`, `setup-java`, `setup-go` | Installs a language at the version you ask for |
| `actions/cache` | Saves dependencies between runs, so builds get faster |
| `actions/upload-artifact`, `download-artifact` | Keeps files after the runner is destroyed |
| `docker/build-push-action` | Builds and pushes a container image |
| `aws-actions/configure-aws-credentials`, `azure/login`, `google-github-actions/auth` | Signs in to a cloud |

> [!TIP]
> A ✅ **verified creator** badge on the Marketplace means GitHub has confirmed who the publisher is. It is a signal of identity, not a code review.

---

<p align="center">
  <a href="04-the-three-kinds-of-action.md">⬅️ The three kinds of action</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="06-pinning-which-version-should-you-use.md"><b>Next: Pinning: which version should you use? ➡️</b></a>
</p>
