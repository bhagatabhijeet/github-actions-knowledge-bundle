---
type: Tutorial
title: Executing Jobs in Sequence with needs (Hands-On)
description: A deep dive into needs - the cost of sequencing, chains, fan-out and fan-in, how failure turns into skipped, status functions like always() and !cancelled(), needs.<job>.result, and why outputs only flow from direct dependencies.
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
  <b>Lesson 9 of 14</b> &nbsp;·&nbsp; ⏱️ 16 min &nbsp;·&nbsp; 🛠️ Hands-on
</p>

# ⛓️ Executing Jobs in Sequence with `needs`

In the last lesson `needs:` fixed a race in one line. It deserves a closer look, because that one keyword decides **when** jobs start, **what happens when one fails**, and **which data** each job can see. Get it right and your pipeline can't deploy untested code. Get it wrong and jobs get silently skipped, or wait for no reason.

## 🗺️ In this topic

9 subtopics, about 13 minutes in all. Read them in order, or jump to the one you need.

| # | Subtopic | Time |
|---|---|---|
| 1 | 🎯 [**The rule in one sentence**](01-the-rule-in-one-sentence.md) | 1 min |
| 2 | ⏱️ [**What sequencing costs, and buys**](02-what-sequencing-costs-and-buys.md) | 2 min |
| 3 | 🧩 [**Four shapes you can build**](03-four-shapes-you-can-build.md) | 1 min |
| 4 | 💥 [**When a job fails: skipped, not failed**](04-when-a-job-fails-skipped-not-failed.md) | 1 min |
| 5 | 🚦 [**Overriding the rule with `if:`**](05-overriding-the-rule-with-if.md) | 2 min |
| 6 | 📤 [**Outputs only flow from direct `needs`**](06-outputs-only-flow-from-direct-needs.md) | 1 min |
| 7 | 🪤 [**Common mistakes**](07-common-mistakes.md) | 1 min |
| 8 | 🛠️ [**Try it yourself**](08-try-it-yourself.md) | 2 min |
| 9 | ✅ [**Checkpoint**](09-checkpoint.md) | 2 min |

<p align="center">
  <a href="01-the-rule-in-one-sentence.md"><b>▶️ Start with The rule in one sentence</b></a>
</p>

## 🎯 What you learned

- **`needs:`** makes a job wait for others to **succeed**; take a string for one job or a list for several
- Sequencing adds wall-clock time. A run is as fast as its **longest chain**, so keep independent jobs parallel
- Failure spreads down the graph as **skipped**, and so do skips
- Status functions override that: **`failure()`**, **`!cancelled()`** (preferred) and **`always()`**
- **`needs.<job>.result`** tells you exactly what happened to each job
- Job outputs are visible only from **direct** `needs`

---

<p align="center">
  <a href="../08-workflows-with-multiple-jobs/README.md">⬅️ Multiple Jobs</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="../index.md">📚 Chapter 4</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="../10-storing-workflow-data-as-artifacts/README.md"><b>Next: Storing Data as Artifacts ➡️</b></a>
</p>
