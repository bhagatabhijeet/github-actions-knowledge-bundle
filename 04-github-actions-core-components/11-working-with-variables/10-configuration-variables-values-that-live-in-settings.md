---
type: Tutorial
title: "Working with Variables: Configuration variables: values that live in Settings"
description: "env: lives in the YAML, so changing it means a commit. Configuration variables live in the repository's settings, so you can change them without touching the workflow, and share them across many workflows."
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
  <a href="README.md">📂 <b>Working with Variables</b></a> &nbsp;·&nbsp; Lesson 11 · Part 10 of 14 &nbsp;·&nbsp; ⏱️ 2 min
</p>

# ⚙️ Configuration variables: values that live in Settings

`env:` lives in the YAML, so changing it means a commit. **Configuration variables** live in the repository's settings, so you can change them without touching the workflow, and share them across many workflows.

**Create one:** **Settings → Secrets and variables → Actions → Variables tab → New repository variable**. Or with the CLI:

```bash
gh variable set DOCKER_USERNAME --body "dockerUsername"
gh variable set CONTAINER_REGISTRY --body "docker.io"
gh variable list
```

**Use it** with the `vars` context:

```yaml
env:
  CONTAINER_REGISTRY: ${{ vars.CONTAINER_REGISTRY }}
  DOCKER_USERNAME: ${{ vars.DOCKER_USERNAME }}
  IMAGE_NAME: imageName
```

| Level | Set in | Shared with | Precedence |
|---|---|---|---|
| 🏢 Organisation | Org settings | Chosen repositories | Lowest |
| 📁 Repository | Repo settings | Every workflow in the repo | Middle |
| 🌍 Environment | Repo settings → **Environments** | Jobs that use `environment: <name>` | **Highest** |

> [!TIP]
> **Give a fallback** so a workflow still runs before anyone sets the variable: `${{ vars.CONTAINER_REGISTRY || 'docker.io' }}`. An unset variable is an empty string, not an error.

Environment-level variables are how one workflow deploys to **staging** and **production** with different values:

```yaml
  deploy:
    runs-on: ubuntu-latest
    environment: production        # 👈 vars now come from the "production" environment first
    steps:
      - run: echo "Deploying to ${{ vars.APP_URL }}"
```

---

<p align="center">
  <a href="09-setting-a-variable-while-the-job-runs.md">⬅️ Setting a variable while the job runs</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="11-env-or-vars-and-secrets.md"><b>Next: `env` or `vars`? (and `secrets`) ➡️</b></a>
</p>
