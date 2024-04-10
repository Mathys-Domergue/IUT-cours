mkdir "repertoire avec espace"{1,2} &>/dev/null && touch "fichier "{1,2} \
& > /dev/null || echo -e "rep et fichiers presents"
for n in $(ls) ; do echo $n ; done
echo -e "-------------------"
echo -e "Avec IFS modifié"
IFS=$'\n'; for n in $(ls) ; do echo $n ; done
