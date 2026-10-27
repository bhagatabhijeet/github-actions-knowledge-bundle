---
type: Tutorial
title: "Anatomy of a Workflow File: The five YAML traps"
description: "Nine out of ten \"my workflow won't start\" problems are one of these."
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
  <a href="README.md">📂 <b>Anatomy of a Workflow File</b></a> &nbsp;·&nbsp; Lesson 3 · Part 5 of 6 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# 🪤 The five YAML traps

Nine out of ten "my workflow won't start" problems are one of these.

| | Trap | ❌ Wrong | ✅ Right |
|---|---|---|---|
| 1 | **Tabs** | a tab character | spaces only (2 per level) |
| 2 | **Misaligned keys** | `steps:` deeper than `runs-on:` | siblings share a column |
| 3 | **Missing dash** | `steps:` then `run: ...` | `- run: ...` |
| 4 | **Versions as numbers** | `python-version: 3.10` (becomes `3.1`!) | `python-version: '3.10'` |
| 5 | **Wrong folder** | `.github/workflow/` | `.github/workflows/` |

> [!TIP]
> Trap 4 is famous. YAML reads `3.10` as the number three-point-one. Quote your versions and you'll never meet it.

---

<p align="center">
  <a href="04-two-extras-you-ll-see-everywhere.md">⬅️ Two extras you'll see everywhere</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="06-read-it-aloud.md"><b>Next: Read it aloud ➡️</b></a>
</p>
