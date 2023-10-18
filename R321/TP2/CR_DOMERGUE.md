### Matys DOMERGUE
### RT2

## <center> TP2

## 1 - Etude du passage d’un signal sinusoïdal à travers un filtre

1. Réaliser sous GNURadio, un filtre passe-bas « Low Pass » dont la fréquence de coupure est de 20 kHz et la plage de transition de 3 KHz. On choisira une fréquence d’échantillonnage globale de 1 MHz. Ne pas oublier le bloc « Throttle ».

    ![maquette_signal_1](tp2/../img/maquette_signal_1.png)
    

2. Appliquer à l’entrée de ce filtre un signal sinusoïdal de fréquence 1 KHz et observer la sortie du filtre. Quel est la forme du signal en sortie du filtre ? Mesurer son amplitude.

    ![signal_1](tp2/../img/signal_1.png)


    Comme nous pouvons le voir ci-dessus, le signal est un signal sinusoîdal d'amplitude 1.

3. Refaire la question précédente avec un signal sinusoïdal de fréquence 10 KHz, 18 KHz, 20 KHz et 25 KHz. Que constatez-vous ?

    Voici le signal à 10 kHz:
    ![signal_10k](tp2/../img/signal_10khz.png)

    Nous avos un amplitude de 1.

    Voici le signal à 18 kHz :

    ![signal_18k](tp2/../img/signal_18khz.png)

    L'amplitude est aussi de 1.

    Voici le signal à 20 kHz:

    ![signal_20k](tp2/../img/signal_20khz.png)

    L'amplitude est divisée de 2, elle est de 0.5.


    Voici le signal à 25 kHz :

    ![signal_25k](tp2/../img/signal_25khz.png)

    Nous avons plus d'amplitude car le signal n'est plus dans la plage de fréquence demandée.

    Nous pouvons contasté que le filtr passe-bas ne prends plus en compte les fréquences au-delà de 20 kHz.


4. Quelle est l’amplitude du signal de sortie à la fréquence de 20 KHz ? Est-elle conforme à vos attentes ? Expliquer.

    L'amplitude est de -0.5 à 0.5. Oui elle est conforme à mes attentes, car le signal commence à se déformer et l'amplitude diminue

5. Utiliser à présent un curseur « QT Gui Range » pour faire varier la fréquence du signal d’entrée de manière interactive.

    ![montage_range](tp2/../img/montage_range.png)


6. Comparer les résultats obtenus avec une plage de transition de 10 KHz, 1 KHz puis 100 Hz. Commentez.

Voici le signal avec une plange de transition de 10 kHz :

![signal-trans-10000](img/TP2/../signal_trans_10000.png)

On eput voir que notre signal n'est pas déformé et que l'amplitude est de -1 à 1.

Voici le signal avec une plage de transition de 1 kHz:

![signal-trans-10000](img/TP2/../signal_trans_1000.png)

Le signal reste le même que le précédent.


Voici le signal avec une plage de tansmition de 100 Hz :

![signal-trans-100](img/TP2/../signal_trans_100.png)

Le signal 

