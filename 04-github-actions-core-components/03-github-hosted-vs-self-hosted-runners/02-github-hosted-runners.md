---
type: Tutorial
title: "GitHub-Hosted vs Self-Hosted Runners: GitHub-hosted runners"
description: "GitHub owns the machine, starts it for your job and throws it away afterwards."
tags: [github-actions, runners, github-hosted, self-hosted, comparison]
status: stable
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-07T00:00:00Z }
sources:
  - id: gh-hosted-runners
    resource: https://docs.github.com/en/actions/concepts/runners/github-hosted-runners
    title: GitHub-hosted runners
  - id: gh-self-hosted-runners
    resource: https://docs.github.com/en/actions/concepts/runners/self-hosted-runners
    title: Self-hosted runners
  - id: gh-runner-images
    resource: https://github.com/actions/runner-images
    title: GitHub Actions runner images (preinstalled software lists)
  - id: gh-secure-use
    resource: https://docs.github.com/en/actions/reference/security/secure-use
    title: Secure use reference
  - id: gh-billing
    resource: https://docs.github.com/en/billing/concepts/product-billing/github-actions
    title: GitHub Actions billing
---

<p align="center">
  <a href="README.md">📂 <b>GitHub-Hosted vs Self-Hosted Runners</b></a> &nbsp;·&nbsp; Lesson 3 · Part 2 of 8 &nbsp;·&nbsp; ⏱️ 3 min
</p>

# ☁️ GitHub-hosted runners

GitHub owns the machine, starts it for your job and throws it away afterwards.

## 🎁 What GitHub takes off your plate

This is one of the biggest advantages of GitHub Actions. With a traditional CI server, someone on your team had three standing jobs (see [Chapter 3](../../03-problem-with-traditional-ci-cd-tools/02-hidden-costs-of-self-hosted-ci/README.md)). With GitHub-hosted runners, GitHub does all three:

<p align="center">
  <img src="../../assets/images/github-manages-infrastructure.svg" alt="GitHub handles setting up servers, scaling resources and managing the execution environment. Ubuntu, Windows and macOS runners are available out of the box" width="100%">
</p>

| # | Job | Who did it before | Who does it now |
|---|---|---|---|
| 01 | 🖥️ **Setting up servers** | You: buy, install, patch | GitHub boots a fresh VM per job |
| 02 | 📈 **Scaling resources** | You: guess capacity, queue builds | GitHub adds machines as jobs arrive |
| 03 | ⚙️ **Managing the execution environment** | You: install and update tools | GitHub maintains the OS images |

All three major operating systems work **out of the box**. Pick one with a single label: `ubuntu-latest`, `windows-latest` or `macos-latest`.

| | What you get | Detail |
|---|---|---|
| 🧼 | **A clean VM for every job** | Nothing is left over from anyone's previous run, including your own |
| 🧰 | **A stocked toolbox** | Git, Docker, Node.js, Python, Java, cloud CLIs and much more are preinstalled |
| 🖼️ | **A choice of systems** | `ubuntu-latest`, `windows-latest`, `macos-latest`, plus specific versions |
| 🔧 | **Zero maintenance** | GitHub patches and updates the images |
| 📈 | **Scale without planning** | Ten jobs get ten machines |

> [!NOTE]
> GitHub runs its Linux and Windows runners as virtual machines in Microsoft Azure. You never see or manage that infrastructure. You only see the label you asked for.

---

<p align="center">
  <a href="01-the-difference-in-one-picture.md">⬅️ The difference in one picture</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="03-self-hosted-runners.md"><b>Next: Self-hosted runners ➡️</b></a>
</p>
