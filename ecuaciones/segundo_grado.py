#Este programa determina el resultado de una ecuacion de segundo grado.

from math import sqrt

print('Programa para la resolucion de la ecuacion a x*x + b x + c= 0.')

a = float(input('Valor de a: '))
b = float(input('Valor de b: '))
c = float(input('Valor de c: '))

if a != 0:
	x1 = (-b+sqrt(b**2-4*a*c)) / (2*a)
	x2 = (-b-sqrt(b**2-4*a*c)) / (2*a)
	print('Soluciones de las ecuaciones: x1={0:.3f} y x2={0:.3f}'.format(x1, x2))

else:
	if b != 0:
		x = -c/b
		print('Solucion: x={0:.3f}.'.format(x))

	else:
		if c != 0:
			print('La ecuacion no tiene solucion.')
		else:
			print('La ecuacion tiene infinitas Soluciones')
			
