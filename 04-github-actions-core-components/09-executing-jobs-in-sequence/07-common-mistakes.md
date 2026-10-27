---
type: Tutorial
title: "Executing Jobs in Sequence with needs: Common mistakes"
description: "The usual needs: mistakes, from typos in job IDs and cycles to reading outputs from indirect dependencies."
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
  <a href="README.md">📂 <b>Executing Jobs in Sequence with needs</b></a> &nbsp;·&nbsp; Lesson 9 · Part 7 of 9 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# 🪤 Common mistakes

| Mistake | What you see | Fix |
|---|---|---|
| Typo in a job ID, e.g. `needs: buidl` | The workflow is **invalid** and never starts. The Actions tab names the unknown job | Use the job's **ID** (the YAML key), not its `name:` |
| Two jobs that need each other | Invalid workflow: a dependency cycle | Draw the graph; it must flow one way |
| A report job without `if:` | It's skipped exactly when you need it | Add `if: ${{ !cancelled() }}` |
| Reading outputs from a grandparent job | An empty string, no error | List that job in `needs:` too |
| Sequencing independent checks | Slow pipelines | Run them in parallel and fan in |

---

<p align="center">
  <a href="06-outputs-only-flow-from-direct-needs.md">⬅️ Outputs only flow from direct `needs`</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="08-try-it-yourself.md"><b>Next: Try it yourself ➡️</b></a>
</p>
