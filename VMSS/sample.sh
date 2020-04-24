
az group create --name VMSS2 --location westus2

az vmss create \
  --resource-group VMSS2 \
  --name myScaleSet2 \
  --image UbuntuLTS \
  --upgrade-policy-mode automatic \
  --admin-username azureuser \
  --generate-ssh-keys

token=$(az account get-access-token | jq -r .accessToken)


curl -X GET --header 'Accept: application/json' \
        --header "authorization: Bearer ${token}" \
        'https://management.azure.com/subscriptions/{SubscriptionID}/resourceGroups/{VMSS2}/providers/Microsoft.Compute/virtualMachineScaleSets/myScaleSet2/virtualMachines?api-version=2019-07-01&$expand=InstanceView' \ | 
        jq '.'
