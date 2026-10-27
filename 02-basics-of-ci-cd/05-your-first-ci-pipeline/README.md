---
type: Tutorial
title: Your First CI Pipeline (Hands-On)
description: Build a real three-stage pipeline - lint, test across a matrix, package an artifact - using the CI Basics workflow and sample app that ship in this repository.
resource: /.github/workflows/02-ci-basics.yml
tags: [ci-cd, hands-on, pipeline, matrix, artifacts, python, pull-requests]
status: stable
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-07T00:00:00Z }
sources:
  - id: gh-python
    resource: https://docs.github.com/en/actions/tutorials/build-and-test-code/python
    title: Building and testing Python
  - id: gh-artifacts
    resource: https://docs.github.com/en/actions/tutorials/store-and-share-data
    title: Store and share data with workflow artifacts
  - id: gh-concurrency
    resource: https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/control-workflow-concurrency
    title: Control the concurrency of workflows and jobs
---

<p align="center">
  <b>Lesson 5 of 6</b> &nbsp;·&nbsp; ⏱️ 25 min hands-on &nbsp;·&nbsp; 🛠️ Keyboard required
</p>

# 🛠️ Your First CI Pipeline

Time to turn theory into green ticks. You'll run a real pipeline, watch it catch a bug you plant, and download what it builds.

## 🗺️ In this topic

9 subtopics, about 12 minutes in all. Read them in order, or jump to the one you need.

| # | Subtopic | Time |
|---|---|---|
| 1 | 🧰 [**The cast**](01-the-cast.md) | 1 min |
| 2 | 🗺️ [**The pipeline you're about to run**](02-the-pipeline-you-re-about-to-run.md) | 1 min |
| 3 | 📄 [**The workflow, piece by piece**](03-the-workflow-piece-by-piece.md) | 3 min |
| 4 | ▶️ [**Exercise 1: Go green**](04-exercise-1-go-green.md) | 1 min |
| 5 | 🎁 [**Exercise 2: Collect your artifact**](05-exercise-2-collect-your-artifact.md) | 1 min |
| 6 | 🐛 [**Exercise 3: Plant a bug, watch CI catch it**](06-exercise-3-plant-a-bug-watch-ci.md) | 2 min |
| 7 | 🧹 [**Exercise 4: Fail the lint gate**](07-exercise-4-fail-the-lint-gate.md) | 1 min |
| 8 | 🔒 [**Bonus: Make the tick mandatory**](08-bonus-make-the-tick-mandatory.md) | 1 min |
| 9 | 🧯 [**Something went wrong?**](09-something-went-wrong.md) | 1 min |

<p align="center">
  <a href="01-the-cast.md"><b>▶️ Start with The cast</b></a>
</p>

## 🎯 What you learned

- How to stage a pipeline with `needs`
- How a `matrix` multiplies one job across versions
- How artifacts carry a build out of a runner
- How `paths`, `concurrency` and `permissions` keep a pipeline lean and safe
- What it feels like when CI catches a bug before a human does

---

<p align="center">
  <a href="../04-anatomy-of-a-pipeline/README.md">⬅️ Anatomy of a Pipeline</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="../index.md">📚 Chapter 2</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="../06-cheat-sheet-and-quiz/README.md"><b>Next: Cheat Sheet & Quiz ➡️</b></a>
</p>
