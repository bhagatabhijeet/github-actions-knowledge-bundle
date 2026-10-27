---
type: Tutorial
title: "Storing Workflow Data as Artifacts: Retention and storage"
description: "How long artifacts live by default, where to change retention, and how deleting artifacts frees storage."
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
  - id: gh-remove-artifacts
    resource: https://docs.github.com/en/actions/how-tos/manage-workflow-runs/remove-workflow-artifacts
    title: Removing workflow artifacts
  - id: gh-limits
    resource: https://docs.github.com/en/actions/reference/limits
    title: Actions limits
---

<p align="center">
  <a href="README.md">📂 <b>Storing Workflow Data as Artifacts</b></a> &nbsp;·&nbsp; Lesson 10 · Part 6 of 10 &nbsp;·&nbsp; ⏱️ 2 min
</p>

# ⏳ Retention and storage

| Setting | Where | Range |
|---|---|---|
| Per upload | `retention-days:` | 1 up to the repository's maximum |
| Repository default | **Settings → Actions → General → Artifact and log retention** | Up to 90 days on public repos, up to 400 on private ones |
| Organisation or enterprise | Org or enterprise settings | Sets the ceiling for every repository |

> [!NOTE]
> Expired artifacts are deleted automatically. You can delete one early from the run's Summary page (🗑️ next to its name) or through the REST API, which frees the storage at once.

> [!NOTE]
> **📘 From the GitHub docs:** by default GitHub keeps build logs and artifacts for **90 days**. A deleted artifact **can't be restored**, and deleting it needs write access. Deleting a workflow run also deletes all of its artifacts. ([Removing workflow artifacts](https://docs.github.com/en/actions/how-tos/manage-workflow-runs/remove-workflow-artifacts))

> [!NOTE]
> **📘 From the GitHub docs:** artifact storage depends on your plan. It starts at 500 MB on GitHub Free and goes up to 50 GB on GitHub Enterprise Cloud. Short `retention-days` on bulky uploads keep you under it. ([Actions limits](https://docs.github.com/en/actions/reference/limits))

---

<p align="center">
  <a href="05-keep-evidence-when-things-break.md">⬅️ Keep evidence when things break</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="07-security-assume-anyone-can-read-it.md"><b>Next: Security: assume anyone can read it ➡️</b></a>
</p>
