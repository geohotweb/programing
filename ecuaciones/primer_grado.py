#Este programa determina el resultado de una ecuacion de primer grado.

kl = float(input('Introduce el valor de a: '))
lk = float(input('Introduce el valor de b: '))
if kl !=0:
	x = -lk / kl
	print('Solucion',x)
else kl == 0:
	print('La ecuacion no tiene Solucion')
