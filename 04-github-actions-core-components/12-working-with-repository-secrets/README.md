---
type: Tutorial
title: Working with Repository-Level Secrets (Hands-On)
description: Get passwords and tokens out of your workflow files - what a secret is and how GitHub protects it, creating repository secrets in Settings or with gh, using them safely in run steps and actions, log masking and its limits, forks, GITHUB_TOKEN, and what to do when a secret leaks.
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
  <b>Lesson 12 of 14</b> &nbsp;·&nbsp; ⏱️ 28 min &nbsp;·&nbsp; 🛠️ Hands-on &nbsp;·&nbsp; 🔐 Security essential
</p>

# 🔐 Working with Repository-Level Secrets

In [Lesson 11](../11-working-with-variables/README.md) we cleaned up a Docker workflow with variables, and left one problem on purpose:

```yaml
    - name: Docker Login
      run: docker login --username=dockerUsername --password=s3cUrePaSsw0rd   # 🚨
```

That password is now readable by everyone who can see the repository, in every fork and clone, and in the Git history forever. **Secrets** exist so this never happens. This lesson fixes the line properly, and shows exactly what secrets protect you from, and what they don't.

## 🗺️ In this topic

10 subtopics, about 23 minutes in all. Read them in order, or jump to the one you need.

| # | Subtopic | Time |
|---|---|---|
| 1 | 💡 [**What a secret is**](01-what-a-secret-is.md) | 2 min |
| 2 | 🛠️ [**Creating a repository secret, step by step**](02-creating-a-repository-secret-step-by-step.md) | 8 min |
| 3 | ✅ [**Using it: fixing the Docker login**](03-using-it-fixing-the-docker-login.md) | 2 min |
| 4 | 🙈 [**Log masking: what it catches, and what it misses**](04-log-masking-what-it-catches-and-what.md) | 2 min |
| 5 | 🚦 [**Rules that catch people out**](05-rules-that-catch-people-out.md) | 2 min |
| 6 | 🎟️ [**The secret you get for free: `GITHUB_TOKEN`**](06-the-secret-you-get-for-free-github.md) | 1 min |
| 7 | 🏢 [**Repository, environment or organisation?**](07-repository-environment-or-organisation.md) | 1 min |
| 8 | 🚨 [**If a secret leaks**](08-if-a-secret-leaks.md) | 1 min |
| 9 | 🧪 [**Try it yourself**](09-try-it-yourself.md) | 2 min |
| 10 | ✅ [**Checkpoint**](10-checkpoint.md) | 2 min |

<p align="center">
  <a href="01-what-a-secret-is.md"><b>▶️ Start with What a secret is</b></a>
</p>

## 🎯 What you learned

- A **secret** is encrypted before upload, **write-only** in Settings, decrypted only for the job, and **masked** in logs
- Create one in **Settings → Secrets and variables → Actions**, or with **`gh secret set`** (let it prompt)
- Read it as **`${{ secrets.NAME }}`**; in `run:`, pass it through **`env:`** and use stdin, like `--password-stdin`
- Masking only catches the **exact** value; register derived values with **`::add-mask::`**, and never print secrets
- **Forks** and **Dependabot** runs don't get your Actions secrets; actions only get what you pass them
- **`GITHUB_TOKEN`** is a free, short-lived secret; limit it with **`permissions:`**
- If a secret leaks, **rotate it at the source first**

---

<p align="center">
  <a href="../11-working-with-variables/README.md">⬅️ Variables</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="../index.md">📚 Chapter 4</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="../13-triggering-workflows-in-detail/README.md"><b>Next: Triggering Workflows in Detail ➡️</b></a>
</p>
