from math import sqrt

x = -1

while x < 0:
	
	x = float(input('Introduce un numero positivo: '))
print('La raiz cuadrada de {0} es {1:.1f}'.format(x, sqrt(x)))