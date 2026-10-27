---
type: Tutorial
title: "Storing Workflow Data as Artifacts: What an artifact is"
description: "An artifact is a set of files a job uploads to storage attached to its workflow run. It outlives the runner, and it can be downloaded by later jobs, by people, by the CLI, or by other workflows."
tags: [github-actions, artifacts, upload-artifact, download-artifact, retention, storage, hands-on]
status: stable
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-26T00:00:00Z }
sources:
  - id: gh-artifacts
    resource: https://docs.github.com/en/actions/tutorials/store-and-share-data
    title: Store and share data with workflow artifacts
  - id: upload-artifact
    resource: https://github.com/actions/upload-artifact
    title: actions/upload-artifact
  - id: download-artifact
    resource: https://github.com/actions/download-artifact
    title: actions/download-artifact
  - id: gh-run-download
    resource: https://cli.github.com/manual/gh_run_download
    title: gh run download
---

<p align="center">
  <a href="README.md">📂 <b>Storing Workflow Data as Artifacts</b></a> &nbsp;·&nbsp; Lesson 10 · Part 1 of 10 &nbsp;·&nbsp; ⏱️ 2 min
</p>

# 💡 What an artifact is

> **An artifact is a set of files a job uploads to storage attached to its workflow run.** It outlives the runner, and it can be downloaded by later jobs, by people, by the CLI, or by other workflows.

<p align="center">
  <img src="../../assets/images/artifact-lifecycle.svg" alt="Files on a runner are zipped and uploaded to artifact storage attached to the run, where they stay for 1 to 90 days after the runner is destroyed. From there they can be downloaded by a later job, from the browser, with the gh CLI, or by another workflow run. Good things to keep: build outputs, test reports, coverage, failure screenshots, logs" width="100%">
</p>

| | Fact |
|---|---|
| 🗜️ **Format** | Zipped on upload. Downloaded from the browser as a `.zip` |
| 🔗 **Belongs to** | One workflow run. Listed at the bottom of the run's **Summary** page |
| ⏳ **Lifetime** | 90 days by default, or what your repository or organisation sets. Lower it per upload with `retention-days` |
| 👀 **Who can download** | Anyone with **read** access to the repository. On a public repo, that's everyone |
| 💰 **Cost** | Counts toward your account's GitHub Actions **storage** quota until it expires or is deleted |

---

<p align="center">
  <a href="README.md">⬅️ Overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="02-uploading-the-inputs-worth-knowing.md"><b>Next: Uploading: the inputs worth knowing ➡️</b></a>
</p>
