---
type: Reference
title: "Chapter 4 Cheat Sheet and Quiz: Hosted vs self-hosted"
description: "Hosted vs self-hosted, part 5 of 9 of Chapter 4 Cheat Sheet and Quiz."
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
  <a href="README.md">📂 <b>Chapter 4 Cheat Sheet and Quiz</b></a> &nbsp;·&nbsp; Lesson 14 · Part 5 of 9 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# 🖥️ Hosted vs self-hosted

| | ☁️ GitHub-hosted | 🏢 Self-hosted |
|---|---|---|
| Maintained by | GitHub | You |
| State | Clean VM per job | Persists between jobs |
| Extra software | Install in a step, every run | Install once, it stays |
| Network | Public cloud | Yours |
| Longest job | 6 hours | 5 days |
| `runs-on` | `ubuntu-latest` | `self-hosted` |

---

<p align="center">
  <a href="04-matrix-in-four-lines.md">⬅️ Matrix in four lines</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="06-finding-your-way-in-the-actions-tab.md"><b>Next: Finding your way in the Actions tab ➡️</b></a>
</p>
