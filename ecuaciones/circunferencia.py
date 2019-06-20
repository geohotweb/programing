
def circunferencia():
	#radio = 6cm
	radio = int(input('Introduzca el valor del radio: '))
	pi = 3.14
	area = (pi*radio**2)
	perimetro = 2*pi*radio
	print('El area es:',area,'cm')
	print('El perimetro es:',perimetro,'cm')
circunferencia()
