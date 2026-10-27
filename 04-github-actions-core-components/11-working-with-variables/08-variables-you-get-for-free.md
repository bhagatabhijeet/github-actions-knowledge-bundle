---
type: Tutorial
title: "Working with Variables: Variables you get for free"
description: "Every job starts with default variables already set:"
tags: [github-actions, variables, env, vars, configuration-variables, github-env, hands-on]
status: stable
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-26T00:00:00Z }
sources:
  - id: gh-variables
    resource: https://docs.github.com/en/actions/concepts/workflows-and-actions/variables
    title: Variables
  - id: gh-variables-ref
    resource: https://docs.github.com/en/actions/reference/workflows-and-actions/variables
    title: Variables reference
  - id: gh-contexts
    resource: https://docs.github.com/en/actions/reference/workflows-and-actions/contexts
    title: Contexts reference
  - id: gh-workflow-commands
    resource: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-commands
    title: Workflow commands for GitHub Actions
---

<p align="center">
  <a href="README.md">📂 <b>Working with Variables</b></a> &nbsp;·&nbsp; Lesson 11 · Part 8 of 14 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# 🎁 Variables you get for free

Every job starts with default variables already set:

| Variable | Example value | Use it to... |
|---|---|---|
| `GITHUB_REPOSITORY` | `octo-org/dragon-web` | Build image names, API URLs |
| `GITHUB_REF_NAME` | `main` | Tag images by branch |
| `GITHUB_SHA` | `ffac537e6cbbf9...` | Tag images by commit |
| `GITHUB_ACTOR` | `octocat` | Say who triggered the run |
| `GITHUB_EVENT_NAME` | `push` | Behave differently per trigger |
| `GITHUB_RUN_NUMBER` | `42` | Build numbers that go up |
| `GITHUB_WORKSPACE` | `/home/runner/work/repo/repo` | Find the checked-out code |
| `RUNNER_OS` | `Linux`, `Windows`, `macOS` | Branch per OS in scripts |
| `CI` | `true` | Let tools know they're in CI |

Most have a matching context value, e.g. `${{ github.sha }}`, `${{ runner.os }}`. You **can't override** names that start with `GITHUB_` or `RUNNER_`.

---

<p align="center">
  <a href="07-inside-the-expression-language-and-its-contexts.md">⬅️ Inside `${{ }}`: the expression language and its contexts</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="09-setting-a-variable-while-the-job-runs.md"><b>Next: Setting a variable while the job runs ➡️</b></a>
</p>
