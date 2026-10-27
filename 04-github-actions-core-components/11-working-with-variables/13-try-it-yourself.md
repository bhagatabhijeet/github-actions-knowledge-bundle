---
type: Tutorial
title: "Working with Variables: Try it yourself"
description: "This repository ships a safe version of the example that prints the docker commands instead of running them: 04-variables.yml."
tags: [github-actions, variables, env, vars, configuration-variables, github-env, hands-on]
status: stable
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-26T00:00:00Z }
sources:
  - id: gh-variables
    resource: https://docs.github.com/en/actions/concepts/workflows-and-actions/variables
    title: Variables
  - id: gh-variables-ref
    resource: https://docs.github.com/en/actions/reference/workflows-and-actions/variables
    title: Variables reference
  - id: gh-contexts
    resource: https://docs.github.com/en/actions/reference/workflows-and-actions/contexts
    title: Contexts reference
  - id: gh-workflow-commands
    resource: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-commands
    title: Workflow commands for GitHub Actions
---

<p align="center">
  <a href="README.md">📂 <b>Working with Variables</b></a> &nbsp;·&nbsp; Lesson 11 · Part 13 of 14 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# 🛠️ Try it yourself

This repository ships a safe version of the example that **prints** the docker commands instead of running them: [`04-variables.yml`](../../.github/workflows/04-variables.yml).

1. **Actions** tab → **04 - Variables** → **Run workflow**
2. In the **docker** job, open **Who wins? (step level)**: both lines say `rc-1`. Open **Back to the job value**: it's `stable` again
3. **Default variables GitHub gives you** lists the repository, branch, commit and more
4. On the **Summary** page, the table from **deploy** shows `IMAGE_TAG` is `latest` there: the job-level override didn't reach another job
5. **Make it yours:** in a fork, add a repository variable `DOCKER_USERNAME` with your name, re-run, and watch it replace `demo-user`. No commit needed

---

<p align="center">
  <a href="12-common-mistakes.md">⬅️ Common mistakes</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="14-checkpoint.md"><b>Next: Checkpoint ➡️</b></a>
</p>
