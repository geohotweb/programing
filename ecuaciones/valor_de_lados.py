def valor_de_lados():
	l1 = int(input('Ingrese el el valor del lado 1: '))
	l2 = int(input('Ingrese el valor del lado 2: '))
	suml1l2 = l1 + l2
	perimetro = float(l1+l2+l1+l2)
	area = float(l1*l2)
	print('El perimetro es:',perimetro)
	print('El area es:',area)
valor_de_lados()
