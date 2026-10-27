---
type: Tutorial
title: "Life of a Workflow Run: Six stages"
description: "The six stages every run goes through - event, queue, provision, execute, report and clean up - and what happens in each."
tags: [github-actions, workflow-run, matrix, logs, artifacts, hands-on]
status: stable
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-26T00:00:00Z }
sources:
  - id: gh-workflow-syntax
    resource: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
    title: Workflow syntax for GitHub Actions
  - id: gh-logs
    resource: https://docs.github.com/en/actions/how-tos/monitor-workflows/use-workflow-run-logs
    title: Using workflow run logs
  - id: gh-artifacts
    resource: https://docs.github.com/en/actions/concepts/workflows-and-actions/workflow-artifacts
    title: Workflow artifacts
---

<p align="center">
  <a href="README.md">📂 <b>Life of a Workflow Run</b></a> &nbsp;·&nbsp; Lesson 2 · Part 2 of 7 &nbsp;·&nbsp; ⏱️ 2 min
</p>

# 🪜 Six stages

| | Stage | What happens |
|---|---|---|
| 1 | 🔔 **Event** | A push arrives. GitHub finds every workflow whose `on:` matches it |
| 2 | 📋 **Queue** | A workflow run is created. The matrix expands into three jobs |
| 3 | 🖥️ **Provision** | GitHub starts one fresh VM per job, all at the same time |
| 4 | 👣 **Execute** | Each runner works through its steps, one after another |
| 5 | 📡 **Report** | Logs stream back to GitHub live, step by step |
| 6 | 🧹 **Clean up** | Each runner is destroyed. Only logs and artifacts survive |

```mermaid
sequenceDiagram
    autonumber
    actor Dev as 🧑‍💻 Developer
    participant GH as 🐙 GitHub
    participant R as 🖥️ 3 runners

    Dev->>GH: git push
    GH->>GH: Match event, queue 3 jobs
    GH->>R: Provision 3 fresh VMs
    R->>R: checkout → setup-python → tests
    R-->>GH: Logs, status, artifacts
    GH->>R: Destroy the VMs
    GH-->>Dev: ✅ or ❌ on the commit
```

---

<p align="center">
  <a href="01-the-whole-run-in-one-picture.md">⬅️ The whole run in one picture</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="03-parallel-outside-serial-inside.md"><b>Next: Parallel outside, serial inside ➡️</b></a>
</p>
