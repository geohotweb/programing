#Este programa determina si el caracter introducido es vocal mayuscula o vocal minuscula y si es consonante mayuscula o minuscula tambien dice si hay un caraccter desconocido.
#! usr/bin/python

letra_o_vocal = input('Introduce la primera vocal o consonante: ')
	
mayusculas1 = 'BCDFGHJKLMNPQRSTVWXYZ'
minusculas1 = 'bcdfghjklmnpqrstvwxyz'
vocal_mayus = 'AEIOU'
vocal_minus = 'aeiou'


if letra_o_vocal in vocal_minus:
	print('Es una vocal minuscula.')
if letra_o_vocal in vocal_mayus:
	print('Es una vocal mayuscula.')
if letra_o_vocal in minusculas1:
	print('Es una consonante minuscula.')
if letra_o_vocal in mayusculas1:
	print('Es una consonante mayuscula.')
