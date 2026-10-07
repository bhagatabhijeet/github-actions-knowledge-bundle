---
type: Tutorial
title: What is GitHub Actions?
description: The plain-English answer - an automation engine inside your repository that reacts to events and runs your instructions on a fresh machine.
tags: [github-actions, introduction, automation, beginner]
status: stable
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-07T00:00:00Z }
sources:
  - id: gh-understand
    resource: https://docs.github.com/en/actions/get-started/understand-github-actions
    title: Understanding GitHub Actions
  - id: gh-billing
    resource: https://docs.github.com/en/billing/concepts/product-billing/github-actions
    title: GitHub Actions billing
---

<p align="center">
  <img src="../assets/images/chapter-01-banner.svg" alt="Chapter 1: Introduction to GitHub Actions" width="100%">
</p>

<p align="center">
  <b>Lesson 1 of 5</b> &nbsp;·&nbsp; ⏱️ 6 min read &nbsp;·&nbsp; 🟢 No experience needed
</p>

# 🤖 What is GitHub Actions?

## 🌧️ It's 4:55 pm on a Friday

You fixed the bug. You're proud of it. All that's left is the ritual:

1. Pull the latest code
2. Install dependencies
3. Run the tests (all 14 minutes of them)
4. Build the release
5. Copy it to the server
6. Tell the team

You skip step 3, because it's Friday. Production goes down at 5:10 pm.

Now picture the other version of that Friday. You push your fix and close the laptop. Somewhere in a data center, a brand-new computer boots up, downloads your code, runs every test, builds the release, and ships it only if everything is green. If something breaks, you get a message before any customer notices.

**That computer, and the instructions it follows, is GitHub Actions.**

## 💡 The one-sentence definition

> [!IMPORTANT]
> **GitHub Actions is an automation engine built into GitHub. When something happens in your repository, it runs the instructions you wrote, on a machine it provides.**

Read that again and notice three parts. They are the whole product:

| | Part | Question it answers | Example |
|---|---|---|---|
| 🔔 | **Something happens** | *When* should work start? | Someone pushes a commit |
| 📜 | **Your instructions** | *What* should be done? | Install, test, build |
| 🖥️ | **A machine** | *Where* does it run? | A fresh Ubuntu VM |

Everything else in this guide is detail layered on top of those three ideas.

## 🍳 An analogy that sticks

Think of a restaurant kitchen.

| Kitchen | GitHub Actions |
|---|---|
| 🛎️ An order arrives | An **event** fires (a push, a pull request, a timer) |
| 📖 The recipe card | A **workflow** file you wrote in YAML |
| 👩‍🍳 A cook at a clean station | A **runner**: a fresh virtual machine |
| 🔪 Chop, sear, plate | **Steps**, performed in order |
| 🧂 A ready-made sauce from the pantry | An **action**: reusable logic someone already packaged |

The cook doesn't improvise and doesn't get tired. They follow the card exactly, every time, at 3 am on a Sunday if that's when the order comes in.

## 🎁 What can it actually do?

Most people meet GitHub Actions through CI/CD (testing and shipping code), and [Chapter 2](../02-basics-of-ci-cd/01-what-is-ci-cd.md) is devoted to it. But it is a general-purpose automation tool. If it can be scripted, it can be an Actions workflow.

| | You want to... | Triggered by |
|---|---|---|
| 🧪 | Run tests on every pull request | `pull_request` |
| 🚀 | Deploy the site when `main` changes | `push` |
| 📦 | Publish a package when you cut a release | `release` |
| 🏷️ | Label and triage new issues | `issues` |
| 🌙 | Run a nightly security scan | `schedule` |
| 🔘 | Give teammates a "Deploy" button | `workflow_dispatch` |
| 👋 | Welcome first-time contributors | `pull_request_target` |

## 🧭 Where it lives

There is nothing to install and no server to rent. Two places matter:

```text
your-repo/
├── .github/
│   └── workflows/        👈 your instructions live here, as .yml files
│       └── ci.yml
├── src/
└── README.md
```

and the **Actions** tab at the top of every repository on GitHub, where you watch runs happen live.

> [!TIP]
> Because workflows are just files in your repo, they get everything code gets: version history, code review, branches, and blame. Your automation is no longer a mystery living on one person's laptop.

## 💸 What does it cost?

| Repository | Standard GitHub-hosted runners |
|---|---|
| 🌍 **Public** | Free |
| 🔒 **Private** | A monthly allowance of free minutes (2,000 on the Free plan), then pay per minute |

Billing details change over time, so treat the [official billing page](https://docs.github.com/en/billing/concepts/product-billing/github-actions) as the source of truth. For following this guide in a public repository, you will pay nothing.

## 🆚 Why not just use a script?

A fair question. You could run `./deploy.sh` yourself. Here is what you'd be giving up:

| | A script on your laptop | GitHub Actions |
|---|---|---|
| Runs when you forget? | ❌ | ✅ |
| Clean machine every time? | ❌ "works on my machine" | ✅ |
| Visible to the whole team? | ❌ | ✅ |
| Blocks a bad merge? | ❌ | ✅ |
| Runs on Linux, Windows and macOS? | ❌ | ✅ |

The script is still valuable. GitHub Actions is what runs it reliably.

## ✅ Checkpoint

<details>
<summary><b>What are the three parts of the one-sentence definition?</b></summary>

<br>

An **event** (when), a **workflow** of instructions (what), and a **runner** machine (where).

</details>

<details>
<summary><b>Where do workflow files go?</b></summary>

<br>

In the `.github/workflows/` folder of your repository, as `.yml` or `.yaml` files.

</details>

<details>
<summary><b>True or false: GitHub Actions is only for testing code.</b></summary>

<br>

False. CI/CD is the most common use, but any event on GitHub (issues, releases, schedules, a manual button) can drive any scriptable task.

</details>

## 🎯 What you learned

- GitHub Actions reacts to **events** by running **your instructions** on **a machine it provides**
- Workflows are YAML files in `.github/workflows/`
- It's free for public repositories on standard runners
- It beats a local script because it is automatic, clean, visible and repeatable

---

<p align="center">
  <a href="../README.md">🏠 Home</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="index.md">📚 Chapter 1</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="02-core-concepts.md"><b>Next: The Six Core Concepts ➡️</b></a>
</p>
