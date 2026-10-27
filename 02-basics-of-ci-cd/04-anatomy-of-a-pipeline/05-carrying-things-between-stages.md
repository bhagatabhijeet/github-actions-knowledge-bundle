---
type: Tutorial
title: "Anatomy of a Pipeline: Carrying things between stages"
description: "Remember the rule from Chapter 1: every job gets a fresh, empty runner. So how does the thing you built in package reach deploy?"
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
---

<p align="center">
  <a href="README.md">📂 <b>Anatomy of a Pipeline</b></a> &nbsp;·&nbsp; Lesson 4 · Part 5 of 7 &nbsp;·&nbsp; ⏱️ 2 min
</p>

# 🎒 Carrying things between stages

Remember the rule from Chapter 1: **every job gets a fresh, empty runner**. So how does the thing you built in `package` reach `deploy`?

| | Mechanism | Carries | Lives for |
|---|---|---|---|
| 📦 | **Artifacts** | Files (builds, reports, logs) | Days; downloadable from the run page |
| 🏷️ | **Job outputs** | Small strings (a version, a URL) | The workflow run |
| ⚡ | **Cache** | Dependencies you'd otherwise re-download | Across runs, until evicted |

```yaml
  package:
    steps:
      - run: tar -czf app.tar.gz src/
      - uses: actions/upload-artifact@v7
        with:
          name: app
          path: app.tar.gz

  deploy:
    needs: package
    steps:
      - uses: actions/download-artifact@v8
        with:
          name: app
      - run: ./deploy.sh app.tar.gz
```

This is **build once, deploy many** in practice: `deploy` receives the exact bytes `package` produced.

> [!WARNING]
> **Artifact or cache?** They look similar and are often confused.
> - An **artifact** is an *output* of your pipeline. You want to keep it or pass it on.
> - A **cache** is a *speed-up*. If it disappeared, the pipeline would still work, just slower.

> [!NOTE]
> **📘 From the GitHub docs:** Artifacts and caches "cannot be used interchangeably". Use a **cache** for files that rarely change between runs, like downloaded dependencies. Use an **artifact** for files a job produces that you want to keep after the run or hand to another job. ([Workflow artifacts](https://docs.github.com/en/actions/concepts/workflows-and-actions/workflow-artifacts))

---

<p align="center">
  <a href="04-the-matrix-one-job-many-variations.md">⬅️ The matrix: one job, many variations</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="06-what-makes-a-pipeline-good.md"><b>Next: What makes a pipeline good? ➡️</b></a>
</p>
