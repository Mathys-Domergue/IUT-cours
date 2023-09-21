<link rel="stylesheet" href="style.css">

#### CAUBEL Aksel
#### PRUVOST Arnaud
#### DOMERGUE Mathys
## Groupe IOT-51

</br>

<h1 class='headerTemplate'><center>Compte Rendu Partie Commanditaire</center></h1>

</br>
</br>

# Poulailler Connecter : Mission Poulette !

<div style="background-color:white">
<center>
<img src=".\image\logo_iut_um.png"/>

<img src=".\image\commanditaire.PNG"/>
</center>
</div>

<br>
<br>
<br>

<h2 class="underline"> Objectif de la mission : </h2>

<pre>

    - Monitorer la température et l'humidité à l'intérieur du poulailler (bien-être animal).

    - Déterminer la présence des poules dans le poulailler. Il faudra notamment s'assurer de la présence des poules dans le poulailler lorsque celui-ci est fermé durant la nuit.

    - Déterminer la présence d'animaux aux alentours du poulailler durant la nuit. On suppose qu'un animal présent la nuit dans l'enclos est forcément un renard. En cas de présence avérée, le client pourra déclencher à distance un dispositif lumineux et sonore destiné à faire fuir le renard.

    - Accès aux données pour le personnel concerné

</pre>

<h2 class="underline"> Contrainte de la mission : </h2>


<pre>

    - 2 jours pour préparer l'infrastructure avant la pose.
  
    - Trouver des solutions de prototypage a partir de capteurs imposés.
  
    - Containte réseaux ( accès au port )

</pre>



<div style="page-break-after: always; visibility: hidden"> 
\pagebreak 
</div>

<div style="page-break-after: always; visibility: hidden"> 
\pagebreak 
</div>

# Capteur mise en place au CEFE


<p>Pour répondre au mieux au cahier est charge, une première évaluation à été faite afin de savoir quels sont les capteurs que nous aurions besoin.</p>
<p>Après réflection avec l'ensemble du groupe plusieurs idées ont émergé : </p>

<li>Nous avons besoin de capteur de mouvement, pour cela notre regard c'est porté sur le capteur communiquant avec SigFox avec les caractéristique suivant : </li>

<pre> 
Un champ de vision de 90° * 90°
    Pouvant repéré un mouvement jusqu'à 5m
Une donnée envoyé chaque 30min
Un battement de coeur par jour
</pre>

Un intérupteur LoRa MCF-LW13IO

Des capteurs Sigfox Sens'It 3 :
<pre>Pour la fonction de 
    Capteur de Température & Humidité
    
Possibilité futur pour vérifier si la porte est ouverte ou fermé avec sa fonction magnéto-mètre </pre>