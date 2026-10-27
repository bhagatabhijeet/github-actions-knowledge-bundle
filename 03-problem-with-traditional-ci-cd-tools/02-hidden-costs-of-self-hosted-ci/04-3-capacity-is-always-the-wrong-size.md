---
type: Tutorial
title: "The Hidden Costs of Running Your Own CI Server: 3️⃣ Capacity is always the wrong size"
description: "You have to decide how many agents to run in advance. Developers don't push code at an even pace."
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
  <a href="README.md">📂 <b>The Hidden Costs of Running Your Own CI Server</b></a> &nbsp;·&nbsp; Lesson 2 · Part 4 of 10 &nbsp;·&nbsp; ⏱️ 2 min
</p>

# 3️⃣ Capacity is always the wrong size

You have to decide how many agents to run **in advance**. Developers don't push code at an even pace.

| Time | Builds wanted | With 2 agents |
|---|:---:|---|
| 🌅 09:00 | 1 | 😴 One agent idle |
| ☀️ 11:00 | 3 | ⏳ One build waits |
| 🔥 16:30, before a release | 9 | ⏳⏳⏳ Seven builds wait |
| 🌙 02:00 | 0 | 💸 Two agents idle, still on the bill |

Too few agents and people wait. Too many and you pay for machines that sit idle. Scaling automatically is possible, but that is another system for you to build and maintain.

> [!NOTE]
> Slow feedback has a real cost. In [Chapter 2](../../02-basics-of-ci-cd/02-continuous-integration/README.md) you learned that CI works because feedback arrives in minutes. A 50-minute queue quietly undoes that.

---

<p align="center">
  <a href="03-2-agents-turn-into-snowflakes.md">⬅️ 2️⃣ Agents turn into snowflakes</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="05-4-plugins-the-superpower-and-the-weak.md"><b>Next: 4️⃣ Plugins: the superpower and the weak point ➡️</b></a>
</p>
