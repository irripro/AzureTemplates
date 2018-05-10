# Managed Service Identity (MSI Azure) - User Assigned Identity

## Create a Resource Group
```bash
export rg="testingMSI"
export location="eastus"
az group create -l $location -n $rg
```
## Create a new User Assigned Identity

```bash
export nameMSI="ocpMSI"
export rg="testingMSI"
az identity create -g $rg -n $nameMSI
```
Sample Output
<a name="principalid"></a>
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

When a User assigned Identity is created, a ***service principal*** is also created in the background within the Azure Active directory and the following information is of note:
* ```clientId``` 
* ```name```
* ```tenantId``` 
* **```principalId```** - Note this value is not created when you simply create a Service Principal


Also note there is no ```secret``` value present when creating a User assigned identity, while it is present when creating a service principal.
<br><br><br>

To view the details of the ***Service Principal*** (*Created in the background when user assigned identity was created*):
```bash
export servicePrincipalID="94eee889-12d1-47b2-870c-f5cd4ff3e1e8"
az ad sp show --id $servicePrincipalID -o table

#  Output
AppId                                 DisplayName    ObjectId                              ObjectType
------------------------------------  -------------  ------------------------------------  ----------------
94eee889-12d1-47b2-870c-f5cd4ff3e1e8  ocpMSI         70682c4c-c8f5-4759-9b93-6315fef6c6f9  ServicePrincipal

```
By default the ***Service principal*** does **not** have any roles assigned to it. <br> You can view the roles assigned to the service principal:
<a name="findrole"></a>
```bash
export servicePrincipalID="94eee889-12d1-47b2-870c-f5cd4ff3e1e8"
az role assignment list --assign $servicePrincipalID
[]
```

***By Default the User assigned identity created does not have any permissions because there is no role associated to the Service Principal that had been created.***
<br><br>
To prove this lets go ahead and create a **VM** along with a **Storage Account** and try to access the storage account from within the VM.
<br><br>

#### Lets Create a VM and give it the User assigned identity (Managed Service Identity) that was just created.
```bash
export rg="testingMSI"
export vmName="vmWithMSI"
export image="UbuntuLTS"
export userName="azureuser"
export msiID="/subscriptions/e729c299-db43-40ce-991a-7e4572a69d50/resourcegroups/testingMSI/providers/Microsoft.ManagedIdentity/userAssignedIdentities/ocpMSI"
export uniqDNS="ocptestingMSI"
az vm create --resource-group $rg \
    --name $vmName --image $image \
    --admin-username $userName --admin-password "Great.Password" \
    --assign-identity $msiID
```

#### Lets Create a Storage Account
<a name="storage"></a>
```bash
export storageName="ocptesting123"
export rg="testingMSI"

# Validate the Name is not in use
az storage account check-name --name $storageName
#Output
{
  "message": null,
  "nameAvailable": true,
  "reason": null
}

# Create the storage account
az storage account create --name $storageName --resource-group $rg \
    --kind StorageV2
```

The ***value*** of note from the output is:

**Storage Account ID**: ```/subscriptions/e729c299-db43-40ce-991a-7e4572a69d50/resourceGroups/testingMSI/providers/Microsoft.Storage/storageAccounts/ocptesting123```

#### Log Into the VM
```bash
export vmPIP="<Your VM Public IP Address>"
ssh azureuser@$vmPIP
```

#### Get an access token using the VM's identity (From within the VM)
As a prerequisite step install jq on the machine
```bash
sudo apt install jq -y
```

Obtain the token
```bash
token=$(curl 'http://169.254.169.254/metadata/identity/oauth2/token?api-version=2018-02-01&resource=https%3A%2F%2Fmanagement.azure.com%2F' -H Metadata:true | jq .access_token | awk -F '"' '{print $2}')

# Display the token
echo $token
```

#### Use the token to access the Storage Account Key
```bash
export storageAccountID="/subscriptions/e729c299-db43-40ce-991a-7e4572a69d50/resourceGroups/testingMSI/providers/Microsoft.Storage/storageAccounts/ocptesting123"
curl https://management.azure.com$storageAccountID/listKeys?api-version=2016-12-01 --request POST -d "" -H "Authorization: Bearer $token" | jq
# Output
{
  "error": {
    "code": "AuthorizationFailed",
    "message": "The client '70682c4c-c8f5-4759-9b93-6315fef6c6f9' with object id '70682c4c-c8f5-4759-9b93-6315fef6c6f9' does not have authorization to perform action 'Microsoft.Storage/storageAccounts/listKeys/action' over scope '/subscriptions/e729c299-db43-40ce-991a-7e4572a69d50/resourceGroups/testingMSI/providers/Microsoft.Storage/storageAccounts/ocptesting123'."
  }
}
```

