---
type: Tutorial
title: "Storing Workflow Data as Artifacts: Artifact, cache, release or package?"
description: "Choose between an artifact, the dependency cache, a release asset or a package for the file you want to keep."
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
  - id: gh-limits
    resource: https://docs.github.com/en/actions/reference/limits
    title: Actions limits
---

<p align="center">
  <a href="README.md">📂 <b>Storing Workflow Data as Artifacts</b></a> &nbsp;·&nbsp; Lesson 10 · Part 8 of 10 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# 🔀 Artifact, cache, release or package?

| | 📦 Artifact | 🗄️ Cache | 🏷️ Release asset | 📚 Package |
|---|---|---|---|---|
| **Purpose** | Output of **this run** | Speed up **future runs** | Ship a version to users | Publish for other projects to install |
| **Typical content** | Build output, reports, logs | Dependencies (`node_modules`, pip) | Installers, binaries | npm, Maven, container images |
| **Lives** | Retention days | 7 days unused, size-capped | Until you delete it | Until you delete it |
| **Downloaded by** | Jobs, people, CLI | Only `actions/cache` | Anyone who can see the release | Package managers |

> [!NOTE]
> **📘 From the GitHub docs:** the cache is capped at **10 GB per repository** on every plan, and each repository can upload at most 200 cache entries per minute. That's another reason to keep build output in artifacts and only dependencies in the cache. ([Actions limits](https://docs.github.com/en/actions/reference/limits))

---

<p align="center">
  <a href="07-security-assume-anyone-can-read-it.md">⬅️ Security: assume anyone can read it</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="09-try-it-yourself.md"><b>Next: Try it yourself ➡️</b></a>
</p>
