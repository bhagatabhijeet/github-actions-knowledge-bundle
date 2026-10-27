---
type: Tutorial
title: Anatomy of a Workflow File
description: A line-by-line tour of workflow YAML - name, on, jobs, runs-on and steps - plus the YAML rules that trip up every beginner.
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
  <b>Lesson 3 of 5</b> &nbsp;·&nbsp; ⏱️ 9 min read &nbsp;·&nbsp; 🟢 Beginner
</p>

# 🔬 Anatomy of a Workflow File

You know the six concepts. Now let's see how they look on the page. By the end of this lesson, a workflow file will read like a sentence.

## 🗺️ In this topic

6 subtopics, about 7 minutes in all. Read them in order, or jump to the one you need.

| # | Subtopic | Time |
|---|---|---|
| 1 | 🦴 [**The skeleton**](01-the-skeleton.md) | 1 min |
| 2 | 🗺️ [**The nesting map**](02-the-nesting-map.md) | 1 min |
| 3 | 🔍 [**Key by key**](03-key-by-key.md) | 2 min |
| 4 | 🧠 [**Two extras you'll see everywhere**](04-two-extras-you-ll-see-everywhere.md) | 1 min |
| 5 | 🪤 [**The five YAML traps**](05-the-five-yaml-traps.md) | 1 min |
| 6 | 🧪 [**Read it aloud**](06-read-it-aloud.md) | 1 min |

<p align="center">
  <a href="01-the-skeleton.md"><b>▶️ Start with The skeleton</b></a>
</p>

## 🎯 What you learned

- A workflow answers **what's it called, when, where, what**
- Indentation is structure; `jobs` contain `steps`
- A step either `uses` an action or `run`s a command
- `${{ }}` injects values; keep untrusted input out of `run:`
- Quote versions, use spaces, mind the dash

---

<p align="center">
  <a href="../02-core-concepts/README.md">⬅️ The Six Core Concepts</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="../index.md">📚 Chapter 1</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="../04-your-first-workflow/README.md"><b>Next: Your First Workflow ➡️</b></a>
</p>
