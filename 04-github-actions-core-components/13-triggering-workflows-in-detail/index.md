# Triggering Workflows in Detail

* [Overview](README.md) - Everything that can start a workflow - repository events and their activity types, branch, tag and path filters, manual runs with workflow_dispatch and typed inputs, cron schedules, repository_dispatch, workflow_run and workflow_call, which commit a run uses, and the loop guard on GITHUB_TOKEN.
* [Four doors into a workflow](01-four-doors-into-a-workflow.md) - Workflows start from four places: events in your repository, a manual button, a schedule, or a call from outside or from another workflow.
* [Repository events and activity types](02-repository-events-and-activity-types.md) - Most of the 35 or so events have activity types: the different things that can happen to the same object. An issue can be opened, edited, labeled, closed and more. Without types: you get every activity type, which is...
* [Filters: branches, tags and paths](03-filters-branches-tags-and-paths.md) - Activity types say what happened. Filters say where. They are how you stop the README typo from starting a full build.
* [Manual runs with `workflow_dispatch`](04-manual-runs-with-workflow-dispatch.md) - This is the trigger in the screenshot from GitHub's docs. It adds a Run workflow button to the workflow's page in the Actions tab.
* [Schedules with cron](05-schedules-with-cron.md) - Run a workflow on a timer with five-field cron lines, and know the limits: UTC by default, 5-minute minimum, late or dropped runs, default branch only.
* [Triggers from outside and from other workflows](06-triggers-from-outside-and-from-other-workflows.md) - Any system with a token can start a workflow through the API: a CMS, a monitoring tool, a script on your laptop.
* [The loop guard: `GITHUB_TOKEN` doesn't start new runs](07-the-loop-guard-github-token-doesn-t.md) - Picture a workflow that runs on push and pushes a formatting fix. If that push started the workflow again, it would loop forever. GitHub prevents this:
* [`pull_request` vs `pull_request_target`](08-pull-request-vs-pull-request-target.md) - These look alike but run in very different security contexts.
* [Which trigger do I need?](09-which-trigger-do-i-need.md) - Real workflows often combine several, like the companion workflow: push for changes, schedule as a safety net, and workflowdispatch so you can always run it by hand.
* [Common mistakes](10-common-mistakes.md) - The trigger mistakes that leave workflows silent or running too often, with the cause and fix for each.
* [Try it yourself](11-try-it-yourself.md) - The companion workflow 04-triggers.yml listens on all four doors and prints what started it.
* [Checkpoint](12-checkpoint.md) - The button only appears when the workflow file is on the default branch. Merge it to main first. After that you can choose the feature branch in the form.
