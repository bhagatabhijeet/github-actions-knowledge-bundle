---
type: Tutorial
title: "Storing Workflow Data as Artifacts: Retention and storage"
description: "Expired artifacts are deleted automatically. You can delete one early from the run's Summary page (🗑️ next to its name) or through the REST API, which frees the storage at once."
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
  <a href="README.md">📂 <b>Storing Workflow Data as Artifacts</b></a> &nbsp;·&nbsp; Lesson 10 · Part 6 of 10 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# ⏳ Retention and storage

| Setting | Where | Range |
|---|---|---|
| Per upload | `retention-days:` | 1 up to the repository's maximum |
| Repository default | **Settings → Actions → General → Artifact and log retention** | Up to 90 days on public repos, up to 400 on private ones |
| Organisation or enterprise | Org or enterprise settings | Sets the ceiling for every repository |

> [!NOTE]
> Expired artifacts are deleted automatically. You can delete one early from the run's Summary page (🗑️ next to its name) or through the REST API, which frees the storage at once.

---

<p align="center">
  <a href="05-keep-evidence-when-things-break.md">⬅️ Keep evidence when things break</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="07-security-assume-anyone-can-read-it.md"><b>Next: Security: assume anyone can read it ➡️</b></a>
</p>
