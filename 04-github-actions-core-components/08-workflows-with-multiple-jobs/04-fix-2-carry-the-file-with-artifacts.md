---
type: Tutorial
title: "Workflows with Multiple Jobs: Fix 2: carry the file with artifacts"
description: "An artifact is a file or folder a job uploads to storage attached to the workflow run. Any later job in the same run can download it."
tags: [github-actions, jobs, needs, parallel, artifacts, hands-on]
status: stable
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-25T00:00:00Z }
sources:
  - id: gh-workflow-syntax
    resource: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
    title: Workflow syntax for GitHub Actions
  - id: gh-artifacts
    resource: https://docs.github.com/en/actions/tutorials/store-and-share-data
    title: Store and share data with workflow artifacts
  - id: upload-artifact
    resource: https://github.com/actions/upload-artifact
    title: actions/upload-artifact
  - id: download-artifact
    resource: https://github.com/actions/download-artifact
    title: actions/download-artifact
---

<p align="center">
  <a href="README.md">📂 <b>Workflows with Multiple Jobs</b></a> &nbsp;·&nbsp; Lesson 8 · Part 4 of 8 &nbsp;·&nbsp; ⏱️ 3 min
</p>

# 📦 Fix 2: carry the file with artifacts

An **artifact** is a file or folder a job uploads to storage attached to the workflow run. Any later job in the same run can download it.

```yaml
jobs:
  build_job:
    runs-on: ubuntu-latest
    steps:
      - name: Install cowsay
        run: sudo apt-get install -y -qq cowsay
      - name: Generate ASCII art
        run: cowsay -f dragon "Run for cover, I am a DRAGON....RAWR" > dragon.txt
      - name: Upload dragon.txt
        uses: actions/upload-artifact@v7      # 📤
        with:
          name: dragon-text-file
          path: dragon.txt
          retention-days: 3

  test_job:
    needs: build_job
    runs-on: ubuntu-latest
    steps:
      - name: Download dragon.txt
        uses: actions/download-artifact@v8    # 📥
        with:
          name: dragon-text-file
      - name: Test the file contains a dragon
        run: grep -i "dragon" dragon.txt

  deploy_job:
    needs: test_job
    runs-on: ubuntu-latest
    steps:
      - name: Download dragon.txt
        uses: actions/download-artifact@v8
        with:
          name: dragon-text-file
      - name: Deploy (print the file)
        run: cat dragon.txt
```

| Input | On | Meaning |
|---|---|---|
| `name` | upload and download | The label that links them. Must match exactly |
| `path` | upload | File, folder or glob to save, e.g. `dist/` or `reports/*.xml` |
| `path` | download | Where to put it. Defaults to the workspace root |
| `retention-days` | upload | How long GitHub keeps it. Default 90 days, or your repo's setting |

👉 [Lesson 10](../10-storing-workflow-data-as-artifacts/README.md) covers artifacts in depth: naming, patterns, retention and downloading from other runs.

> [!TIP]
> Artifacts also appear on the run's **Summary** page as downloadable zip files. That's handy for build outputs, test reports and screenshots, even after the runners are long gone.

---

<p align="center">
  <a href="03-fix-1-put-the-jobs-in-order.md">⬅️ Fix 1: put the jobs in order with `needs`</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="05-reading-the-job-graph.md"><b>Next: Reading the job graph ➡️</b></a>
</p>
