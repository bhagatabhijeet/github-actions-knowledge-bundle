# Anatomy of a Workflow File

* [Overview](README.md) - A line-by-line tour of workflow YAML - name, on, jobs, runs-on and steps - plus the YAML rules that trip up every beginner.
* [The skeleton](01-the-skeleton.md) - Every workflow answers four questions:
* [The nesting map](02-the-nesting-map.md) - Indentation in YAML is the structure. This is the shape hiding inside every workflow:
* [Key by key](03-key-by-key.md) - The label shown in the Actions tab. Optional, but without it GitHub shows the file path, and nobody wants to read .github/workflows/ci.yml forty times.
* [Two extras you'll see everywhere](04-two-extras-you-ll-see-everywhere.md) - Double curly braces ask GitHub to fill in a value before the step runs.
* [The five YAML traps](05-the-five-yaml-traps.md) - Nine out of ten "my workflow won't start" problems are one of these.
* [Read it aloud](06-read-it-aloud.md) - Here's a real workflow. Before opening the answer, try saying what it does in plain English.
