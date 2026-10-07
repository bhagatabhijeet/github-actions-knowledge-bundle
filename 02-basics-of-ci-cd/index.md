# Chapter 2: Basics of CI/CD

* [What is CI/CD?](01-what-is-ci-cd.md) - The problem CI/CD solves - integration hell and scary releases - and the simple idea behind it - make small changes and let machines verify and ship them.
* [Continuous Integration](02-continuous-integration.md) - What CI really means - merge small changes often and let an automated build prove each one - with the checks a CI run performs and the habits that make it work.
* [Continuous Delivery vs Continuous Deployment](03-delivery-vs-deployment.md) - The two meanings of CD untangled - one keeps a human approval before production, the other removes it - with environments, artifacts and how to choose.
* [Anatomy of a Pipeline](04-anatomy-of-a-pipeline.md) - The stages every pipeline shares - source, build, test, package, deploy - and exactly how each one maps onto GitHub Actions jobs, needs, matrices and artifacts.
* [Your First CI Pipeline (Hands-On)](05-your-first-ci-pipeline.md) - Build a real three-stage pipeline - lint, test across a matrix, package an artifact - using the CI Basics workflow and sample app that ship in this repository.
* [Chapter 2 Cheat Sheet and Quiz](06-cheat-sheet-and-quiz.md) - CI/CD on one page - definitions, pipeline stages, the Actions features that implement them - followed by an eight-question self-check.

# Companion Files

* [02-ci-basics.yml](../.github/workflows/02-ci-basics.yml) - The live three-stage CI pipeline used in the hands-on lesson.
* [sample-app](../sample-app/) - The tiny Python app the pipeline lints, tests and packages.
* [job-dependencies.yml](../assets/snippets/job-dependencies.yml) - Ordering jobs with `needs`.
