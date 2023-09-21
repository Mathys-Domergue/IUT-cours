// msg=getdata(data,deb),
// Recuperation des donnees transportées dans les blocs d'un burst GSM
// Format du burst : Tail(3) block(58) seq(26) block(58) Tail(3)
// Un block contient 7 octets (ascii) et se fini par 0 0
//
// deb est le debut de la sequence d'apprentissage dans le message complet
// 
// Christophe Borelly 
// IUT GTR Béziers - Mars 2003
funcprot(0);
function msg=getdata(data,deb),
blocks=[data(deb-58:deb-58+55) data(deb+26:deb+26+55)];
msg=[];
n=2^[7:-1:0];
for i=1:8:length(blocks),
	d=(blocks(i:i+7)); // Binaire
    codeASCII=d*n'; // Multiplication par les puissances de 2
	msg=[msg codeASCII];
end
msg=ascii(msg);
endfunction