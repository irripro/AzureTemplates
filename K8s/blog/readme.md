# Container Orchestrators: The what, why, and how from an operation team's perspective


**Disclaimer:** *This blog post assumes the reader understands the fundamental value proposition that the Docker engine provides and the need to have orchestration around the containers deployed on top of it.*

The container frenzy is in full swing across the IT universe and it has likely engulfed you and your organization as well. And why should it not, it promises consistency, resiliency, and build-in elasticity within applications and the infrastructure they run on. On top of all that, containers give control of the applications, their dependencies as well as the infrastructure that they run on back to developers instead of having the operations teams having to manage it all on behalf of the development teams. 

By abstracting the infrastructure binaries, containers put the onus of uptime back in the hands of the development teams. No longer is compiled code and the dictated configurations for said code, going to be handed over to operations teams to be run and maintain. Instead, development teams output a fully *vetted* Docker image which contains the application code, its dependencies as well as the required configurations. So life is good as an operations team, what could the problem be? But wait, how and who manages the containers in production? How do you scale a container for load? How do you deploy new containers in production as part of a CI/CD pipeline? How do you manage the infrastructure below Docker engine? 

**These are some of the questions that this blog is going to answer.**

Let's start with the **who**? That is an easy one actually, what you dont want is to have the development teams worry about the scaling of containers, OS uptime, OS patching as well as scaling the infrastructure on which Docker engine is running on. Lets have the development teams worry about outputting *vetted* Docker images and have the centralized operations team manage all the docker containers and the infrastructure they run on. The operations team chooses the container orchestrator that best facilitates the needs of the development teams and their applications as well as fine tune it to run on the platform on which it is deployed on.

Let's move on to **how**. How do we manage containers in production? This is where container orchestrators come into the picture. The container orchestrators main job is to automate the provisioning of containerized infrastructure and provide load balancing for the services that containers are used to create. Deploying and managing orchestrators can be difficult due to the constant development around Docker as well as the orchestration application chosen. As such there are Azure platform tools available that make life easier, but which one to choose and why? 



