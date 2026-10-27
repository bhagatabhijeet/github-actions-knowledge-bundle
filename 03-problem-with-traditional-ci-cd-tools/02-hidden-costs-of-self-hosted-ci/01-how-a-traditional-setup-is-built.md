---
type: Tutorial
title: "The Hidden Costs of Running Your Own CI Server: How a traditional setup is built"
description: "The CI server decides what should run. The agents do the running. Plugins extend the server. Your code lives somewhere else and pokes the server with a webhook when something changes."
tags: [ci-cd, self-hosted, jenkins, plugins, build-agents, maintenance]
status: stable
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-07T00:00:00Z }
sources:
  - id: jenkins-scale
    resource: https://www.jenkins.io/doc/book/scaling/architecting-for-scale/
    title: Architecting for Scale (Jenkins User Handbook)
  - id: jenkins-agents
    resource: https://www.jenkins.io/doc/book/using/using-agents/
    title: Using Jenkins agents
  - id: jenkins-plugins
    resource: https://www.jenkins.io/doc/book/managing/plugins/
    title: Managing Plugins (Jenkins User Handbook)
  - id: jenkins-advisories
    resource: https://www.jenkins.io/security/advisories/
    title: Jenkins Security Advisories
---

<p align="center">
  <a href="README.md">📂 <b>The Hidden Costs of Running Your Own CI Server</b></a> &nbsp;·&nbsp; Lesson 2 · Part 1 of 10 &nbsp;·&nbsp; ⏱️ 2 min
</p>

# 🏗️ How a traditional setup is built

```mermaid
flowchart LR
    G[(📁 Code host)]:::grey -- webhook --> C
    subgraph YOURS[" 🏢 Everything in this box is yours to run "]
        C[🧠 CI server]:::blue
        P[🧩 Plugins]:::purple
        A1[💪 Agent 1<br/>Linux]:::orange
        A2[💪 Agent 2<br/>Linux]:::orange
        A3[💪 Agent 3<br/>Windows]:::orange
        P -.- C
        C --> A1
        C --> A2
        C --> A3
    end

    classDef grey fill:#161b22,stroke:#8b949e,color:#fff,stroke-width:2px
    classDef blue fill:#0c1d3a,stroke:#58a6ff,color:#fff,stroke-width:2px
    classDef purple fill:#22123f,stroke:#bc8cff,color:#fff,stroke-width:2px
    classDef orange fill:#3d1d00,stroke:#ffa657,color:#fff,stroke-width:2px
```

The **CI server** decides what should run. The **agents** do the running. **Plugins** extend the server. Your code lives somewhere else and pokes the server with a **webhook** when something changes.

Now the six pains, one box at a time.

---

<p align="center">
  <a href="README.md">⬅️ Overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="02-1-you-own-a-server.md"><b>Next: 1️⃣ You own a server ➡️</b></a>
</p>
