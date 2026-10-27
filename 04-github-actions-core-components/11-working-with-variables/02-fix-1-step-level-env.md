---
type: Tutorial
title: "Working with Variables: Fix 1: step-level `env`"
description: "A step-level env: block sets variables that only that one step can see."
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
  <a href="README.md">📂 <b>Working with Variables</b></a> &nbsp;·&nbsp; Lesson 11 · Part 2 of 14 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# 🧱 Fix 1: step-level `env`

`env:` defines environment variables. Put it on a step, and only that step sees them:

```yaml
    - name: Docker Build
      env:
        CONTAINER_REGISTRY: docker.io
        DOCKER_USERNAME: dockerUsername
        IMAGE_NAME: imageName
      run: docker build -t $CONTAINER_REGISTRY/$DOCKER_USERNAME/$IMAGE_NAME:latest .
```

Better, but **Docker Publish** needs the same values, and it can't see them. Step-level `env` is for values only one step uses.

---

<p align="center">
  <a href="01-spot-the-problems.md">⬅️ Spot the problems</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="03-fix-2-job-level-env.md"><b>Next: Fix 2: job-level `env` ➡️</b></a>
</p>
