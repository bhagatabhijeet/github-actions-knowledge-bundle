---
type: Tutorial
title: "Anatomy of a Pipeline: What makes a pipeline good?"
description: "Five qualities of a good pipeline (fast, reliable, repeatable, visible, secure) with a rule of thumb for each."
tags: [ci-cd, pipeline, stages, artifacts, matrix, needs, caching]
status: stable
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-26T00:00:00Z }
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
  - id: gh-secure-use
    resource: https://docs.github.com/en/actions/reference/security/secure-use
    title: Secure use reference
---

<p align="center">
  <a href="README.md">📂 <b>Anatomy of a Pipeline</b></a> &nbsp;·&nbsp; Lesson 4 · Part 6 of 7 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# ⏱️ What makes a pipeline good?

| | Quality | Rule of thumb |
|---|---|---|
| ⚡ | **Fast** | Feedback in under ten minutes |
| 🎯 | **Reliable** | Fails only when the code is wrong; flaky tests get fixed or removed |
| 🔁 | **Repeatable** | Same commit, same result, every time |
| 👀 | **Visible** | Anyone can see what ran and why it failed |
| 🔒 | **Secure** | Minimal permissions; secrets never printed |

> [!NOTE]
> **📘 From the GitHub docs:** For the 🔒 row, GitHub recommends giving the `GITHUB_TOKEN` the minimum permissions it needs: read-only by default, raised per job only where required.
>
> ```yaml
> permissions:
>   contents: read
> ```
>
> ([Secure use reference](https://docs.github.com/en/actions/reference/security/secure-use))

---

<p align="center">
  <a href="05-carrying-things-between-stages.md">⬅️ Carrying things between stages</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="07-checkpoint.md"><b>Next: Checkpoint ➡️</b></a>
</p>
