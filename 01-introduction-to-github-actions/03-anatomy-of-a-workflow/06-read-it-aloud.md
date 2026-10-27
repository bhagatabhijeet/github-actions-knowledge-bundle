---
type: Tutorial
title: "Anatomy of a Workflow File: Read it aloud"
description: "Here's a real workflow. Before opening the answer, try saying what it does in plain English."
tags: [github-actions, yaml, workflow-syntax, beginner]
status: stable
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-07T00:00:00Z }
sources:
  - id: gh-syntax
    resource: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
    title: Workflow syntax for GitHub Actions
  - id: gh-contexts
    resource: https://docs.github.com/en/actions/reference/workflows-and-actions/contexts
    title: Contexts reference
---

<p align="center">
  <a href="README.md">📂 <b>Anatomy of a Workflow File</b></a> &nbsp;·&nbsp; Lesson 3 · Part 6 of 6 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# 🧪 Read it aloud

Here's a real workflow. Before opening the answer, try saying what it does in plain English.

```yaml
name: Tests

on:
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v7
      - uses: actions/setup-python@v7
        with:
          python-version: '3.13'
      - run: python -m unittest discover -v
```

<details>
<summary><b>Reveal the translation</b></summary>

<br>

*"Whenever someone opens or updates a pull request targeting `main`, start a fresh Ubuntu machine, download the repository onto it, install Python 3.13, and run the unit tests. Show a green tick on the pull request if they pass and a red cross if they don't."*

If you got that, you can read workflows. 🎉

</details>

---

<p align="center">
  <a href="05-the-five-yaml-traps.md">⬅️ The five YAML traps</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md#-what-you-learned"><b>Wrap up: What you learned ➡️</b></a>
</p>
