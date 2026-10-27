---
type: Tutorial
title: "Your First CI Pipeline: Exercise 3: Plant a bug, watch CI catch it"
description: "This is the moment CI earns its keep."
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
  <a href="README.md">📂 <b>Your First CI Pipeline</b></a> &nbsp;·&nbsp; Lesson 5 · Part 6 of 9 &nbsp;·&nbsp; ⏱️ 2 min
</p>

# 🐛 Exercise 3: Plant a bug, watch CI catch it

This is the moment CI earns its keep.

**1. Create a branch**

```bash
git switch -c break-the-greeting
```

**2. Break the app.** In `sample-app/greeter/core.py`, change the greeting:

```diff
-    return f"Hello, {cleaned or 'World'}!"
+    return f"Howdy, {cleaned or 'World'}!"
```

**3. Push and open a pull request** (against `main` *of your own fork*)

```bash
git commit -am "Make the greeting friendlier"
git push -u origin break-the-greeting
```

**4. Watch the pull request page.** Within a minute:

```text
❌ 02 - CI Basics / test (3.12)   Failing
❌ 02 - CI Basics / test (3.13)   Failing
❌ 02 - CI Basics / test (3.14)   Failing
⏭️ 02 - CI Basics / package       Skipped
```

Open a failing job and the log tells you precisely what's wrong:

```text
FAIL: test_greets_by_name (tests.test_core.GreetTests.test_greets_by_name)
AssertionError: 'Howdy, Octocat!' != 'Hello, Octocat!'
```

Look at what just happened:

- ✅ `lint` passed (the code is *valid*, just *wrong*)
- ❌ `test` caught the behaviour change, on all three versions
- ⏭️ `package` never ran, so **no broken artifact exists**

Nobody had to remember to run the tests. Nobody reviewed broken code. The bug never reached `main`.

**5. Fix it.** Change `Howdy` back to `Hello`, commit and push. The same pull request turns green.

> [!TIP]
> Notice you didn't open a new pull request. Each push to the branch re-runs CI, and `concurrency` cancels any run that's now out of date.

---

<p align="center">
  <a href="05-exercise-2-collect-your-artifact.md">⬅️ Exercise 2: Collect your artifact</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="07-exercise-4-fail-the-lint-gate.md"><b>Next: Exercise 4: Fail the lint gate ➡️</b></a>
</p>
