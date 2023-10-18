### Mathys DOMERGUE
### RT2

## <center> TP2


### 4 Vérification du bon fonctionnement du MTA Postfix via le CLI


2)Pour réalaiser la configuration de nos mails sous le format Maildir, il faut :

- configurer Postfix pour qu'il utilise le format Maildir :
   
   
    ```bash
    sudo postconf -e "home_mailbox = Maildir/"
    ```
- Restart Postfix :
    
    ```bash
    sudo /etc/init.d/postfix restart
    ```
- Vous pouvez visualiser les mails avec la commande suivante :

    ```bash
    su - root
    vim Maildir/new/fichier_mail
    ```

3) Pour envoyer des mails avec swaks, on utilise la syntax suivante:

    ```
    swaks --to root@localhost.localdomain --from test@localhost.localdomain
    ```

4) Nous ne pouvons envoyer de mail sur les adresses universitaires mais aussi sur les mails externes. Cela est du au fait sue notre serveur ne possède pas de connexion ssl sécurisé, il ne peut donc pas envoyer ces mails.

### 5 Configuration de Postfix comme relais avec authentification vers smtp.umontpellier.fr


2) Cette commande pernet d'obtenir notre fichier d'autetification hasher.

3) ```
    smtp_sasl_auth_enable = yes
    smtpd_use_tls = yes
    smtp_sasl_password_maps = hash :/etc/postfix/smtp_auth
    smtp_sasl_security_options = noanonymous
    smtp_tls_cert_file=/etc/ssl/certs/ssl-cert-snakeoil.pem
    smtp_tls_key_file=/etc/ssl/private/ssl-cert-snakeoil.key
    smtp_tls_security_level=may
    relayhost :smtp.umontpellier.fr:587
    ```

    Pour la génération de clé ssl privé et de certifaction, nous passons les commandes suivantes :


    ```
    openssl genrsa -out ssl-cert-snakeoil.pem
    openssl genrsa -out ssl-cert-snakeoil.key
    ```