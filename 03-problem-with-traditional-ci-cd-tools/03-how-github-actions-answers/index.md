# How GitHub Actions Answers the Problem

* [Overview](README.md) - The install list and the six pains checked against GitHub Actions line by line - hosted runners, fresh machines, actions instead of plugins - with the honest trade-offs and when a traditional tool is still the right call.
* [The shift in one picture](01-the-shift-in-one-picture.md) - On the left, every layer is yours. On the right, you keep the one layer that is actually about your product: the pipeline definition. That is the workflow file you learned to read in Chapter 1.
* [Abhijeet's install list, revisited](02-abhijeet-s-install-list-revisited.md) - Here are the seven tasks from Lesson 1, and what becomes of each.
* [Six pains, six answers](03-six-pains-six-answers.md) - And the day-two pains from Lesson 2:
* [Plugins vs actions](04-plugins-vs-actions.md) - This one deserves a closer look, because actions and plugins sound like the same idea.
* [Same pipeline, two worlds](05-same-pipeline-two-worlds.md) - Tessaloop's Node.js project isn't in this repository, but a small Python sample app is. Here is a lint-and-test pipeline for it, written for Jenkins:
* [What is still your job](06-what-is-still-your-job.md) - GitHub Actions doesn't remove responsibility. It moves the line.
* [The honest trade-offs](07-the-honest-trade-offs.md) - A fair comparison has two columns. Here is what you give up.
* [The middle path: self-hosted runners](08-the-middle-path-self-hosted-runners.md) - GitHub Actions also lets you bring your own machines, called self-hosted runners. GitHub still does the scheduling, the UI and the logs. Your machine does the running.
* [So which should you use?](09-so-which-should-you-use.md) - A traditional tool is still a sound choice when you have a platform team, strict rules about where builds may run, or years of working pipelines that nobody needs to change.
* [Already on a traditional tool?](10-already-on-a-traditional-tool.md) - You don't have to move everything at once. Most teams start new projects on GitHub Actions and migrate old pipelines one at a time. GitHub publishes a migration guide for Jenkins that maps each concept across:
* [Checkpoint](11-checkpoint.md) - In everything that must exist before the file runs. The Jenkinsfile needs a server, a prepared agent, plugins, a webhook and a credential. The workflow needs only to be committed.
