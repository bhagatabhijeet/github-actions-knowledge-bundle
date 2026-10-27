# Your First Workflow

* [Overview](README.md) - Run the Hello, Actions workflow that ships in this repository, read its logs, trigger it by hand, and break it on purpose.
* [Before you start](01-before-you-start.md) - The checklist before the hands-on: your own fork of this repository with Actions enabled.
* [The workflow](02-the-workflow.md) - The full Hello, Actions workflow file you will run in this lesson.
* [What each part teaches](03-what-each-part-teaches.md) - A fresh runner is an empty machine. Your repository is not on it until actions/checkout puts it there. Forgetting checkout is the classic first-week mistake.
* [Exercise 1: Run it with the button](04-exercise-1-run-it-with-the-button.md) - Start the Hello, Actions workflow by hand from the Actions tab with the Run workflow button, and why that button needs the file on the default branch.
* [Exercise 2: Read the logs](05-exercise-2-read-the-logs.md) - How to open a run, expand each step's log and find the output your workflow printed.
* [Exercise 3: Trigger it with a push](06-exercise-3-trigger-it-with-a-push.md) - Push a small commit to main and watch the push event start the workflow on its own.
* [Exercise 4: Break it on purpose](07-exercise-4-break-it-on-purpose.md) - Add a failing step on purpose to see how a non-zero exit code turns a run red and stops the job.
* [Something went wrong?](08-something-went-wrong.md) - A symptom-to-cause table for the common first-run problems: workflow not listed, invalid YAML, no Run workflow button, and nothing running on push.
