---
type: Tutorial
title: "Continuous Integration: How it maps to GitHub Actions"
description: "You already know the pieces from Chapter 1. CI is just a particular way of arranging them."
tags: [ci-cd, continuous-integration, testing, linting, pull-requests]
status: stable
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-07T00:00:00Z }
sources:
  - id: fowler-ci
    resource: https://martinfowler.com/articles/continuousIntegration.html
    title: Continuous Integration
    author: Martin Fowler
  - id: gh-ci
    resource: https://docs.github.com/en/actions/get-started/continuous-integration
    title: Continuous integration (GitHub Docs)
  - id: gh-protection
    resource: https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches
    title: About protected branches
---

<p align="center">
  <a href="README.md">📂 <b>Continuous Integration</b></a> &nbsp;·&nbsp; Lesson 2 · Part 7 of 8 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# 🧩 How it maps to GitHub Actions

You already know the pieces from Chapter 1. CI is just a particular way of arranging them.

| CI idea | GitHub Actions feature |
|---|---|
| "On every change" | `on: [push, pull_request]` |
| "In a clean environment" | A fresh runner per job |
| "Build and test" | `steps` with `run:` |
| "Fail fast" | `needs:` to order jobs |
| "On every version we support" | `strategy.matrix` |
| "Block bad merges" | Required status checks |

A minimal CI workflow is only this:

```yaml
name: CI

on:
  push:
    branches: [main]
  pull_request:

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

Fourteen lines stand between you and "nobody can merge broken code".

---

<p align="center">
  <a href="06-the-five-habits-of-ci.md">⬅️ The five habits of CI</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="08-checkpoint.md"><b>Next: Checkpoint ➡️</b></a>
</p>
