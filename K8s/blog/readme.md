# Container Orchestrators: The [Who](#who), [What](#what), [Why](#why) and [How](#how) from an operation team's perspective

The container frenzy is in full swing across the IT universe and it has likely engulfed you and your organization as well. And why should it not, containers have fundamentally changed the way developers develop their applications, the way applications are deployed, and the way system administrators manage their environments. Containers offer a broadly accepted and open standard, enabling simple portability between platforms and between clouds. On top of all that, containers give control of the applications, their dependencies as well as the infrastructure that they run on back to developers instead of having the operations teams having to manage it all on behalf of the development teams. 

By abstracting the infrastructure binaries, containers put the onus of uptime back in the hands of the development teams. No longer is compiled code and the dictated configurations for said code, going to be handed over to operations teams to be run and maintain. Instead, development teams output a fully *vetted* Docker image which contains the application code, its dependencies as well as the required configurations. So life is good as an operations team, what could the problem be? But wait, how and who manages the containers in production? How do you scale a container for load? How do you deploy new containers in production as part of a CI/CD pipeline? How do you manage the infrastructure below Docker engine? 

**These are some of the questions that this blog is going to answer.**

## Who
Let's start with the **who**? That is an easy one. What you do not want is to have the development teams worry about the scaling of containers, OS uptime, OS patching as well as scaling the infrastructure on which Docker engine is running on. Let's have the development teams worry about outputting *vetted* Docker images and have the centralized operations team manage all the docker containers and the infrastructure they run on. The operations team chooses the container orchestrator that best facilitates the needs of the development teams and their applications as well as fine tune it to run on the platform on which it is deployed on.

## How
Let's move on to **how**. How do we manage containers in production? This is where container orchestrators come into the picture. The container orchestrators main job is to automate the provisioning of containerized infrastructure and provide load balancing for the services that containers are used to create. Deploying and managing orchestrators can be difficult due to the constant development around Docker as well as the orchestration application chosen. As such there are a number of Azure platform tools available that make life easier, but which one to choose and why? 

## What
That leads to the **what**. What are the orchestrators available? Which one to choose and why? There are three orchestrators that are generally referred to when it comes to container orchestration. They are Docker Swarm, Apache Mesos, and Kubernetes. All three are open-source projects and well supported either by the enterprises that created them and/or the open source community. But the one discussed here will be Kubernetes. The reason for that is Kubernetes is emerging as the front runner in the orchestration game and as such Microsoft Azure has three managed services around it.

That leads to the other **what**? That being: What are the Azure platform services available to facilitate the management of these orchestrators? The options are, Azure Container Service (aka ACS), Azure Container Service Engine (aka ACS-engine), Azure Kubernetes Service (aka AKS), and Azure Container Instance.

## Why
Let's get the to final question as to **why**? Why should you use Kubernetes.

Kubernetes (aka K8s) was first released in June of 2014, and is written in Go. The project originated from and was open-sourced by Google, and is based on their experience running containers at a massive scale. Microsoft Azure uses Kubernetes in its managed Azure Kubernetes Service (AKS). Google uses Kubernetes for its Container as a Service (CaaS) offering, called Google Container Engine (GKE). Both Docker and CoreOS (rkt aka rocket) are supported container engines within Kubernetes. Major features include built-in auto-scaling, load balancing, volume management, and secrets management. In addition, there is a web UI to help with managing and troubleshooting the cluster.

Kubernetes has the most momentum going and as such both community and adoption is strong. The application has been proven at some scale and is evolving constantly. It is the only orchestrator that has *cloud-provider* concept natively, which allows seamless integration into public clouds such as Microsoft Azure, Amazon Web Services and Google Cloud Platform. With cloud providers making investments in services such as AKS, ACS-Engine, ACI and GKE, it is the best bet to win the war of orchestrators.

**Lets expand on the Services available to manage Kubernetes on Azure.**
### Azure Kubernetes Service (aka AKS)
Recently released service in preview makes it easier to manage and operate Kubernetes environments, all without sacrificing portability. AKS features an Azure-hosted control plane, automated upgrades, self-healing, easy scaling, and a simple user experience for both developers and cluster operators. With AKS, customers get the benefit of open source Kubernetes without complexity and operational overhead. AKS is free and you only pay for the consumption resulting from agent nodes and the infrastructure associated with them.

### Azure Container Service Engine (aka ACS-Engine)
Currently there is a service called Azure Container Service (ACS) which will be deprecated in favor of a managed Kubernetes service described above (AKS). However, there is still an open-source project called ACS-Engine which can be used to deploy unmanaged clusters on the Azure platform. The Azure Container Service Engine (acs-engine) generates ARM (Azure Resource Manager) templates for Docker enabled clusters on Microsoft Azure with your choice of DCOS, Kubernetes, or Swarm orchestrators. The input to acs-engine is a cluster definition file which describes the desired cluster, including orchestrator, features, and agents. 

### Azure Container Instance - Kubernetes Connector (Preview)
An Azure Container Instance is a single container that starts in seconds and is billed by the second. ACI offer highly versatile sizing, allowing you to select the exact amount of memory separate from the exact count of vCPUs, so your application perfectly fits on the infrastructure. 

The Azure Container Instances Connector for Kubernetes allows Kubernetes clusters to deploy Azure Container Instances. This enables on-demand and nearly instantaneous container compute, orchestrated by Kubernetes, without having VM infrastructure to manage and while still leveraging the portable Kubernetes API. This will allow you to utilize both VMs and container instances simultaneously in the same Kubernetes cluster, giving you the best of both worlds.

### Deploying Cluster on Azure VMs manually (Hard-way)
The last option to deploy an orchestrator is to deploy generic Azure VMs and installing and configuring the appropriate orchestrator from scratch. This is the most cumbersome method of deployment and management but allows the most control over the deployed orchestrator. 

## Rule of thumb: Picking an Orchestrator

**Docker Swarm**: Use Swarm when not in production and/or deployment at scale not required.

**Kubernetes**: Cloud Native Apps requiring deployment at medium scale (tens/~~*maybe*~~ hundreds of nodes) in production.

**Apache Mesos (DC/OS)**: Most flexible, making it a viable option for any kind of application and proven at a massive scale (thousands of nodes) in production.

## Rule of thumb: Picking a deployment method

**AKS**: Use Swarm when not in production and/or deployment at scale not required.

**Kubernetes**: Cloud Native Apps requiring deployment at medium scale (tens/~~*maybe*~~ hundreds of nodes) in production.

**Apache Mesos (DC/OS)**: Most flexible, making it a viable option for any kind of application and proven at a massive scale (thousands of nodes) in production.
