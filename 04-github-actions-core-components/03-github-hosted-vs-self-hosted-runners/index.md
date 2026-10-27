# GitHub-Hosted vs Self-Hosted Runners

* [Overview](README.md) - The two kinds of runner compared - who maintains them, what state they keep, how far you can customise them, what they cost - plus two common myths and a guide to choosing.
* [The difference in one picture](01-the-difference-in-one-picture.md) - In the workflow file, the whole decision is one line:
* [GitHub-hosted runners](02-github-hosted-runners.md) - GitHub owns the machine, starts it for your job and throws it away afterwards.
* [Self-hosted runners](03-self-hosted-runners.md) - You install GitHub's small runner application on a machine you control: a server, a VM, a cloud instance, even a laptop. It connects to GitHub and waits for jobs.
* [Side by side](04-side-by-side.md) - Cost details change. The billing page is the source of truth.
* [Two myths](05-two-myths.md) - You can. A step can install whatever it needs, and on Linux you even have passwordless sudo:
* [One security rule](06-one-security-rule.md) - Be very careful with self-hosted runners on public repositories. Anyone can open a pull request against a public repository. If that pull request's workflow runs on your machine, a stranger's code is executing inside...
* [Which should you choose?](07-which-should-you-choose.md) - Start hosted. Nearly every project can. Move a job to a self-hosted runner only when you can name the specific thing it needs. You can also mix them: most jobs hosted, one deploy job self-hosted.
* [Checkpoint](08-checkpoint.md) - runs-on. A GitHub label such as ubuntu-latest requests a hosted runner. self-hosted, or a label you defined, sends the job to your own machine.
