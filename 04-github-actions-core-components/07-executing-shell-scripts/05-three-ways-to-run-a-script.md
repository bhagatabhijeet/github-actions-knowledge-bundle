---
type: Tutorial
title: "Executing Shell Scripts in a Workflow: Three ways to run a script"
description: "Scripts can take arguments and read environment variables, just like on your laptop:"
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
  <a href="README.md">📂 <b>Executing Shell Scripts in a Workflow</b></a> &nbsp;·&nbsp; Lesson 7 · Part 5 of 9 &nbsp;·&nbsp; ⏱️ 2 min
</p>

# 🔀 Three ways to run a script

| Command | Needs the executable bit? | Needs a shebang? | When to use it |
|---|---|---|---|
| `./scripts/ascii-script.sh` | ✅ Yes | ✅ Yes | The normal way. The script decides its own interpreter |
| `bash scripts/ascii-script.sh` | ❌ No | ❌ No | Quick fix when the executable bit is missing |
| `run: \|` with `source scripts/env.sh` | ❌ No | ❌ No | To load variables or functions into the step's shell |

Scripts can take **arguments** and read **environment variables**, just like on your laptop:

```yaml
- name: Execute the script
  env:
    MESSAGE: "Run for cover!"            # read as $MESSAGE inside the script
  run: ./scripts/ascii-script.sh dragon  # read as $1 inside the script
```

Other interpreters work the same way. Change the shebang or call the interpreter: `python scripts/report.py`, `pwsh scripts/deploy.ps1`, `node scripts/build.mjs`.

---

<p align="center">
  <a href="04-what-each-line-of-the-script-does.md">⬅️ What each line of the script does</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="06-something-went-wrong.md"><b>Next: Something went wrong? ➡️</b></a>
</p>
