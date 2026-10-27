---
type: Tutorial
title: "Working with Repository-Level Secrets: Try it yourself"
description: "This repository ships a workflow that's safe to run with or without any secrets: 04-secrets.yml."
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
  <a href="README.md">📂 <b>Working with Repository-Level Secrets</b></a> &nbsp;·&nbsp; Lesson 12 · Part 9 of 10 &nbsp;·&nbsp; ⏱️ 2 min
</p>

# 🧪 Try it yourself

This repository ships a workflow that's safe to run with or without any secrets: [`04-secrets.yml`](../../.github/workflows/04-secrets.yml).

1. **Actions** → **04 - Secrets** → **Run workflow**. With nothing set, both jobs pass and leave a ℹ️ notice telling you what to add
2. In a fork, add a repository secret **`DEMO_SECRET`** with any harmless value, like `dragon-123`, and run it again
3. Open **Print it (GitHub masks it)**: the log shows `The secret is ***`
4. Open **A changed copy is NOT masked automatically**: the base64 copy is masked only because the step called `::add-mask::` first
5. **Optional:** add a `DOCKER_USERNAME` **variable** and a `DOCKER_PASSWORD` **secret** holding a Docker Hub access token. The **docker-login** job logs in for real
6. Go back to **Settings → Secrets**: try to view `DEMO_SECRET`. You can only update or remove it

---

<p align="center">
  <a href="08-if-a-secret-leaks.md">⬅️ If a secret leaks</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="10-checkpoint.md"><b>Next: Checkpoint ➡️</b></a>
</p>
