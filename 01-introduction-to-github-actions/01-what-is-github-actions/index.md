# What is GitHub Actions?

* [Overview](README.md) - The plain-English answer - an automation engine inside your repository that reacts to events and runs your instructions on a fresh machine.
* [It's 4:55 pm on a Friday](01-it-s-4-55-pm-on-a.md) - A Friday-afternoon story of a manual release going wrong, showing the problem GitHub Actions exists to solve.
* [The one-sentence definition](02-the-one-sentence-definition.md) - GitHub Actions is an automation engine built into GitHub. When something happens in your repository, it runs the instructions you wrote, on a machine it provides.
* [An analogy that sticks](03-an-analogy-that-sticks.md) - A restaurant-kitchen analogy that maps orders, recipe cards, cooks, cooking steps and ready-made sauces onto events, workflows, runners, steps and actions.
* [What can it actually do?](04-what-can-it-actually-do.md) - Most people meet GitHub Actions through CI/CD (testing and shipping code), and Chapter 2 is devoted to it. But it is a general-purpose automation tool. If it can be scripted, it can be an Actions workflow.
* [Where it lives](05-where-it-lives.md) - Where GitHub Actions lives: workflow files in .github/workflows/ and run history in the repository's Actions tab.
* [What does it cost?](06-what-does-it-cost.md) - What GitHub Actions costs: free on standard runners in public repositories, a monthly minute allowance in private ones, plus the storage and time limits that apply either way.
* [Why not just use a script?](07-why-not-just-use-a-script.md) - Why a workflow beats running ./deploy.sh by hand: it runs when you forget, on a clean machine, visible to the team, and can block a bad merge.
* [Checkpoint](08-checkpoint.md) - Quick self-check on Lesson 1: the event, workflow and runner that make up every GitHub Actions run.
