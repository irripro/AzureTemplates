# How to deploy the Template

There are 3 templates in this directory.
1. The first [template](https://github.com/alihhussain/AzureTemplates/blob/master/osp-engagement/UGH/Networking/v2networkingAzureDeploy.json) will deploy the Networking resources
2. The second [template](https://github.com/alihhussain/AzureTemplates/blob/master/osp-engagement/UGH/VMs/v2vmsazuredeploy.json) will deploy the following:
    * Application Gateway 
        * Public IP
        * No https and SSL Configuration
    * Application VMs
        * Network Interfaces
        * All the VMs are associated to an Availability Set
3. The third [template](https://github.com/alihhussain/AzureTemplates/blob/master/osp-engagement/UGH/v2azuredeploytogether.json) is a template which via nested deployments deploys the 1st and 2nd template
    * To deploy the templates run the following commands in a bash prompt (CloudShell will also work):
        1. Download the Master Template
            ```bash
            wget https://raw.githubusercontent.com/alihhussain/AzureTemplates/master/osp-engagement/UGH/v2azuredeploytogether.json
            ```
        2. Specify ResourceGroup Name and Location through environment variables  
            ```bash
            export rgName="<YourName>"
            export rgLocation="<YourLocation>"
            ```
            As an example
            ```bash
            export rgName="ugh"
            export rgLocation="eastus"
            ```
        3. Create a resource Group
            ```bash
            az group create -l $rgLocation -n $rgName
            ```
        4. Create a deployment to deploy the nested template
            ```bash
            az group deployment create --name MasterDeployment --resource-group $rgName --template-file ./v2azuredeploytogether.json --no-wait
            ```
        5. To Delete the resource group
            ```bash
            az group delete -n $rgName -y --no-wait
            ```

