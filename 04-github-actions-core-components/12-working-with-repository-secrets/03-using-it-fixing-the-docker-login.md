---
type: Tutorial
title: "Working with Repository-Level Secrets: Using it: fixing the Docker login"
description: "Pass the Docker password from secrets into the login step through env: and stdin, so it never appears in the command line or the YAML."
tags: [github-actions, secrets, security, masking, github-token, docker, hands-on]
status: stable
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-26T00:00:00Z }
sources:
  - id: gh-secrets
    resource: https://docs.github.com/en/actions/concepts/security/secrets
    title: Secrets
  - id: gh-use-secrets
    resource: https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/use-secrets
    title: Using secrets in GitHub Actions
  - id: gh-secure-use
    resource: https://docs.github.com/en/actions/reference/security/secure-use
    title: Secure use reference
  - id: gh-secret-set
    resource: https://cli.github.com/manual/gh_secret_set
    title: gh secret set
  - id: docker-login-action
    resource: https://github.com/docker/login-action
    title: docker/login-action
---

<p align="center">
  <a href="README.md">📂 <b>Working with Repository-Level Secrets</b></a> &nbsp;·&nbsp; Lesson 12 · Part 3 of 10 &nbsp;·&nbsp; ⏱️ 2 min
</p>

# ✅ Using it: fixing the Docker login

## Option A: in a `run:` step

```yaml
    - name: Docker Login
      env:
        DOCKER_PASSWORD: ${{ secrets.DOCKER_PASSWORD }}     # 1️⃣ map the secret to an env var
      run: echo "$DOCKER_PASSWORD" | docker login --username "$DOCKER_USERNAME" --password-stdin   # 2️⃣ read it from stdin
```

Two details make this safe:

| | Detail | Why |
|---|---|---|
| 1️⃣ | Pass the secret through **`env:`**, read it as `$DOCKER_PASSWORD` | `${{ secrets.X }}` written directly in `run:` is pasted into the script text before it runs, where special characters can break the command |
| 2️⃣ | Use **`--password-stdin`**, not `--password=` | A value on the command line can show up in process lists, and Docker warns about it |

## Option B: with an action

```yaml
    - name: Docker Login
      uses: docker/login-action@v4
      with:
        username: ${{ vars.DOCKER_USERNAME }}
        password: ${{ secrets.DOCKER_PASSWORD }}
```

The action handles stdin and logs out at the end of the job for you.

## The whole workflow, fixed

```yaml
name: Exploring Variables and Secrets

on: push

env:
  CONTAINER_REGISTRY: docker.io
  DOCKER_USERNAME: ${{ vars.DOCKER_USERNAME }}     # ⚙️ variable: not sensitive
  IMAGE_NAME: imageName

jobs:
  docker:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v7

      - name: Docker Login
        uses: docker/login-action@v4
        with:
          username: ${{ vars.DOCKER_USERNAME }}
          password: ${{ secrets.DOCKER_PASSWORD }}  # 🔐 secret: sensitive

      - name: Docker Build
        run: docker build -t $CONTAINER_REGISTRY/$DOCKER_USERNAME/$IMAGE_NAME:${{ github.sha }} .

      - name: Docker Publish
        run: docker push $CONTAINER_REGISTRY/$DOCKER_USERNAME/$IMAGE_NAME:${{ github.sha }}
```

No password anywhere in the file. Rotate it in Settings and the workflow keeps working, with no commit.

---

<p align="center">
  <a href="02-creating-a-repository-secret-step-by-step.md">⬅️ Creating a repository secret, step by step</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="04-log-masking-what-it-catches-and-what.md"><b>Next: Log masking: what it catches, and what it misses ➡️</b></a>
</p>
