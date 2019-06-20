#Este programa calcula la suma de los nummeros pares comprendidos entre  los que introduzca el usuario.
try:
	numero1 = int(input('Dame el primer numero: '))
	nummero2 = int(input('Dame el ssegundo numero: '))
	sum=0

	for i in range(numero1, nummero2):
		if i % 2==0:
			sum=sum+(i)
			i += sum+2
			print(i)

except:
	print('\nTienen que ser enteros los numeros.')
