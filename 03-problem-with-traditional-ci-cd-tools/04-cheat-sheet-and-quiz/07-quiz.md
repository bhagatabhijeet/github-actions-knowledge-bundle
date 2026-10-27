---
type: Reference
title: "Chapter 3 Cheat Sheet and Quiz: Quiz"
description: "A central CI server, build agents, and plugins."
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
  <a href="README.md">📂 <b>Chapter 3 Cheat Sheet and Quiz</b></a> &nbsp;·&nbsp; Lesson 4 · Part 7 of 8 &nbsp;·&nbsp; ⏱️ 4 min
</p>

# 🧠 Quiz

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

## 📊 How did you do?

| Score | Verdict |
|---|---|
| 8 | 🏆 Abhijeet would hire you |
| 5 to 7 | 💪 Strong. Revisit the lessons you missed |
| 0 to 4 | 🔁 Reread [The Hidden Costs](../02-hidden-costs-of-self-hosted-ci/README.md); the rest follows from it |

---

<p align="center">
  <a href="06-golden-rules.md">⬅️ Golden rules</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="08-chapter-complete.md"><b>Next: Chapter complete ➡️</b></a>
</p>
