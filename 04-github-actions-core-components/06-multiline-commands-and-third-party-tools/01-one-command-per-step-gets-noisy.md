---
type: Tutorial
title: "Multi-line Commands and Third-Party Tools: One command per step gets noisy"
description: "That works, but it's four steps, four log sections and four shell start-ups for what is really one idea. YAML lets you put several lines in one run:."
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
  <a href="README.md">📂 <b>Multi-line Commands and Third-Party Tools</b></a> &nbsp;·&nbsp; Lesson 6 · Part 1 of 6 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# 🤔 One command per step gets noisy

```yaml
steps:
  - run: sudo apt-get update
  - run: sudo apt-get install -y cowsay
  - run: cowsay "Hello" > hello.txt
  - run: cat hello.txt
```

That works, but it's four steps, four log sections and four shell start-ups for what is really one idea. YAML lets you put several lines in one `run:`.

---

<p align="center">
  <a href="README.md">⬅️ Overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="02-two-ways-to-write-a-multi-line.md"><b>Next: Two ways to write a multi-line `run:` ➡️</b></a>
</p>
