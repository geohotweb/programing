#Este programa determina si un numero es el doble de un impar

def dobleDelInpar():
	n = int(input('Introduce un numero entero: '))
	if n/2 %4 ==3:
		print('Es el doble de un numero impar')
	else:
		print('No es doble de ningun impar')
dobleDelInpar()
