---
type: Tutorial
title: "The Hidden Costs of Running Your Own CI Server: 4️⃣ Plugins: the superpower and the weak point"
description: "Traditional CI servers do very little on their own. Talking to Git is a plugin. Storing credentials is a plugin. Sending a Slack message is a plugin. Jenkins has well over a thousand of them, written by many different..."
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
  <a href="README.md">📂 <b>The Hidden Costs of Running Your Own CI Server</b></a> &nbsp;·&nbsp; Lesson 2 · Part 5 of 10 &nbsp;·&nbsp; ⏱️ 2 min
</p>

# 4️⃣ Plugins: the superpower and the weak point

Traditional CI servers do very little on their own. Talking to Git is a plugin. Storing credentials is a plugin. Sending a Slack message is a plugin. Jenkins has well over a thousand of them, written by many different volunteers and vendors.

That openness is why these tools can do almost anything. It is also where a lot of the fragility comes from.

```mermaid
flowchart TD
    U[⬆️ Upgrade the CI server]:::blue --> Q{Do all your plugins<br/>support the new version?}:::yellow
    Q -- Yes --> OK[✅ Carry on]:::green
    Q -- No --> X{Is the broken plugin<br/>still maintained?}:::yellow
    X -- Yes --> W[⏳ Wait for a fix,<br/>stay unpatched meanwhile]:::orange
    X -- No --> R[🔨 Replace it and<br/>rewrite your pipelines]:::red

    classDef blue fill:#0c1d3a,stroke:#58a6ff,color:#fff,stroke-width:2px
    classDef yellow fill:#3d2a00,stroke:#e3b341,color:#fff,stroke-width:2px
    classDef green fill:#0f2d17,stroke:#3fb950,color:#fff,stroke-width:2px
    classDef orange fill:#3d1d00,stroke:#ffa657,color:#fff,stroke-width:2px
    classDef red fill:#4a0d0d,stroke:#f85149,color:#fff,stroke-width:2px
```

| | Plugin problem | Why it bites |
|---|---|---|
| 🕸️ | **Dependency chains** | Plugins depend on other plugins. Updating one can force updates to five |
| 🌍 | **Server-wide scope** | A plugin is installed once for everyone. One team's upgrade can break another team's pipeline |
| 🛡️ | **Security advisories** | Plugins run inside the server, so a flaw in one is a flaw in the server |
| 🪦 | **Abandonment** | Volunteer maintainers move on. The plugin stays in your pipeline |

---

<p align="center">
  <a href="04-3-capacity-is-always-the-wrong-size.md">⬅️ 3️⃣ Capacity is always the wrong size</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="06-5-glue-between-the-tool-and-your.md"><b>Next: 5️⃣ Glue between the tool and your code ➡️</b></a>
</p>
