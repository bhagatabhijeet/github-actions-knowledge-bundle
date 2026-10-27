---
type: Tutorial
title: "How GitHub Actions Answers the Problem: The middle path: self-hosted runners"
description: "GitHub Actions also lets you bring your own machines, called self-hosted runners. GitHub still does the scheduling, the UI and the logs. Your machine does the running."
tags: [github-actions, ci-cd, hosted-runners, self-hosted-runners, jenkins, comparison, migration]
status: stable
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-26T00:00:00Z }
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
  - id: gh-limits
    resource: https://docs.github.com/en/actions/reference/limits
    title: Actions limits
---

<p align="center">
  <a href="README.md">📂 <b>How GitHub Actions Answers the Problem</b></a> &nbsp;·&nbsp; Lesson 3 · Part 8 of 11 &nbsp;·&nbsp; ⏱️ 3 min
</p>

# 🌉 The middle path: self-hosted runners

GitHub Actions also lets you bring your own machines, called **self-hosted runners**. GitHub still does the scheduling, the UI and the logs. Your machine does the running.

```mermaid
flowchart LR
    W[📜 Workflow]:::blue --> Q{runs-on}:::yellow
    Q -- ubuntu-latest --> H[☁️ GitHub-hosted runner<br/>fresh VM, nothing to maintain]:::green
    Q -- self-hosted --> S[🏢 Your machine<br/>your network, your upkeep]:::orange

    classDef blue fill:#0c1d3a,stroke:#58a6ff,color:#fff,stroke-width:2px
    classDef yellow fill:#3d2a00,stroke:#e3b341,color:#fff,stroke-width:2px
    classDef green fill:#0f2d17,stroke:#3fb950,color:#fff,stroke-width:2px
    classDef orange fill:#3d1d00,stroke:#ffa657,color:#fff,stroke-width:2px
```

They solve the private-network and special-hardware problems. They also bring back pains 1 to 3 from Lesson 2 for those machines: you patch them, you keep them clean and you decide how many to run.

> [!TIP]
> Start with GitHub-hosted runners. Reach for self-hosted ones only when you hit a specific wall, such as needing a GPU or access to an internal system.

### 📘 What the GitHub docs say about self-hosted runners

| | Fact | What it means for you |
|---|---|---|
| 💰 | Free to use with GitHub Actions | You still pay for the machines and their upkeep |
| 🔧 | Only the runner application updates itself | The OS and every other tool are yours to patch |
| 🧹 | No clean instance per job | Leftovers from one job can affect the next |
| ⏱️ | Jobs can run for up to 5 days | Instead of 6 hours on GitHub-hosted runners |

> [!WARNING]
> GitHub says self-hosted runners "should almost never be used for public repositories". Anyone can open a pull request, and that pull request's code would run on your machine. ([Secure use reference](https://docs.github.com/en/actions/reference/security/secure-use))

Sources: [Self-hosted runners](https://docs.github.com/en/actions/concepts/runners/self-hosted-runners) · [Actions limits](https://docs.github.com/en/actions/reference/limits)

---

<p align="center">
  <a href="07-the-honest-trade-offs.md">⬅️ The honest trade-offs</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="09-so-which-should-you-use.md"><b>Next: So which should you use? ➡️</b></a>
</p>
