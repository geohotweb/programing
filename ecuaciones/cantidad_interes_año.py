def cantidad_interes_años():
	c =float(input('Ingrese la cantidad: '))
	x = float(input('Ingrese el por cien: '))
	n = int(input('Ingrese la cantidad de años: '))

	tinteres = c*(1+x/100)**n
	print('El capital final es de:',tinteres,'Euros en un total de',n,'años')
cantidad_interes_años()

