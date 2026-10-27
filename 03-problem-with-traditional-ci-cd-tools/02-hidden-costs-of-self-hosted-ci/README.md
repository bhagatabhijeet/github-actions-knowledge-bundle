---
type: Tutorial
title: The Hidden Costs of Running Your Own CI Server
description: Six pains of traditional self-hosted CI/CD tools - server upkeep, snowflake agents, wrong-sized capacity, fragile plugins, integration glue and knowledge silos - and why a free licence is not a free tool.
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
  <b>Lesson 2 of 4</b> &nbsp;·&nbsp; ⏱️ 8 min read &nbsp;·&nbsp; 🟢 Beginner
</p>

# 🧊 The Hidden Costs of Running Your Own CI Server

Abhijeet's list in [Lesson 1](../01-the-problem-statement/README.md) covered **day one**: what he'd have to install before the first build. This lesson is about **day two and every day after**. Suppose he had gone ahead. Here are the six pains his team would have met, and you'll recognise them in any self-hosted CI tool, not just one.

## 🗺️ In this topic

10 subtopics, about 15 minutes in all. Read them in order, or jump to the one you need.

| # | Subtopic | Time |
|---|---|---|
| 1 | 🏗️ [**How a traditional setup is built**](01-how-a-traditional-setup-is-built.md) | 2 min |
| 2 | 📄 [**1️⃣ You own a server**](02-1-you-own-a-server.md) | 1 min |
| 3 | 📄 [**2️⃣ Agents turn into snowflakes**](03-2-agents-turn-into-snowflakes.md) | 2 min |
| 4 | 📄 [**3️⃣ Capacity is always the wrong size**](04-3-capacity-is-always-the-wrong-size.md) | 2 min |
| 5 | 📄 [**4️⃣ Plugins: the superpower and the weak point**](05-4-plugins-the-superpower-and-the-weak.md) | 2 min |
| 6 | 📄 [**5️⃣ Glue between the tool and your code**](06-5-glue-between-the-tool-and-your.md) | 1 min |
| 7 | 📄 [**6️⃣ The knowledge lives in one head**](07-6-the-knowledge-lives-in-one-head.md) | 1 min |
| 8 | 🧊 [**The iceberg**](08-the-iceberg.md) | 1 min |
| 9 | ⚖️ [**To be fair**](09-to-be-fair.md) | 1 min |
| 10 | ✅ [**Checkpoint**](10-checkpoint.md) | 2 min |

<p align="center">
  <a href="01-how-a-traditional-setup-is-built.md"><b>▶️ Start with How a traditional setup is built</b></a>
</p>

## 🎯 What you learned

- A self-hosted CI server is a **production system** you must patch, back up and monitor
- Long-lived agents drift into **snowflakes** and carry leftovers between builds
- Fixed capacity is **too small at peak and too large at night**
- Plugins give flexibility and take away **safe, easy upgrades**
- Connecting the server to your code host is **glue you maintain**
- Setup knowledge tends to live **outside version control**, in one person's head

---

<p align="center">
  <a href="../01-the-problem-statement/README.md">⬅️ The Problem Statement</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="../index.md">📚 Chapter 3</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="../03-how-github-actions-answers/README.md"><b>Next: How GitHub Actions Answers ➡️</b></a>
</p>
