---
type: Tutorial
title: "Working with Repository-Level Secrets: Repository, environment or organisation?"
description: "This lesson uses repository secrets. There are two more levels, and the most specific wins when names clash:"
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
  <a href="README.md">📂 <b>Working with Repository-Level Secrets</b></a> &nbsp;·&nbsp; Lesson 12 · Part 7 of 10 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# 🏢 Repository, environment or organisation?

This lesson uses **repository** secrets. There are two more levels, and the most specific wins when names clash:

| Level | Set in | Available to | Precedence |
|---|---|---|---|
| 🏢 Organisation | Org settings | Repositories you choose | Lowest |
| 📁 **Repository** | Repo settings → Secrets and variables → Actions | Every workflow in the repo | Middle |
| 🌍 Environment | Repo settings → Environments → *name* | Jobs with `environment: <name>`, optionally only after a **required reviewer** approves | **Highest** |

Keep production credentials in an **environment** secret behind required reviewers, so no job can use them without someone approving the deployment.

---

<p align="center">
  <a href="06-the-secret-you-get-for-free-github.md">⬅️ The secret you get for free: `GITHUB_TOKEN`</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="08-if-a-secret-leaks.md"><b>Next: If a secret leaks ➡️</b></a>
</p>
