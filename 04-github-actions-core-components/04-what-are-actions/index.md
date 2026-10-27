# What Are Actions?

* [Overview](README.md) - The reusable building blocks of GitHub Actions - what an action is, how to read a uses line, the three kinds of action, where to find them in the Marketplace, and how to pin them safely.
* [The one-sentence definition](01-the-one-sentence-definition.md) - An action is a reusable, packaged step. Someone writes it once, versions it, and anyone can call it with a single uses: line.
* [Reading a `uses:` line](02-reading-a-uses-line.md) - Actions can also hand outputs back, which later steps read through steps.<id>.outputs.<name>.
* [Action vs command: the two kinds of step](03-action-vs-command-the-two-kinds-of.md) - Every step does exactly one of two things:
* [The three kinds of action](04-the-three-kinds-of-action.md) - Every action, whatever its kind, has a metadata file called action.yml at its root. It declares the name, inputs, outputs and how to run it. Here's a tiny composite action:
* [Where actions come from](05-where-actions-come-from.md) - The GitHub Marketplace lists tens of thousands of actions. A few you will meet almost everywhere:
* [Pinning: which version should you use?](06-pinning-which-version-should-you-use.md) - An action is someone else's code running with your repository's token and secrets. The version you pin decides how much you trust them.
* [Checkpoint](07-checkpoint.md) - The owner is docker, the repository is login-action and the version is v3, a major tag.
