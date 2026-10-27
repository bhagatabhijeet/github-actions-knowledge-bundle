---
type: Tutorial
title: "Executing Shell Scripts in a Workflow: Try it yourself"
description: "This repository ships the script and a live workflow: scripts/ascii-script.sh and 04-shell-script.yml."
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
  <a href="README.md">📂 <b>Executing Shell Scripts in a Workflow</b></a> &nbsp;·&nbsp; Lesson 7 · Part 8 of 9 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# 🛠️ Try it yourself

This repository ships the script and a live workflow: [`scripts/ascii-script.sh`](../../scripts/ascii-script.sh) and [`04-shell-script.yml`](../../.github/workflows/04-shell-script.yml).

1. Open the **Actions** tab, pick **04 - Shell Script** and click **Run workflow**
2. Open **Execute the script**. The install output is folded under **Install cowsay**; the dragon and the file listing follow it
3. **Break it:** in a fork, remove the executable bit with `git update-index --chmod=-x scripts/ascii-script.sh` and push. Read the `Permission denied` error, then fix it by changing the step to `bash ./scripts/ascii-script.sh`
4. **Stretch:** make the script take the cow as an argument (`${1:-dragon}`) and pass `tux` from the workflow

---

<p align="center">
  <a href="07-inline-run-or-a-script-file.md">⬅️ Inline `run:` or a script file?</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="09-checkpoint.md"><b>Next: Checkpoint ➡️</b></a>
</p>
