# Working with Variables

* [Overview](README.md) - Stop hard-coding values - env at workflow, job and step level and which one wins, $VAR versus ${{ env.VAR }}, default GITHUB_ variables, setting values at runtime with $GITHUB_ENV, and configuration variables stored in Settings with the vars context.
* [Spot the problems](01-spot-the-problems.md) - Here is a workflow that builds a Docker image, pushes it, and runs it. It works. Before reading on, see how many problems you can find.
* [Fix 1: step-level `env`](02-fix-1-step-level-env.md) - A step-level env: block sets variables that only that one step can see.
* [Fix 2: job-level `env`](03-fix-2-job-level-env.md) - Moving env: up to the job makes a variable visible to every step in that job.
* [Fix 3: workflow-level `env`](04-fix-3-workflow-level-env.md) - A workflow-level env: block shares a variable with every job in the file.
* [Which one wins?](05-which-one-wins.md) - When the same name is set at several levels, the most specific one wins: step, then job, then workflow.
* [`$VAR` or `${{ env.VAR }}`?](06-var-or-env-var.md) - Use $VAR inside run: scripts and ${{ env.VAR }} everywhere GitHub evaluates YAML, because they resolve at different moments.
* [Inside `${{ }}`: the expression language and its contexts](07-inside-the-expression-language-and-its-contexts.md) - ${{ }} isn't the shell. It's GitHub's own expression language, evaluated by GitHub before anything reaches the runner. It doesn't know your variable names directly. It only knows a fixed set of top-level objects called...
* [Variables you get for free](08-variables-you-get-for-free.md) - Every job starts with default variables already set:
* [Setting a variable while the job runs](09-setting-a-variable-while-the-job-runs.md) - Some values only exist at runtime, like a version read from a file. Append NAME=value to the file in $GITHUBENV, and later steps in the same job can read it:
* [Configuration variables: values that live in Settings](10-configuration-variables-values-that-live-in-settings.md) - Configuration variables live in Settings at organisation, repository or environment level, are read with ${{ vars.NAME }}, and change without a commit.
* [`env` or `vars`? (and `secrets`)](11-env-or-vars-and-secrets.md) - 👉 Lesson 12 covers secrets in full.
* [Common mistakes](12-common-mistakes.md) - The variable slips learners make most: wrong syntax for the place, wrong scope, $GITHUB_ENV timing and secrets stored as variables.
* [Try it yourself](13-try-it-yourself.md) - This repository ships a safe version of the example that prints the docker commands instead of running them: 04-variables.yml.
* [Checkpoint](14-checkpoint.md) - Workflow, job and step. The most specific wins: step beats job beats workflow.
