#!/bin/bash

# This shell script uses the Azure CLI 2.0 to move a single Managed Disk from one Azure subscription to 
# a storage account in a different, target subscription.
#
# Pre-reqs
# - VM should be stopped 
# - ??? should the User be logged in to the source or destination subscription or neither?
# - Need service principal for source subscription
# - Need service principal for target subscription
#
# Future features
# - Create VM in Target with VHD(s) attached
# - Convert VHDs in Target to Managed Disks
# - Move multiple Managed Disks at the same time
# - Get name of associated VM, check if stopped and stop if needed
#
# Set variables
#   The current version does not function interactively so presumes that all variables
#   needed to run are provided below.
#
targetRegionDestination="eastus"
targetRGName="incoming3"
targetSAName="incomingstorage3"
targetStorageSKU="Premium_LRS"
targetStorageContainer="vhds"
sourceSubServicePrincipal="http://sluper_test_sp"
sourceSubServicePrincipalPassword="D3mop@ss"
sourceSubTenant="72f988bf-86f1-41af-91ab-2d7cd011db47"
targetSubServicePrincipal="e4a791b3-261a-4f7c-8d6a-1a9144df3ec5"
targetSubServicePrincipalPassword="D3mop@ss"
targetSubTenant="c469bdb8-f6e2-4c7c-a97f-0d32832f74cd"
sourceManagedDisk="movetocsp_OsDisk_1_69784cb264b8441d98fe7d17c0b6140b"
sourceRGName="MOVEME-RG"
#
read -p "Variables set. Press [Enter] key to continue..."
#
# Log in to target subscription using service principal
# az login --service-principal --username $sourceSubServicePrincipal  --password $sourceSubServicePrincipalPassword  --tenant $sourceSubTenant
# az login --service-principal --username e4a791b3-261a-4f7c-8d6a-1a9144df3ec5 --password D3mop@ss --tenant c469bdb8-f6e2-4c7c-a97f-0d32832f74cd
echo "targetsp=" $targetSubServicePrincipal
echo "targetpass=" $targetSubServicePrincipalPassword
echo "targettenant=" $targetSubTenant
read -p " Press [Enter] key to continue..."
az login --service-principal -u $targetSubServicePrincipal --password $targetSubServicePrincipalPassword --tenant $targetSubTenant
read -p "Logged in to Target. Press [Enter] key to continue..."
# Create resource group in target subscription
az group create -l $targetRegionDestination --name $targetRGName
read -p "Target RG created. Press [Enter] key to continue..."
#
# Create storage account in target subscription
az storage account create --name $targetSAName --resource-group $targetRGName --location $targetRegionDestination --sku  $targetStorageSKU
#
# Get & display target storage account key
# az storage  account keys list --account-name incomingstorage --resource-group incoming 
#
# Get target storage account key into variable
targetSaKey=$(az storage account keys list --account-name $targetSAName --resource-group $targetRGName | jq .[0].value)
echo "targetSaKey=" + $targetSaKey
#
# Create target storage container
az storage container create --name $targetStorageContainer --account-name $targetSAName --account-key $targetSaKey
#
# *** continue cleanup & testing here ***
#
# Create SAS URL (for source - if container)
# az storage container generate-sas --name vhds --account-name  --account-key 
#
# Create SAS URL (for source - if managed disk)
sasUrl=$(az disk grant-access --duration-in-seconds 3600 --name $sourceManagedDisk --resource-group $sourceRGName | jq .accessSas)
echo "sasUrl=" + $sasUrl
#
read -p "Press [Enter] key to continue..."
#
# Copy container from source to target
az storage blob copy start --destination-blob {name} --destination-container {container} --source-account-key {key} --source-account-name {name} --source-blob {blob} --source-container {container} --source-sas {sas}
#
# Convert to Managed Disk
