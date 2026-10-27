---
type: Tutorial
title: "Continuous Delivery vs Continuous Deployment: Which one should you choose?"
description: "Which one should you choose?, part 6 of 7 of Continuous Delivery vs Continuous Deployment."
tags: [ci-cd, continuous-delivery, continuous-deployment, environments, approvals]
status: stable
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-07T00:00:00Z }
sources:
  - id: fowler-cd
    resource: https://martinfowler.com/bliki/ContinuousDelivery.html
    title: Continuous Delivery
    author: Martin Fowler
  - id: gh-cd
    resource: https://docs.github.com/en/actions/get-started/continuous-deployment
    title: Continuous deployment (GitHub Docs)
  - id: gh-environments
    resource: https://docs.github.com/en/actions/how-tos/deploy/configure-and-manage-deployments/manage-environments
    title: Managing environments for deployment
---

<p align="center">
  <a href="README.md">📂 <b>Continuous Delivery vs Continuous Deployment</b></a> &nbsp;·&nbsp; Lesson 3 · Part 6 of 7 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# 🧭 Which one should you choose?

```mermaid
flowchart TD
    Q1{Can you deploy with<br/>one command or click?}:::yellow
    Q1 -- No --> A1[🔧 Automate the deploy first]:::red
    Q1 -- Yes --> Q2{Do you trust your tests<br/>to catch real problems?}:::yellow
    Q2 -- Not yet --> A2[🚚 Continuous Delivery<br/>keep the approval]:::orange
    Q2 -- Yes --> Q3{Does something outside the team<br/>control release timing?}:::yellow
    Q3 -- Yes --> A2
    Q3 -- No --> A3[🚀 Continuous Deployment]:::green

    classDef yellow fill:#3d2a00,stroke:#e3b341,color:#fff,stroke-width:2px
    classDef red fill:#4a0d0d,stroke:#f85149,color:#fff,stroke-width:2px
    classDef orange fill:#3d1d00,stroke:#ffa657,color:#fff,stroke-width:2px
    classDef green fill:#0f2d17,stroke:#3fb950,color:#fff,stroke-width:2px
```

---

<p align="center">
  <a href="05-deploying-without-fear.md">⬅️ Deploying without fear</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="07-checkpoint.md"><b>Next: Checkpoint ➡️</b></a>
</p>
