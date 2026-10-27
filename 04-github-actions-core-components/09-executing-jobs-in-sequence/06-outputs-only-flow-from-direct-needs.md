---
type: Tutorial
title: "Executing Jobs in Sequence with needs: Outputs only flow from direct `needs`"
description: "A job can read needs.<job>.outputs only for jobs it lists in its own needs:, not for jobs further up the chain."
tags: [github-actions, jobs, needs, sequence, if, status-functions, outputs, hands-on]
status: stable
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-26T00:00:00Z }
sources:
  - id: gh-workflow-syntax
    resource: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
    title: Workflow syntax for GitHub Actions
  - id: gh-expressions
    resource: https://docs.github.com/en/actions/reference/workflows-and-actions/expressions
    title: Evaluate expressions in workflows and actions
  - id: gh-contexts
    resource: https://docs.github.com/en/actions/reference/workflows-and-actions/contexts
    title: Contexts reference
---

<p align="center">
  <a href="README.md">📂 <b>Executing Jobs in Sequence with needs</b></a> &nbsp;·&nbsp; Lesson 9 · Part 6 of 9 &nbsp;·&nbsp; ⏱️ 1 min
</p>

# 📤 Outputs only flow from direct `needs`

A job can read `needs.<job>.outputs` **only for jobs it lists in its own `needs:`**. Being further down the chain isn't enough:

```yaml
  build:
    outputs:
      version: ${{ steps.v.outputs.version }}
    ...
  test:
    needs: build
    ...
  deploy:
    needs: test                                     # ❌ needs.build is empty here
    steps:
      - run: echo "${{ needs.build.outputs.version }}"
```

```yaml
  deploy:
    needs: [build, test]                            # ✅ list build too
    steps:
      - run: echo "${{ needs.build.outputs.version }}"
```

Listing `build` adds no waiting, since `test` already waited for it. It just opens the door to its outputs.

---

<p align="center">
  <a href="05-overriding-the-rule-with-if.md">⬅️ Overriding the rule with `if:`</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="07-common-mistakes.md"><b>Next: Common mistakes ➡️</b></a>
</p>
