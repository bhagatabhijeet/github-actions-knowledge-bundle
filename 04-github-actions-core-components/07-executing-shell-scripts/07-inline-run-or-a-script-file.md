---
type: Tutorial
title: "Executing Shell Scripts in a Workflow: Inline `run:` or a script file?"
description: "Inline `run:` or a script file?, part 7 of 9 of Executing Shell Scripts in a Workflow."
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
  <a href="README.md">📂 <b>Executing Shell Scripts in a Workflow</b></a> &nbsp;·&nbsp; Lesson 7 · Part 7 of 9 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# ⚖️ Inline `run:` or a script file?

| Keep it inline when... | Move it to a script when... |
|---|---|
| It's one to five short lines | It's long, or has loops, functions or `if`s |
| It's specific to this one workflow | Several workflows, or developers, run the same thing |
| You want each command as its own log section | You want to test it locally, or lint it with **ShellCheck** |

---

<p align="center">
  <a href="06-something-went-wrong.md">⬅️ Something went wrong?</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="08-try-it-yourself.md"><b>Next: Try it yourself ➡️</b></a>
</p>
