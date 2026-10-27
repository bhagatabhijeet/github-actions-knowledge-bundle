---
type: Tutorial
title: Multi-line Commands and Third-Party Tools (Hands-On)
description: Run several commands in one step with YAML's literal and folded blocks, understand how the shell treats them, then install and use a third-party tool on the runner - with apt, pip, npm or a setup action.
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
  <b>Lesson 6 of 14</b> &nbsp;·&nbsp; ⏱️ 18 min &nbsp;·&nbsp; 🛠️ Hands-on
</p>

# 📜 Multi-line Commands and Third-Party Tools

So far each `run:` step has held one command. Real steps often need several, and they often need tools that aren't part of your code. This lesson covers both.

## 🗺️ In this topic

6 subtopics, about 14 minutes in all. Read them in order, or jump to the one you need.

| # | Subtopic | Time |
|---|---|---|
| 1 | 🤔 [**One command per step gets noisy**](01-one-command-per-step-gets-noisy.md) | 1 min |
| 2 | ✍️ [**Two ways to write a multi-line `run:`**](02-two-ways-to-write-a-multi-line.md) | 2 min |
| 3 | 🐚 [**How the shell runs your lines**](03-how-the-shell-runs-your-lines.md) | 2 min |
| 4 | 📦 [**Executing third-party tools**](04-executing-third-party-tools.md) | 6 min |
| 5 | 🛠️ [**Try it yourself**](05-try-it-yourself.md) | 1 min |
| 6 | ✅ [**Checkpoint**](06-checkpoint.md) | 2 min |

<p align="center">
  <a href="01-one-command-per-step-gets-noisy.md"><b>▶️ Start with One command per step gets noisy</b></a>
</p>

## 🎯 What you learned

- **`run: |`** keeps each line as a separate command; **`run: >`** folds lines into one
- All lines of a step run in **one shell**: state carries **within** a step, not **between** steps
- Bash stops at the **first failing line**; `shell: bash` adds **pipefail**
- Check the **runner image** before installing anything; much is preinstalled
- Install third-party tools with **apt, pip, npm, brew** or a **setup action**, every run
- **Pin and verify** anything you download with `curl`

---

<p align="center">
  <a href="../05-configuring-the-checkout-action/README.md">⬅️ Configuring Checkout</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="../index.md">📚 Chapter 4</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="../07-executing-shell-scripts/README.md"><b>Next: Executing Shell Scripts ➡️</b></a>
</p>
