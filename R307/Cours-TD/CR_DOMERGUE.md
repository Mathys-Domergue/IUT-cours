# R307 Etude du réseau d’accès optique en France

## DOMERGUE Mathys

### Partie 1 : Aspects structurels

1) <br />

    ![schéma-réseau-access](img/schéma_réseau_d_acces.png)


    L'autre nom du réseau d'accés est boule locale

2) Voici plusieurs exemples de technologies XDSL :  
    - ADSL (Asymmetric Digital Subscriber Line) transmission de donnés de manière asimétrique.
    - VDSL (Very high speed Digital Subscriber Line) Transmission de data à haut débit
    - SDSL (symmetric digital subscriber line)


3) Les différents acronymes de FTTxx :

   - FTTH qui signifie “fiber to the home” (Fibre non dédiée qui part de l'opérateur vers un point de mutualisation, en cas de problème l'opérateur n'a pas de nécéssité de remise en place de la fibre)

   - FTTLA qui signifie “fiber to the last amplifier”

   - FTTO qui signifie “fiber to the office” (Fibre dédiée qui part de l'opérateur, en cas de problème l'opérateur à une nécessité de remettre en place )
  
   - FTTB qui signifie “fiber to the building”
  
   - FTTN qui signifie “fiber to the node”
  
   - FTTDP qui signifie “fiber to the distribution point”


    > **Note**  
    > source : https://fibre.guide/deploiement/technologies

4) L’architecture P2P (point à point) est une architecture de déploiement de réseaux fibres, qui ne passe pas par le NRO ( nœud de raccordement optique) et qui va du FAI (fournisseur d'accès internet) jusqu’au particulier. L’avantage de cette architecture est qu’il permet d’avoir une allocation qui est dédiée au particulier.

    L'architecture P2MP part du FAI  jusqu'au PM pour ensuite déservire les clients.

    > **Note**  
    > source : https://fr.wikipedia.org/wiki/FTTH_P2P  
    >http://igm.univ-mlv.fr/~dr/XPOSE2007/ffraux_FTTH/solutions.html

5) BLOM : La boucle local optique mutualisée est le déploiement d’une seule fibre qui par la suite va ensuite pouvoir passer par des SRO (sous répartiteur optique) qui ensuite part chez des particuliers.

    BLOD : La boucle local optique dédiée est le déploiement de la fibre du NRO jusqu’au particulier, elle est aussi appelé FTTO
    > **Note**  
    > source : https://www.gersnumerique.fr/harmonisation-des-reseaux/architecture-et-terminologie-du-reseau.html
    >https://essonnenumerique.com/glossaire/blod-boucle-locale-optique-dediee/


6) GPON : Gygabit-capable Passive Optical Network, est un architecture qui multiplexe le trafic de plusieurs abonnés de manière dynamique. La norme du GPON est la norme G.984.x

    > **Note**  
    > source : https://fr.wikipedia.org/wiki/GPON


7) 
    NRO : noeud de raccordement optique, déploiement et 
    obtention du très haut débit
    
    SRO: sous-répartiteur optique, distribution de la fibre vers chez les particuliers
    
    PBO: point de raccordement optique, raccordement final entre un abonné au réseau fibre et son opérateur
    
    PTO: point de terminaison optique, transformation de signal optique en signal électrique

    PM: se trouve entre le NRO et le SRO, il permet de mutualiser sur une même ligne deux opérateurs différents

    OTL: transformation d’un signal électrique en signal optique, se situe côté opérateur

    ONU: conversion du signal optique en signal électrique, se situe dans PTO
![schéma-réseau-accés](img/schéma_réseau_d_acces%20(1).png)

    > **Note**  
    > source : https://www.gersnumerique.fr/harmonisation-des-reseaux/architecture-et-terminologie-du-reseau.html
    >https://essonnenumerique.com/glossaire/blod-boucle-locale-optique-dediee/

8) L'équipement qui permet de déservir plusieurs fibre est le coupleur.

9) Dans les ZTD les opérateur relient du NRO jusq'au PM qui se situe en bas de l'immeuble.  
    Dans les zones ZMD le déploiement des fibre est souvent à l'initiatives des collectivité

> **Note**  
> source : https://fibre.guide/deploiement/zmd  
> https://fibre.guide/deploiement/ztd


10) Nombre d'abonnés d’un RNO 24000 clients.
    La distance entre une NRO et SRO sur une ZMD, est choisie par les opérateurs.

>**Note**  
>source : http://www.lissieu.fr/IMG/pdf/architecture_deploiement_reseau_ftth_zmd.pdf

