---
type: Tutorial
title: "The Hidden Costs of Running Your Own CI Server: 1️⃣ You own a server"
description: "The CI server is an application like any other. It needs everything a production application needs:"
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
  <a href="README.md">📂 <b>The Hidden Costs of Running Your Own CI Server</b></a> &nbsp;·&nbsp; Lesson 2 · Part 2 of 10 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# 1️⃣ You own a server

The CI server is an application like any other. It needs everything a production application needs:

| | Chore | What happens if you skip it |
|---|---|---|
| 🩹 | Operating system patches | Known vulnerabilities on a machine that holds your deploy keys |
| ⬆️ | CI server upgrades | You fall behind on security fixes |
| 💾 | Backups | One dead disk erases every pipeline and its history |
| 📈 | Monitoring disk, memory, CPU | The disk fills up on Saturday and nobody notices until Monday |
| 🔐 | User accounts, TLS certificates | An expired certificate stops all builds at once |

> [!WARNING]
> A CI server is one of the most valuable targets in a company. It can read your source code and it holds the credentials that deploy to production. "We'll patch it later" is a risky sentence.

---

<p align="center">
  <a href="01-how-a-traditional-setup-is-built.md">⬅️ How a traditional setup is built</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="03-2-agents-turn-into-snowflakes.md"><b>Next: 2️⃣ Agents turn into snowflakes ➡️</b></a>
</p>
