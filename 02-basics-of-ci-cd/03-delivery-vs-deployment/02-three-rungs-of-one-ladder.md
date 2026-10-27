---
type: Tutorial
title: "Continuous Delivery vs Continuous Deployment: Three rungs of one ladder"
description: "Each practice builds on the one below it. You can't skip a rung."
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
  <a href="README.md">📂 <b>Continuous Delivery vs Continuous Deployment</b></a> &nbsp;·&nbsp; Lesson 3 · Part 2 of 7 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# 🪜 Three rungs of one ladder

Each practice builds on the one below it. You can't skip a rung.

```mermaid
flowchart BT
    CI["🧪 <b>Continuous Integration</b><br/>every change is built and tested"]:::blue
    CDE["🚚 <b>Continuous Delivery</b><br/>every change is ready to release"]:::orange
    CDP["🚀 <b>Continuous Deployment</b><br/>every change is released"]:::green
    CI --> CDE --> CDP

    classDef blue fill:#0c1d3a,stroke:#58a6ff,color:#fff,stroke-width:2px
    classDef orange fill:#3d1d00,stroke:#ffa657,color:#fff,stroke-width:2px
    classDef green fill:#0f2d17,stroke:#3fb950,color:#fff,stroke-width:2px
```

> [!NOTE]
> Continuous deployment isn't "better" than continuous delivery. It's a choice. Many excellent teams deliberately stop at delivery because a regulator, an app store, or a marketing calendar decides when releases happen.

---

<p align="center">
  <a href="01-the-difference-in-one-picture.md">⬅️ The difference in one picture</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="03-environments-the-rehearsal-stages.md"><b>Next: Environments: the rehearsal stages ➡️</b></a>
</p>
