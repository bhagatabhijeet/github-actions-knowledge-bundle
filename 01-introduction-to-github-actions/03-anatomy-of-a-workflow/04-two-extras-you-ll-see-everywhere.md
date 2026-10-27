---
type: Tutorial
title: "Anatomy of a Workflow File: Two extras you'll see everywhere"
description: "Double curly braces ask GitHub to fill in a value before the step runs."
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
  <a href="README.md">📂 <b>Anatomy of a Workflow File</b></a> &nbsp;·&nbsp; Lesson 3 · Part 4 of 6 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# 🧠 Two extras you'll see everywhere

## `${{ }}` expressions

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

## `permissions`

Every run gets a temporary `GITHUB_TOKEN`. `permissions:` says how much it's allowed to do. Start minimal:

```yaml
permissions:
  contents: read
```

---

<p align="center">
  <a href="03-key-by-key.md">⬅️ Key by key</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="05-the-five-yaml-traps.md"><b>Next: The five YAML traps ➡️</b></a>
</p>
