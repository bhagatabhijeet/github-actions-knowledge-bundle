---
type: Tutorial
title: "Working with Variables: Fix 3: workflow-level `env`"
description: "A workflow-level env: block shares a variable with every job in the file."
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
  <a href="README.md">📂 <b>Working with Variables</b></a> &nbsp;·&nbsp; Lesson 11 · Part 4 of 14 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# 📜 Fix 3: workflow-level `env`

Put `env:` at the top, and **every job** sees it:

```yaml
name: Exploring Variables and Secrets

on: push

env:
  CONTAINER_REGISTRY: docker.io
  DOCKER_USERNAME: dockerUsername
  IMAGE_NAME: imageName
  IMAGE_TAG: ${{ github.sha }}          # 🏷️ a unique tag per commit, from a context

jobs:
  docker:
    runs-on: ubuntu-latest
    steps:
    - name: Docker Build
      run: docker build -t $CONTAINER_REGISTRY/$DOCKER_USERNAME/$IMAGE_NAME:$IMAGE_TAG .
    - name: Docker Publish
      run: docker push $CONTAINER_REGISTRY/$DOCKER_USERNAME/$IMAGE_NAME:$IMAGE_TAG

  deploy:
    needs: docker
    runs-on: ubuntu-latest
    steps:
    - name: Docker Run
      run: docker run -d -p 8080:80 $CONTAINER_REGISTRY/$DOCKER_USERNAME/$IMAGE_NAME:$IMAGE_TAG
```

Rename the image in **one** place, and both jobs follow. Every deploy now names the exact commit it came from.

---

<p align="center">
  <a href="03-fix-2-job-level-env.md">⬅️ Fix 2: job-level `env`</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="05-which-one-wins.md"><b>Next: Which one wins? ➡️</b></a>
</p>
