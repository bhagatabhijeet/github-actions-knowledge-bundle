# Chapter 4: GitHub Actions Core Components

* [The Core Components](01-the-core-components.md) - Workflow, job, step and runner seen inside one real workflow file - what each part is, how they nest, and how a small matrix turns one job into three machines.
* [Life of a Workflow Run (Hands-On)](02-life-of-a-workflow-run.md) - Follow one push from event to green tick - three runners provisioned in parallel, steps in series, how job results roll up - then run the Core Components workflow and read its logs and artifacts.
* [GitHub-Hosted vs Self-Hosted Runners](03-github-hosted-vs-self-hosted-runners.md) - The two kinds of runner compared - who maintains them, what state they keep, how far you can customise them, what they cost - plus two common myths and a guide to choosing.
* [Chapter 4 Cheat Sheet and Quiz](04-cheat-sheet-and-quiz.md) - The core components on one page - workflow, job, step, runner, how a run unfolds, hosted versus self-hosted - followed by an eight-question self-check.

# Companion Files

* [04-core-components.yml](../.github/workflows/04-core-components.yml) - The live workflow used in the hands-on lesson: one job, three operating systems, one artifact each.
* [sample-app](../sample-app/) - The tiny Python app the workflow tests.
* [workflow-yaml-annotated.svg](../assets/images/workflow-yaml-annotated.svg) - A workflow file with every component labelled.
* [workflow-run-timeline.svg](../assets/images/workflow-run-timeline.svg) - One push fanning out to three runners and rolling up into one result.
* [hosted-vs-self-hosted.svg](../assets/images/hosted-vs-self-hosted.svg) - The two kinds of runner compared row by row.
* [github-manages-infrastructure.svg](../assets/images/github-manages-infrastructure.svg) - The three jobs GitHub handles for you, and the three operating systems available out of the box.
