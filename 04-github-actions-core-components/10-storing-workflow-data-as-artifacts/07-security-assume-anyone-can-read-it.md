---
type: Tutorial
title: "Storing Workflow Data as Artifacts: Security: assume anyone can read it"
description: "Never put secrets in an artifact. Everyone with read access can download it, which on a public repository means the whole internet. Watch out for .env files, kubeconfigs, cloud credential files and debug dumps that..."
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
  <a href="README.md">📂 <b>Storing Workflow Data as Artifacts</b></a> &nbsp;·&nbsp; Lesson 10 · Part 7 of 10 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# 🔐 Security: assume anyone can read it

> [!WARNING]
> **Never put secrets in an artifact.** Everyone with read access can download it, which on a public repository means the whole internet. Watch out for `.env` files, kubeconfigs, cloud credential files and debug dumps that print environment variables. Keep `include-hidden-files` off unless you have checked what the hidden files contain.

---

<p align="center">
  <a href="06-retention-and-storage.md">⬅️ Retention and storage</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="08-artifact-cache-release-or-package.md"><b>Next: Artifact, cache, release or package? ➡️</b></a>
</p>
