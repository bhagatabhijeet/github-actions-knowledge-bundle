---
type: Tutorial
title: How GitHub Actions Answers the Problem
description: The install list and the six pains checked against GitHub Actions line by line - hosted runners, fresh machines, actions instead of plugins - with the honest trade-offs and when a traditional tool is still the right call.
tags: [github-actions, ci-cd, hosted-runners, self-hosted-runners, jenkins, comparison, migration]
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
  - id: gh-migrate-jenkins
    resource: https://docs.github.com/en/actions/tutorials/migrate-to-github-actions/manual-migrations/migrate-from-jenkins
    title: Migrating from Jenkins to GitHub Actions
  - id: gh-secure-use
    resource: https://docs.github.com/en/actions/reference/security/secure-use
    title: Secure use reference
  - id: gh-billing
    resource: https://docs.github.com/en/billing/concepts/product-billing/github-actions
    title: GitHub Actions billing
---

<p align="center">
  <b>Lesson 3 of 4</b> &nbsp;·&nbsp; ⏱️ 9 min read &nbsp;·&nbsp; 🟢 Beginner
</p>

# 🛟 How GitHub Actions Answers the Problem

[Lesson 1](01-the-problem-statement.md) ended with Abhijeet choosing GitHub Actions. [Lesson 2](02-hidden-costs-of-self-hosted-ci.md) listed the six pains he avoided. They share one root: **you were running a tool**. GitHub Actions changes the deal. You stop running a tool and start using a service.

## 🎯 The shift in one picture

<p align="center">
  <img src="../assets/images/who-maintains-what.svg" alt="With a self-hosted CI server you maintain all seven layers, from machines up to the pipeline definition. With GitHub Actions on hosted runners you maintain only the pipeline definition" width="100%">
</p>

On the left, every layer is yours. On the right, you keep the one layer that is actually about your product: **the pipeline definition**. That is the workflow file you learned to read in [Chapter 1](../01-introduction-to-github-actions/03-anatomy-of-a-workflow.md).

## 🧾 Abhijeet's install list, revisited

Here are the seven tasks from [Lesson 1](01-the-problem-statement.md), and what becomes of each.

| | With a self-hosted CI server | With GitHub Actions |
|---|---|---|
| 1 | Provision and maintain a virtual machine | `runs-on: ubuntu-latest`. GitHub provides the machine |
| 2 | Install Java, firewall rules, CI plugins | Nothing. There is no server |
| 3 | Install Node.js and npm | `actions/setup-node` picks the version in one step |
| 4 | Keep several Node.js versions side by side | A **matrix**: each version gets its own clean machine |
| 5 | Install Docker | Already on the Ubuntu runner |
| 6 | Install kubectl and Helm | Already on the Ubuntu runner |
| 7 | Install CLIs for test and reporting tools | An action or an install step, in the workflow that needs it |

Task 4, the one that causes version conflicts on a shared machine, becomes a few lines of YAML:

```yaml
jobs:
  unit-testing:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        node-version: [20, 22, 24]
    steps:
      - uses: actions/checkout@v7
      - uses: actions/setup-node@v7
        with:
          node-version: ${{ matrix.node-version }}
      - run: npm ci
      - run: npm test
```

Three versions, three separate machines, running at the same time. They can't conflict because they never share a disk.

The "and it grows" list shrinks the same way:

| | Later need | On a GitHub-hosted Ubuntu runner |
|---|---|---|
| ☕ | Java and Maven | Preinstalled. `actions/setup-java` selects a specific version |
| 🐍 | Python | Preinstalled. `actions/setup-python` selects a specific version |
| ☁️ | AWS CLI and Azure CLI | Preinstalled |
| 🛡️ | Trivy, kubesec | Not preinstalled. Add an action or an install step where you need them |

