---
type: Tutorial
title: "What Are Actions?: The three kinds of action"
description: "Every action, whatever its kind, has a metadata file called action.yml at its root. It declares the name, inputs, outputs and how to run it. Here's a tiny composite action:"
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
  <a href="README.md">📂 <b>What Are Actions?</b></a> &nbsp;·&nbsp; Lesson 4 · Part 4 of 7 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# 🧱 The three kinds of action

| | Kind | How it runs | Runs on | Pick it when |
|---|---|---|---|---|
| ⚡ | **JavaScript** | Node.js, directly on the runner | Linux, Windows, macOS | You want speed and every OS |
| 🐳 | **Docker container** | Inside a container image it brings | Linux only | You need specific tools, or another language |
| 🧩 | **Composite** | A list of steps, written in YAML | Wherever its steps can run | You keep copy-pasting the same steps |

Every action, whatever its kind, has a metadata file called `action.yml` at its root. It declares the name, inputs, outputs and how to run it. Here's a tiny composite action:

```yaml
# action.yml
name: Greet
description: Say hello to someone
inputs:
  who:
    description: Who to greet
    default: world
runs:
  using: composite
  steps:
    - run: echo "Hello, ${{ inputs.who }}!"
      shell: bash
```

---

<p align="center">
  <a href="03-action-vs-command-the-two-kinds-of.md">⬅️ Action vs command: the two kinds of step</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="05-where-actions-come-from.md"><b>Next: Where actions come from ➡️</b></a>
</p>
