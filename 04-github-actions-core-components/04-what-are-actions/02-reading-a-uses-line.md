---
type: Tutorial
title: "What Are Actions?: Reading a `uses:` line"
description: "Actions can also hand outputs back, which later steps read through steps.<id>.outputs.<name>."
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
  <a href="README.md">📂 <b>What Are Actions?</b></a> &nbsp;·&nbsp; Lesson 4 · Part 2 of 7 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# 🔬 Reading a `uses:` line

<p align="center">
  <img src="../../assets/images/anatomy-of-an-action.svg" alt="The step 'uses: actions/checkout@v7' with 'with: fetch-depth: 0' broken into owner, repository, version and inputs, and the three kinds of action below: JavaScript, Docker container and composite" width="100%">
</p>

| Part | Example | What it means |
|---|---|---|
| 🔵 **Owner** | `actions` | The GitHub user or organisation that publishes it. `actions` is GitHub's own |
| 🩷 **Repository** | `checkout` | The repo holding the action's code and its `action.yml` |
| 🟢 **Version** | `@v7` | A tag, a branch or a full commit SHA. Decides exactly which code runs |
| 🟠 **Inputs** | `with: fetch-depth: 0` | Settings the action accepts, like arguments to a function |

Actions can also hand **outputs** back, which later steps read through `steps.<id>.outputs.<name>`.

---

<p align="center">
  <a href="01-the-one-sentence-definition.md">⬅️ The one-sentence definition</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="03-action-vs-command-the-two-kinds-of.md"><b>Next: Action vs command: the two kinds of step ➡️</b></a>
</p>
