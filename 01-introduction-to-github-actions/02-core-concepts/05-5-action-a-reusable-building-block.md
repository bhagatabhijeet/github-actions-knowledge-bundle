---
type: Tutorial
title: "The Six Core Concepts: 5. Action: a reusable building block"
description: "An action is packaged logic that someone already wrote so you don't have to. You call it with uses:."
tags: [github-actions, concepts, workflow, job, step, action, runner, event]
status: stable
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-07T00:00:00Z }
sources:
  - id: gh-understand
    resource: https://docs.github.com/en/actions/get-started/understand-github-actions
    title: Understanding GitHub Actions
  - id: gh-runners
    resource: https://docs.github.com/en/actions/concepts/runners/github-hosted-runners
    title: GitHub-hosted runners
  - id: gh-events
    resource: https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows
    title: Events that trigger workflows
---

<p align="center">
  <a href="README.md">📂 <b>The Six Core Concepts</b></a> &nbsp;·&nbsp; Lesson 2 · Part 5 of 8 &nbsp;·&nbsp; ⏱️ 2 min
</p>

# 🧱 5. Action: a reusable building block

An action is packaged logic that someone already wrote so you don't have to. You call it with `uses:`.

```yaml
- uses: actions/setup-python@v7
  with:
    python-version: '3.13'
```

Read the reference like an address:

```text
actions / setup-python @ v7
   │           │          │
 owner       repo      version
```

Thousands of actions are published on the [GitHub Marketplace](https://github.com/marketplace?type=actions): log in to a cloud, send a Slack message, publish to npm.

> [!WARNING]
> **Naming trap.** The product is called GitHub Action**s**. An **action** is one reusable building block inside it. A workflow is *not* an action. When someone says "I wrote an action", ask which they mean.

> [!CAUTION]
> An action is someone else's code running with access to your repository. Prefer actions from owners you trust, and always pin a version (`@v7`), never a moving branch like `@main`.

📎 Side-by-side comparison: [assets/snippets/run-vs-uses.yml](../../assets/snippets/run-vs-uses.yml)

---

<p align="center">
  <a href="04-4-step-one-thing-at-a-time.md">⬅️ 4. Step: one thing at a time</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="06-6-runner-the-machine.md"><b>Next: 6. Runner: the machine ➡️</b></a>
</p>
