---
type: Tutorial
title: "How GitHub Actions Answers the Problem: Six pains, six answers"
description: "And the day-two pains from Lesson 2:"
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
  <a href="README.md">📂 <b>How GitHub Actions Answers the Problem</b></a> &nbsp;·&nbsp; Lesson 3 · Part 3 of 11 &nbsp;·&nbsp; ⏱️ 2 min
</p>

# ✅ Six pains, six answers

And the day-two pains from [Lesson 2](../02-hidden-costs-of-self-hosted-ci/README.md):

| | Pain | GitHub Actions gives you | Meet it in |
|---|---|---|---|
| 1️⃣ | Server upkeep | No server. GitHub runs the service and maintains the runner images | [1.1](../../01-introduction-to-github-actions/01-what-is-github-actions/README.md) |
| 2️⃣ | Snowflake agents | A **fresh virtual machine per job**, thrown away afterwards. Tool versions are declared in the workflow | [2.5](../../02-basics-of-ci-cd/05-your-first-ci-pipeline/README.md) |
| 3️⃣ | Queues and idle cost | Each job gets its own **GitHub-hosted runner**, billed **per minute**. Free on public repositories with standard runners | [1.2](../../01-introduction-to-github-actions/02-core-concepts/README.md) |
| 4️⃣ | Fragile plugins | **Actions** are chosen per workflow and per version, not installed server-wide | [1.3](../../01-introduction-to-github-actions/03-anatomy-of-a-workflow/README.md) |
| 5️⃣ | Integration glue | Code and CI live in the same place. No webhook, no clone token, no second set of accounts | [1.1](../../01-introduction-to-github-actions/01-what-is-github-actions/05-where-it-lives.md) |
| 6️⃣ | Knowledge in one head | Workflows are **YAML files in `.github/workflows/`**, reviewed in pull requests | [1.3](../../01-introduction-to-github-actions/03-anatomy-of-a-workflow/README.md) |

---

<p align="center">
  <a href="02-abhijeet-s-install-list-revisited.md">⬅️ Abhijeet's install list, revisited</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="04-plugins-vs-actions.md"><b>Next: Plugins vs actions ➡️</b></a>
</p>
