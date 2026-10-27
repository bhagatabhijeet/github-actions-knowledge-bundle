---
type: Tutorial
title: "Configuring the Checkout Action: The fix: one line"
description: "Now ls shows your files and cat prints the README."
tags: [github-actions, actions, checkout, hands-on, fetch-depth, sparse-checkout]
status: stable
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-25T00:00:00Z }
sources:
  - id: checkout-repo
    resource: https://github.com/actions/checkout
    title: actions/checkout README
  - id: gh-workflow-syntax
    resource: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
    title: Workflow syntax for GitHub Actions
---

<p align="center">
  <a href="README.md">📂 <b>Configuring the Checkout Action</b></a> &nbsp;·&nbsp; Lesson 5 · Part 3 of 7 &nbsp;·&nbsp; ⏱️ 2 min
</p>

# ✅ The fix: one line

```yaml
    steps:
      - name: Checkout repository
        uses: actions/checkout@v7       # 👈 add this first

      - name: Welcome message
        run: echo "My first GitHub Actions job"

      - name: List files
        run: ls

      - name: Read file
        run: cat README.md
```

Now `ls` shows your files and `cat` prints the README.

What checkout does by default:

| | Default behaviour |
|---|---|
| 📍 **Where** | Into `$GITHUB_WORKSPACE`, the job's working folder |
| 🎯 **Which commit** | The one that triggered the run (`github.sha`) |
| 📏 **How much history** | Just that **one commit** (`fetch-depth: 1`), which is fast |
| 🔑 **Credentials** | Uses the job's `GITHUB_TOKEN`, and leaves it in git config so later `git` commands work |

> [!TIP]
> **Use the GitHub Actions extension in VS Code** (or the web editor at `github.dev`). It autocompletes action names and their `with:` inputs, and underlines typos before you push.

---

<p align="center">
  <a href="02-why-it-fails.md">⬅️ Why it fails</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="04-configuring-it-with-with.md"><b>Next: Configuring it with `with:` ➡️</b></a>
</p>
