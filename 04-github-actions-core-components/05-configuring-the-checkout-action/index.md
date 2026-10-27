# Configuring the Checkout Action

* [Overview](README.md) - Why a fresh runner has none of your code, how actions/checkout fixes it, and the inputs you'll actually use - fetch-depth, ref, path, repository, token, submodules, sparse-checkout and persist-credentials.
* [A workflow that looks right](01-a-workflow-that-looks-right.md) - Here is a first workflow many people write. It greets you, lists the files and prints the README:
* [Why it fails](02-why-it-fails.md) - The runner does not have your code. It's a brand-new virtual machine. Your workflow file was read by GitHub to plan the run, but the repository itself is never copied onto the runner unless a step does it. That step is...
* [The fix: one line](03-the-fix-one-line.md) - Now ls shows your files and cat prints the README.
* [Configuring it with `with:`](04-configuring-it-with-with.md) - Checkout takes inputs. These are the ones you'll actually use:
* [Try it yourself](05-try-it-yourself.md) - This repository ships the before-and-after as a live workflow: 04-checkout.yml.
* [Something went wrong?](06-something-went-wrong.md) - Something went wrong?
* [Checkpoint](07-checkpoint.md) - The workspace folder exists, it's just empty. Listing an empty folder is not an error. Only reading a file that isn't there fails.
