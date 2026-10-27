# Working with Repository-Level Secrets

* [Overview](README.md) - Get passwords and tokens out of your workflow files - what a secret is and how GitHub protects it, creating repository secrets in Settings or with gh, using them safely in run steps and actions, log masking and its limits, forks, GITHUB_TOKEN, and what to do when a secret leaks.
* [What a secret is](01-what-a-secret-is.md) - A secret is a variable that GitHub encrypts, never shows again, and hides from the logs. You read it in a workflow with ${{ secrets.NAME }}.
* [Creating a repository secret, step by step](02-creating-a-repository-secret-step-by-step.md) - Secrets and variables can live at three levels: organisation, repository and environment. This lesson uses the repository level: one place, usable by every workflow in the repo.
* [Using it: fixing the Docker login](03-using-it-fixing-the-docker-login.md) - Pass the Docker password from secrets into the login step through env: and stdin, so it never appears in the command line or the YAML.
* [Log masking: what it catches, and what it misses](04-log-masking-what-it-catches-and-what.md) - Masking hides only the exact secret value; encoded, partial or derived copies leak unless you register them with ::add-mask::.
* [Rules that catch people out](05-rules-that-catch-people-out.md) - Nine secret rules that surprise people: no secrets in if:, empty when missing, none for forks or Dependabot, no automatic sharing, naming rules and size limits.
* [The secret you get for free: `GITHUB_TOKEN`](06-the-secret-you-get-for-free-github.md) - Every run gets an automatic secret, secrets.GITHUBTOKEN. It's a short-lived token for this repository, created when the job starts and expired when it ends. Actions such as actions/checkout use it by default.
* [Repository, environment or organisation?](07-repository-environment-or-organisation.md) - This lesson uses repository secrets. There are two more levels, and the most specific wins when names clash:
* [If a secret leaks](08-if-a-secret-leaks.md) - Let GitHub watch for you. Secret scanning with push protection (Settings → Code security) blocks pushes that contain known token formats, before they reach the repository. It's free for public repositories.
* [Try it yourself](09-try-it-yourself.md) - This repository ships a workflow that's safe to run with or without any secrets: 04-secrets.yml.
* [Checkpoint](10-checkpoint.md) - You can't. Secrets are write-only. Get the value from its source, or create a new one and update the secret.
