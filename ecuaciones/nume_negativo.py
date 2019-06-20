#Este programa determina si el numero introducido es negativo y de ser asi retornara un mensaje afirmandolo.

neg = float(input('Ingrese cualquier numero: '))

if neg < 0:
	print('El numero introducido es negativo')
elif neg == 0:
	print('El numero introducido es neutro')
else:
	print('El numero introducido es positivo')
