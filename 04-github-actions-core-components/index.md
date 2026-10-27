# Chapter 4: GitHub Actions Core Components

* [The Core Components](01-the-core-components/README.md) - Workflow, job, step and runner seen inside one real workflow file - what each part is, how they nest, and how a small matrix turns one job into three machines.
* [Life of a Workflow Run (Hands-On)](02-life-of-a-workflow-run/README.md) - Follow one push from event to green tick - three runners provisioned in parallel, steps in series, how job results roll up - then run the Core Components workflow and read its logs and artifacts.
* [GitHub-Hosted vs Self-Hosted Runners](03-github-hosted-vs-self-hosted-runners/README.md) - The two kinds of runner compared - who maintains them, what state they keep, how far you can customise them, what they cost - plus two common myths and a guide to choosing.
* [What Are Actions?](04-what-are-actions/README.md) - The reusable building blocks of GitHub Actions - what an action is, how to read a uses line, the three kinds of action, where to find them in the Marketplace, and how to pin them safely.
* [Configuring the Checkout Action (Hands-On)](05-configuring-the-checkout-action/README.md) - Why a fresh runner has none of your code, how actions/checkout fixes it, and the inputs you'll actually use - fetch-depth, ref, path, repository, token, submodules, sparse-checkout and persist-credentials.
* [Multi-line Commands and Third-Party Tools (Hands-On)](06-multiline-commands-and-third-party-tools/README.md) - Run several commands in one step with YAML's literal and folded blocks, understand how the shell treats them, then install and use a third-party tool on the runner - with apt, pip, npm or a setup action.
* [Executing Shell Scripts in a Workflow (Hands-On)](07-executing-shell-scripts/README.md) - Move a workflow's commands into a shell script in the repository and run it in one step - the shebang, set -euo pipefail, the executable bit, LF line endings, passing arguments, and the errors you'll meet on the way.
* [Workflows with Multiple Jobs (Hands-On)](08-workflows-with-multiple-jobs/README.md) - Split a workflow into build, test and deploy jobs - why they run in parallel by default, how needs puts them in order, how artifacts carry files between runners, and how to read the job graph.
* [Executing Jobs in Sequence with needs (Hands-On)](09-executing-jobs-in-sequence/README.md) - A deep dive into needs - the cost of sequencing, chains, fan-out and fan-in, how failure turns into skipped, status functions like always() and !cancelled(), needs.<job>.result, and why outputs only flow from direct dependencies.
* [Storing Workflow Data as Artifacts (Hands-On)](10-storing-workflow-data-as-artifacts/README.md) - Keep files after the runner is gone - what artifacts are, every upload-artifact input worth knowing, unique names and immutability, downloading by pattern, from the browser, the CLI or another run, retention and storage, and when to use cache, releases or packages instead.
* [Working with Variables (Hands-On)](11-working-with-variables/README.md) - Stop hard-coding values - env at workflow, job and step level and which one wins, $VAR versus ${{ env.VAR }}, default GITHUB_ variables, setting values at runtime with $GITHUB_ENV, and configuration variables stored in Settings with the vars context.
* [Working with Repository-Level Secrets (Hands-On)](12-working-with-repository-secrets/README.md) - Get passwords and tokens out of your workflow files - what a secret is and how GitHub protects it, creating repository secrets in Settings or with gh, using them safely in run steps and actions, log masking and its limits, forks, GITHUB_TOKEN, and what to do when a secret leaks.
* [Triggering Workflows in Detail (Hands-On)](13-triggering-workflows-in-detail/README.md) - Everything that can start a workflow - repository events and activity types, branch, tag and path filters, manual runs with workflow_dispatch and typed inputs, cron schedules, repository_dispatch, workflow_run and workflow_call, which commit a run uses, and the GITHUB_TOKEN loop guard.
* [Chapter 4 Cheat Sheet and Quiz](14-cheat-sheet-and-quiz/README.md) - The core components on one page - workflow, job, step, runner, how a run unfolds, hosted versus self-hosted - followed by an eleven-question self-check.

# Companion Files

