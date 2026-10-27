# Chapter 4 Cheat Sheet and Quiz

* [Overview](README.md) - The core components on one page - workflow, job, step, runner, how a run unfolds, hosted versus self-hosted - followed by an eleven-question self-check.
* [The four components](01-the-four-components.md) - Every Chapter 4 building block on one page: workflow, job, step, runner and action, plus quick rules for scripts, jobs, artifacts, variables, secrets and triggers.
* [A run in six stages](02-a-run-in-six-stages.md) - Every run moves through the same six stages: event, queue, provision, execute, report and clean up.
* [How results roll up](03-how-results-roll-up.md) - A step passes when it exits cleanly, a job when every step passes, and a run when every job passes.
* [Matrix in four lines](04-matrix-in-four-lines.md) - A matrix turns one job definition into one job per value, and fail-fast decides whether one failure cancels the rest.
* [Hosted vs self-hosted](05-hosted-vs-self-hosted.md) - GitHub-hosted and self-hosted runners compared side by side: who maintains them, state, software, network, job length and runs-on.
* [Finding your way in the Actions tab](06-finding-your-way-in-the-actions-tab.md) - Where to click in the Actions tab to find a step log, the cause of a failure, the artifacts a run produced, or the re-run button.
* [Golden rules](07-golden-rules.md) - Jobs in parallel, steps in series. Most surprises come from forgetting one half.
* [Quiz](08-quiz.md) - Eleven quick questions on components, runs, matrices, runners, secrets, variables and triggers, with answers hidden until you click.
* [Chapter complete](09-chapter-complete.md) - You can point at any line of a workflow and say which component it is, describe what happens between a push and a green tick, and choose the right kind of runner.
