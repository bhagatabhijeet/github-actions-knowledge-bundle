---
type: Tutorial
title: "Anatomy of a Pipeline: The matrix: one job, many variations"
description: "\"Does it work on Python 3.12, 3.13 and 3.14?\" Don't copy the job three times. Describe the variations and let GitHub multiply."
tags: [ci-cd, pipeline, stages, artifacts, matrix, needs, caching]
status: stable
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-07T00:00:00Z }
sources:
  - id: gh-syntax
    resource: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
    title: Workflow syntax for GitHub Actions
  - id: gh-artifacts
    resource: https://docs.github.com/en/actions/concepts/workflows-and-actions/workflow-artifacts
    title: Workflow artifacts
  - id: gh-cache
    resource: https://docs.github.com/en/actions/concepts/workflows-and-actions/dependency-caching
    title: Dependency caching
---

<p align="center">
  <a href="README.md">📂 <b>Anatomy of a Pipeline</b></a> &nbsp;·&nbsp; Lesson 4 · Part 4 of 7 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# 🧮 The matrix: one job, many variations

"Does it work on Python 3.12, 3.13 *and* 3.14?" Don't copy the job three times. Describe the variations and let GitHub multiply.

```yaml
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ['3.12', '3.13', '3.14']
    steps:
      - uses: actions/checkout@v7
      - uses: actions/setup-python@v7
        with:
          python-version: ${{ matrix.python-version }}
      - run: python -m unittest discover -v
```

One job definition becomes three parallel jobs, each with a different value in `${{ matrix.python-version }}`.

> [!TIP]
> Add a second key, such as `os: [ubuntu-latest, windows-latest]`, and you get every combination: 3 versions × 2 systems = 6 jobs.

---

<p align="center">
  <a href="03-fan-out-and-fan-in.md">⬅️ Fan-out and fan-in</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="05-carrying-things-between-stages.md"><b>Next: Carrying things between stages ➡️</b></a>
</p>
