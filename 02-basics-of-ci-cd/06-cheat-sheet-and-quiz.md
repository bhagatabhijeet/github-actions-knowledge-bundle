---
type: Reference
title: Chapter 2 Cheat Sheet and Quiz
description: CI/CD on one page - definitions, pipeline stages, the Actions features that implement them - followed by an eight-question self-check.
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
  <b>Lesson 6 of 6</b> &nbsp;·&nbsp; ⏱️ 5 min &nbsp;·&nbsp; 🏁 Chapter finale
</p>

# 📋 Chapter 2 Cheat Sheet & Quiz

## 🔤 The three practices

| | Practice | One-liner | Final step to production |
|---|---|---|---|
| 🧪 | **Continuous Integration** | Merge small, verify automatically | n/a |
| 🚚 | **Continuous Delivery** | Always releasable | Human approves |
| 🚀 | **Continuous Deployment** | Always released | Automatic |

## 🚉 Pipeline stages

| Stage | Question | Typical commands |
|---|---|---|
| 📥 Source | What changed? | `actions/checkout` |
| 🏗️ Build | Does it assemble? | `pip install`, `npm ci`, `mvn compile` |
| 🧪 Test | Does it behave? | `ruff check`, `unittest`, `npm test` |
| 📦 Package | What do we ship? | `tar`, `docker build`, `upload-artifact` |
| 🚀 Deploy | Is it live? | Your cloud's CLI or action |

## 🧩 Idea → GitHub Actions

| CI/CD idea | Feature | Snippet |
|---|---|---|
| Run on every change | Events | `on: [push, pull_request]` |
| Stage order | Job dependencies | `needs: test` |
| Multiple versions | Matrix | `strategy.matrix` |
| Pass files between stages | Artifacts | `upload-artifact` / `download-artifact` |
| Speed up installs | Cache | `cache: pip` |
| Skip irrelevant runs | Path filters | `paths: ['src/**']` |
| Cancel stale runs | Concurrency | `cancel-in-progress: true` |
| Approval before prod | Environments | `environment: production` |
| Block bad merges | Rulesets | Required status checks |

## 🏆 Golden rules

> [!IMPORTANT]
> 1. **Small changes, merged often.** The practice matters more than the tool.
> 2. **Fail fast.** Cheapest checks first.
> 3. **Red `main` stops the line.** Fix or revert.
> 4. **Build once, deploy many.** Ship the artifact you tested.
> 5. **Keep it under ten minutes.** Slow feedback gets ignored.
> 6. **Config is not code.** Environment differences are supplied at deploy time.

## 🧠 Quiz

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

### 📊 How did you do?

| Score | Verdict |
|---|---|
| 8 | 🏆 You think in pipelines now |
| 5 to 7 | 💪 Strong. Revisit the lessons you missed |
| 0 to 4 | 🔁 Redo the [hands-on lesson](05-your-first-ci-pipeline.md); doing beats reading |

## 🎉 Chapter complete

You understand why CI/CD exists, can tell delivery from deployment, and have built a staged pipeline with a matrix and an artifact.

> [!NOTE]
> **More chapters are on the way.** This guide grows one topic at a time. Check the [change log](../log.md) to see what's new.

---

<p align="center">
  <a href="05-your-first-ci-pipeline.md">⬅️ Your First CI Pipeline</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="index.md">📚 Chapter 2</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="../README.md"><b>🏠 Back to Home</b></a>
</p>
