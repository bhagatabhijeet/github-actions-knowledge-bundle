---
type: Tutorial
title: "How GitHub Actions Answers the Problem: So which should you use?"
description: "A traditional tool is still a sound choice when you have a platform team, strict rules about where builds may run, or years of working pipelines that nobody needs to change."
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
  <a href="README.md">📂 <b>How GitHub Actions Answers the Problem</b></a> &nbsp;·&nbsp; Lesson 3 · Part 9 of 11 &nbsp;·&nbsp; ⏱️ 2 min
</p>

# 🧭 So which should you use?

```mermaid
flowchart TD
    Q1{Is your code on GitHub?}:::yellow
    Q1 -- No --> A1[🧰 Use the CI built into your code host,<br/>or a traditional tool]:::orange
    Q1 -- Yes --> Q2{Do builds need your private<br/>network or special hardware?}:::yellow
    Q2 -- No --> A2[☁️ GitHub Actions<br/>with hosted runners]:::green
    Q2 -- Yes --> Q3{Do you have people to<br/>look after build machines?}:::yellow
    Q3 -- Yes --> A3[🏢 GitHub Actions with<br/>self-hosted runners]:::blue
    Q3 -- No --> A4[🤔 Solve the access problem first,<br/>then use hosted runners]:::orange

    classDef yellow fill:#3d2a00,stroke:#e3b341,color:#fff,stroke-width:2px
    classDef green fill:#0f2d17,stroke:#3fb950,color:#fff,stroke-width:2px
    classDef blue fill:#0c1d3a,stroke:#58a6ff,color:#fff,stroke-width:2px
    classDef orange fill:#3d1d00,stroke:#ffa657,color:#fff,stroke-width:2px
```

A traditional tool is still a sound choice when you have a platform team, strict rules about where builds may run, or years of working pipelines that nobody needs to change.

---

<p align="center">
  <a href="08-the-middle-path-self-hosted-runners.md">⬅️ The middle path: self-hosted runners</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="10-already-on-a-traditional-tool.md"><b>Next: Already on a traditional tool? ➡️</b></a>
</p>
