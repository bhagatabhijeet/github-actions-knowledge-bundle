# Chapter 4 Cheat Sheet and Quiz

* [Overview](README.md) - The core components on one page - workflow, job, step, runner, how a run unfolds, hosted versus self-hosted - followed by an eight-question self-check.
* [The four components](01-the-four-components.md) - A runner starts empty. Make actions/checkout the first step of any job that reads your files. Add fetch-depth: 0 when you need full history.
* [A run in six stages](02-a-run-in-six-stages.md) - A run in six stages
* [How results roll up](03-how-results-roll-up.md) - How results roll up
* [Matrix in four lines](04-matrix-in-four-lines.md) - Matrix in four lines
* [Hosted vs self-hosted](05-hosted-vs-self-hosted.md) - Hosted vs self-hosted
* [Finding your way in the Actions tab](06-finding-your-way-in-the-actions-tab.md) - Finding your way in the Actions tab
* [Golden rules](07-golden-rules.md) - Jobs in parallel, steps in series. Most surprises come from forgetting one half.
* [Quiz](08-quiz.md) - Workflow, job, step. The fourth, the runner, isn't inside the others: it's the machine each job runs on.
* [Chapter complete](09-chapter-complete.md) - You can point at any line of a workflow and say which component it is, describe what happens between a push and a green tick, and choose the right kind of runner.
