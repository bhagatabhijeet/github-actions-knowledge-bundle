---
okf_version: "0.2"
---

# GitHub Actions Knowledge Bundle

* [GitHub Actions - The Knowledge Bundle](README.md) - Front door to a sequential, hands-on guide to GitHub Actions, packaged as an Open Knowledge Format (OKF) bundle.

# Chapters

* [01 - Introduction to GitHub Actions](01-introduction-to-github-actions/) - What GitHub Actions is, its six core concepts, how to read workflow YAML, and a first hands-on workflow.
* [02 - Basics of CI/CD](02-basics-of-ci-cd/) - Why CI/CD exists, continuous integration, delivery versus deployment, pipeline anatomy, and a first hands-on CI pipeline.
* [03 - The Problem with Traditional CI/CD Tools](03-problem-with-traditional-ci-cd-tools/) - The problem statement for self-hosted CI servers, their six hidden costs, and how GitHub Actions answers each one, trade-offs included.

# Sample Workflows

* [01 - Hello, Actions](.github/workflows/01-hello-world.yml) - Push and manual triggers, an input, run versus uses, default variables and a job summary.
* [02 - CI Basics](.github/workflows/02-ci-basics.yml) - A lint, test and package pipeline with a Python version matrix, pip caching and an uploaded artifact.

# Assets

* [Images](assets/images/) - SVG banners and diagrams referenced by the lessons.
* [Snippets](assets/snippets/) - Standalone YAML snippets referenced by the lessons.
* [Sample app](sample-app/) - A tiny Python package that the CI Basics workflow lints, tests and packages.

# History

* [Change log](log.md) - Date-grouped record of additions and updates to this bundle.
