---
type: Tutorial
title: "The Six Core Concepts: Checkpoint"
description: "Quick self-check on the six core concepts, including whether two jobs without needs run in order or in parallel."
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
  <a href="README.md">📂 <b>The Six Core Concepts</b></a> &nbsp;·&nbsp; Lesson 2 · Part 8 of 8 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# ✅ Checkpoint

<details>
<summary><b>Two jobs have no <code>needs:</code> between them. Which runs first?</b></summary>

<br>

Neither. They start at the same time, in parallel, on separate runners.

</details>

<details>
<summary><b>Job A creates <code>report.txt</code>. Can Job B read it?</b></summary>

<br>

Not directly. Each job gets its own fresh runner. Job A would need to upload the file as an artifact and Job B would download it.

</details>

<details>
<summary><b>What is the difference between <code>run:</code> and <code>uses:</code>?</b></summary>

<br>

`run:` executes shell commands you type inline. `uses:` executes a packaged, reusable action.

</details>

---

<p align="center">
  <a href="07-the-whole-family-one-table.md">⬅️ The whole family, one table</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="../03-anatomy-of-a-workflow/README.md"><b>Next topic ➡️</b></a>
</p>
