---
type: Tutorial
title: "Storing Workflow Data as Artifacts: Keep evidence when things break"
description: "Upload logs, screenshots and reports with if: failure() so you still have evidence after a run breaks."
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
  <a href="README.md">📂 <b>Storing Workflow Data as Artifacts</b></a> &nbsp;·&nbsp; Lesson 10 · Part 5 of 10 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# 📸 Keep evidence when things break

The most valuable artifacts are often the ones you only need on a bad day:

```yaml
- name: Run end-to-end tests
  run: npx playwright test

- name: Upload screenshots and traces
  if: ${{ failure() }}                 # only when a step above failed
  uses: actions/upload-artifact@v7
  with:
    name: e2e-evidence-${{ github.run_attempt }}
    path: test-results/
    retention-days: 14
```

Adding `run_attempt` to the name stops a **re-run** from clashing with the first attempt's artifact.

---

<p align="center">
  <a href="04-four-ways-to-get-an-artifact-back.md">⬅️ Four ways to get an artifact back</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="06-retention-and-storage.md"><b>Next: Retention and storage ➡️</b></a>
</p>