* [04-triggers.yml](../.github/workflows/04-triggers.yml) - Live workflow: a filtered push, a weekly schedule, a manual run with typed inputs and a repository_dispatch, each printing what started it.
* [trigger-doors.svg](../assets/images/trigger-doors.svg) - The four ways a run can start, and what GitHub does when an event fires.
* [workflow-dispatch-form.svg](../assets/images/workflow-dispatch-form.svg) - workflow_dispatch inputs in YAML and the Run workflow form GitHub draws from them.
* [04-core-components.yml](../.github/workflows/04-core-components.yml) - The live workflow used in the hands-on lesson: one job, three operating systems, one artifact each.
* [sample-app](../sample-app/) - The tiny Python app the workflow tests.
* [workflow-yaml-annotated.svg](../assets/images/workflow-yaml-annotated.svg) - A workflow file with every component labelled.
* [workflow-run-timeline.svg](../assets/images/workflow-run-timeline.svg) - One push fanning out to three runners and rolling up into one result.
* [hosted-vs-self-hosted.svg](../assets/images/hosted-vs-self-hosted.svg) - The two kinds of runner compared row by row.
* [github-manages-infrastructure.svg](../assets/images/github-manages-infrastructure.svg) - The three jobs GitHub handles for you, and the three operating systems available out of the box.
* [04-checkout.yml](../.github/workflows/04-checkout.yml) - Live workflow: the same steps with and without checkout.
* [04-multiline-commands.yml](../.github/workflows/04-multiline-commands.yml) - Live workflow: install cowsay, use it in a multi-line step, check the result.
* [04-secrets.yml](../.github/workflows/04-secrets.yml) - Live workflow: log masking, ::add-mask:: and an optional Docker Hub login, safe to run with no secrets set.
* [secrets-step1-navigate.svg](../assets/images/secrets-step1-navigate.svg) - Where to find Settings → Secrets and variables → Actions, with numbered callouts.
* [secrets-step2-create.svg](../assets/images/secrets-step2-create.svg) - The New secret form, and what you can and can't do once it's saved.
* [secrets-step3-variable.svg](../assets/images/secrets-step3-variable.svg) - The New variable form, and variables versus secrets side by side.
* [secrets-step4-run-logs.svg](../assets/images/secrets-step4-run-logs.svg) - Run logs showing the masked password and the empty-username gotcha.
* [secret-journey.svg](../assets/images/secret-journey.svg) - How a secret is encrypted, stored, decrypted and masked, and what it is and isn't protected from.
* [04-variables.yml](../.github/workflows/04-variables.yml) - Live workflow: env at three levels, which wins, default variables, $GITHUB_ENV and vars with a fallback.
* [variable-scopes.svg](../assets/images/variable-scopes.svg) - Nested env scopes, configuration variable precedence, and $VAR versus ${{ env.VAR }}.
* [04-artifacts.yml](../.github/workflows/04-artifacts.yml) - Live workflow: three matrix jobs upload uniquely named artifacts, a gallery job collects them by pattern.
* [artifact-lifecycle.svg](../assets/images/artifact-lifecycle.svg) - From runner to artifact storage to the four ways of downloading.
* [04-needs-sequence.yml](../.github/workflows/04-needs-sequence.yml) - Live workflow: build, test, deploy and an always-on report, with a switch to make the tests fail.
* [needs-sequence-timeline.svg](../assets/images/needs-sequence-timeline.svg) - Timelines for parallel jobs, a needs chain, and a failure that skips deploy.
* [04-multiple-jobs.yml](../.github/workflows/04-multiple-jobs.yml) - Live workflow: build, test and deploy jobs chained with needs, passing a file by artifact.
* [multiple-jobs-needs.svg](../assets/images/multiple-jobs-needs.svg) - Parallel jobs failing versus jobs chained with needs and artifacts.
* [04-shell-script.yml](../.github/workflows/04-shell-script.yml) - Live workflow: check out, then run one script.
* [ascii-script.sh](../scripts/ascii-script.sh) - The script it runs.
* [workflow-to-shell-script.svg](../assets/images/workflow-to-shell-script.svg) - Six inline steps become a two-step workflow and a script file.
* [multiline-run-blocks.svg](../assets/images/multiline-run-blocks.svg) - Literal versus folded run blocks, and the install-use-check flow.
* [checkout-before-after.svg](../assets/images/checkout-before-after.svg) - An empty runner versus one with the repository checked out.
* [anatomy-of-an-action.svg](../assets/images/anatomy-of-an-action.svg) - A uses line broken into owner, repository, version and inputs, plus the three kinds of action.
