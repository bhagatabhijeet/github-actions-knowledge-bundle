---
type: Tutorial
title: "Storing Workflow Data as Artifacts: Try it yourself"
description: "This repository ships a matrix-and-gallery workflow: 04-artifacts.yml."
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
  <a href="README.md">📂 <b>Storing Workflow Data as Artifacts</b></a> &nbsp;·&nbsp; Lesson 10 · Part 9 of 10 &nbsp;·&nbsp; ⏱️ 2 min
</p>

# 🛠️ Try it yourself

This repository ships a matrix-and-gallery workflow: [`04-artifacts.yml`](../../.github/workflows/04-artifacts.yml).

```mermaid
flowchart LR
    D1["🐉 draw: dragon"]:::blue --> A1["📦 cow-dragon"]:::purple
    D2["🐧 draw: tux"]:::blue --> A2["📦 cow-tux"]:::purple
    D3["🦕 draw: stegosaurus"]:::blue --> A3["📦 cow-stegosaurus"]:::purple
    A1 --> G["🖼️ gallery<br/>pattern: cow-*"]:::green
    A2 --> G
    A3 --> G
    G --> A4["📦 cow-gallery"]:::purple

    classDef blue fill:#0c1d3a,stroke:#58a6ff,color:#fff,stroke-width:2px
    classDef purple fill:#22123f,stroke:#bc8cff,color:#fff,stroke-width:2px
    classDef green fill:#0f2d17,stroke:#3fb950,color:#fff,stroke-width:2px
```

1. **Actions** tab → **04 - Artifacts** → **Run workflow**
2. Open a **draw** job and its **Show what was stored** step: the artifact's ID, URL and SHA-256 digest
3. On the **Summary** page, find **four** artifacts: three cows and the gallery. Download `cow-gallery` and unzip it
4. If you have the GitHub CLI: `gh run download <run-id> -p 'cow-*'` and look at the folders it creates
5. **Break it:** in a fork, change the upload name to a fixed `drawing`. Two of the three draw jobs fail with a "conflict" error
6. **Stretch:** set `merge-multiple: false` in the gallery job and see how the folder layout changes

---

<p align="center">
  <a href="08-artifact-cache-release-or-package.md">⬅️ Artifact, cache, release or package?</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="10-checkpoint.md"><b>Next: Checkpoint ➡️</b></a>
</p>
