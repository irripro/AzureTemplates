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
  "clientSecretUrl": "https://control-eastus.identity.azure.net/subscriptions/e729c299-db43-40ce-991a-7e4572a69d50/resourcegroups/testingMSI/providers/Microsoft.ManagedIdentity/userAssignedIdentities/ocpMSI/credentials?tid=72f988bf-86f1-41af-91ab-2d7cd011db47&oid=70682c4c-c8f5-4759-9b93-6315fef6c6f9&aid=94eee889-12d1-47b2-870c-f5cd4ff3e1e8",
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