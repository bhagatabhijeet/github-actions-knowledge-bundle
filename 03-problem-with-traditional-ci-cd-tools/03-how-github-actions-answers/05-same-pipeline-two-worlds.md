---
type: Tutorial
title: "How GitHub Actions Answers the Problem: Same pipeline, two worlds"
description: "Tessaloop's Node.js project isn't in this repository, but a small Python sample app is. Here is a lint-and-test pipeline for it, written for Jenkins:"
tags: [github-actions, ci-cd, hosted-runners, self-hosted-runners, jenkins, comparison, migration]
status: stable
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-07T00:00:00Z }
sources:
  - id: gh-hosted-runners
    resource: https://docs.github.com/en/actions/concepts/runners/github-hosted-runners
    title: GitHub-hosted runners
  - id: gh-self-hosted-runners
    resource: https://docs.github.com/en/actions/concepts/runners/self-hosted-runners
    title: Self-hosted runners
  - id: gh-runner-images
    resource: https://github.com/actions/runner-images
    title: GitHub Actions runner images (preinstalled software lists)
  - id: gh-migrate-jenkins
    resource: https://docs.github.com/en/actions/tutorials/migrate-to-github-actions/manual-migrations/migrate-from-jenkins
    title: Migrating from Jenkins to GitHub Actions
  - id: gh-secure-use
    resource: https://docs.github.com/en/actions/reference/security/secure-use
    title: Secure use reference
  - id: gh-billing
    resource: https://docs.github.com/en/billing/concepts/product-billing/github-actions
    title: GitHub Actions billing
---

<p align="center">
  <a href="README.md">📂 <b>How GitHub Actions Answers the Problem</b></a> &nbsp;·&nbsp; Lesson 3 · Part 5 of 11 &nbsp;·&nbsp; ⏱️ 2 min
</p>

# 🔍 Same pipeline, two worlds

Tessaloop's Node.js project isn't in this repository, but a small Python [sample app](../../sample-app/) is. Here is a lint-and-test pipeline for it, written for Jenkins:

```groovy
pipeline {
    agent { label 'linux-python' }
    stages {
        stage('Lint') {
            steps {
                sh 'python -m pip install -r requirements-dev.txt'
                sh 'ruff check .'
            }
        }
        stage('Test') {
            steps {
                sh 'python -m unittest discover -v'
            }
        }
    }
}
```

And the same thing as a GitHub Actions workflow:

```yaml
name: CI
on: [push, pull_request]

jobs:
  lint-and-test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v7
      - uses: actions/setup-python@v7
        with:
          python-version: '3.13'
      - run: python -m pip install -r requirements-dev.txt
      - run: ruff check .
      - run: python -m unittest discover -v
```

The two files are about the same length, and that is the point. **The difference isn't in the file. It's in what has to exist before the file can run.**

| | Before the Jenkinsfile runs | Before the workflow runs |
|---|---|---|
| 🧠 | A CI server, installed and reachable | Nothing |
| 💪 | An agent labelled `linux-python`, with the right Python on it | Nothing: `runs-on` requests a machine, `setup-python` picks the version |
| 🧩 | Pipeline and Git plugins, at compatible versions | Nothing |
| 🔗 | A webhook and a clone credential | Nothing |
| 📄 | The file, committed | The file, committed |

Notice the line `agent { label 'linux-python' }`. It doesn't describe a machine. It **points at one that somebody built by hand**. The workflow's `python-version: '3.13'` describes what it needs, and gets it on a clean machine every time.

---

<p align="center">
  <a href="04-plugins-vs-actions.md">⬅️ Plugins vs actions</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="06-what-is-still-your-job.md"><b>Next: What is still your job ➡️</b></a>
</p>
