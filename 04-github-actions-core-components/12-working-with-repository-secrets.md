---
type: Tutorial
title: Working with Repository-Level Secrets (Hands-On)
description: Get passwords and tokens out of your workflow files - what a secret is and how GitHub protects it, creating repository secrets in Settings or with gh, using them safely in run steps and actions, log masking and its limits, forks, GITHUB_TOKEN, and what to do when a secret leaks.
tags: [github-actions, secrets, security, masking, github-token, docker, hands-on]
status: stable
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-26T00:00:00Z }
sources:
  - id: gh-secrets
    resource: https://docs.github.com/en/actions/concepts/security/secrets
    title: Secrets
  - id: gh-use-secrets
    resource: https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/use-secrets
    title: Using secrets in GitHub Actions
  - id: gh-secure-use
    resource: https://docs.github.com/en/actions/reference/security/secure-use
    title: Secure use reference
  - id: gh-secret-set
    resource: https://cli.github.com/manual/gh_secret_set
    title: gh secret set
  - id: docker-login-action
    resource: https://github.com/docker/login-action
    title: docker/login-action
---

<p align="center">
  <b>Lesson 12 of 13</b> &nbsp;·&nbsp; ⏱️ 22 min &nbsp;·&nbsp; 🛠️ Hands-on &nbsp;·&nbsp; 🔐 Security essential
</p>

# 🔐 Working with Repository-Level Secrets

In [Lesson 11](11-working-with-variables.md) we cleaned up a Docker workflow with variables, and left one problem on purpose:

```yaml
    - name: Docker Login
      run: docker login --username=dockerUsername --password=s3cUrePaSsw0rd   # 🚨
```

That password is now readable by everyone who can see the repository, in every fork and clone, and in the Git history forever. **Secrets** exist so this never happens. This lesson fixes the line properly, and shows exactly what secrets protect you from, and what they don't.

## 💡 What a secret is

> **A secret is a variable that GitHub encrypts, never shows again, and hides from the logs.** You read it in a workflow with `${{ secrets.NAME }}`.

<p align="center">
  <img src="../assets/images/secret-journey.svg" alt="You type a secret in Settings; it is encrypted on your machine with the repository's public key, stored encrypted by GitHub where nobody can read it back, and decrypted only on the runner for the job, where it is masked as three asterisks in logs. It is protected from people reading code, Settings or logs and from fork pull requests, but not from changed copies, workflows that send it elsewhere, third-party actions, files and artifacts, or people with write access" width="100%">
</p>

| Stage | What happens |
|---|---|
| ⌨️ **You save it** | In **Settings** or with `gh secret set` |
| 🔒 **Encrypted before upload** | Your browser or the CLI seals it with the repository's public key ([libsodium sealed box](https://libsodium.gitbook.io/doc/public-key_cryptography/sealed_boxes)), so it never travels in plain text |
| 🗄️ **Stored write-only** | Settings shows the name and when it was updated, never the value. You can **update** or **delete** it, not read it |
| 🖥️ **Decrypted for the job** | Only when a job runs, and only reaches the steps you pass it to |
| 🙈 **Masked in logs** | If the exact value appears in a log, GitHub prints `***` instead |

## 🛠️ Creating a repository secret

### In the browser

1. Open the repository → **Settings**
2. **Secrets and variables** → **Actions**
3. The **Secrets** tab → **New repository secret**
4. **Name:** `DOCKER_PASSWORD` · **Secret:** paste the value → **Add secret**

### With the GitHub CLI

```bash
gh secret set DOCKER_PASSWORD                      # prompts, input hidden ✅
gh secret set DOCKER_PASSWORD < token.txt          # from a file
gh secret set KUBECONFIG < ~/.kube/config          # whole files work too
gh secret list                                     # names and dates only
gh secret delete DOCKER_PASSWORD
```

> [!WARNING]
> **Avoid `gh secret set NAME --body "value"`.** The value lands in your shell history. Let it prompt you, or read from a file.

### Naming rules

| Rule | ✅ OK | ❌ Not OK |
|---|---|---|
| Letters, digits and `_` only | `DOCKER_PASSWORD` | `docker-password` |
| Can't start with a digit | `AWS_KEY_2` | `2FA_SECRET` |
| Can't start with `GITHUB_` | `GH_DEPLOY_TOKEN` | `GITHUB_DEPLOY_TOKEN` |
| Not case-sensitive | `Docker_Password` and `DOCKER_PASSWORD` are the same secret | |

> [!TIP]
> **Store a token, not your password.** For Docker Hub, create a **personal access token** with only the permissions the workflow needs (Account settings → Personal access tokens) and store that. You can revoke it without changing your password, and it can do less damage if it leaks.

## ✅ Using it: fixing the Docker login

### Option A: in a `run:` step

