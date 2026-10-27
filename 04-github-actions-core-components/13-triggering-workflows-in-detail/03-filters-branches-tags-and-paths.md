---
type: Tutorial
title: "Triggering Workflows in Detail: Filters: branches, tags and paths"
description: "Activity types say what happened. Filters say where. They are how you stop the README typo from starting a full build."
tags: [github-actions, triggers, events, on, workflow_dispatch, schedule, cron, repository_dispatch, workflow_run, filters, hands-on]
status: stable
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-26T00:00:00Z }
sources:
  - id: gh-workflows-concepts
    resource: https://docs.github.com/en/actions/concepts/workflows-and-actions/workflows#workflow-triggers
    title: Workflows - Workflow triggers
  - id: gh-events
    resource: https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows
    title: Events that trigger workflows
  - id: gh-workflow-syntax
    resource: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
    title: Workflow syntax for GitHub Actions
---

<p align="center">
  <a href="README.md">📂 <b>Triggering Workflows in Detail</b></a> &nbsp;·&nbsp; Lesson 13 · Part 3 of 12 &nbsp;·&nbsp; ⏱️ 3 min
</p>

# 🎯 Filters: branches, tags and paths

Activity types say *what happened*. Filters say *where*. They are how you stop the README typo from starting a full build.

```yaml
on:
  push:
    branches:
      - main
      - 'release/**'          # release/1.0, release/2024/q1 ...
    tags:
      - 'v*'                  # v1, v1.2.3
    paths:
      - 'src/**'
      - 'package.json'
      - '!src/**/*.md'        # ...but not Markdown inside src
  pull_request:
    branches: [main]          # the PR's TARGET branch, not its source
```

| Filter | Runs when... | Opposite |
|---|---|---|
| `branches:` | the branch matches a pattern | `branches-ignore:` |
| `tags:` | the tag matches a pattern | `tags-ignore:` |
| `paths:` | **at least one** changed file matches | `paths-ignore:` |

**The rules that bite:**

- **One or the other.** You can't use `branches` and `branches-ignore` for the same event (or `paths` with `paths-ignore`). To exclude inside an include list, use `!` as above. Order matters: a later pattern overrides an earlier one.
- **Filters combine with AND.** With both `branches:` and `paths:`, a push must match **both**.
- **`branches` alone means "not on tags".** If you set only `branches:`, tag pushes don't run the workflow, and the reverse is also true. Add both if you want both.
- **Patterns are globs.** `*` matches anything except `/`, and `**` matches anything including `/`. Quote patterns that start with `*` or `!`, because YAML treats those characters specially.
- **Diffs over 300 files** may not be fully checked by `paths:`. If no match is found in the first 300 files, the workflow doesn't run.
- **Tag pushes in bulk** don't create events. The docs say tag events aren't created when more than **three tags** are pushed at once.

> [!TIP]
> Every pushed commit can opt out on its own. Put **`[skip ci]`**, `[ci skip]`, `[no ci]`, `[skip actions]` or `[actions skip]` in the commit message, and `push` and `pull_request` workflows won't run for it.

---

<p align="center">
  <a href="02-repository-events-and-activity-types.md">⬅️ Repository events and activity types</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="04-manual-runs-with-workflow-dispatch.md"><b>Next: Manual runs with `workflow_dispatch` ➡️</b></a>
</p>
