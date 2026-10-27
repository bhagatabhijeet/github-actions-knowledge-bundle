---
type: Tutorial
title: "The Hidden Costs of Running Your Own CI Server: 6️⃣ The knowledge lives in one head"
description: "Over time the setup becomes a collection of decisions made through an admin screen: which plugins, which versions, which agents carry which label, which credentials go where."
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
  <a href="README.md">📂 <b>The Hidden Costs of Running Your Own CI Server</b></a> &nbsp;·&nbsp; Lesson 2 · Part 7 of 10 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# 6️⃣ The knowledge lives in one head

Over time the setup becomes a collection of decisions made through an admin screen: which plugins, which versions, which agents carry which label, which credentials go where.

| | Question | Answer on many teams |
|---|---|---|
| ❓ | Why does agent 3 have that environment variable? | "Ask whoever set it up" |
| ❓ | Who changed the deploy job last week? | "Not sure, it isn't in Git" |
| ❓ | Could we rebuild this server from scratch? | "Please don't make us find out" |

> [!NOTE]
> Modern traditional tools can keep a lot in version control. Jenkins, for example, lets you write the pipeline as a `Jenkinsfile` in your repository. That helps with the pipeline itself. The server, its plugins, its agents and its credentials still live outside the repo.

---

<p align="center">
  <a href="06-5-glue-between-the-tool-and-your.md">⬅️ 5️⃣ Glue between the tool and your code</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="08-the-iceberg.md"><b>Next: The iceberg ➡️</b></a>
</p>
