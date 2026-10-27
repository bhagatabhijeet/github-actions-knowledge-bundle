---
type: Tutorial
title: "Continuous Integration: Checkpoint"
description: "No. They have automated testing, but they aren't integrating continuously. After three weeks, merging is still a painful event."
tags: [ci-cd, continuous-integration, testing, linting, pull-requests]
status: stable
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-07T00:00:00Z }
sources:
  - id: fowler-ci
    resource: https://martinfowler.com/articles/continuousIntegration.html
    title: Continuous Integration
    author: Martin Fowler
  - id: gh-ci
    resource: https://docs.github.com/en/actions/get-started/continuous-integration
    title: Continuous integration (GitHub Docs)
  - id: gh-protection
    resource: https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches
    title: About protected branches
---

<p align="center">
  <a href="README.md">📂 <b>Continuous Integration</b></a> &nbsp;·&nbsp; Lesson 2 · Part 8 of 8 &nbsp;·&nbsp; ⏱️ 2 min
</p>

# ✅ Checkpoint

<details>
<summary><b>A team runs a full test suite on every push, but feature branches live for three weeks. Are they doing CI?</b></summary>

<br>

No. They have automated testing, but they aren't *integrating* continuously. After three weeks, merging is still a painful event.

</details>

<details>
<summary><b>Both pull requests passed CI. Why run it again on <code>main</code> after merging?</b></summary>

<br>

Each pull request was tested separately. After both are merged, `main` holds a combination of changes that has never been tested together. The run on `main` is the first to check it.

</details>

<details>
<summary><b>Why run lint before the tests?</b></summary>

<br>

Fail fast. Lint takes seconds; if it's going to fail, you want to know before spending minutes on tests.

</details>

<details>
<summary><b>What should happen when <code>main</code> goes red?</b></summary>

<br>

It becomes the team's top priority. Fix it, or revert the change that broke it, before merging anything else.

</details>

---

<p align="center">
  <a href="07-how-it-maps-to-github-actions.md">⬅️ How it maps to GitHub Actions</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="../03-delivery-vs-deployment/README.md"><b>Next topic ➡️</b></a>
</p>
