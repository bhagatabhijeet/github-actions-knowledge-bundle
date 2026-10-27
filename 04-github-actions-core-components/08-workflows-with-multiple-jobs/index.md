# Workflows with Multiple Jobs

* [Overview](README.md) - Split a workflow into build, test and deploy jobs - why they run in parallel by default, how needs puts them in order, how artifacts carry files between runners, and how to read the job graph.
* [Why split into jobs?](01-why-split-into-jobs.md) - What you gain by splitting one big job into several: clearer logs, parallel speed, partial re-runs, and per-job runners and permissions.
* [Attempt 1: just split it](02-attempt-1-just-split-it.md) - Splitting the workflow into three jobs naively makes two of them fail, because jobs run in parallel on separate runners.
* [Fix 1: put the jobs in order with `needs`](03-fix-1-put-the-jobs-in-order.md) - Use needs: with one job ID or a list to make jobs wait for each other.
* [Fix 2: carry the file with artifacts](04-fix-2-carry-the-file-with-artifacts.md) - An artifact is a file or folder a job uploads to storage attached to the workflow run. Any later job in the same run can download it.
* [Reading the job graph](05-reading-the-job-graph.md) - Read the job graph on the run's Summary page to see how needs: connects jobs and where a run failed.
* [Artifacts, outputs or cache?](06-artifacts-outputs-or-cache.md) - Choose between artifacts, job outputs and the cache to pass data between jobs or between runs.
* [Try it yourself](07-try-it-yourself.md) - This repository ships the finished three-job workflow: 04-multiple-jobs.yml.
* [Checkpoint](08-checkpoint.md) - All at the same time, each on its own runner. There is no order.
