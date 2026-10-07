# Chapter 3: The Problem with Traditional CI/CD Tools

* [The Problem Statement](01-the-problem-statement.md) - A Monday meeting about a build server that keeps breaking - the complaints that add up to the case against traditional, self-hosted CI/CD tools.
* [The Hidden Costs of Running Your Own CI Server](02-hidden-costs-of-self-hosted-ci.md) - Six pains of traditional self-hosted CI/CD tools - server upkeep, snowflake agents, wrong-sized capacity, fragile plugins, integration glue and knowledge silos - and why a free licence is not a free tool.
* [How GitHub Actions Answers the Problem](03-how-github-actions-answers.md) - The team's wish list checked against GitHub Actions line by line - hosted runners, fresh machines, actions instead of plugins - with the honest trade-offs and when a traditional tool is still the right call.
* [Chapter 3 Cheat Sheet and Quiz](04-cheat-sheet-and-quiz.md) - The case against traditional CI/CD tools on one page - the six pains, how GitHub Actions answers each, the trade-offs - followed by an eight-question self-check.

# Companion Files

* [who-maintains-what.svg](../assets/images/who-maintains-what.svg) - Side-by-side picture of the layers you maintain with a self-hosted CI server versus GitHub Actions on hosted runners.
* [02-ci-basics.yml](../.github/workflows/02-ci-basics.yml) - The live pipeline whose lint and test stages are compared with a Jenkinsfile in Lesson 3.
* [sample-app](../sample-app/) - The tiny Python app both versions of that pipeline build.
