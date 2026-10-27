---
type: Tutorial
title: Storing Workflow Data as Artifacts (Hands-On)
description: Keep files after the runner is gone - what artifacts are, every upload-artifact input worth knowing, unique names and immutability, downloading by pattern, from the browser, the CLI or another run, retention and storage, and when to use cache, releases or packages instead.
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
  <b>Lesson 10 of 14</b> &nbsp;·&nbsp; ⏱️ 16 min &nbsp;·&nbsp; 🛠️ Hands-on
</p>

# 📦 Storing Workflow Data as Artifacts

A runner is wiped the moment its job ends. Your build output, your test report, the screenshot of the failing page: all gone, unless you **store them as artifacts**. In [Lesson 8](../08-workflows-with-multiple-jobs/README.md) you used an artifact to hand one file to the next job. This lesson covers everything else: what to keep, how to name it, how long it lives and how to get it back.

## 🗺️ In this topic

10 subtopics, about 15 minutes in all. Read them in order, or jump to the one you need.

| # | Subtopic | Time |
|---|---|---|
| 1 | 💡 [**What an artifact is**](01-what-an-artifact-is.md) | 2 min |
| 2 | 📤 [**Uploading: the inputs worth knowing**](02-uploading-the-inputs-worth-knowing.md) | 2 min |
| 3 | 🏷️ [**Names are unique and artifacts are immutable**](03-names-are-unique-and-artifacts-are-immutable.md) | 2 min |
| 4 | 📥 [**Four ways to get an artifact back**](04-four-ways-to-get-an-artifact-back.md) | 1 min |
| 5 | 📸 [**Keep evidence when things break**](05-keep-evidence-when-things-break.md) | 1 min |
| 6 | ⏳ [**Retention and storage**](06-retention-and-storage.md) | 1 min |
| 7 | 🔐 [**Security: assume anyone can read it**](07-security-assume-anyone-can-read-it.md) | 1 min |
| 8 | 🔀 [**Artifact, cache, release or package?**](08-artifact-cache-release-or-package.md) | 1 min |
| 9 | 🛠️ [**Try it yourself**](09-try-it-yourself.md) | 2 min |
| 10 | ✅ [**Checkpoint**](10-checkpoint.md) | 2 min |

<p align="center">
  <a href="01-what-an-artifact-is.md"><b>▶️ Start with What an artifact is</b></a>
</p>

## 🎯 What you learned

- An **artifact** is a zipped set of files attached to a run, kept after the runner is gone
- Choose files with **`path`** (globs, `!` excludes) and fail loudly with **`if-no-files-found: error`**
- Names are **unique per run** and artifacts are **immutable**: in a matrix, put the matrix value in the name
- Collect many with **`pattern`** and **`merge-multiple`**; fetch from other runs with **`run-id`**
- Get them back from a **job**, the **browser**, **`gh run download`** or **another workflow**
- Set **`retention-days`**, keep **secrets** out, and use **cache** for dependencies

---

<p align="center">
  <a href="../09-executing-jobs-in-sequence/README.md">⬅️ Jobs in Sequence</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="../index.md">📚 Chapter 4</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="../11-working-with-variables/README.md"><b>Next: Working with Variables ➡️</b></a>
</p>
