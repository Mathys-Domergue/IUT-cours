# <center> AT et CRON


## <center> AT



1) a) at 03:10 AM ou at 03:10  
   b) at 03:10 PM ou at 15:10  
   c) at 05:25 21.01.48  
   d) at now + 20min  
   e) at now + 3 days  
   f) at -m now + 3 days  
   g) at 03:10 -f /home/user/script  
2) atq ou at -l  
3) atrm id ou at -r id  
4) Le dossier est /var/spool/cron/  
5) 



## <center> CRON


1) a) /var/spool/cron/crontabs
   b) heures : /etc/cron.hourly/
      jours : /etc/cron.daily/
      semaines : /etc/cron.weekly/
      mois : /etc/cron.monthly/
    c)utilisateur qui execute la commande
    d)ils sont lancés à l'heure et la date précisé dans l'execution de la commande
    e) run-parts execute les scripts se situant dans le dossier.

2) a) Pour visualiser l'éditeur par défault, on fait la commande :
      ```
      crontab -e
      ```

   b) Pour modifier l'éditeur par defaut, il faut :

      ```
      export EDITOR=vim
      ```
   c) Les fichier sont stockés dans le dossier suivants :

      ```
      /var/spool/cron/crontabs
      ```
   d) La synthaxe est 
      ```
      crontab [options] ***** <commande>
                     ou
      crontab [options] ***** <chemin/du/script>               
      ```

   e) 05 3 * * *
   f) */05 * * * *
   g) */05 8-17 * * *
   h) 1 13 1 * 1

> Notes  
> Site qui peut aider : https://crontab.guru/#