```yaml
    - name: Docker Login
      env:
        DOCKER_PASSWORD: ${{ secrets.DOCKER_PASSWORD }}     # 1️⃣ map the secret to an env var
      run: echo "$DOCKER_PASSWORD" | docker login --username "$DOCKER_USERNAME" --password-stdin   # 2️⃣ read it from stdin
```

Two details make this safe:

| | Detail | Why |
|---|---|---|
| 1️⃣ | Pass the secret through **`env:`**, read it as `$DOCKER_PASSWORD` | `${{ secrets.X }}` written directly in `run:` is pasted into the script text before it runs, where special characters can break the command |
| 2️⃣ | Use **`--password-stdin`**, not `--password=` | A value on the command line can show up in process lists, and Docker warns about it |

### Option B: with an action

```yaml
    - name: Docker Login
      uses: docker/login-action@v4
      with:
        username: ${{ vars.DOCKER_USERNAME }}
        password: ${{ secrets.DOCKER_PASSWORD }}
```

The action handles stdin and logs out at the end of the job for you.

### The whole workflow, fixed

```yaml
name: Exploring Variables and Secrets

on: push

env:
  CONTAINER_REGISTRY: docker.io
  DOCKER_USERNAME: ${{ vars.DOCKER_USERNAME }}     # ⚙️ variable: not sensitive
  IMAGE_NAME: imageName

jobs:
  docker:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v7

      - name: Docker Login
        uses: docker/login-action@v4
        with:
          username: ${{ vars.DOCKER_USERNAME }}
          password: ${{ secrets.DOCKER_PASSWORD }}  # 🔐 secret: sensitive

      - name: Docker Build
        run: docker build -t $CONTAINER_REGISTRY/$DOCKER_USERNAME/$IMAGE_NAME:${{ github.sha }} .

      - name: Docker Publish
        run: docker push $CONTAINER_REGISTRY/$DOCKER_USERNAME/$IMAGE_NAME:${{ github.sha }}
```

No password anywhere in the file. Rotate it in Settings and the workflow keeps working, with no commit.

## 🙈 Log masking: what it catches, and what it misses

GitHub scans the logs for the **exact** secret value and replaces it with `***`:

```text
Run echo "The secret is $DEMO_SECRET"
The secret is ***
```

That's a safety net, not a guarantee. It misses **changed copies**:

| You print | Masked? |
|---|---|
| The exact value | ✅ `***` |
| The value base64-encoded | ❌ Readable |
| Part of it (`${SECRET:0:4}`) | ❌ Readable |
| A JSON secret, one field at a time | ❌ Often readable. Store each field as its own secret instead |
| A value you derived, after `echo "::add-mask::$VALUE"` | ✅ `***` |

```yaml
- run: |
    TOKEN_B64=$(printf '%s' "$API_TOKEN" | base64)
    echo "::add-mask::$TOKEN_B64"       # register the derived value for masking first
    echo "Encoded: $TOKEN_B64"          # → Encoded: ***
```

> [!CAUTION]
> **Never print a secret on purpose, even "just to check it".** If you need to know it's set, print its length or test that it's non-empty.

## 🚦 Rules that catch people out

| Rule | What it means | What to do |
|---|---|---|
| 🚫 **No secrets in `if:` directly** | `if: secrets.TOKEN != ''` isn't allowed | Map it to job-level `env:`, then test `env.TOKEN` in a step's `if:`, or map a `!= ''` check as this repo's live workflow does |
| 📭 **Missing secret = empty string** | No error, just an empty value. `docker login` then fails with a confusing message | Check it's set at the start of the job |
| 🍴 **Forks don't get secrets** | Workflows triggered by a `pull_request` **from a fork** run without your secrets (only a read-only `GITHUB_TOKEN`) | Expected: strangers can't steal them by opening a PR. Don't "fix" it with `pull_request_target` and checking out their code |
| 🤖 **Dependabot runs don't get Actions secrets** | Workflows triggered by Dependabot see **Dependabot secrets** instead | Add the ones it needs under **Secrets and variables → Dependabot** |
| 🧩 **Actions don't see secrets automatically** | An action only gets what you pass in `with:` or `env:` | Pass only the secrets each step needs |
| 🔁 **Reusable workflows don't inherit them** | A called workflow gets secrets only if you pass them | `secrets: inherit`, or pass them one by one |
| 📏 **Limits** | Up to 48 KB per secret, 100 secrets per repository | For bigger files, encrypt the file in the repo and store only the key as a secret |

## 🎟️ The secret you get for free: `GITHUB_TOKEN`

Every run gets an automatic secret, `secrets.GITHUB_TOKEN`. It's a short-lived token for **this repository**, created when the job starts and expired when it ends. Actions such as `actions/checkout` use it by default.

Control what it can do with `permissions:`. Start from read-only and add only what a job needs:

