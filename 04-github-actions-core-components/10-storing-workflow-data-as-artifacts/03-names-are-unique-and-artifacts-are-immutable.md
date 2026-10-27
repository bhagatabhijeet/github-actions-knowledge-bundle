---
type: Tutorial
title: "Storing Workflow Data as Artifacts: Names are unique and artifacts are immutable"
description: "Since upload-artifact@v4, an artifact can't be changed after upload, and two uploads with the same name in one run fail. This bites hardest in a matrix:"
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
  <a href="README.md">📂 <b>Storing Workflow Data as Artifacts</b></a> &nbsp;·&nbsp; Lesson 10 · Part 3 of 10 &nbsp;·&nbsp; ⏱️ 2 min
</p>

# 🏷️ Names are unique and artifacts are immutable

Since `upload-artifact@v4`, an artifact **can't be changed after upload**, and two uploads with the same name in one run **fail**. This bites hardest in a matrix:

```yaml
strategy:
  matrix:
    cow: [dragon, tux, stegosaurus]
steps:
  - uses: actions/upload-artifact@v7
    with:
      name: drawing                    # ❌ three jobs, one name: two of them fail
      path: art/
```

```yaml
  - uses: actions/upload-artifact@v7
    with:
      name: cow-${{ matrix.cow }}      # ✅ cow-dragon, cow-tux, cow-stegosaurus
      path: art/
```

Then collect them in a later job with a **pattern**:

```yaml
- uses: actions/download-artifact@v8
  with:
    pattern: cow-*         # every artifact whose name matches
    merge-multiple: true   # put all their files in one folder
    path: gallery
```

| Download input | Default | What it does |
|---|---|---|
| `name` | *(all)* | One artifact by name. Leave out `name` and `pattern` to download **every** artifact in the run |
| `pattern` | | A glob over artifact names, e.g. `cow-*` |
| `merge-multiple` | `false` | `false`: one subfolder per artifact. `true`: everything in one folder |
| `path` | Workspace root | Where to put the files |
| `run-id` + `github-token` | This run | Download from a **different** run (needs `actions: read`) |

---

<p align="center">
  <a href="02-uploading-the-inputs-worth-knowing.md">⬅️ Uploading: the inputs worth knowing</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="04-four-ways-to-get-an-artifact-back.md"><b>Next: Four ways to get an artifact back ➡️</b></a>
</p>
