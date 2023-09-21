## Mathys DOMERGUE
## RT2 App

# <center> TP1 R411


## Uplink 

La taille du préambule est de 19 bit et elle ressemble à :

0b1010101010101010101

Voici les formats de trame Sigfox pour chaque classe de transmission :

    Classe A : Les trames de classe A ont une longueur maximale de 12 octets et sont composées de :
        Un champ Préambule de 2 octets
        Un champ Données de 1 à 12 octets (selon les besoins de l'application)
        Un champ Postambule de 4 octets

    Classe B : Les trames de classe B ont une longueur maximale de 46 octets et sont composées de :
        Un champ Préambule de 2 octets
        Un champ Données de 1 à 46 octets (selon les besoins de l'application)
        Un champ Postambule de 4 octets

    Classe C : Les trames de classe C ont une longueur maximale de 222 octets et sont composées de :
        Un champ Préambule de 2 octets
        Un champ Données de 1 à 222 octets (selon les besoins de l'application)
        Un champ Postambule de 4 octets

    Classe D : Les trames de classe D sont utilisées pour la géolocalisation et ont un format spécifique qui n'inclut pas de champ de données.

    Classe E : Les trames de classe E sont utilisées pour les tests de communication et ont un format spécifique qui n'inclut pas de champ de données.

## Downlink


La différence entre les trames du sens montant et les trames du sens déscendant est que pour les trames dans le sens déscendant la trame est toujours de 13 bits et à pour valeur : 

0b100100010011


Le FEC dans les trames downlink Sigfox est calculé de la manière suivante :

    Les données downlink sont divisées en paquets de 8 bits appelés symboles FEC.

    Pour chaque paquet de 8 bits, 3 bits de redondance FEC sont ajoutés, ce qui donne un symbole FEC de 11 bits.

    Les symboles FEC de 11 bits sont ensuite regroupés par groupes de 2, 4 ou 8 symboles (en fonction de la longueur de la trame) pour former des blocs FEC.

    Les blocs FEC sont ensuite transmis à travers le réseau Sigfox.

    Lorsque le périphérique reçoit les blocs FEC, il les décode en utilisant le code de Hamming pour détecter et corriger les erreurs de transmission.

    Les données downlink sont ensuite extraites des blocs FEC décodés et transmises au périphérique.



## Etude du signal




<img src=img/cpul0.png>


Voici si-dessus un changement de phase.


<img src =img/sul0.png>


### Démodulation et decodage du signal uplink0.wav
<img src=img/ul0.png>


On peut voir que les trois trames se ressemblent.




Pour vérifier si les MAC sont corrects on utilise l'option -k lors de la commande


<img src=img/mul0.png>





### Decodage de uplink1.wav


<img src=img/dul1.png>

On remarque que pour le deuxième signal, les changements sont le sequence numbre et le paylod.