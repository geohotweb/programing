def tres_lados_triangulo():
	l1 = int(input('Ingrese el valor del lado 1: '))
	l2 = int(input('Ingrese el valor del lado 2: '))
	l3 = int(input('Ingrese el valor del lado 3: '))

	area = float(l1*l2 /2)
	perimetro = float(l1+l2+l3)
	print('El area es:',area)
	print('El perimetro es:',perimetro)
tres_lados_triangulo()
