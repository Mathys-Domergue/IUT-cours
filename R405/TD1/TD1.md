# <center> TD2 (Bash)

## 1 Que font ces oneliners ou ces scripts BASH ? écrivez ce que vous pensez voir en sortie de la commande ou du script bash


1) cela donne la d'aujourdhui

2) 55

3)  ```
    -rw-r----- 1 root adm 14K avril  3 16:37 /var/log/apport.log
    find: ‘/var/log/gdm3’: Permission denied
    -rw-r----- 1 syslog adm 12M avril  4 09:47 /var/log/kern.log
    -rw-r--r-- 1 root root 1,4K avril  4 07:57 /var/log/gpu-manager.log
    -rw-r--r-- 1 root root 106K févr. 20 20:22 /var/log/bootstrap.log
    -rw------- 1 root root 53K avril  4 07:57 /var/log/boot.log
    -rw-r--r-- 1 root root 3,4K avril  4 07:57 /var/log/vbox-setup.log
    -rw-r--r-- 1 root root 0 avril  2 21:14 /var/log/unattended-upgrades/unattended-upgrades-shutdown.log
    -rw-r--r-- 1 root root 40K avril  3 13:27 /var/log/alternatives.log
    -rw-r----- 1 syslog adm 63K avril  4 09:46 /var/log/auth.log
    -rw-r--r-- 1 root root 143K avril  3 13:38 /var/log/apt/history.log
    -rw-r----- 1 root adm 225K avril  3 13:38 /var/log/apt/term.log
    -rw-r--r-- 1 root root 1,4M avril  3 13:38 /var/log/dpkg.log
    find: ‘/var/log/speech-dispatcher’: Permission denied
    -rw-r----- 1 root adm 1,9K avril  2 22:56 /var/log/installer/casper.log
    find: ‘/var/log/private’: Permission denied
    -rw-r--r-- 1 root root 50K avril  4 07:58 /var/log/ubuntu-advantage.log
    -rw-r--r-- 1 root root 12K avril  2 21:30 /var/log/fontconfig.log
    ```


4) créer un alias temporairement

5) 111-aa+xx-222 111-aa+yy-222 111-aa+zz-222 111-bb+xx-222 111-bb+yy-222 111-bb+zz-222 111-cc+xx-222 111-cc+yy-222 111-cc+zz-222

6) "" tous les argumnts

7) cp filename filename.bak

8) kill le bash

9)  ```
    ping -c1 localhost && { echo succes;} || { echo pasglop; }
    PING localhost (127.0.0.1) 56(84) bytes of data.
    64 bytes from localhost (127.0.0.1): icmp_seq=1 ttl=64 time=0.030 ms

    --- localhost ping statistics ---
    1 packets transmitted, 1 received, 0% packet loss, time 0ms
    rtt min/avg/max/mdev = 0.030/0.030/0.030/0.000 ms
    succes

    ```

## 2 Explorons $* et $@ : quels résultats donnent les scripts suivants ?

1) ```
    lucky@lucky-the-one:~$ ./loopargs1.sh un deux trois quatre
    un
    deux
    trois
    quatre


    un
    deux
    trois
    quatre


    un deux trois quatre


    un
    deux
    trois
    quatre

    ```


## 3 Solutions pour lire un fichier.

1) a)  Cette commande permet de créer 2 dossiers et 2 fichiers puis de lister les éléments dans le répertoire actif.  
   IFS permet de rendre plus présentable la sortie du terminal.

    b) Le script permet de visualer le contenue du fichier au même titre que cat.
2) 