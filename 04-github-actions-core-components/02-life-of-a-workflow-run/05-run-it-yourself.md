---
type: Tutorial
title: "Life of a Workflow Run: Run it yourself"
description: "This repository ships the workflow from the picture: 04-core-components.yml. It tests the sample app on Ubuntu, Windows and macOS."
tags: [github-actions, workflow-run, matrix, logs, artifacts, hands-on]
status: stable
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-07T00:00:00Z }
sources:
  - id: gh-workflow-syntax
    resource: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
    title: Workflow syntax for GitHub Actions
  - id: gh-logs
    resource: https://docs.github.com/en/actions/how-tos/monitor-workflows/use-workflow-run-logs
    title: Using workflow run logs
  - id: gh-artifacts
    resource: https://docs.github.com/en/actions/concepts/workflows-and-actions/workflow-artifacts
    title: Workflow artifacts
---

<p align="center">
  <a href="README.md">📂 <b>Life of a Workflow Run</b></a> &nbsp;·&nbsp; Lesson 2 · Part 5 of 7 &nbsp;·&nbsp; ⏱️ 4 min
</p>

# 🛠️ Run it yourself

This repository ships the workflow from the picture: [`04-core-components.yml`](../../.github/workflows/04-core-components.yml). It tests the [sample app](../../sample-app/) on Ubuntu, Windows and macOS.

```yaml
jobs:
  unit-testing:
    name: unit-testing (${{ matrix.os }})
    runs-on: ${{ matrix.os }}
    strategy:
      fail-fast: false
      matrix:
        os: [ubuntu-latest, windows-latest, macos-latest]
    steps:
      - name: Check out the repository
        uses: actions/checkout@v7

      - name: Set up Python
        uses: actions/setup-python@v7
        with:
          python-version: '3.13'

      - name: Run unit tests
        run: python -m unittest discover -v 2>&1 | tee test-report.txt

      - name: Upload the test report
        uses: actions/upload-artifact@v7
        with:
          name: test-report-${{ runner.os }}
          path: sample-app/test-report.txt
          retention-days: 7
```

It has one more step than the picture: the last one saves the test output as an **artifact**, so there's something to download afterwards.

## 1️⃣ Start a run

In your fork, open the **Actions** tab, choose **04 - Core Components** in the left sidebar, then **Run workflow** → **Run workflow**.

## 2️⃣ Watch three runners start

Click the new run. On the left you'll see three jobs:

```text
unit-testing (ubuntu-latest)     🟡
unit-testing (windows-latest)    🟡
unit-testing (macos-latest)      🟡
```

They turn green one at a time, not together. Note which one finishes first.

## 3️⃣ Read a job's logs

Click **unit-testing (ubuntu-latest)**. Each step is a collapsible section.

| | Section | What to look for |
|---|---|---|
| ⚙️ | **Set up job** | The runner image and its version. This is GitHub telling you which machine you got |
| 📥 | **Check out the repository** | The commit that was fetched |
| 🐍 | **Set up Python** | The exact Python version installed |
| 🧪 | **Run unit tests** | Five tests, each ending in `ok` |
| 🧹 | **Complete job** | Clean-up before the machine is destroyed |

Now open the same step in the **Windows** job and compare. Same steps, same result, a completely different machine.

## 4️⃣ Download the artifacts

Go back to the run's **Summary** page and scroll to **Artifacts**. There are three, one per runner:

```text
test-report-Linux
test-report-Windows
test-report-macOS
```

Download one and open it. It's the output you just read in the log, saved as a file. The runner that produced it no longer exists, but the artifact does.

## 5️⃣ Break it on purpose

Edit [`sample-app/greeter/core.py`](../../sample-app/greeter/core.py) in your fork so that a test fails (change `Hello` to `Hi`), commit, then run the workflow again by hand.

| | Watch for | Why |
|---|---|---|
| ❌ | All three jobs fail | The bug isn't specific to one operating system |
| ⏭️ | **Upload the test report** is skipped | Steps after a failed step don't run |
| 📭 | No artifacts on the summary page | The upload step never happened |
| ❌ | The run is marked failed | One failed job is enough |

Put `Hello` back when you're done.

> [!TIP]
> When a workflow misbehaves, the fastest route is always the same: **run → failed job → red step → last lines of its log**. The error is almost always in the final screenful.

---

<p align="center">
  <a href="04-how-results-roll-up.md">⬅️ How results roll up</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="06-where-everything-lives.md"><b>Next: Where everything lives ➡️</b></a>
</p>
