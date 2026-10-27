---
type: Tutorial
title: "Working with Variables: Fix 2: job-level `env`"
description: "Move env: up to the job, and every step in that job sees it:"
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
  <a href="README.md">📂 <b>Working with Variables</b></a> &nbsp;·&nbsp; Lesson 11 · Part 3 of 14 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# 📦 Fix 2: job-level `env`

Move `env:` up to the job, and **every step in that job** sees it:

```yaml
  docker:
    runs-on: ubuntu-latest
    env:
      CONTAINER_REGISTRY: docker.io
      DOCKER_USERNAME: dockerUsername
      IMAGE_NAME: imageName
    steps:
    - name: Docker Build
      run: docker build -t $CONTAINER_REGISTRY/$DOCKER_USERNAME/$IMAGE_NAME:latest .
    - name: Docker Publish
      run: docker push $CONTAINER_REGISTRY/$DOCKER_USERNAME/$IMAGE_NAME:latest
```

But `deploy` is a different job, on a different runner. It still has nothing.

---

<p align="center">
  <a href="02-fix-1-step-level-env.md">⬅️ Fix 1: step-level `env`</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="04-fix-3-workflow-level-env.md"><b>Next: Fix 3: workflow-level `env` ➡️</b></a>
</p>
