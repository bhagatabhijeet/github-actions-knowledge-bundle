---
type: Tutorial
title: "Working with Repository-Level Secrets: If a secret leaks"
description: "Let GitHub watch for you. Secret scanning with push protection (Settings → Code security) blocks pushes that contain known token formats, before they reach the repository. It's free for public repositories."
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
  <a href="README.md">📂 <b>Working with Repository-Level Secrets</b></a> &nbsp;·&nbsp; Lesson 12 · Part 8 of 10 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# 🚨 If a secret leaks

| Step | Action |
|---|---|
| 1️⃣ **Revoke or rotate it at the source** | Docker Hub, AWS, npm... This is the only step that actually stops the damage |
| 2️⃣ **Update the GitHub secret** | Settings, or `gh secret set` |
| 3️⃣ **Delete affected logs** | The run's ⋯ menu → **Delete all logs** |
| 4️⃣ **Remove it from the code** | And treat the old commit as public forever. Rewriting history doesn't reach existing clones and forks |
| 5️⃣ **Check for misuse** | The provider's audit or access logs |

> [!TIP]
> **Let GitHub watch for you.** **Secret scanning** with **push protection** (Settings → Code security) blocks pushes that contain known token formats, before they reach the repository. It's free for public repositories.

---

<p align="center">
  <a href="07-repository-environment-or-organisation.md">⬅️ Repository, environment or organisation?</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="09-try-it-yourself.md"><b>Next: Try it yourself ➡️</b></a>
</p>
