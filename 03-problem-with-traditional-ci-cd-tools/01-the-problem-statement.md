---
type: Tutorial
title: The Problem Statement
description: A Monday meeting about a build server that keeps breaking - the complaints that add up to the case against traditional, self-hosted CI/CD tools.
tags: [ci-cd, problem-statement, self-hosted, jenkins, beginner]
status: stable
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-07T00:00:00Z }
sources:
  - id: jenkins-scale
    resource: https://www.jenkins.io/doc/book/scaling/architecting-for-scale/
    title: Architecting for Scale (Jenkins User Handbook)
  - id: gh-understand
    resource: https://docs.github.com/en/actions/get-started/understand-github-actions
    title: Understanding GitHub Actions
---

<p align="center">
  <img src="../assets/images/chapter-03-banner.svg" alt="Chapter 3: The Problem with Traditional CI/CD Tools" width="100%">
</p>

<p align="center">
  <b>Lesson 1 of 4</b> &nbsp;·&nbsp; ⏱️ 6 min read &nbsp;·&nbsp; 🟢 No experience needed
</p>

# 🧯 The Problem Statement

Chapter 2 convinced you that CI/CD is worth doing. It skipped one awkward question: **what does the pipeline run on?**

For years the answer was "a server we look after ourselves". This chapter is about what that costs. Once you've felt the pain, nearly every design decision in GitHub Actions will make sense.

## 🗓️ Monday, 10:00 am: "Why is the build red again?"

Remember the team of five from [Chapter 2](../02-basics-of-ci-cd/01-what-is-ci-cd.md), the ones with the 43-step deploy document? They learned their lesson. A year ago they installed a popular open-source CI server on a spare virtual machine, wired it to their repository, and automated everything.

It was wonderful for about three months. Today they've booked a meeting room to talk about it.

| | Who | What they said |
|---|---|---|
| ⏳ | **Asha** | "My pull request waited 50 minutes for a build. There were three ahead of it and we have one build machine." |
| 🤷 | **Ben** | "It passes on my laptop and fails on the server. The server has Node 16. I need Node 20, and I'm scared to upgrade it because the other project still needs 16." |
| 💾 | **The team lead** | "The disk filled up on Saturday. Every build failed for two days and nobody knew until this morning." |
| 🧩 | **The newest hire** | "There's a security update for the CI server, but installing it breaks two plugins we depend on. So we're three versions behind." |
| 🏝️ | **Asha** | "Only Ben knows how it's all configured. Ben is on holiday next month." |
| 💸 | **Whoever pays the bills** | "That machine runs 24 hours a day. We build for about three of them." |

Nobody in that room is complaining about CI/CD. They still love the green ticks. They are complaining about **the thing that produces the green ticks**.

## 🧱 What "traditional CI/CD tool" means here

In this guide, a **traditional CI/CD tool** is a CI server that you install and operate yourself. Jenkins is the best-known example. TeamCity and Bamboo are in the same family when run on your own machines.

They share a shape:

| | Part | Job |
|---|---|---|
| 🧠 | **A central server** | Stores the pipeline configuration, schedules builds, shows the dashboard |
| 💪 | **Build agents** | The machines that actually run your builds |
| 🧩 | **Plugins** | Add-ons that teach the server to talk to Git, Docker, Slack, your cloud |

Every one of those parts is software running on a machine that **somebody on your team has to keep alive**.

> [!NOTE]
> This is not a claim that these tools are bad. They are powerful, flexible and proven at enormous scale. The problem is the amount of care they need, and who ends up providing it.

## 📝 The problem statement

Boil the meeting down to one sentence and you get this:

> [!IMPORTANT]
> **We adopted CI/CD to spend less time on releases. We now spend that time looking after the CI/CD tool.**

The team wanted to ship an online shop. Without anyone deciding it, they also became the operators of a small build farm.

```mermaid
flowchart LR
    A[🎯 Goal:<br/>ship the product]:::green --> B[🔧 Install a CI server]:::blue
    B --> C[🧩 Add plugins,<br/>agents, tools]:::orange
    C --> D[🚨 Patch, scale,<br/>fix, repeat]:::red
    D --> E[⌛ Less time for<br/>the product]:::red

    classDef green fill:#0f2d17,stroke:#3fb950,color:#fff,stroke-width:2px
    classDef blue fill:#0c1d3a,stroke:#58a6ff,color:#fff,stroke-width:2px
    classDef orange fill:#3d1d00,stroke:#ffa657,color:#fff,stroke-width:2px
    classDef red fill:#4a0d0d,stroke:#f85149,color:#fff,stroke-width:2px
```

## 🛒 The wish list

Before the meeting ends, the team lead turns each complaint into a requirement. This is what they want from whatever comes next:

| | Complaint | Requirement |
|---|---|---|
| ⏳ | Builds queue behind each other | **Capacity on demand**: ten builds at once should be as easy as one |
| 🤷 | "Works on my machine" | **A clean, predictable machine** for every build |
| 💾 | The server fell over unnoticed | **Nothing to install, patch or monitor** |
| 🧩 | Upgrades break plugins | **Integrations that don't hold the whole system hostage** |
| 🏝️ | Only one person understands it | **Configuration in the repository**, reviewed like code |
| 💸 | Paying for an idle machine | **Pay for what you use** |

> [!TIP]
> Keep this list in mind. In [Lesson 3](03-how-github-actions-answers.md) we hold it up against GitHub Actions, line by line.

## ✅ Checkpoint

<details>
<summary><b>What do we mean by a "traditional CI/CD tool" in this guide?</b></summary>

<br>

A CI server that you install and run on your own machines, made of a central server, build agents and plugins. Jenkins is the classic example.

</details>

<details>
<summary><b>Was the team unhappy with CI/CD itself?</b></summary>

<br>

No. They were unhappy with the cost of operating the tool that runs it: queues, version drift, outages, risky upgrades and knowledge held by one person.

</details>

<details>
<summary><b>State the problem in one sentence.</b></summary>

<br>

The time CI/CD was supposed to save is being spent on maintaining the CI/CD tool.

</details>

## 🎯 What you learned

- A traditional CI/CD tool is a **server you operate**: central server, build agents, plugins
- The practice of CI/CD was never the problem; **running the infrastructure** was
- The team's complaints turn into six requirements: on-demand capacity, clean machines, nothing to maintain, safe integrations, config as code, pay per use

---

<p align="center">
  <a href="../02-basics-of-ci-cd/06-cheat-sheet-and-quiz.md">⬅️ Chapter 2 Quiz</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="index.md">📚 Chapter 3</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="02-hidden-costs-of-self-hosted-ci.md"><b>Next: The Hidden Costs ➡️</b></a>
</p>
