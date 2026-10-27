---
type: Tutorial
title: "Anatomy of a Pipeline: The five stations"
description: "Each stage is a quality gate. A change only moves right if the gate opens. A failure anywhere stops the line."
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
  <a href="README.md">📂 <b>Anatomy of a Pipeline</b></a> &nbsp;·&nbsp; Lesson 4 · Part 1 of 7 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# 🚉 The five stations

| | Stage | Question | Output |
|---|---|---|---|
| 1️⃣ | 📥 **Source** | What changed? | A commit |
| 2️⃣ | 🏗️ **Build** | Does it assemble? | Compiled code, installed dependencies |
| 3️⃣ | 🧪 **Test** | Does it behave? | A pass or fail verdict |
| 4️⃣ | 📦 **Package** | What exactly are we shipping? | One versioned artifact |
| 5️⃣ | 🚀 **Deploy** | Is it in front of users? | A running release |

Each stage is a **quality gate**. A change only moves right if the gate opens. A failure anywhere stops the line.

---

<p align="center">
  <a href="README.md">⬅️ Overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="02-pipelines-in-github-actions.md"><b>Next: Pipelines in GitHub Actions ➡️</b></a>
</p>
