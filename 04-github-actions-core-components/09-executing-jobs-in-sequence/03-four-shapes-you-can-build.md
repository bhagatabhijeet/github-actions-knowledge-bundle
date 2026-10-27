---
type: Tutorial
title: "Executing Jobs in Sequence with needs: Four shapes you can build"
description: "Four shapes you can build, part 3 of 9 of Executing Jobs in Sequence with needs."
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
  <a href="README.md">📂 <b>Executing Jobs in Sequence with needs</b></a> &nbsp;·&nbsp; Lesson 9 · Part 3 of 9 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# 🧩 Four shapes you can build

```mermaid
flowchart LR
    subgraph C["⛓️ Chain"]
      direction LR
      a1[build] --> a2[test] --> a3[deploy]
    end
    subgraph F["🌿 Fan-out"]
      direction LR
      b1[build] --> b2[test-linux]
      b1 --> b3[test-windows]
    end
    subgraph I["🎯 Fan-in"]
      direction LR
      c1[lint] --> c3[deploy]
      c2[test] --> c3
    end
    subgraph D["💎 Diamond"]
      direction LR
      d1[build] --> d2[unit]
      d1 --> d3[e2e]
      d2 --> d4[release]
      d3 --> d4
    end
```

| Shape | YAML | Use it for |
|---|---|---|
| ⛓️ Chain | each job `needs:` the one before | Strict stages: build → test → deploy |
| 🌿 Fan-out | several jobs `needs: build` | Testing one build on many platforms at once |
| 🎯 Fan-in | `needs: [lint, test]` | A gate that waits for every check |
| 💎 Diamond | fan-out, then fan-in | Most real pipelines |

---

<p align="center">
  <a href="02-what-sequencing-costs-and-buys.md">⬅️ What sequencing costs, and buys</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="04-when-a-job-fails-skipped-not-failed.md"><b>Next: When a job fails: skipped, not failed ➡️</b></a>
</p>
