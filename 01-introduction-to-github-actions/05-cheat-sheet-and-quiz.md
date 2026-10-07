---
type: Reference
title: Chapter 1 Cheat Sheet and Quiz
description: Everything from Chapter 1 on one page - vocabulary, YAML keys and default variables - followed by an eight-question self-check.
tags: [github-actions, cheat-sheet, quiz, recap]
status: stable
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-07T00:00:00Z }
sources:
  - id: gh-syntax
    resource: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
    title: Workflow syntax for GitHub Actions
  - id: gh-variables
    resource: https://docs.github.com/en/actions/reference/workflows-and-actions/variables
    title: Variables reference
---

<p align="center">
  <b>Lesson 5 of 5</b> &nbsp;·&nbsp; ⏱️ 5 min &nbsp;·&nbsp; 🏁 Chapter finale
</p>

# 📋 Chapter 1 Cheat Sheet & Quiz

Bookmark this page. It's the one you'll come back to.

## 🗣️ Vocabulary

| | Term | Meaning |
|---|---|---|
| 🔔 | **Event** | What happened that starts a workflow |
| 📜 | **Workflow** | A YAML file in `.github/workflows/` |
| 🏃 | **Workflow run** | One execution of a workflow |
| 📦 | **Job** | Steps that share one runner; parallel by default |
| 👣 | **Step** | One task; sequential |
| 🧱 | **Action** | Reusable step logic, called with `uses:` |
| 🖥️ | **Runner** | The machine; fresh per job when GitHub-hosted |

## ⌨️ YAML keys

| Key | Level | Does |
|---|---|---|
| `name` | workflow | Display name |
| `on` | workflow | Events that trigger it |
| `permissions` | workflow / job | Limits the run's token |
| `jobs.<id>` | workflow | Defines a job |
| `runs-on` | job | Picks the runner |
| `needs` | job | Waits for other jobs |
| `steps` | job | Ordered list of tasks |
| `uses` / `with` | step | Run an action with inputs |
| `run` | step | Run shell commands |
| `env` | any | Environment variables |
| `if` | job / step | Conditional execution |

## 🧾 Default variables worth knowing

| Variable | Example value |
|---|---|
| `GITHUB_EVENT_NAME` | `push` |
| `GITHUB_REPOSITORY` | `octocat/hello-world` |
| `GITHUB_REF_NAME` | `main` |
| `GITHUB_SHA` | `8f3a1c...` |
| `GITHUB_ACTOR` | `octocat` |
| `GITHUB_WORKSPACE` | where checkout puts your code |
| `RUNNER_OS` | `Linux` |
| `GITHUB_STEP_SUMMARY` | file to append Markdown summaries to |

## 🏆 Golden rules

> [!IMPORTANT]
> 1. **Checkout first.** The runner starts empty.
> 2. **Jobs are parallel and isolated.** Use `needs` to order, artifacts to share.
> 3. **Non-zero exit = failure.** That's how a workflow knows.
> 4. **Quote your versions.** `'3.10'`, not `3.10`.
> 5. **Pin your actions.** `@v7`, never `@main`.
> 6. **Least privilege.** Start with `permissions: contents: read`.

## 🧠 Quiz

Eight questions. No peeking until you've committed to an answer.

<details>
<summary><b>1. Which folder must workflow files be in?</b></summary>

<br>

`.github/workflows/` (plural, with the leading dot).

</details>

<details>
<summary><b>2. Your workflow has jobs <code>a</code>, <code>b</code> and <code>c</code> with no <code>needs</code>. How many runners are used, and in what order do the jobs run?</b></summary>

<br>

Three runners, one per job, all started in parallel. There is no order.

</details>

<details>
<summary><b>3. What does <code>uses: actions/checkout@v7</code> do, and what happens without it?</b></summary>

<br>

It clones your repository onto the runner. Without it the workspace is empty, so any step that expects your files will fail.

</details>

<details>
<summary><b>4. Step 2 of 5 fails. What happens to steps 3, 4 and 5?</b></summary>

<br>

They're skipped, and the job is marked failed. (Later you'll learn `if: always()` to override this for cleanup steps.)

</details>

<details>
<summary><b>5. Which event adds a "Run workflow" button?</b></summary>

<br>

`workflow_dispatch`.

</details>

<details>
<summary><b>6. Why is <code>python-version: 3.10</code> a bug?</b></summary>

<br>

YAML parses unquoted `3.10` as the number `3.1`, so you'd get Python 3.1. Write `'3.10'`.

</details>

<details>
<summary><b>7. What is the difference between "GitHub Actions" and "an action"?</b></summary>

<br>

GitHub Actions is the whole automation platform. An action is a single reusable building block that a step calls with `uses:`.

</details>

<details>
<summary><b>8. Why pass a form input through <code>env:</code> instead of writing <code>${{ inputs.who }}</code> inside <code>run:</code>?</b></summary>

<br>

`${{ }}` is substituted into the script text before the shell runs, so a malicious value could inject commands. An environment variable is treated as data, not code.

</details>

### 📊 How did you do?

| Score | Verdict |
|---|---|
| 8 | 🏆 Ready for Chapter 2 |
| 5 to 7 | 💪 Solid. Skim the lessons you missed |
| 0 to 4 | 🔁 Re-read [Core Concepts](02-core-concepts.md); it unlocks the rest |

## 🎉 Chapter complete

You can now explain what GitHub Actions is, name its six building blocks, read a workflow file, and you've run one yourself.

Next up: **why** teams automate in the first place, and how the ideas of CI and CD turn a pile of workflows into a pipeline.

---

<p align="center">
  <a href="04-your-first-workflow.md">⬅️ Your First Workflow</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="../README.md">🏠 Home</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="../02-basics-of-ci-cd/01-what-is-ci-cd.md"><b>Next: Chapter 2, Basics of CI/CD ➡️</b></a>
</p>
