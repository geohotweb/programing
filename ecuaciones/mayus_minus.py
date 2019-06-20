#Este programa determina si una letra que es introducida por el usuario es mayuscula o minuscula.

print('Programa que lee una letra y determina si es mayùscula o minuscula')

mayuscula = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
minuscula = 'abcdefghijklmnñopqrstuvwxyz'

letra = input('Introduzca una letra: ')

if letra in mayuscula:
	print('La letra introducida es mayùscula.')

else:
	if letra in minuscula:
		print('La letra es minùscula.')
	else:
		print('El caracter introducido no es una letra.')
