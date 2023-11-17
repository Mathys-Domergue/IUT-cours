# R3D17


## <center> TP1



## Environnement du TP


### 3.1 Installations nécessaires au TP


### 3.2 URLs p our réaliser une net instal


## 4 Création de machines virtuelles K-VMs


### 4.1 Création de VMs avec virt-manager

#### 4.1.1 Accès à virt-manager

1) 

![info-KVM](img/virshinfo.png)

2) 

![list-KVM](img/lsit-vm.png)

3) 
   
![all-list-KVM](img/list-all.png)

4) 

![shutdown-start-KVM](img/shutdown_start.png)

5) 

![autosart-enable-disable](img/autosart.png)

6) 
   
![kvm-info](img/kvminfo.png)

7) 

![graceful-shudow](img/gracefull-shutdown.png)

### 4.2 Création d'une KVM Debian avec virt-install

1) Voici la commande pour réaliser la VM

```Bash
virt-install  --osinfo detect=on,name=debian12 --vcpus 1 --ram 1024 --disk size=5 -l http://ftp.fr.debian.org/debian/dists/stable/main/installer-amd64/
```

2) 

![info-kvm](img/info-kvm.png)
![info-kvm](img/info-kvm-2.png)
![info-kvm](img/info-kvm-3.png)

3) 

![adding-2-vcpu](img/vcpu-kvm.png)

### 4.3 Création de VMs avec virt-builder

![crate-virtual-machine](img/virtbuilder.png)

![use-qcow2-disk](img/lancemnt-virtbuilder.png)


### 4.4 Création de VMs avec virt-customize

![debian-virtbuilder](img/virt-builder-debian.png)

![virt-customize](img/virtcustom.png)

## 5 Découverte de l'architecture KVM

### 5.1 Gestion de réseau

1) 

![list-bridge](img/list-brgde.png)

Le bridge utilisé par ma machine virtuelle est le bridge default.

2) Le bridge fonctionne comme un switch pour les VM de KVM.

![scema-reseau](schéma.drawio.png)


3) 

![add-bridge](img/create-bridge.png)

![add-bridge](img/bridge-conf.png)


4) 