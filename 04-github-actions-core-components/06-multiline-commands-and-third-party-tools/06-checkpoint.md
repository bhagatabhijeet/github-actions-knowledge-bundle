---
type: Tutorial
title: "Multi-line Commands and Third-Party Tools: Checkpoint"
description: "The workspace root. Each step starts a new shell, so the cd from the previous step is gone. Use working-directory:, or put both commands in one multi-line step."
tags: [github-actions, run, multi-line, yaml, shell, apt-get, third-party, hands-on]
status: stable
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-25T00:00:00Z }
sources:
  - id: gh-workflow-syntax
    resource: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
    title: Workflow syntax for GitHub Actions
  - id: gh-runner-images
    resource: https://github.com/actions/runner-images
    title: GitHub Actions runner images
  - id: yaml-spec
    resource: https://yaml.org/spec/1.2.2/#81-block-scalar-styles
    title: YAML 1.2 block scalar styles
---

<p align="center">
  <a href="README.md">📂 <b>Multi-line Commands and Third-Party Tools</b></a> &nbsp;·&nbsp; Lesson 6 · Part 6 of 6 &nbsp;·&nbsp; ⏱️ 2 min
</p>

# ✅ Checkpoint

<details>
<summary><b>A step runs <code>cd sample-app</code> and the next step runs <code>ls</code>. Which folder does <code>ls</code> list?</b></summary>

<br>

The workspace root. Each step starts a new shell, so the `cd` from the previous step is gone. Use `working-directory:`, or put both commands in one multi-line step.

</details>

<details>
<summary><b>Line 2 of a 4-line <code>run: |</code> block fails on Ubuntu. Do lines 3 and 4 run?</b></summary>

<br>

No. Bash runs with `-e`, so the script stops at the first failing command and the step is marked as failed.

</details>

<details>
<summary><b>You wrote a three-line <code>run: &gt;</code> block, but the commands ran as one garbled line. Why?</b></summary>

<br>

`>` folds lines into one, joined by spaces. Use `|` to keep each line a separate command.

</details>

<details>
<summary><b>You installed a tool with <code>apt-get</code> yesterday. Is it still there in today's run?</b></summary>

<br>

No. Each job gets a fresh runner, so the install must be in the workflow every time. Cache it if it's slow.

</details>

---

<p align="center">
  <a href="05-try-it-yourself.md">⬅️ Try it yourself</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md#-what-you-learned"><b>Wrap up: What you learned ➡️</b></a>
</p>
