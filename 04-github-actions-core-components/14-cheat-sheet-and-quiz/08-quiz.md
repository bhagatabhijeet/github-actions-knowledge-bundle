---
type: Reference
title: "Chapter 4 Cheat Sheet and Quiz: Quiz"
description: "Workflow, job, step. The fourth, the runner, isn't inside the others: it's the machine each job runs on."
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
  <a href="README.md">📂 <b>Chapter 4 Cheat Sheet and Quiz</b></a> &nbsp;·&nbsp; Lesson 14 · Part 8 of 9 &nbsp;·&nbsp; ⏱️ 3 min
</p>

# 🧠 Quiz

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

## 📊 How did you do?

| Score | Verdict |
|---|---|
| 8 | 🏆 You can read a run like a timeline |
| 5 to 7 | 💪 Strong. Revisit the lessons you missed |
| 0 to 4 | 🔁 Redo the [hands-on lesson](../02-life-of-a-workflow-run/README.md); watching a run beats reading about one |

---

<p align="center">
  <a href="07-golden-rules.md">⬅️ Golden rules</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="09-chapter-complete.md"><b>Next: Chapter complete ➡️</b></a>
</p>
