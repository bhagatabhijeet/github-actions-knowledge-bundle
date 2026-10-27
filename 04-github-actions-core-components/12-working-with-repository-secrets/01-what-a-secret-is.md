---
type: Tutorial
title: "Working with Repository-Level Secrets: What a secret is"
description: "A secret is a variable that GitHub encrypts, never shows again, and hides from the logs. You read it in a workflow with ${{ secrets.NAME }}."
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
  <a href="README.md">📂 <b>Working with Repository-Level Secrets</b></a> &nbsp;·&nbsp; Lesson 12 · Part 1 of 10 &nbsp;·&nbsp; ⏱️ 2 min
</p>

# 💡 What a secret is

> **A secret is a variable that GitHub encrypts, never shows again, and hides from the logs.** You read it in a workflow with `${{ secrets.NAME }}`.

<p align="center">
  <img src="../../assets/images/secret-journey.svg" alt="You type a secret in Settings; it is encrypted on your machine with the repository's public key, stored encrypted by GitHub where nobody can read it back, and decrypted only on the runner for the job, where it is masked as three asterisks in logs. It is protected from people reading code, Settings or logs and from fork pull requests, but not from changed copies, workflows that send it elsewhere, third-party actions, files and artifacts, or people with write access" width="100%">
</p>

| Stage | What happens |
|---|---|
| ⌨️ **You save it** | In **Settings** or with `gh secret set` |
| 🔒 **Encrypted before upload** | Your browser or the CLI seals it with the repository's public key ([libsodium sealed box](https://libsodium.gitbook.io/doc/public-key_cryptography/sealed_boxes)), so it never travels in plain text |
| 🗄️ **Stored write-only** | Settings shows the name and when it was updated, never the value. You can **update** or **delete** it, not read it |
| 🖥️ **Decrypted for the job** | Only when a job runs, and only reaches the steps you pass it to |
| 🙈 **Masked in logs** | If the exact value appears in a log, GitHub prints `***` instead |

---

<p align="center">
  <a href="README.md">⬅️ Overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="02-creating-a-repository-secret-step-by-step.md"><b>Next: Creating a repository secret, step by step ➡️</b></a>
</p>
