---
type: Tutorial
title: "GitHub-Hosted vs Self-Hosted Runners: Two myths"
description: "You can. A step can install whatever it needs, and on Linux you even have passwordless sudo:"
tags: [github-actions, runners, github-hosted, self-hosted, comparison]
status: stable
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-26T00:00:00Z }
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
  - id: gh-hosted-ref
    resource: https://docs.github.com/en/actions/reference/runners/github-hosted-runners
    title: GitHub-hosted runners reference
---

<p align="center">
  <a href="README.md">📂 <b>GitHub-Hosted vs Self-Hosted Runners</b></a> &nbsp;·&nbsp; Lesson 3 · Part 5 of 8 &nbsp;·&nbsp; ⏱️ 2 min
</p>

# 🚫 Two myths

<details>
<summary><b>"You can't install anything on a GitHub-hosted runner"</b></summary>

<br>

You can. A step can install whatever it needs, and on Linux you even have passwordless `sudo`:

```yaml
- run: sudo apt-get update && sudo apt-get install -y graphviz
```

What you can't do is make it **stick**. The machine is destroyed after the job, so the next run installs it again. That is the price of a clean start, and caching usually makes it cheap.

</details>

<details>
<summary><b>"Self-hosted runners are free"</b></summary>

<br>

You still pay for the machine, its electricity or cloud bill, and the time someone spends looking after it. It's the same iceberg you met in [Chapter 3](../../03-problem-with-traditional-ci-cd-tools/02-hidden-costs-of-self-hosted-ci/08-the-iceberg.md), on a smaller scale.

</details>

> [!NOTE]
> **📘 From the GitHub docs:** Linux and macOS runners use passwordless `sudo`. Windows runners run as administrator with User Account Control (UAC) turned off. So installing extra software works on all three. ([GitHub-hosted runners reference](https://docs.github.com/en/actions/reference/runners/github-hosted-runners))

---

<p align="center">
  <a href="04-side-by-side.md">⬅️ Side by side</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="06-one-security-rule.md"><b>Next: One security rule ➡️</b></a>
</p>
