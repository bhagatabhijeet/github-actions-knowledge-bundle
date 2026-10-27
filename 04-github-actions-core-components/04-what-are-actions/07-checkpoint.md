---
type: Tutorial
title: "What Are Actions?: Checkpoint"
description: "The owner is docker, the repository is login-action and the version is v3, a major tag."
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
  <a href="README.md">📂 <b>What Are Actions?</b></a> &nbsp;·&nbsp; Lesson 4 · Part 7 of 7 &nbsp;·&nbsp; ⏱️ 2 min
</p>

# ✅ Checkpoint

<details>
<summary><b>In <code>uses: docker/login-action@v3</code>, what are the owner, the repository and the version?</b></summary>

<br>

The owner is `docker`, the repository is `login-action` and the version is `v3`, a major tag.

</details>

<details>
<summary><b>You need a tool that only runs on Linux, packaged with its dependencies. Which kind of action fits?</b></summary>

<br>

A Docker container action. It brings its own environment, but it only runs on Linux runners.

</details>

<details>
<summary><b>Three of your workflows repeat the same five setup steps. What would you build?</b></summary>

<br>

A composite action in your repository, for example at `.github/actions/setup/action.yml`, called with `uses: ./.github/actions/setup`.

</details>

<details>
<summary><b>Why is <code>@main</code> a risky way to reference a third-party action?</b></summary>

<br>

Whatever is pushed to that branch runs in your workflow next time, with access to your token and secrets. You'd be trusting every future commit sight unseen.

</details>

---

<p align="center">
  <a href="06-pinning-which-version-should-you-use.md">⬅️ Pinning: which version should you use?</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md#-what-you-learned"><b>Wrap up: What you learned ➡️</b></a>
</p>
