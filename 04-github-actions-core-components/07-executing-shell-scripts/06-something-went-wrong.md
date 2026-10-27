---
type: Tutorial
title: "Executing Shell Scripts in a Workflow: Something went wrong?"
description: "Look at the bottom-right of your editor. If it says CRLF, a .sh file will break on a Linux runner. Click it and switch to LF. This repository's .gitattributes forces LF for every .sh file, so Git fixes it for you on..."
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
  <a href="README.md">📂 <b>Executing Shell Scripts in a Workflow</b></a> &nbsp;·&nbsp; Lesson 7 · Part 6 of 9 &nbsp;·&nbsp; ⏱️ 2 min
</p>

# 🧯 Something went wrong?

| Error in the log | Cause | Fix |
|---|---|---|
| `./scripts/ascii-script.sh: No such file or directory` | No checkout step, or the wrong path | Check out first. Paths are relative to the repository root |
| `./scripts/ascii-script.sh: Permission denied` | The executable bit wasn't committed. Common when the file was made on Windows or in the web editor | `git update-index --chmod=+x scripts/ascii-script.sh`, commit, push. Or run it with `bash` |
| `/usr/bin/env: 'bash\r': No such file or directory` or `$'\r': command not found` | The file has Windows **CRLF** line endings | Save as LF, and add `*.sh text eol=lf` to `.gitattributes` |
| The run is ✅ green but the output is wrong | Missing `set -e`, so failures were ignored | Add `set -euo pipefail` at the top |

> [!TIP]
> Look at the bottom-right of your editor. If it says **CRLF**, a `.sh` file will break on a Linux runner. Click it and switch to **LF**. This repository's [`.gitattributes`](../../.gitattributes) forces LF for every `.sh` file, so Git fixes it for you on commit.

---

<p align="center">
  <a href="05-three-ways-to-run-a-script.md">⬅️ Three ways to run a script</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="07-inline-run-or-a-script-file.md"><b>Next: Inline `run:` or a script file? ➡️</b></a>
</p>
