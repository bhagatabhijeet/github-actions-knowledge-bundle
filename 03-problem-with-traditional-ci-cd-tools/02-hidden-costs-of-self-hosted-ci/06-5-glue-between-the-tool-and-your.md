---
type: Tutorial
title: "The Hidden Costs of Running Your Own CI Server: 5️⃣ Glue between the tool and your code"
description: "Your code is in one system and your CI server is in another. Connecting them is your job:"
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
  <a href="README.md">📂 <b>The Hidden Costs of Running Your Own CI Server</b></a> &nbsp;·&nbsp; Lesson 2 · Part 6 of 10 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# 5️⃣ Glue between the tool and your code

Your code is in one system and your CI server is in another. Connecting them is your job:

- A **webhook** so the code host can tell the server about pushes
- A **network path** so that webhook can reach a server inside your firewall
- An **access token** so the server can clone the repository
- Another integration so the result shows up as a ✅ or ❌ on the pull request
- A second set of **user accounts and permissions** to keep in step with the first

None of it is hard. All of it breaks silently when a token expires or an address changes, and developers find out when their pull request shows no status at all.

---

<p align="center">
  <a href="05-4-plugins-the-superpower-and-the-weak.md">⬅️ 4️⃣ Plugins: the superpower and the weak point</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="07-6-the-knowledge-lives-in-one-head.md"><b>Next: 6️⃣ The knowledge lives in one head ➡️</b></a>
</p>
