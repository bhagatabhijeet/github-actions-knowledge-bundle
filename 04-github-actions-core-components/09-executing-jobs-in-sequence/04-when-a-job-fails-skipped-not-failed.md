---
type: Tutorial
title: "Executing Jobs in Sequence with needs: When a job fails: skipped, not failed"
description: "Failure spreads down the graph as skipped:"
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
  <a href="README.md">📂 <b>Executing Jobs in Sequence with needs</b></a> &nbsp;·&nbsp; Lesson 9 · Part 4 of 9 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# 💥 When a job fails: skipped, not failed

Failure spreads **down** the graph as **skipped**:

| Job | Result | Why |
|---|---|---|
| 🔨 build | ✅ success | |
| 🧪 test | ❌ failure | A step exited non-zero |
| 🚀 deploy (`needs: test`) | ⊘ skipped | Something it needed didn't succeed |
| 📣 announce (`needs: deploy`) | ⊘ skipped | Something *it* needed was skipped. Skips spread too |
| **The workflow run** | ❌ failure | Any failed job fails the run |

> [!NOTE]
> **Re-run failed jobs** re-runs `test` *and* every job downstream of it. `build` keeps its earlier result and its artifacts, so you don't pay to rebuild.

---

<p align="center">
  <a href="03-four-shapes-you-can-build.md">⬅️ Four shapes you can build</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="05-overriding-the-rule-with-if.md"><b>Next: Overriding the rule with `if:` ➡️</b></a>
</p>
