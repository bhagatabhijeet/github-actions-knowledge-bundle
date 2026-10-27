---
type: Tutorial
title: "Executing Jobs in Sequence with needs: Overriding the rule with `if:`"
description: "Sometimes a job should run after a failure: a report, a Slack alert, a cleanup. Add a job-level if: with a status function:"
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
  <a href="README.md">📂 <b>Executing Jobs in Sequence with needs</b></a> &nbsp;·&nbsp; Lesson 9 · Part 5 of 9 &nbsp;·&nbsp; ⏱️ 2 min
</p>

# 🚦 Overriding the rule with `if:`

Sometimes a job **should** run after a failure: a report, a Slack alert, a cleanup. Add a job-level `if:` with a **status function**:

| `if:` | Runs when the jobs it needs... | Typical use |
|---|---|---|
| *(nothing)* = `success()` | all succeeded | Normal stages |
| `${{ failure() }}` | at least one **failed** | 🔔 Alert the team |
| `${{ !cancelled() }}` | finished any way, unless the run was **cancelled** | 📋 Reports, test summaries |
| `${{ always() }}` | finished any way, **even when cancelled** | 🧹 Must-run cleanup |
| `${{ cancelled() }}` | the run was cancelled | Releasing a lock |

> [!IMPORTANT]
> **Prefer `!cancelled()` over `always()`.** A job with `always()` still runs after you press **Cancel workflow**, which is rarely what you meant when you cancelled.

To react to **one particular** job, read its result from the `needs` context:

```yaml
  notify:
    needs: [test, deploy]
    if: ${{ !cancelled() && needs.test.result == 'failure' }}
    runs-on: ubuntu-latest
    steps:
      - run: echo "Tests failed. Deploy was ${{ needs.deploy.result }}."
```

`needs.<job>.result` is one of `success`, `failure`, `cancelled` or `skipped`.

---

<p align="center">
  <a href="04-when-a-job-fails-skipped-not-failed.md">⬅️ When a job fails: skipped, not failed</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="06-outputs-only-flow-from-direct-needs.md"><b>Next: Outputs only flow from direct `needs` ➡️</b></a>
</p>
