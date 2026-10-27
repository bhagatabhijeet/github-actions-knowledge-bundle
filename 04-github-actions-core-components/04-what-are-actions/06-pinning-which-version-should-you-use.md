---
type: Tutorial
title: "What Are Actions?: Pinning: which version should you use?"
description: "An action is someone else's code running with your repository's token and secrets. The version you pin decides how much you trust them."
tags: [github-actions, actions, uses, marketplace, composite, docker, javascript, security]
status: stable
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-26T00:00:00Z }
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
  <a href="README.md">📂 <b>What Are Actions?</b></a> &nbsp;·&nbsp; Lesson 4 · Part 6 of 7 &nbsp;·&nbsp; ⏱️ 2 min
</p>

# 🔐 Pinning: which version should you use?

An action is **someone else's code running with your repository's token and secrets.** The version you pin decides how much you trust them.

| Pin | Example | Updates automatically? | Safety |
|---|---|---|---|
| Branch | `@main` | Every commit | 🔴 Anything can change, any time |
| Major tag | `@v7` | Bug fixes and features | 🟡 Convenient. Fine for trusted publishers |
| Exact tag | `@v7.0.1` | No, but tags can be moved | 🟡 Better, still not immutable |
| Full commit SHA | `@8e5e7e5ab8b370d6c329ec480221332ada57f0ab` | Never | 🟢 The only truly immutable choice |

> [!IMPORTANT]
> **Pin third-party actions to a full commit SHA**, with the version in a comment so humans can read it:
>
> ```yaml
> - uses: some-org/some-action@8e5e7e5ab8b370d6c329ec480221332ada57f0ab  # v2.3.1
> ```
>
> Then let **Dependabot** propose updates. Tags can be moved to point at new code; a SHA cannot. For GitHub's own `actions/*`, a major tag is a common, reasonable trade-off.

> [!NOTE]
> **📘 From the GitHub docs:** Before you pin a SHA, check it comes from the action's **own** repository, not a fork. A commit from a fork can look identical in your workflow file but contain different code. ([Secure use reference](https://docs.github.com/en/actions/reference/security/secure-use))

---

<p align="center">
  <a href="05-where-actions-come-from.md">⬅️ Where actions come from</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="07-checkpoint.md"><b>Next: Checkpoint ➡️</b></a>
</p>
