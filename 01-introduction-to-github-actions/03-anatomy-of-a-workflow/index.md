# Anatomy of a Workflow File

* [Overview](README.md) - A line-by-line tour of workflow YAML - name, on, jobs, runs-on and steps - plus the YAML rules that trip up every beginner.
* [The skeleton](01-the-skeleton.md) - The four questions every workflow answers (name, when, where, what) and the minimal YAML skeleton that answers them.
* [The nesting map](02-the-nesting-map.md) - Indentation in YAML is the structure. This is the shape hiding inside every workflow:
* [Key by key](03-key-by-key.md) - Each top-level workflow key explained with a small example: name and run-name, on, jobs, runs-on and steps, including the naming rules GitHub enforces.
* [Two extras you'll see everywhere](04-two-extras-you-ll-see-everywhere.md) - The ${{ }} expression syntax with the github context, how to avoid script injection, and limiting the GITHUB_TOKEN with permissions.
* [The five YAML traps](05-the-five-yaml-traps.md) - Nine out of ten "my workflow won't start" problems are one of these.
* [Read it aloud](06-read-it-aloud.md) - Here's a real workflow. Before opening the answer, try saying what it does in plain English.
