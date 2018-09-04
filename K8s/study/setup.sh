#!/bin/bash
# Ensure your session has already been logged in by utilizing az login command

#How to use the script
usage=''
usage+="The script should be utilized as follows:"
usage+="./setup.sh [action]"
usage+="Actions:"
usage+="create  -   Create the cluster"
usage+="delete  -   Delete the cluster"

# Setting Variables
myRG=myK8swithKubeadm
myLocation=eastus


#Check for usage
if [ $# -eq 0 ]
  then
    echo $usage
    exit
fi

deploy_cluster() {

    echo "You have selected to create the cluster."
}

delete_cluster() {
    echo "You have selected to delete the cluster."
}

# Decide action based on argument passed
action=$1
if [ $action = "create" ]
then
    deploy_cluster
elif [ $action = "delete" ]
then
    delete_cluster
fi