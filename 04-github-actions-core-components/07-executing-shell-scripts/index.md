# Executing Shell Scripts in a Workflow

* [Overview](README.md) - Move a workflow's commands into a shell script in the repository and run it in one step - the shebang, set -euo pipefail, the executable bit, LF line endings, passing arguments, and the errors you'll meet on the way.
* [Where we left off](01-where-we-left-off.md) - Six steps, each a single command. It works, and the log is easy to follow. But the logic lives only in YAML.
* [Move the commands into a script](02-move-the-commands-into-a-script.md) - 1. Write the script at scripts/ascii-script.sh:
* [Watching the script run](03-watching-the-script-run.md) - Push the change and open the run. Here's a run whose commit message was "added permissions", the commit that set the executable bit, caught while the script is still running:
* [What each line of the script does](04-what-each-line-of-the-script-does.md) - A script that hides its failures makes a green run that's lying. Without set -e, a script carries on after errors, and only the last command's exit code decides whether the step passes. Always start with set -euo...
* [Three ways to run a script](05-three-ways-to-run-a-script.md) - Scripts can take arguments and read environment variables, just like on your laptop:
* [Something went wrong?](06-something-went-wrong.md) - Look at the bottom-right of your editor. If it says CRLF, a .sh file will break on a Linux runner. Click it and switch to LF. This repository's .gitattributes forces LF for every .sh file, so Git fixes it for you on...
* [Inline `run:` or a script file?](07-inline-run-or-a-script-file.md) - Inline `run:` or a script file?
* [Try it yourself](08-try-it-yourself.md) - This repository ships the script and a live workflow: scripts/ascii-script.sh and 04-shell-script.yml.
* [Checkpoint](09-checkpoint.md) - Most likely the actions/checkout step. The runner starts empty, so the script isn't there until the repository is checked out.
