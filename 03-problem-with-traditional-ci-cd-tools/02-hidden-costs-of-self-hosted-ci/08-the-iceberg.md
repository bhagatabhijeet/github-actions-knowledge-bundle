---
type: Tutorial
title: "The Hidden Costs of Running Your Own CI Server: The iceberg"
description: "Most of these tools are free to download. That is the part above the water."
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
  <a href="README.md">📂 <b>The Hidden Costs of Running Your Own CI Server</b></a> &nbsp;·&nbsp; Lesson 2 · Part 8 of 10 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# 🧊 The iceberg

Most of these tools are free to download. That is the part above the water.

| 🌊 Above the waterline | 🧊 Below the waterline |
|---|---|
| Licence: free | Machines running around the clock |
| | Hours spent patching and upgrading |
| | Builds lost to outages |
| | Developers waiting in queues |
| | A specialist, or a developer acting as one |
| | The risk of an unpatched server holding production keys |

> [!IMPORTANT]
> **A free licence is not a free tool.** The real price of a self-hosted CI server is paid in engineering time.

---

<p align="center">
  <a href="07-6-the-knowledge-lives-in-one-head.md">⬅️ 6️⃣ The knowledge lives in one head</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="09-to-be-fair.md"><b>Next: To be fair ➡️</b></a>
</p>
