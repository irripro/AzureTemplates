#!/bin/bash

az group create --name myResourceGroup --location eastus

az vm create \
  --resource-group myResourceGroup \
  --name centos74 \
  --image OpenLogic:CentOS:7-CI:latest \
  --custom-data myScript.sh \
  --ssh-key-value @id_rsa.pub