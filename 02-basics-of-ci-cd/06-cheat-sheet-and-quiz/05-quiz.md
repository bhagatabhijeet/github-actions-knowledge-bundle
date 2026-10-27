---
type: Reference
title: "Chapter 2 Cheat Sheet and Quiz: Quiz"
description: "They integrate small changes into the shared branch frequently, and every change is automatically built and tested."
tags: [ci-cd, cheat-sheet, quiz, recap]
status: stable
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-07T00:00:00Z }
sources:
  - id: gh-ci
    resource: https://docs.github.com/en/actions/get-started/continuous-integration
    title: Continuous integration (GitHub Docs)
  - id: gh-cd
    resource: https://docs.github.com/en/actions/get-started/continuous-deployment
    title: Continuous deployment (GitHub Docs)
---

<p align="center">
  <a href="README.md">📂 <b>Chapter 2 Cheat Sheet and Quiz</b></a> &nbsp;·&nbsp; Lesson 6 · Part 5 of 6 &nbsp;·&nbsp; ⏱️ 3 min
</p>

# 🧠 Quiz

<details>
<summary><b>1. What two things must both be true for a team to be "doing CI"?</b></summary>

<br>

They integrate small changes into the shared branch frequently, **and** every change is automatically built and tested.

</details>

<details>
<summary><b>2. What is the single difference between continuous delivery and continuous deployment?</b></summary>

<br>

Whether the final release to production needs a human approval (delivery) or happens automatically (deployment).

</details>

<details>
<summary><b>3. In the CI Basics workflow, <code>lint</code> fails. Which jobs run afterwards?</b></summary>

<br>

None. `test` needs `lint`, and `package` needs `test`, so both are skipped.

</details>

<details>
<summary><b>4. What does "build once, deploy many" protect you from?</b></summary>

<br>

Shipping an artifact to production that differs from the one you tested in staging.

</details>

<details>
<summary><b>5. You push three commits in ten seconds. With <code>cancel-in-progress: true</code>, how many runs finish?</b></summary>

<br>

One, for the latest commit. The two older runs in the same concurrency group are cancelled.

</details>

<details>
<summary><b>6. Artifact or cache: the compiled app you intend to deploy?</b></summary>

<br>

Artifact. It's an output you need, not a speed-up you could live without.

</details>

<details>
<summary><b>7. Why did the workflow use <code>path: sample-app/dist/</code> when <code>working-directory</code> was already <code>sample-app</code>?</b></summary>

<br>

`working-directory` only affects `run:` steps. Action inputs are resolved from the repository root.

</details>

<details>
<summary><b>8. Your pipeline takes 40 minutes. Name two ways to speed it up using what you've learned.</b></summary>

<br>

Any two of: run independent jobs in parallel instead of serially; cache dependencies; use `paths` filters to skip irrelevant runs; put fast checks first so failures surface early; cancel stale runs with `concurrency`.

</details>

## 📊 How did you do?

| Score | Verdict |
|---|---|
| 8 | 🏆 You think in pipelines now |
| 5 to 7 | 💪 Strong. Revisit the lessons you missed |
| 0 to 4 | 🔁 Redo the [hands-on lesson](../05-your-first-ci-pipeline/README.md); doing beats reading |

---

<p align="center">
  <a href="04-golden-rules.md">⬅️ Golden rules</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="06-chapter-complete.md"><b>Next: Chapter complete ➡️</b></a>
</p>
