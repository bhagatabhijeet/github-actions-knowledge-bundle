---
type: Tutorial
title: Anatomy of a Workflow File
description: A line-by-line tour of workflow YAML - name, on, jobs, runs-on and steps - plus the YAML rules that trip up every beginner.
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
  <b>Lesson 3 of 5</b> &nbsp;·&nbsp; ⏱️ 9 min read &nbsp;·&nbsp; 🟢 Beginner
</p>

# 🔬 Anatomy of a Workflow File

You know the six concepts. Now let's see how they look on the page. By the end of this lesson, a workflow file will read like a sentence.

## 🦴 The skeleton

Every workflow answers four questions:

```yaml
name: Skeleton              # 🏷️ What is it called?

on: push                    # 🔔 WHEN does it run?

jobs:
  greet:
    runs-on: ubuntu-latest  # 🖥️ WHERE does it run?
    steps:                  # 👣 WHAT does it do?
      - run: echo "Hello from GitHub Actions"
```

📎 Copy it from [assets/snippets/workflow-skeleton.yml](../assets/snippets/workflow-skeleton.yml)

That's a complete, working workflow. Seven lines.

## 🗺️ The nesting map

Indentation in YAML *is* the structure. This is the shape hiding inside every workflow:

```text
workflow
├── name
├── on ─────────────── events
└── jobs
    ├── job-one
    │   ├── runs-on ── runner
    │   └── steps
    │       ├── step ─ uses (an action)
    │       └── step ─ run  (a command)
    └── job-two
        ├── needs ──── job-one
        ├── runs-on
        └── steps
```

## 🔍 Key by key

### 🏷️ `name`

```yaml
name: CI
```

The label shown in the Actions tab. Optional, but without it GitHub shows the file path, and nobody wants to read `.github/workflows/ci.yml` forty times.

### 🔔 `on`

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

### 📦 `jobs`

A map of job ids to job definitions. You choose the ids.

```yaml
jobs:
  build:            # 👈 job id: letters, numbers, - and _
    name: Build it  # optional pretty name
    runs-on: ubuntu-latest
    steps: [...]
```

### 🖥️ `runs-on`

```yaml
runs-on: ubuntu-latest     # or windows-latest, macos-latest
```

> [!NOTE]
> Reach for `ubuntu-latest` unless you have a reason not to. It starts fastest and is the cheapest per minute.

### 👣 `steps`

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

## 🧠 Two extras you'll see everywhere

### `${{ }}` expressions

Double curly braces ask GitHub to fill in a value before the step runs.

```yaml
- run: echo "Run number ${{ github.run_number }} by ${{ github.actor }}"
```

`github` is a **context**: a bag of facts about the current run. You'll meet others (`env`, `secrets`, `matrix`, `inputs`) throughout this guide.

> [!CAUTION]
> Never paste untrusted text (an issue title, a branch name, a form input) straight into a `run:` script with `${{ }}`. It is substituted *before* the shell runs, so a crafted value can inject commands. Pass it through `env:` instead:
>
> ```yaml
> - env:
>     TITLE: ${{ github.event.issue.title }}
>   run: echo "$TITLE"
> ```

### `permissions`

Every run gets a temporary `GITHUB_TOKEN`. `permissions:` says how much it's allowed to do. Start minimal:

```yaml
permissions:
  contents: read
```

## 🪤 The five YAML traps

Nine out of ten "my workflow won't start" problems are one of these.

| | Trap | ❌ Wrong | ✅ Right |
|---|---|---|---|
| 1 | **Tabs** | a tab character | spaces only (2 per level) |
| 2 | **Misaligned keys** | `steps:` deeper than `runs-on:` | siblings share a column |
| 3 | **Missing dash** | `steps:` then `run: ...` | `- run: ...` |
| 4 | **Versions as numbers** | `python-version: 3.10` (becomes `3.1`!) | `python-version: '3.10'` |
| 5 | **Wrong folder** | `.github/workflow/` | `.github/workflows/` |

> [!TIP]
> Trap 4 is famous. YAML reads `3.10` as the number three-point-one. Quote your versions and you'll never meet it.

## 🧪 Read it aloud

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

## 🎯 What you learned

- A workflow answers **what's it called, when, where, what**
- Indentation is structure; `jobs` contain `steps`
- A step either `uses` an action or `run`s a command
- `${{ }}` injects values; keep untrusted input out of `run:`
- Quote versions, use spaces, mind the dash

---

<p align="center">
  <a href="02-core-concepts.md">⬅️ The Six Core Concepts</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="index.md">📚 Chapter 1</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="04-your-first-workflow.md"><b>Next: Your First Workflow ➡️</b></a>
</p>
