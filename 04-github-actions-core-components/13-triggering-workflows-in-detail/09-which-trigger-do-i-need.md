---
type: Tutorial
title: "Triggering Workflows in Detail: Which trigger do I need?"
description: "Real workflows often combine several, like the companion workflow: push for changes, schedule as a safety net, and workflowdispatch so you can always run it by hand."
tags: [github-actions, triggers, events, on, workflow_dispatch, schedule, cron, repository_dispatch, workflow_run, filters, hands-on]
status: stable
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-26T00:00:00Z }
sources:
  - id: gh-workflows-concepts
    resource: https://docs.github.com/en/actions/concepts/workflows-and-actions/workflows#workflow-triggers
    title: Workflows - Workflow triggers
  - id: gh-events
    resource: https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows
    title: Events that trigger workflows
  - id: gh-workflow-syntax
    resource: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
    title: Workflow syntax for GitHub Actions
---

<p align="center">
  <a href="README.md">📂 <b>Triggering Workflows in Detail</b></a> &nbsp;·&nbsp; Lesson 13 · Part 9 of 12 &nbsp;·&nbsp; ⏱️ 2 min
</p>

# 🧭 Which trigger do I need?

```mermaid
flowchart TD
    Q{"What should start it?"}:::gold
    Q -->|"Code changes"| A["push / pull_request<br/>+ branches, paths filters"]:::blue
    Q -->|"A clock"| B["schedule<br/>cron, in UTC"]:::pink
    Q -->|"A person"| C["workflow_dispatch<br/>+ typed inputs"]:::green
    Q -->|"Another system"| D["repository_dispatch<br/>+ client_payload"]:::purple
    Q -->|"Another workflow"| E{"Same file?"}:::gold
    E -->|"Yes"| F["needs:"]:::blue
    E -->|"No, after it"| G["workflow_run"]:::purple
    E -->|"No, reuse it"| H["workflow_call"]:::purple
    classDef blue fill:#0c1d3a,stroke:#58a6ff,color:#fff,stroke-width:2px
    classDef pink fill:#3a0f2b,stroke:#f778ba,color:#fff,stroke-width:2px
    classDef green fill:#0f2d17,stroke:#3fb950,color:#fff,stroke-width:2px
    classDef purple fill:#22123f,stroke:#bc8cff,color:#fff,stroke-width:2px
    classDef gold fill:#3d2a00,stroke:#e3b341,color:#fff,stroke-width:2px
```

Real workflows often combine several, like the companion workflow: `push` for changes, `schedule` as a safety net, and `workflow_dispatch` so you can always run it by hand.

---

<p align="center">
  <a href="08-pull-request-vs-pull-request-target.md">⬅️ `pull_request` vs `pull_request_target`</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="10-common-mistakes.md"><b>Next: Common mistakes ➡️</b></a>
</p>
