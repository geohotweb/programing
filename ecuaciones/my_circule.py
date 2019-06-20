#Este programa calcula una serie de factores introduciendo vectores para poder dar el resultado.

from math import acos, pi, sqrt

opcion = ''

while opcion != '9':
	print('1) Introducir el primer vector.')
	print('2) Introducir el segundo vetor.')
	print('3) Calcular la suma.')
	print('4) Calcular la diferencia.')
	print('5) Calcular el producto escalar.')
	print('6) Calcular el producto vectorial.')
	print('7) Calcular el angulo (en grados) entre ellos.')
	print('8) Calcular longitud.')
	print('9) Finalizar.')
	opcion = input('Teclea un numero del 1 al 9 y pulsa retorno de carro: ')
	
	if opcion == '1':
		print('Pedimos el primer vector.')
		x1 = int(input('Dame el valor de x1: '))
		y1 = int(input('Dame el valor de y1: '))
		z1 = int(input('Dame el valor de z1: '))
	
	elif opcion == '2':
		print('Pedimos el segundo vector.')
		x2 = int(input('Dame el valor de x2: ')) 
		y2 = int(input('Dame el valor de y2: '))
		z2 = int(input('Dame el valor de z2: '))

	elif opcion == '3':
		print('1) seleccione esta opcion para obtener la suma de vectores.')
		opcion = input('Elija una opcion: ') 
		if opcion == '1':
			print('EL RESULTADO ES:',(x1+x2,y1+y2,z1+z2))
	
	elif opcion == '4':
		print('1) Primer vector menos segundo vector.')
		print('2) segundo vector menos Primer vector.')	
		opcion = input('Elija una opcion: ')
		if opcion == '1':
			print('EL RESULTADO ES:',(x1-x2,y1-y2,z1-z2))
		else:
			if opcion == '2':
				print('EL RESULTADO ES:',(x2-x1,y2-y1,z2-z1))

	elif opcion == '5':
		print('1) Seleccione esta opcion para calcular el producto escalar.')
		opcion = input('Elija una opcion: ')
		if opcion == '1':
			print('EL RESULTADO ES:',(x1*x2+y1*y2+z1*z2))

	elif opcion == '6':
		print('1) Seleccione esta opcion para calcular el producto vectorial.')
		opcion = input('Elija una opcion: ')
		if opcion == '1':
			print('EL RESULTADO ES:',(y1*z2-z1*y2,z1*x2-x1*z2,x1*y2-y1*x2))

	elif opcion == '7':
		print('1) Seleccione esta opcion para calcular el angulo.')
		opcion = input('Elija una opcion: ')
		if opcion == '1':
			numerador = (x1*x2+y1*y2+z1*z2)
			denominador = sqrt(x1**2+y1**2+z1**2) * sqrt(x2**2+y2**2+z2**2)
			angulo = 180/pi*acos(numerador/denominador)
			print('EL RESULTADO ES {0:.4f}'.format(angulo),'grados')
	
	elif opcion == '8':
		print('1) Calcular la longitud.')
		opcion = input('Elija una opcion: ')
		if opcion == '1':
			print('EL RESULTADO ES:',sqrt(x**2+y**2+z**2))

	elif opcion == '9':
		print('Gracias por usar este programa. Adiós!.')
		break