---
type: Tutorial
title: "Working with Variables: Checkpoint"
description: "Workflow, job and step. The most specific wins: step beats job beats workflow."
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
  <a href="README.md">📂 <b>Working with Variables</b></a> &nbsp;·&nbsp; Lesson 11 · Part 14 of 14 &nbsp;·&nbsp; ⏱️ 2 min
</p>

# ✅ Checkpoint

<details>
<summary><b>Name the three places you can put <code>env:</code>, and which wins.</b></summary>

<br>

Workflow, job and step. The most specific wins: step beats job beats workflow.

</details>

<details>
<summary><b><code>run: echo "${{ IMAGE_NAME }}"</code> fails with "Unrecognized named-value". Why, and what's the fix?</b></summary>

<br>

Inside `${{ }}` every value must start with a context, which tells GitHub where to look. Write `${{ env.IMAGE_NAME }}`, or `${{ vars.IMAGE_NAME }}` if it lives in Settings.

</details>

<details>
<summary><b>Why does <code>with: tags: $IMAGE_NAME</code> pass the literal text <code>$IMAGE_NAME</code>?</b></summary>

<br>

`with:` isn't run by a shell, so nothing expands `$IMAGE_NAME`. Use `${{ env.IMAGE_NAME }}`, which GitHub replaces before the step runs.

</details>

<details>
<summary><b>The team wants to change the registry without editing the workflow. Where should the value live?</b></summary>

<br>

In a configuration variable, read as `${{ vars.CONTAINER_REGISTRY }}`. Changing it in Settings takes effect on the next run, with no commit.

</details>

<details>
<summary><b>A repository variable and a <code>production</code> environment variable are both called <code>APP_URL</code>. Which does a job with <code>environment: production</code> get?</b></summary>

<br>

The environment's. Environment beats repository, which beats organisation.

</details>

<details>
<summary><b>Is a configuration variable a safe place for an API key?</b></summary>

<br>

No. Variables are plain text and appear in logs. Use a secret.

</details>

---

<p align="center">
  <a href="13-try-it-yourself.md">⬅️ Try it yourself</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md#-what-you-learned"><b>Wrap up: What you learned ➡️</b></a>
</p>