**The output above validates the VM identity does not have any permissions to access the storage account.**

## Next lets decide on a role and assign it to the User MSI.


#### Create/Choose a role for assignment
```bash
az role definition list -o table
```
This will output all the buildin roles that are available to be assigned.
<br>
A custom role can always be [created](https://docs.microsoft.com/en-us/cli/azure/role/definition?view=azure-cli-latest#az-role-definition-create).
<br><br>
The one chosen for this example is of type ```owner```.

#### Assign a role to User assigned identity 
In the backtground your assigning the role to the Service Principal that was created when the user assigned identity was created.<br>
<br>**Required Values**:
* Retrive the value of principalID from the [output of User Assigned Identity creation command.](#principalid)
* Scope - The scope used in this example is that of the [storage account which was created earlier.](#storage) Storage ID will be used to define the scope.

```bash
export principalID="70682c4c-c8f5-4759-9b93-6315fef6c6f9"
export roleType="owner"
storageAccountID="/subscriptions/e729c299-db43-40ce-991a-7e4572a69d50/resourceGroups/testingMSI/providers/Microsoft.Storage/storageAccounts/ocptesting123"
az role assignment create --assignee-object-id $principalID --role $roleType \
    --scope $storageAccountID
```

To validate the role was assigned to the Service Principal, lets [re-run](#findrole) the following command.
```bash
export servicePrincipalID="70682c4c-c8f5-4759-9b93-6315fef6c6f9"
az role assignment list --all | grep -B 10 -A 5 $servicePrincipalID

#Output
{
    "id": "/subscriptions/e729c299-db43-40ce-991a-7e4572a69d50/resourceGroups/testingMSI/providers/Microsoft.Storage/storageAccounts/ocptesting123/providers/Microsoft.Authorization/roleAssignments/4633382d-788d-4c67-8c8e-dbd2c6a65e57",
    "name": "4633382d-788d-4c67-8c8e-dbd2c6a65e57",
    "properties": {
      "additionalProperties": {
        "createdBy": "d291c899-5297-4604-aa71-a6683b02397b",
        "createdOn": "2018-05-10T19:19:02.5469177Z",
        "updatedBy": "d291c899-5297-4604-aa71-a6683b02397b",
        "updatedOn": "2018-05-10T19:19:02.5469177Z"
      },
      "principalId": "70682c4c-c8f5-4759-9b93-6315fef6c6f9",
      "principalName": "94eee889-12d1-47b2-870c-f5cd4ff3e1e8",
      "roleDefinitionId": "/subscriptions/e729c299-db43-40ce-991a-7e4572a69d50/providers/Microsoft.Authorization/roleDefinitions/8e3af657-a8ff-443c-a75c-2fe8c4bcb635",
      "roleDefinitionName": "Owner",
      "scope": "/subscriptions/e729c299-db43-40ce-991a-7e4572a69d50/resourceGroups/testingMSI/providers/Microsoft.Storage/storageAccounts/ocptesting123"
    },
```

## Validate the User Assigned Identity has access to the storage account
#### Log Into the VM
```bash
export vmPIP="<Your VM Public IP Address>"
ssh azureuser@$vmPIP
```

#### Get an access token using the VM's user assigned identity (From within the VM)
Obtain the token
```bash
token=$(curl 'http://169.254.169.254/metadata/identity/oauth2/token?api-version=2018-02-01&resource=https%3A%2F%2Fmanagement.azure.com%2F' -H Metadata:true | jq .access_token | awk -F '"' '{print $2}')

# Display the token
echo $token
```

#### Use the token to access the Storage Account Key
```bash
export storageAccountID="/subscriptions/e729c299-db43-40ce-991a-7e4572a69d50/resourceGroups/testingMSI/providers/Microsoft.Storage/storageAccounts/ocptesting123"
curl https://management.azure.com$storageAccountID/listKeys?api-version=2016-12-01 --request POST -d "" -H "Authorization: Bearer $token" | jq
# Output
{
  "keys": [
    {
      "keyName": "key1",
      "value": "<Key Value 1>",
      "permissions": "FULL"
    },
    {
      "keyName": "key2",
      "value": "<Key Value 2>",
      "permissions": "FULL"
    }
  ]
}
```
This time the response returns the storage key values, which can be utilized to access the storage account.