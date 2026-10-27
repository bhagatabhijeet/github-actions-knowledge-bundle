---
type: Tutorial
title: "The Hidden Costs of Running Your Own CI Server: Checkpoint"
description: "A long-lived build machine that has been changed by hand so many times that it is unique. Builds behave differently depending on which agent runs them, and nobody can recreate the machine reliably."
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
  <a href="README.md">📂 <b>The Hidden Costs of Running Your Own CI Server</b></a> &nbsp;·&nbsp; Lesson 2 · Part 10 of 10 &nbsp;·&nbsp; ⏱️ 2 min
</p>

# ✅ Checkpoint

<details>
<summary><b>What is a "snowflake" agent, and why is it a problem?</b></summary>

<br>

A long-lived build machine that has been changed by hand so many times that it is unique. Builds behave differently depending on which agent runs them, and nobody can recreate the machine reliably.

</details>

<details>
<summary><b>Why can a plugin stop you from installing a security update?</b></summary>

<br>

Plugins are tied to server versions and to each other. If a plugin you depend on doesn't work with the new server version, you must either wait, replace the plugin, or stay on the vulnerable version.

</details>

<details>
<summary><b>Your team has two agents. Name the two opposite ways that number can be wrong on the same day.</b></summary>

<br>

Too few at peak time, so builds queue. Too many overnight, so you pay for idle machines.

</details>

<details>
<summary><b>"It's open source, so it costs nothing." What's missing from that sentence?</b></summary>

<br>

Everything below the waterline: the machines, the maintenance hours, the outages, the queues and the people needed to run it.

</details>

---

<p align="center">
  <a href="09-to-be-fair.md">⬅️ To be fair</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md#-what-you-learned"><b>Wrap up: What you learned ➡️</b></a>
</p>