7. Tester le comportement d’autres filtres (passe-haut, passe-bande et réjecteur de bande (blocs High Pass, Band Pass et Band Reject).

Filtre Passe-haut :

![montage-hpf](img/tp2/../montage_hpf.png)
![signal-hpf](img/tp2/../signal_hpf.png)

Filtre Passe-bande :

![montage-bpf](img/tp2/../montage_bpf.png)
![signal-bpf](img/tp2/../signal_bpf.png)

Filtre Rejecteur de Bande:

![montage-bjf](img/tp2/../montage_bjf.png)
![signal-bjf](img/tp2/../signal_bjf.png)

8. Vous pouvez également tester des combinaisons de plusieurs filtres (par exemple deux filtres en série).

![montage-df](img/tp2/../montage_df.png)
![signal-df](img/tp2/../signal_df.png)

## 2 - Caractérisation d’un filtre à l’aide d’une source de bruit blanc

9. Réaliser un diagramme de flux sous GNU Radio contenant un bloc Noise Source (ne pas oublier le bloc habituel Throttle). Ce bloc permet de générer un bruit blanc. On choisira une fréquence d’échantillonnage globale de 1 Mhz. Afficher l’évolution temporelle ainsi que le spectre d’amplitude de ce bruit. Commentez. Pour le spectre d’amplitude, on utilisera un bloc « QT GUI Frequency Sink » pour lequel on choisira la propriété « Spectrum Width » à Half afin de ne voir que les fréquences positives.

Voici le montage pour réaliser un bruit blanc :

![montage-bruit-blanc](img/montage_bruit_blanc.png)

10.  Utiliser ce bruit pour caractériser un filtre passe-bas dont la fréquence de coupure est de 20 kHz et la plage de transition de 100 Hz. Pour cela afficher et relever le spectre d’amplitude de la sortie du filtre. Ce spectre donne une vue instantanée de la caractéristique fréquentielle du filtre.

![signal-bruit-blanc](img/frequence_bb.png)

11.  Refaire l’expérimentation avec une plage de transition de 1 kHz puis de 10 kHz (aidez-vous de blocs « QT Gui Range »). Que constatez-vous ?

![montage-bb-range](img/montage_bb_range.png)

![signal-bb-1khz](img/frequence_bb_1khz.png)

![signal-bb-10khz](img/frequence_bb_10khz.png)

Nous pouvons voir en comparant les deux signaux fréquencielles que laa fréquence de coupure est différante.

12.   Tester le comportement d’autres filtres (passe-haut, passe-bande et réjecteur de bande (blocs High Pass, Band Pass et Band Reject).

13.   Quel est, en pratique, l’inconvénient d’avoir des transitions abruptes (plages de transitions abruptes) ?

## 3 - Pour aller plus loin (et si le temps le permet) : réalisation d’un égaliseur musical « equalizer »

Un égaliseur musical (ou equalizer) permet de modifier un son ou un morceau musical en renforçant
ou en atténuant certaines plages de fréquences. L’usage d’un equalizer est très fréquent dans le
monde de la production musicale ou de l’écoute. Il permet par exemple d’ajouter des effets à une
musique ou à compenser la mauvaise reproduction d’un casque d’écoute. De nombreux lecteurs de
musiques intègrent aujourd’hui un equalizer.
Vous possédez, à présent, toutes les compétences pour réaliser un tel dispositif avec GNU Radio.
Dans cette dernière partie, il est demandé de réaliser un equalizer minimaliste constitué de trois
filtres :

- Un filtre passe bas pour renforcer ou atténuer les basses fréquences et dont la fréquence de coupure pourra être réglée à l’aide d’un curseur entre 0 Hz et 1 kHz.
- Un filtre passe bande pour agir sur les fréquences moyennes et dont la limite basse peut être réglée entre 0 Hz et 6 kHz et la limite haute entre 6,1 kHz et 15 kHz.
- Un filtre passe haut pour agir sur les hautes fréquences et dont la fréquence de coupure peut être réglée entre 10 kHz et 20 kHz.

    On choisira une fréquence d’échantillonnage globale de 44 kHz

14. Réaliser un diagramme de flux permettant de tester cet equalizer en utilisant comme signal d’origine, un bruit blanc.
15. Vérifier le fonctionnement des différents filtres et des différents curseurs de réglage.
16. Enfin, utiliser un véritable morceau musical pour tester le résultat en affichant son spectre d’amplitude ou un diagramme chute (QT GUI Waterfall Sink) qui représente l’évolution du spectre d’amplitude au cours du temps. Pour cela, on utilisera un bloc Wave File Source dans lequel on chargera le fichier drums_loop.wav fourni.
17. Si vous disposez d’un écouteur, écouter le résultat en modifiant les réglages en temps réel. On utilisera pour cela un bloc Audio Sink.

    > **Attention:**  
    > Régler le volume de son à un niveau bas avant d’exécuter votre diagramme de flux.

18.  Décrire les résultats obtenus