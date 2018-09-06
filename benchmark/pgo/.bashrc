# .bashrc

# User specific aliases and functions

alias rm='rm -i'
alias cp='cp -i'
alias mv='mv -i'

#For PGO
export GOPATH=$HOME/odev
export GOBIN=$GOPATH/bin
export PATH=$PATH:$GOBIN
export CO_NAMESPACE=demo
export CO_CMD=kubectl
export COROOT=$GOPATH/src/github.com/crunchydata/postgres-operator
export CO_IMAGE_PREFIX=crunchydata
export CO_BASEOS=centos7
export CO_VERSION=3.2
export CO_IMAGE_TAG=centos7-$CO_VERSION
export PGO_CA_CERT=$COROOT/conf/apiserver/server.crt
export PGO_CLIENT_CERT=$COROOT/conf/apiserver/server.crt
export PGO_CLIENT_KEY=$COROOT/conf/apiserver/server.key
alias setip='export CO_APISERVER_URL=https://`kubectl get service postgres-operator -o=jsonpath="{.spec.clusterIP}"`:8443'

# Source global definitions
if [ -f /etc/bashrc ]; then
    . /etc/bashrc
fi
