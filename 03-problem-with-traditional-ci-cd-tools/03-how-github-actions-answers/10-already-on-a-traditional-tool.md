---
type: Tutorial
title: "How GitHub Actions Answers the Problem: Already on a traditional tool?"
description: "You don't have to move everything at once. Most teams start new projects on GitHub Actions and migrate old pipelines one at a time. GitHub publishes a migration guide for Jenkins that maps each concept across:"
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
  <a href="README.md">📂 <b>How GitHub Actions Answers the Problem</b></a> &nbsp;·&nbsp; Lesson 3 · Part 10 of 11 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# 🚚 Already on a traditional tool?

You don't have to move everything at once. Most teams start new projects on GitHub Actions and migrate old pipelines one at a time. GitHub publishes a [migration guide for Jenkins](https://docs.github.com/en/actions/tutorials/migrate-to-github-actions/manual-migrations/migrate-from-jenkins) that maps each concept across:

| Jenkins | GitHub Actions |
|---|---|
| `Jenkinsfile` | Workflow file in `.github/workflows/` |
| `agent` | `runs-on` |
| `stage` | Job |
| `steps` | `steps` |
| Plugin | Action |
| Credentials | Secrets |

---

<p align="center">
  <a href="09-so-which-should-you-use.md">⬅️ So which should you use?</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="11-checkpoint.md"><b>Next: Checkpoint ➡️</b></a>
</p>
