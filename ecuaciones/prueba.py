def calcular_perimetro_y_area():
	lado1 = int(input('Ingrese el valor del lado #1: '))
	lado2 = int(input('Ingrese el valor del lado #2: '))
	perimetro = int(lado1+lado2+lado1+lado2)
	area = lado1*lado2
	print('El valor del perimetro es de',perimetro,'metros')
	print('El valor del area es de',area,'metros cuadrados')
calcular_perimetro_y_area()
