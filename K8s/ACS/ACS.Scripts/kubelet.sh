#!/bin/bash
set -e


# Azure does not support two LoadBalancers(LB) sharing the same nic and backend port.
# As a workaround, the Internal LB(ILB) listens for apiserver traffic on port 4443 and the External LB(ELB) on port 443
# This IPTable rule then redirects ILB traffic to port 443 in the prerouting chain
iptables -t nat -A PREROUTING -p tcp --dport 4443 -j REDIRECT --to-port 443


sed -i "s|<kubernetesAddonManagerSpec>|gcrio.azureedge.net/google_containers/kube-addon-manager-amd64:v6.4-beta.2|g" "/etc/kubernetes/manifests/kube-addon-manager.yaml"
sed -i "s|<kubernetesHyperkubeSpec>|gcrio.azureedge.net/google_containers/hyperkube-amd64:v1.6.6|g; s|<kubeServiceCidr>|10.0.0.0/16|g; s|<masterEtcdClientPort>|2379|g; s|<kubernetesAPIServerIP>|10.240.255.15|g" "/etc/kubernetes/manifests/kube-apiserver.yaml"
sed -i "s|<kubernetesHyperkubeSpec>|gcrio.azureedge.net/google_containers/hyperkube-amd64:v1.6.6|g; s|<masterFqdnPrefix>|myk8sclust-k8scluster-e729c2mgmt|g; s|<allocateNodeCidrs>|True|g; s|<kubeClusterCidr>|10.244.0.0/16|g; s|<kubernetesCtrlMgrNodeMonitorGracePeriod>|40s|g; s|<kubernetesCtrlMgrPodEvictionTimeout>|5m0s|g; s|<kubernetesCtrlMgrRouteReconciliationPeriod>|10s|g" "/etc/kubernetes/manifests/kube-controller-manager.yaml"
sed -i "s|<kubernetesHyperkubeSpec>|gcrio.azureedge.net/google_containers/hyperkube-amd64:v1.6.6|g" "/etc/kubernetes/manifests/kube-scheduler.yaml"
sed -i "s|<kubernetesHyperkubeSpec>|gcrio.azureedge.net/google_containers/hyperkube-amd64:v1.6.6|g; s|<kubeClusterCidr>|10.244.0.0/16|g" "/etc/kubernetes/addons/kube-proxy-daemonset.yaml"
sed -i "s|<kubernetesKubeDNSSpec>|gcrio.azureedge.net/google_containers/k8s-dns-kube-dns-amd64:1.14.4|g; s|<kubernetesDNSMasqSpec>|gcrio.azureedge.net/google_containers/k8s-dns-dnsmasq-amd64:1.13.0|g; s|<kubernetesExecHealthzSpec>|gcrio.azureedge.net/google_containers/exechealthz-amd64:1.2|g" "/etc/kubernetes/addons/kube-dns-deployment.yaml"
sed -i "s|<kubernetesHeapsterSpec>|gcrio.azureedge.net/google_containers/heapster:v1.3.0|g; s|<kubernetesAddonResizerSpec>|gcrio.azureedge.net/google_containers/addon-resizer:1.7|g" "/etc/kubernetes/addons/kube-heapster-deployment.yaml"
sed -i "s|<kubernetesDashboardSpec>|gcrio.azureedge.net/google_containers/kubernetes-dashboard-amd64:v1.6.1|g" "/etc/kubernetes/addons/kubernetes-dashboard-deployment.yaml"
sed -i "s|<kubernetesTillerSpec>|gcrio.azureedge.net/kubernetes-helm/tiller:v2.5.1|g" "/etc/kubernetes/addons/kube-tiller-deployment.yaml"