11) 
![sens-de-trans](img/schema_10.png)





## Partie II

1) Le débit dans le sens descendant est de 1 244,160 Mbit/s et de 2 488,320 Mbit/s  et le débit dans le sens montant est de 155,520 Mbit/s, de 622,080 Mbit/s, de 1 244,160 Mbit/s et de 2 488,320 Mbit/s.

>*Note*  
>source : https://moodle-but.iutbeziers.fr/moodle/pluginfile.php/19113/mod_resource/content/1/T-REC-G.984.2-201908-I%21%21PDF-E.pdf page 11



2) Exemple de transmission symétrique : la VOIP.
    Exemple  de transmission asymétrique : téléchargement.

>*Note*  
>source : https://www.lafibrelyonnaise.fr/debits-symetriques-vs-asymetriques

3) Les débits les plus fréquemment utilisés sont 1,2 Gbits/s et 2,4 Gbits/s


>*Note*  
>source : https://moodle-but.iutbeziers.fr/moodle/pluginfile.php/19112/mod_resource/content/1/T-REC-G.984.1-200803-I%21%21PDF-E.pdf page 13  
>https://moodle-but.iutbeziers.fr/moodle/pluginfile.php/19113/mod_resource/content/1/T-REC-G.984.2-201908-I%21%21PDF-E.pdf page 11  
>https://moodle-but.iutbeziers.fr/moodle/pluginfile.php/19114/mod_resource/content/1/T-REC-G.984.3-201401-I%21%21PDF-E-1.pdf page 42



4) Pour réaliser un transmission bidirectionnelle, on utilise un multiplexage par division de longueur d’onde sur une fibre ou transmission unidirectionnelle sur deux fibres.

>*Note*  
>source : https://moodle-but.iutbeziers.fr/moodle/pluginfile.php/19113/mod_resource/content/1/T-REC-G.984.2-201908-I%21%21PDF-E.pdf page 12

5) On utilise un code NRZ, sur le signal cela signifie que les 1 sont sur un haut niveau de lumière et les 0 sont sur un bas niveau de lumières.

>*Note*  
>source : https://moodle-but.iutbeziers.fr/moodle/pluginfile.php/19113/mod_resource/content/1/T-REC-G.984.2-201908-I%21%21PDF-E.pdf page 12

6) Pour une seule fibre, la plage d’ondes est de 1480 nm à 1500 nm, la valeur médiane est de 1490 nm.
    Pour deux fibres, la plage d’ondes est de 1260 nm à 1360 nm, la valeur médiane est de 1310nm.
>*Note*  
>source : https://moodle-but.iutbeziers.fr/moodle/pluginfile.php/19113/mod_resource/content/1/T-REC-G.984.2-201908-I%21%21PDF-E.pdf page 12

7) La plage d’ondes est de 1260 nm à 1360 nm.

>*Note*  
>source : https://moodle-but.iutbeziers.fr/moodle/pluginfile.php/19113/mod_resource/content/1/T-REC-G.984.2-201908-I%21%21PDF-E.pdf page 12

8) C’est la norme ITU-T G.652.

>*Note*  
>source : https://moodle-but.iutbeziers.fr/moodle/pluginfile.php/19113/mod_resource/content/1/T-REC-G.984.2-201908-I%21%21PDF-E.pdf page 16 


9) Les fibres utilisables dans ce cas sont les fibres SM (Singlemode)

>*Note*  
>source: Norme ITU-T G.652 page 1

10) Pour que l'on a un ORL minimum nous devons recevoir une puissance supérieur à 32 dB.

>*Note*  
>source: https://moodle-but.iutbeziers.fr/moodle/pluginfile.php/30665/mod_resource/content/1/T-REC-G.984.2-201908-I%21%21PDF-E.pdf page 16

11) La distance de couverture maximal est de 20 km.

>*Note*  
> source: https://moodle-but.iutbeziers.fr/moodle/pluginfile.php/30665/mod_resource/content/1/T-REC-G.984.2-201908-I%21%21PDF-E.pdf page 16


12) Voici les aténuation selon les classes:  
    Class A: 5-20  
    Class B: 10-25  
    Class C: 15-30  


>*Note*  
>source: https://moodle-but.iutbeziers.fr/moodle/pluginfile.php/30665/mod_resource/content/1/T-REC-G.984.2-201908-I%21%21PDF-E.pdf page 16

13) Pour les trois classes, le tableau nous indique le minimum moyen et maximum moyen de la puissance envoyé.