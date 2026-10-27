---
type: Tutorial
title: "Your First CI Pipeline: Exercise 2: Collect your artifact"
description: "Scroll to the bottom of the run's Summary page. Under Artifacts, click greeter to download it. Inside is a .tar.gz named after your commit."
resource: /.github/workflows/02-ci-basics.yml
tags: [ci-cd, hands-on, pipeline, matrix, artifacts, python, pull-requests]
status: stable
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-26T00:00:00Z }
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
  - id: gh-limits
    resource: https://docs.github.com/en/actions/reference/limits
    title: Actions limits
---

<p align="center">
  <a href="README.md">📂 <b>Your First CI Pipeline</b></a> &nbsp;·&nbsp; Lesson 5 · Part 5 of 9 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# 🎁 Exercise 2: Collect your artifact

Scroll to the bottom of the run's **Summary** page. Under **Artifacts**, click **greeter** to download it. Inside is a `.tar.gz` named after your commit.

You just produced a traceable, versioned build without touching your own machine. In a real pipeline, that is the file a deploy job would ship.

> [!NOTE]
> **📘 From the GitHub docs:** Artifact storage has a plan limit: 500 MB on Free, 1 GB on Pro, 2 GB on Team and 50 GB on Enterprise Cloud. GitHub Support can't raise these limits, so upload what you need, not your whole workspace. ([Actions limits](https://docs.github.com/en/actions/reference/limits))

---

<p align="center">
  <a href="04-exercise-1-go-green.md">⬅️ Exercise 1: Go green</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="06-exercise-3-plant-a-bug-watch-ci.md"><b>Next: Exercise 3: Plant a bug, watch CI catch it ➡️</b></a>
</p>
