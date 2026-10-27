---
type: Reference
title: "Chapter 1 Cheat Sheet and Quiz: Golden rules"
description: "Six rules for safe, working workflows, plus the key GitHub Actions limits worth remembering."
tags: [github-actions, cheat-sheet, quiz, recap]
status: stable
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-26T00:00:00Z }
sources:
  - id: gh-syntax
    resource: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
    title: Workflow syntax for GitHub Actions
  - id: gh-variables
    resource: https://docs.github.com/en/actions/reference/workflows-and-actions/variables
    title: Variables reference
  - id: gh-limits
    resource: https://docs.github.com/en/actions/reference/limits
    title: Actions limits
  - id: gh-events
    resource: https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows
    title: Events that trigger workflows
---

<p align="center">
  <a href="README.md">📂 <b>Chapter 1 Cheat Sheet and Quiz</b></a> &nbsp;·&nbsp; Lesson 5 · Part 4 of 6 &nbsp;·&nbsp; ⏱️ 2 min
</p>

# 🏆 Golden rules

> [!IMPORTANT]
> 1. **Checkout first.** The runner starts empty.
> 2. **Jobs are parallel and isolated.** Use `needs` to order, artifacts to share.
> 3. **Non-zero exit = failure.** That's how a workflow knows.
> 4. **Quote your versions.** `'3.10'`, not `3.10`.
> 5. **Pin your actions.** `@v7`, never `@main`.
> 6. **Least privilege.** Start with `permissions: contents: read`.

## 📏 Numbers worth remembering

| Limit | Value |
|---|---|
| Workflow file location | `.github/workflows/*.yml` or `*.yaml` |
| One job on a GitHub-hosted runner | 6 hours max |
| One workflow run | 35 days max |
| Jobs from one matrix | 256 max |
| Shortest `schedule` interval | every 5 minutes |
| Concurrent hosted jobs, Free plan | 20 |

Sources: [Actions limits](https://docs.github.com/en/actions/reference/limits), [Events that trigger workflows](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows).

---

<p align="center">
  <a href="03-default-variables-worth-knowing.md">⬅️ Default variables worth knowing</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="05-quiz.md"><b>Next: Quiz ➡️</b></a>
</p>
