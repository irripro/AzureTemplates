# CosmosDB
The very first thing we need to do is setup CosmosDB.
## Prerequisites
*   Azure Subscription
*   Azure CLI
## The following steps are going to be taken to create a MongoDB within a CosmosDB Account
* Authenticate in AzureCLI 2.0
* Create Resource Group
* Create CosmosDB Account
* Create CosmosDB Database
* Create CosmosDB Collection
* Put together the python connection string

### Authenticate in AzureCLI 2.0
Login to the Azure CLI 2.0 by running the following command:
```
az login
```
The output your going to get is going to look like:
```
To sign in, use a web browser to open the page https://aka.ms/devicelogin and enter the code <YourCodeHere> to authenticate.
```
Go to the [Login Page](https://aka.ms/devicelogin) and authenticate using the code specified in the output of Login command **YourCodeHere**

Once successfully logged in you will see the following output:
```
[
  {
    "cloudName": "AzureCloud",
    "id": "<YourSubscriptionID>",
    "isDefault": false,
    "name": "Visual Studio Enterprise",
    "state": "Enabled",
    "tenantId": "<YourTenantID>",
    "user": {
      "name": "<YourUserName>",
      "type": "user"
    }
  }
]
```
### Create Resource Group
Before you execute the command lets set some environment variables:
```
location="eastus"
resourcegroup="CosmosDB"
```
Now that the environment variables have been set lets execute the resource group creation command:
```
az group create -l $location -n $resourcegroup
```
Your output will look like:
```
{
  "id": "/subscriptions/e729c299-db43-40ce-****-******/resourceGroups/CosmosDB",
  "location": "eastus",
  "managedBy": null,
  "name": "CosmosDB",
  "properties": {
    "provisioningState": "Succeeded"
  },
  "tags": null
}

```
### Create CosmosDB Account
Before you execute the command lets set some environment variables:
```
resourcegroup="CosmosDB"
dbkind="MongoDB"
dbaccountname="mongodbcosmos$(shuf -i1-1000 -n1)"
```
Lets now create the CosmosDB account by executing the following command:
```
az cosmosdb create -n $dbaccountname -g $resourcegroup --kind $dbkind
```
Your output will look like:
```

```
