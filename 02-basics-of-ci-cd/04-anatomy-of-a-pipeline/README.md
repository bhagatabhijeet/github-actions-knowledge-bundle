---
type: Tutorial
title: Anatomy of a Pipeline
description: The stages every pipeline shares - source, build, test, package, deploy - and exactly how each one maps onto GitHub Actions jobs, needs, matrices and artifacts.
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
  <b>Lesson 4 of 6</b> &nbsp;·&nbsp; ⏱️ 9 min read &nbsp;·&nbsp; 🟡 Builds on Chapter 1
</p>

# 🏭 Anatomy of a Pipeline

A **pipeline** is the automated path a change takes from "pushed" to "running in production". Tools differ, languages differ, but the stages are remarkably consistent.

<p align="center">
  <img src="../../assets/images/cicd-pipeline.svg" alt="Pipeline stages: commit, build, test, package, staging, production" width="100%">
</p>

## 🗺️ In this topic

7 subtopics, about 10 minutes in all. Read them in order, or jump to the one you need.

| # | Subtopic | Time |
|---|---|---|
| 1 | 🚉 [**The five stations**](01-the-five-stations.md) | 1 min |
| 2 | 🧩 [**Pipelines in GitHub Actions**](02-pipelines-in-github-actions.md) | 2 min |
| 3 | 🔀 [**Fan-out and fan-in**](03-fan-out-and-fan-in.md) | 2 min |
| 4 | 🧮 [**The matrix: one job, many variations**](04-the-matrix-one-job-many-variations.md) | 1 min |
| 5 | 🎒 [**Carrying things between stages**](05-carrying-things-between-stages.md) | 2 min |
| 6 | ⏱️ [**What makes a pipeline good?**](06-what-makes-a-pipeline-good.md) | 1 min |
| 7 | ✅ [**Checkpoint**](07-checkpoint.md) | 1 min |

<p align="center">
  <a href="01-the-five-stations.md"><b>▶️ Start with The five stations</b></a>
</p>

---

<p align="center">
  <a href="../03-delivery-vs-deployment/README.md">⬅️ Delivery vs Deployment</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="../index.md">📚 Chapter 2</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="../05-your-first-ci-pipeline/README.md"><b>Next: Your First CI Pipeline ➡️</b></a>
</p>
