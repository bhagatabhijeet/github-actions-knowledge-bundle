# The Core Components

* [Overview](README.md) - Workflow, job, step and runner seen inside one real workflow file - what each part is, how they nest, and how a small matrix turns one job into three machines.
* [Four components, one picture](01-four-components-one-picture.md) - Four components do the work. An event sets them off.
* [They nest like boxes](02-they-nest-like-boxes.md) - They nest like boxes
* [Workflow: the process](03-workflow-the-process.md) - A workflow is an automated process that carries out one or more jobs. It lives in a YAML file inside .github/workflows/.
* [Job: work for one machine](04-job-work-for-one-machine.md) - Inside a workflow you define one or more jobs. A job is a list of steps that all run on the same runner.
* [Step: one task](05-step-one-task.md) - Steps are the individual tasks inside a job. They run one after another, top to bottom, on the same machine, so each step can use what the previous one left behind.
* [Runner: the machine](06-runner-the-machine.md) - A runner is a virtual machine that executes a job. You never create it. You ask for one with runs-on, and GitHub provisions it when the job starts.
* [One job, three machines](07-one-job-three-machines.md) - Look again at the picture. The job doesn't name one operating system. It names a matrix of three:
* [Checkpoint](08-checkpoint.md) - One to one. Every job runs on exactly one runner, and all of that job's steps share it.
