# The Problem Statement

* [Overview](README.md) - A new DevOps lead plans a pipeline for a Node.js project, picks a traditional CI server, and discovers how much he must install and maintain before the first build - the case that leads to GitHub Actions.
* [Meet Tessaloop Technologies](01-meet-tessaloop-technologies.md) - Tessaloop Technologies is a made-up company. Its situation is not: you'll find this story inside most software teams.
* [What Abhijeet found](02-what-abhijeet-found.md) - Before designing anything, he takes a quick look at how the Node.js project has been built so far.
* [His four-step plan](03-his-four-step-plan.md) - Abhijeet writes down a plan that addresses every finding:
* [Which tool will run all this?](04-which-tool-will-run-all-this.md) - Something has to execute those four steps every time code changes. There is no shortage of candidates: Jenkins, Travis CI, Bamboo, Spinnaker, CircleCI and more.
* [The bill before the first build](05-the-bill-before-the-first-build.md) - And that is only the first project.
* [What "traditional CI/CD tool" means here](06-what-traditional-ci-cd-tool-means-here.md) - In this guide, a traditional CI/CD tool is a CI server that you install and operate yourself. Jenkins is the best-known example. TeamCity and Bamboo are in the same family when run on your own machines.
* [The problem statement](07-the-problem-statement.md) - Put Abhijeet's list into one sentence and you get this:
* [Abhijeet's two criteria](08-abhijeet-s-two-criteria.md) - So he goes looking again, this time with two requirements written at the top of the page:
* [Checkpoint](09-checkpoint.md) - A CI server that you install and run on your own machines, made of a central server, build agents and plugins. Jenkins is the classic example.
