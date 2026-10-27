---
type: Tutorial
title: "Executing Jobs in Sequence with needs: The rule in one sentence"
description: "A job with needs: waits until every job it lists has finished successfully. If any of them fails or is skipped, it is skipped too."
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
  <a href="README.md">📂 <b>Executing Jobs in Sequence with needs</b></a> &nbsp;·&nbsp; Lesson 9 · Part 1 of 9 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# 🎯 The rule in one sentence

> **A job with `needs:` waits until every job it lists has finished successfully. If any of them fails or is skipped, it is skipped too.**

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps: [...]

  test:
    needs: build              # one job: a string
    runs-on: ubuntu-latest
    steps: [...]

  deploy:
    needs: [build, test]      # several jobs: a list
    runs-on: ubuntu-latest
    steps: [...]
```

---

<p align="center">
  <a href="README.md">⬅️ Overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="02-what-sequencing-costs-and-buys.md"><b>Next: What sequencing costs, and buys ➡️</b></a>
</p>
