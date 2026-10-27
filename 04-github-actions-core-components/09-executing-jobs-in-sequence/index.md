# Executing Jobs in Sequence with needs

* [Overview](README.md) - A deep dive into needs - the cost of sequencing, chains, fan-out and fan-in, how failure turns into skipped, status functions like always() and !cancelled(), needs.<job>.result, and why outputs only flow from direct dependencies.
* [The rule in one sentence](01-the-rule-in-one-sentence.md) - A job with needs: waits until every job it lists has finished successfully. If any of them fails or is skipped, it is skipped too.
* [What sequencing costs, and buys](02-what-sequencing-costs-and-buys.md) - Sequence only what truly depends on something else. Lint, unit tests and a security scan don't depend on each other, so let them run side by side, and put needs: only on the job that must wait for all of them. The run...
* [Four shapes you can build](03-four-shapes-you-can-build.md) - Four shapes you can build
* [When a job fails: skipped, not failed](04-when-a-job-fails-skipped-not-failed.md) - Failure spreads down the graph as skipped:
* [Overriding the rule with `if:`](05-overriding-the-rule-with-if.md) - Sometimes a job should run after a failure: a report, a Slack alert, a cleanup. Add a job-level if: with a status function:
* [Outputs only flow from direct `needs`](06-outputs-only-flow-from-direct-needs.md) - A job can read needs.<job>.outputs only for jobs it lists in its own needs:. Being further down the chain isn't enough:
* [Common mistakes](07-common-mistakes.md) - Common mistakes
* [Try it yourself](08-try-it-yourself.md) - This repository ships a four-job pipeline with a "break it" switch: 04-needs-sequence.yml.
* [Checkpoint](09-checkpoint.md) - It's skipped too. A job runs only if everything it needs succeeded, and skipped isn't success.
