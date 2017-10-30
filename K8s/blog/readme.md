# Container Orchestrators: The [Who](#who), [What](#what), [Why](#why) and [How](#how) from an operation team's perspective


**Disclaimer:** *This blog post assumes the reader understands the fundamental value proposition that the Docker engine provides and the need to have orchestration around the containers deployed on top of it.*

The container frenzy is in full swing across the IT universe and it has likely engulfed you and your organization as well. And why should it not, containers have fundamentally changed the way developers develop their applications, the way applications are deployed, and the way system administrators manage their environments. Containers offer a broadly accepted and open standard, enabling simple portability between platforms and between clouds. On top of all that, containers give control of the applications, their dependencies as well as the infrastructure that they run on back to developers instead of having the operations teams having to manage it all on behalf of the development teams. 

By abstracting the infrastructure binaries, containers put the onus of uptime back in the hands of the development teams. No longer is compiled code and the dictated configurations for said code, going to be handed over to operations teams to be run and maintain. Instead, development teams output a fully *vetted* Docker image which contains the application code, its dependencies as well as the required configurations. So life is good as an operations team, what could the problem be? But wait, how and who manages the containers in production? How do you scale a container for load? How do you deploy new containers in production as part of a CI/CD pipeline? How do you manage the infrastructure below Docker engine? 

**These are some of the questions that this blog is going to answer.**

## Who
Let's start with the **who**? That is an easy one. What you do not want is to have the development teams worry about the scaling of containers, OS uptime, OS patching as well as scaling the infrastructure on which Docker engine is running on. Let's have the development teams worry about outputting *vetted* Docker images and have the centralized operations team manage all the docker containers and the infrastructure they run on. The operations team chooses the container orchestrator that best facilitates the needs of the development teams and their applications as well as fine tune it to run on the platform on which it is deployed on.

## How
Let's move on to **how**. How do we manage containers in production? This is where container orchestrators come into the picture. The container orchestrators main job is to automate the provisioning of containerized infrastructure and provide load balancing for the services that containers are used to create. Deploying and managing orchestrators can be difficult due to the constant development around Docker as well as the orchestration application chosen. As such there are a number of Azure platform tools available that make life easier, but which one to choose and why? 

## What
That leads to the **what**. What are the orchestrators available? Which one to choose and why? The orchestrators discussed will be Docker Swarm, Apache Mesos, and Kubernetes. All three are open-source projects and well supported either by the enterprises that created them and/or the open source community. The other **what** that will be discussed is: What are the Azure platform services available to facilitate the management of these orchestrators? The options are: Azure Container Service (aka ACS), Azure Container Service Engine (aka ACS-engine), Azure Kubernetes Service (aka AKS), and Azure Container Instance.

Let's first discuss the following orchestrators and which situation should each be utilized
*   [Docker Swarm](#docker-swarm)
*   [Apache Mesos](#apache-mesos)
*   [Kubernetes](#kubernetes)

### [Docker Swarm](https://docs.docker.com/engine/swarm/)
Docker Swarm is Docker’s native Container Orchestration Engine. Swarm is tightly integrated with the Docker API, making it well-suited for use with Docker. This can simplify managing container infrastructure, as there is no need to configure a separate orchestration engine, or relearn Docker concepts in order to use Swarm. Swarm does not support native auto-scaling or external load balancing. Scaling must be done manually or through third-party solutions. Swarm includes ingress load balancing, but external load balancing would be done through platform load balancer such as Azure Load Balancer or other third party tools. Also notable is a lack of a web interface for Swarm.

### [Kubernetes](https://kubernetes.io/docs/home/)

Kubernetes (aka K8s) was first released in June of 2014, and is written in Go. The project originated from and was open-sourced by Google, and is based on their experience running containers at a massive scale. Kubernetes has a large community behind it and has the most momentum behind it as it relates to adoption. Microsoft Azure uses Kubernetes in its managed Azure Kubernetes Service (AKS). Google uses Kubernetes for its Container as a Service (CaaS) offering, called Google Container Engine (GKE). Both Docker and CoreOS (rkt aka rocket) are supported container engines within Kubernetes. Major features include built-in auto-scaling, load balancing, volume management, and secrets management. In addition, there is a web UI to help with managing and troubleshooting the cluster. With these features included, Kubernetes often requires less third-party software than Swarm or Mesos.

###  [Apache Mesos aka Mesosphere DC/OS](http://mesos.apache.org/documentation/latest/)
Apache Mesos version 1.0 was released in July of 2016, but it has roots going all the way back to 2009. Mesos takes a distributed approach to managing resources and can have multiple masters to keep track of cluster state which allows it to achieve high-availability. In addition, Mesosphere DC/OS, a distributed datacenter operating system, is based on Apache Mesos. Mesos can scale to tens of thousands of nodes, and is used by the likes of Twitter, Airbnb, Yelp, and eBay. Notable features available in Mesos include support for multiple types of container engines, including Docker and its own “Containerizer,” as well as a web UI, and the ability to run on multiple OSes, including Linux, OS X, and even Windows.

## Why
Let's get the to final question as to **why**? Why should you use Docker Swarm, Kubernetes or Apache Mesos?

#### Docker Swarm
Docker swarm is the natural extension of Docker engine. It has the easier learning curve in terms of deployment and management for anyone who is already working and developing on Docker API. However, it lacks a few key features within it to have it be deployed in production. As such, Docker Swarm should be deployed in situations where the operational team is lacking or when developers are looking to get up and running to test out using an orchestrator engine. 

**Rule of thumb**: Use Swarm when not in production and/or deployment at scale not required.

#### Kubernetes
Kubernetes has the most momentum going and as such both community and adoption is strong. The application has been proven at some scale and is evolving constantly. It is the only orchestrator that has *cloud-provider* concept natively, which allows seamless integration into public clouds such as Microsoft Azure, Amazon Web Services and Google Cloud Platform. With services like AKS and GKE it is the best bet to win the war of orchestrators.

**Rule of thumb**: Cloud Native Apps requiring deployment at medium scale (tens/~~*maybe*~~ hundreds of nodes) in production.

#### Apache Mesos aka Mesosphere DC/OS
Is the most robust and is the proven kid on the block when it comes to orchestrators. Provides the most knobs and as such can be fine tuned to support any type of application at scale. This flexibility also makes it harder in terms of portability across platforms and a steeper learning curve for deployment and maintenance. 

**Rule of thumb**: Most flexible to deploy any kind of application and proven at a massive scale (thousands of nodes) in production.