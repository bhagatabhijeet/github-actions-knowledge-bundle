# The Hidden Costs of Running Your Own CI Server

* [Overview](README.md) - Six pains of traditional self-hosted CI/CD tools - server upkeep, snowflake agents, wrong-sized capacity, fragile plugins, integration glue and knowledge silos - and why a free licence is not a free tool.
* [How a traditional setup is built](01-how-a-traditional-setup-is-built.md) - The CI server decides what should run. The agents do the running. Plugins extend the server. Your code lives somewhere else and pokes the server with a webhook when something changes.
* [1️⃣ You own a server](02-1-you-own-a-server.md) - The CI server is an application like any other. It needs everything a production application needs:
* [2️⃣ Agents turn into snowflakes](03-2-agents-turn-into-snowflakes.md) - A build agent is usually a long-lived machine. Somebody installed Java on it in March, Node in June, and a newer Node in September "just for one project". This is task 4 on Abhijeet's list, several Node.js versions side...
* [3️⃣ Capacity is always the wrong size](04-3-capacity-is-always-the-wrong-size.md) - You have to decide how many agents to run in advance. Developers don't push code at an even pace.
* [4️⃣ Plugins: the superpower and the weak point](05-4-plugins-the-superpower-and-the-weak.md) - Traditional CI servers do very little on their own. Talking to Git is a plugin. Storing credentials is a plugin. Sending a Slack message is a plugin. Jenkins has well over a thousand of them, written by many different...
* [5️⃣ Glue between the tool and your code](06-5-glue-between-the-tool-and-your.md) - Your code is in one system and your CI server is in another. Connecting them is your job:
* [6️⃣ The knowledge lives in one head](07-6-the-knowledge-lives-in-one-head.md) - Over time the setup becomes a collection of decisions made through an admin screen: which plugins, which versions, which agents carry which label, which credentials go where.
* [The iceberg](08-the-iceberg.md) - Most of these tools are free to download. That is the part above the water.
* [To be fair](09-to-be-fair.md) - Plenty of organisations run traditional CI tools extremely well. They usually have something Abhijeet's brand-new team does not: a dedicated platform team whose whole job is the build system. With that investment you...
* [Checkpoint](10-checkpoint.md) - A long-lived build machine that has been changed by hand so many times that it is unique. Builds behave differently depending on which agent runs them, and nobody can recreate the machine reliably.
