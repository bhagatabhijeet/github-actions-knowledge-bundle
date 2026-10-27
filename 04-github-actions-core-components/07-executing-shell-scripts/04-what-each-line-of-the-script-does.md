---
type: Tutorial
title: "Executing Shell Scripts in a Workflow: What each line of the script does"
description: "A script that hides its failures makes a green run that's lying. Without set -e, a script carries on after errors, and only the last command's exit code decides whether the step passes. Always start with set -euo..."
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
  <a href="README.md">📂 <b>Executing Shell Scripts in a Workflow</b></a> &nbsp;·&nbsp; Lesson 7 · Part 4 of 9 &nbsp;·&nbsp; ⏱️ 2 min
</p>

# 🔬 What each line of the script does

| Line | Why it's there |
|---|---|
| `#!/usr/bin/env bash` | The **shebang**. Tells the OS to run this file with bash, wherever bash is installed |
| `set -e` | Stop at the first command that fails, just like a `run:` step does |
| `set -u` | Treat an unset variable as an error, instead of silently using an empty string |
| `set -o pipefail` | Fail if *any* command in a pipe fails, not just the last one |
| `echo "::group::…"` / `"::endgroup::"` | **Workflow commands**: fold the noisy install output into one collapsible section in the log |
| `> /dev/null` | Hide `grep`'s output; only its exit code matters here |

> [!IMPORTANT]
> **A script that hides its failures makes a green run that's lying.** Without `set -e`, a script carries on after errors, and only the *last* command's exit code decides whether the step passes. Always start with `set -euo pipefail`.

---

<p align="center">
  <a href="03-watching-the-script-run.md">⬅️ Watching the script run</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="05-three-ways-to-run-a-script.md"><b>Next: Three ways to run a script ➡️</b></a>
</p>
