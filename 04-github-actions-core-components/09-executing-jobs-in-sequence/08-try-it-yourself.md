---
type: Tutorial
title: "Executing Jobs in Sequence with needs: Try it yourself"
description: "This repository ships a four-job pipeline with a \"break it\" switch: 04-needs-sequence.yml."
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
  <a href="README.md">📂 <b>Executing Jobs in Sequence with needs</b></a> &nbsp;·&nbsp; Lesson 9 · Part 8 of 9 &nbsp;·&nbsp; ⏱️ 2 min
</p>

# 🛠️ Try it yourself

This repository ships a four-job pipeline with a "break it" switch: [`04-needs-sequence.yml`](../../.github/workflows/04-needs-sequence.yml).

```mermaid
flowchart LR
    B["🔨 build<br/>outputs: version"]:::blue --> T["🧪 test"]:::purple --> D["🚀 deploy<br/>needs: [build, test]"]:::green
    B --> D
    B --> R["📋 report<br/>if: !cancelled()"]:::gold
    T --> R
    D --> R

    classDef blue fill:#0c1d3a,stroke:#58a6ff,color:#fff,stroke-width:2px
    classDef purple fill:#22123f,stroke:#bc8cff,color:#fff,stroke-width:2px
    classDef green fill:#0f2d17,stroke:#3fb950,color:#fff,stroke-width:2px
    classDef gold fill:#3d2a00,stroke:#e3b341,color:#fff,stroke-width:2px
```

1. **Actions** tab → **04 - Jobs in Sequence** → **Run workflow**, leaving the box unticked
2. Watch the graph fill in one box at a time. Open **deploy**: it prints `Deploying version 1.0.<run number>`, an output read from `build`
3. Scroll down the **Summary** page to the results table that `report` wrote: all `success`
4. Run it again with **Make the tests fail** ticked. `test` goes ❌, `deploy` is ⊘ skipped, and `report` still runs and records `failure` and `skipped`
5. Click **Re-run failed jobs**. Notice `build` is not re-run
6. **Stretch:** in a fork, add a `notify` job that runs only when `needs.test.result == 'failure'`

---

<p align="center">
  <a href="07-common-mistakes.md">⬅️ Common mistakes</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="09-checkpoint.md"><b>Next: Checkpoint ➡️</b></a>
</p>
