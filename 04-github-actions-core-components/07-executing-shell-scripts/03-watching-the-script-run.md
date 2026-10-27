---
type: Tutorial
title: "Executing Shell Scripts in a Workflow: Watching the script run"
description: "Push the change and follow the script's output live in the run log, with grouped sections for the noisy parts."
tags: [github-actions, shell, bash, scripts, chmod, line-endings, hands-on]
status: stable
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-26T00:00:00Z }
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
  <a href="README.md">📂 <b>Executing Shell Scripts in a Workflow</b></a> &nbsp;·&nbsp; Lesson 7 · Part 3 of 9 &nbsp;·&nbsp; ⏱️ 3 min
</p>

# 👀 Watching the script run

Push the change and open the run. Here's a run whose commit message was *"added permissions"*, the commit that set the executable bit, caught while the script is still running:

```text
🟡 added permissions #3                        [ Cancel workflow ]

   ascii_job · Started 27s ago
   ✅ Set up job                      2s
   ✅ Checkout Repo                   5s
   ✅ List Repo Files                 0s
   🟡 Executing Shell Script         21s   ← running now
   ⚪ Post Checkout Repo                   ← waiting
```

| What you see | What it means |
|---|---|
| **added permissions #3** | The run is named after the commit message. `#3` is this workflow's third run |
| 🟡 next to the run, the job and a step | In progress. The step's timer keeps counting until it finishes |
| ⚪ hollow circle | Queued. It runs when the steps above it finish |
| **Executing Shell Script** takes about 20s | It's one step, but it does a lot: the whole `apt-get` install happens inside the script |
| **Post Checkout Repo** | A step you never wrote. `actions/checkout` registers a **post step** that runs at the end of the job to remove the credentials it saved. Many actions do this. It always runs last, in reverse order |
| **Cancel workflow** | Stops the run now. Steps still waiting are skipped |

> [!TIP]
> **Click the running step to watch its log live.** With one big script step, everything lands in one log section, so the `::group::` lines in the script are what keep it readable.

> [!NOTE]
> If run #2 failed with `Permission denied` and run #3 is green, the only change between them was the executable bit. Comparing two runs like this is one of the quickest ways to debug.

---

<p align="center">
  <a href="02-move-the-commands-into-a-script.md">⬅️ Move the commands into a script</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="04-what-each-line-of-the-script-does.md"><b>Next: What each line of the script does ➡️</b></a>
</p>
