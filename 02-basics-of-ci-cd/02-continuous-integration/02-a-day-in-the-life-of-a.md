---
type: Tutorial
title: "Continuous Integration: A day in the life of a change"
description: "Notice step 4. The failure reached the author within minutes, while the change was still fresh in their head, and before a reviewer spent any time on it. That fast feedback is the whole value of CI."
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
  <a href="README.md">📂 <b>Continuous Integration</b></a> &nbsp;·&nbsp; Lesson 2 · Part 2 of 8 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# 🎬 A day in the life of a change

```mermaid
sequenceDiagram
    autonumber
    actor Dev as 🧑‍💻 Developer
    participant GH as 🐙 GitHub
    participant CI as 🤖 CI workflow
    actor Rev as 👀 Reviewer

    Dev->>GH: Push branch, open pull request
    GH->>CI: pull_request event
    CI->>CI: Lint, build, test
    CI-->>GH: ❌ A test failed
    GH-->>Dev: Red cross on the PR
    Dev->>GH: Push a fix
    GH->>CI: pull_request event
    CI-->>GH: ✅ All checks passed
    Rev->>GH: Approve
    Dev->>GH: Merge to main
```

Notice step 4. The failure reached the author within minutes, while the change was still fresh in their head, and before a reviewer spent any time on it. That **fast feedback** is the whole value of CI.

---

<p align="center">
  <a href="01-the-definition.md">⬅️ The definition</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="03-two-developers-one-main.md"><b>Next: Two developers, one `main` ➡️</b></a>
</p>
