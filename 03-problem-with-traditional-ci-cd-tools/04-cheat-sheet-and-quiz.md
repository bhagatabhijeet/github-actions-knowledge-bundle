---
type: Reference
title: Chapter 3 Cheat Sheet and Quiz
description: The case against traditional CI/CD tools on one page - the six pains, how GitHub Actions answers each, the trade-offs - followed by an eight-question self-check.
tags: [ci-cd, github-actions, self-hosted, cheat-sheet, quiz, recap]
status: stable
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-07T00:00:00Z }
sources:
  - id: gh-hosted-runners
    resource: https://docs.github.com/en/actions/concepts/runners/github-hosted-runners
    title: GitHub-hosted runners
  - id: gh-migrate-jenkins
    resource: https://docs.github.com/en/actions/tutorials/migrate-to-github-actions/manual-migrations/migrate-from-jenkins
    title: Migrating from Jenkins to GitHub Actions
---

<p align="center">
  <b>Lesson 4 of 4</b> &nbsp;·&nbsp; ⏱️ 5 min &nbsp;·&nbsp; 🏁 Chapter finale
</p>

# 📋 Chapter 3 Cheat Sheet & Quiz

## 📝 The problem statement

> [!IMPORTANT]
> **We adopted CI/CD to spend less time on releases. We now spend that time looking after the CI/CD tool.**

## 🧱 Anatomy of a traditional CI/CD tool

| | Part | Job | Your burden |
|---|---|---|---|
| 🧠 | **CI server** | Schedules builds, stores config | Patch, upgrade, back up, monitor |
| 💪 | **Build agents** | Run the builds | Install tools, keep clean, decide how many |
| 🧩 | **Plugins** | Add integrations | Keep compatible, track advisories |

## 🧊 Six pains → six answers

| | Pain | Cause | GitHub Actions answer |
|---|---|---|---|
| 1️⃣ | Server upkeep | You run the CI server | No server; it's a service |
| 2️⃣ | Snowflake agents | Long-lived machines, hand-installed tools | Fresh VM per job; versions declared in YAML |
| 3️⃣ | Queues and idle cost | Capacity fixed in advance | A runner per job, billed per minute |
| 4️⃣ | Fragile plugins | Installed server-wide, tied to server version | Actions versioned per workflow |
| 5️⃣ | Integration glue | Code and CI are separate systems | CI lives in the repository |
| 6️⃣ | Knowledge in one head | Config set through an admin screen | Workflows are reviewed files in Git |

## ⚖️ Trade-offs to remember

| | Trade-off | Mitigation |
|---|---|---|
| 🔒 | Tied to GitHub | Keep real logic in scripts; let the workflow just call them |
| 🌐 | No private-network access | Self-hosted runners |
| 🔧 | Limited machine choice | Larger or self-hosted runners |
| ⏱️ | 6-hour job limit on hosted runners | Split the job, or self-host |
| 💰 | Per-minute cost on private repos | Caching, path filters, concurrency |
| 🛡️ | Third-party action risk | Vet actions; pin to a commit SHA |

## 🔁 Jenkins → GitHub Actions dictionary

| Jenkins | GitHub Actions |
|---|---|
| `Jenkinsfile` | `.github/workflows/*.yml` |
| `agent { label '...' }` | `runs-on:` |
| `stage` | Job |
| `steps` | `steps:` |
| Plugin | Action (`uses:`) |
| Credentials | Secrets |
| Build agent | Runner |

## 🏆 Golden rules

> [!IMPORTANT]
> 1. **A free licence is not a free tool.** Count the hours, not the invoice.
> 2. **Describe the machine, don't point at one.** `python-version: '3.13'` beats "the agent with Python on it".
> 3. **Clean beats fast.** A fresh machine per job is why builds are repeatable.
> 4. **Hosted first.** Add self-hosted runners only when you hit a specific wall.
> 5. **Actions are other people's code.** Treat them with the care you'd give any dependency.

## 🧠 Quiz

<details>
<summary><b>1. What are the three parts of a traditional self-hosted CI/CD tool?</b></summary>

<br>

A central CI server, build agents, and plugins.

</details>

<details>
<summary><b>2. A build passes on one agent and fails on another with identical code. What is the likely cause?</b></summary>

<br>

Snowflake agents. The two machines have drifted apart: different tool versions, or leftovers from earlier builds.

</details>

<details>
<summary><b>3. Why is fixed build capacity "always the wrong size"?</b></summary>

<br>

Demand is uneven. Enough agents for the pre-release rush are mostly idle the rest of the time, and enough for a quiet morning cause queues at peak.

</details>

<details>
<summary><b>4. How does a plugin end up blocking a security update?</b></summary>

<br>

The plugin doesn't support the new server version. You either stay on the vulnerable version, wait for a fix, or replace the plugin and rework your pipelines.

</details>

<details>
<summary><b>5. Which single layer do you still maintain on GitHub Actions with hosted runners?</b></summary>

<br>

The pipeline definition: your workflow files.

</details>

<details>
<summary><b>6. What is the key difference between a server plugin and an action?</b></summary>

<br>

Scope. A plugin is installed once for the whole server at one version. An action is referenced per workflow at a version that workflow chooses, and it runs on the disposable runner.

</details>

<details>
<summary><b>7. Give two honest reasons a team might <i>not</i> choose GitHub-hosted runners.</b></summary>

<br>

Any two of: builds need access to a private network; they need hardware GitHub doesn't offer; jobs run longer than six hours; build volume is high enough that owning machines is cheaper; policy dictates where builds may run.

</details>

<details>
<summary><b>8. What do self-hosted runners give you, and what do they bring back?</b></summary>

<br>

They give you your own network and hardware while GitHub still handles scheduling, logs and the UI. They bring back machine upkeep: patching, cleanliness and capacity planning.

</details>

### 📊 How did you do?

| Score | Verdict |
|---|---|
| 8 | 🏆 You could chair that Monday meeting |
| 5 to 7 | 💪 Strong. Revisit the lessons you missed |
| 0 to 4 | 🔁 Reread [The Hidden Costs](02-hidden-costs-of-self-hosted-ci.md); the rest follows from it |

## 🎉 Chapter complete

You can state the problem with traditional CI/CD tools, name the six pains behind it, and explain what GitHub Actions changes and what it costs you in return.

> [!NOTE]
> **More chapters are on the way.** This guide grows one topic at a time. Check the [change log](../log.md) to see what's new.

---

<p align="center">
  <a href="03-how-github-actions-answers.md">⬅️ How GitHub Actions Answers</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="index.md">📚 Chapter 3</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="../README.md"><b>🏠 Back to Home</b></a>
</p>
