---
type: Tutorial
title: "Your First CI Pipeline: Exercise 1: Go green"
description: "In your fork, open Actions → 02 - CI Basics"
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
  <a href="README.md">📂 <b>Your First CI Pipeline</b></a> &nbsp;·&nbsp; Lesson 5 · Part 4 of 9 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# ▶️ Exercise 1: Go green

1. In your fork, open **Actions → 02 - CI Basics**
2. Click **Run workflow**, then the green button
3. Click into the run and watch the graph fill in from left to right

When it finishes you'll see five ✅ jobs. Expand **test (3.13) → Run unit tests**:

```text
test_blank_name_falls_back_to_world ... ok
test_defaults_to_world ... ok
test_greets_by_name ... ok
test_trims_whitespace ... ok
test_shouts ... ok

Ran 5 tests in 0.001s

OK
```

---

<p align="center">
  <a href="03-the-workflow-piece-by-piece.md">⬅️ The workflow, piece by piece</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="05-exercise-2-collect-your-artifact.md"><b>Next: Exercise 2: Collect your artifact ➡️</b></a>
</p>
