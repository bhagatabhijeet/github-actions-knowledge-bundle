---
type: Tutorial
title: "Storing Workflow Data as Artifacts: Uploading: the inputs worth knowing"
description: "The upload-artifact inputs worth knowing, from path patterns and retention-days to if-no-files-found, and the outputs it returns."
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
  <a href="README.md">📂 <b>Storing Workflow Data as Artifacts</b></a> &nbsp;·&nbsp; Lesson 10 · Part 2 of 10 &nbsp;·&nbsp; ⏱️ 2 min
</p>

# 📤 Uploading: the inputs worth knowing

```yaml
- name: Upload test results
  uses: actions/upload-artifact@v7
  with:
    name: test-results               # what people and jobs will ask for
    path: |                          # one path per line; globs allowed
      reports/**/*.xml
      coverage/
      !coverage/**/*.tmp             # ! excludes
    if-no-files-found: error         # fail loudly if nothing matched
    retention-days: 7                # 1-90, can't exceed the repo setting
    compression-level: 6             # 0 = none (fast), 9 = smallest
```

| Input | Default | What it does |
|---|---|---|
| `name` | `artifact` | The artifact's name. **Must be unique within the run** |
| `path` | *(required)* | Files, folders or globs, one per line. Start a line with `!` to exclude |
| `if-no-files-found` | `warn` | `warn`, `error` or `ignore` when `path` matches nothing |
| `retention-days` | Repo setting | How long to keep it |
| `compression-level` | `6` | `0` for already-compressed files like images or `.zip`, `9` for big text files |
| `overwrite` | `false` | `true` replaces an existing artifact with the same name in this run |
| `include-hidden-files` | `false` | Include dot-files such as `.env.example`. Off by default so secrets in hidden files don't leak |

It also returns **outputs** you can use in later steps:

| Output | Example use |
|---|---|
| `artifact-id` | Call the REST API to fetch or delete it |
| `artifact-url` | Post a direct download link in a PR comment or the job summary |
| `artifact-digest` | A SHA-256 checksum, to prove the file wasn't changed |

> [!TIP]
> **Make `if-no-files-found: error` your habit for anything important.** The default only warns, so a typo in `path` gives you a green run with an empty or missing artifact.

---

<p align="center">
  <a href="01-what-an-artifact-is.md">⬅️ What an artifact is</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="03-names-are-unique-and-artifacts-are-immutable.md"><b>Next: Names are unique and artifacts are immutable ➡️</b></a>
</p>
