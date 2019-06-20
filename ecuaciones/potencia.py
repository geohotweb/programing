#Este programa muestra todos los numero potencia de 2 entre 2 y 2 a la 30.

i = int(input('valor inicial: '))
potencia = int(input('limite: '))

while i < potencia:
	i *= 2
	print(i)