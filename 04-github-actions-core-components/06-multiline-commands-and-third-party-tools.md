---
type: Tutorial
title: Multi-line Commands and Third-Party Tools (Hands-On)
description: Run several commands in one step with YAML's literal and folded blocks, understand how the shell treats them, then install and use a third-party tool on the runner - with apt, pip, npm or a setup action.
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
  <b>Lesson 6 of 9</b> &nbsp;·&nbsp; ⏱️ 18 min &nbsp;·&nbsp; 🛠️ Hands-on
</p>

# 📜 Multi-line Commands and Third-Party Tools

So far each `run:` step has held one command. Real steps often need several, and they often need tools that aren't part of your code. This lesson covers both.

## 🤔 One command per step gets noisy

```yaml
steps:
  - run: sudo apt-get update
  - run: sudo apt-get install -y cowsay
  - run: cowsay "Hello" > hello.txt
  - run: cat hello.txt
```

That works, but it's four steps, four log sections and four shell start-ups for what is really one idea. YAML lets you put several lines in one `run:`.

## ✍️ Two ways to write a multi-line `run:`

<p align="center">
  <img src="../assets/images/multiline-run-blocks.svg" alt="Literal block with a pipe keeps each line as a separate command; folded block with a greater-than sign joins lines into one command. Below, installing a third-party tool, using it and checking the result" width="100%">
</p>

| | Symbol | YAML name | What the shell receives | Use it for |
|---|---|---|---|---|
| 🟢 | **`\|`** | Literal block | Each line as its own command, in order | ✅ Almost always: a small script |
| 🟠 | **`>`** | Folded block | All lines joined by spaces into one command | One very long command you want to read easily |

```yaml
- name: Install and use a tool      # | : two commands
  run: |
    sudo apt-get install -y cowsay
    cowsay "Hello" > hello.txt

- name: Build an image                # > : one command, wrapped for reading
  run: >
    docker build
    --tag my-app:1.0
    --label team=payments
    .
```

> [!TIP]
> Prefer `|` with a backslash `\` at the end of a line when you need to wrap one command inside a script. It's what most people expect, and it keeps working when you add more lines.

## 🐚 How the shell runs your lines

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

## 📦 Executing third-party tools

A third-party tool is any program you didn't write and your repository doesn't contain: a linter, a CLI, a converter, a game like `cowsay`. To use one, you **install it on the runner, then run it**.

### First, check if it's already there

GitHub-hosted runners come with a lot preinstalled: git, Docker, Node.js, Python, Java, Go, the AWS, Azure and Google Cloud CLIs, `jq`, `curl` and many more. The full list for each image is in [actions/runner-images](https://github.com/actions/runner-images). If your tool is on it, skip the install.

### If not, pick the right installer

| Tool comes from | Install with | Example |
|---|---|---|
| 🐧 Ubuntu packages | `apt-get` (with `sudo`, no password needed) | `sudo apt-get install -y cowsay` |
| 🐍 Python packages | `pip` | `pip install yamllint` |
| 🟩 npm packages | `npm` / `npx` | `npx markdownlint-cli2 "**/*.md"` |
| 🍺 macOS packages | `brew` | `brew install tree` |
| 📥 A release binary | `curl` then run | `curl -sSfL https://.../install.sh \| sh` |
| 🧩 A setup action | `uses:` | `uses: hashicorp/setup-terraform@v3` |

> [!NOTE]
> **Installs don't stick.** The runner is thrown away after the job, so every run installs again. For slow installs, use `actions/cache` or a setup action with built-in caching (for example `actions/setup-python` with `cache: pip`).

### Worked example: a dragon that talks 🐉

```yaml
jobs:
  ascii-art:
    runs-on: ubuntu-latest
    steps:
      - name: Install cowsay
        run: |
          sudo apt-get update -qq
          sudo apt-get install -y -qq cowsay

      - name: Generate ASCII art
        run: |
          cowsay -f dragon "Run for cover, I am a DRAGON....RAWR" > dragon.txt
          echo "Lines written: $(wc -l < dragon.txt)"

      - name: Check the file
        run: grep -i "dragon" dragon.txt

      - name: Show the file
        run: cat dragon.txt
```

| Step | Does | Fails when |
|---|---|---|
| 📦 Install | Fetches the package list, installs `cowsay` | The package name is wrong |
| ⚙️ Generate | Runs the tool, saves its output to a file | `cowsay` isn't installed |
| 🔍 Check | `grep` looks for the word | The word isn't there: `grep` exits with 1 and the step fails |
| 📄 Show | Prints the dragon in the log | The file is missing |

