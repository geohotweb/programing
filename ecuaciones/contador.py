#Programa que muestra todos los multiplos de 6 entre 6 y 150, ambos inclusive.

i = int(input('Valor inicial: '))
limite = int(input('Limite: '))
incremento = int(input('incremento: '))

while i < limite:
	i += incremento
	print(i)
