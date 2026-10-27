---
type: Tutorial
title: "Executing Jobs in Sequence with needs: What sequencing costs, and buys"
description: "Sequence only what truly depends on something else. Lint, unit tests and a security scan don't depend on each other, so let them run side by side, and put needs: only on the job that must wait for all of them. The run..."
tags: [github-actions, jobs, needs, sequence, if, status-functions, outputs, hands-on]
status: stable
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-26T00:00:00Z }
sources:
  - id: gh-workflow-syntax
    resource: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
    title: Workflow syntax for GitHub Actions
  - id: gh-expressions
    resource: https://docs.github.com/en/actions/reference/workflows-and-actions/expressions
    title: Evaluate expressions in workflows and actions
  - id: gh-contexts
    resource: https://docs.github.com/en/actions/reference/workflows-and-actions/contexts
    title: Contexts reference
---

<p align="center">
  <a href="README.md">📂 <b>Executing Jobs in Sequence with needs</b></a> &nbsp;·&nbsp; Lesson 9 · Part 2 of 9 &nbsp;·&nbsp; ⏱️ 2 min
</p>

# ⏱️ What sequencing costs, and buys

<p align="center">
  <img src="../../assets/images/needs-sequence-timeline.svg" alt="Timelines comparing jobs with no needs, which all start at once and finish in about 30 seconds but deploy before tests end, with jobs chained by needs, which take about 60 seconds but only deploy tested code, and a failure case where test fails, deploy is skipped and a report job with if not cancelled still runs" width="100%">
</p>

| | No `needs` | With `needs` |
|---|---|---|
| ⏱️ Wall-clock time | The **longest** job | The **sum** of the chain |
| 🛡️ Safety | Deploy may run before or despite failed tests | Deploy runs only after tests pass |
| 🧾 Minutes billed | Same | Same: you pay for job time, not waiting time |

> [!TIP]
> **Sequence only what truly depends on something else.** Lint, unit tests and a security scan don't depend on each other, so let them run side by side, and put `needs:` only on the job that must wait for all of them. The run takes as long as its **longest chain**, often called the critical path.

---

<p align="center">
  <a href="01-the-rule-in-one-sentence.md">⬅️ The rule in one sentence</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="03-four-shapes-you-can-build.md"><b>Next: Four shapes you can build ➡️</b></a>
</p>
