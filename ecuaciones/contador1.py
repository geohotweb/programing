#Programa que muestra todos los multiplos de n entre n y m*n, ambos inclusive.


n = int(input('Valor inicial: '))
m = int(input('Limite: '))
multip = int(input('Multiplo: '))
incremento = m*n

if n <= 0:
	incremento = multip
while n < m:
	n += incremento
	print(n)
