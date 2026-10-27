---
type: Reference
title: "Chapter 1 Cheat Sheet and Quiz: Quiz"
description: "Eight questions. No peeking until you've committed to an answer."
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
  <a href="README.md">📂 <b>Chapter 1 Cheat Sheet and Quiz</b></a> &nbsp;·&nbsp; Lesson 5 · Part 5 of 6 &nbsp;·&nbsp; ⏱️ 3 min
</p>

# 🧠 Quiz

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

## 📊 How did you do?

| Score | Verdict |
|---|---|
| 8 | 🏆 Ready for Chapter 2 |
| 5 to 7 | 💪 Solid. Skim the lessons you missed |
| 0 to 4 | 🔁 Re-read [Core Concepts](../02-core-concepts/README.md); it unlocks the rest |

---

<p align="center">
  <a href="04-golden-rules.md">⬅️ Golden rules</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="06-chapter-complete.md"><b>Next: Chapter complete ➡️</b></a>
</p>
