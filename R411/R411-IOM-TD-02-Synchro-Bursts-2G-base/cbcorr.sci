// z=cbcorr(x,y),
// Correlation de x avec y par decalages
// ATTENTION, dans le résultat la première valeur correspond à un décalage de 0 !
// 
// Christophe Borelly 
// IUT GTR Béziers - Mars 2003
function z=cbcorr(x,y),
[mx,nx]=size(x);
[my,ny]=size(y);
if mx==1 & nx>=ny
	a=[x x];
	for i=1:nx,
		fin=i+ny-1;
		z(i)=a(i:fin)*y';
	end
end
plot2d3(z);
endfunction