# Chapter 1: Introduction to GitHub Actions

* [What is GitHub Actions?](01-what-is-github-actions.md) - The plain-English answer - an automation engine inside your repository that reacts to events and runs your instructions on a fresh machine.
* [The Six Core Concepts](02-core-concepts.md) - Event, workflow, job, step, action and runner - the six words that explain every GitHub Actions workflow you will ever read.
* [Anatomy of a Workflow File](03-anatomy-of-a-workflow.md) - A line-by-line tour of workflow YAML - name, on, jobs, runs-on and steps - plus the YAML rules that trip up every beginner.
* [Your First Workflow (Hands-On)](04-your-first-workflow.md) - Run the Hello, Actions workflow that ships in this repository, read its logs, trigger it by hand, and break it on purpose.
* [Chapter 1 Cheat Sheet and Quiz](05-cheat-sheet-and-quiz.md) - Everything from Chapter 1 on one page - vocabulary, YAML keys and default variables - followed by an eight-question self-check.

# Companion Files

* [01-hello-world.yml](../.github/workflows/01-hello-world.yml) - The live workflow used in the hands-on lesson.
* [workflow-skeleton.yml](../assets/snippets/workflow-skeleton.yml) - The smallest useful workflow.
* [triggers.yml](../assets/snippets/triggers.yml) - Common events for the `on:` key.
* [run-vs-uses.yml](../assets/snippets/run-vs-uses.yml) - The two kinds of step, side by side.
* [job-dependencies.yml](../assets/snippets/job-dependencies.yml) - Ordering jobs with `needs`.
