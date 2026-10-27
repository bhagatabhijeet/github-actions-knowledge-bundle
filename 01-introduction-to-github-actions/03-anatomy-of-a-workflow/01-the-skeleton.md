---
type: Tutorial
title: "Anatomy of a Workflow File: The skeleton"
description: "Every workflow answers four questions:"
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
  <a href="README.md">📂 <b>Anatomy of a Workflow File</b></a> &nbsp;·&nbsp; Lesson 3 · Part 1 of 6 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# 🦴 The skeleton

Every workflow answers four questions:

```yaml
name: Skeleton              # 🏷️ What is it called?

on: push                    # 🔔 WHEN does it run?

jobs:
  greet:
    runs-on: ubuntu-latest  # 🖥️ WHERE does it run?
    steps:                  # 👣 WHAT does it do?
      - run: echo "Hello from GitHub Actions"
```

📎 Copy it from [assets/snippets/workflow-skeleton.yml](../../assets/snippets/workflow-skeleton.yml)

That's a complete, working workflow. Seven lines.

---

<p align="center">
  <a href="README.md">⬅️ Overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="02-the-nesting-map.md"><b>Next: The nesting map ➡️</b></a>
</p>
