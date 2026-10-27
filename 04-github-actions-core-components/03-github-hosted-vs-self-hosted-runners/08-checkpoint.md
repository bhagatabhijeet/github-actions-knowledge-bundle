---
type: Tutorial
title: "GitHub-Hosted vs Self-Hosted Runners: Checkpoint"
description: "runs-on. A GitHub label such as ubuntu-latest requests a hosted runner. self-hosted, or a label you defined, sends the job to your own machine."
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
  <a href="README.md">📂 <b>GitHub-Hosted vs Self-Hosted Runners</b></a> &nbsp;·&nbsp; Lesson 3 · Part 8 of 8 &nbsp;·&nbsp; ⏱️ 2 min
</p>

# ✅ Checkpoint

<details>
<summary><b>Which line of a workflow decides between a hosted and a self-hosted runner?</b></summary>

<br>

`runs-on`. A GitHub label such as `ubuntu-latest` requests a hosted runner. `self-hosted`, or a label you defined, sends the job to your own machine.

</details>

<details>
<summary><b>Your job needs a tool that isn't preinstalled on <code>ubuntu-latest</code>. Do you need a self-hosted runner?</b></summary>

<br>

No. Add a step that installs it. You only need a self-hosted runner for things a step can't provide: private network access, special hardware, or very long jobs.

</details>

<details>
<summary><b>What is the main risk of a runner that keeps its state between jobs?</b></summary>

<br>

Leftovers. Files, caches or processes from an earlier job can change the result of a later one, so builds stop being repeatable. On a public repository it is also a security risk.

</details>

---

<p align="center">
  <a href="07-which-should-you-choose.md">⬅️ Which should you choose?</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md#-what-you-learned"><b>Wrap up: What you learned ➡️</b></a>
</p>
