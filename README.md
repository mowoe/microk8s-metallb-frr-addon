# MetalLB (FRR) for microk8s

This addon provides the charts to deploy metallb featuring frr-mode in microk8s. The charts are largely identical to the ones from [microk8s core addons](https://github.com/canonical/microk8s-core-addons/tree/main) and have been adapted with the necessary additional containers and environment variable.

## Installation
First, add this repo as a source for addons on your cluster:
```bash
microk8s addons repo add mowoe-metallb-frr https://github.com/mowoe/microk8s-metallb-frr-addon
microk8s addons repo update mowoe-metallb
```
Then you can enable (-> install) the addon:
```bash
microk8s enable mowoe-metallb-frr/metallb-frr
```

### ⚠️ 
This addon is incompatible with the core metallb addon and *will* break deployments, if they are installed simultaneously. To be safe, be sure to disable all other metallb addons, before installing this one.