---
type: Tutorial
title: "Working with Repository-Level Secrets: Checkpoint"
description: "You can't. Secrets are write-only. Get the value from its source, or create a new one and update the secret."
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
  <a href="README.md">📂 <b>Working with Repository-Level Secrets</b></a> &nbsp;·&nbsp; Lesson 12 · Part 10 of 10 &nbsp;·&nbsp; ⏱️ 2 min
</p>

# ✅ Checkpoint

<details>
<summary><b>You saved a secret yesterday and forgot what it was. How do you read it back from GitHub?</b></summary>

<br>

You can't. Secrets are write-only. Get the value from its source, or create a new one and update the secret.

</details>

<details>
<summary><b>Why pass a secret through <code>env:</code> instead of writing <code>${{ secrets.X }}</code> inside <code>run:</code>?</b></summary>

<br>

An expression in `run:` is pasted into the script text before it runs, so quotes or special characters in the value can break the command. Through `env:`, the shell receives it as data in `$X`.

</details>

<details>
<summary><b>A step prints a secret base64-encoded. Will the log show <code>***</code>?</b></summary>

<br>

No. Masking only matches the exact value. Register the encoded value with `::add-mask::` first, or better, don't print it at all.

</details>

<details>
<summary><b>A contributor opens a pull request from their fork, and your deploy step fails with an empty password. Bug?</b></summary>

<br>

No, it's protection. Workflows triggered by pull requests from forks don't receive your secrets, so a stranger can't steal them by changing the workflow in their PR.

</details>

<details>
<summary><b>A password was committed and you've deleted the line. Are you safe?</b></summary>

<br>

No. It's still in the Git history and in every clone and fork. Rotate the password at its source first.

</details>

---

<p align="center">
  <a href="09-try-it-yourself.md">⬅️ Try it yourself</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md#-what-you-learned"><b>Wrap up: What you learned ➡️</b></a>
</p>