```yaml
permissions:
  contents: read            # the whole workflow: read-only by default

jobs:
  release:
    permissions:
      contents: write       # this job alone may create a release
    runs-on: ubuntu-latest
    steps:
      - run: gh release create v1.0.0
        env:
          GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

> [!TIP]
> **Prefer `GITHUB_TOKEN` over a personal access token** for anything inside the same repository. It expires on its own and can't reach your other repositories.

## 🏢 Repository, environment or organisation?

This lesson uses **repository** secrets. There are two more levels, and the most specific wins when names clash:

| Level | Set in | Available to | Precedence |
|---|---|---|---|
| 🏢 Organisation | Org settings | Repositories you choose | Lowest |
| 📁 **Repository** | Repo settings → Secrets and variables → Actions | Every workflow in the repo | Middle |
| 🌍 Environment | Repo settings → Environments → *name* | Jobs with `environment: <name>`, optionally only after a **required reviewer** approves | **Highest** |

Keep production credentials in an **environment** secret behind required reviewers, so no job can use them without someone approving the deployment.

## 🚨 If a secret leaks

| Step | Action |
|---|---|
| 1️⃣ **Revoke or rotate it at the source** | Docker Hub, AWS, npm... This is the only step that actually stops the damage |
| 2️⃣ **Update the GitHub secret** | Settings, or `gh secret set` |
| 3️⃣ **Delete affected logs** | The run's ⋯ menu → **Delete all logs** |
| 4️⃣ **Remove it from the code** | And treat the old commit as public forever. Rewriting history doesn't reach existing clones and forks |
| 5️⃣ **Check for misuse** | The provider's audit or access logs |

> [!TIP]
> **Let GitHub watch for you.** **Secret scanning** with **push protection** (Settings → Code security) blocks pushes that contain known token formats, before they reach the repository. It's free for public repositories.

## 🧪 Try it yourself

This repository ships a workflow that's safe to run with or without any secrets: [`04-secrets.yml`](../.github/workflows/04-secrets.yml).

1. **Actions** → **04 - Secrets** → **Run workflow**. With nothing set, both jobs pass and leave a ℹ️ notice telling you what to add
2. In a fork, add a repository secret **`DEMO_SECRET`** with any harmless value, like `dragon-123`, and run it again
3. Open **Print it (GitHub masks it)**: the log shows `The secret is ***`
4. Open **A changed copy is NOT masked automatically**: the base64 copy is masked only because the step called `::add-mask::` first
5. **Optional:** add a `DOCKER_USERNAME` **variable** and a `DOCKER_PASSWORD` **secret** holding a Docker Hub access token. The **docker-login** job logs in for real
6. Go back to **Settings → Secrets**: try to view `DEMO_SECRET`. You can only update or remove it

## ✅ Checkpoint

<details>
<summary><b>You saved a secret yesterday and forgot what it was. How do you read it back from GitHub?</b></summary>

<br>

You can't. Secrets are write-only. Get the value from its source, or create a new one and update the secret.

</details>

<details>
<summary><b>Why pass a secret through <code>env:</code> instead of writing <code>${{ secrets.X }}</code> inside <code>run:</code>?</b></summary>

<br>

An expression in `run:` is pasted into the script text before it runs, so quotes or special characters in the value can break the command. Through `env:`, the shell receives it as data in `$X`.

</details>

<details>
<summary><b>A step prints a secret base64-encoded. Will the log show <code>***</code>?</b></summary>

<br>

No. Masking only matches the exact value. Register the encoded value with `::add-mask::` first, or better, don't print it at all.

</details>

<details>
<summary><b>A contributor opens a pull request from their fork, and your deploy step fails with an empty password. Bug?</b></summary>

<br>

No, it's protection. Workflows triggered by pull requests from forks don't receive your secrets, so a stranger can't steal them by changing the workflow in their PR.

</details>

<details>
<summary><b>A password was committed and you've deleted the line. Are you safe?</b></summary>

<br>

No. It's still in the Git history and in every clone and fork. Rotate the password at its source first.

</details>

## 🎯 What you learned

- A **secret** is encrypted before upload, **write-only** in Settings, decrypted only for the job, and **masked** in logs
- Create one in **Settings → Secrets and variables → Actions**, or with **`gh secret set`** (let it prompt)
- Read it as **`${{ secrets.NAME }}`**; in `run:`, pass it through **`env:`** and use stdin, like `--password-stdin`
- Masking only catches the **exact** value; register derived values with **`::add-mask::`**, and never print secrets
- **Forks** and **Dependabot** runs don't get your Actions secrets; actions only get what you pass them
- **`GITHUB_TOKEN`** is a free, short-lived secret; limit it with **`permissions:`**
- If a secret leaks, **rotate it at the source first**

---

<p align="center">
  <a href="11-working-with-variables.md">⬅️ Variables</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="index.md">📚 Chapter 4</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="13-cheat-sheet-and-quiz.md"><b>Next: Cheat Sheet & Quiz ➡️</b></a>
</p>
