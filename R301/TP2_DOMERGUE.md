# <center> TP2
Mathys Domergue

</br>
</br>

## 2. Configuration du protocole OSPF sur le routeur R1

<pre>
R1(config)#router ospf 1
R1(config-router)#network 192.168.10.0 0.0.0.3 area 0
R1(config-router)#network 172.16.1.16 0.0.0.15 area 0
</pre>

## 3. Configuration OSPF sur le routeur R2 et R3


<pre>
R2(config)#router ospf 1
R2(config-router)#network 192.168.10.0 0.0.0.3 area 0
R2(config-router)#network 10.10.10.0 0.0.0.255 area 0

R3(config)#router ospf 1
R3(config-router)#network 192.168.10.0 0.0.0.3 area 0
R3(config-router)#network 172.16.1.32 0.0.0.7 area 0
</pre>


## 4. Configuration des ID des routeurs OSPF

<pre>
Avant reémarrage :

ID routeur 1 : 192.168.10.5
ID routeur 2 : 192.168.10.2
ID routeur 3 : 192.168.10.10

Après redémarrage :

ID routeur 1 : 10.1.1.1
ID routeur 2 : 10.2.2.2
ID routeur 3 : 10.3.3.3



Routeur R1

Router#sh ip ospf neighbor 


Neighbor ID     Pri   State           Dead Time   Address   Interface
10.2.2.2          0   FULL/  -        00:00:35    192.168.10.2 Serial0/3/1
10.3.3.3          0   FULL/  -        00:00:32    192.168.10.6 Serial0/3/0

Routeur R2

Router#sh ip ospf neighbor 


Neighbor ID     Pri   State           Dead Time   Address    Interface
10.3.3.3          0   FULL/  -        00:00:30    192.168.10.10Serial0/3/0
10.1.1.1          0   FULL/  -        00:00:37    192.168.10.1 Serial0/3/1


Routeur R3

Router#sh ip ospf neighbor 


Neighbor ID     Pri   State           Dead Time   Address   Interface
10.2.2.2          0   FULL/  -        00:00:34    192.168.10.9 Serial0/3/1
10.1.1.1          0   FULL/  -        00:00:30    192.168.10.5 Serial0/3/0


Pour le routeur R1, voici le résultat

Router#sh ip protocols

Routing Protocol is "ospf 1"
  Outgoing update filter list for all interfaces is not set 
  Incoming update filter list for all interfaces is not set 
  Router ID 10.3.3.3
  Number of areas in this router is 1. 1 normal 0 stub 0 nssa
  Maximum path: 4
  Routing for Networks:
    172.16.1.32 0.0.0.7 area 0
    192.168.10.4 0.0.0.3 area 0
    192.168.10.8 0.0.0.3 area 0
  Routing Information Sources:  
    Gateway         Distance      Last Update 
    10.1.1.1             110      00:00:45
    10.2.2.2             110      00:01:20
    10.3.3.3             110      00:00:45
  Distance: (default is 110)

</pre>



## 5. Configuration du coût OSPF

<pre>
Le cout est de 64 .


Le nouveau cout est de 1562 pour la liaison avec R2 et pour la liaison avec R3, le cout est de 390

Liaison R1/R2 :


1000000/64000 = 1562

Liaison R1/R3 :

1000000/256000 = 390
</pre>