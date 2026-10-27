---
type: Tutorial
title: "Your First CI Pipeline: The cast"
description: "The app is deliberately boring, so the pipeline can be the star:"
resource: /.github/workflows/02-ci-basics.yml
tags: [ci-cd, hands-on, pipeline, matrix, artifacts, python, pull-requests]
status: stable
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-07T00:00:00Z }
sources:
  - id: gh-python
    resource: https://docs.github.com/en/actions/tutorials/build-and-test-code/python
    title: Building and testing Python
  - id: gh-artifacts
    resource: https://docs.github.com/en/actions/tutorials/store-and-share-data
    title: Store and share data with workflow artifacts
  - id: gh-concurrency
    resource: https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/control-workflow-concurrency
    title: Control the concurrency of workflows and jobs
---

<p align="center">
  <a href="README.md">📂 <b>Your First CI Pipeline</b></a> &nbsp;·&nbsp; Lesson 5 · Part 1 of 9 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# 🧰 The cast

| | File | Role |
|---|---|---|
| 🐍 | [`sample-app/greeter/core.py`](../../sample-app/greeter/core.py) | The app: two tiny functions |
| 🧪 | [`sample-app/tests/test_core.py`](../../sample-app/tests/test_core.py) | Five unit tests |
| 📋 | [`sample-app/requirements-dev.txt`](../../sample-app/requirements-dev.txt) | Dev tools (the Ruff linter) |
| ⚙️ | [`.github/workflows/02-ci-basics.yml`](../../.github/workflows/02-ci-basics.yml) | The pipeline |

The app is deliberately boring, so the pipeline can be the star:

```python
def greet(name: str = "World") -> str:
    """Return a friendly greeting, falling back to World for blank names."""
    cleaned = name.strip()
    return f"Hello, {cleaned or 'World'}!"
```

> [!NOTE]
> You don't need to know Python. Every idea here transfers directly to Node.js, Java, Go or anything else. Only the commands inside `run:` change.

---

<p align="center">
  <a href="README.md">⬅️ Overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="02-the-pipeline-you-re-about-to-run.md"><b>Next: The pipeline you're about to run ➡️</b></a>
</p>
