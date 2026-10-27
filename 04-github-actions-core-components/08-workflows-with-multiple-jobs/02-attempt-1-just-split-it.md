---
type: Tutorial
title: "Workflows with Multiple Jobs: Attempt 1: just split it"
description: "Push it, and two of the three jobs fail within seconds:"
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
  <a href="README.md">📂 <b>Workflows with Multiple Jobs</b></a> &nbsp;·&nbsp; Lesson 8 · Part 2 of 8 &nbsp;·&nbsp; ⏱️ 2 min
</p>

# 💥 Attempt 1: just split it

```yaml
name: Generate ASCII Artwork

on: push

jobs:
  build_job:
    runs-on: ubuntu-latest
    steps:
      - name: Install cowsay
        run: sudo apt-get install -y cowsay
      - name: Generate ASCII art
        run: cowsay -f dragon "Run for cover, I am a DRAGON....RAWR" > dragon.txt

  test_job:
    runs-on: ubuntu-latest
    steps:
      - name: Test the file contains a dragon
        run: grep -i "dragon" dragon.txt

  deploy_job:
    runs-on: ubuntu-latest
    steps:
      - name: Deploy (print the file)
        run: cat dragon.txt
```

Push it, and two of the three jobs fail **within seconds**:

<p align="center">
  <img src="../../assets/images/multiple-jobs-needs.svg" alt="Without needs, build, test and deploy start together on runners A, B and C; test and deploy fail because dragon.txt is only on runner A. With needs and artifacts, build uploads dragon.txt, test downloads and checks it, deploy downloads and prints it" width="100%">
</p>

Two separate problems caused this:

| | Problem | Rule |
|---|---|---|
| ⏱️ | `test_job` and `deploy_job` didn't **wait** for `build_job` | **Jobs run in parallel by default** |
| 📂 | Even if they had waited, `dragon.txt` was on a **different machine** | **Each job gets its own fresh runner. Jobs share no files** |

---

<p align="center">
  <a href="01-why-split-into-jobs.md">⬅️ Why split into jobs?</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="03-fix-1-put-the-jobs-in-order.md"><b>Next: Fix 1: put the jobs in order with `needs` ➡️</b></a>
</p>
