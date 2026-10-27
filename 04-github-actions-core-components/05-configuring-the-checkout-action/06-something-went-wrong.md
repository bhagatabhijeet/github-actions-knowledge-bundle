---
type: Tutorial
title: "Configuring the Checkout Action: Something went wrong?"
description: "Five common checkout failures - missing files, no tags, repository not found, vanished files, pushes that trigger nothing - and how to fix each."
tags: [github-actions, actions, checkout, hands-on, fetch-depth, sparse-checkout]
status: stable
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-26T00:00:00Z }
sources:
  - id: checkout-repo
    resource: https://github.com/actions/checkout
    title: actions/checkout README
  - id: gh-workflow-syntax
    resource: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
    title: Workflow syntax for GitHub Actions
---

<p align="center">
  <a href="README.md">📂 <b>Configuring the Checkout Action</b></a> &nbsp;·&nbsp; Lesson 5 · Part 6 of 7 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# 🧯 Something went wrong?

| Symptom | Likely cause | Fix |
|---|---|---|
| `No such file or directory` | No checkout step, or it comes after the step that needs files | Make checkout the **first** step |
| `git describe` or changelog tools find no tags | Shallow clone | `fetch-depth: 0` |
| `Repository not found` for another repo | `GITHUB_TOKEN` can only read this repo | Pass a `token:` with access to the other repo |
| Files from the last job are gone (self-hosted) | `clean: true` wiped them | That's intended. Use artifacts to pass files between jobs |
| A push from the workflow doesn't trigger other workflows | Pushes made with `GITHUB_TOKEN` don't start new runs | Use a GitHub App token or PAT in `token:` |

---

<p align="center">
  <a href="05-try-it-yourself.md">⬅️ Try it yourself</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="07-checkpoint.md"><b>Next: Checkpoint ➡️</b></a>
</p>
