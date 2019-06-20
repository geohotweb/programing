from math import pi

radio = float(input('Dame el radio de un circulo: '))

opción = ''
while opción != 'd':
	print('Escoge  una opción: ')
	print('a) Calcular el diámetro.')
	print('b) Calcular el perímetro.')
	print('c) Calcular el área. ')
	print('d) Finalizar.')
	opción = input('Teclea a, b, c o d y pulsa retorno de carro: ')
	if opción == 'a':
		radio = float(input('Dame el radio de un circulo: '))
		diámetro = 2*radio
		print('El diámetro es:',diámetro)
	elif opción == 'b':
		radio = float(input('Dame el radio de un circulo: '))
		perímetro = 2*pi*radio
		print('El perímetro es:',perímetro)
	elif opción == 'c':
		radio = float(input('Dame el radio de un circulo: '))
		área = pi*radio**2
		print('El área es:',área)
	elif opción == 'd':
		break
	elif opción != 'd':
		print('Solo hay cuatro opciones: a, b, c o d. Tu has tecleado',opción)
print('Gracias por usar este programa.')
