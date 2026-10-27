---
type: Tutorial
title: "Storing Workflow Data as Artifacts: Checkpoint"
description: "The first upload succeeds and the others fail, because artifact names must be unique in a run. Include a matrix value in the name, such as results-${{ matrix.os }}."
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
  <a href="README.md">📂 <b>Storing Workflow Data as Artifacts</b></a> &nbsp;·&nbsp; Lesson 10 · Part 10 of 10 &nbsp;·&nbsp; ⏱️ 2 min
</p>

# ✅ Checkpoint

<details>
<summary><b>A matrix of four jobs all upload an artifact named <code>results</code>. What happens?</b></summary>

<br>

The first upload succeeds and the others fail, because artifact names must be unique in a run. Include a matrix value in the name, such as `results-${{ matrix.os }}`.

</details>

<details>
<summary><b>The upload step is green, but the artifact isn't on the Summary page. What's the likely cause, and the fix?</b></summary>

<br>

`path` matched nothing, and the default `if-no-files-found: warn` only printed a warning. Fix the path, and set `if-no-files-found: error` so it can't happen silently.

</details>

<details>
<summary><b>You want to save Playwright screenshots, but only when the tests fail. How?</b></summary>

<br>

Put `if: ${{ failure() }}` on the upload step, after the test step.

</details>

<details>
<summary><b>Should <code>node_modules</code> be an artifact or a cache?</b></summary>

<br>

A cache. It exists to make future runs faster, not to keep this run's output.

</details>

---

<p align="center">
  <a href="09-try-it-yourself.md">⬅️ Try it yourself</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md#-what-you-learned"><b>Wrap up: What you learned ➡️</b></a>
</p>
