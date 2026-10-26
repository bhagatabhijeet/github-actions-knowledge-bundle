---
type: Reference
title: Chapter 4 Cheat Sheet and Quiz
description: The core components on one page - workflow, job, step, runner, how a run unfolds, hosted versus self-hosted - followed by an eight-question self-check.
tags: [github-actions, core-components, runners, cheat-sheet, quiz, recap]
status: stable
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-07T00:00:00Z }
sources:
  - id: gh-understand
    resource: https://docs.github.com/en/actions/get-started/understand-github-actions
    title: Understanding GitHub Actions
  - id: gh-workflow-syntax
    resource: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
    title: Workflow syntax for GitHub Actions
---

<p align="center">
  <b>Lesson 7 of 7</b> &nbsp;·&nbsp; ⏱️ 5 min &nbsp;·&nbsp; 🏁 Chapter finale
</p>

# 📋 Chapter 4 Cheat Sheet & Quiz

## 🧱 The four components

| | Component | It is... | In YAML | Rule to remember |
|---|---|---|---|---|
| 📜 | **Workflow** | An automated process in one file | `.github/workflows/*.yml` | Many per repository |
| 📦 | **Job** | Steps that share a machine | `jobs.<id>:` | Parallel by default |
| 👣 | **Step** | One action or command | `- uses:` / `- run:` | In series, top to bottom |
| 🖥️ | **Runner** | The machine for a job | `runs-on:` | One per job, fresh each time |
| 🧩 | **Action** | A reusable, packaged step | `- uses: owner/repo@version` | Pin third-party actions to a full SHA |

> [!IMPORTANT]
> **A runner starts empty.** Make `actions/checkout` the first step of any job that reads your files. Add `fetch-depth: 0` when you need full history.

> [!TIP]
> **`run: |`** keeps each line as its own command; **`run: >`** folds them into one. Lines in one step share a shell; separate steps do not. Tools you install vanish with the runner.

## 🎬 A run in six stages

| 1 | 2 | 3 | 4 | 5 | 6 |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 🔔 | 📋 | 🖥️ | 👣 | 📡 | 🧹 |
| Event | Queue | Provision | Execute | Report | Clean up |

## 🚦 How results roll up

| Level | Passes when |
|---|---|
| 👣 Step | Its command or action exits successfully |
| 📦 Job | Every step passes |
| 📜 Workflow run | Every job passes |

## ✖️ Matrix in four lines

```yaml
runs-on: ${{ matrix.os }}
strategy:
  matrix:
    os: [ubuntu-latest, windows-latest, macos-latest]
```

| Setting | Effect |
|---|---|
| `matrix:` | One job definition becomes one job per value |
| `fail-fast: true` (default) | A failing matrix job cancels the rest |
| `fail-fast: false` | Every matrix job runs to the end |

## 🖥️ Hosted vs self-hosted

| | ☁️ GitHub-hosted | 🏢 Self-hosted |
|---|---|---|
| Maintained by | GitHub | You |
| State | Clean VM per job | Persists between jobs |
| Extra software | Install in a step, every run | Install once, it stays |
| Network | Public cloud | Yours |
| Longest job | 6 hours | 5 days |
| `runs-on` | `ubuntu-latest` | `self-hosted` |

## 🗺️ Finding your way in the Actions tab

| You want | Path |
|---|---|
| A step's log | Actions → run → job → expand the step |
| Why it failed | Run → red job → red step → last lines |
| Files it produced | Run → Summary → Artifacts |
| To try again | Run → Re-run jobs |

## 🏆 Golden rules

> [!IMPORTANT]
> 1. **Jobs in parallel, steps in series.** Most surprises come from forgetting one half.
> 2. **One job, one runner, nothing shared.** Pass files between jobs with artifacts.
> 3. **The runner is disposable.** Only logs and artifacts survive.
> 4. **Write the job once, multiply it with a matrix.**
> 5. **Start hosted.** Self-host for a named reason, and not on public repositories.

## 🧠 Quiz

<details>
<summary><b>1. Name the four core components, from largest to smallest container.</b></summary>

<br>

Workflow, job, step. The fourth, the runner, isn't inside the others: it's the machine each job runs on.

</details>

<details>
<summary><b>2. A workflow has two jobs and no <code>needs:</code>. One job has four steps. What runs in parallel and what runs in series?</b></summary>

<br>

The two jobs run in parallel on separate runners. The four steps run in series on their job's runner.

</details>

<details>
<summary><b>3. A matrix lists three operating systems and two Python versions. How many runners are provisioned?</b></summary>

<br>

Six. The matrix produces every combination, three times two, and each job gets its own runner.

</details>

<details>
<summary><b>4. Two of three matrix jobs pass and one fails. What is the status of the workflow run?</b></summary>

<br>

Failed. A run passes only when every job passes.

</details>

<details>
<summary><b>5. Step 2 of 5 fails. What happens to steps 3, 4 and 5?</b></summary>

<br>

They are skipped, and the job is marked as failed.

</details>

<details>
<summary><b>6. The runner was destroyed an hour ago. Name two things from the job you can still get.</b></summary>

<br>

The logs for every step, and any artifacts the job uploaded.

</details>

<details>
<summary><b>7. True or false: you cannot install extra software on a GitHub-hosted runner.</b></summary>

<br>

False. You can install it in a step. It just disappears with the machine when the job ends.

</details>

<details>
<summary><b>8. Give two good reasons to use a self-hosted runner.</b></summary>

<br>

Any two of: access to a private network, special hardware such as a GPU, jobs longer than six hours, or policy about where builds must run.

</details>

### 📊 How did you do?

| Score | Verdict |
|---|---|
| 8 | 🏆 You can read a run like a timeline |
| 5 to 7 | 💪 Strong. Revisit the lessons you missed |
| 0 to 4 | 🔁 Redo the [hands-on lesson](02-life-of-a-workflow-run.md); watching a run beats reading about one |

## 🎉 Chapter complete

You can point at any line of a workflow and say which component it is, describe what happens between a push and a green tick, and choose the right kind of runner.

> [!NOTE]
> **More chapters are on the way.** This guide grows one topic at a time. Check the [change log](../log.md) to see what's new.

---

<p align="center">
  <a href="06-multiline-commands-and-third-party-tools.md">⬅️ Multi-line Commands</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="index.md">📚 Chapter 4</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="../README.md"><b>🏠 Back to Home</b></a>
</p>
