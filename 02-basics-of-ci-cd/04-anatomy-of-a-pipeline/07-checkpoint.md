---
type: Tutorial
title: "Anatomy of a Pipeline: Checkpoint"
description: "Make each stage a job and give B needs: A."
tags: [ci-cd, pipeline, stages, artifacts, matrix, needs, caching]
status: stable
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-07T00:00:00Z }
sources:
  - id: gh-syntax
    resource: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
    title: Workflow syntax for GitHub Actions
  - id: gh-artifacts
    resource: https://docs.github.com/en/actions/concepts/workflows-and-actions/workflow-artifacts
    title: Workflow artifacts
  - id: gh-cache
    resource: https://docs.github.com/en/actions/concepts/workflows-and-actions/dependency-caching
    title: Dependency caching
---

<p align="center">
  <a href="README.md">📂 <b>Anatomy of a Pipeline</b></a> &nbsp;·&nbsp; Lesson 4 · Part 7 of 7 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# ✅ Checkpoint

<details>
<summary><b>How do you express "stage B runs after stage A" in GitHub Actions?</b></summary>

<br>

Make each stage a job and give B `needs: A`.

</details>

<details>
<summary><b>A matrix has <code>python-version: ['3.12', '3.13']</code> and <code>os: [ubuntu-latest, windows-latest, macos-latest]</code>. How many jobs run?</b></summary>

<br>

Six: 2 versions × 3 operating systems.

</details>

<details>
<summary><b>You want to stop re-downloading 400 MB of dependencies on every run. Artifact or cache?</b></summary>

<br>

Cache. It's a speed-up, not an output you need to keep.

</details>

---

<p align="center">
  <a href="06-what-makes-a-pipeline-good.md">⬅️ What makes a pipeline good?</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="../05-your-first-ci-pipeline/README.md"><b>Next topic ➡️</b></a>
</p>
