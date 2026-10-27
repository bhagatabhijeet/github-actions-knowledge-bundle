---
type: Tutorial
title: "Multi-line Commands and Third-Party Tools: Try it yourself"
description: "This repository ships the dragon as a live workflow: 04-multiline-commands.yml."
tags: [github-actions, run, multi-line, yaml, shell, apt-get, third-party, hands-on]
status: stable
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-25T00:00:00Z }
sources:
  - id: gh-workflow-syntax
    resource: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
    title: Workflow syntax for GitHub Actions
  - id: gh-runner-images
    resource: https://github.com/actions/runner-images
    title: GitHub Actions runner images
  - id: yaml-spec
    resource: https://yaml.org/spec/1.2.2/#81-block-scalar-styles
    title: YAML 1.2 block scalar styles
---

<p align="center">
  <a href="README.md">📂 <b>Multi-line Commands and Third-Party Tools</b></a> &nbsp;·&nbsp; Lesson 6 · Part 5 of 6 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# 🛠️ Try it yourself

This repository ships the dragon as a live workflow: [`04-multiline-commands.yml`](../../.github/workflows/04-multiline-commands.yml).

1. Open the **Actions** tab and pick **04 - Multi-line Commands**
2. Click **Run workflow**
3. Open **Show the file** to see the dragon, and **A folded command** to see three YAML lines printed as one
4. **Break it:** in a fork, change `grep -i "dragon"` to `grep -i "unicorn"`. The **Check the file** step fails, and **Show the file** is skipped
5. **Stretch:** swap `-f dragon` for another cow from `cowsay -l`

---

<p align="center">
  <a href="04-executing-third-party-tools.md">⬅️ Executing third-party tools</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="06-checkpoint.md"><b>Next: Checkpoint ➡️</b></a>
</p>
