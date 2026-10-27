# The Six Core Concepts

* [Overview](README.md) - Event, workflow, job, step, action and runner - the six words that explain every GitHub Actions workflow you will ever read.
* [1. Event: the trigger](01-1-event-the-trigger.md) - An event is something that happened. It's the reason a workflow starts.
* [2. Workflow: the recipe](02-2-workflow-the-recipe.md) - A workflow is one YAML file in .github/workflows/. It names the events it listens for and the jobs to run when they fire.
* [3. Job: a unit of work on one machine](03-3-job-a-unit-of-work-on.md) - What a job is, why jobs run in parallel on separate machines, how needs puts them in order, and how long one may run.
* [4. Step: one thing at a time](04-4-step-one-thing-at-a-time.md) - Steps are the individual tasks inside a job. They run in order, top to bottom, and because they share a runner, they share its files. Step 1 checks out the code, so step 2 can test it.
* [5. Action: a reusable building block](05-5-action-a-reusable-building-block.md) - An action is packaged logic that someone already wrote so you don't have to. You call it with uses:.
* [6. Runner: the machine](06-6-runner-the-machine.md) - GitHub-hosted versus self-hosted runners, the fresh-VM-per-job model, and which shell runs your run: steps.
* [The whole family, one table](07-the-whole-family-one-table.md) - All six core concepts side by side in one table, with what each one is and where it appears in YAML.
* [Checkpoint](08-checkpoint.md) - Quick self-check on the six core concepts, including whether two jobs without needs run in order or in parallel.
