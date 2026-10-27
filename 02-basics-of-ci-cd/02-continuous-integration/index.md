# Continuous Integration

* [Overview](README.md) - What CI really means - merge small changes often and let an automated build prove each one - with the checks a CI run performs and the habits that make it work.
* [The definition](01-the-definition.md) - Continuous Integration is the habit of merging small changes into the shared branch frequently, with every change automatically built and tested.
* [A day in the life of a change](02-a-day-in-the-life-of-a.md) - Notice step 4. The failure reached the author within minutes, while the change was still fresh in their head, and before a reviewer spent any time on it. That fast feedback is the whole value of CI.
* [Two developers, one `main`](03-two-developers-one-main.md) - Real teams have several changes in flight at once. Follow two of them.
* [What does a CI run check?](04-what-does-a-ci-run-check.md) - Checks are ordered cheapest first, so obvious mistakes fail fast.
* [The meaning of the tick](05-the-meaning-of-the-tick.md) - What the pending, success and failure marks on a commit mean, and how required checks turn the green tick into a merge gate.
* [The five habits of CI](06-the-five-habits-of-ci.md) - Tools don't do CI. Teams do. These habits are what make it real:
* [How it maps to GitHub Actions](07-how-it-maps-to-github-actions.md) - You already know the pieces from Chapter 1. CI is just a particular way of arranging them.
* [Checkpoint](08-checkpoint.md) - No. They have automated testing, but they aren't integrating continuously. After three weeks, merging is still a painful event.
