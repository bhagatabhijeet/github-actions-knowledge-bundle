---
type: Tutorial
title: "Working with Variables: `env` or `vars`? (and `secrets`)"
description: "👉 Lesson 12 covers secrets in full."
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
  <a href="README.md">📂 <b>Working with Variables</b></a> &nbsp;·&nbsp; Lesson 11 · Part 11 of 14 &nbsp;·&nbsp; ⏱️ 2 min
</p>

# 🔀 `env` or `vars`? (and `secrets`)

| | `env:` in YAML | `vars` in Settings | `secrets` in Settings |
|---|---|---|---|
| Where it's stored | The workflow file, in Git | GitHub settings | GitHub settings, **encrypted** |
| Change it | Commit | Settings or `gh variable set` | Settings or `gh secret set` |
| Shown in logs | Yes | Yes | **No**, masked as `***` |
| Good for | Values tied to this workflow | Usernames, URLs, regions, flags | Passwords, tokens, keys |
| Our example | `IMAGE_NAME` | `DOCKER_USERNAME`, `CONTAINER_REGISTRY` | The Docker password |

## 🔐 A preview: fixing the password

👉 [Lesson 12](../12-working-with-repository-secrets/README.md) covers secrets in full.

`vars` are **plain text**: anyone with read access sees them, and they print in logs. The password needs a **secret** instead:

```yaml
    - name: Docker Login
      run: echo "$DOCKER_PASSWORD" | docker login --username "$DOCKER_USERNAME" --password-stdin
      env:
        DOCKER_PASSWORD: ${{ secrets.DOCKER_PASSWORD }}
```

> [!CAUTION]
> **If a password was ever committed, change the password.** Deleting it from the file isn't enough: it stays in the Git history and in any fork or clone made since.

---

<p align="center">
  <a href="10-configuration-variables-values-that-live-in-settings.md">⬅️ Configuration variables: values that live in Settings</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="12-common-mistakes.md"><b>Next: Common mistakes ➡️</b></a>
</p>
