# Chapter 4: GitHub Actions Core Components

* [The Core Components](01-the-core-components.md) - Workflow, job, step and runner seen inside one real workflow file - what each part is, how they nest, and how a small matrix turns one job into three machines.
* [Life of a Workflow Run (Hands-On)](02-life-of-a-workflow-run.md) - Follow one push from event to green tick - three runners provisioned in parallel, steps in series, how job results roll up - then run the Core Components workflow and read its logs and artifacts.
* [GitHub-Hosted vs Self-Hosted Runners](03-github-hosted-vs-self-hosted-runners.md) - The two kinds of runner compared - who maintains them, what state they keep, how far you can customise them, what they cost - plus two common myths and a guide to choosing.
* [What Are Actions?](04-what-are-actions.md) - The reusable building blocks of GitHub Actions - what an action is, how to read a uses line, the three kinds of action, where to find them in the Marketplace, and how to pin them safely.
* [Configuring the Checkout Action (Hands-On)](05-configuring-the-checkout-action.md) - Why a fresh runner has none of your code, how actions/checkout fixes it, and the inputs you'll actually use - fetch-depth, ref, path, repository, token, submodules, sparse-checkout and persist-credentials.
* [Multi-line Commands and Third-Party Tools (Hands-On)](06-multiline-commands-and-third-party-tools.md) - Run several commands in one step with YAML's literal and folded blocks, understand how the shell treats them, then install and use a third-party tool on the runner - with apt, pip, npm or a setup action.
* [Executing Shell Scripts in a Workflow (Hands-On)](07-executing-shell-scripts.md) - Move a workflow's commands into a shell script in the repository and run it in one step - the shebang, set -euo pipefail, the executable bit, LF line endings, passing arguments, and the errors you'll meet on the way.
* [Chapter 4 Cheat Sheet and Quiz](08-cheat-sheet-and-quiz.md) - The core components on one page - workflow, job, step, runner, how a run unfolds, hosted versus self-hosted - followed by an eight-question self-check.

# Companion Files

* [04-core-components.yml](../.github/workflows/04-core-components.yml) - The live workflow used in the hands-on lesson: one job, three operating systems, one artifact each.
* [sample-app](../sample-app/) - The tiny Python app the workflow tests.
* [workflow-yaml-annotated.svg](../assets/images/workflow-yaml-annotated.svg) - A workflow file with every component labelled.
* [workflow-run-timeline.svg](../assets/images/workflow-run-timeline.svg) - One push fanning out to three runners and rolling up into one result.
* [hosted-vs-self-hosted.svg](../assets/images/hosted-vs-self-hosted.svg) - The two kinds of runner compared row by row.
* [github-manages-infrastructure.svg](../assets/images/github-manages-infrastructure.svg) - The three jobs GitHub handles for you, and the three operating systems available out of the box.
* [04-checkout.yml](../.github/workflows/04-checkout.yml) - Live workflow: the same steps with and without checkout.
* [04-multiline-commands.yml](../.github/workflows/04-multiline-commands.yml) - Live workflow: install cowsay, use it in a multi-line step, check the result.
* [04-shell-script.yml](../.github/workflows/04-shell-script.yml) - Live workflow: check out, then run one script.
* [ascii-script.sh](../scripts/ascii-script.sh) - The script it runs.
* [workflow-to-shell-script.svg](../assets/images/workflow-to-shell-script.svg) - Six inline steps become a two-step workflow and a script file.
* [multiline-run-blocks.svg](../assets/images/multiline-run-blocks.svg) - Literal versus folded run blocks, and the install-use-check flow.
* [checkout-before-after.svg](../assets/images/checkout-before-after.svg) - An empty runner versus one with the repository checked out.
* [anatomy-of-an-action.svg](../assets/images/anatomy-of-an-action.svg) - A uses line broken into owner, repository, version and inputs, plus the three kinds of action.
