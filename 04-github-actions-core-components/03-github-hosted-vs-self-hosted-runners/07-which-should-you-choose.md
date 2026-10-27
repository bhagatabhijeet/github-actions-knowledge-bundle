---
type: Tutorial
title: "GitHub-Hosted vs Self-Hosted Runners: Which should you choose?"
description: "Start hosted. Nearly every project can. Move a job to a self-hosted runner only when you can name the specific thing it needs. You can also mix them: most jobs hosted, one deploy job self-hosted."
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
  <a href="README.md">📂 <b>GitHub-Hosted vs Self-Hosted Runners</b></a> &nbsp;·&nbsp; Lesson 3 · Part 7 of 8 &nbsp;·&nbsp; ⏱️ 2 min
</p>

# 🧭 Which should you choose?

```mermaid
flowchart TD
    Q1{Do jobs need something<br/>a hosted runner can't offer?}:::yellow
    Q1 -- No --> A1[☁️ GitHub-hosted]:::green
    Q1 -- Yes --> Q2{What do they need?}:::yellow
    Q2 -- More CPU or memory --> A2[☁️ A larger<br/>GitHub-hosted runner]:::green
    Q2 -- Private network access --> A3[🏢 Self-hosted]:::orange
    Q2 -- GPU or special hardware --> A3
    Q2 -- Jobs over 6 hours --> A3

    classDef yellow fill:#3d2a00,stroke:#e3b341,color:#fff,stroke-width:2px
    classDef green fill:#0f2d17,stroke:#3fb950,color:#fff,stroke-width:2px
    classDef orange fill:#3d1d00,stroke:#ffa657,color:#fff,stroke-width:2px
```

> [!TIP]
> **Start hosted.** Nearly every project can. Move a job to a self-hosted runner only when you can name the specific thing it needs. You can also mix them: most jobs hosted, one deploy job self-hosted.

Everything in this guide uses GitHub-hosted runners, so there is nothing for you to set up.

---

<p align="center">
  <a href="06-one-security-rule.md">⬅️ One security rule</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="08-checkpoint.md"><b>Next: Checkpoint ➡️</b></a>
</p>