### 🔎 Reading the install log

Open the run, click the job, then expand **Install Cowsay Program**. A successful install looks like this:

```text
▶ Run sudo apt-get install cowsay -y
  Reading package lists...
  Building dependency tree...
  Reading state information...
  Suggested packages:
    filters cowsay-off
  The following NEW packages will be installed:
    cowsay
  0 upgraded, 1 newly installed, 0 to remove and 30 not upgraded.
  Need to get 18.6 kB of archives.
  Get:2 http://azure.archive.ubuntu.com/ubuntu jammy/universe amd64 cowsay all 3.03+dfsg2-8 [18.6 kB]
  Fetched 18.6 kB in 0s (269 kB/s)
  Selecting previously unselected package cowsay.
  ...
```

| Log line | What it tells you |
|---|---|
| `▶ Run sudo apt-get install cowsay -y` | The exact command GitHub ran. Click ▶ to see the shell and environment it used |
| `Reading package lists...` | `apt` is loading its catalogue of available packages |
| `Suggested packages: filters cowsay-off` | Optional extras. **Not** installed, and safe to ignore |
| `The following NEW packages will be installed: cowsay` | Confirms it found the package you asked for |
| `1 newly installed ... 30 not upgraded` | Only `cowsay` was added. Other packages were left alone |
| `azure.archive.ubuntu.com ... jammy/universe` | Downloaded from Ubuntu's mirror inside Azure, where hosted runners live. `jammy` is Ubuntu 22.04 |
| `Fetched 18.6 kB in 0s` | Small tools install in seconds. Big ones are worth caching |

> [!TIP]
> **`-y` matters.** Without it, `apt-get` stops to ask "Do you want to continue? [Y/n]". Nobody can answer on a runner, so the step fails. Every install command in a workflow must be non-interactive.

> [!NOTE]
> This run skipped `apt-get update` and still worked, because the runner image ships with a fairly fresh package list. When an install fails with `Unable to locate package` or a 404, add `sudo apt-get update` first.

> [!WARNING]
> **`curl ... | sh` runs whatever that URL serves today.** Pin a version in the URL, check a checksum when the project publishes one, and prefer a package manager or a pinned setup action when there is one.

## 🛠️ Try it yourself

This repository ships the dragon as a live workflow: [`04-multiline-commands.yml`](../.github/workflows/04-multiline-commands.yml).

1. Open the **Actions** tab and pick **04 - Multi-line Commands**
2. Click **Run workflow**
3. Open **Show the file** to see the dragon, and **A folded command** to see three YAML lines printed as one
4. **Break it:** in a fork, change `grep -i "dragon"` to `grep -i "unicorn"`. The **Check the file** step fails, and **Show the file** is skipped
5. **Stretch:** swap `-f dragon` for another cow from `cowsay -l`

## ✅ Checkpoint

<details>
<summary><b>A step runs <code>cd sample-app</code> and the next step runs <code>ls</code>. Which folder does <code>ls</code> list?</b></summary>

<br>

The workspace root. Each step starts a new shell, so the `cd` from the previous step is gone. Use `working-directory:`, or put both commands in one multi-line step.

</details>

<details>
<summary><b>Line 2 of a 4-line <code>run: |</code> block fails on Ubuntu. Do lines 3 and 4 run?</b></summary>

<br>

No. Bash runs with `-e`, so the script stops at the first failing command and the step is marked as failed.

</details>

<details>
<summary><b>You wrote a three-line <code>run: &gt;</code> block, but the commands ran as one garbled line. Why?</b></summary>

<br>

`>` folds lines into one, joined by spaces. Use `|` to keep each line a separate command.

</details>

<details>
<summary><b>You installed a tool with <code>apt-get</code> yesterday. Is it still there in today's run?</b></summary>

<br>

No. Each job gets a fresh runner, so the install must be in the workflow every time. Cache it if it's slow.

</details>

## 🎯 What you learned

- **`run: |`** keeps each line as a separate command; **`run: >`** folds lines into one
- All lines of a step run in **one shell**: state carries **within** a step, not **between** steps
- Bash stops at the **first failing line**; `shell: bash` adds **pipefail**
- Check the **runner image** before installing anything; much is preinstalled
- Install third-party tools with **apt, pip, npm, brew** or a **setup action**, every run
- **Pin and verify** anything you download with `curl`

---

<p align="center">
  <a href="05-configuring-the-checkout-action.md">⬅️ Configuring Checkout</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="index.md">📚 Chapter 4</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="07-executing-shell-scripts.md"><b>Next: Executing Shell Scripts ➡️</b></a>
</p>
