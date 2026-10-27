---
type: Tutorial
title: "How GitHub Actions Answers the Problem: What is still your job"
description: "GitHub Actions doesn't remove responsibility. It moves the line."
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
  <a href="README.md">📂 <b>How GitHub Actions Answers the Problem</b></a> &nbsp;·&nbsp; Lesson 3 · Part 6 of 11 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# 🧾 What is still your job

GitHub Actions doesn't remove responsibility. It moves the line.

| | Still yours | Why |
|---|---|---|
| 📜 | Writing and maintaining workflows | That's the pipeline definition: the layer you kept |
| ⬆️ | Keeping action versions current | Old versions stop getting fixes |
| 🔑 | Managing secrets | Deploy credentials are as sensitive as ever |
| 🛡️ | Vetting third-party actions | An action is someone else's code running with access to your repository |
| 💰 | Watching minutes on private repositories | Pay-per-use means a wasteful pipeline costs money |

> [!WARNING]
> Actions from the Marketplace are written by many different authors, just like plugins. Prefer well-maintained ones, read what they do, and for anything sensitive pin the action to a full commit SHA so the code can't change underneath you.

---

<p align="center">
  <a href="05-same-pipeline-two-worlds.md">⬅️ Same pipeline, two worlds</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="07-the-honest-trade-offs.md"><b>Next: The honest trade-offs ➡️</b></a>
</p>
