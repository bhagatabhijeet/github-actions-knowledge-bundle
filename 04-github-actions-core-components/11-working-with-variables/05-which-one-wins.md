---
type: Tutorial
title: "Working with Variables: Which one wins?"
description: "When the same name is set at several levels, the most specific one wins: step, then job, then workflow."
tags: [github-actions, variables, env, vars, configuration-variables, github-env, hands-on]
status: stable
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-26T00:00:00Z }
sources:
  - id: gh-variables
    resource: https://docs.github.com/en/actions/concepts/workflows-and-actions/variables
    title: Variables
  - id: gh-variables-ref
    resource: https://docs.github.com/en/actions/reference/workflows-and-actions/variables
    title: Variables reference
  - id: gh-contexts
    resource: https://docs.github.com/en/actions/reference/workflows-and-actions/contexts
    title: Contexts reference
  - id: gh-workflow-commands
    resource: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-commands
    title: Workflow commands for GitHub Actions
---

<p align="center">
  <a href="README.md">📂 <b>Working with Variables</b></a> &nbsp;·&nbsp; Lesson 11 · Part 5 of 14 &nbsp;·&nbsp; ⏱️ 2 min
</p>

# 🥇 Which one wins?

<p align="center">
  <img src="../../assets/images/variable-scopes.svg" alt="Nested workflow, job and step scopes each setting IMAGE_TAG; inside the step the value is rc-1 because the closest scope wins. Configuration variables live in Settings at organisation, repository and environment level, and environment wins. At the bottom, $IMAGE_TAG is read by the shell on the runner, while ${{ env.IMAGE_TAG }} is replaced by GitHub before the step runs" width="100%">
</p>

When the same name is set at several levels, **the most specific one wins**: step, then job, then workflow.

| Level | Seen by | Overridden by |
|---|---|---|
| 📜 Workflow `env:` | Every job and step | Job or step `env:` |
| 📦 Job `env:` | Every step in that job | Step `env:` |
| 👣 Step `env:` | That step only | Nothing |

> [!NOTE]
> An override only lasts for its own scope. A job that overrides `IMAGE_TAG` doesn't change it for the other jobs, which still see the workflow value.

## 🧩 Puzzle

```yaml
env:
  GREETING: Hello

jobs:
  one:
    runs-on: ubuntu-latest
    env:
      GREETING: Hi
    steps:
      - run: echo "$GREETING"            # A
      - env:
          GREETING: Hey
        run: echo "$GREETING"            # B
  two:
    runs-on: ubuntu-latest
    steps:
      - run: echo "$GREETING"            # C
```

<details>
<summary><b>What do A, B and C print?</b></summary>

<br>

**A** prints `Hi` (job beats workflow). **B** prints `Hey` (step beats job). **C** prints `Hello`: job `two` has no override, so it gets the workflow value.

</details>

---

<p align="center">
  <a href="04-fix-3-workflow-level-env.md">⬅️ Fix 3: workflow-level `env`</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="06-var-or-env-var.md"><b>Next: `$VAR` or `${{ env.VAR }}`? ➡️</b></a>
</p>
