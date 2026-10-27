---
type: Tutorial
title: "Executing Shell Scripts in a Workflow: Where we left off"
description: "Six steps, each a single command. It works, and the log is easy to follow. But the logic lives only in YAML."
tags: [github-actions, shell, bash, scripts, chmod, line-endings, hands-on]
status: stable
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-25T00:00:00Z }
sources:
  - id: gh-workflow-syntax
    resource: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
    title: Workflow syntax for GitHub Actions
  - id: gh-workflow-commands
    resource: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-commands
    title: Workflow commands for GitHub Actions
  - id: git-attributes
    resource: https://git-scm.com/docs/gitattributes
    title: gitattributes
---

<p align="center">
  <a href="README.md">📂 <b>Executing Shell Scripts in a Workflow</b></a> &nbsp;·&nbsp; Lesson 7 · Part 1 of 9 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# 🧩 Where we left off

```yaml
name: Generate ASCII Artwork

on: push

jobs:
  ascii_job:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Repo
        uses: actions/checkout@v4

      - name: Install Cowsay Program
        run: sudo apt-get install cowsay -y

      - name: Execute Cowsay CMD
        run: cowsay -f dragon "Run for cover, I am a DRAGON....RAWR" >> dragon.txt

      - name: Test File Exists
        run: grep -i "dragon" dragon.txt

      - name: Read File
        run: cat dragon.txt

      - name: List Repo Files
        run: ls -ltra
```

Six steps, each a single command. It works, and the log is easy to follow. But the logic lives *only* in YAML.

---

<p align="center">
  <a href="README.md">⬅️ Overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="02-move-the-commands-into-a-script.md"><b>Next: Move the commands into a script ➡️</b></a>
</p>
