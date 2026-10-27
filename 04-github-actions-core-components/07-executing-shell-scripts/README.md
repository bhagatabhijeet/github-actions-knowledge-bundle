---
type: Tutorial
title: Executing Shell Scripts in a Workflow (Hands-On)
description: Move a workflow's commands into a shell script in the repository and run it in one step - the shebang, set -euo pipefail, the executable bit, LF line endings, passing arguments, and the errors you'll meet on the way.
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
  <b>Lesson 7 of 14</b> &nbsp;·&nbsp; ⏱️ 18 min &nbsp;·&nbsp; 🛠️ Hands-on
</p>

# 🐚 Executing Shell Scripts in a Workflow

In the last lesson the dragon took a step per command. That's fine for five lines. When a job grows to fifty, the YAML gets hard to read, and you can't run any of it on your own machine. The fix is to put the commands in a **shell script** in your repository and have the workflow run it.

## 🗺️ In this topic

9 subtopics, about 16 minutes in all. Read them in order, or jump to the one you need.

| # | Subtopic | Time |
|---|---|---|
| 1 | 🧩 [**Where we left off**](01-where-we-left-off.md) | 1 min |
| 2 | 🔄 [**Move the commands into a script**](02-move-the-commands-into-a-script.md) | 2 min |
| 3 | 👀 [**Watching the script run**](03-watching-the-script-run.md) | 3 min |
| 4 | 🔬 [**What each line of the script does**](04-what-each-line-of-the-script-does.md) | 2 min |
| 5 | 🔀 [**Three ways to run a script**](05-three-ways-to-run-a-script.md) | 2 min |
| 6 | 🧯 [**Something went wrong?**](06-something-went-wrong.md) | 2 min |
| 7 | ⚖️ [**Inline `run:` or a script file?**](07-inline-run-or-a-script-file.md) | 1 min |
| 8 | 🛠️ [**Try it yourself**](08-try-it-yourself.md) | 1 min |
| 9 | ✅ [**Checkpoint**](09-checkpoint.md) | 2 min |

<p align="center">
  <a href="01-where-we-left-off.md"><b>▶️ Start with Where we left off</b></a>
</p>

## 🎯 What you learned

- Put long or reused logic in a **script in the repo**; keep the workflow to **checkout + run**
- Start every bash script with a **shebang** and **`set -euo pipefail`**
- Commit the **executable bit**, or call the script with **`bash`**
- Keep **LF line endings** for `.sh` files, enforced by **`.gitattributes`**
- Pass data with **arguments** and **`env:`**; tidy logs with **`::group::`**

---

<p align="center">
  <a href="../06-multiline-commands-and-third-party-tools/README.md">⬅️ Multi-line Commands</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="../index.md">📚 Chapter 4</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="../08-workflows-with-multiple-jobs/README.md"><b>Next: Multiple Jobs ➡️</b></a>
</p>
