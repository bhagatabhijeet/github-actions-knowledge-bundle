---
type: Tutorial
title: "Working with Variables: Setting a variable while the job runs"
description: "Some values only exist at runtime, like a version read from a file. Append NAME=value to the file in $GITHUBENV, and later steps in the same job can read it:"
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
  <a href="README.md">📂 <b>Working with Variables</b></a> &nbsp;·&nbsp; Lesson 11 · Part 9 of 14 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# ✍️ Setting a variable while the job runs

Some values only exist at runtime, like a version read from a file. Append `NAME=value` to the file in `$GITHUB_ENV`, and **later steps** in the same job can read it:

```yaml
- name: Read the version
  run: echo "APP_VERSION=$(cat VERSION)" >> "$GITHUB_ENV"

- name: Use it
  run: echo "Building version $APP_VERSION"
```

> [!NOTE]
> The step that writes it **can't** see it yet; only steps after it can. To pass a value to **another job**, use a job output, as in [Lesson 9](../09-executing-jobs-in-sequence/README.md).

---

<p align="center">
  <a href="08-variables-you-get-for-free.md">⬅️ Variables you get for free</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="10-configuration-variables-values-that-live-in-settings.md"><b>Next: Configuration variables: values that live in Settings ➡️</b></a>
</p>
