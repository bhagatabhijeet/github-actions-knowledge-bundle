# Multi-line Commands and Third-Party Tools

* [Overview](README.md) - Run several commands in one step with YAML's literal and folded blocks, understand how the shell treats them, then install and use a third-party tool on the runner - with apt, pip, npm or a setup action.
* [One command per step gets noisy](01-one-command-per-step-gets-noisy.md) - That works, but it's four steps, four log sections and four shell start-ups for what is really one idea. YAML lets you put several lines in one run:.
* [Two ways to write a multi-line `run:`](02-two-ways-to-write-a-multi-line.md) - Prefer | with a backslash \ at the end of a line when you need to wrap one command inside a script. It's what most people expect, and it keeps working when you add more lines.
* [How the shell runs your lines](03-how-the-shell-runs-your-lines.md) - All lines of one run: go into one script run by one shell. That has three consequences:
* [Executing third-party tools](04-executing-third-party-tools.md) - A third-party tool is any program you didn't write and your repository doesn't contain: a linter, a CLI, a converter, a game like cowsay. To use one, you install it on the runner, then run it.
* [Try it yourself](05-try-it-yourself.md) - This repository ships the dragon as a live workflow: 04-multiline-commands.yml.
* [Checkpoint](06-checkpoint.md) - The workspace root. Each step starts a new shell, so the cd from the previous step is gone. Use working-directory:, or put both commands in one multi-line step.
