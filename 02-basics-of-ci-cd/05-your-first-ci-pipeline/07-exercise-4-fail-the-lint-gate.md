---
type: Tutorial
title: "Your First CI Pipeline: Exercise 4: Fail the lint gate"
description: "Add an unused import to the top of core.py and push:"
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
  <a href="README.md">📂 <b>Your First CI Pipeline</b></a> &nbsp;·&nbsp; Lesson 5 · Part 7 of 9 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# 🧹 Exercise 4: Fail the lint gate

Add an unused import to the top of `core.py` and push:

```python
import os
```

This time `lint` fails with rule **F401** (`os` imported but unused), and **`test` and `package` are both skipped**. The pipeline stopped at the first, cheapest gate, in seconds. That's *fail fast*. Remove the line to recover.

---

<p align="center">
  <a href="06-exercise-3-plant-a-bug-watch-ci.md">⬅️ Exercise 3: Plant a bug, watch CI catch it</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="08-bonus-make-the-tick-mandatory.md"><b>Next: Bonus: Make the tick mandatory ➡️</b></a>
</p>
