---
type: Tutorial
title: "The Six Core Concepts: The whole family, one table"
description: "All six core concepts side by side in one table, with what each one is and where it appears in YAML."
tags: [github-actions, concepts, workflow, job, step, action, runner, event]
status: stable
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-07T00:00:00Z }
sources:
  - id: gh-understand
    resource: https://docs.github.com/en/actions/get-started/understand-github-actions
    title: Understanding GitHub Actions
  - id: gh-runners
    resource: https://docs.github.com/en/actions/concepts/runners/github-hosted-runners
    title: GitHub-hosted runners
  - id: gh-events
    resource: https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows
    title: Events that trigger workflows
---

<p align="center">
  <a href="README.md">📂 <b>The Six Core Concepts</b></a> &nbsp;·&nbsp; Lesson 2 · Part 7 of 8 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# 🗺️ The whole family, one table

| | Concept | It is... | In YAML | How many |
|---|---|---|---|---|
| 🔔 | **Event** | what happened | `on:` | 1+ per workflow |
| 📜 | **Workflow** | the file | `.github/workflows/*.yml` | many per repo |
| 📦 | **Job** | work on one machine | `jobs.<id>:` | 1+ per workflow |
| 👣 | **Step** | one task | `steps: - ...` | 1+ per job |
| 🧱 | **Action** | reusable step logic | `uses:` | 0+ per job |
| 🖥️ | **Runner** | the machine | `runs-on:` | 1 per job |

---

<p align="center">
  <a href="06-6-runner-the-machine.md">⬅️ 6. Runner: the machine</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="08-checkpoint.md"><b>Next: Checkpoint ➡️</b></a>
</p>
