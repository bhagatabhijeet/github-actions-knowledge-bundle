---
type: Tutorial
title: "Anatomy of a Workflow File: Key by key"
description: "The label shown in the Actions tab. Optional, but without it GitHub shows the file path, and nobody wants to read .github/workflows/ci.yml forty times."
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
  <a href="README.md">📂 <b>Anatomy of a Workflow File</b></a> &nbsp;·&nbsp; Lesson 3 · Part 3 of 6 &nbsp;·&nbsp; ⏱️ 2 min
</p>

# 🔍 Key by key

## 🏷️ `name`

```yaml
name: CI
```

The label shown in the Actions tab. Optional, but without it GitHub shows the file path, and nobody wants to read `.github/workflows/ci.yml` forty times.

## 🔔 `on`

It grows with your needs:

```yaml
on: push                        # one event

on: [push, pull_request]        # several events

on:                             # events with filters
  push:
    branches: [main]
    paths: ['src/**']
  workflow_dispatch:
```

> [!TIP]
> Always add `workflow_dispatch:` while you're learning. It gives you a **Run workflow** button, so you can re-run without inventing a fake commit.

## 📦 `jobs`

A map of job ids to job definitions. You choose the ids.

```yaml
jobs:
  build:            # 👈 job id: letters, numbers, - and _
    name: Build it  # optional pretty name
    runs-on: ubuntu-latest
    steps: [...]
```

## 🖥️ `runs-on`

```yaml
runs-on: ubuntu-latest     # or windows-latest, macos-latest
```

> [!NOTE]
> Reach for `ubuntu-latest` unless you have a reason not to. It starts fastest and is the cheapest per minute.

## 👣 `steps`

An ordered list. Each item starts with a dash.

```yaml
steps:
  - name: Check out the code        # optional label for the logs
    uses: actions/checkout@v7       # an action...

  - name: Install Python
    uses: actions/setup-python@v7
    with:                           # ...with inputs
      python-version: '3.13'

  - name: Run tests
    run: python -m unittest discover -v   # a command

  - name: Many commands
    run: |                          # the | starts a multi-line script
      echo "one"
      echo "two"
```

| Step key | Purpose |
|---|---|
| `name` | Label in the logs |
| `uses` | Run an action |
| `with` | Inputs for that action |
| `run` | Run shell commands |
| `env` | Environment variables for this step |
| `if` | Only run when a condition is true |

---

<p align="center">
  <a href="02-the-nesting-map.md">⬅️ The nesting map</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="04-two-extras-you-ll-see-everywhere.md"><b>Next: Two extras you'll see everywhere ➡️</b></a>
</p>
