---
type: Tutorial
title: "Working with Variables: `$VAR` or `${{ env.VAR }}`?"
description: "There are two ways to read a variable, and they work at different moments:"
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
  <a href="README.md">📂 <b>Working with Variables</b></a> &nbsp;·&nbsp; Lesson 11 · Part 6 of 14 &nbsp;·&nbsp; ⏱️ 2 min
</p>

# 💲 `$VAR` or `${{ env.VAR }}`?

There are two ways to read a variable, and they work at different moments:

| | `$IMAGE_NAME` | `${{ env.IMAGE_NAME }}` |
|---|---|---|
| Read by | The **shell**, on the runner | **GitHub**, before the step is sent to the runner |
| Works in | `run:` only | `run:`, `with:`, `name:`, step `if:` and more |
| On Windows (PowerShell) | `$env:IMAGE_NAME` | Same expression, any shell |
| Sees `$GITHUB_ENV` values from earlier steps | ✅ | ✅ |

```yaml
- name: Build ${{ env.IMAGE_NAME }}        # expression: works in a name
  uses: docker/build-push-action@v7
  with:
    tags: ${{ env.CONTAINER_REGISTRY }}/${{ env.IMAGE_NAME }}:latest   # with: needs the expression
```

> [!TIP]
> **Inside `run:`, prefer `$VAR`.** The expression is pasted into your script as plain text before it runs, so a value containing quotes or `;` can break the command or, if it came from user input such as a PR title, inject one. Pass untrusted values through `env:` and read them as `$VAR`.

> [!WARNING]
> **`env` doesn't work everywhere.** It isn't available in `runs-on:` or in a job-level `if:`, because GitHub decides those before the job's environment exists. Use `vars`, `inputs` or `github` there instead.

---

<p align="center">
  <a href="05-which-one-wins.md">⬅️ Which one wins?</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="07-inside-the-expression-language-and-its-contexts.md"><b>Next: Inside `${{ }}`: the expression language and its contexts ➡️</b></a>
</p>
