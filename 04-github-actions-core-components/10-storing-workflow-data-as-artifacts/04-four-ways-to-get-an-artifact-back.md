---
type: Tutorial
title: "Storing Workflow Data as Artifacts: Four ways to get an artifact back"
description: "Downloading from another run:"
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
  <a href="README.md">📂 <b>Storing Workflow Data as Artifacts</b></a> &nbsp;·&nbsp; Lesson 10 · Part 4 of 10 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# 📥 Four ways to get an artifact back

| Who | How |
|---|---|
| 🔗 **A later job in the same run** | `actions/download-artifact` with `name` or `pattern` |
| 🌐 **You, in the browser** | Run → **Summary** → scroll to **Artifacts** → click the name to download a `.zip` |
| ⌨️ **You, in a terminal** | `gh run download <run-id> -n cow-gallery` or `gh run download <run-id> -p 'cow-*'` |
| 🔁 **Another workflow** | `download-artifact` with `run-id` and `github-token`, e.g. a deploy workflow fetching a build from CI |

Downloading from another run:

```yaml
permissions:
  actions: read
steps:
  - uses: actions/download-artifact@v8
    with:
      name: dist
      run-id: ${{ github.event.workflow_run.id }}   # e.g. from a workflow_run trigger
      github-token: ${{ secrets.GITHUB_TOKEN }}
```

---

<p align="center">
  <a href="03-names-are-unique-and-artifacts-are-immutable.md">⬅️ Names are unique and artifacts are immutable</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="05-keep-evidence-when-things-break.md"><b>Next: Keep evidence when things break ➡️</b></a>
</p>
