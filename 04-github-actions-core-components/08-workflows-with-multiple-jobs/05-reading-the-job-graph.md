---
type: Tutorial
title: "Workflows with Multiple Jobs: Reading the job graph"
description: "Open the run's Summary and GitHub draws the jobs as a graph:"
tags: [github-actions, jobs, needs, parallel, artifacts, hands-on]
status: stable
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-25T00:00:00Z }
sources:
  - id: gh-workflow-syntax
    resource: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
    title: Workflow syntax for GitHub Actions
  - id: gh-artifacts
    resource: https://docs.github.com/en/actions/tutorials/store-and-share-data
    title: Store and share data with workflow artifacts
  - id: upload-artifact
    resource: https://github.com/actions/upload-artifact
    title: actions/upload-artifact
  - id: download-artifact
    resource: https://github.com/actions/download-artifact
    title: actions/download-artifact
---

<p align="center">
  <a href="README.md">📂 <b>Workflows with Multiple Jobs</b></a> &nbsp;·&nbsp; Lesson 8 · Part 5 of 8 &nbsp;·&nbsp; ⏱️ 2 min
</p>

# 🗺️ Reading the job graph

Open the run's **Summary** and GitHub draws the jobs as a graph:

```mermaid
flowchart LR
    B["🔨 build_job"]:::blue --> T["🧪 test_job"]:::purple --> D["🚀 deploy_job"]:::green

    classDef blue fill:#0c1d3a,stroke:#58a6ff,color:#fff,stroke-width:2px
    classDef purple fill:#22123f,stroke:#bc8cff,color:#fff,stroke-width:2px
    classDef green fill:#0f2d17,stroke:#3fb950,color:#fff,stroke-width:2px
```

| You see | Meaning |
|---|---|
| Boxes side by side in one column | They run in parallel |
| A line between two boxes | A `needs:` relationship |
| ⚪ greyed-out box | Waiting on the job before it |
| ⊘ skipped box | A job it needed failed |
| 📦 **Artifacts** section below | Files uploaded during the run |

A more realistic pipeline mixes both shapes, fanning out to parallel checks and back in before deploying:

```mermaid
flowchart LR
    B["🔨 build"]:::blue --> U["🧪 unit tests"]:::purple
    B --> L["🧹 lint"]:::purple
    B --> S["🛡️ security scan"]:::purple
    U --> D["🚀 deploy"]:::green
    L --> D
    S --> D

    classDef blue fill:#0c1d3a,stroke:#58a6ff,color:#fff,stroke-width:2px
    classDef purple fill:#22123f,stroke:#bc8cff,color:#fff,stroke-width:2px
    classDef green fill:#0f2d17,stroke:#3fb950,color:#fff,stroke-width:2px
```

```yaml
  deploy:
    needs: [unit_tests, lint, security_scan]
```

---

<p align="center">
  <a href="04-fix-2-carry-the-file-with-artifacts.md">⬅️ Fix 2: carry the file with artifacts</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="06-artifacts-outputs-or-cache.md"><b>Next: Artifacts, outputs or cache? ➡️</b></a>
</p>
