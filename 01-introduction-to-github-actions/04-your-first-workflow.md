---
type: Tutorial
title: Your First Workflow (Hands-On)
description: Run the Hello, Actions workflow that ships in this repository, read its logs, trigger it by hand, and break it on purpose.
resource: /.github/workflows/01-hello-world.yml
tags: [github-actions, hands-on, hello-world, workflow-dispatch, logs]
status: stable
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-07T00:00:00Z }
sources:
  - id: gh-quickstart
    resource: https://docs.github.com/en/actions/get-started/quickstart
    title: Quickstart for GitHub Actions
  - id: gh-summary
    resource: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-commands
    title: Workflow commands (job summaries)
---

<p align="center">
  <b>Lesson 4 of 5</b> &nbsp;·&nbsp; ⏱️ 15 min hands-on &nbsp;·&nbsp; 🛠️ Keyboard required
</p>

# 🚀 Your First Workflow

Enough reading. Time to make a machine in the cloud do your bidding.

This repository ships with a real workflow, [`.github/workflows/01-hello-world.yml`](../.github/workflows/01-hello-world.yml). You're going to run it, read it, and break it.

## 🎒 Before you start

- [ ] A GitHub account
- [ ] Your own copy of this repository (**Fork** it, top right of the repo page)
- [ ] Actions enabled on your fork: open the **Actions** tab and click **I understand my workflows, go ahead and enable them**

> [!NOTE]
> GitHub disables workflows on fresh forks as a safety measure. That one click turns them on.

## 📄 The workflow

```yaml
name: 01 - Hello, Actions

on:
  push:
    branches: [main]
  workflow_dispatch:
    inputs:
      who:
        description: Who should we greet?
        required: false
        default: World

permissions:
  contents: read

jobs:
  say-hello:
    runs-on: ubuntu-latest
    steps:
      - name: Greet
        env:
          WHO: ${{ inputs.who || 'World' }}
        run: echo "Hello, $WHO! This runner is all yours."

      - name: Check out the repository
        uses: actions/checkout@v7

      - name: Look around
        run: |
          echo "Triggered by : $GITHUB_EVENT_NAME"
          echo "Repository   : $GITHUB_REPOSITORY"
          echo "Branch       : $GITHUB_REF_NAME"
          echo "Commit       : $GITHUB_SHA"
          echo "Runner OS    : $RUNNER_OS"
          echo "--- files in the workspace ---"
          ls -1

      - name: Write a job summary
        env:
          WHO: ${{ inputs.who || 'World' }}
        run: |
          {
            echo "## Hello, $WHO!"
            echo ""
            echo "| | |"
            echo "|---|---|"
            echo "| Event | \`$GITHUB_EVENT_NAME\` |"
            echo "| Branch | \`$GITHUB_REF_NAME\` |"
            echo "| Runner | \`$RUNNER_OS\` |"
          } >> "$GITHUB_STEP_SUMMARY"
```

## 🔎 What each part teaches

| Lines | Concept | Why it's there |
|---|---|---|
| `on.push` | Event | Runs on every push to `main` |
| `on.workflow_dispatch` | Event + input | Adds a **Run workflow** button with a text box |
| `permissions` | Security | The run's token can only read the repo |
| `Greet` | `run` + `env` | The form input reaches the shell safely through an environment variable |
| `Check out` | `uses` | Without it, the runner has **no copy of your code** |
| `Look around` | Default variables | GitHub hands every step facts like `$GITHUB_SHA` |
| `Write a job summary` | `$GITHUB_STEP_SUMMARY` | Markdown appended to this file appears on the run page |

> [!IMPORTANT]
> A fresh runner is an empty machine. Your repository is **not** on it until `actions/checkout` puts it there. Forgetting checkout is the classic first-week mistake.

## ▶️ Exercise 1: Run it with the button

1. Open the **Actions** tab of your fork
2. In the left sidebar, click **01 - Hello, Actions**
3. Click **Run workflow** (right side)
4. Type your name in **Who should we greet?**
5. Click the green **Run workflow** button

A new run appears with a spinning 🟡. Within about twenty seconds it turns ✅.

## 📖 Exercise 2: Read the logs

Click the run, then click the **say-hello** job. You'll see this:

```text
✅ Set up job
✅ Greet
✅ Check out the repository
✅ Look around
✅ Write a job summary
✅ Post Check out the repository
✅ Complete job
```

Expand **Greet** and find your name. Then expand **Look around** and compare it to the file list of the repo.

<details>
<summary><b>🤔 Wait, I didn't write "Set up job" or "Post Check out the repository"</b></summary>

<br>

Correct. GitHub adds them.

- **Set up job** boots the runner and downloads the actions you referenced
- **Post Check out the repository** is cleanup that the checkout action registered for itself
- **Complete job** tears everything down

</details>

Now scroll to the bottom of the run's **Summary** page. That table is the job summary your last step wrote. 🎉

## ⚡ Exercise 3: Trigger it with a push

Events, not buttons, are the real power. Make any small edit (add a line to a file) and push it to `main`:

```bash
git commit --allow-empty -m "Wake up the robot"
git push
```

Back in the Actions tab a new run has started on its own, and this time **Look around** reports `Triggered by : push`.

> [!TIP]
> Notice the greeting says `World`. A push has no form, so `inputs.who` is empty and the expression `${{ inputs.who || 'World' }}` falls back to the default.

## 💥 Exercise 4: Break it on purpose

You learn a tool properly when you see it fail. In `01-hello-world.yml`, add this as the **second** step, then push:

```yaml
      - name: Fail on purpose
        run: exit 1
```

Observe three things:

1. The run turns ❌ and GitHub emails you
2. Every step **after** the failing one is skipped
3. The log shows `Process completed with exit code 1`

> [!NOTE]
> This is the entire basis of CI. A command that exits with a non-zero code fails the step, which fails the job, which fails the run. Test runners exit non-zero when a test fails. That's all the magic there is.

Remove the failing step and push again to get back to green.

## 🧯 Something went wrong?

| Symptom | Likely cause |
|---|---|
| Workflow isn't listed in the Actions tab | File isn't in `.github/workflows/`, or doesn't end in `.yml` |
| "Invalid workflow file" | Indentation. Check for tabs and misaligned keys |
| No **Run workflow** button | `workflow_dispatch` is missing, or the file isn't on the default branch |
| Nothing runs on push | You pushed to a branch other than `main` |
| Actions tab shows a big enable button | Workflows are disabled on your fork; click it |

## 🎯 What you learned

- How to run a workflow by **button** and by **push**
- How to read a run: jobs, steps, logs, summary
- Why **checkout** is almost always your first real step
- That a **non-zero exit code** is what makes a run fail

---

<p align="center">
  <a href="03-anatomy-of-a-workflow.md">⬅️ Anatomy of a Workflow</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="index.md">📚 Chapter 1</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="05-cheat-sheet-and-quiz.md"><b>Next: Cheat Sheet & Quiz ➡️</b></a>
</p>
