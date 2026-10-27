---
type: Tutorial
title: "Continuous Delivery vs Continuous Deployment: Build once, deploy many"
description: "One rule separates trustworthy pipelines from hopeful ones:"
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
  <a href="README.md">📂 <b>Continuous Delivery vs Continuous Deployment</b></a> &nbsp;·&nbsp; Lesson 3 · Part 4 of 7 &nbsp;·&nbsp; ⏱️ 2 min
</p>

# 📦 Build once, deploy many

One rule separates trustworthy pipelines from hopeful ones:

> [!IMPORTANT]
> **Build the artifact once. Deploy that exact same artifact to every environment.**

An **artifact** is the packaged output of your build: a zip, a container image, a compiled binary.

```mermaid
flowchart LR
    B[🏗️ Build once]:::blue --> A[(📦 Artifact<br/>v1.4.2)]:::pink
    A --> S[🎭 Staging]:::orange
    A --> P[🌍 Production]:::green

    classDef blue fill:#0c1d3a,stroke:#58a6ff,color:#fff,stroke-width:2px
    classDef pink fill:#3a0f2b,stroke:#f778ba,color:#fff,stroke-width:2px
    classDef orange fill:#3d1d00,stroke:#ffa657,color:#fff,stroke-width:2px
    classDef green fill:#0f2d17,stroke:#3fb950,color:#fff,stroke-width:2px
```

If you rebuild for production, you are shipping something that was **never tested**. A dependency may have released a new version in between. Staging proved nothing.

Differences between environments (database URLs, API keys) belong in **configuration**, supplied at deploy time, never baked into the build.

---

<p align="center">
  <a href="03-environments-the-rehearsal-stages.md">⬅️ Environments: the rehearsal stages</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="05-deploying-without-fear.md"><b>Next: Deploying without fear ➡️</b></a>
</p>
