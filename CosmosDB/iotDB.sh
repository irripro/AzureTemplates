#!/bin/bash
#Define the Variables
dblocation="eastus"
dbresourcegroup="iotdbrg1"
dbname="iotdb"
dbkind="MongoDB"

#Craete the Resource Group
az group create -l $dblocation -n $dbresourcegroup

#Create the CosmosDB
az cosmosdb create -n $dbname -g $dbresourcegroup --kind $dbkind
az cosmosdb show -n $dbname -g $dbresourcegroup | jq .documentEndpoint | awk -F '"' '{print $2}' > iotdb_endpoint.txt
az cosmosdb list-keys -n $dbname -g $dbresourcegroup | jq .primaryMasterKey | awk -F '"' '{print $2}' > iotdbkey.txt

az cosmosdb collection create --collection-name mongodbcollection --db-name $dbname

az cosmosdb collection list --db-name $dbname --key $(cat iotdbkey.txt) -g $dbresourcegroup --url-connection $(cat iotdb_endpoint.txt) --name $dbname