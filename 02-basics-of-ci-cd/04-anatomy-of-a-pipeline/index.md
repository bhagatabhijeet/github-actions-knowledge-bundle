# Anatomy of a Pipeline

* [Overview](README.md) - The stages every pipeline shares - source, build, test, package, deploy - and exactly how each one maps onto GitHub Actions jobs, needs, matrices and artifacts.
* [The five stations](01-the-five-stations.md) - Each stage is a quality gate. A change only moves right if the gate opens. A failure anywhere stops the line.
* [Pipelines in GitHub Actions](02-pipelines-in-github-actions.md) - GitHub Actions has no keyword called pipeline or stage. You build them from pieces you already know:
* [Fan-out and fan-in](03-fan-out-and-fan-in.md) - needs takes a list, so stages can run side by side and then join up.
* [The matrix: one job, many variations](04-the-matrix-one-job-many-variations.md) - "Does it work on Python 3.12, 3.13 and 3.14?" Don't copy the job three times. Describe the variations and let GitHub multiply.
* [Carrying things between stages](05-carrying-things-between-stages.md) - Remember the rule from Chapter 1: every job gets a fresh, empty runner. So how does the thing you built in package reach deploy?
* [What makes a pipeline good?](06-what-makes-a-pipeline-good.md) - What makes a pipeline good?
* [Checkpoint](07-checkpoint.md) - Make each stage a job and give B needs: A.
