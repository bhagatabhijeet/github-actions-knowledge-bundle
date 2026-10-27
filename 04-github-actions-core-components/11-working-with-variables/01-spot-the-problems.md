---
type: Tutorial
title: "Working with Variables: Spot the problems"
description: "Here is a workflow that builds a Docker image, pushes it, and runs it. It works. Before reading on, see how many problems you can find."
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
  <a href="README.md">📂 <b>Working with Variables</b></a> &nbsp;·&nbsp; Lesson 11 · Part 1 of 14 &nbsp;·&nbsp; ⏱️ 2 min
</p>

# 🕵️ Spot the problems

Here is a workflow that builds a Docker image, pushes it, and runs it. It works. Before reading on, see how many problems you can find.

```yaml
name: Exploring Variables and Secrets

on:
  push

jobs:
  docker:
    runs-on: ubuntu-latest
    steps:
    - name: Docker Build
      run: docker build -t docker.io/dockerUsername/imageName:latest

    - name: Docker Login
      run: docker login --username=dockerUsername --password=s3cUrePaSsw0rd

    - name: Docker Publish
      run: docker push docker.io/dockerUsername/imageName:latest

  deploy:
    needs: docker
    runs-on: ubuntu-latest
    steps:
    - name: Docker Run
      run: docker run -d -p 8080:80 docker.io/dockerUsername/imageName:latest
```

<details>
<summary><b>🔍 Reveal the problems</b></summary>

<br>

| | Problem | What goes wrong |
|---|---|---|
| 🔁 | `docker.io/dockerUsername/imageName:latest` is typed **three times** | Rename the image and you must find every copy. Miss one and you deploy the wrong image |
| 👤 | `dockerUsername` appears **four times**, in two jobs | Same again, across jobs |
| 🏷️ | The tag is always `latest` | You can't tell which commit is running, or roll back |
| 🚨 | **The password is in the file** | Anyone who can read the repository, and its whole Git history, now has your Docker Hub password |

The first three are fixed with **variables**, in this lesson. The fourth needs a **secret**, which is a variable GitHub encrypts and hides. There's a short preview below.

</details>

---

<p align="center">
  <a href="README.md">⬅️ Overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="02-fix-1-step-level-env.md"><b>Next: Fix 1: step-level `env` ➡️</b></a>
</p>
