---
type: Tutorial
title: "Your First CI Pipeline: The workflow, piece by piece"
description: "The cheapest check goes first. cache: pip saves downloaded packages between runs, keyed on the requirements file."
resource: /.github/workflows/02-ci-basics.yml
tags: [ci-cd, hands-on, pipeline, matrix, artifacts, python, pull-requests]
status: stable
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-07T00:00:00Z }
sources:
  - id: gh-python
    resource: https://docs.github.com/en/actions/tutorials/build-and-test-code/python
    title: Building and testing Python
  - id: gh-artifacts
    resource: https://docs.github.com/en/actions/tutorials/store-and-share-data
    title: Store and share data with workflow artifacts
  - id: gh-concurrency
    resource: https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/control-workflow-concurrency
    title: Control the concurrency of workflows and jobs
---

<p align="center">
  <a href="README.md">📂 <b>Your First CI Pipeline</b></a> &nbsp;·&nbsp; Lesson 5 · Part 3 of 9 &nbsp;·&nbsp; ⏱️ 3 min
</p>

# 📄 The workflow, piece by piece

## 🔔 Part 1: When it runs

```yaml
name: 02 - CI Basics

on:
  push:
    branches: [main]
    paths:
      - sample-app/**
      - .github/workflows/02-ci-basics.yml
  pull_request:
    paths:
      - sample-app/**
      - .github/workflows/02-ci-basics.yml
  workflow_dispatch:
```

| Trigger | Why |
|---|---|
| `pull_request` | Verify a change **before** it merges |
| `push` to `main` | Verify the result **after** it merges |
| `paths` | Skip the pipeline when only docs changed |
| `workflow_dispatch` | A manual button, for experimenting |

## 🛡️ Part 2: Ground rules

```yaml
permissions:
  contents: read

concurrency:
  group: ci-${{ github.ref }}
  cancel-in-progress: true

defaults:
  run:
    working-directory: sample-app
```

| Key | Effect |
|---|---|
| `permissions` | The run can read the repo and nothing more |
| `concurrency` | Push twice quickly and the older run on that branch is cancelled. No wasted minutes |
| `defaults.run.working-directory` | Every `run:` step starts inside `sample-app/` |

## 🧹 Part 3: Stage one, lint

```yaml
jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v7

      - uses: actions/setup-python@v7
        with:
          python-version: '3.13'
          cache: pip
          cache-dependency-path: sample-app/requirements-dev.txt

      - name: Install dev tools
        run: python -m pip install -r requirements-dev.txt

      - name: Lint
        run: ruff check .
```

The cheapest check goes first. `cache: pip` saves downloaded packages between runs, keyed on the requirements file.

## 🧪 Part 4: Stage two, test on three Pythons

```yaml
  test:
    needs: lint
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ['3.12', '3.13', '3.14']
    steps:
      - uses: actions/checkout@v7

      - uses: actions/setup-python@v7
        with:
          python-version: ${{ matrix.python-version }}

      - name: Run unit tests
        run: python -m unittest discover -v
```

`needs: lint` is the gate. The `matrix` multiplies this one job into three.

## 📦 Part 5: Stage three, package

```yaml
  package:
    needs: test
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v7

      - name: Build the artifact
        run: |
          mkdir -p dist
          tar -czf "dist/greeter-${GITHUB_SHA::7}.tar.gz" greeter
          ls -lh dist

      - name: Upload the artifact
        uses: actions/upload-artifact@v7
        with:
          name: greeter
          path: sample-app/dist/
          retention-days: 7
```

The archive is named after the commit (`greeter-8f3a1c2.tar.gz`), so you always know exactly which code is inside.

> [!WARNING]
> **A subtle one.** `working-directory` applies to `run:` steps only. Inputs to actions, like `path:` here, are relative to the repository root. That's why it says `sample-app/dist/` and not `dist/`.

---

<p align="center">
  <a href="02-the-pipeline-you-re-about-to-run.md">⬅️ The pipeline you're about to run</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="04-exercise-1-go-green.md"><b>Next: Exercise 1: Go green ➡️</b></a>
</p>
