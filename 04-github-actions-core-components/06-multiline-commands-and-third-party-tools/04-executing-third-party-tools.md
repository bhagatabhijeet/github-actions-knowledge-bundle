---
type: Tutorial
title: "Multi-line Commands and Third-Party Tools: Executing third-party tools"
description: "A third-party tool is any program you didn't write and your repository doesn't contain: a linter, a CLI, a converter, a game like cowsay. To use one, you install it on the runner, then run it."
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
  <a href="README.md">📂 <b>Multi-line Commands and Third-Party Tools</b></a> &nbsp;·&nbsp; Lesson 6 · Part 4 of 6 &nbsp;·&nbsp; ⏱️ 6 min
</p>

# 📦 Executing third-party tools

A third-party tool is any program you didn't write and your repository doesn't contain: a linter, a CLI, a converter, a game like `cowsay`. To use one, you **install it on the runner, then run it**.

## First, check if it's already there

GitHub-hosted runners come with a lot preinstalled: git, Docker, Node.js, Python, Java, Go, the AWS, Azure and Google Cloud CLIs, `jq`, `curl` and many more. The full list for each image is in [actions/runner-images](https://github.com/actions/runner-images). If your tool is on it, skip the install.

## If not, pick the right installer

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

## Worked example: a dragon that talks 🐉

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

## 🔎 Reading the install log

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

---

<p align="center">
  <a href="03-how-the-shell-runs-your-lines.md">⬅️ How the shell runs your lines</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="05-try-it-yourself.md"><b>Next: Try it yourself ➡️</b></a>
</p>
