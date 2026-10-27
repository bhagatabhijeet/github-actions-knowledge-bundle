---
type: Tutorial
title: "Executing Jobs in Sequence with needs: Checkpoint"
description: "It's skipped too. A job runs only if everything it needs succeeded, and skipped isn't success."
tags: [github-actions, jobs, needs, sequence, if, status-functions, outputs, hands-on]
status: stable
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-26T00:00:00Z }
sources:
  - id: gh-workflow-syntax
    resource: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
    title: Workflow syntax for GitHub Actions
  - id: gh-expressions
    resource: https://docs.github.com/en/actions/reference/workflows-and-actions/expressions
    title: Evaluate expressions in workflows and actions
  - id: gh-contexts
    resource: https://docs.github.com/en/actions/reference/workflows-and-actions/contexts
    title: Contexts reference
---

<p align="center">
  <a href="README.md">📂 <b>Executing Jobs in Sequence with needs</b></a> &nbsp;·&nbsp; Lesson 9 · Part 9 of 9 &nbsp;·&nbsp; ⏱️ 2 min
</p>

# ✅ Checkpoint

<details>
<summary><b><code>deploy</code> has <code>needs: test</code>, and <code>test</code> was skipped. What happens to <code>deploy</code>?</b></summary>

<br>

It's skipped too. A job runs only if everything it needs **succeeded**, and skipped isn't success.

</details>

<details>
<summary><b>Build takes 2 minutes, then lint (1 min) and tests (4 min) both need build, and deploy needs both. Roughly how long is the run?</b></summary>

<br>

About 2 + 4 + deploy time. Lint and tests run side by side after build, so the longest branch (tests) decides. Lint adds nothing.

</details>

<details>
<summary><b>Your summary job should run after failures, but not if someone cancels the run. Which <code>if:</code>?</b></summary>

<br>

`if: ${{ !cancelled() }}`. `always()` would also run after a cancel.

</details>

<details>
<summary><b><code>deploy</code> has <code>needs: test</code> and prints <code>needs.build.outputs.version</code>, but gets an empty string. Why?</b></summary>

<br>

Outputs are only visible from jobs listed directly in `needs:`. Change it to `needs: [build, test]`.

</details>

---

<p align="center">
  <a href="08-try-it-yourself.md">⬅️ Try it yourself</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md#-what-you-learned"><b>Wrap up: What you learned ➡️</b></a>
</p>
