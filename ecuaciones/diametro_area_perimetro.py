#Este programa determina cual es el area perimetro y diametro de un circulo a partir de su radio.

from math import pi

radio = float(input('Dame el radio de un circulo: '))

#Menú
print('Escoge una opcion.')
print('a) Calcular el diametro.')
print('b) Calcular el perímetro.')
print('c)Calcular el área.')
print('d)Seleccione esta opción.')
opción = input('Teclea a, b o c y pylsa el retorno de carro: ')

if opción == 'a' or opción =='A':
	diametro = 2*radio
	print('El diametro es {0}.'.format(diametro))
else:
	if opción == 'b' or opción == 'B':
		perímetro = 2*pi*radio
		print('El perímetro es {0}.'.format(perímetro))
	else:
		if opción == 'c' or opción == 'C':
			área = pi*radio**2
			print('El area es {0}.'.format(área))
		else:
			if opción == 'd' or 'D':
				print('Solo hay tres opciones para calcular y esta para rellenar el programa.')
				print('Tu has tecleado "{0}".'.format(opción))
