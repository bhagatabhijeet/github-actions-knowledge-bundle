---
type: Tutorial
title: "The Six Core Concepts: 6. Runner: the machine"
description: "GitHub-hosted versus self-hosted runners, the fresh-VM-per-job model, and which shell runs your run: steps."
tags: [github-actions, concepts, workflow, job, step, action, runner, event]
status: stable
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-26T00:00:00Z }
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
  - id: gh-syntax
    resource: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
    title: Workflow syntax for GitHub Actions
---

<p align="center">
  <a href="README.md">📂 <b>The Six Core Concepts</b></a> &nbsp;·&nbsp; Lesson 2 · Part 6 of 8 &nbsp;·&nbsp; ⏱️ 2 min
</p>

# 🖥️ 6. Runner: the machine

A runner is the computer that executes a job.

| | GitHub-hosted | Self-hosted |
|---|---|---|
| Who maintains it | GitHub | You |
| State | Fresh VM per job, destroyed after | Whatever you left on it |
| Labels | `ubuntu-latest`, `windows-latest`, `macos-latest` | Your own |
| Best for | Almost everyone, to start | Special hardware, private networks |

```yaml
runs-on: ubuntu-latest
```

GitHub-hosted runners come with a huge toolbox pre-installed: Git, Docker, Node.js, Python, Java, cloud CLIs and more.

🐚 Which shell runs your `run:` lines? On Linux and macOS it's `bash` (falling back to `sh` if bash is missing), started as `bash -e`, so the step stops at the first failing command. On Windows the default is `pwsh` (PowerShell). ([Workflow syntax](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax))

> [!NOTE]
> "Fresh VM per job" is the most important mental model in GitHub Actions. It's why builds are reproducible, and it's also why a file you created in one job has vanished by the next. Sharing between jobs needs **artifacts** or **outputs**, which you'll use in [Chapter 2](../../02-basics-of-ci-cd/05-your-first-ci-pipeline/README.md).

---

<p align="center">
  <a href="05-5-action-a-reusable-building-block.md">⬅️ 5. Action: a reusable building block</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="07-the-whole-family-one-table.md"><b>Next: The whole family, one table ➡️</b></a>
</p>
