# Migration
Aspects to consider when moving to applications to public cloud.
Modern Approach as well as Traditional Approach
* [Traditional Migration (VMs Workloads)](#traditional-migration-approach)
* [Modern Migration (VM to Containers with DevOps)](#modern-migration-approach)
* [Tools](#tools)
* [Training](#training)

## Traditional Migration Approach
There are three stages involved in executing a migration of a multi-tiered application deployed on virtual machines in a privately hosted data centers.
![Traditional Approach](./src/traditional.jpg)
1. [Assessment](#assessment)
2. [Migration Planning](#migration-planning)
3. [Executing the Migration](#execution)

### Assessment
*   Inventory Analysis
    *   What is deployed? How many **VMs**(CPU)/**disk**(IO)/**network**(latency)/etc?
*   Requirement Definition
    *   Define business requirements 

### Migration Planning
*   Cloud-fit Analysis
    *   Qualifying workloads to seek compatibility issues such as:
        *   OS support
        *   IO throughput
        *   Latency requirement
*   Dependency Mapping
    *   Identifying dependent workloads such as:
        *   Identity
        *   Monitoring
        *   Network connectivity
*   Application Mapping
    *   In a staged approach what and when should the application be moved.
*   Financial Modeling
    *   Initial stage cost
    *   Optimized for cloud cost

### Execution
*   Migration Automation - Automating execution of the migration as much as possible.
   
## Modern Migration Approach
![Migration Stages](./src/stages.jpg)

# Tools
Some first party Azure tools as well as 3rd party tools are listed below:
* First party tools: 
    * [**Azure Migration Tool**](https://azure.microsoft.com/en-us/migrate/virtual-machines-migration/)
    * [**Heptio - Ark**](https://github.com/heptio/ark)
    * [**Azure Site Recovery**](https://docs.microsoft.com/en-us/azure/site-recovery/site-recovery-overview)
    * [**Azure Backup**](https://docs.microsoft.com/en-us/azure/backup/backup-introduction-to-azure-backup)
    * [**StorSimple**](https://docs.microsoft.com/en-us/azure/storsimple/)
* 3rd party tools: 
    * [**Stratozone**](http://www.stratozone.com/migrate.aspx)
    * [**CloudEndure**](https://www.cloudendure.com/live-migration/)

# Training 
* [Linux Migration Hackfest organized by Azure GBB is a great place to start learning about migrations.](https://github.com/stuartatmicrosoft/Azure-Linux-Migration-Workshop)
* [For modern migration strategy training the container hackfest also organized by GBB is a good place to start.](https://github.com/chzbrgr71/container-hackfest)
