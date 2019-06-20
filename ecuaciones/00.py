#Este programa solicita un numero entre 0 y 10 ambos inclusive para leer un numero entre los valores pedidos
#y en caso de no ser asi vuelve a ejecutar el bucle hasta que se cumpla la condicion

x = int(input('Introduce un nummero positivo entre 0 y 10 ambos inclusive: '))

while x < 0 or x > 10:
	x = int(input('Introduce un nummero positivo entre 0 y 10 ambos inclusive: '))

print('El numero introducido es:',x)
