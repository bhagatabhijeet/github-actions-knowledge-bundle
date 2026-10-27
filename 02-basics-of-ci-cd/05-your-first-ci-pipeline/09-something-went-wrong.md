---
type: Tutorial
title: "Your First CI Pipeline: Something went wrong?"
description: "Something went wrong?, part 9 of 9 of Your First CI Pipeline."
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
  <a href="README.md">📂 <b>Your First CI Pipeline</b></a> &nbsp;·&nbsp; Lesson 5 · Part 9 of 9 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# 🧯 Something went wrong?

| Symptom | Likely cause |
|---|---|
| Pipeline didn't start on push | Your change wasn't under `sample-app/`, so `paths` filtered it out |
| PR shows no checks | The PR targets the original repo, not your fork |
| `No file matched to requirements-dev.txt` | `cache-dependency-path` is relative to the repo root |
| `ModuleNotFoundError: greeter` | A `run:` step isn't in `sample-app/`; check `working-directory` |
| Artifact upload finds no files | `path:` must be relative to the repo root |

---

<p align="center">
  <a href="08-bonus-make-the-tick-mandatory.md">⬅️ Bonus: Make the tick mandatory</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md#-what-you-learned"><b>Wrap up: What you learned ➡️</b></a>
</p>
