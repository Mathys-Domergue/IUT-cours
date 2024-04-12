### DOMERGUE Mathys
### RT2 App

# <center> TP2 R401





## 1. Question primaires

Exercice 1


Pour que le client interne puisse avoir internet, on va utilisé la commande iptables

<img src = "con_int.png">

Exercice 2

Configuration Client OPENVPN

<img src = "conf_vpn.png">

Configuration Passerelle

<img src = "conf_pass1.png">

Configuration Client interne

<img src = "conf_int.png">


Configuration IPTABLES

<img src = "conf_pass.png">

## 2. Premiers tests

Exercice 4

<pre>
Sur la passerelle :

openvpn --dev tun0 --ifconfig 10.10.10.1 10.10.10.2

Sur le client Openvpn:

openvpn --remote 10.0.2.2 --dev tun0 --ifconfig 10.10.10.2 10.10.10.1
</pre>

Exercice 5

<img src ="ping_vm.png">

Exercice 6

Interface passerelle :

<img src ="inter_pass.png">

Interface Oenvpn :

<img src ="inter_vm.png">



On peut remarquer dans les deux cas que notre machine obtient une nouvelle interface pour la communication VPN


Exercice 7

<img src="ws_vm.png">
<img src="ws_pass.png">

## 3. Ajout d'une clé sécurisé

Exercice 9


<img src = "sta_key.png">

Exercice 10

La clée est une clée vpn.

Exercice 11

La longueur de la clée est de 2048 bits.