---
type: Tutorial
title: "How GitHub Actions Answers the Problem: Abhijeet's install list, revisited"
description: "Here are the seven tasks from Lesson 1, and what becomes of each."
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
  <a href="README.md">📂 <b>How GitHub Actions Answers the Problem</b></a> &nbsp;·&nbsp; Lesson 3 · Part 2 of 11 &nbsp;·&nbsp; ⏱️ 3 min
</p>

# 🧾 Abhijeet's install list, revisited

Here are the seven tasks from [Lesson 1](../01-the-problem-statement/README.md), and what becomes of each.

| | With a self-hosted CI server | With GitHub Actions |
|---|---|---|
| 1 | Provision and maintain a virtual machine | `runs-on: ubuntu-latest`. GitHub provides the machine |
| 2 | Install Java, firewall rules, CI plugins | Nothing. There is no server |
| 3 | Install Node.js and npm | `actions/setup-node` picks the version in one step |
| 4 | Keep several Node.js versions side by side | A **matrix**: each version gets its own clean machine |
| 5 | Install Docker | Already on the Ubuntu runner |
| 6 | Install kubectl and Helm | Already on the Ubuntu runner |
| 7 | Install CLIs for test and reporting tools | An action or an install step, in the workflow that needs it |

Task 4, the one that causes version conflicts on a shared machine, becomes a few lines of YAML:

```yaml
jobs:
  unit-testing:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        node-version: [20, 22, 24]
    steps:
      - uses: actions/checkout@v7
      - uses: actions/setup-node@v7
        with:
          node-version: ${{ matrix.node-version }}
      - run: npm ci
      - run: npm test
```

Three versions, three separate machines, running at the same time. They can't conflict because they never share a disk.

The "and it grows" list shrinks the same way:

| | Later need | On a GitHub-hosted Ubuntu runner |
|---|---|---|
| ☕ | Java and Maven | Preinstalled. `actions/setup-java` selects a specific version |
| 🐍 | Python | Preinstalled. `actions/setup-python` selects a specific version |
| ☁️ | AWS CLI and Azure CLI | Preinstalled |
| 🛡️ | Trivy, kubesec | Not preinstalled. Add an action or an install step where you need them |

> [!NOTE]
> The preinstalled list changes over time. The exact contents of every runner image are published in the [actions/runner-images](https://github.com/actions/runner-images) repository.

**Against his two criteria:**

| | Criterion | Verdict |
|---|---|---|
| 1️⃣ | Simple to set up, nothing to install | ✅ Commit a YAML file and it runs |
| 2️⃣ | Pipelines, not infrastructure or scale | ✅ GitHub provisions and scales the runners |

---

<p align="center">
  <a href="01-the-shift-in-one-picture.md">⬅️ The shift in one picture</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="03-six-pains-six-answers.md"><b>Next: Six pains, six answers ➡️</b></a>
</p>
