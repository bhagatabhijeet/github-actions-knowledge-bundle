# Workflows with Multiple Jobs

* [Overview](README.md) - Split a workflow into build, test and deploy jobs - why they run in parallel by default, how needs puts them in order, how artifacts carry files between runners, and how to read the job graph.
* [Why split into jobs?](01-why-split-into-jobs.md) - Why split into jobs?
* [Attempt 1: just split it](02-attempt-1-just-split-it.md) - Push it, and two of the three jobs fail within seconds:
* [Fix 1: put the jobs in order with `needs`](03-fix-1-put-the-jobs-in-order.md) - needs: takes one job ID or a list:
* [Fix 2: carry the file with artifacts](04-fix-2-carry-the-file-with-artifacts.md) - An artifact is a file or folder a job uploads to storage attached to the workflow run. Any later job in the same run can download it.
* [Reading the job graph](05-reading-the-job-graph.md) - Open the run's Summary and GitHub draws the jobs as a graph:
* [Artifacts, outputs or cache?](06-artifacts-outputs-or-cache.md) - Three ways to pass something from one job to another, or from one run to the next:
* [Try it yourself](07-try-it-yourself.md) - This repository ships the finished three-job workflow: 04-multiple-jobs.yml.
* [Checkpoint](08-checkpoint.md) - All at the same time, each on its own runner. There is no order.
