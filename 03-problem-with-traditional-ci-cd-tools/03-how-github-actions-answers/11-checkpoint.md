---
type: Tutorial
title: "How GitHub Actions Answers the Problem: Checkpoint"
description: "In everything that must exist before the file runs. The Jenkinsfile needs a server, a prepared agent, plugins, a webhook and a credential. The workflow needs only to be committed."
tags: [github-actions, ci-cd, hosted-runners, self-hosted-runners, jenkins, comparison, migration]
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
  - id: gh-migrate-jenkins
    resource: https://docs.github.com/en/actions/tutorials/migrate-to-github-actions/manual-migrations/migrate-from-jenkins
    title: Migrating from Jenkins to GitHub Actions
  - id: gh-secure-use
    resource: https://docs.github.com/en/actions/reference/security/secure-use
    title: Secure use reference
  - id: gh-billing
    resource: https://docs.github.com/en/billing/concepts/product-billing/github-actions
    title: GitHub Actions billing
---

<p align="center">
  <a href="README.md">📂 <b>How GitHub Actions Answers the Problem</b></a> &nbsp;·&nbsp; Lesson 3 · Part 11 of 11 &nbsp;·&nbsp; ⏱️ 2 min
</p>

# ✅ Checkpoint

<details>
<summary><b>The Jenkinsfile and the workflow were about the same length. So where is the saving?</b></summary>

<br>

In everything that must exist before the file runs. The Jenkinsfile needs a server, a prepared agent, plugins, a webhook and a credential. The workflow needs only to be committed.

</details>

<details>
<summary><b>Why can't upgrading an action break another team's pipeline the way upgrading a plugin can?</b></summary>

<br>

A plugin is installed once for the whole server. An action is referenced, with its version, inside a single workflow file. Changing it there changes nothing anywhere else.

</details>

<details>
<summary><b>Name two things that are still your responsibility on GitHub Actions.</b></summary>

<br>

Any two of: writing and maintaining workflows, keeping action versions current, managing secrets, vetting third-party actions, and watching minute usage on private repositories.

</details>

<details>
<summary><b>Your tests must talk to a database inside the company network. What are you likely to need?</b></summary>

<br>

A self-hosted runner inside that network, or another way of giving hosted runners access. Standard GitHub-hosted runners can't reach private systems on their own.

</details>

---

<p align="center">
  <a href="10-already-on-a-traditional-tool.md">⬅️ Already on a traditional tool?</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md#-what-you-learned"><b>Wrap up: What you learned ➡️</b></a>
</p>
