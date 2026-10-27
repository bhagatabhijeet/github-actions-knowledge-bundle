---
type: Tutorial
title: "Your First CI Pipeline: Bonus: Make the tick mandatory"
description: "Right now a red pull request can still be merged. To close that door:"
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
  <a href="README.md">📂 <b>Your First CI Pipeline</b></a> &nbsp;·&nbsp; Lesson 5 · Part 8 of 9 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# 🔒 Bonus: Make the tick mandatory

Right now a red pull request can still be merged. To close that door:

1. **Settings → Rules → Rulesets → New branch ruleset**
2. Target the default branch
3. Enable **Require status checks to pass** and add the checks: `lint`, each `test (3.x)` variant, and `package`
4. Save

The **Merge** button is now disabled until CI is green. Your pipeline has become a gate.

---

<p align="center">
  <a href="07-exercise-4-fail-the-lint-gate.md">⬅️ Exercise 4: Fail the lint gate</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="09-something-went-wrong.md"><b>Next: Something went wrong? ➡️</b></a>
</p>
