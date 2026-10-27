---
type: Tutorial
title: "Working with Repository-Level Secrets: Rules that catch people out"
description: "Rules that catch people out, part 5 of 10 of Working with Repository-Level Secrets."
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
  <a href="README.md">📂 <b>Working with Repository-Level Secrets</b></a> &nbsp;·&nbsp; Lesson 12 · Part 5 of 10 &nbsp;·&nbsp; ⏱️ 2 min
</p>

# 🚦 Rules that catch people out

| Rule | What it means | What to do |
|---|---|---|
| 🚫 **No secrets in `if:` directly** | `if: secrets.TOKEN != ''` isn't allowed | Map it to job-level `env:`, then test `env.TOKEN` in a step's `if:`, or map a `!= ''` check as this repo's live workflow does |
| 📭 **Missing secret = empty string** | No error, just an empty value. `docker login` then fails with a confusing message | Check it's set at the start of the job |
| 🍴 **Forks don't get secrets** | Workflows triggered by a `pull_request` **from a fork** run without your secrets (only a read-only `GITHUB_TOKEN`) | Expected: strangers can't steal them by opening a PR. Don't "fix" it with `pull_request_target` and checking out their code |
| 🤖 **Dependabot runs don't get Actions secrets** | Workflows triggered by Dependabot see **Dependabot secrets** instead | Add the ones it needs under **Secrets and variables → Dependabot** |
| 🧩 **Actions don't see secrets automatically** | An action only gets what you pass in `with:` or `env:` | Pass only the secrets each step needs |
| 🔁 **Reusable workflows don't inherit them** | A called workflow gets secrets only if you pass them | `secrets: inherit`, or pass them one by one |
| 📏 **Limits** | Up to 48 KB per secret, 100 secrets per repository | For bigger files, encrypt the file in the repo and store only the key as a secret |

---

<p align="center">
  <a href="04-log-masking-what-it-catches-and-what.md">⬅️ Log masking: what it catches, and what it misses</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="06-the-secret-you-get-for-free-github.md"><b>Next: The secret you get for free: `GITHUB_TOKEN` ➡️</b></a>
</p>
