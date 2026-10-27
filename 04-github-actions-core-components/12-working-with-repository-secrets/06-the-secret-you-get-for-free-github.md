---
type: Tutorial
title: "Working with Repository-Level Secrets: The secret you get for free: `GITHUB_TOKEN`"
description: "Every run gets an automatic secret, secrets.GITHUBTOKEN. It's a short-lived token for this repository, created when the job starts and expired when it ends. Actions such as actions/checkout use it by default."
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
  <a href="README.md">📂 <b>Working with Repository-Level Secrets</b></a> &nbsp;·&nbsp; Lesson 12 · Part 6 of 10 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# 🎟️ The secret you get for free: `GITHUB_TOKEN`

Every run gets an automatic secret, `secrets.GITHUB_TOKEN`. It's a short-lived token for **this repository**, created when the job starts and expired when it ends. Actions such as `actions/checkout` use it by default.

Control what it can do with `permissions:`. Start from read-only and add only what a job needs:

```yaml
permissions:
  contents: read            # the whole workflow: read-only by default

jobs:
  release:
    permissions:
      contents: write       # this job alone may create a release
    runs-on: ubuntu-latest
    steps:
      - run: gh release create v1.0.0
        env:
          GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

> [!TIP]
> **Prefer `GITHUB_TOKEN` over a personal access token** for anything inside the same repository. It expires on its own and can't reach your other repositories.

---

<p align="center">
  <a href="05-rules-that-catch-people-out.md">⬅️ Rules that catch people out</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="07-repository-environment-or-organisation.md"><b>Next: Repository, environment or organisation? ➡️</b></a>
</p>
