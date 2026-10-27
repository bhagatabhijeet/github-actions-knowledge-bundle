---
type: Tutorial
title: "How GitHub Actions Answers the Problem: Plugins vs actions"
description: "This one deserves a closer look, because actions and plugins sound like the same idea."
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
  <a href="README.md">📂 <b>How GitHub Actions Answers the Problem</b></a> &nbsp;·&nbsp; Lesson 3 · Part 4 of 11 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# 🧩 Plugins vs actions

This one deserves a closer look, because actions and plugins sound like the same idea.

| | 🧩 Server plugin | ⚡ Action |
|---|---|---|
| **Installed** | Once, into the server, by an admin | Never. You reference it in a step |
| **Scope** | Every pipeline on the server | Only the workflow that names it |
| **Version** | One version for everybody | Each workflow picks its own |
| **Upgrading** | Can break other teams' pipelines | Affects only the file you edit |
| **Runs** | Inside the CI server | On the throwaway runner |

```yaml
steps:
  - uses: actions/checkout@v7        # this workflow's choice
  - uses: actions/setup-python@v7    # change it here, nothing else moves
```

The upgrade trap from Lesson 2 can't happen. There is no server to upgrade, and bumping an action in one workflow leaves every other workflow untouched.

---

<p align="center">
  <a href="03-six-pains-six-answers.md">⬅️ Six pains, six answers</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="05-same-pipeline-two-worlds.md"><b>Next: Same pipeline, two worlds ➡️</b></a>
</p>
