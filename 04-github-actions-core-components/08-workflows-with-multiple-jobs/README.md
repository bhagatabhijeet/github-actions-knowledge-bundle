---
type: Tutorial
title: Workflows with Multiple Jobs (Hands-On)
description: Split a workflow into build, test and deploy jobs - why they run in parallel by default, how needs puts them in order, how artifacts carry files between runners, and how to read the job graph.
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
  <b>Lesson 8 of 14</b> &nbsp;·&nbsp; ⏱️ 18 min &nbsp;·&nbsp; 🛠️ Hands-on
</p>

# 🔗 Workflows with Multiple Jobs

Every dragon so far lived in a single job. Real pipelines have stages: **build** something, **test** it, then **deploy** it. In GitHub Actions each stage is usually its own job. This lesson splits the dragon workflow into three jobs, watches it break, and fixes it.

## 🗺️ In this topic

8 subtopics, about 14 minutes in all. Read them in order, or jump to the one you need.

| # | Subtopic | Time |
|---|---|---|
| 1 | ✂️ [**Why split into jobs?**](01-why-split-into-jobs.md) | 1 min |
| 2 | 💥 [**Attempt 1: just split it**](02-attempt-1-just-split-it.md) | 2 min |
| 3 | ⏩ [**Fix 1: put the jobs in order with `needs`**](03-fix-1-put-the-jobs-in-order.md) | 2 min |
| 4 | 📦 [**Fix 2: carry the file with artifacts**](04-fix-2-carry-the-file-with-artifacts.md) | 3 min |
| 5 | 🗺️ [**Reading the job graph**](05-reading-the-job-graph.md) | 2 min |
| 6 | 🔀 [**Artifacts, outputs or cache?**](06-artifacts-outputs-or-cache.md) | 1 min |
| 7 | 🛠️ [**Try it yourself**](07-try-it-yourself.md) | 1 min |
| 8 | ✅ [**Checkpoint**](08-checkpoint.md) | 2 min |

<p align="center">
  <a href="01-why-split-into-jobs.md"><b>▶️ Start with Why split into jobs?</b></a>
</p>

## 🎯 What you learned

- Split stages into **jobs** for clearer logs, parallel speed and re-running only what failed
- Jobs run **in parallel** by default; **`needs:`** puts them in order
- A failed job **skips** the jobs that need it, unless they use `if: always()`
- Each job has its **own runner**, so files travel by **artifact**: upload, then download by the same name
- Use **outputs** for small strings and **cache** for slow-to-rebuild files

---

<p align="center">
  <a href="../07-executing-shell-scripts/README.md">⬅️ Executing Shell Scripts</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="../index.md">📚 Chapter 4</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="../09-executing-jobs-in-sequence/README.md"><b>Next: Jobs in Sequence ➡️</b></a>
</p>
