---
type: Tutorial
title: "Configuring the Checkout Action: Checkpoint"
description: "The workspace folder exists, it's just empty. Listing an empty folder is not an error. Only reading a file that isn't there fails."
tags: [github-actions, actions, checkout, hands-on, fetch-depth, sparse-checkout]
status: stable
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-25T00:00:00Z }
sources:
  - id: checkout-repo
    resource: https://github.com/actions/checkout
    title: actions/checkout README
  - id: gh-workflow-syntax
    resource: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
    title: Workflow syntax for GitHub Actions
---

<p align="center">
  <a href="README.md">📂 <b>Configuring the Checkout Action</b></a> &nbsp;·&nbsp; Lesson 5 · Part 7 of 7 &nbsp;·&nbsp; ⏱️ 2 min
</p>

# ✅ Checkpoint

<details>
<summary><b>The workflow ran <code>ls</code> and printed nothing, without an error. Why no error?</b></summary>

<br>

The workspace folder exists, it's just empty. Listing an empty folder is not an error. Only reading a file that isn't there fails.

</details>

<details>
<summary><b>How many commits does checkout fetch by default, and how do you get all of them?</b></summary>

<br>

One, the commit that triggered the run. Set `fetch-depth: 0` to get the full history.

</details>

<details>
<summary><b>You need code from a private repository in your organisation as well as this one. Which three inputs do you set on the second checkout?</b></summary>

<br>

`repository` (which repo), `path` (so it doesn't overwrite the first checkout) and `token` (a credential that can read the private repo).

</details>

---

<p align="center">
  <a href="06-something-went-wrong.md">⬅️ Something went wrong?</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md#-what-you-learned"><b>Wrap up: What you learned ➡️</b></a>
</p>
