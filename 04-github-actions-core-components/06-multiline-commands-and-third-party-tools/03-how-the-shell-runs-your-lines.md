---
type: Tutorial
title: "Multi-line Commands and Third-Party Tools: How the shell runs your lines"
description: "All lines of one run: share one shell: state carries between lines but not between steps, and the exact shell flags decide when a step fails."
tags: [github-actions, run, multi-line, yaml, shell, apt-get, third-party, hands-on]
status: stable
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-26T00:00:00Z }
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
  <a href="README.md">📂 <b>Multi-line Commands and Third-Party Tools</b></a> &nbsp;·&nbsp; Lesson 6 · Part 3 of 6 &nbsp;·&nbsp; ⏱️ 3 min
</p>

# 🐚 How the shell runs your lines

All lines of one `run:` go into **one script** run by **one shell**. That has three consequences:

| | Rule | Example |
|---|---|---|
| 🔗 | **State carries between lines** of the same step | `cd src` on line 1 still applies on line 2 |
| 🧱 | **State does not carry between steps** | A `cd` or `export` in step 1 is gone in step 2 |
| 🛑 | **The first failing line stops the step** (on Linux and macOS) | GitHub runs bash with `-e`, so the step ends at the first non-zero exit code |

> [!IMPORTANT]
> The default shell on Linux and macOS is `bash -e {0}` when you don't set `shell:`. With `shell: bash` set explicitly, GitHub adds `-o pipefail` too, so a failure in the middle of a pipe (`a | b`) also fails the step. On Windows the default is PowerShell.

To pass values between steps, write them to `$GITHUB_ENV` (environment variables) or `$GITHUB_OUTPUT` (step outputs):

```yaml
- id: version
  run: echo "tag=v$(date +%Y.%m.%d)" >> "$GITHUB_OUTPUT"
- run: echo "Releasing ${{ steps.version.outputs.tag }}"
```

Two more step keys help with multi-line scripts:

```yaml
- name: Run the tests
  working-directory: sample-app     # where the script starts
  shell: bash                       # adds pipefail; also: pwsh, python, sh, cmd
  run: |
    python -m pip install -r requirements.txt
    python -m pytest -q
```

To set these once for every `run:` step in a job (or the whole workflow), use `defaults.run`:

```yaml
jobs:
  test:
    runs-on: ubuntu-latest
    defaults:
      run:
        shell: bash
        working-directory: sample-app
    steps:
      - uses: actions/checkout@v7
      - run: python -m pytest -q
```

> [!NOTE]
> **📘 From the GitHub docs:** If you don't set `shell:` on Linux or macOS, GitHub runs `bash -e {0}`. If bash isn't on the PATH, it falls back to `sh`. Set `shell: bash` and you get `bash --noprofile --norc -eo pipefail {0}` instead, which also skips `~/.bash_profile` and `~/.bashrc`. ([Workflow syntax for GitHub Actions](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#defaultsrunshell))

> [!TIP]
> **📘 From the GitHub docs:** the `working-directory` must already exist on the runner when the step starts. A folder that only appears after checkout won't work in a step before `actions/checkout`. ([Workflow syntax for GitHub Actions](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#defaultsrunworking-directory))

---

<p align="center">
  <a href="02-two-ways-to-write-a-multi-line.md">⬅️ Two ways to write a multi-line `run:`</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="04-executing-third-party-tools.md"><b>Next: Executing third-party tools ➡️</b></a>
</p>
