---
type: Tutorial
title: "Workflows with Multiple Jobs: Artifacts, outputs or cache?"
description: "Choose between artifacts, job outputs and the cache to pass data between jobs or between runs."
tags: [github-actions, jobs, needs, parallel, artifacts, hands-on]
status: stable
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-26T00:00:00Z }
sources:
  - id: gh-workflow-syntax
    resource: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
    title: Workflow syntax for GitHub Actions
  - id: gh-artifacts
    resource: https://docs.github.com/en/actions/tutorials/store-and-share-data
    title: Store and share data with workflow artifacts
  - id: upload-artifact
    resource: https://github.com/actions/upload-artifact
    title: actions/upload-artifact
  - id: download-artifact
    resource: https://github.com/actions/download-artifact
    title: actions/download-artifact
---

<p align="center">
  <a href="README.md">📂 <b>Workflows with Multiple Jobs</b></a> &nbsp;·&nbsp; Lesson 8 · Part 6 of 8 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# 🔀 Artifacts, outputs or cache?

Three ways to pass something from one job to another, or from one run to the next:

| | Use for | Lives for | Example |
|---|---|---|---|
| 📦 **Artifact** | Files produced by this run | The run, plus retention days | `dist/`, `dragon.txt`, test reports |
| 🏷️ **Job output** | Small strings | This run | A version number, an image tag |
| 🗄️ **Cache** | Files that rarely change, to save time | Across runs, up to 7 days unused | `node_modules`, `~/.cache/pip` |

A job output looks like this:

```yaml
jobs:
  build_job:
    runs-on: ubuntu-latest
    outputs:
      version: ${{ steps.v.outputs.version }}
    steps:
      - id: v
        run: echo "version=1.4.$GITHUB_RUN_NUMBER" >> "$GITHUB_OUTPUT"

  deploy_job:
    needs: build_job
    runs-on: ubuntu-latest
    steps:
      - run: echo "Deploying ${{ needs.build_job.outputs.version }}"
```

---

<p align="center">
  <a href="05-reading-the-job-graph.md">⬅️ Reading the job graph</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="07-try-it-yourself.md"><b>Next: Try it yourself ➡️</b></a>
</p>
