---
type: Tutorial
title: "Configuring the Checkout Action: Configuring it with `with:`"
description: "Checkout takes inputs. These are the ones you'll actually use:"
tags: [github-actions, actions, checkout, hands-on, fetch-depth, sparse-checkout]
status: stable
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-25T00:00:00Z }
sources:
  - id: checkout-repo
    resource: https://github.com/actions/checkout
    title: actions/checkout README
  - id: gh-workflow-syntax
    resource: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
    title: Workflow syntax for GitHub Actions
---

<p align="center">
  <a href="README.md">📂 <b>Configuring the Checkout Action</b></a> &nbsp;·&nbsp; Lesson 5 · Part 4 of 7 &nbsp;·&nbsp; ⏱️ 3 min
</p>

# ⚙️ Configuring it with `with:`

Checkout takes inputs. These are the ones you'll actually use:

| Input | Default | Set it when you need to... | Example |
|---|---|---|---|
| `fetch-depth` | `1` | Get full history for tags, changelogs or `git describe` | `fetch-depth: 0` (everything) |
| `ref` | The triggering commit | Build a different branch, tag or SHA | `ref: release/2.0` |
| `path` | Workspace root | Put the code in a subfolder | `path: app` |
| `repository` | This repo | Check out **another** repository | `repository: my-org/shared-config` |
| `token` | `GITHUB_TOKEN` | Read a **private** other repo, or push changes that start new workflows | `token: ${{ secrets.MY_PAT }}` |
| `submodules` | `false` | Include git submodules | `submodules: recursive` |
| `lfs` | `false` | Download Git LFS files | `lfs: true` |
| `sparse-checkout` | Off | Fetch only some folders of a large monorepo | see below |
| `fetch-tags` | `false` | Get tags without full history | `fetch-tags: true` |
| `persist-credentials` | `true` | **Not** leave the token behind for later steps | `persist-credentials: false` |
| `clean` | `true` | Keep files from earlier jobs (self-hosted runners) | `clean: false` |

## 🍳 Recipes

**Full history, for versioning or changelogs**

```yaml
- uses: actions/checkout@v7
  with:
    fetch-depth: 0
```

**Two repositories side by side**

```yaml
- uses: actions/checkout@v7          # this repo → ./
- uses: actions/checkout@v7
  with:
    repository: my-org/shared-config # another repo → ./config
    path: config
    token: ${{ secrets.CONFIG_REPO_TOKEN }}   # needed only if it's private
```

**Just the folders you need from a monorepo**

```yaml
- uses: actions/checkout@v7
  with:
    sparse-checkout: |
      services/payments
      shared/lib
```

**Safer default for jobs that never push**

```yaml
- uses: actions/checkout@v7
  with:
    persist-credentials: false   # later steps can't reuse the token
```

> [!WARNING]
> **Only check out what you trust.** With `pull_request_target`, checking out the pull request's code (`ref: ${{ github.event.pull_request.head.sha }}`) runs a stranger's code with your secrets. Use plain `pull_request` for running tests on contributions.

---

<p align="center">
  <a href="03-the-fix-one-line.md">⬅️ The fix: one line</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="05-try-it-yourself.md"><b>Next: Try it yourself ➡️</b></a>
</p>
