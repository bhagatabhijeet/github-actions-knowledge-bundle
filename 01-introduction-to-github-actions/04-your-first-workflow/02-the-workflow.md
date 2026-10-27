---
type: Tutorial
title: "Your First Workflow: The workflow"
description: "The full Hello, Actions workflow file you will run in this lesson."
resource: /.github/workflows/01-hello-world.yml
tags: [github-actions, hands-on, hello-world, workflow-dispatch, logs]
status: stable
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-07T00:00:00Z }
sources:
  - id: gh-quickstart
    resource: https://docs.github.com/en/actions/get-started/quickstart
    title: Quickstart for GitHub Actions
  - id: gh-summary
    resource: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-commands
    title: Workflow commands (job summaries)
---

<p align="center">
  <a href="README.md">📂 <b>Your First Workflow</b></a> &nbsp;·&nbsp; Lesson 4 · Part 2 of 8 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# 📄 The workflow

```yaml
name: 01 - Hello, Actions

on:
  push:
    branches: [main]
  workflow_dispatch:
    inputs:
      who:
        description: Who should we greet?
        required: false
        default: World

permissions:
  contents: read

jobs:
  say-hello:
    runs-on: ubuntu-latest
    steps:
      - name: Greet
        env:
          WHO: ${{ inputs.who || 'World' }}
        run: echo "Hello, $WHO! This runner is all yours."

      - name: Check out the repository
        uses: actions/checkout@v7

      - name: Look around
        run: |
          echo "Triggered by : $GITHUB_EVENT_NAME"
          echo "Repository   : $GITHUB_REPOSITORY"
          echo "Branch       : $GITHUB_REF_NAME"
          echo "Commit       : $GITHUB_SHA"
          echo "Runner OS    : $RUNNER_OS"
          echo "--- files in the workspace ---"
          ls -1

      - name: Write a job summary
        env:
          WHO: ${{ inputs.who || 'World' }}
        run: |
          {
            echo "## Hello, $WHO!"
            echo ""
            echo "| | |"
            echo "|---|---|"
            echo "| Event | \`$GITHUB_EVENT_NAME\` |"
            echo "| Branch | \`$GITHUB_REF_NAME\` |"
            echo "| Runner | \`$RUNNER_OS\` |"
          } >> "$GITHUB_STEP_SUMMARY"
```

---

<p align="center">
  <a href="01-before-you-start.md">⬅️ Before you start</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="03-what-each-part-teaches.md"><b>Next: What each part teaches ➡️</b></a>
</p>
