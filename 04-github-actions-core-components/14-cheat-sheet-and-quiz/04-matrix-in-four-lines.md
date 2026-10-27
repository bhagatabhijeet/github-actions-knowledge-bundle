---
type: Reference
title: "Chapter 4 Cheat Sheet and Quiz: Matrix in four lines"
description: "A matrix turns one job definition into one job per value, and fail-fast decides whether one failure cancels the rest."
tags: [github-actions, core-components, runners, cheat-sheet, quiz, recap]
status: stable
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-26T00:00:00Z }
sources:
  - id: gh-understand
    resource: https://docs.github.com/en/actions/get-started/understand-github-actions
    title: Understanding GitHub Actions
  - id: gh-workflow-syntax
    resource: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
    title: Workflow syntax for GitHub Actions
---

<p align="center">
  <a href="README.md">📂 <b>Chapter 4 Cheat Sheet and Quiz</b></a> &nbsp;·&nbsp; Lesson 14 · Part 4 of 9 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# ✖️ Matrix in four lines

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

---

<p align="center">
  <a href="03-how-results-roll-up.md">⬅️ How results roll up</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="05-hosted-vs-self-hosted.md"><b>Next: Hosted vs self-hosted ➡️</b></a>
</p>
