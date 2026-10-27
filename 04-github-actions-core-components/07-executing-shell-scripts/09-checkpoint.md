---
type: Tutorial
title: "Executing Shell Scripts in a Workflow: Checkpoint"
description: "Most likely the actions/checkout step. The runner starts empty, so the script isn't there until the repository is checked out."
tags: [github-actions, shell, bash, scripts, chmod, line-endings, hands-on]
status: stable
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-25T00:00:00Z }
sources:
  - id: gh-workflow-syntax
    resource: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
    title: Workflow syntax for GitHub Actions
  - id: gh-workflow-commands
    resource: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-commands
    title: Workflow commands for GitHub Actions
  - id: git-attributes
    resource: https://git-scm.com/docs/gitattributes
    title: gitattributes
---

<p align="center">
  <a href="README.md">📂 <b>Executing Shell Scripts in a Workflow</b></a> &nbsp;·&nbsp; Lesson 7 · Part 9 of 9 &nbsp;·&nbsp; ⏱️ 2 min
</p>

# ✅ Checkpoint

<details>
<summary><b>The script step fails with <code>No such file or directory</code>, but the file is in the repo. What's missing?</b></summary>

<br>

Most likely the `actions/checkout` step. The runner starts empty, so the script isn't there until the repository is checked out.

</details>

<details>
<summary><b>What does <code>Permission denied</code> mean when running <code>./script.sh</code>, and what are two fixes?</b></summary>

<br>

The file isn't marked executable in Git. Either commit the bit with `git update-index --chmod=+x script.sh`, or run it as `bash script.sh`, which doesn't need the bit.

</details>

<details>
<summary><b>A script's second command fails, yet the step is green. Why?</b></summary>

<br>

Without `set -e`, bash carries on after a failure, and the step's result comes from the last command only. Start scripts with `set -euo pipefail`.

</details>

---

<p align="center">
  <a href="08-try-it-yourself.md">⬅️ Try it yourself</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md#-what-you-learned"><b>Wrap up: What you learned ➡️</b></a>
</p>
