# Life of a Workflow Run

* [Overview](README.md) - Follow one push from event to green tick - three runners provisioned in parallel, steps in series, how job results roll up - then run the Core Components workflow and read its logs and artifacts.
* [The whole run in one picture](01-the-whole-run-in-one-picture.md) - A single timeline of one push: three jobs start in parallel on three operating systems, and the run passes only when all three pass.
* [Six stages](02-six-stages.md) - The six stages every run goes through - event, queue, provision, execute, report and clean up - and what happens in each.
* [Parallel outside, serial inside](03-parallel-outside-serial-inside.md) - Two rules explain the shape of the picture.
* [How results roll up](04-how-results-roll-up.md) - Every level gets its own verdict.
* [Run it yourself](05-run-it-yourself.md) - This repository ships the workflow from the picture: 04-core-components.yml. It tests the sample app on Ubuntu, Windows and macOS.
* [Where everything lives](06-where-everything-lives.md) - Where to find runs, jobs, step logs, artifacts and the re-run button in the Actions tab.
* [Checkpoint](07-checkpoint.md) - Not yet. The run is only marked successful once every job has finished successfully. Until then it shows as in progress.
