---
type: Tutorial
title: "The Problem Statement: His four-step plan"
description: "Abhijeet's four-step pipeline plan that answers every problem he found in the project's build history."
tags: [ci-cd, problem-statement, devops, self-hosted, jenkins, beginner]
status: stable
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-26T00:00:00Z }
sources:
  - id: jenkins-install
    resource: https://www.jenkins.io/doc/book/installing/
    title: Installing Jenkins (Jenkins User Handbook)
  - id: jenkins-scale
    resource: https://www.jenkins.io/doc/book/scaling/architecting-for-scale/
    title: Architecting for Scale (Jenkins User Handbook)
  - id: gh-understand
    resource: https://docs.github.com/en/actions/get-started/understand-github-actions
    title: Understanding GitHub Actions
---

<p align="center">
  <a href="README.md">📂 <b>The Problem Statement</b></a> &nbsp;·&nbsp; Lesson 1 · Part 3 of 9 &nbsp;·&nbsp; ⏱️ 2 min
</p>

# 🗺️ His four-step plan

Abhijeet writes down a plan that addresses every finding:

```mermaid
flowchart LR
    A["1️⃣ GitHub<br/>version control<br/>and collaboration"]:::blue --> B["2️⃣ Unit tests<br/>and code coverage"]:::purple
    B --> C["3️⃣ Docker build and push,<br/>deploy to Kubernetes"]:::orange
    C --> D["4️⃣ Automated<br/>integration tests"]:::green

    classDef blue fill:#0c1d3a,stroke:#58a6ff,color:#fff,stroke-width:2px
    classDef purple fill:#22123f,stroke:#bc8cff,color:#fff,stroke-width:2px
    classDef orange fill:#3d1d00,stroke:#ffa657,color:#fff,stroke-width:2px
    classDef green fill:#0f2d17,stroke:#3fb950,color:#fff,stroke-width:2px
```

| | Step | Fixes |
|---|---|---|
| 1️⃣ | **GitHub** for version control and collaboration | Hand-merged code, isolated developers |
| 2️⃣ | **Unit tests and code coverage** on every change | Slow manual testing, bugs found late |
| 3️⃣ | **Docker build and push**, then **deploy to Kubernetes** | Manual, inconsistent deployments |
| 4️⃣ | **Automated integration tests** as the final gate | Risky releases |

It's a good plan. It leaves one question open.

---

<p align="center">
  <a href="02-what-abhijeet-found.md">⬅️ What Abhijeet found</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="04-which-tool-will-run-all-this.md"><b>Next: Which tool will run all this? ➡️</b></a>
</p>
