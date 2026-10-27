---
type: Tutorial
title: "What Are Actions?: Action vs command: the two kinds of step"
description: "Every step does exactly one of two things:"
tags: [github-actions, actions, uses, marketplace, composite, docker, javascript, security]
status: stable
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-25T00:00:00Z }
sources:
  - id: gh-about-actions
    resource: https://docs.github.com/en/actions/concepts/workflows-and-actions/custom-actions
    title: About custom actions
  - id: gh-workflow-syntax
    resource: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
    title: Workflow syntax for GitHub Actions
  - id: gh-secure-use
    resource: https://docs.github.com/en/actions/reference/security/secure-use
    title: Secure use reference
  - id: gh-marketplace
    resource: https://github.com/marketplace?type=actions
    title: GitHub Marketplace - Actions
---

<p align="center">
  <a href="README.md">📂 <b>What Are Actions?</b></a> &nbsp;·&nbsp; Lesson 4 · Part 3 of 7 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# ⚖️ Action vs command: the two kinds of step

Every step does exactly one of two things:

```yaml
steps:
  - uses: actions/setup-node@v5     # 🧩 call an action
    with:
      node-version: 22
  - run: npm test                   # ⌨️ run a shell command
```

| | `uses:` (action) | `run:` (command) |
|---|---|---|
| What it is | Someone's packaged, tested code | Your own shell line |
| Best for | Common jobs everyone needs | Things specific to your project |
| Takes settings via | `with:` inputs | Environment variables, arguments |
| Rule of thumb | Don't reinvent setup, caching, login | Don't wrap one-liners in an action |

Without actions, "check out the code" would be a dozen lines of `git` commands, tokens and edge cases, copied into every workflow you write. With actions it's one line, maintained by someone else.

---

<p align="center">
  <a href="02-reading-a-uses-line.md">⬅️ Reading a `uses:` line</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="04-the-three-kinds-of-action.md"><b>Next: The three kinds of action ➡️</b></a>
</p>
