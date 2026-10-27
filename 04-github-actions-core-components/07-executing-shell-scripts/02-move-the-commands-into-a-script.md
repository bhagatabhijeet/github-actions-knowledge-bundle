---
type: Tutorial
title: "Executing Shell Scripts in a Workflow: Move the commands into a script"
description: "1. Write the script at scripts/ascii-script.sh:"
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
  <a href="README.md">📂 <b>Executing Shell Scripts in a Workflow</b></a> &nbsp;·&nbsp; Lesson 7 · Part 2 of 9 &nbsp;·&nbsp; ⏱️ 2 min
</p>

# 🔄 Move the commands into a script

<p align="center">
  <img src="../../assets/images/workflow-to-shell-script.svg" alt="Six one-command steps become a workflow with two steps, checkout and run scripts/ascii-script.sh, while the commands move into the script file. Below, three requirements: check the script out first, give it the executable bit, keep LF line endings" width="100%">
</p>

**1. Write the script** at [`scripts/ascii-script.sh`](../../scripts/ascii-script.sh):

```bash
#!/usr/bin/env bash
set -euo pipefail

echo "::group::Install cowsay"
sudo apt-get install -y -qq cowsay
echo "::endgroup::"

cowsay -f dragon "Run for cover, I am a DRAGON....RAWR" > dragon.txt

grep -i "dragon" dragon.txt > /dev/null
echo "✅ dragon.txt contains a dragon"

cat dragon.txt
ls -ltra
```

**2. Make it executable, and commit that**

```bash
chmod +x scripts/ascii-script.sh
git add scripts/ascii-script.sh
git update-index --chmod=+x scripts/ascii-script.sh   # needed on Windows, harmless elsewhere
git commit -m "Add ASCII art script"
```

**3. Run it from the workflow**

```yaml
steps:
  - name: Checkout repo
    uses: actions/checkout@v7          # 👈 the script is in the repo, so check out first

  - name: Execute the script
    run: ./scripts/ascii-script.sh
```

Six steps became two, and you can now run `./scripts/ascii-script.sh` on any Linux machine to test it.

---

<p align="center">
  <a href="01-where-we-left-off.md">⬅️ Where we left off</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="03-watching-the-script-run.md"><b>Next: Watching the script run ➡️</b></a>
</p>
