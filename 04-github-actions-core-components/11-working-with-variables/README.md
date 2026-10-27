---
type: Tutorial
title: Working with Variables (Hands-On)
description: Stop hard-coding values - env at workflow, job and step level and which one wins, $VAR versus ${{ env.VAR }}, default GITHUB_ variables, setting values at runtime with $GITHUB_ENV, and configuration variables stored in Settings with the vars context.
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
  <b>Lesson 11 of 14</b> &nbsp;·&nbsp; ⏱️ 32 min &nbsp;·&nbsp; 🛠️ Hands-on &nbsp;·&nbsp; ⭐ Fundamental
</p>

# 🔤 Working with Variables

> [!IMPORTANT]
> **Almost every real workflow uses variables.** Image names, registries, versions, URLs, feature flags: they're what turn a demo into something you can reuse, change safely and share with a team. Learn this lesson properly and the rest of GitHub Actions gets easier.

## 🗺️ In this topic

14 subtopics, about 33 minutes in all. Read them in order, or jump to the one you need.

| # | Subtopic | Time |
|---|---|---|
| 1 | 🕵️ [**Spot the problems**](01-spot-the-problems.md) | 2 min |
| 2 | 🧱 [**Fix 1: step-level `env`**](02-fix-1-step-level-env.md) | 1 min |
| 3 | 📦 [**Fix 2: job-level `env`**](03-fix-2-job-level-env.md) | 1 min |
| 4 | 📜 [**Fix 3: workflow-level `env`**](04-fix-3-workflow-level-env.md) | 1 min |
| 5 | 🥇 [**Which one wins?**](05-which-one-wins.md) | 2 min |
| 6 | 💲 [**`$VAR` or `${{ env.VAR }}`?**](06-var-or-env-var.md) | 2 min |
| 7 | 🧠 [**Inside `${{ }}`: the expression language and its contexts**](07-inside-the-expression-language-and-its-contexts.md) | 13 min |
| 8 | 🎁 [**Variables you get for free**](08-variables-you-get-for-free.md) | 1 min |
| 9 | ✍️ [**Setting a variable while the job runs**](09-setting-a-variable-while-the-job-runs.md) | 1 min |
| 10 | ⚙️ [**Configuration variables: values that live in Settings**](10-configuration-variables-values-that-live-in-settings.md) | 2 min |
| 11 | 🔀 [**`env` or `vars`? (and `secrets`)**](11-env-or-vars-and-secrets.md) | 2 min |
| 12 | 🪤 [**Common mistakes**](12-common-mistakes.md) | 2 min |
| 13 | 🛠️ [**Try it yourself**](13-try-it-yourself.md) | 1 min |
| 14 | ✅ [**Checkpoint**](14-checkpoint.md) | 2 min |

<p align="center">
  <a href="01-spot-the-problems.md"><b>▶️ Start with Spot the problems</b></a>
</p>

## 🎯 What you learned

- **Don't repeat values.** Name them once with **`env:`** at the step, job or workflow level
- **The most specific level wins**, and an override stays inside its own scope
- **`$VAR`** is read by the shell inside `run:`; **`${{ env.VAR }}`** is filled in by GitHub and works in `with:`, `name:` and `if:`
- Inside **`${{ }}`** every value starts with a **context**: `github`, `env`, `vars`, `secrets`, `runner`, `job`, `steps`, `needs`, `matrix`, `strategy`, `inputs`
- GitHub gives you **default variables** like `GITHUB_SHA` and `RUNNER_OS` for free
- **`$GITHUB_ENV`** sets a variable for **later steps** in the same job
- **Configuration variables** (`vars`) live in Settings at org, repo or environment level, with **environment winning**
- **Passwords and tokens are never variables.** They're **secrets**

---

<p align="center">
  <a href="../10-storing-workflow-data-as-artifacts/README.md">⬅️ Artifacts</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="../index.md">📚 Chapter 4</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="../12-working-with-repository-secrets/README.md"><b>Next: Repository Secrets ➡️</b></a>
</p>
