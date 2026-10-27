---
type: Tutorial
title: "Workflows with Multiple Jobs: Try it yourself"
description: "This repository ships the finished three-job workflow: 04-multiple-jobs.yml."
tags: [github-actions, jobs, needs, parallel, artifacts, hands-on]
status: stable
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-25T00:00:00Z }
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
  <a href="README.md">📂 <b>Workflows with Multiple Jobs</b></a> &nbsp;·&nbsp; Lesson 8 · Part 7 of 8 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# 🛠️ Try it yourself

This repository ships the finished three-job workflow: [`04-multiple-jobs.yml`](../../.github/workflows/04-multiple-jobs.yml).

1. Open the **Actions** tab, pick **04 - Multiple Jobs** and click **Run workflow**
2. Watch the graph: `build_job` runs while the other two wait ⚪
3. When it finishes, scroll the Summary to **Artifacts** and download `dragon-text-file`
4. **Break it (order):** in a fork, delete the two `needs:` lines. All three jobs start together; test and deploy fail
5. **Break it (files):** put `needs:` back but delete the download steps. Jobs wait correctly, and still fail with `No such file or directory`
6. **Stretch:** add a `lint_job` that also `needs: build_job`, and make `deploy_job` need `[test_job, lint_job]`

---

<p align="center">
  <a href="06-artifacts-outputs-or-cache.md">⬅️ Artifacts, outputs or cache?</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="08-checkpoint.md"><b>Next: Checkpoint ➡️</b></a>
</p>
