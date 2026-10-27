---
type: Tutorial
title: "Working with Variables: Common mistakes"
description: "The variable slips learners make most: wrong syntax for the place, wrong scope, $GITHUB_ENV timing and secrets stored as variables."
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
  <a href="README.md">📂 <b>Working with Variables</b></a> &nbsp;·&nbsp; Lesson 11 · Part 12 of 14 &nbsp;·&nbsp; ⏱️ 2 min
</p>

# 🪤 Common mistakes

| Mistake | What you see | Fix |
|---|---|---|
| `${{ IMAGE_NAME }}` without a context | `Unrecognized named-value: 'IMAGE_NAME'` | Add the context: `${{ env.IMAGE_NAME }}` |
| Reading `steps.build.outputs.x` from a step with no `id: build` | Empty value | Give the step `id: build` |
| Variable set in one job, read in another | Empty value | Move it to workflow `env`, or pass a job output |
| `${{ vars.NAME }}` before the variable exists | Empty value, no error | Create it in Settings, or add a `\|\| 'default'` fallback |
| Using `$VAR` in `with:` | The literal text `$VAR` is passed | Use `${{ env.VAR }}` in `with:` |
| `env.X` in `runs-on:` or a job `if:` | Workflow error | Use `vars.X` there |
| Reading a `$GITHUB_ENV` value in the same step | Empty | Read it in a later step |
| Putting a password in `env:` or `vars` | It's visible to everyone with read access | Use `secrets` |

---

<p align="center">
  <a href="11-env-or-vars-and-secrets.md">⬅️ `env` or `vars`? (and `secrets`)</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="13-try-it-yourself.md"><b>Next: Try it yourself ➡️</b></a>
</p>