> [!NOTE]
> The preinstalled list changes over time. The exact contents of every runner image are published in the [actions/runner-images](https://github.com/actions/runner-images) repository.

**Against his two criteria:**

| | Criterion | Verdict |
|---|---|---|
| 1️⃣ | Simple to set up, nothing to install | ✅ Commit a YAML file and it runs |
| 2️⃣ | Pipelines, not infrastructure or scale | ✅ GitHub provisions and scales the runners |

## ✅ Six pains, six answers

And the day-two pains from [Lesson 2](02-hidden-costs-of-self-hosted-ci.md):

| | Pain | GitHub Actions gives you | Meet it in |
|---|---|---|---|
| 1️⃣ | Server upkeep | No server. GitHub runs the service and maintains the runner images | [1.1](../01-introduction-to-github-actions/01-what-is-github-actions.md) |
| 2️⃣ | Snowflake agents | A **fresh virtual machine per job**, thrown away afterwards. Tool versions are declared in the workflow | [2.5](../02-basics-of-ci-cd/05-your-first-ci-pipeline.md) |
| 3️⃣ | Queues and idle cost | Each job gets its own **GitHub-hosted runner**, billed **per minute**. Free on public repositories with standard runners | [1.2](../01-introduction-to-github-actions/02-core-concepts.md) |
| 4️⃣ | Fragile plugins | **Actions** are chosen per workflow and per version, not installed server-wide | [1.3](../01-introduction-to-github-actions/03-anatomy-of-a-workflow.md) |
| 5️⃣ | Integration glue | Code and CI live in the same place. No webhook, no clone token, no second set of accounts | [1.1](../01-introduction-to-github-actions/01-what-is-github-actions.md#-where-it-lives) |
| 6️⃣ | Knowledge in one head | Workflows are **YAML files in `.github/workflows/`**, reviewed in pull requests | [1.3](../01-introduction-to-github-actions/03-anatomy-of-a-workflow.md) |

## 🧩 Plugins vs actions

This one deserves a closer look, because actions and plugins sound like the same idea.

| | 🧩 Server plugin | ⚡ Action |
|---|---|---|
| **Installed** | Once, into the server, by an admin | Never. You reference it in a step |
| **Scope** | Every pipeline on the server | Only the workflow that names it |
| **Version** | One version for everybody | Each workflow picks its own |
| **Upgrading** | Can break other teams' pipelines | Affects only the file you edit |
| **Runs** | Inside the CI server | On the throwaway runner |

```yaml
steps:
  - uses: actions/checkout@v7        # this workflow's choice
  - uses: actions/setup-python@v7    # change it here, nothing else moves
```

The upgrade trap from Lesson 2 can't happen. There is no server to upgrade, and bumping an action in one workflow leaves every other workflow untouched.

## 🔍 Same pipeline, two worlds

Tessaloop's Node.js project isn't in this repository, but a small Python [sample app](../sample-app/) is. Here is a lint-and-test pipeline for it, written for Jenkins:

```groovy
pipeline {
    agent { label 'linux-python' }
    stages {
        stage('Lint') {
            steps {
                sh 'python -m pip install -r requirements-dev.txt'
                sh 'ruff check .'
            }
        }
        stage('Test') {
            steps {
                sh 'python -m unittest discover -v'
            }
        }
    }
}
```

And the same thing as a GitHub Actions workflow:

```yaml
name: CI
on: [push, pull_request]

jobs:
  lint-and-test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v7
      - uses: actions/setup-python@v7
        with:
          python-version: '3.13'
      - run: python -m pip install -r requirements-dev.txt
      - run: ruff check .
      - run: python -m unittest discover -v
```

The two files are about the same length, and that is the point. **The difference isn't in the file. It's in what has to exist before the file can run.**

| | Before the Jenkinsfile runs | Before the workflow runs |
|---|---|---|
| 🧠 | A CI server, installed and reachable | Nothing |
| 💪 | An agent labelled `linux-python`, with the right Python on it | Nothing: `runs-on` requests a machine, `setup-python` picks the version |
| 🧩 | Pipeline and Git plugins, at compatible versions | Nothing |
| 🔗 | A webhook and a clone credential | Nothing |
| 📄 | The file, committed | The file, committed |

Notice the line `agent { label 'linux-python' }`. It doesn't describe a machine. It **points at one that somebody built by hand**. The workflow's `python-version: '3.13'` describes what it needs, and gets it on a clean machine every time.

## 🧾 What is still your job

GitHub Actions doesn't remove responsibility. It moves the line.

| | Still yours | Why |
|---|---|---|
| 📜 | Writing and maintaining workflows | That's the pipeline definition: the layer you kept |
| ⬆️ | Keeping action versions current | Old versions stop getting fixes |
| 🔑 | Managing secrets | Deploy credentials are as sensitive as ever |
| 🛡️ | Vetting third-party actions | An action is someone else's code running with access to your repository |
| 💰 | Watching minutes on private repositories | Pay-per-use means a wasteful pipeline costs money |

> [!WARNING]
> Actions from the Marketplace are written by many different authors, just like plugins. Prefer well-maintained ones, read what they do, and for anything sensitive pin the action to a full commit SHA so the code can't change underneath you.

## ⚖️ The honest trade-offs

A fair comparison has two columns. Here is what you give up.

| | Trade-off | What it means |
|---|---|---|
| 🔒 | **Tied to GitHub** | Workflow syntax is specific to GitHub. Moving to another platform means rewriting pipelines |
| 🌐 | **Hosted runners live on the public internet** | They can't reach a database or server inside your private network without extra setup |
| 🔧 | **Less control over the machine** | You pick from the runner sizes and images GitHub offers |
| ⏱️ | **Job time limit** | A job on a GitHub-hosted runner is stopped after 6 hours |
| 💰 | **Cost at very high volume** | Per-minute pricing can exceed the cost of your own machines if you build constantly |
| 🚨 | **Someone else's outage** | If the service has an incident, you wait. You can't log in and fix it |

## 🌉 The middle path: self-hosted runners

GitHub Actions also lets you bring your own machines, called **self-hosted runners**. GitHub still does the scheduling, the UI and the logs. Your machine does the running.

```mermaid
flowchart LR
    W[📜 Workflow]:::blue --> Q{runs-on}:::yellow
    Q -- ubuntu-latest --> H[☁️ GitHub-hosted runner<br/>fresh VM, nothing to maintain]:::green
    Q -- self-hosted --> S[🏢 Your machine<br/>your network, your upkeep]:::orange

    classDef blue fill:#0c1d3a,stroke:#58a6ff,color:#fff,stroke-width:2px
    classDef yellow fill:#3d2a00,stroke:#e3b341,color:#fff,stroke-width:2px
    classDef green fill:#0f2d17,stroke:#3fb950,color:#fff,stroke-width:2px
    classDef orange fill:#3d1d00,stroke:#ffa657,color:#fff,stroke-width:2px
```

They solve the private-network and special-hardware problems. They also bring back pains 1 to 3 from Lesson 2 for those machines: you patch them, you keep them clean and you decide how many to run.

> [!TIP]
> Start with GitHub-hosted runners. Reach for self-hosted ones only when you hit a specific wall, such as needing a GPU or access to an internal system.

## 🧭 So which should you use?

```mermaid
flowchart TD
    Q1{Is your code on GitHub?}:::yellow
    Q1 -- No --> A1[🧰 Use the CI built into your code host,<br/>or a traditional tool]:::orange
    Q1 -- Yes --> Q2{Do builds need your private<br/>network or special hardware?}:::yellow
    Q2 -- No --> A2[☁️ GitHub Actions<br/>with hosted runners]:::green
    Q2 -- Yes --> Q3{Do you have people to<br/>look after build machines?}:::yellow
    Q3 -- Yes --> A3[🏢 GitHub Actions with<br/>self-hosted runners]:::blue
    Q3 -- No --> A4[🤔 Solve the access problem first,<br/>then use hosted runners]:::orange

    classDef yellow fill:#3d2a00,stroke:#e3b341,color:#fff,stroke-width:2px
    classDef green fill:#0f2d17,stroke:#3fb950,color:#fff,stroke-width:2px
    classDef blue fill:#0c1d3a,stroke:#58a6ff,color:#fff,stroke-width:2px
    classDef orange fill:#3d1d00,stroke:#ffa657,color:#fff,stroke-width:2px
```

A traditional tool is still a sound choice when you have a platform team, strict rules about where builds may run, or years of working pipelines that nobody needs to change.

## 🚚 Already on a traditional tool?

You don't have to move everything at once. Most teams start new projects on GitHub Actions and migrate old pipelines one at a time. GitHub publishes a [migration guide for Jenkins](https://docs.github.com/en/actions/tutorials/migrate-to-github-actions/manual-migrations/migrate-from-jenkins) that maps each concept across:

| Jenkins | GitHub Actions |
|---|---|
| `Jenkinsfile` | Workflow file in `.github/workflows/` |
| `agent` | `runs-on` |
| `stage` | Job |
| `steps` | `steps` |
| Plugin | Action |
| Credentials | Secrets |

## ✅ Checkpoint

<details>
<summary><b>The Jenkinsfile and the workflow were about the same length. So where is the saving?</b></summary>

<br>

In everything that must exist before the file runs. The Jenkinsfile needs a server, a prepared agent, plugins, a webhook and a credential. The workflow needs only to be committed.

</details>

<details>
<summary><b>Why can't upgrading an action break another team's pipeline the way upgrading a plugin can?</b></summary>

<br>

A plugin is installed once for the whole server. An action is referenced, with its version, inside a single workflow file. Changing it there changes nothing anywhere else.

</details>

<details>
<summary><b>Name two things that are still your responsibility on GitHub Actions.</b></summary>

<br>

Any two of: writing and maintaining workflows, keeping action versions current, managing secrets, vetting third-party actions, and watching minute usage on private repositories.

</details>

<details>
<summary><b>Your tests must talk to a database inside the company network. What are you likely to need?</b></summary>

<br>

A self-hosted runner inside that network, or another way of giving hosted runners access. Standard GitHub-hosted runners can't reach private systems on their own.

</details>

## 🎯 What you learned

- GitHub Actions swaps **running a tool** for **using a service**: you keep only the pipeline definition
- Abhijeet's seven-task install list collapses into **`runs-on`, a setup action and a matrix**
- Hosted runners answer the queue, snowflake and upkeep problems with a **fresh machine per job**
- **Actions** are versioned per workflow, so upgrades are local and safe
- You still own workflows, secrets, action hygiene and cost
- The trade-offs are real: **GitHub lock-in, no private-network access by default, less machine control**
- **Self-hosted runners** are the middle path, and they bring some upkeep back

---

<p align="center">
  <a href="02-hidden-costs-of-self-hosted-ci.md">⬅️ The Hidden Costs</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="index.md">📚 Chapter 3</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="04-cheat-sheet-and-quiz.md"><b>Next: Cheat Sheet & Quiz ➡️</b></a>
</p>
