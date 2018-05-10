# Managed Service Identity (MSI Azure)

## Create a Resource Group
```bash
export rg="testingMSI"
export location="eastus"
az group create -l $location -n $rg
```
## Create a new User Identity

```bash
export nameMSI="ocpMSI"
export rg="testingMSI"
az identity create -g $rg -n $nameMSI
```
Sample Output
```json
{
  "clientId": "94eee889-12d1-47b2-870c-f5cd4ff3e1e8",
  "clientSecretUrl": <URL>,
  "id": "/subscriptions/e729c299-db43-40ce-991a-7e4572a69d50/resourcegroups/testingMSI/providers/Microsoft.ManagedIdentity/userAssignedIdentities/ocpMSI",
  "location": "eastus",
  "name": "ocpMSI",
  "principalId": "70682c4c-c8f5-4759-9b93-6315fef6c6f9",
  "resourceGroup": "testingMSI",
  "tags": {},
  "tenantId": "72f988bf-86f1-41af-91ab-2d7cd011db47",
  "type": "Microsoft.ManagedIdentity/userAssignedIdentities"
}
```

When a User Identity is created a ***service principal*** is created in the background within the Azure Active directory and the following information is of note:
* ```clientId``` 
* ```name```
* ```tenantId``` 
* **```principalId```** - Note this value is not created when you simply create a Service Principal


Also note there is no ```secret``` value present when creating a User MSI, while it is present when creating a service principal.
<br><br><br>

To view the details of the ***Service Principal***:
```bash
export servicePrincipalID="94eee889-12d1-47b2-870c-f5cd4ff3e1e8"
az ad sp show --id $servicePrincipalID -o table
```
Sample Output
```bash
AppId                                 DisplayName    ObjectId                              ObjectType
------------------------------------  -------------  ------------------------------------  ----------------
94eee889-12d1-47b2-870c-f5cd4ff3e1e8  ocpMSI         70682c4c-c8f5-4759-9b93-6315fef6c6f9  ServicePrincipal

```
By default the Service principal does not have any roles assigned to it. <br> You can view the roles assigned to the service principal
```bash
export servicePrincipalID="94eee889-12d1-47b2-870c-f5cd4ff3e1e8"
az role assignment list --assign $servicePrincipalID
```

