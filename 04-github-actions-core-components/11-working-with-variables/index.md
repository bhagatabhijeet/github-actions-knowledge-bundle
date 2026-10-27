# Working with Variables

* [Overview](README.md) - Stop hard-coding values - env at workflow, job and step level and which one wins, $VAR versus ${{ env.VAR }}, default GITHUB_ variables, setting values at runtime with $GITHUB_ENV, and configuration variables stored in Settings with the vars context.
* [Spot the problems](01-spot-the-problems.md) - Here is a workflow that builds a Docker image, pushes it, and runs it. It works. Before reading on, see how many problems you can find.
* [Fix 1: step-level `env`](02-fix-1-step-level-env.md) - env: defines environment variables. Put it on a step, and only that step sees them:
* [Fix 2: job-level `env`](03-fix-2-job-level-env.md) - Move env: up to the job, and every step in that job sees it:
* [Fix 3: workflow-level `env`](04-fix-3-workflow-level-env.md) - Put env: at the top, and every job sees it:
* [Which one wins?](05-which-one-wins.md) - When the same name is set at several levels, the most specific one wins: step, then job, then workflow.
* [`$VAR` or `${{ env.VAR }}`?](06-var-or-env-var.md) - There are two ways to read a variable, and they work at different moments:
* [Inside `${{ }}`: the expression language and its contexts](07-inside-the-expression-language-and-its-contexts.md) - ${{ }} isn't the shell. It's GitHub's own expression language, evaluated by GitHub before anything reaches the runner. It doesn't know your variable names directly. It only knows a fixed set of top-level objects called...
* [Variables you get for free](08-variables-you-get-for-free.md) - Every job starts with default variables already set:
* [Setting a variable while the job runs](09-setting-a-variable-while-the-job-runs.md) - Some values only exist at runtime, like a version read from a file. Append NAME=value to the file in $GITHUBENV, and later steps in the same job can read it:
* [Configuration variables: values that live in Settings](10-configuration-variables-values-that-live-in-settings.md) - env: lives in the YAML, so changing it means a commit. Configuration variables live in the repository's settings, so you can change them without touching the workflow, and share them across many workflows.
* [`env` or `vars`? (and `secrets`)](11-env-or-vars-and-secrets.md) - 👉 Lesson 12 covers secrets in full.
* [Common mistakes](12-common-mistakes.md) - Common mistakes
* [Try it yourself](13-try-it-yourself.md) - This repository ships a safe version of the example that prints the docker commands instead of running them: 04-variables.yml.
* [Checkpoint](14-checkpoint.md) - Workflow, job and step. The most specific wins: step beats job beats workflow.
