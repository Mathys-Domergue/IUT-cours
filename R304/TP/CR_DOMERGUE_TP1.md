# R304
### Mathys Domergue RT2

## <center>TP1 Découverte d'Open LDAP



## 1. Entraînement sur un annuaire de test

### 1.1 Installation de l'annuaire de test

### 1.2 Exploitation de l'annuaire de test

1) 
2) 
   Pour torouver le nombre d'entrées dans notre anuaire
   ``` sh
   ldapsearch -x -H ldap://localhost -b dc=gouv,dc=fr -s sub -D "cn=admin,dc=gouv,dc=fr" -w iutbrt "(objectclass=organizationalUnit)"

   ```
3) 
    ``` sh
    ldapsearch -x -H ldap://localhost -b dc=gouv,dc=fr -s sub -D "cn=admin,dc=gouv,dc=fr" -w iutbrt "(objectclass=*)"

    ```
4) L'option + dans le filtre objectclass permet de sortir toutes les attributs opérationnels.

5) L'option -x permet de réaliser un authentification simple pour s'authentifier.


6) 

7) Il y a 333 entré pour le savoir on tape cette commande :

    ``` sh
    ldapsearch -x -H ldap://localhost -b dc=gouv,dc=fr -s sub -D "cn=admin,dc=gouv,dc=fr" -w iutbrt "(ou=Reseaux)"
    ```
8) Il y a 671 entrée avec la commande :

    ``` sh
    ldapsearch -x -H ldap://localhost -b dc=gouv,dc=fr -s sub -D "cn=admin,dc=gouv,dc=fr" -w iutbrt "(|(ou=Reseaux)(ou=Administratif))"

    ```
9)  Il y a 583 en sortie avec la commande 
    
    ``` sh
    dapsearch -x -H ldap://localhost -b dc=gouv,dc=fr -s sub -D "cn=admin,dc=gouv,dc=fr" -w iutbrt "(&(&(objectclass=inertOrgPerson)(|(ou=Reseaux)(ou=Administratif)))(|(!(sn=s*))(!(sn=a*)))))"
    ```

10)  Il y a 5018 entrées avce la commande suivante:
    ``` sh
    ldapsearch -x -H ldap://localhost -b dc=gouv,dc=fr -s sub -D "cn=admin,dc=gouv,dc=fr" -w iutbrt "(entryDN=*)"
    ```
11) 
11) 
12) 