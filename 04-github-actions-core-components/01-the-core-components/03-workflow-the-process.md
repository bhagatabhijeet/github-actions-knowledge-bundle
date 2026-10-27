---
type: Tutorial
title: "The Core Components: Workflow: the process"
description: "A workflow is an automated process that carries out one or more jobs. It lives in a YAML file inside .github/workflows/."
tags: [github-actions, core-components, workflow, job, step, runner, matrix]
status: stable
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-07T00:00:00Z }
sources:
  - id: gh-understand
    resource: https://docs.github.com/en/actions/get-started/understand-github-actions
    title: Understanding GitHub Actions
  - id: gh-workflow-syntax
    resource: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
    title: Workflow syntax for GitHub Actions
  - id: gh-hosted-runners
    resource: https://docs.github.com/en/actions/concepts/runners/github-hosted-runners
    title: GitHub-hosted runners
---

<p align="center">
  <a href="README.md">📂 <b>The Core Components</b></a> &nbsp;·&nbsp; Lesson 1 · Part 3 of 8 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# 📜 Workflow: the process

A workflow is an automated process that carries out one or more jobs. It lives in a YAML file inside `.github/workflows/`.

- A repository can hold **many workflows**: one for tests, one for deployments, one for labelling issues
- Each workflow says **which events it listens for**
- The file name is yours to choose. The folder is not

```text
.github/
└── workflows/
    ├── unit-tests.yml      👈 runs on every push
    ├── deploy.yml          👈 runs when a release is published
    └── triage.yml          👈 runs when an issue is opened
```

---

<p align="center">
  <a href="02-they-nest-like-boxes.md">⬅️ They nest like boxes</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="04-job-work-for-one-machine.md"><b>Next: Job: work for one machine ➡️</b></a>
</p>
