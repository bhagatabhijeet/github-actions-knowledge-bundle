# Your First CI Pipeline

* [Overview](README.md) - Build a real three-stage pipeline - lint, test across a matrix, package an artifact - using the CI Basics workflow and sample app that ship in this repository.
* [The cast](01-the-cast.md) - The app is deliberately boring, so the pipeline can be the star:
* [The pipeline you're about to run](02-the-pipeline-you-re-about-to-run.md) - Three stages, five jobs, one artifact.
* [The workflow, piece by piece](03-the-workflow-piece-by-piece.md) - The cheapest check goes first. cache: pip saves downloaded packages between runs, keyed on the requirements file.
* [Exercise 1: Go green](04-exercise-1-go-green.md) - In your fork, open Actions → 02 - CI Basics
* [Exercise 2: Collect your artifact](05-exercise-2-collect-your-artifact.md) - Scroll to the bottom of the run's Summary page. Under Artifacts, click greeter to download it. Inside is a .tar.gz named after your commit.
* [Exercise 3: Plant a bug, watch CI catch it](06-exercise-3-plant-a-bug-watch-ci.md) - This is the moment CI earns its keep.
* [Exercise 4: Fail the lint gate](07-exercise-4-fail-the-lint-gate.md) - Add an unused import to the top of core.py and push:
* [Bonus: Make the tick mandatory](08-bonus-make-the-tick-mandatory.md) - Right now a red pull request can still be merged. To close that door:
* [Something went wrong?](09-something-went-wrong.md) - Something went wrong?
