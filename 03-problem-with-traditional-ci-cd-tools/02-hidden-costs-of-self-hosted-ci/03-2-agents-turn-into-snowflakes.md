---
type: Tutorial
title: "The Hidden Costs of Running Your Own CI Server: 2️⃣ Agents turn into snowflakes"
description: "A build agent is usually a long-lived machine. Somebody installed Java on it in March, Node in June, and a newer Node in September \"just for one project\". This is task 4 on Abhijeet's list, several Node.js versions side..."
tags: [ci-cd, self-hosted, jenkins, plugins, build-agents, maintenance]
status: stable
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-26T00:00:00Z }
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
  - id: gh-hosted-runners
    resource: https://docs.github.com/en/actions/concepts/runners/github-hosted-runners
    title: GitHub-hosted runners
---

<p align="center">
  <a href="README.md">📂 <b>The Hidden Costs of Running Your Own CI Server</b></a> &nbsp;·&nbsp; Lesson 2 · Part 3 of 10 &nbsp;·&nbsp; ⏱️ 2 min
</p>

# 2️⃣ Agents turn into snowflakes

A build agent is usually a long-lived machine. Somebody installed Java on it in March, Node in June, and a newer Node in September "just for one project". This is task 4 on Abhijeet's list, several Node.js versions side by side, a year later.

Two problems follow.

**Tool drift.** Agent 1 has Python 3.11. Agent 2 has 3.13. Your build passes or fails depending on which agent picks it up.

**Leftovers.** When a build finishes, the machine is not wiped. Old files, cached packages, a stray background process and a half-written config file are all still there for the next build to trip over.

| | Long-lived agent | What you actually want |
|---|---|---|
| Starting state | Whatever the last build left behind | Identical every time |
| Installed tools | Whatever someone added by hand | Declared in the pipeline |
| "Works on agent 2" | A real sentence people say | Impossible |

Each agent slowly becomes unique, a **snowflake**. Nobody can rebuild it from memory.

> [!NOTE]
> **📘 From the GitHub docs:** This is the pain GitHub-hosted runners remove. Each one is a new virtual machine, and GitHub refreshes the tools in its runner images weekly. Machine maintenance and upgrades are taken care of for you. ([GitHub-hosted runners](https://docs.github.com/en/actions/concepts/runners/github-hosted-runners))

---

<p align="center">
  <a href="02-1-you-own-a-server.md">⬅️ 1️⃣ You own a server</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="04-3-capacity-is-always-the-wrong-size.md"><b>Next: 3️⃣ Capacity is always the wrong size ➡️</b></a>
</p>
