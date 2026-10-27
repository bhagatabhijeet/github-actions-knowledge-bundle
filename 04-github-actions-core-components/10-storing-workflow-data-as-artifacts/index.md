# Storing Workflow Data as Artifacts

* [Overview](README.md) - Keep files after the runner is gone - what artifacts are, every upload-artifact input worth knowing, unique names and immutability, downloading by pattern, from the browser, the CLI or another run, retention and storage, and when to use cache, releases or packages instead.
* [What an artifact is](01-what-an-artifact-is.md) - An artifact is a set of files a job uploads to storage attached to its workflow run. It outlives the runner, and it can be downloaded by later jobs, by people, by the CLI, or by other workflows.
* [Uploading: the inputs worth knowing](02-uploading-the-inputs-worth-knowing.md) - It also returns outputs you can use in later steps:
* [Names are unique and artifacts are immutable](03-names-are-unique-and-artifacts-are-immutable.md) - Since upload-artifact@v4, an artifact can't be changed after upload, and two uploads with the same name in one run fail. This bites hardest in a matrix:
* [Four ways to get an artifact back](04-four-ways-to-get-an-artifact-back.md) - Downloading from another run:
* [Keep evidence when things break](05-keep-evidence-when-things-break.md) - The most valuable artifacts are often the ones you only need on a bad day:
* [Retention and storage](06-retention-and-storage.md) - Expired artifacts are deleted automatically. You can delete one early from the run's Summary page (🗑️ next to its name) or through the REST API, which frees the storage at once.
* [Security: assume anyone can read it](07-security-assume-anyone-can-read-it.md) - Never put secrets in an artifact. Everyone with read access can download it, which on a public repository means the whole internet. Watch out for .env files, kubeconfigs, cloud credential files and debug dumps that...
* [Artifact, cache, release or package?](08-artifact-cache-release-or-package.md) - Artifact, cache, release or package?
* [Try it yourself](09-try-it-yourself.md) - This repository ships a matrix-and-gallery workflow: 04-artifacts.yml.
* [Checkpoint](10-checkpoint.md) - The first upload succeeds and the others fail, because artifact names must be unique in a run. Include a matrix value in the name, such as results-${{ matrix.os }}.
