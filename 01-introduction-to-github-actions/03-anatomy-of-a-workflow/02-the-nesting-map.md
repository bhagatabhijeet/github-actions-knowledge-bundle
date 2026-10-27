---
type: Tutorial
title: "Anatomy of a Workflow File: The nesting map"
description: "Indentation in YAML is the structure. This is the shape hiding inside every workflow:"
tags: [github-actions, yaml, workflow-syntax, beginner]
status: stable
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-07T00:00:00Z }
sources:
  - id: gh-syntax
    resource: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
    title: Workflow syntax for GitHub Actions
  - id: gh-contexts
    resource: https://docs.github.com/en/actions/reference/workflows-and-actions/contexts
    title: Contexts reference
---

<p align="center">
  <a href="README.md">📂 <b>Anatomy of a Workflow File</b></a> &nbsp;·&nbsp; Lesson 3 · Part 2 of 6 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# 🗺️ The nesting map

Indentation in YAML *is* the structure. This is the shape hiding inside every workflow:

```text
workflow
├── name
├── on ─────────────── events
└── jobs
    ├── job-one
    │   ├── runs-on ── runner
    │   └── steps
    │       ├── step ─ uses (an action)
    │       └── step ─ run  (a command)
    └── job-two
        ├── needs ──── job-one
        ├── runs-on
        └── steps
```

---

<p align="center">
  <a href="01-the-skeleton.md">⬅️ The skeleton</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="03-key-by-key.md"><b>Next: Key by key ➡️</b></a>
</p>
